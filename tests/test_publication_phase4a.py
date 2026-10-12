from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

import pytest
import yaml
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "publication" / "scripts"
sys.path.insert(0, str(SCRIPTS))

import build_facsimile as facsimile  # noqa: E402
import check_sources as source_check  # noqa: E402
import prepare as preparation  # noqa: E402


def manuscript_metadata(data: bytes = b"authoritative") -> source_check.ManuscriptMetadata:
    return source_check.ManuscriptMetadata(
        file_id="file-id",
        name="manuscript.pdf",
        sha256=hashlib.sha256(data).hexdigest(),
        size_bytes=len(data),
        pages=18,
    )


def checked_sources(tmp_path: Path) -> source_check.CheckedSources:
    data = b"authoritative"
    pdf = tmp_path / "outside" / "manuscript.pdf"
    pdf.parent.mkdir()
    pdf.write_bytes(data)
    return source_check.CheckedSources(pdf, manuscript_metadata(data), (), 35)


def publication_root(tmp_path: Path, checked: source_check.CheckedSources) -> Path:
    root = tmp_path / "publication"
    meta = root / "meta"
    meta.mkdir(parents=True)
    assets = {
        "schema_version": 1,
        "assets": [
            {
                "asset_id": facsimile.FACSIMILE_ASSET_ID,
                "source": {
                    "provider": "google_drive",
                    "file_id": checked.manuscript.file_id,
                    "name": checked.manuscript.name,
                    "sha256": checked.manuscript.sha256,
                    "pages": [1, 18],
                },
                "transformation": {
                    "kind": "rasterize_complete_pages",
                    "dpi": 180,
                    "format": "png",
                    "preserve_materiality": True,
                },
                "page_count": 18,
                "destination_pattern": (
                    "generated/assets/facsimile/page-{page:02d}.png"
                ),
                "authority": "derivative",
                "versioned": False,
                "versioning_policy": "generated_ignored",
            }
        ],
    }
    (meta / "assets.yml").write_text(
        yaml.safe_dump(assets, sort_keys=False), encoding="utf-8"
    )
    return root


def fake_complete_page_renderer(commands: list[list[str]]):
    def run(command, *, check, shell):
        assert check is True
        assert shell is False
        assert "-singlefile" in command
        assert not ({"-x", "-y", "-W", "-H"} & set(command))
        first = int(command[command.index("-f") + 1])
        last = int(command[command.index("-l") + 1])
        assert first == last
        commands.append(command)
        Image.new("RGB", (100 + first, 160), "white").save(
            Path(command[-1]).with_suffix(".png")
        )

    return run


def output_hashes(paths: tuple[Path, ...]) -> dict[str, str]:
    return {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in paths
    }


def test_missing_manuscript_is_rejected_without_remote_fallback(tmp_path):
    repository = tmp_path / "repository"
    repository.mkdir()

    with pytest.raises(source_check.SourceCheckError) as error:
        source_check.resolve_manuscript_pdf(repository, {}, tmp_path / "home")

    assert "No se realizará ninguna descarga automática" in str(error.value)


def test_manuscript_inside_checkout_is_rejected(tmp_path):
    repository = tmp_path / "repository"
    pdf = repository / "manuscript.pdf"
    repository.mkdir()
    pdf.write_bytes(b"pdf")

    with pytest.raises(source_check.SourceCheckError, match="fuera del checkout Git"):
        source_check.resolve_manuscript_pdf(
            repository,
            {source_check.MANUSCRIPT_ENV: str(pdf)},
            tmp_path / "home",
        )


def test_wrong_manuscript_sha256_is_rejected(tmp_path, monkeypatch):
    pdf = tmp_path / "manuscript.pdf"
    pdf.write_bytes(b"wrong")
    metadata = source_check.ManuscriptMetadata(
        "file-id", "manuscript.pdf", "0" * 64, len(b"wrong"), 18
    )
    monkeypatch.setattr(source_check, "_pdf_pages", lambda path: 18)

    with pytest.raises(source_check.SourceCheckError, match="SHA-256 incorrecto"):
        source_check.verify_local_manuscript(pdf, metadata)


def test_wrong_manuscript_page_count_is_rejected(tmp_path, monkeypatch):
    data = b"authoritative"
    pdf = tmp_path / "manuscript.pdf"
    pdf.write_bytes(data)
    monkeypatch.setattr(source_check, "_pdf_pages", lambda path: 17)

    with pytest.raises(source_check.SourceCheckError, match="17; esperado 18"):
        source_check.verify_local_manuscript(pdf, manuscript_metadata(data))


def test_unit_sequence_requires_exactly_thirty_five_units(tmp_path):
    repository = tmp_path / "repository"
    control = repository / "project" / "00_CONTROL"
    control.mkdir(parents=True)
    canonical = yaml.safe_load(
        (ROOT / "project/00_CONTROL/unidades.yaml").read_text(encoding="utf-8")
    )
    canonical["units"][10]["order"] = 99
    (control / "unidades.yaml").write_text(
        yaml.safe_dump(canonical, sort_keys=False), encoding="utf-8"
    )

    with pytest.raises(source_check.SourceCheckError, match="orden canónico"):
        source_check._validate_units(repository, 18)


def test_missing_versioned_source_reports_its_logical_name_and_path(tmp_path):
    repository = tmp_path / "repository"
    repository.mkdir()
    source = source_check.Source(
        "critical_edition", "project/missing-edition.md", "3.6"
    )

    with pytest.raises(source_check.SourceCheckError) as error:
        source_check._validate_source_versions(repository, (source,))

    message = str(error.value)
    assert source.name in message
    assert source.path in message


def test_facsimile_generates_complete_ordered_unique_pages_and_provenance(
    tmp_path, monkeypatch
):
    checked = checked_sources(tmp_path)
    root = publication_root(tmp_path, checked)
    commands: list[list[str]] = []
    monkeypatch.setattr(
        facsimile.subprocess, "run", fake_complete_page_renderer(commands)
    )
    executable = tmp_path / "pdftoppm"
    project_marker = tmp_path / "project" / "canonical.txt"
    project_marker.parent.mkdir()
    project_marker.write_text("intacto", encoding="utf-8")

    outputs = facsimile.build_facsimile(root, checked, pdftoppm=executable)

    assert len(outputs) == 19
    assert len(commands) == 18
    assert [int(command[command.index("-f") + 1]) for command in commands] == list(
        range(1, 19)
    )
    images = outputs[1:]
    assert [path.name for path in images] == [
        f"page-{page:02d}.png" for page in range(1, 19)
    ]
    assert len({path.resolve() for path in images}) == 18
    qmd = outputs[0].read_text(encoding="utf-8")
    assert qmd.count("{#pagina-digital-") == 18
    assert re.findall(r"assets/facsimile/page-(\d{2})\.png", qmd) == [
        f"{page:02d}" for page in range(1, 19)
    ]
    assert checked.manuscript.file_id in qmd
    assert re.search(r"page-01\.png\)\{[^}]*width=\"62%\"", qmd)
    landscape_pages = re.findall(
        r"page-(?:0[2-9]|1[0-8])\.png\)\{[^}]*width=\"82%\"", qmd
    )
    assert len(landscape_pages) == 17
    assert "Transcripción paleográfica" not in qmd
    assert project_marker.read_text(encoding="utf-8") == "intacto"


def test_facsimile_is_idempotent_and_rebuilds_only_its_own_outputs(
    tmp_path, monkeypatch
):
    checked = checked_sources(tmp_path)
    root = publication_root(tmp_path, checked)
    commands: list[list[str]] = []
    monkeypatch.setattr(
        facsimile.subprocess, "run", fake_complete_page_renderer(commands)
    )
    executable = tmp_path / "pdftoppm"
    unrelated = root / "generated" / "15-transcripcion-prototipo.qmd"
    unrelated.parent.mkdir(parents=True)
    unrelated.write_text("regresión", encoding="utf-8")

    first = facsimile.build_facsimile(root, checked, pdftoppm=executable)
    first_hashes = output_hashes(first)
    stale = root / "generated" / "assets" / "facsimile" / "page-99.png"
    stale.write_bytes(b"stale")
    second = facsimile.build_facsimile(root, checked, pdftoppm=executable)

    assert output_hashes(second) == first_hashes
    assert not stale.exists()
    assert unrelated.read_text(encoding="utf-8") == "regresión"


def test_prepare_coordinates_source_check_prototype_and_facsimile(monkeypatch, tmp_path):
    checked = checked_sources(tmp_path)
    prototype_output = tmp_path / "prototype.qmd"
    facsimile_output = tmp_path / "facsimile.qmd"
    transcription_output = tmp_path / "transcription.qmd"
    modernized_output = tmp_path / "modernized.qmd"
    apparatus_output = tmp_path / "glossary.qmd"
    index_output = tmp_path / "index.qmd"
    f3_output = tmp_path / "f3.qmd"
    calls: list[str] = []

    monkeypatch.setattr(
        preparation,
        "build_f3_prototype",
        lambda repository, publication, result: calls.append("f3") or (f3_output,),
    )
    monkeypatch.setattr(
        preparation,
        "check_sources",
        lambda repository, publication: calls.append("check") or checked,
    )
    monkeypatch.setattr(
        preparation,
        "build_vertical_prototype",
        lambda repository, publication, pdf: calls.append("prototype")
        or (prototype_output,),
    )
    monkeypatch.setattr(
        preparation,
        "build_facsimile",
        lambda publication, result: calls.append("facsimile") or (facsimile_output,),
    )
    monkeypatch.setattr(
        preparation,
        "build_transcription",
        lambda repository, publication, result: calls.append("transcription")
        or (transcription_output,),
    )
    monkeypatch.setattr(
        preparation,
        "build_modernized",
        lambda repository, publication: calls.append("modernized")
        or (modernized_output,),
    )
    monkeypatch.setattr(
        preparation,
        "build_apparatus",
        lambda repository, publication, manuscript_name: calls.append("apparatus")
        or (apparatus_output,),
    )
    monkeypatch.setattr(
        preparation,
        "build_indexes",
        lambda repository, publication: calls.append("indexes") or (index_output,),
    )

    assert preparation.prepare() == (
        facsimile_output,
        transcription_output,
        f3_output,
        modernized_output,
        apparatus_output,
        index_output,
        prototype_output,
    )
    assert calls == [
        "check",
        "facsimile",
        "transcription",
        "f3",
        "modernized",
        "apparatus",
        "indexes",
        "prototype",
    ]


def test_phase4a_metadata_declares_unversioned_complete_page_series():
    data = yaml.safe_load(
        (ROOT / "publication/meta/assets.yml").read_text(encoding="utf-8")
    )
    series = next(
        asset
        for asset in data["assets"]
        if asset["asset_id"] == facsimile.FACSIMILE_ASSET_ID
    )

    assert series["source"]["pages"] == [1, 18]
    assert series["page_count"] == 18
    assert series["transformation"] == {
        "kind": "rasterize_complete_pages",
        "dpi": 180,
        "format": "png",
        "preserve_materiality": True,
    }
    assert series["destination_pattern"].endswith("page-{page:02d}.png")
    assert series["authority"] == "derivative"
    assert series["versioned"] is False
    assert series["versioning_policy"] == "generated_ignored"

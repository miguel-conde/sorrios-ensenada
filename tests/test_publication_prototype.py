from pathlib import Path
import sys

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "publication" / "scripts"
sys.path.insert(0, str(SCRIPTS))

import build_vertical_prototype as prototype  # noqa: E402
import prepare as preparation  # noqa: E402
import validate_publication as validator  # noqa: E402


EXPECTED_EVIDENCE = {
    "D": ("HID-001", "HID-003", "HID-005", "HID-006"),
    "C": ("HID-002", "HID-004", "CAL-012", "CAL-013"),
    "I": ("HID-007", "INT-005"),
    "E": ("HID-008",),
    "L": ("LIM-005", "LIM-010"),
}


def read_front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    _, metadata, _ = text.split("---", 2)
    return yaml.safe_load(metadata)


def test_vertical_sample_is_strictly_fixed():
    assert prototype.PROTOTYPE_PAGE == 12
    assert prototype.PROTOTYPE_UNIT == "folio_315v"
    assert prototype.PROTOTYPE_RESPONSE == 17
    assert prototype.EVIDENCE_GROUPS == EXPECTED_EVIDENCE


def test_all_prototype_evidence_exists_in_register_1_2():
    register = (
        ROOT
        / "project"
        / "30_RESULTADOS"
        / "ESTUDIO_HISTORICO"
        / "Registro_Afirmaciones_Calculos_v1.md"
    ).read_text(encoding="utf-8")
    rows = prototype.read_evidence_rows(register)
    assert set(rows) == {
        identifier for identifiers in EXPECTED_EVIDENCE.values() for identifier in identifiers
    }


def test_editorial_chapter_declares_required_metadata():
    metadata = read_front_matter(
        ROOT
        / "publication"
        / "content"
        / "02-estudio"
        / "09-rio-molinos-recursos.qmd"
    )
    assert metadata["chapter-id"] == "rio-molinos-recursos"
    assert metadata["publication-status"] == "prototype"
    assert metadata["sources"]
    assert {
        level: tuple(values) for level, values in metadata["evidence"].items()
    } == EXPECTED_EVIDENCE


def test_asset_manifest_has_only_page_12_and_folio_315v():
    manifest = yaml.safe_load(
        (ROOT / "publication" / "meta" / "assets.yml").read_text(encoding="utf-8")
    )
    assert [asset["asset_id"] for asset in manifest["assets"]] == [
        "manuscript-page-12",
        "folio-315v",
    ]
    assert all(asset["source"]["page"] == 12 for asset in manifest["assets"])
    assert all(
        asset["destination"].startswith("generated/assets/")
        for asset in manifest["assets"]
    )


def test_navigation_is_limited_to_the_vertical_prototype():
    quarto = (ROOT / "publication" / "_quarto.yml").read_text(encoding="utf-8")
    assert "content/02-estudio/09-rio-molinos-recursos.qmd" in quarto
    assert quarto.count("generated/") == 4


def test_paleographic_transcription_uses_one_semantic_line_block():
    edition = (
        ROOT / "project" / "20_TRABAJO_EDITORIAL" / "Edicion_Critica.md"
    ).read_text(encoding="utf-8")
    canonical = prototype.read_paleographic_lines(edition)
    generated = prototype._transcription_page(edition)

    assert len(canonical) == prototype.PALEOGRAPHIC_LINE_COUNT == 18
    assert validator._generated_paleographic_lines(generated) == canonical
    assert generated.count("\n| ") == 18


def test_paleographic_transcription_keeps_sections_and_documentary_hyphens():
    edition = (
        ROOT / "project" / "20_TRABAJO_EDITORIAL" / "Edicion_Critica.md"
    ).read_text(encoding="utf-8")
    generated = prototype._transcription_page(edition)
    headings = tuple(
        line.removeprefix("### ")
        for line in generated.splitlines()
        if line.startswith("### ")
    )
    lines = validator._generated_paleographic_lines(generated)

    assert headings == validator.UNIT_HEADINGS
    assert tuple(
        line.rsplit(maxsplit=1)[-1] for line in lines if line.endswith("-")
    ) == validator.DOCUMENTARY_HYPHEN_ENDINGS


def test_html_line_block_parser_rejects_collapsed_paragraph():
    canonical = ("primera línea", "segunda línea")
    semantic = validator._LineBlockParser()
    semantic.feed('<div class="line-block">primera línea<br>segunda línea</div>')
    collapsed = validator._LineBlockParser()
    collapsed.feed("<p>primera línea segunda línea</p>")

    assert semantic.blocks == [canonical]
    assert collapsed.blocks == []


def test_local_manuscript_environment_override_has_priority(tmp_path):
    repository = tmp_path / "repository"
    repository.mkdir()
    override = tmp_path / "override" / "manuscript.pdf"
    override.parent.mkdir()
    override.write_bytes(b"override")
    xdg_copy = tmp_path / "xdg" / "sorrios-ensenada" / "manuscript.pdf"
    xdg_copy.parent.mkdir(parents=True)
    xdg_copy.write_bytes(b"xdg")

    resolved = preparation._resolve_manuscript_pdf(
        repository,
        {
            preparation.MANUSCRIPT_ENV: str(override),
            "XDG_DATA_HOME": str(tmp_path / "xdg"),
        },
        tmp_path / "home",
    )

    assert resolved == override.resolve()


def test_local_manuscript_uses_xdg_data_home(tmp_path):
    repository = tmp_path / "repository"
    repository.mkdir()
    manuscript = tmp_path / "xdg" / "sorrios-ensenada" / "manuscript.pdf"
    manuscript.parent.mkdir(parents=True)
    manuscript.write_bytes(b"xdg")

    resolved = preparation._resolve_manuscript_pdf(
        repository,
        {"XDG_DATA_HOME": str(tmp_path / "xdg")},
        tmp_path / "home",
    )

    assert resolved == manuscript.resolve()


def test_local_manuscript_uses_home_fallback(tmp_path):
    repository = tmp_path / "repository"
    repository.mkdir()
    home = tmp_path / "home"
    manuscript = home / ".local" / "share" / "sorrios-ensenada" / "manuscript.pdf"
    manuscript.parent.mkdir(parents=True)
    manuscript.write_bytes(b"home")

    resolved = preparation._resolve_manuscript_pdf(repository, {}, home)

    assert resolved == manuscript.resolve()


def test_local_manuscript_missing_fails_without_remote_fallback(tmp_path):
    repository = tmp_path / "repository"
    repository.mkdir()
    home = tmp_path / "home"

    with pytest.raises(preparation.PreparationError) as error:
        preparation._resolve_manuscript_pdf(repository, {}, home)

    message = str(error.value)
    assert "No se realizará ninguna descarga automática" in message
    assert str(home / ".local" / "share" / "sorrios-ensenada" / "manuscript.pdf") in message


def test_local_manuscript_inside_checkout_is_rejected(tmp_path):
    repository = tmp_path / "repository"
    manuscript = repository / ".local" / "manuscript.pdf"
    manuscript.parent.mkdir(parents=True)
    manuscript.write_bytes(b"inside")

    with pytest.raises(preparation.PreparationError, match="fuera del checkout Git"):
        preparation._resolve_manuscript_pdf(
            repository,
            {preparation.MANUSCRIPT_ENV: str(manuscript)},
            tmp_path / "home",
        )

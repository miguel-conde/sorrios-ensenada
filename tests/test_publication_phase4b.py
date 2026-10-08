from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
import yaml
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "publication" / "scripts"
sys.path.insert(0, str(SCRIPTS))

import build_transcription as transcription  # noqa: E402
import check_sources as source_check  # noqa: E402
import critical_edition as critical  # noqa: E402
import fix_rendered_links as rendered_links  # noqa: E402
import validate_publication as validator  # noqa: E402


EDITION = ROOT / "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md"
UNITS = ROOT / "project/00_CONTROL/unidades.yaml"
MANUSCRIPT_NAME = "sorrios_ensenada_orden_lectura_calidad_original.pdf"


@pytest.fixture(scope="module")
def specs() -> tuple[critical.UnitSpec, ...]:
    return critical.load_unit_specs(UNITS)


@pytest.fixture(scope="module")
def canonical_units(specs) -> tuple[critical.CriticalUnit, ...]:
    return critical.parse_critical_edition(
        EDITION.read_text(encoding="utf-8"), specs, MANUSCRIPT_NAME
    )


def _edition_text() -> str:
    return EDITION.read_text(encoding="utf-8")


def _hashes(paths: tuple[Path, ...]) -> dict[str, str]:
    return {
        str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths
    }


def _checked(tmp_path: Path) -> source_check.CheckedSources:
    pdf = tmp_path / "outside" / "manuscript.pdf"
    pdf.parent.mkdir(parents=True)
    pdf.write_bytes(b"authoritative")
    metadata = source_check.ManuscriptMetadata(
        "file-id",
        MANUSCRIPT_NAME,
        hashlib.sha256(b"authoritative").hexdigest(),
        len(b"authoritative"),
        18,
    )
    return source_check.CheckedSources(pdf, metadata, (), 35)


def _isolated_tree(tmp_path: Path) -> tuple[Path, Path, source_check.CheckedSources]:
    checked = _checked(tmp_path)
    repository = tmp_path / "repository"
    publication = repository / "publication"
    (repository / "project/00_CONTROL").mkdir(parents=True)
    (repository / "project/20_TRABAJO_EDITORIAL").mkdir(parents=True)
    shutil.copy2(UNITS, repository / "project/00_CONTROL/unidades.yaml")
    shutil.copy2(EDITION, repository / "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md")
    (publication / "meta").mkdir(parents=True)
    asset = {
        "schema_version": 1,
        "assets": [
            {
                "asset_id": transcription.TRANSCRIPTION_ASSET_ID,
                "source": {
                    "file_id": checked.manuscript.file_id,
                    "name": checked.manuscript.name,
                    "sha256": checked.manuscript.sha256,
                    "pages": [1, 18],
                },
                "transformation": {
                    "kind": "crop_units_from_facsimile_pages",
                    "source_pattern": "generated/assets/facsimile/page-{page:02d}.png",
                    "crop_semantics": "render_unit.py",
                    "format": "png",
                },
                "unit_count": 35,
                "destination_pattern": "generated/assets/transcription/{unit_id}.png",
            }
        ],
    }
    (publication / "meta/assets.yml").write_text(
        yaml.safe_dump(asset, sort_keys=False), encoding="utf-8"
    )
    facsimile = publication / "generated/assets/facsimile"
    facsimile.mkdir(parents=True)
    for page in range(1, 19):
        Image.new("RGB", (100, 60), (page, 0, 255 - page)).save(
            facsimile / f"page-{page:02d}.png"
        )
    return repository, publication, checked


def test_source_has_exactly_35_units_in_orders_1_to_35(specs, canonical_units):
    assert len(specs) == len(canonical_units) == 35
    assert [spec.order for spec in specs] == list(range(1, 36))


def test_ids_labels_and_anchors_are_unique(specs):
    assert len({spec.unit_id for spec in specs}) == 35
    assert len({spec.label for spec in specs}) == 35
    assert len({spec.anchor for spec in specs}) == 35


def test_edition_corresponds_completely_and_in_order_to_manifest(specs, canonical_units):
    assert [unit.spec for unit in canonical_units] == list(specs)


def test_every_unit_has_exactly_six_ordered_sections(canonical_units):
    assert all(tuple(unit.sections) == critical.SECTION_NAMES for unit in canonical_units)


def test_missing_section_is_rejected(specs):
    mutated = _edition_text().replace("### Notas históricas\n", "", 1)
    with pytest.raises(critical.CriticalEditionError, match="seis secciones"):
        critical.parse_critical_edition(mutated, specs, MANUSCRIPT_NAME)


def test_duplicated_section_is_rejected(specs):
    mutated = _edition_text().replace(
        "### Notas históricas\n", "### Notas históricas\n\nDuplicada\n\n### Notas históricas\n", 1
    )
    with pytest.raises(critical.CriticalEditionError, match="seis secciones"):
        critical.parse_critical_edition(mutated, specs, MANUSCRIPT_NAME)


def test_missing_unit_is_rejected(specs):
    text = _edition_text()
    start = text.index("## Portada")
    end = text.index("## Reverso de la portada")
    with pytest.raises(critical.CriticalEditionError, match="34 bloques"):
        critical.parse_critical_edition(text[:start] + text[end:], specs, MANUSCRIPT_NAME)


def test_extra_unit_is_rejected(specs):
    text = _edition_text().replace(
        "# 4. Apéndices", "## Unidad extra\n\n### Imagen\n\nx\n\n# 4. Apéndices"
    )
    with pytest.raises(critical.CriticalEditionError, match="36 bloques"):
        critical.parse_critical_edition(text, specs, MANUSCRIPT_NAME)


def test_ambiguous_or_reordered_correspondence_is_rejected(specs):
    mutated = _edition_text().replace("## Reverso de la portada", "## Portada", 1)
    with pytest.raises(critical.CriticalEditionError, match="discordante"):
        critical.parse_critical_edition(mutated, specs, MANUSCRIPT_NAME)


@pytest.mark.parametrize(
    ("original", "replacement", "message"),
    [
        ("página 1 (página completa)", "página 2 (página completa)", "portada"),
        ("página 2 (izquierda)", "página 2 (derecha)", "reverso_portada"),
        ("página 2 (derecha)", "página 3 (derecha)", "folio_306r"),
    ],
)
def test_page_and_position_mismatches_are_actionable(
    specs, original, replacement, message
):
    mutated = _edition_text().replace(original, replacement, 1)
    with pytest.raises(critical.CriticalEditionError) as error:
        critical.parse_critical_edition(mutated, specs, MANUSCRIPT_NAME)
    assert message in str(error.value)


def test_generated_qmd_has_35_units_images_and_unique_anchors(canonical_units, tmp_path):
    checked = _checked(tmp_path)
    text = transcription.transcription_qmd(canonical_units, checked)
    generated = validator._generated_transcription_units(text)
    assert len(generated) == 35
    assert [anchor for _, anchor, _ in generated] == [
        critical.published_unit_anchor(unit.spec) for unit in canonical_units
    ]
    assert text.count("assets/transcription/") == 35


def test_all_five_text_sections_are_explicitly_equivalent(canonical_units):
    checked = source_check.CheckedSources(
        Path("/outside/manuscript.pdf"),
        source_check.ManuscriptMetadata("id", MANUSCRIPT_NAME, "0" * 64, 1, 18),
        (),
        35,
    )
    generated = validator._generated_transcription_units(
        transcription.transcription_qmd(canonical_units, checked)
    )
    for canonical, (_, _, sections) in zip(canonical_units, generated, strict=True):
        for name in critical.TEXT_SECTION_NAMES:
            actual = sections[name]
            if name == "Transcripción paleográfica":
                actual = validator._decode_line_block(actual)
            assert actual == canonical.sections[name], f"{canonical.spec.unit_id} / {name}"


def test_paleographic_lineation_including_croquis_blank_line_is_preserved(canonical_units):
    checked = source_check.CheckedSources(
        Path("/outside/manuscript.pdf"),
        source_check.ManuscriptMetadata("id", MANUSCRIPT_NAME, "0" * 64, 1, 18),
        (),
        35,
    )
    generated = validator._generated_transcription_units(
        transcription.transcription_qmd(canonical_units, checked)
    )
    for canonical, (_, _, sections) in zip(canonical_units, generated, strict=True):
        actual = validator._decode_line_block(sections["Transcripción paleográfica"])
        assert actual.splitlines() == canonical.sections["Transcripción paleográfica"].splitlines()
    assert "\n|\n" in transcription.transcription_qmd(canonical_units, checked)


def test_explicit_empty_canonical_notes_are_preserved(canonical_units):
    checked = source_check.CheckedSources(
        Path("/outside/manuscript.pdf"),
        source_check.ManuscriptMetadata("id", MANUSCRIPT_NAME, "0" * 64, 1, 18),
        (),
        35,
    )
    text = transcription.transcription_qmd(canonical_units, checked)
    expected = sum(
        unit.sections["Notas históricas"] == "*(Sin notas históricas.)*"
        for unit in canonical_units
    )
    assert text.count("*(Sin notas históricas.)*") == expected


def test_crop_semantics_complete_left_and_right_match_render_unit(tmp_path):
    page = tmp_path / "page.png"
    image = Image.new("RGB", (101, 20), "red")
    for x in range(50, 101):
        for y in range(20):
            image.putpixel((x, y), (0, 0, 255))
    image.save(page)
    with Image.open(page) as opened:
        assert transcription._crop_box(opened, "complete") == (0, 0, 101, 20)
        assert transcription._crop_box(opened, "left") == (0, 0, 50, 20)
        assert transcription._crop_box(opened, "right") == (50, 0, 101, 20)


def test_build_generates_exactly_35_correctly_associated_images(tmp_path, specs):
    repository, publication, checked = _isolated_tree(tmp_path)
    outputs = transcription.build_transcription(repository, publication, checked)
    assert len(outputs) == 36
    assert [path.name for path in outputs[1:]] == [f"{spec.unit_id}.png" for spec in specs]
    for spec, path in zip(specs, outputs[1:], strict=True):
        with Image.open(path) as image:
            expected_width = 100 if spec.position == "complete" else 50
            assert image.size == (expected_width, 60)
            assert image.getpixel((0, 0))[0] == spec.pdf_page


def test_build_is_idempotent_and_cleans_only_its_owned_outputs(tmp_path):
    repository, publication, checked = _isolated_tree(tmp_path)
    first = transcription.build_transcription(repository, publication, checked)
    first_hashes = _hashes(first)
    stale = publication / "generated/assets/transcription/stale.png"
    stale.write_bytes(b"stale")
    prototype = publication / "generated/15-transcripcion-prototipo.qmd"
    prototype.write_text("regresión", encoding="utf-8")
    facsimile = publication / "generated/assets/facsimile/page-01.png"
    facsimile_hash = hashlib.sha256(facsimile.read_bytes()).hexdigest()
    second = transcription.build_transcription(repository, publication, checked)
    assert _hashes(second) == first_hashes
    assert not stale.exists()
    assert prototype.read_text(encoding="utf-8") == "regresión"
    assert hashlib.sha256(facsimile.read_bytes()).hexdigest() == facsimile_hash


def test_build_does_not_write_project_or_plugins(tmp_path):
    repository, publication, checked = _isolated_tree(tmp_path)
    plugins = repository / "plugins"
    plugins.mkdir()
    marker = plugins / "marker.txt"
    marker.write_text("intacto", encoding="utf-8")
    project_files = tuple(
        path for path in (repository / "project").rglob("*") if path.is_file()
    )
    before = _hashes(project_files + (marker,))
    transcription.build_transcription(repository, publication, checked)
    after = _hashes(project_files + (marker,))
    assert before == after


def test_real_navigation_replaces_visible_prototype_and_preserves_regression_manifest():
    quarto = yaml.safe_load((ROOT / "publication/_quarto.yml").read_text(encoding="utf-8"))
    chapters = yaml.safe_load(
        (ROOT / "publication/meta/chapters.yml").read_text(encoding="utf-8")
    )["chapters"]
    navigation = quarto["book"]["chapters"]
    assert navigation.count("generated/15-transcripcion.qmd") == 1
    assert "generated/15-transcripcion-prototipo.qmd" not in navigation
    assert sum(item.get("path") == "generated/15-transcripcion-prototipo.qmd" for item in chapters) == 1
    assert quarto["project"]["post-render"] == "scripts/fix_rendered_links.py"


def test_post_render_rewrites_only_legacy_prototype_links(tmp_path):
    html = tmp_path / "chapter.html"
    html.write_text(
        '<a href="../../generated/14-facsimil-prototipo.qmd#pagina-digital-12">A</a>'
        '<a href="../../generated/15-transcripcion-prototipo.qmd#folio-315v">B</a>',
        encoding="utf-8",
    )
    assert rendered_links.fix_rendered_links(tmp_path) == 2
    updated = html.read_text(encoding="utf-8")
    assert "14-facsimil.html#pagina-digital-12" in updated
    assert "15-transcripcion.html#folio-315v" in updated
    assert "-prototipo.qmd#" not in updated


def test_binary_policy_keeps_generated_pngs_out_of_git():
    result = subprocess.run(
        ["git", "check-ignore", "publication/generated/assets/transcription/folio_315v.png"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    assert result.stdout.strip().endswith("folio_315v.png")


def test_folio_315v_matches_the_accepted_prototype(canonical_units):
    unit = next(unit for unit in canonical_units if unit.spec.unit_id == "folio_315v")
    prototype_text = (ROOT / "publication/generated/15-transcripcion-prototipo.qmd").read_text(
        encoding="utf-8"
    )
    assert unit.spec.pdf_page == 12
    assert unit.spec.position == "left"
    assert tuple(unit.sections["Transcripción paleográfica"].splitlines()) == (
        validator._generated_paleographic_lines(prototype_text)
    )
    prototype_parts = {
        name: body.strip()
        for name, body in re_sections(prototype_text).items()
        if name in critical.TEXT_SECTION_NAMES
    }
    for name in critical.TEXT_SECTION_NAMES[1:]:
        assert prototype_parts[name] == unit.sections[name]
    assert hashlib.sha256(
        (ROOT / "publication/generated/assets/transcription/folio_315v.png").read_bytes()
    ).hexdigest() == hashlib.sha256(
        (ROOT / "publication/generated/assets/folio-315v.png").read_bytes()
    ).hexdigest()


def re_sections(text: str) -> dict[str, str]:
    import re

    matches = list(re.finditer(r"^### (?P<name>[^\n]+)\s*$", text, re.MULTILINE))
    result: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        content = text[match.end():end].strip()
        if content.endswith(
            "[Volver al capítulo histórico](../content/02-estudio/09-rio-molinos-recursos.qmd)."
        ):
            content = content.rsplit("\n", 2)[0].rstrip()
        result[match.group("name")] = content
    return result

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "publication/scripts"
sys.path.insert(0, str(SCRIPTS))

import build_facsimile as facsimile  # noqa: E402
import build_transcription as transcription  # noqa: E402
import check_sources as source_check  # noqa: E402
import critical_edition as critical  # noqa: E402
import f3_model as f3  # noqa: E402
import validate_publication as validator  # noqa: E402


UNITS = ROOT / "project/00_CONTROL/unidades.yaml"
EDITION = ROOT / "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md"
MANUSCRIPT_NAME = "sorrios_ensenada_orden_lectura_calidad_original.pdf"


@pytest.fixture(scope="module")
def specs() -> tuple[critical.UnitSpec, ...]:
    return critical.load_unit_specs(UNITS)


@pytest.fixture(scope="module")
def units(specs) -> tuple[critical.CriticalUnit, ...]:
    return critical.parse_critical_edition(
        EDITION.read_text(encoding="utf-8"), specs, MANUSCRIPT_NAME
    )


@pytest.fixture(scope="module")
def checked() -> source_check.CheckedSources:
    return source_check.CheckedSources(
        Path("/outside/manuscript.pdf"),
        source_check.ManuscriptMetadata("id", MANUSCRIPT_NAME, "0" * 64, 1, 18),
        (),
        35,
    )


@pytest.fixture(scope="module")
def mapping(specs) -> tuple[f3.PageUnits, ...]:
    return f3.validate_f3_mapping(specs, 18)


@pytest.fixture(scope="module")
def facsimile_qmd(specs, checked) -> str:
    config = facsimile.FacsimileConfig(
        180, "png", 18, "generated/assets/facsimile/page-{page:02d}.png"
    )
    return facsimile._facsimile_qmd(checked, config, specs)


@pytest.fixture(scope="module")
def transcription_qmd(units, checked) -> str:
    return transcription.transcription_qmd(units, checked)


def test_gf3_01_exactly_18_facsimile_pages(mapping, facsimile_qmd):
    assert len(mapping) == 18
    assert len(re.findall(r"^## Página digital \d{2}", facsimile_qmd, re.MULTILINE)) == 18


def test_gf3_02_exactly_35_transcription_units(units, transcription_qmd):
    assert len(units) == 35
    assert len(validator._generated_transcription_units(transcription_qmd)) == 35


def test_gf3_03_all_units_have_an_associated_page(specs, mapping):
    associated = [spec.unit_id for item in mapping for spec in item.units]
    assert associated == [spec.unit_id for spec in specs]


def test_gf3_04_all_page_anchors_are_unique(mapping):
    assert len({item.anchor for item in mapping}) == 18


def test_gf3_05_all_unit_anchors_are_unique(specs):
    anchors = [critical.published_unit_anchor(spec) for spec in specs]
    assert len(set(anchors)) == 35


def test_gf3_06_every_page_unit_relation_has_an_html_link(mapping, facsimile_qmd):
    for item in mapping:
        for spec in item.units:
            target = f"15-transcripcion.qmd#{critical.published_unit_anchor(spec)}"
            assert facsimile_qmd.count(target) == 1


def test_gf3_07_all_units_link_back_to_their_facsimile(specs, transcription_qmd):
    for spec in specs:
        assert f"14-facsimil.qmd#{f3.page_anchor(spec.pdf_page)}" in transcription_qmd


def test_gf3_08_all_html_units_use_the_approved_74_percent_crop(transcription_qmd):
    assert transcription_qmd.count("{.f3-html-crop}") == 35
    assert transcription_qmd.count(f'width="{f3.HTML_CROP_WIDTH}"') == 35


def test_gf3_09_all_html_units_use_native_lightbox(transcription_qmd):
    assert "lightbox: true" in transcription_qmd
    assert transcription_qmd.count("{.f3-html-crop}") == 35


def test_gf3_10_all_html_units_have_an_accessible_direct_fallback(transcription_qmd):
    assert transcription_qmd.count("Ampliar el recorte completo de ") == 35
    assert transcription_qmd.count('aria-label="Abrir el recorte completo') == 35
    assert "cdn" not in transcription_qmd.casefold()


def test_gf3_11_all_pdf_units_use_the_approved_28_percent_locator(transcription_qmd):
    assert transcription_qmd.count("{.f3-pdf-locator}") == 35
    assert transcription_qmd.count(f'width="{f3.PDF_LOCATOR_WIDTH}"') == 35


def test_gf3_12_all_pdf_units_express_page_and_position(specs, transcription_qmd):
    for spec in specs:
        position = critical.POSITION_LABELS[spec.position]
        assert f"**Localización:** página digital {spec.pdf_page}, {position}." in transcription_qmd


def test_gf3_13_all_pdf_units_link_to_the_complete_facsimile(specs, transcription_qmd):
    for spec in specs:
        target = f"14-facsimil.qmd#{f3.page_anchor(spec.pdf_page)}"
        assert target in transcription_qmd


def test_gf3_14_all_facsimile_targets_are_valid_unit_anchors(specs, facsimile_qmd):
    targets = re.findall(r"15-transcripcion\.qmd#([a-z0-9-]+)", facsimile_qmd)
    expected = [critical.published_unit_anchor(spec) for spec in specs]
    assert targets == expected


def test_gf3_15_preserves_canonical_transcription_and_reader_facing_apparatus(
    units, transcription_qmd
):
    generated = validator._generated_transcription_units(transcription_qmd)
    for canonical, (_, _, sections) in zip(units, generated, strict=True):
        for name in critical.TEXT_SECTION_NAMES:
            actual = sections[name]
            expected = canonical.sections[name]
            if name == "Transcripción paleográfica":
                actual = validator._decode_line_block(actual)
            else:
                expected = transcription.reader_facing_source_text(expected)
            assert actual == expected


def test_gf3_16_mapping_has_no_duplicates_or_orphans(specs, mapping):
    relations = [(item.page, spec.unit_id) for item in mapping for spec in item.units]
    assert len(relations) == len(set(relations)) == len(specs) == 35
    assert {page for page, _ in relations} == set(range(1, 19))


def test_gf3_17_generated_outputs_remain_unversioned():
    result = subprocess.run(
        ["git", "ls-files", "publication/generated"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    assert result.stdout == ""


def test_gf3_18_production_is_not_governed_by_prototype_sample_hardcodes():
    production = "\n".join(
        (SCRIPTS / name).read_text(encoding="utf-8")
        for name in (
            "f3_model.py",
            "build_facsimile.py",
            "build_transcription.py",
            "prepare.py",
        )
    )
    for marker in ("folio_315v", "folio_316r", "F3_PAGE", "F3_UNIT_IDS"):
        assert marker not in production

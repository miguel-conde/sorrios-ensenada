from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "publication/scripts"
sys.path.insert(0, str(SCRIPTS))

import build_f3_prototype as f3  # noqa: E402
import check_sources as source_check  # noqa: E402
import critical_edition as critical  # noqa: E402


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
def sample(specs, units) -> tuple[critical.CriticalUnit, ...]:
    selected = f3.select_f3_sample(specs)
    by_id = {unit.spec.unit_id: unit for unit in units}
    return tuple(by_id[spec.unit_id] for spec in selected)


@pytest.fixture(scope="module")
def checked() -> source_check.CheckedSources:
    metadata = source_check.ManuscriptMetadata(
        "1GgBs68iTi53ue8-TbrYFABALxadhQe5u",
        MANUSCRIPT_NAME,
        "0" * 64,
        1,
        18,
    )
    return source_check.CheckedSources(Path("/outside/manuscript.pdf"), metadata, (), 35)


def test_f3_01_facsimile_page_has_deterministic_existing_anchor(specs, checked):
    text = f3._facsimile_qmd(f3.select_f3_sample(specs), checked)
    assert "## Página digital 12 {#pagina-digital-12}" in text


def test_f3_02_page_knows_all_its_units(specs):
    assert tuple(spec.unit_id for spec in f3.units_for_page(specs, 12)) == (
        "folio_315v",
        "folio_316r",
    )


def test_f3_03_each_unit_knows_page_and_position(sample):
    assert [(unit.spec.pdf_page, unit.spec.position) for unit in sample] == [
        (12, "left"),
        (12, "right"),
    ]


def test_f3_04_html_uses_complete_documentary_crops(sample):
    for unit in sample:
        block = f3._unit_image(unit, output="html")
        assert f"assets/{unit.spec.unit_id}.png" in block
        assert f'width="{f3.HTML_CROP_WIDTH}"' in block
        assert 'when-format="html"' in block


def test_f3_05_html_has_local_accessible_enlargement(sample, checked):
    text = f3._transcription_qmd(sample, checked)
    assert "lightbox: true" in text
    assert text.count("Ampliar el recorte completo") == 2
    assert text.count('aria-label="Abrir el recorte completo') == 2
    assert "cdn" not in text.lower()


def test_f3_06_html_transcription_links_to_facsimile(sample, checked):
    text = f3._transcription_qmd(sample, checked)
    assert text.count("index.qmd#pagina-digital-12") == 4


def test_f3_07_facsimile_links_to_both_transcriptions(specs, checked):
    text = f3._facsimile_qmd(f3.select_f3_sample(specs), checked)
    assert "transcripcion-f3.qmd#folio-315v" in text
    assert "transcripcion-f3.qmd#folio-316r" in text


def test_f3_08_pdf_uses_reduced_locator_not_html_crop_size(sample):
    for unit in sample:
        html = f3._unit_image(unit, output="html")
        pdf = f3._unit_image(unit, output="pdf")
        assert f'width="{f3.PDF_LOCATOR_WIDTH}"' in pdf
        assert f3.HTML_CROP_WIDTH not in pdf
        assert 'when-format="pdf"' in pdf
        assert html != pdf


def test_f3_09_pdf_locator_links_back_to_facsimile(sample):
    for unit in sample:
        block = f3._unit_image(unit, output="pdf")
        assert "facsímil de la página completa" in block
        assert "index.qmd#pagina-digital-12" in block


def test_f3_10_paleographic_text_is_byte_equivalent(sample, checked):
    text = f3._transcription_qmd(sample, checked)
    for unit in sample:
        expected = critical.line_block(unit.sections["Transcripción paleográfica"])
        assert expected in text
        for name in critical.TEXT_SECTION_NAMES[1:]:
            assert unit.sections[name] in text


def test_f3_11_sample_selection_does_not_change_canonical_mapping(specs):
    before = hashlib.sha256(UNITS.read_bytes()).hexdigest()
    selected = f3.select_f3_sample(specs)
    assert [spec.order for spec in selected] == [22, 23]
    assert hashlib.sha256(UNITS.read_bytes()).hexdigest() == before


def test_f3_12_generated_prototype_is_ignored_and_untracked():
    result = subprocess.run(
        ["git", "check-ignore", "publication/generated/f3-prototype/_quarto.yml"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    assert result.stdout.strip().endswith("publication/generated/f3-prototype/_quarto.yml")
    tracked = subprocess.run(
        ["git", "ls-files", "publication/generated"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    assert tracked.stdout == ""

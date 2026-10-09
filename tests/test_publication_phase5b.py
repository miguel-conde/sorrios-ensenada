from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PUBLICATION = ROOT / "publication"
SCRIPTS = PUBLICATION / "scripts"
sys.path.insert(0, str(SCRIPTS))

import fix_rendered_links as html_fixer  # noqa: E402
import quality_audit as quality  # noqa: E402


def _navigation() -> tuple[list[object], list[str]]:
    quarto = yaml.safe_load((PUBLICATION / "_quarto.yml").read_text(encoding="utf-8"))
    items = quarto["book"]["chapters"]
    return items, quality.navigation_paths(items)


def test_final_book_has_six_parts_sixteen_chapters_four_apparatus_and_nine_indexes():
    items, paths = _navigation()
    assert tuple(item["part"] for item in items if isinstance(item, dict)) == quality.PARTS
    numbered = [
        path
        for path in paths
        if re.match(r"(?:content/(?:01-catastro|02-estudio)|generated)/(?:0?[1-9]|1[0-6])-", path)
        and "indices/" not in path
    ]
    assert len(numbered) == 16
    assert paths[14:17] == [
        "generated/14-facsimil.qmd",
        "generated/15-transcripcion.qmd",
        "generated/16-edicion-modernizada.qmd",
    ]
    assert paths[17:21] == [path.replace(".html", ".qmd") for path in quality.APPARATUS]
    assert paths[-9:] == [path.replace(".html", ".qmd") for path in quality.INDEXES]


def test_scaffolding_remains_as_regression_source_but_is_not_published():
    _, paths = _navigation()
    technical = PUBLICATION / "content/00-preliminares/00-prueba-tecnica.qmd"
    assert technical.is_file()
    assert "content/00-preliminares/00-prueba-tecnica.qmd" not in paths
    assert "prueba técnica" not in (PUBLICATION / "index.qmd").read_text(
        encoding="utf-8"
    ).casefold()


def test_configuration_and_contrast_audits_pass():
    assert quality.audit_configuration(PUBLICATION) == []
    assert quality.audit_contrast() == []
    assert quality.contrast_ratio("#6b3f20", "#ffffff") >= 4.5
    assert quality.contrast_ratio("#005fcc", "#ffffff") >= 3


def test_public_sources_have_no_local_markdown_link_targets():
    _, paths = _navigation()
    for relative in paths:
        text = (PUBLICATION / relative).read_text(encoding="utf-8")
        targets = re.findall(r"\[[^]]+\]\(([^)]+)\)", text)
        assert not any("/home/" in target or target.startswith("project/") for target in targets)


def test_html_parser_audits_language_headings_landmarks_images_tables_and_controls(tmp_path):
    page = tmp_path / "page.html"
    page.write_text(
        """<!doctype html><html lang="es"><head><title>Único</title></head><body>
        <nav aria-label="Principal"><a href="#tabla">Ir a la tabla</a></nav>
        <main><h1>Título</h1><h2>Sección</h2>
        <img src="folio.png" alt="Folio 315v usado como testimonio documental">
        <button aria-label="Buscar"></button>
        <table id="tabla" aria-label="Cifras"><thead><tr><th scope="col">Dato</th></tr></thead>
        <tbody><tr><td>1</td></tr></tbody></table></main></body></html>""",
        encoding="utf-8",
    )
    parsed = quality.parse_html(page)
    assert parsed.lang == "es"
    assert parsed.h1_count == parsed.main_count == 1
    assert parsed.nav_count == 1
    assert parsed.headings == [(1, "Título"), (2, "Sección")]
    assert parsed.images[0]["alt"].startswith("Folio 315v")
    assert parsed.tables[0].has_thead
    assert parsed.tables[0].header_scopes == ["col"]
    assert parsed.buttons[0]["aria-label"] == "Buscar"


def test_post_render_table_semantics_are_named_scoped_responsive_and_idempotent(tmp_path):
    page = tmp_path / "index.html"
    source = (
        '<html><head><title>Libro</title></head><body><h2>Cifras críticas</h2>'
        '<table class="table"><thead><tr><th>Valor</th></tr></thead>'
        '<tbody><tr><td>8</td></tr></tbody></table></body></html>'
    )
    page.write_text(source, encoding="utf-8")
    html_fixer.fix_rendered_links(tmp_path)
    first = page.read_text(encoding="utf-8")
    html_fixer.fix_rendered_links(tmp_path)
    second = page.read_text(encoding="utf-8")
    assert first == second
    assert first.count('class="table-scroll"') == 1
    assert 'aria-label="Tabla de Cifras críticas"' in first
    assert '<th scope="col">' in first
    assert 'tabindex="0"' in first


def test_pdf_filter_removes_only_internal_qmd_uri_annotations():
    source = (SCRIPTS / "pdf_internal_links.lua").read_text(encoding="utf-8")
    assert 'path:match("%.qmd$")' in source
    assert "return link.content" in source
    assert "http" not in source


def test_generated_document_counts_and_accessible_alternatives():
    facsimile = (PUBLICATION / "generated/14-facsimil.qmd").read_text(encoding="utf-8")
    transcription = (PUBLICATION / "generated/15-transcripcion.qmd").read_text(
        encoding="utf-8"
    )
    modernized = (PUBLICATION / "generated/16-edicion-modernizada.qmd").read_text(
        encoding="utf-8"
    )
    assert len(re.findall(r"^## Página digital \d{2}", facsimile, re.MULTILINE)) == 18
    assert facsimile.count('fig-alt="Página digital ') == 18
    assert len(re.findall(r"^## .+ \{#[a-z0-9-]+\}$", transcription, re.MULTILINE)) == 35
    assert transcription.count("fig-alt=") == 35
    assert len(re.findall(r"^## Respuesta \d+\.", modernized, re.MULTILINE)) == 40
    assert modernized.count("{.question-external}") == 40


def test_four_apparatus_nine_indexes_and_levels_are_explicit():
    _, paths = _navigation()
    assert len([path for path in paths if path in {p.replace('.html', '.qmd') for p in quality.APPARATUS}]) == 4
    assert len([path for path in paths if path in {p.replace('.html', '.qmd') for p in quality.INDEXES}]) == 9
    matrix = (PUBLICATION / "generated/matriz-evidencia.qmd").read_text(encoding="utf-8")
    for level in "DCIEL":
        assert f"`{level}`" in matrix
    for state in ("Admitida", "Condicionada", "Estado y cautela"):
        assert state in matrix


def test_pdf_and_html_auditors_cover_required_interfaces():
    source = (SCRIPTS / "quality_audit.py").read_text(encoding="utf-8")
    for tool in ("pdfinfo", "pdffonts", "pdftotext", "pdfimages", "pdftoppm"):
        assert f'"{tool}"' in source
    for check in ("numbered", "scope", "aria-label", "fragment", "focus"):
        assert check in source


def test_rendered_book_passes_phase5b_audits_when_artifacts_exist():
    technical_html = quality.BOOK_ROOT / "content/00-preliminares/00-prueba-tecnica.html"
    current_html = (
        quality.BOOK_ROOT.is_dir()
        and quality.PDF_PATH.is_file()
        and not technical_html.exists()
        and 'lang="es"' in (quality.BOOK_ROOT / "index.html").read_text(encoding="utf-8")
    )
    if current_html:
        assert quality.audit_html_book(quality.BOOK_ROOT) == []
        assert quality.audit_pdf(quality.PDF_PATH) == []
    else:
        # Clean clones validate the same contract during validate_publication --rendered.
        assert "audit_html_book" in (
            SCRIPTS / "validate_publication.py"
        ).read_text(encoding="utf-8")
        assert "audit_pdf" in (
            SCRIPTS / "validate_publication.py"
        ).read_text(encoding="utf-8")

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PUBLICATION = ROOT / "publication"
SCRIPTS = PUBLICATION / "scripts"
sys.path.insert(0, str(SCRIPTS))

import apparatus_sources  # noqa: E402
import build_apparatus  # noqa: E402


CANONICAL_COMMIT = "a162fad1792aa9b3804a5499d348ab355e5ce574"
REGISTER = (
    ROOT
    / "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md"
)
MATRIX = PUBLICATION / "generated/matriz-evidencia.qmd"
ACTIVE_KEYS = frozenset(build_apparatus.EVIDENCE_CITATIONS.values())
ACTIVE_KEYS = frozenset(key for group in ACTIVE_KEYS for key in group)
QA1 = {
    "QA-001",
    "QA-002",
    "QA-003",
    "QA-004",
    "QA-005",
    "QA-009",
    "QA-011",
    "QA-012",
    "QA-013",
}
OBJECTS = {
    "Volumen completo",
    "Facsímil",
    "Página del manuscrito",
    "Folio",
    "Unidad",
    "Respuesta",
    "Transcripción paleográfica",
    "Edición modernizada",
    "Capítulo histórico",
    "Entrada D/C/I/E/L",
    "Fuente externa",
}


def _git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()


def _bib_keys() -> set[str]:
    text = (PUBLICATION / "references.bib").read_text(encoding="utf-8")
    return set(re.findall(r"^@[A-Za-z]+\{([^,]+),", text, re.MULTILINE))


def _qmd_texts() -> str:
    paths = [*PUBLICATION.rglob("*.qmd")]
    return "\n".join(path.read_text(encoding="utf-8") for path in paths)


def test_sync_01_provenance_represents_the_current_project_tree():
    publication = yaml.safe_load(
        (PUBLICATION / "meta/publication.yml").read_text(encoding="utf-8")
    )
    assert publication["base"]["git_commit"] == CANONICAL_COMMIT
    assert _git("rev-parse", f"{CANONICAL_COMMIT}:project") == _git(
        "rev-parse", "HEAD:project"
    )


def test_sync_02_register_and_parser_use_the_real_canonical_version():
    register = apparatus_sources.load_evidence_register(REGISTER)
    assert register.version == apparatus_sources.REGISTER_VERSION == "1.3"
    assert len(register.entries) == 111


def test_sync_03_to_04_retired_tra_006_is_absent_from_current_publication():
    current = "\n".join(
        path.read_text(encoding="utf-8")
        for root in (PUBLICATION / "content", PUBLICATION / "generated")
        for path in root.rglob("*.qmd")
    )
    assert "TRA-006" not in current
    for name in (
        "11-hacienda-concejil-servicios-colectivos.qmd",
        "13-economia-rural-integrada-vulnerabilidades-resiliencia-limites.qmd",
    ):
        assert "TRA-006" not in next((PUBLICATION / "content").rglob(name)).read_text(
            encoding="utf-8"
        )


def test_sync_05_dem_005_is_generated_from_the_canonical_register():
    register = apparatus_sources.load_evidence_register(REGISTER)
    entry = next(item for item in register.entries if item.identifier == "DEM-005")
    matrix = MATRIX.read_text(encoding="utf-8")
    assert entry.statement in matrix
    assert "cabezas de casa o familias" in entry.statement
    assert "viudas con casa abierta" in entry.statement


def test_sync_06_to_07_bib_015_is_bounded_to_domestic_organization():
    chapter = (
        PUBLICATION / "content/02-estudio/06-vecinos-hogares-viviendas-trabajo.qmd"
    ).read_text(encoding="utf-8")
    assert "en distintos lugares las viudas podían contarse como medios vecinos" not in chapter
    paragraph = next(
        part for part in chapter.split("\n\n") if "@camarerobullon2002catastro" in part
    )
    assert "no sustenta una regla sobre el *medio vecino*" in paragraph
    assert "no autoriza coeficientes de población" in paragraph


def test_bib_01_references_parse_with_the_native_pandoc_processor():
    keys = sorted(_bib_keys())
    source = "[" + "; ".join(f"@{key}" for key in keys) + "]"
    result = subprocess.run(
        [
            "quarto",
            "pandoc",
            "-f",
            "markdown",
            "-t",
            "plain",
            "--citeproc",
            f"--bibliography={PUBLICATION / 'references.bib'}",
        ],
        cwd=ROOT,
        input=source,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr


def test_bib_02_to_03_every_cited_key_exists_and_active_keys_are_complete():
    keys = _bib_keys()
    cited = set(
        re.findall(r"(?<![A-Za-z0-9._%+-])@([A-Za-z][A-Za-z0-9_-]+)", _qmd_texts())
    )
    cited = {key for key in cited if not key.startswith(("tbl-", "fig-", "sec-"))}
    assert cited <= keys
    assert keys == ACTIVE_KEYS
    assert len(keys) == 24


def test_bib_04_public_bibliography_uses_the_native_refs_container():
    page = (PUBLICATION / "content/06-aparatos/bibliografia.qmd").read_text(
        encoding="utf-8"
    )
    assert "#refs" in page
    assert "@*" in page
    assert "<script" not in page

    styles = (PUBLICATION / "styles/book.scss").read_text(encoding="utf-8")
    assert "#refs .csl-entry" in styles
    assert "#refs a" in styles
    assert "overflow-wrap: anywhere" in styles


def test_bib_05_bib_012_does_not_reappear_as_vecera_support():
    bibliography = (PUBLICATION / "references.bib").read_text(encoding="utf-8")
    assert "cuadrosleon" not in bibliography.casefold()
    assert "vecera" not in bibliography.casefold()


def test_bib_06_to_07_active_sources_and_verified_metadata_are_controlled():
    bibliography = (PUBLICATION / "references.bib").read_text(encoding="utf-8")
    assert len(ACTIVE_KEYS) == 24
    assert bibliography.count("urldate = {2026-10-11}") == 15
    for forbidden in ("fecha desconocida", "autor desconocido", "doi pendiente"):
        assert forbidden not in bibliography.casefold()


def test_trace_01_matrix_anchors_are_unique_and_complete():
    matrix = MATRIX.read_text(encoding="utf-8")
    anchors = re.findall(r"^### [A-Z]+-\d{3} \{#(evidencia-[a-z]+-\d{3})", matrix, re.MULTILINE)
    assert len(anchors) == len(set(anchors)) == 111


def test_trace_02_visible_marks_are_converted_by_the_shared_filter():
    lua = (SCRIPTS / "evidence_links.lua").read_text(encoding="utf-8")
    assert "matriz-evidencia.qmd#evidencia-" in lua
    assert "[DCIEL/]+" in lua
    assert 'identifier:match("^CAL%-%d%d%d$")' in lua
    quarto = yaml.safe_load((PUBLICATION / "_quarto.yml").read_text(encoding="utf-8"))
    assert "scripts/evidence_links.lua" in quarto["format"]["html"]["filters"]
    assert "scripts/evidence_links.lua" in quarto["format"]["pdf"]["filters"]


def test_trace_03_matrix_returns_have_real_section_fragments():
    matrix = MATRIX.read_text(encoding="utf-8")
    returns = re.findall(r"\]\((\.\./content/[^)#]+\.qmd)#([a-z0-9-]+)\)", matrix)
    assert returns
    for relative, anchor in returns:
        target = (PUBLICATION / "generated" / relative).resolve()
        assert target.is_file()
        assert f"{{#{anchor}" in target.read_text(encoding="utf-8")


def test_trace_04_every_current_external_entry_has_bibliography_mapping():
    register = apparatus_sources.load_evidence_register(REGISTER)
    external = {entry.identifier for entry in register.entries if "E" in entry.level_components}
    assert len(external) == 24
    assert set(build_apparatus.EVIDENCE_CITATIONS) == external


def test_trace_05_top_006_remains_only_in_the_matrix():
    narrative = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (PUBLICATION / "content").rglob("*.qmd")
    )
    assert "TOP-006" not in narrative
    assert "### TOP-006" in MATRIX.read_text(encoding="utf-8")


def test_trace_06_no_retired_identifier_is_published_as_current():
    assert "TRA-006" not in _qmd_texts()


def test_qa1_apparatus_contains_exactly_the_nine_approved_questions():
    page = (PUBLICATION / "content/06-aparatos/cuestiones-abiertas.qmd").read_text(
        encoding="utf-8"
    )
    identifiers = set(re.findall(r"^### (QA-\d{3})", page, re.MULTILINE))
    assert identifiers == QA1
    assert page.count("../../generated/matriz-evidencia.qmd#evidencia-lim-") == 9
    for excluded in ("QA-006", "QA-007", "QA-008", "QA-010"):
        assert excluded not in page


def test_citation_models_cover_all_eleven_objects_in_seven_families():
    page = (PUBLICATION / "content/06-aparatos/como-citar.qmd").read_text(
        encoding="utf-8"
    )
    rows = re.findall(r"^\| ([^|]+?) \| ([^|]+?) \|", page, re.MULTILINE)
    rows = [(obj.strip(), family.strip()) for obj, family in rows if obj != "Objeto citable"]
    assert {obj for obj, _ in rows} == OBJECTS
    assert len(rows) == 11
    assert len({family for _, family in rows}) == 7
    assert "Miguel Conde de Simón" in page
    assert "Conde de Simón, Miguel" in page
    assert "ISBN" in page and "No se\nañade ISBN" in page
    assert "URL canónica pendiente" not in page
    assert page.count("https://sorribos-santibanez-1752.netlify.app/") >= 11


def test_intellectual_history_is_reader_facing_not_a_git_changelog():
    page = (
        PUBLICATION / "content/06-aparatos/historia-intelectual-editorial.qmd"
    ).read_text(encoding="utf-8")
    normalized = " ".join(page.split())
    for required in (
        "manuscrito de 1752",
        "edición crítica",
        "edición modernizada",
        "estudio histórico",
        "matriz D/C/I/E/L",
        "navegación bidireccional",
    ):
        assert required in normalized
    for forbidden in (
        "commit", "SHA", "rama", "pytest", "integración continua",
        "Registro 1.3", "composición 0.6", "edición Quarto",
    ):
        assert forbidden not in page


def test_glossary_keeps_historical_context_unpublished_and_generated_ignored():
    glossary = (PUBLICATION / "generated/glosario.qmd").read_text(encoding="utf-8")
    assert "Contexto histórico" not in glossary
    assert _git("ls-files", "publication/generated") == ""

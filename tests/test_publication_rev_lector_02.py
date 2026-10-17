from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PUBLICATION = ROOT / "publication"
BASE_COMMIT = "a9ffe2cd67238323f152d7c709e81176d3f673a0"
sys.path.insert(0, str(PUBLICATION / "scripts"))

import build_apparatus  # noqa: E402
import reader_text  # noqa: E402


def _body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    return text.split("---", 2)[-1] if text.startswith("---") else text


def _git(*arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *arguments], cwd=ROOT, capture_output=True, text=True, check=False
    )


def test_reader_facing_sources_remove_internal_versions_paths_and_workflow_terms():
    texts = [
        _body(path)
        for path in sorted((PUBLICATION / "content").rglob("*.qmd"))
        if path.name != "00-prueba-tecnica.qmd"
    ]
    texts.extend(
        _body(path)
        for path in sorted((PUBLICATION / "generated").rglob("*.qmd"))
        if "prototipo" not in path.name and "f3-prototype" not in path.parts
    )
    public = "\n".join(texts)
    for residue in (
        "publication/content/",
        "publication/generated/",
        "front matter",
        "`casefold`",
        "NFKD",
        "Registro 1.3",
        "Estudio Histórico 1.3",
        "Edición Crítica 3.6",
        "edición crítica 3.6",
        "edición modernizada 1.3",
        "composición 0.6",
        "libro Quarto",
        "edición Quarto",
        "previa a candidata",
        "en el release",
        "clasificados como QA1",
        "nivel canónico",
        "`references.bib`",
    ):
        assert residue not in public


def test_chapter_nine_links_directly_to_current_documentary_layers():
    text = (
        PUBLICATION / "content/02-estudio/09-rio-molinos-recursos.qmd"
    ).read_text(encoding="utf-8")
    expected = {
        "../../generated/14-facsimil.qmd#pagina-digital-12",
        "../../generated/15-transcripcion.qmd#folio-315v",
        "../../generated/16-edicion-modernizada.qmd#respuesta-17",
        "../../generated/matriz-evidencia.qmd#evidencia-hid-001",
    }
    assert all(target in text for target in expected)
    assert "-prototipo.qmd#" not in text
    assert "aparato-molinos.qmd#matriz-molinera" not in text


def test_link_corrections_use_only_destinations_verified_by_link_01():
    bibliography = (PUBLICATION / "references.bib").read_text(encoding="utf-8")
    assert bibliography.count("@") == 24
    assert "pares.mcu.es" not in bibliography
    assert "10.17811/er.0.1984.71-94" not in bibliography
    assert "https://reunido.uniovi.es/index.php/RCG/article/download/894/824" in bibliography
    public_generated = "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted((PUBLICATION / "generated").rglob("*.qmd"))
        if "prototipo" not in path.name and "f3-prototype" not in path.parts
    )
    assert "pares.mcu.es" not in public_generated
    assert "gredos.usal.es/bitstream/handle/10366/151409" not in public_generated
    assert "https://gredos.usal.es/handle/10366/151409" in public_generated
    assert all(new in public_generated or new in bibliography for new in reader_text.PUBLIC_URL_REPLACEMENTS.values())


def test_contact_section_is_localized_and_repository_remains_future_tense():
    contact = PUBLICATION / "content/06-aparatos/correcciones-contacto.qmd"
    body = _body(contact)
    assert "# Correcciones y contacto" in body
    assert "EMAIL DE CONTACTO — PLACEHOLDER PENDIENTE" in body
    assert "Cuando el repositorio público esté disponible" in body
    assert not re.search(r"https?://[^\s)]*github\.com", body)
    quarto = yaml.safe_load((PUBLICATION / "_quarto.yml").read_text(encoding="utf-8"))
    part = next(
        item for item in quarto["book"]["chapters"]
        if isinstance(item, dict) and item.get("part") == "Parte VI. Aparatos e índices"
    )
    chapters = part["chapters"]
    assert chapters.index("content/06-aparatos/como-citar.qmd") < chapters.index(
        "content/06-aparatos/correcciones-contacto.qmd"
    ) < chapters.index("content/06-aparatos/bibliografia.qmd")


def test_facsimile_states_resolution_once_and_transcription_hides_source_filenames():
    facsimile = (PUBLICATION / "generated/14-facsimil.qmd").read_text(encoding="utf-8")
    transcription = (PUBLICATION / "generated/15-transcripcion.qmd").read_text(
        encoding="utf-8"
    )
    assert facsimile.count("180 ppp") == 1
    assert facsimile.count("rasterización completa") == 0
    assert len(re.findall(r"^Página \d+ de 18\.$", facsimile, re.MULTILINE)) == 18
    body = transcription.split("---", 2)[-1]
    for residue in (
        "unidades.yaml",
        "Edicion_Critica.md",
        "Manual Editorial v",
        "duda D-001",
        "durante esta operación",
    ):
        assert residue not in body


def test_evidence_apparatus_keeps_d_c_i_e_l_while_using_reader_labels():
    matrix = (PUBLICATION / "generated/matriz-evidencia.qmd").read_text(
        encoding="utf-8"
    )
    assert "La matriz reúne las formulaciones controladas" in matrix
    assert "**Formulación controlada:**" in matrix
    assert len(re.findall(r"^### [A-Z]+-\d{3} \{#evidencia-", matrix, re.MULTILINE)) == 111
    for level in ("`D`", "`C`", "`I`", "`E`", "`L`"):
        assert level in matrix
    identifiers = set(re.findall(r"^### ([A-Z]+-\d{3})", matrix, re.MULTILINE))
    assert set(build_apparatus.EVIDENCE_CITATIONS) <= identifiers


def test_canonical_project_tree_remains_unchanged_from_e3_baseline():
    assert _git("diff", "--quiet", BASE_COMMIT, "--", "project/").returncode == 0

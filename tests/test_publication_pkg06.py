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

import quality_audit as quality  # noqa: E402


BASE_COMMIT = "dc4982714a39f5ac9839d016090a8510bb727f29"
PRELIMINARIES = (
    "content/00-preliminares/01-creditos.qmd",
    "content/00-preliminares/02-prologo.qmd",
    "content/00-preliminares/03-introduccion.qmd",
    "content/00-preliminares/04-convenciones.qmd",
)


def _yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _front_matter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    _, raw, body = text.split("---", 2)
    return yaml.safe_load(raw), body


def _git(*arguments: str) -> str:
    return subprocess.run(
        ["git", *arguments],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout


def test_public_identity_and_landing_are_final_in_form_but_not_release_metadata():
    quarto = _yaml(PUBLICATION / "_quarto.yml")
    assert quarto["book"]["title"] == "Sorribos y Santibáñez de Ordás en 1752"
    assert quarto["book"]["subtitle"] == (
        "Estudio histórico y edición integral del Catastro de Ensenada"
    )
    assert quarto["book"]["author"] == "Miguel Conde de Simón"
    landing = (PUBLICATION / "index.qmd").read_text(encoding="utf-8")
    assert "Proyecto Sorríos — Catastro de Ensenada" in landing
    assert "Ruta histórica" in landing and "Ruta documental" in landing
    assert "edición en desarrollo" not in landing.casefold()
    assert "prepublicación" not in landing.casefold()


def test_preliminaries_precede_the_unchanged_six_part_macroorder():
    quarto = _yaml(PUBLICATION / "_quarto.yml")
    items = quarto["book"]["chapters"]
    paths = quality.navigation_paths(items)
    assert tuple(paths[:5]) == ("index.qmd", *PRELIMINARIES)
    assert tuple(item["part"] for item in items if isinstance(item, dict)) == quality.PARTS
    assert len(paths) == 39
    assert paths[-1] == "content/06-aparatos/colofon.qmd"


def test_manifest_registers_the_four_preliminaries_in_public_order():
    manifest = _yaml(PUBLICATION / "meta/chapters.yml")["chapters"]
    assert tuple(item["path"] for item in manifest[1:5]) == PRELIMINARIES
    assert tuple(item["chapter_id"] for item in manifest[1:5]) == (
        "creditos-derechos",
        "prologo",
        "introduccion-general",
        "convenciones-lectura",
    )


def test_credits_assign_only_the_approved_human_responsibilities_and_rights():
    text = (PUBLICATION / PRELIMINARIES[0]).read_text(encoding="utf-8")
    for role in (
        "Autor, investigación y dirección editorial",
        "Edición crítica",
        "Transcripción paleográfica y revisión",
        "Edición modernizada y revisión",
    ):
        assert f"**{role}:** Miguel Conde de Simón" in text
    assert "CC BY 4.0" in text
    assert "contenido original" in text
    for component in ("facsímil", "reproducciones", "cartografía"):
        assert component in text
    assert "único participante humano" in text


def test_prologue_is_an_explicit_controlled_placeholder_with_six_topics():
    metadata, body = _front_matter(PUBLICATION / PRELIMINARIES[1])
    assert metadata["publication-status"] == "placeholder"
    assert "PENDIENTE DE REDACCIÓN PERSONAL DEL AUTOR" in body
    assert "no es un prólogo terminado" in body
    assert "antes de `GATE-02`" in body
    assert len(re.findall(r"^\d\. ", body, re.MULTILINE)) == 6
    assert not re.search(r"\b(?:yo|mi|mis|me)\b", body.casefold())


def test_introduction_is_compact_and_connects_both_routes_to_chapter_four():
    _, body = _front_matter(PUBLICATION / PRELIMINARIES[2])
    assert len(body.split()) < 500
    for phrase in (
        "ruta histórica",
        "ruta documental",
        "facsímil",
        "transcripción paleográfica",
        "edición en español actual",
        "D/C/I/E/L",
        "capítulo 4",
    ):
        assert phrase in body


def test_conventions_cover_spelling_locators_answers_evidence_and_links():
    _, body = _front_matter(PUBLICATION / PRELIMINARIES[3])
    for phrase in (
        "Grafía histórica y modernizada",
        "Páginas y folios",
        "Preguntas y respuestas",
        "D/C/I/E/L",
        "Enlaces",
    ):
        assert phrase in body
    assert len(body.split()) < 300


def test_detailed_methodology_chapter_is_byte_identical_to_the_base():
    relative = "publication/content/01-catastro/04-manuscrito-volumen-actual.qmd"
    expected = _git("show", f"{BASE_COMMIT}:{relative}")
    assert (ROOT / relative).read_text(encoding="utf-8") == expected


def test_informative_closure_titles_preserve_the_stable_anchors():
    expected = {
        "09-rio-molinos-recursos.qmd": (
            "Recursos documentados, capacidad no calculable",
            "recursos-sintesis",
        ),
        "10-iglesia-senorio-fiscalidad.qmd": (
            "Derechos diferenciados, carga total no calculable",
            "fiscal-sintesis",
        ),
        "11-hacienda-concejil-servicios-colectivos.qmd": (
            "Repartimiento y servicios sin presupuesto completo",
            "hacienda-sintesis",
        ),
        "12-dinero-oficios-conexiones-exteriores.qmd": (
            "Dinero y conexiones sin mercado reconstruible",
            "dinero-sintesis",
        ),
    }
    directory = PUBLICATION / "content/02-estudio"
    for filename, (heading, anchor) in expected.items():
        text = (directory / filename).read_text(encoding="utf-8")
        assert f"## {heading} {{#{anchor}}}" in text
        assert f"## Síntesis {{#{anchor}}}" not in text


def test_pkg06_does_not_modify_canonical_sources_or_generated_outputs():
    assert _git("diff", "--quiet", BASE_COMMIT, "--", "project/") == ""
    assert _git("diff", "--quiet", BASE_COMMIT, "--", "publication/generated/") == ""


def test_static_publication_audit_accepts_the_pkg06_architecture():
    assert quality.audit_configuration(PUBLICATION) == []

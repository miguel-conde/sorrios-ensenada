from __future__ import annotations

import hashlib
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PUBLICATION = ROOT / "publication"

CREDITS_DECLARATION = """En la elaboración de esta obra se utilizaron herramientas digitales y
sistemas de inteligencia artificial como apoyo auxiliar en tareas de
transcripción y análisis paleográfico, localización y contraste de fuentes,
investigación histórica, análisis y estructuración de información, revisión
de consistencia y preparación editorial. Estas herramientas no son autoras ni
sustituyen el juicio histórico, paleográfico o editorial. Las lecturas, las
fuentes utilizadas, las interpretaciones y las decisiones editoriales y de
publicación fueron revisadas y validadas por Miguel Conde de Simón, que asume
la responsabilidad intelectual y final de la obra."""

COLOPHON_DECLARATION = """### Herramientas digitales e inteligencia artificial

En la elaboración de esta obra se utilizaron herramientas digitales y sistemas
de inteligencia artificial como apoyo auxiliar en tareas de transcripción y
análisis paleográfico; localización, contraste y organización de fuentes;
investigación histórica; análisis y estructuración de información; revisión de
consistencia; preparación editorial; programación y automatización de
controles; y tareas técnicas y documentales asociadas a una composición
reproducible.

Entre las principales herramientas utilizadas se encuentran **ChatGPT**,
**Codex** y **GitHub Copilot** como sistemas de asistencia basados en
inteligencia artificial, y **Python** y **Quarto** para los procesos de
tratamiento, validación, generación reproducible y composición de las versiones
HTML y PDF. El proyecto se ha gestionado mediante infraestructura de control de
versiones y repositorio, cuya descripción técnica detallada se conserva en la
documentación del proyecto.

Los sistemas de inteligencia artificial **no se utilizaron como fuentes
históricas**. Las afirmaciones de la obra se fundamentan en el manuscrito, en
los cálculos reproducibles derivados de él o en las fuentes externas
identificadas y citadas.

Estas herramientas no son autoras de la obra ni sustituyen el juicio histórico,
paleográfico o editorial. Las lecturas del manuscrito, la selección y valoración
de las fuentes, las interpretaciones históricas y las decisiones editoriales y
de publicación fueron revisadas y validadas por **Miguel Conde de Simón**, que
asume la responsabilidad intelectual y final de la obra."""


def _front_matter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    _, raw, body = text.split("---", 2)
    return yaml.safe_load(raw), body


def test_human_prologue_is_preserved_and_marked_final():
    metadata, body = _front_matter(
        PUBLICATION / "content/00-preliminares/02-prologo.qmd"
    )
    assert metadata["publication-status"] == "prepublication"
    assert hashlib.sha256(body.encode()).hexdigest() == (
        "819746169d343d0eaaa62bdccbf3bb98f235c50949ef2cdfedb6a5e0a2aca410"
    )
    assert body.lstrip().startswith("# Prólogo {.unnumbered}\n")
    assert body.rstrip().endswith("**Miguel Conde de Simón**<br>\nSorríos, 2026")


def test_colophon_ai_declaration_is_preserved_and_credits_refer_to_it():
    credits = (
        PUBLICATION / "content/00-preliminares/01-creditos.qmd"
    ).read_text(encoding="utf-8")
    colophon = (
        PUBLICATION / "content/06-aparatos/colofon.qmd"
    ).read_text(encoding="utf-8")
    assert CREDITS_DECLARATION not in credits
    assert "se detallan en el [colofón]" in credits
    assert colophon.count(COLOPHON_DECLARATION) == 1


def test_prologue_metadata_and_remaining_deferrals_are_synchronized():
    chapters = yaml.safe_load(
        (PUBLICATION / "meta/chapters.yml").read_text(encoding="utf-8")
    )["chapters"]
    prologue = next(item for item in chapters if item["chapter_id"] == "prologo")
    assert prologue["publication_status"] == "prepublication"

    publication = yaml.safe_load(
        (PUBLICATION / "meta/publication.yml").read_text(encoding="utf-8")
    )["publication"]
    assert publication["pending"] == {
        "at_release": ["fecha exacta de publicación", "URL canónica"],
        "non_blocking": ["ISBN solo si llega a existir"],
    }


def test_hum01b_dossier_records_deferred_integral_validation():
    dossier = (ROOT / "docs/HUM_01B_CIERRE_INPUTS_EDITORIALES_HUMANOS.md").read_text(
        encoding="utf-8"
    )
    normalized = " ".join(dossier.split())
    for value in (
        "preservado literalmente",
        "`placeholder` a `prepublication`",
        "ChatGPT",
        "Codex",
        "GitHub Copilot",
        "Python",
        "Quarto",
        "no se utilizaron como fuentes históricas",
        "validación integral",
        "PKG-12 no se inicia",
    ):
        assert value in normalized

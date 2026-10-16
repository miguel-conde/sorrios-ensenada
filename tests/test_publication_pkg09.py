from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PUBLICATION = ROOT / "publication"
BASE_COMMIT = "61f91b1a6b378fb66c31fdecb4628815efec9b1d"
TITLE = "Sorribos y Santibáñez de Ordás en 1752"
SUBTITLE = "Estudio histórico y edición integral del Catastro de Ensenada"
AUTHOR = "Miguel Conde de Simón"
PROJECT = "Proyecto Sorríos — Catastro de Ensenada"
COLOPHON = PUBLICATION / "content/06-aparatos/colofon.qmd"

sys.path.insert(0, str(PUBLICATION / "scripts"))
import fix_rendered_links as html_fixer  # noqa: E402


def _yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _git(*arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *arguments],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


def test_identity_metadata_has_one_approved_human_author_and_year_only():
    quarto = _yaml(PUBLICATION / "_quarto.yml")
    book = quarto["book"]
    assert (book["title"], book["subtitle"], book["author"]) == (
        TITLE,
        SUBTITLE,
        AUTHOR,
    )
    assert book["date"] == "2026"
    assert book["date-format"] == "YYYY"
    assert quarto["lang"] == "es"
    assert quarto["project-identity"] == PROJECT
    assert quarto["author-bibliographic"] == "Conde de Simón, Miguel"
    assert "contenido original" in quarto["copyright"]
    assert "solo al contenido original" in quarto["license"]
    assert "terceros" in quarto["license"]
    assert "url" not in {key.casefold() for key in quarto}
    assert "isbn" not in {key.casefold() for key in quarto}


def test_publication_manifest_normalizes_identity_rights_and_deferrals():
    publication = _yaml(PUBLICATION / "meta/publication.yml")["publication"]
    identity = publication["identity"]
    assert publication["version"] == "1.0"
    assert publication["status"] == "prepublication"
    assert identity["title"] == TITLE and identity["subtitle"] == SUBTITLE
    assert identity["project"] == PROJECT
    assert identity["author"] == {
        "display": AUTHOR,
        "bibliographic": "Conde de Simón, Miguel",
    }
    assert identity["language"] == "es" and identity["year"] == 2026
    rights = publication["rights"]
    assert rights["copyright"] == f"© 2026 {AUTHOR}"
    assert "CC BY 4.0" in rights["license"]
    assert "contenido original" in rights["scope"]
    assert all(
        component in rights["third_party"]
        for component in ("facsímil", "reproducciones", "cartografía")
    )
    assert publication["pending"] == {
        "before_candidate": ["texto definitivo del prólogo personal"],
        "at_release": ["fecha exacta de publicación", "URL canónica"],
        "non_blocking": ["ISBN solo si llega a existir"],
    }
    assert "isbn" not in publication and "url" not in publication


def test_credits_are_exact_and_ai_tools_have_no_authorship():
    credits = (
        PUBLICATION / "content/00-preliminares/01-creditos.qmd"
    ).read_text(encoding="utf-8")
    for role in (
        "Autor, investigación y dirección editorial",
        "Edición crítica",
        "Transcripción paleográfica y revisión",
        "Edición modernizada y revisión",
    ):
        assert f"**{role}:** {AUTHOR}" in credits
    assert f"© 2026 {AUTHOR}" in credits
    assert "sistemas de\ninteligencia artificial" in credits
    assert "No tienen\nautoría" in credits
    assert "revisadas y asumidas por\nMiguel Conde de Simón" in credits
    for forbidden in ("ORCID", "afiliación", "coautor", "colaborador humano"):
        assert forbidden.casefold() not in credits.casefold()


def test_colophon_is_compact_complete_and_not_a_technical_changelog():
    text = COLOPHON.read_text(encoding="utf-8")
    body = text.split("---", 2)[-1]
    normalized = " ".join(body.split())
    assert len(body.split()) < 260
    for value in (
        TITLE,
        SUBTITLE,
        AUTHOR,
        PROJECT,
        "© 2026",
        "CC BY 4.0",
        "contenido original",
        "materiales de terceros",
        "sistemas de inteligencia artificial",
        "no tienen autoría",
        "responsabilidad final",
        "fecha exacta de publicación",
        "URL canónica",
    ):
        assert value in normalized
    for residue in ("commit", "SHA-256", "GitHub", "ChatGPT", "Codex", "Copilot"):
        assert residue not in body


def test_citation_models_use_final_identity_and_only_controlled_placeholders():
    text = (PUBLICATION / "content/06-aparatos/como-citar.qmd").read_text(
        encoding="utf-8"
    )
    assert text.count("| Volumen completo |") == 1
    assert len(re.findall(r"^\| (?!Objeto citable)[^|]+ \|", text, re.MULTILINE)) == 11
    assert "Conde de Simón, Miguel" in text
    assert f"*{TITLE}: {SUBTITLE}*" in text
    assert "versión 1.0" in text.casefold() and "2026" in text
    assert "versión y fecha de publicación pendientes" not in text
    assert "URL canónica pendiente" in text
    assert "ISBN" in text and "No se\nañade ISBN" in text


def test_colophon_is_last_and_registered_once():
    quarto = _yaml(PUBLICATION / "_quarto.yml")
    chapters = quarto["book"]["chapters"]
    part_six = next(item for item in chapters if isinstance(item, dict) and item.get("part") == "Parte VI. Aparatos e índices")
    assert part_six["chapters"][-1] == "content/06-aparatos/colofon.qmd"
    manifest = _yaml(PUBLICATION / "meta/chapters.yml")["chapters"]
    entries = [item for item in manifest if item["path"] == "content/06-aparatos/colofon.qmd"]
    assert entries == [
        {
            "chapter_id": "colofon",
            "path": "content/06-aparatos/colofon.qmd",
            "publication_status": "prepublication",
        }
    ]


def test_year_only_html_metadata_does_not_invent_an_exact_date(tmp_path):
    page = tmp_path / "index.html"
    page.write_text(
        '<html><head><meta name="dcterms.date" content="2026-01-01">'
        '<title>Libro</title></head><body></body></html>',
        encoding="utf-8",
    )
    html_fixer.fix_rendered_links(tmp_path)
    rendered = page.read_text(encoding="utf-8")
    assert 'name="dcterms.date" content="2026"' in rendered
    assert "2026-01-01" not in rendered


def test_prologue_project_and_prior_packages_remain_untouched():
    assert _git("diff", "--quiet", BASE_COMMIT, "--", "project/").returncode == 0
    assert _git(
        "diff",
        "--quiet",
        BASE_COMMIT,
        "--",
        "publication/content/00-preliminares/02-prologo.qmd",
        "publication/assets/",
        "publication/references.bib",
    ).returncode == 0
    prologue = (
        PUBLICATION / "content/00-preliminares/02-prologo.qmd"
    ).read_text(encoding="utf-8")
    assert "publication-status: placeholder" in prologue
    assert "PENDIENTE DE REDACCIÓN PERSONAL DEL AUTOR" in prologue


def test_pkg09_does_not_publish_or_version_generated_outputs():
    assert _git("ls-files", "publication/generated", "publication/_book").stdout == ""
    added = _git("diff", "--name-only", "--diff-filter=A", BASE_COMMIT).stdout.splitlines()
    assert not any(Path(path).suffix.casefold() in {".pdf", ".png", ".jpg", ".jpeg"} for path in added)
    assert not any("pkg-10" in path.casefold() or "release" in path.casefold() for path in added)

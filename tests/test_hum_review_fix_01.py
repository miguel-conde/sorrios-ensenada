from __future__ import annotations

import re
import subprocess
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PUBLICATION = ROOT / "publication"
BASE_COMMIT = "550f551f2fc279b5bcc75f013a2b5e8bb4560519"
PROLOGUE = "publication/content/00-preliminares/02-prologo.qmd"


def _git(*arguments: str) -> str:
    return subprocess.run(
        ["git", *arguments],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout


def test_prologue_changes_only_the_authorized_sentence():
    previous = _git("show", f"{BASE_COMMIT}:{PROLOGUE}")
    current = (ROOT / PROLOGUE).read_text(encoding="utf-8")
    old = "La primera vez que conocí Sorríos, poco después de casarnos en 1994,"
    new = "Cuando conocí Sorríos, poco después de casarnos en 1994,"
    assert previous.count(old) == 1
    assert current == previous.replace(old, new, 1)
    assert old not in current
    assert new in current


def test_author_label_override_is_narrow_and_isbn_is_not_pending():
    language = yaml.safe_load(
        (PUBLICATION / "_language.yml").read_text(encoding="utf-8")
    )
    assert language == {"title-block-author-single": "Autor"}
    metadata = yaml.safe_load(
        (PUBLICATION / "meta/publication.yml").read_text(encoding="utf-8")
    )["publication"]
    assert metadata["pending"] == {
        "at_release": ["fecha exacta de publicación"],
    }
    assert "isbn" not in {key.casefold() for key in metadata}


def test_public_readme_explains_the_project_reproduction_rights_and_contact():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    normalized = " ".join(readme.split())
    required = (
        "Sorribos y Santibáñez de Ordás en 1752",
        "Miguel Conde de Simón",
        "https://sorribos-santibanez-1752.netlify.app/",
        "`project/`",
        "`publication/`",
        "`publication/generated/`",
        "`publication/_book/`",
        "Python",
        "Quarto",
        "LuaLaTeX",
        "Poppler",
        "`rsvg-convert`",
        "python publication/scripts/prepare.py",
        "CC BY 4.0",
        "licencia MIT",
        "materiales de terceros",
        "GitHub Issues",
        "miguelco2000@gmail.com",
        "no se solicitará ISBN",
    )
    assert all(value in normalized for value in required)
    for forbidden in (
        "ISBN pendiente",
        "ISBN por asignar",
        "URL canónica pendiente",
        "repositorio privado",
        "próximamente",
        "cuando se publique",
    ):
        assert forbidden.casefold() not in normalized.casefold()
    assert not re.search(r"(?:/home/|/tmp/|[A-Za-z]:\\\\)", readme)


def test_human_review_fix_preserves_canonical_project_and_ignored_outputs():
    assert _git("diff", "--quiet", BASE_COMMIT, "--", "project/") == ""
    assert _git("ls-files", "publication/generated", "publication/_book") == ""

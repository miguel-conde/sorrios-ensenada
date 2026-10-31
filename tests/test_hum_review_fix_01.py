from __future__ import annotations

import re
import subprocess
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PUBLICATION = ROOT / "publication"
FIX01_BASE_COMMIT = "550f551f2fc279b5bcc75f013a2b5e8bb4560519"
FIX02_BASE_COMMIT = "26f271b6a45aabf7ecbf461077fefa63d51503c6"
PROLOGUE = "publication/content/00-preliminares/02-prologo.qmd"

PREVIOUS_OPENING = """Hace ya casi veinte años que una parte importante de nuestras vacaciones familiares de verano transcurre en Sorríos. Es el lugar de origen de la familia paterna de mi esposa y, con el paso del tiempo, ha acabado convirtiéndose también para mí en uno de esos lugares a los que uno siente que pertenece un poco, aunque haya llegado a ellos de adulto.

Sorríos - *Sorribos* en el expediente de 1752 - es hoy un pequeño grupo de casas situado al norte de Santibáñez de Ordás, en el municipio leonés de Santa María de Ordás. Son casas recias, construidas con gruesos muros de piedra y la mampostería tradicional de la zona. Sus paredes mantienen el interior fresco durante el verano y lo protegen del frío en invierno. En muchas de ellas, la vivienda ocupaba la parte superior, mientras que la planta baja, más húmeda, se destinaba a los animales, los aperos y las labores propias de una economía agrícola y ganadera.

En una de esas casas empezamos a pasar nuestros veranos. Hoy, gracias también a las posibilidades del teletrabajo, nuestras estancias son a veces bastante más prolongadas. La casa forma parte de un conjunto de construcciones que pertenecieron a miembros de una misma familia: viviendas, pajares y cuadras muy próximos entre sí, reflejo de una forma de vida en la que familia, trabajo y explotación agraria constituían casi una misma realidad."""

APPROVED_OPENING = """Hace ya casi veinte años que una parte importante de nuestras vacaciones familiares de verano transcurre en Sorríos. Es el lugar de origen de la familia paterna de mi esposa, Regina. Con el paso del tiempo, ha acabado convirtiéndose también para mí en uno de esos lugares a los que uno siente que pertenece un poco, aunque haya llegado a ellos de adulto.

Sorríos —*Sorribos* en el expediente de 1752 que constituye el objeto de este libro— es hoy un pequeño grupo de casas situado al norte de Santibáñez de Ordás, en el municipio leonés de Santa María de Ordás. Son casas recias, construidas con gruesos muros de piedra y la mampostería tradicional de la zona. Sus paredes mantienen el interior fresco durante el verano y lo protegen del frío en invierno. En muchas de ellas, la vivienda ocupaba la parte superior, mientras que la planta baja, más húmeda, se destinaba a los animales, los aperos y las labores propias de una economía agrícola y ganadera.

En una de esas casas empezamos a pasar nuestros veranos. Hoy, gracias también a las posibilidades del teletrabajo, nuestras estancias son a veces bastante más prolongadas. La casa forma parte de un conjunto de construcciones que pertenecieron a miembros de una misma familia: viviendas, pajares y cuadras muy próximos entre sí, reflejo de una forma de vida en la que familia, trabajo y explotación agraria constituían casi una misma realidad. Allí nació mi suegro y allí conocí a los tíos de mi mujer, doña Araceli y don José, maestros ambos. Don José es todavía recordado por los mayores del lugar, pues ejerció en las antiguas escuelas de Sorríos, cuyas ruinas aún pueden verse en las lomas de «Los Cogurutines», que marcan por el norte el límite de la localidad."""


def _git(*arguments: str) -> str:
    return subprocess.run(
        ["git", *arguments],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout


def test_prologue_changes_only_the_authorized_human_review_passages():
    before_fix01 = _git("show", f"{FIX01_BASE_COMMIT}:{PROLOGUE}")
    before_fix02 = _git("show", f"{FIX02_BASE_COMMIT}:{PROLOGUE}")
    current = (ROOT / PROLOGUE).read_text(encoding="utf-8")
    old = "La primera vez que conocí Sorríos, poco después de casarnos en 1994,"
    new = "Cuando conocí Sorríos, poco después de casarnos en 1994,"
    assert before_fix01.count(old) == 1
    assert before_fix02 == before_fix01.replace(old, new, 1)
    assert before_fix02.count(PREVIOUS_OPENING) == 1
    expected = before_fix02.replace(PREVIOUS_OPENING, APPROVED_OPENING, 1)
    expected = expected.replace("Sorríos, 2026", "Madrid, octubre de 2026", 1)
    assert current == expected
    assert old not in current
    assert new in current
    assert PREVIOUS_OPENING not in current
    assert current.count(APPROVED_OPENING) == 1


def test_author_label_override_is_narrow_and_isbn_is_not_pending():
    language = yaml.safe_load(
        (PUBLICATION / "_language.yml").read_text(encoding="utf-8")
    )
    assert language == {"title-block-author-single": "Autor"}
    metadata = yaml.safe_load(
        (PUBLICATION / "meta/publication.yml").read_text(encoding="utf-8")
    )["publication"]
    assert metadata["date"] == "2026-11-01"
    assert metadata["pending"] == {"at_release": []}
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
    assert _git("diff", "--quiet", FIX01_BASE_COMMIT, "--", "project/") == ""
    assert _git("ls-files", "publication/generated", "publication/_book") == ""

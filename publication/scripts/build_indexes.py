#!/usr/bin/env python3
"""Generate the nine reproducible Phase 5A index views."""

from __future__ import annotations

import re
from dataclasses import dataclass
from itertools import zip_longest
from pathlib import Path

from critical_edition import UnitSpec, load_unit_specs
from index_sources import (
    EditorialIndex,
    IndexSourceError,
    LiveIndex,
    Locator,
    load_editorial_indexes,
    load_live_indexes,
    response_index_entries,
    slug,
    sort_key,
    unit_locator,
)
from modernized_edition import ModernizedEdition, load_modernized_edition


UNITS_SOURCE = Path("project/00_CONTROL/unidades.yaml")
MODERNIZED_SOURCE = Path(
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/"
    "Catastro_Sorrios_1752_Version_Modernizada.md"
)
INDEX_METADATA_SOURCE = Path("publication/meta/indexes.yml")
OUTPUT_NAMES = (
    "01-indice-onomastico.qmd",
    "02-indice-toponimos.qmd",
    "03-indice-instituciones.qmd",
    "04-indice-oficios.qmd",
    "05-indice-medidas.qmd",
    "06-indice-productos-recursos.qmd",
    "07-indice-cargas-fiscalidad.qmd",
    "08-indice-preguntas-respuestas.qmd",
    "09-indice-materias.qmd",
)
INDEX_TITLES = {
    "onomastico": "Índice onomástico",
    "toponimos": "Índice de lugares y topónimos",
    "instituciones": "Índice de instituciones, jurisdicciones y entidades",
    "oficios": "Índice de oficios, cargos y condiciones",
    "medidas": "Índice de medidas, monedas y unidades",
    "productos-recursos": "Índice de productos, cultivos, ganados y recursos",
    "cargas-fiscalidad": "Índice de cargas, derechos, rentas y fiscalidad",
    "preguntas-respuestas": "Índice de preguntas y respuestas",
    "materias": "Índice de materias",
}
LIVE_ORDER = ("onomastico", "toponimos", "instituciones", "oficios", "medidas")
DISPLAY_FIELDS = {
    "onomastico": (
        ("Nombre original", "Forma documental"),
        ("Variantes", "Variantes documentales"),
        ("Cargo u oficio", "Cargo u oficio"),
        ("Identificación histórica", "Identificación histórica"),
        ("Grado de seguridad", "Grado de seguridad"),
    ),
    "toponimos": (
        ("Forma original", "Forma documental"),
        ("Forma moderna", "Forma moderna"),
        ("Grado de seguridad", "Grado de seguridad"),
    ),
    "instituciones": (
        ("Forma original", "Forma documental"),
        ("Variantes", "Variantes documentales"),
        ("Clase de institución", "Clase"),
        ("Identificación histórica", "Identificación histórica"),
    ),
    "oficios": (
        ("Forma original", "Forma documental"),
        ("Variantes", "Variantes documentales"),
        ("Forma normalizada", "Forma normalizada"),
        ("Personas o instituciones relacionadas", "Personas o instituciones relacionadas"),
    ),
    "medidas": (
        ("Forma original", "Forma documental"),
        ("Variantes", "Variantes documentales"),
        ("Clase de medida", "Clase"),
        ("Equivalencia histórica o moderna", "Equivalencia documentada"),
    ),
}
CATEGORY_LABELS = {
    "cultivo": "cultivo",
    "producto": "producto",
    "animal": "animal",
    "recurso-natural": "recurso natural",
    "infraestructura-productiva": "infraestructura productiva",
    "carga-fiscal": "carga fiscal",
    "obligacion-eclesiastica": "obligación eclesiástica",
    "derecho": "derecho",
    "renta": "renta",
    "utilidad": "utilidad",
    "pago": "pago",
    "gasto": "gasto",
    "recurso-concejil": "recurso concejil",
    "mecanismo-financiacion": "mecanismo de financiación",
    "materia": "materia",
}


class IndexBuildError(RuntimeError):
    """Report an actionable Phase 5A generation or fidelity failure."""


@dataclass(frozen=True)
class IndexData:
    specs: tuple[UnitSpec, ...]
    live: tuple[LiveIndex, ...]
    editorial: tuple[EditorialIndex, ...]
    modernized: ModernizedEdition


def load_index_data(repository_root: Path, publication_root: Path) -> IndexData:
    try:
        specs = load_unit_specs(repository_root / UNITS_SOURCE)
        live = load_live_indexes(repository_root, specs)
        modernized = load_modernized_edition(repository_root / MODERNIZED_SOURCE)
        editorial = load_editorial_indexes(
            publication_root,
            specs=specs,
            modernized=modernized,
        )
        response_index_entries(modernized)
    except IndexSourceError as exc:
        raise IndexBuildError(str(exc)) from exc
    return IndexData(specs, live, editorial, modernized)


def _header(
    title: str,
    chapter_id: str,
    sources: tuple[str, ...],
    *,
    alphabetical: bool = True,
) -> str:
    source_lines = "\n".join(f"  - {source}" for source in sources)
    ordering = (
        "Las entradas se ordenan mediante una clave Unicode determinista: se aplican\n"
        "`casefold` y descomposición NFKD, se omiten tildes y signos solo en la clave y\n"
        "se conservan en pantalla la grafía canónica, las abreviaturas y las partículas\n"
        "en su posición. Las variantes no duplican localizadores."
        if alphabetical
        else "Las entradas siguen el orden numérico validado del interrogatorio."
    )
    return f'''---
subtitle: "Parte VI. Aparatos e índices"
chapter-id: {chapter_id}
publication-status: generated
numbered: false
number-sections: false
sources:
{source_lines}
---

# {title} {{.unnumbered}}

{ordering}
'''


def _locator_blocks(locators: tuple[Locator, ...]) -> str:
    unique = tuple(dict.fromkeys(locators))
    html = "; ".join(f"[{item.label}]({item.html_path})" for item in unique)
    pdf_parts: list[str] = []
    for position, item in enumerate(unique):
        link = rf"\hyperref[{item.anchor}]{{\pageref*{{{item.anchor}}}}}"
        if position == 0:
            pdf_parts.append(link)
            continue
        comparisons = "".join(
            rf"\ifnum\getpagerefnumber{{{item.anchor}}}=\getpagerefnumber{{{previous.anchor}}}\relax"
            rf"\else"
            for previous in unique[:position]
        )
        closings = r"\fi" * position
        pdf_parts.append(comparisons + ", " + link + closings)
    pdf = "".join(pdf_parts)
    return f'''::: {{.content-visible when-format="html"}}
**Localizadores:** {html}
:::

::: {{.content-visible when-format="pdf"}}
**Páginas:** `{pdf}`{{=latex}}
:::'''


def _entry_div(index_id: str, entry_id: str, term: str, body: tuple[str, ...]) -> str:
    content = "\n\n".join(part for part in body if part)
    return f'''::: {{#indice-{index_id}-{entry_id} .index-entry}}
**{term}**

{content}
:::'''


def _alphabetized_blocks(
    index_id: str, entries: tuple[tuple[str, str, tuple[str, ...]], ...]
) -> str:
    chunks: list[str] = []
    current_letter = None
    for entry_id, term, body in sorted(entries, key=lambda item: sort_key(item[1])):
        letter = sort_key(term)[:1].upper() or "#"
        if letter != current_letter:
            current_letter = letter
            chunks.append(f"## {letter} {{#indice-{index_id}-letra-{slug(letter)} .unnumbered}}")
        chunks.append(_entry_div(index_id, entry_id, term, body))
    return "\n\n".join(chunks)


def live_index_qmd(index: LiveIndex, specs: tuple[UnitSpec, ...]) -> str:
    by_label = {spec.label: spec for spec in specs}
    entries: list[tuple[str, str, tuple[str, ...]]] = []
    for entry in index.entries:
        details = tuple(
            f"**{visible}:** {entry.fields[field]}"
            for field, visible in DISPLAY_FIELDS[index.index_id]
            if field in entry.fields
        )
        locators = tuple(unit_locator(by_label[label]) for label in entry.units)
        entries.append(
            (
                slug(entry.term),
                entry.term,
                (*details, _locator_blocks(locators)),
            )
        )
    return (
        _header(
            INDEX_TITLES[index.index_id],
            f"indice-{index.index_id}",
            (index.source.as_posix(),),
        )
        + "\n"
        + _alphabetized_blocks(index.index_id, tuple(entries))
        + "\n"
    )


def editorial_index_qmd(index: EditorialIndex) -> str:
    by_id = {entry.entry_id: entry for entry in index.entries}
    entries: list[tuple[str, str, tuple[str, ...]]] = []
    for entry in index.entries:
        details: list[str] = [f"**Categoría:** {CATEGORY_LABELS[entry.category]}"]
        if entry.variants:
            details.append("**Variantes:** " + "; ".join(entry.variants))
        if entry.see:
            details.append(
                "**Véase:** "
                + "; ".join(
                    f"[{by_id[target].term}](#indice-{index.index_id}-{target})"
                    for target in entry.see
                )
            )
        if entry.see_also:
            details.append(
                "**Véase también:** "
                + "; ".join(
                    f"[{by_id[target].term}](#indice-{index.index_id}-{target})"
                    for target in entry.see_also
                )
            )
        details.append(_locator_blocks(entry.targets))
        entries.append((entry.entry_id, entry.term, tuple(details)))
    return (
        _header(
            INDEX_TITLES[index.index_id],
            f"indice-{index.index_id}",
            (INDEX_METADATA_SOURCE.as_posix(),),
        )
        + "\n"
        + _alphabetized_blocks(index.index_id, tuple(entries))
        + "\n"
    )


def response_index_qmd(edition: ModernizedEdition) -> str:
    chunks = [
        _header(
            INDEX_TITLES["preguntas-respuestas"],
            "indice-preguntas-respuestas",
            (MODERNIZED_SOURCE.as_posix(),),
            alphabetical=False,
        ),
        "Las cuarenta entradas siguen el orden del interrogatorio validado; no forman una lista manual paralela.",
    ]
    for term, locator in response_index_entries(edition):
        chunks.append(
            _entry_div(
                "preguntas-respuestas",
                locator.key,
                term,
                (_locator_blocks((locator,)),),
            )
        )
    return "\n\n".join(chunks).rstrip() + "\n"


def generated_indexes(data: IndexData) -> dict[str, str]:
    live_by_id = {index.index_id: index for index in data.live}
    editorial_by_id = {index.index_id: index for index in data.editorial}
    return {
        OUTPUT_NAMES[0]: live_index_qmd(live_by_id["onomastico"], data.specs),
        OUTPUT_NAMES[1]: live_index_qmd(live_by_id["toponimos"], data.specs),
        OUTPUT_NAMES[2]: live_index_qmd(live_by_id["instituciones"], data.specs),
        OUTPUT_NAMES[3]: live_index_qmd(live_by_id["oficios"], data.specs),
        OUTPUT_NAMES[4]: live_index_qmd(live_by_id["medidas"], data.specs),
        OUTPUT_NAMES[5]: editorial_index_qmd(editorial_by_id["productos-recursos"]),
        OUTPUT_NAMES[6]: editorial_index_qmd(editorial_by_id["cargas-fiscalidad"]),
        OUTPUT_NAMES[7]: response_index_qmd(data.modernized),
        OUTPUT_NAMES[8]: editorial_index_qmd(editorial_by_id["materias"]),
    }


def _difference_context(expected: str, actual: str) -> tuple[int, str]:
    context = "documento"
    for number, (wanted, found) in enumerate(
        zip_longest(expected.splitlines(), actual.splitlines(), fillvalue=""), start=1
    ):
        if wanted.startswith("**"):
            context = wanted.split("**", 2)[1]
        if wanted != found:
            return number, context
    return 0, context


def validate_index_fidelity(data: IndexData, actual: dict[str, str]) -> None:
    expected = generated_indexes(data)
    if set(actual) != set(expected):
        raise IndexBuildError("Salidas 5A incorrectas: " + ", ".join(sorted(actual)))
    for name in OUTPUT_NAMES:
        if actual[name] != expected[name]:
            line, context = _difference_context(expected[name], actual[name])
            raise IndexBuildError(
                f"{name}, {context}: discordancia con la fuente en la línea {line}."
            )


def index_entry_counts(data: IndexData) -> tuple[int, ...]:
    live = {index.index_id: len(index.entries) for index in data.live}
    editorial = {index.index_id: len(index.entries) for index in data.editorial}
    return (
        *(live[index_id] for index_id in LIVE_ORDER),
        editorial["productos-recursos"],
        editorial["cargas-fiscalidad"],
        len(response_index_entries(data.modernized)),
        editorial["materias"],
    )


def _write_qmd(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8", newline="\n")
    temporary.replace(path)


def build_indexes(repository_root: Path, publication_root: Path) -> tuple[Path, ...]:
    """Rebuild only the nine QMD files owned by the Phase 5A generator."""

    data = load_index_data(repository_root.resolve(), publication_root.resolve())
    contents = generated_indexes(data)
    validate_index_fidelity(data, contents)
    generated_root = (publication_root / "generated" / "indices").resolve()
    outputs = tuple(generated_root / name for name in OUTPUT_NAMES)
    if any(path.parent != generated_root for path in outputs):
        raise IndexBuildError("Ruta de salida 5A insegura.")
    for path in outputs:
        _write_qmd(path, contents[path.name])
    return outputs


__all__ = [
    "INDEX_TITLES",
    "IndexBuildError",
    "IndexData",
    "OUTPUT_NAMES",
    "build_indexes",
    "editorial_index_qmd",
    "generated_indexes",
    "index_entry_counts",
    "live_index_qmd",
    "load_index_data",
    "response_index_qmd",
    "validate_index_fidelity",
]

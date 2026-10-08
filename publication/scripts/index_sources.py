#!/usr/bin/env python3
"""Parse and validate the structured sources used by Phase 5A indexes."""

from __future__ import annotations

import posixpath
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

import yaml

from critical_edition import UnitSpec, published_unit_anchor
from modernized_edition import ModernizedEdition


LIVE_INDEX_SOURCES = {
    "onomastico": Path("project/20_TRABAJO_EDITORIAL/INDICES/Indice_Personas.md"),
    "toponimos": Path("project/20_TRABAJO_EDITORIAL/INDICES/Indice_Toponimos.md"),
    "instituciones": Path("project/20_TRABAJO_EDITORIAL/INDICES/Indice_Instituciones.md"),
    "oficios": Path("project/20_TRABAJO_EDITORIAL/INDICES/Indice_Oficios.md"),
    "medidas": Path("project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md"),
}
EDITORIAL_INDEX_IDS = ("productos-recursos", "cargas-fiscalidad", "materias")
EDITORIAL_INDEX_ORDERS = {
    "productos-recursos": 6,
    "cargas-fiscalidad": 7,
    "materias": 9,
}
ALLOWED_CATEGORIES = {
    "productos-recursos": frozenset(
        {"cultivo", "producto", "animal", "recurso-natural", "infraestructura-productiva"}
    ),
    "cargas-fiscalidad": frozenset(
        {
            "carga-fiscal",
            "obligacion-eclesiastica",
            "derecho",
            "renta",
            "utilidad",
            "pago",
            "gasto",
            "recurso-concejil",
            "mecanismo-financiacion",
        }
    ),
    "materias": frozenset({"materia"}),
}
LIVE_INDEX_FIELDS = {
    "onomastico": {
        "required": (
            "Nombre original",
            "Variantes",
            "Cargo u oficio",
            "Unidades",
            "Identificación histórica",
            "Referencias cruzadas",
        ),
        "allowed": frozenset(
            {
                "Nombre original",
                "Variantes",
                "Cargo u oficio",
                "Unidades",
                "Identificación histórica",
                "Grado de seguridad",
                "Referencias cruzadas",
                "Notas",
            }
        ),
    },
    "toponimos": {
        "required": (
            "Forma original",
            "Forma moderna",
            "Localización",
            "Unidades",
            "Fuente de identificación",
            "Grado de seguridad",
            "Referencias cruzadas",
        ),
        "allowed": frozenset(
            {
                "Forma original",
                "Forma moderna",
                "Localización",
                "Unidades",
                "Fuente de identificación",
                "Grado de seguridad",
                "Referencias cruzadas",
            }
        ),
    },
    "instituciones": {
        "required": (
            "Forma original",
            "Variantes",
            "Clase de institución",
            "Unidades",
            "Referencias cruzadas",
        ),
        "allowed": frozenset(
            {
                "Forma original",
                "Variantes",
                "Clase de institución",
                "Unidades",
                "Identificación histórica",
                "Referencias cruzadas",
            }
        ),
    },
    "oficios": {
        "required": (
            "Forma original",
            "Variantes",
            "Forma normalizada",
            "Personas o instituciones relacionadas",
            "Unidades",
            "Notas",
        ),
        "allowed": frozenset(
            {
                "Forma original",
                "Variantes",
                "Forma normalizada",
                "Personas o instituciones relacionadas",
                "Unidades",
                "Notas",
            }
        ),
    },
    "medidas": {
        "required": (
            "Forma original",
            "Variantes",
            "Clase de medida",
            "Equivalencia histórica o moderna",
            "Unidades",
            "Notas y referencias cruzadas",
        ),
        "allowed": frozenset(
            {
                "Forma original",
                "Variantes",
                "Clase de medida",
                "Equivalencia histórica o moderna",
                "Unidades",
                "Notas y referencias cruzadas",
            }
        ),
    },
}


class IndexSourceError(RuntimeError):
    """Report an actionable structural failure in a Phase 5A source."""


@dataclass(frozen=True)
class Locator:
    kind: str
    key: str
    anchor: str
    html_path: str
    label: str


@dataclass(frozen=True)
class LiveIndexEntry:
    term: str
    fields: dict[str, str]
    units: tuple[str, ...]


@dataclass(frozen=True)
class LiveIndex:
    index_id: str
    title: str
    source: Path
    entries: tuple[LiveIndexEntry, ...]


@dataclass(frozen=True)
class EditorialIndexEntry:
    entry_id: str
    term: str
    category: str
    variants: tuple[str, ...]
    see: tuple[str, ...]
    see_also: tuple[str, ...]
    targets: tuple[Locator, ...]


@dataclass(frozen=True)
class EditorialIndex:
    index_id: str
    order: int
    title: str
    entries: tuple[EditorialIndexEntry, ...]


def sort_key(value: str) -> str:
    """Return a locale-independent key while preserving the visible spelling."""

    expanded = value.replace("[", "").replace("]", "")
    normalized = unicodedata.normalize("NFKD", expanded.casefold())
    without_marks = "".join(
        character for character in normalized if not unicodedata.combining(character)
    )
    return re.sub(r"[^a-z0-9]+", " ", without_marks).strip()


def slug(value: str) -> str:
    return sort_key(value).replace(" ", "-")


def _parse_fields(block: str, source: str, term: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in block.splitlines():
        if not line.startswith("- **"):
            continue
        match = re.fullmatch(r"- \*\*(?P<label>[^:]+):\*\*\s*(?P<value>.+)", line)
        if match is None:
            raise IndexSourceError(
                f"{source}, entrada {term!r}: campo de ficha no reconocible: {line!r}."
            )
        label = match.group("label").strip()
        value = match.group("value").strip()
        if label in fields:
            raise IndexSourceError(
                f"{source}, entrada {term!r}: campo duplicado {label!r}."
            )
        fields[label] = value
    return fields


def parse_live_index(
    text: str,
    index_id: str,
    unit_labels: tuple[str, ...],
    *,
    source: str,
) -> LiveIndex:
    """Parse one canonical live index without deriving entries from book text."""

    if index_id not in LIVE_INDEX_FIELDS:
        raise IndexSourceError(f"Índice vivo no reconocido: {index_id}.")
    title_match = re.search(r"^# (?P<title>[^\n]+)$", text, re.MULTILINE)
    if title_match is None:
        raise IndexSourceError(f"{source}: falta el título H1.")
    marker = "## Entradas"
    if text.count(marker) != 1:
        raise IndexSourceError(f"{source}: debe existir un único bloque «Entradas».")
    region = text.split(marker, 1)[1]
    matches = list(re.finditer(r"^### (?P<term>[^\n]+)\s*$", region, re.MULTILINE))
    if not matches:
        raise IndexSourceError(f"{source}: el bloque «Entradas» está vacío.")
    known_units = {label.casefold(): label for label in unit_labels}
    contract = LIVE_INDEX_FIELDS[index_id]
    entries: list[LiveIndexEntry] = []
    for position, match in enumerate(matches):
        term = match.group("term").strip()
        end = matches[position + 1].start() if position + 1 < len(matches) else len(region)
        fields = _parse_fields(region[match.end():end], source, term)
        missing = [field for field in contract["required"] if field not in fields]
        unknown = [field for field in fields if field not in contract["allowed"]]
        if missing or unknown:
            details = []
            if missing:
                details.append("faltan " + ", ".join(missing))
            if unknown:
                details.append("campos desconocidos " + ", ".join(unknown))
            raise IndexSourceError(f"{source}, entrada {term!r}: {'; '.join(details)}.")
        if any(not value for value in fields.values()):
            raise IndexSourceError(f"{source}, entrada {term!r}: hay un campo vacío.")
        unit_value = fields["Unidades"].rstrip(".")
        units = tuple(item.strip() for item in unit_value.split(";") if item.strip())
        if not units or len(units) != len(set(units)):
            raise IndexSourceError(
                f"{source}, entrada {term!r}: las unidades deben existir y ser únicas."
            )
        missing_units = [unit for unit in units if unit.casefold() not in known_units]
        if missing_units:
            raise IndexSourceError(
                f"{source}, entrada {term!r}: unidades inexistentes: "
                + ", ".join(missing_units)
                + "."
            )
        entries.append(
            LiveIndexEntry(
                term,
                fields,
                tuple(known_units[unit.casefold()] for unit in units),
            )
        )
    folded = [entry.term.casefold() for entry in entries]
    duplicates = sorted({term for term in folded if folded.count(term) > 1})
    if duplicates:
        raise IndexSourceError(f"{source}: entradas duplicadas: {', '.join(duplicates)}.")
    return LiveIndex(
        index_id=index_id,
        title=title_match.group("title").strip(),
        source=LIVE_INDEX_SOURCES[index_id],
        entries=tuple(entries),
    )


def load_live_indexes(
    repository_root: Path, specs: tuple[UnitSpec, ...]
) -> tuple[LiveIndex, ...]:
    unit_labels = tuple(spec.label for spec in specs)
    indexes: list[LiveIndex] = []
    for index_id, relative in LIVE_INDEX_SOURCES.items():
        path = repository_root / relative
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            raise IndexSourceError(f"No se pudo leer {path}: {exc}") from exc
        indexes.append(parse_live_index(text, index_id, unit_labels, source=relative.as_posix()))
    return tuple(indexes)


def unit_locator(spec: UnitSpec) -> Locator:
    return Locator(
        kind="unit",
        key=spec.unit_id,
        anchor=published_unit_anchor(spec),
        html_path=f"../15-transcripcion.qmd#{published_unit_anchor(spec)}",
        label=spec.label,
    )


def response_locator(number: int, title: str) -> Locator:
    return Locator(
        kind="response",
        key=str(number),
        anchor=f"respuesta-{number}",
        html_path=f"../16-edicion-modernizada.qmd#respuesta-{number}",
        label=f"Respuesta {number}: {title}",
    )


def _front_matter(text: str, source: Path) -> dict:
    if not text.startswith("---\n"):
        raise IndexSourceError(f"{source}: falta el front matter.")
    closing = text.find("\n---\n", 4)
    if closing < 0:
        raise IndexSourceError(f"{source}: front matter incompleto.")
    try:
        data = yaml.safe_load(text[4:closing])
    except yaml.YAMLError as exc:
        raise IndexSourceError(f"{source}: front matter inválido: {exc}") from exc
    if not isinstance(data, dict):
        raise IndexSourceError(f"{source}: el front matter debe ser un mapa.")
    return data


def _section_anchors(path: Path) -> dict[str, str]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise IndexSourceError(f"No se pudo leer {path}: {exc}") from exc
    anchors: dict[str, str] = {}
    for match in re.finditer(
        r"^#{1,6}\s+(?P<title>.+?)\s+\{#(?P<anchor>[a-z0-9-]+)(?:\s+[^}]*)?\}\s*$",
        text,
        re.MULTILINE,
    ):
        anchor = match.group("anchor")
        title = re.sub(r"\s+\{.*$", "", match.group("title")).strip()
        if anchor in anchors:
            raise IndexSourceError(f"{path}: ancla duplicada {anchor}.")
        anchors[anchor] = title
    return anchors


def _chapter_map(publication_root: Path) -> dict[str, Path]:
    path = publication_root / "meta" / "chapters.yml"
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        raise IndexSourceError(f"No se pudo leer {path}: {exc}") from exc
    chapters = data.get("chapters") if isinstance(data, dict) else None
    if not isinstance(chapters, list):
        raise IndexSourceError("chapters.yml no declara una lista chapters.")
    mapping: dict[str, Path] = {}
    for raw in chapters:
        if not isinstance(raw, dict) or not raw.get("chapter_id") or not raw.get("path"):
            raise IndexSourceError("chapters.yml contiene una entrada incompleta.")
        chapter_id = str(raw["chapter_id"])
        relative = PurePosixPath(str(raw["path"]))
        if relative.is_absolute() or ".." in relative.parts:
            raise IndexSourceError(f"Ruta insegura en chapters.yml: {relative}.")
        mapping[chapter_id] = publication_root.joinpath(*relative.parts)
    return mapping


def _string_tuple(raw: object, label: str, entry_id: str) -> tuple[str, ...]:
    if raw is None:
        return ()
    if not isinstance(raw, list) or any(not isinstance(item, str) or not item for item in raw):
        raise IndexSourceError(f"{entry_id}: {label} debe ser una lista de textos.")
    values = tuple(raw)
    if len(values) != len(set(value.casefold() for value in values)):
        raise IndexSourceError(f"{entry_id}: {label} contiene duplicados.")
    return values


def _section_locator(
    publication_root: Path,
    chapter_paths: dict[str, Path],
    raw: dict,
    entry_id: str,
) -> Locator:
    if set(raw) != {"type", "chapter", "anchor"}:
        raise IndexSourceError(
            f"{entry_id}: cada destino section debe declarar solo type, chapter y anchor."
        )
    chapter_id = str(raw["chapter"])
    anchor = str(raw["anchor"])
    path = chapter_paths.get(chapter_id)
    if path is None:
        raise IndexSourceError(f"{entry_id}: capítulo inexistente {chapter_id!r}.")
    if not path.is_file():
        raise IndexSourceError(f"{entry_id}: falta el capítulo de destino {path}.")
    anchors = _section_anchors(path)
    if anchor not in anchors:
        raise IndexSourceError(
            f"{entry_id}: ancla inexistente {anchor!r} en el capítulo {chapter_id}."
        )
    index_directory = PurePosixPath("generated/indices")
    chapter_relative = path.relative_to(publication_root).as_posix()
    html_path = posixpath.relpath(chapter_relative, index_directory.as_posix())
    front = _front_matter(path.read_text(encoding="utf-8"), path)
    title = str(front.get("title", chapter_id)).replace(" {.unnumbered}", "")
    return Locator(
        kind="section",
        key=f"{chapter_id}:{anchor}",
        anchor=anchor,
        html_path=f"{html_path}#{anchor}",
        label=f"{title}: {anchors[anchor]}",
    )


def _structured_locator(
    publication_root: Path,
    chapter_paths: dict[str, Path],
    raw: dict,
    entry_id: str,
    specs: tuple[UnitSpec, ...],
    modernized: ModernizedEdition | None,
) -> Locator:
    target_type = raw.get("type")
    if target_type == "section":
        return _section_locator(publication_root, chapter_paths, raw, entry_id)
    if target_type == "unit":
        if set(raw) != {"type", "unit"}:
            raise IndexSourceError(
                f"{entry_id}: cada destino unit debe declarar solo type y unit."
            )
        unit_id = str(raw["unit"])
        by_id = {spec.unit_id: spec for spec in specs}
        if unit_id not in by_id:
            raise IndexSourceError(f"{entry_id}: unidad inexistente {unit_id!r}.")
        return unit_locator(by_id[unit_id])
    if target_type == "response":
        if set(raw) != {"type", "response"}:
            raise IndexSourceError(
                f"{entry_id}: cada destino response debe declarar solo type y response."
            )
        number = raw["response"]
        if isinstance(number, bool) or not isinstance(number, int):
            raise IndexSourceError(f"{entry_id}: response debe ser un entero.")
        responses = {
            response.number: response
            for response in (() if modernized is None else modernized.responses)
        }
        if number not in responses:
            raise IndexSourceError(f"{entry_id}: respuesta inexistente {number!r}.")
        response = responses[number]
        return response_locator(response.number, response.title)
    raise IndexSourceError(
        f"{entry_id}: tipo de destino no válido {target_type!r}; "
        "se admiten section, unit y response."
    )


def load_editorial_indexes(
    publication_root: Path,
    *,
    source: Path | None = None,
    specs: tuple[UnitSpec, ...] = (),
    modernized: ModernizedEdition | None = None,
) -> tuple[EditorialIndex, ...]:
    """Validate indexes.yml and resolve every target against an explicit anchor."""

    path = source or publication_root / "meta" / "indexes.yml"
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        raise IndexSourceError(f"No se pudo leer {path}: {exc}") from exc
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise IndexSourceError("indexes.yml debe declarar schema_version: 1.")
    raw_indexes = data.get("indexes")
    if not isinstance(raw_indexes, list):
        raise IndexSourceError("indexes.yml debe declarar una lista indexes.")
    ids = [item.get("id") for item in raw_indexes if isinstance(item, dict)]
    if tuple(ids) != EDITORIAL_INDEX_IDS:
        raise IndexSourceError(
            "indexes.yml debe declarar, en orden, solo los índices editoriales 6, 7 y 9."
        )
    chapter_paths = _chapter_map(publication_root)
    indexes: list[EditorialIndex] = []
    forbidden_page_key = re.compile(r"(?:^|_)(?:pdf_?)?pages?(?:$|_)", re.I)
    for raw_index in raw_indexes:
        if not isinstance(raw_index, dict):
            raise IndexSourceError("Cada índice editorial debe ser un mapa.")
        index_id = str(raw_index["id"])
        order = raw_index.get("order")
        title = raw_index.get("title")
        entries_raw = raw_index.get("entries")
        if order != EDITORIAL_INDEX_ORDERS[index_id] or not isinstance(title, str):
            raise IndexSourceError(f"{index_id}: order o title inválidos.")
        if not isinstance(entries_raw, list) or not entries_raw:
            raise IndexSourceError(f"{index_id}: entries debe ser una lista no vacía.")
        entries: list[EditorialIndexEntry] = []
        for raw_entry in entries_raw:
            if not isinstance(raw_entry, dict):
                raise IndexSourceError(f"{index_id}: entrada no válida.")
            forbidden = [key for key in raw_entry if forbidden_page_key.search(str(key))]
            if forbidden:
                raise IndexSourceError(
                    f"{index_id}: no se permiten páginas PDF manuales ({', '.join(forbidden)})."
                )
            entry_id = str(raw_entry.get("id", ""))
            term = raw_entry.get("term")
            category = raw_entry.get("category")
            if not re.fullmatch(r"[a-z0-9-]+", entry_id):
                raise IndexSourceError(f"{index_id}: id de entrada inválido {entry_id!r}.")
            if not isinstance(term, str) or not term:
                raise IndexSourceError(f"{entry_id}: falta el término canónico.")
            if category not in ALLOWED_CATEGORIES[index_id]:
                raise IndexSourceError(
                    f"{entry_id}: categoría no válida {category!r} para {index_id}."
                )
            targets_raw = raw_entry.get("targets")
            if not isinstance(targets_raw, list) or not targets_raw:
                raise IndexSourceError(f"{entry_id}: debe declarar destinos estructurados.")
            targets: list[Locator] = []
            for target in targets_raw:
                if not isinstance(target, dict):
                    raise IndexSourceError(f"{entry_id}: destino estructurado no válido.")
                targets.append(
                    _structured_locator(
                        publication_root,
                        chapter_paths,
                        target,
                        entry_id,
                        specs,
                        modernized,
                    )
                )
            if len({target.key for target in targets}) != len(targets):
                raise IndexSourceError(f"{entry_id}: contiene destinos duplicados.")
            entries.append(
                EditorialIndexEntry(
                    entry_id=entry_id,
                    term=term,
                    category=str(category),
                    variants=_string_tuple(raw_entry.get("variants"), "variants", entry_id),
                    see=_string_tuple(raw_entry.get("see"), "see", entry_id),
                    see_also=_string_tuple(raw_entry.get("see_also"), "see_also", entry_id),
                    targets=tuple(targets),
                )
            )
        entry_ids = [entry.entry_id for entry in entries]
        terms = [entry.term.casefold() for entry in entries]
        if len(entry_ids) != len(set(entry_ids)):
            raise IndexSourceError(f"{index_id}: ids de entrada duplicados.")
        if len(terms) != len(set(terms)):
            raise IndexSourceError(f"{index_id}: términos duplicados.")
        known = set(entry_ids)
        for entry in entries:
            missing = sorted(set(entry.see + entry.see_also) - known)
            if missing:
                raise IndexSourceError(
                    f"{index_id}, {entry.entry_id}: remisiones inexistentes: "
                    + ", ".join(missing)
                    + "."
                )
            if entry.entry_id in entry.see + entry.see_also:
                raise IndexSourceError(
                    f"{index_id}, {entry.entry_id}: una entrada no puede remitirse a sí misma."
                )
        indexes.append(EditorialIndex(index_id, int(order), title, tuple(entries)))
    return tuple(indexes)


def response_index_entries(edition: ModernizedEdition) -> tuple[tuple[str, Locator], ...]:
    if tuple(response.number for response in edition.responses) != tuple(range(1, 41)):
        raise IndexSourceError("El índice 8 exige exactamente las respuestas 1–40.")
    return tuple(
        (
            f"Pregunta/Respuesta {response.number} — {response.title}",
            response_locator(response.number, response.title),
        )
        for response in edition.responses
    )


def resolve_pdf_pages(
    locators: tuple[Locator, ...], page_by_anchor: dict[str, str]
) -> tuple[str, ...]:
    """Resolve locator pages from a renderer-produced label map for verification."""

    pages: list[str] = []
    for locator in locators:
        page = page_by_anchor.get(locator.anchor)
        if page is None:
            raise IndexSourceError(
                f"El render PDF no produjo página para el destino {locator.key} "
                f"(ancla {locator.anchor})."
            )
        if page not in pages:
            pages.append(page)
    return tuple(pages)


__all__ = [
    "ALLOWED_CATEGORIES",
    "EDITORIAL_INDEX_IDS",
    "EditorialIndex",
    "EditorialIndexEntry",
    "IndexSourceError",
    "LIVE_INDEX_SOURCES",
    "LiveIndex",
    "LiveIndexEntry",
    "Locator",
    "load_editorial_indexes",
    "load_live_indexes",
    "parse_live_index",
    "response_index_entries",
    "resolve_pdf_pages",
    "slug",
    "sort_key",
    "unit_locator",
]

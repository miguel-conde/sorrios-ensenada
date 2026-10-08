#!/usr/bin/env python3
"""Parse the canonical glossary and evidence register used by Phase 4D."""

from __future__ import annotations

import hashlib
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path


REGISTER_VERSION = "1.2"
GLOSSARY_FIELDS = (
    "Término documentado",
    "Definición",
    "Primera unidad",
    "Referencias",
    "Notas",
)
ALLOWED_LEVELS = frozenset({"D", "C", "I", "E", "L"})
RECOGNIZED_STATES = ("Admitida", "Condicionada", "Excluida", "Mantener cautela")


class ApparatusSourceError(RuntimeError):
    """Report an actionable structural failure in a Phase 4D source."""


@dataclass(frozen=True)
class GlossaryEntry:
    term: str
    documented_term: str
    definition: str
    first_unit: str
    references: str
    notes: str

    @property
    def anchor(self) -> str:
        normalized = unicodedata.normalize("NFKD", self.term)
        ascii_term = "".join(char for char in normalized if not unicodedata.combining(char))
        slug = re.sub(r"[^a-z0-9]+", "-", ascii_term.casefold()).strip("-")
        return f"glosario-{slug}"


@dataclass(frozen=True)
class Glossary:
    title: str
    version: str | None
    entries: tuple[GlossaryEntry, ...]


@dataclass(frozen=True)
class EvidenceEntry:
    identifier: str
    statement: str
    level: str
    evidence: str
    status_caution: str
    section: str

    @property
    def level_components(self) -> tuple[str, ...]:
        return tuple(self.level.split("/"))

    @property
    def state(self) -> str | None:
        return next(
            (state for state in RECOGNIZED_STATES if self.status_caution.startswith(state)),
            None,
        )


@dataclass(frozen=True)
class Calculation:
    identifier: str
    operation: str
    result: str
    inputs: str
    condition: str


@dataclass(frozen=True)
class EvidenceRegister:
    version: str
    entries: tuple[EvidenceEntry, ...]
    calculations: tuple[Calculation, ...]

    @property
    def calculation_map(self) -> dict[str, Calculation]:
        return {calculation.identifier: calculation for calculation in self.calculations}

    @property
    def calculated_entries(self) -> tuple[EvidenceEntry, ...]:
        return tuple(entry for entry in self.entries if entry.level == "C")

    def associated_calculations(self, entry: EvidenceEntry) -> tuple[Calculation, ...]:
        identifiers = tuple(re.findall(r"CAL-\d{3}", entry.evidence))
        calculations = self.calculation_map
        return tuple(calculations[identifier] for identifier in identifiers)


def git_blob_oid(data: bytes) -> str:
    """Return the Git blob identifier without invoking Git."""

    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def _version(text: str) -> str | None:
    match = re.search(r"^\*\*Versión:\*\*\s*(\S+)\s*$", text, re.MULTILINE)
    return match.group(1) if match else None


def parse_glossary(text: str, *, source: str = "Glosario.md") -> Glossary:
    """Parse all canonical glossary entries without rewriting any field."""

    title_match = re.search(r"^# (?P<title>[^\n]+)$", text, re.MULTILINE)
    if title_match is None:
        raise ApparatusSourceError(f"{source}: falta el título H1 del Glosario.")
    marker = "## Entradas"
    if text.count(marker) != 1:
        raise ApparatusSourceError(
            f"{source}: debe existir un único bloque «Entradas» del Glosario."
        )
    region = text.split(marker, 1)[1]
    matches = list(re.finditer(r"^### (?P<term>[^\n]+)\s*$", region, re.MULTILINE))
    if not matches:
        raise ApparatusSourceError(f"{source}: el bloque de entradas está vacío.")
    entries: list[GlossaryEntry] = []
    for index, match in enumerate(matches):
        term = match.group("term").strip()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(region)
        block = region[match.end():end].strip("\n")
        fields = re.findall(
            r"^- \*\*(?P<label>[^:]+):\*\*\s*(?P<value>.+)$",
            block,
            re.MULTILINE,
        )
        labels = tuple(label.strip() for label, _ in fields)
        if labels != GLOSSARY_FIELDS:
            raise ApparatusSourceError(
                f"{source}, entrada {term!r}: campos {labels or 'ausentes'}; "
                f"se exigen {GLOSSARY_FIELDS}."
            )
        values = {label.strip(): value.strip() for label, value in fields}
        empty = [label for label, value in values.items() if not value]
        if empty:
            raise ApparatusSourceError(
                f"{source}, entrada {term!r}: campo vacío {empty[0]!r}."
            )
        entries.append(
            GlossaryEntry(
                term=term,
                documented_term=values["Término documentado"],
                definition=values["Definición"],
                first_unit=values["Primera unidad"],
                references=values["Referencias"],
                notes=values["Notas"],
            )
        )
    folded = [entry.term.casefold() for entry in entries]
    duplicates = sorted({term for term in folded if folded.count(term) > 1})
    if duplicates:
        raise ApparatusSourceError(
            f"{source}: términos duplicados: {', '.join(duplicates)}."
        )
    anchors = [entry.anchor for entry in entries]
    if len(anchors) != len(set(anchors)):
        raise ApparatusSourceError(f"{source}: dos términos producen la misma ancla.")
    return Glossary(title_match.group("title").strip(), _version(text), tuple(entries))


def load_glossary(path: Path) -> Glossary:
    try:
        return parse_glossary(path.read_text(encoding="utf-8"), source=str(path))
    except (OSError, UnicodeError) as exc:
        raise ApparatusSourceError(f"No se pudo leer {path}: {exc}") from exc


def validate_glossary_references(
    glossary: Glossary,
    unit_labels: tuple[str, ...],
    *,
    source: str = "Glosario.md",
) -> None:
    labels = {label.casefold() for label in unit_labels}
    terms = {entry.term for entry in glossary.entries}
    for entry in glossary.entries:
        first_unit = entry.first_unit.rstrip(".").casefold()
        if first_unit not in labels:
            raise ApparatusSourceError(
                f"{source}, entrada {entry.term!r}: primera unidad desconocida "
                f"{entry.first_unit!r}."
            )
        for folio in re.findall(r"\bfolio (\d{3}[rv])\b", entry.references, re.I):
            if f"folio {folio}".casefold() not in labels:
                raise ApparatusSourceError(
                    f"{source}, entrada {entry.term!r}: referencia a folio "
                    f"inexistente {folio}."
                )
        for response in map(
            int, re.findall(r"\brespuesta (\d+)\b", entry.references, re.I)
        ):
            if not 1 <= response <= 40:
                raise ApparatusSourceError(
                    f"{source}, entrada {entry.term!r}: respuesta inexistente "
                    f"{response}."
                )
        for target in re.findall(r"Glosario: `([^`]+)`", entry.references):
            if target not in terms:
                raise ApparatusSourceError(
                    f"{source}, entrada {entry.term!r}: remisión a término "
                    f"inexistente {target!r}."
                )


def _section(text: str, start: str, end: str) -> str:
    if text.count(start) != 1 or text.count(end) != 1:
        raise ApparatusSourceError(
            f"Registro: no se pudo delimitar de forma única {start!r} y {end!r}."
        )
    return text.split(start, 1)[1].split(end, 1)[0]


def _table_cells(line: str) -> tuple[str, ...]:
    if not line.startswith("|") or not line.rstrip().endswith("|"):
        return ()
    return tuple(cell.strip() for cell in line.strip().strip("|").split("|"))


def _parse_evidence_region(
    region: str,
    *,
    inferred_level: str | None,
    source: str,
) -> tuple[EvidenceEntry, ...]:
    entries: list[EvidenceEntry] = []
    section = "Sin subsección"
    for line_number, line in enumerate(region.splitlines(), start=1):
        heading = re.match(r"^#{3,4} (.+)$", line)
        if heading:
            section = heading.group(1).strip()
            continue
        cells = _table_cells(line)
        if not cells or not re.fullmatch(r"[A-Z]+-\d{3}", cells[0]):
            continue
        identifier = cells[0]
        if inferred_level is None:
            if len(cells) != 5:
                raise ApparatusSourceError(
                    f"{source}, {identifier}: fila documental con {len(cells)} columnas; "
                    "se esperaban cinco."
                )
            statement, level, evidence, status = cells[1:]
        elif inferred_level == "I":
            if len(cells) != 4:
                raise ApparatusSourceError(
                    f"{source}, {identifier}: fila interpretativa inválida."
                )
            statement, evidence, status = cells[1:]
            level = "I"
        else:
            if len(cells) != 3:
                raise ApparatusSourceError(
                    f"{source}, {identifier}: fila de límite inválida."
                )
            statement, evidence = cells[1:]
            level = "L"
            status = ""
        components = tuple(level.split("/"))
        if not components or any(component not in ALLOWED_LEVELS for component in components):
            raise ApparatusSourceError(
                f"{source}, {identifier}: nivel no reconocido {level!r}."
            )
        if not statement or not evidence:
            missing = "formulación" if not statement else "evidencia"
            raise ApparatusSourceError(
                f"{source}, {identifier}: falta {missing}."
            )
        if status and not status.startswith(RECOGNIZED_STATES):
            raise ApparatusSourceError(
                f"{source}, {identifier}: estado o cautela no reconocible: {status!r}."
            )
        entries.append(
            EvidenceEntry(identifier, statement, level, evidence, status, section)
        )
    return tuple(entries)


def _parse_calculations(region: str, *, source: str) -> tuple[Calculation, ...]:
    calculations: list[Calculation] = []
    for line in region.splitlines():
        cells = _table_cells(line)
        if not cells or not re.fullmatch(r"CAL-\d{3}", cells[0]):
            continue
        if len(cells) != 5 or any(not cell for cell in cells):
            identifier = cells[0] if cells else "CAL desconocido"
            raise ApparatusSourceError(
                f"{source}, {identifier}: el cálculo debe conservar cinco campos."
            )
        calculations.append(Calculation(*cells))
    if not calculations:
        raise ApparatusSourceError(f"{source}: no se encontraron cálculos CAL-*.")
    return tuple(calculations)


def parse_evidence_register(
    text: str, *, source: str = "Registro_Afirmaciones_Calculos_v1.md"
) -> EvidenceRegister:
    """Parse the complete D/C/I/E/L register and its CAL rows."""

    version = _version(text)
    if version != REGISTER_VERSION:
        raise ApparatusSourceError(
            f"{source}: versión {version or 'ausente'}; se exige {REGISTER_VERSION}."
        )
    documentary = _parse_evidence_region(
        _section(text, "## 3. Registro de afirmaciones documentales", "## 4. Interpretaciones autorizables"),
        inferred_level=None,
        source=source,
    )
    interpretations = _parse_evidence_region(
        _section(text, "## 4. Interpretaciones autorizables", "## 5. Límites y discrepancias que deben permanecer visibles"),
        inferred_level="I",
        source=source,
    )
    limits = _parse_evidence_region(
        _section(text, "## 5. Límites y discrepancias que deben permanecer visibles", "## 6. Registro de cálculos reproducibles"),
        inferred_level="L",
        source=source,
    )
    calculations = _parse_calculations(
        _section(text, "## 6. Registro de cálculos reproducibles", "## 7. Afirmaciones rechazadas o que requieren reformulación"),
        source=source,
    )
    entries = (*documentary, *interpretations, *limits)
    identifiers = [entry.identifier for entry in entries]
    calculation_ids = [calculation.identifier for calculation in calculations]
    all_identifiers = identifiers + calculation_ids
    duplicates = sorted(
        {identifier for identifier in all_identifiers if all_identifiers.count(identifier) > 1}
    )
    if duplicates:
        raise ApparatusSourceError(
            f"{source}: identificadores duplicados: {', '.join(duplicates)}."
        )
    calculation_set = set(calculation_ids)
    for entry in entries:
        referenced = set(re.findall(r"CAL-\d{3}", entry.evidence))
        missing = sorted(referenced - calculation_set)
        if missing:
            raise ApparatusSourceError(
                f"{source}, {entry.identifier}: referencias CAL inexistentes: "
                + ", ".join(missing)
            )
        if entry.level == "C" and not referenced:
            raise ApparatusSourceError(
                f"{source}, {entry.identifier}: una entrada C debe remitir a CAL-*."
            )
    return EvidenceRegister(version, tuple(entries), calculations)


def load_evidence_register(path: Path) -> EvidenceRegister:
    try:
        return parse_evidence_register(path.read_text(encoding="utf-8"), source=str(path))
    except (OSError, UnicodeError) as exc:
        raise ApparatusSourceError(f"No se pudo leer {path}: {exc}") from exc


__all__ = [
    "ALLOWED_LEVELS",
    "ApparatusSourceError",
    "Calculation",
    "EvidenceEntry",
    "EvidenceRegister",
    "Glossary",
    "GlossaryEntry",
    "REGISTER_VERSION",
    "git_blob_oid",
    "load_evidence_register",
    "load_glossary",
    "parse_evidence_register",
    "parse_glossary",
    "validate_glossary_references",
]

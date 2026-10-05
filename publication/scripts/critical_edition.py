#!/usr/bin/env python3
"""Parse the authoritative 3.6 critical-edition unit blocks for publication."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml


EXPECTED_UNIT_COUNT = 35
SECTION_NAMES = (
    "Imagen",
    "Transcripción paleográfica",
    "Observaciones editoriales",
    "Notas paleográficas",
    "Notas históricas",
    "Referencias cruzadas",
)
TEXT_SECTION_NAMES = SECTION_NAMES[1:]
POSITION_LABELS = {
    "complete": "página completa",
    "left": "izquierda",
    "right": "derecha",
}


class CriticalEditionError(RuntimeError):
    """Report one actionable structural mismatch in the critical edition."""


@dataclass(frozen=True)
class UnitSpec:
    unit_id: str
    label: str
    order: int
    pdf_page: int
    position: str

    @property
    def anchor(self) -> str:
        return self.unit_id.replace("_", "-")


@dataclass(frozen=True)
class CriticalUnit:
    spec: UnitSpec
    sections: dict[str, str]


def load_unit_specs(path: Path) -> tuple[UnitSpec, ...]:
    """Load and validate the publication-facing fields of unidades.yaml."""

    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        raise CriticalEditionError(f"No se pudo leer {path}: {exc}") from exc
    units = data.get("units") if isinstance(data, dict) else None
    if not isinstance(data, dict) or data.get("unit_count") != EXPECTED_UNIT_COUNT or not isinstance(units, list):
        raise CriticalEditionError(
            "unidades.yaml debe declarar unit_count: 35 y una lista units."
        )
    if len(units) != EXPECTED_UNIT_COUNT:
        raise CriticalEditionError(
            f"unidades.yaml contiene {len(units)} unidades; se esperaban 35."
        )
    specs: list[UnitSpec] = []
    for index, raw in enumerate(units, start=1):
        if not isinstance(raw, dict):
            raise CriticalEditionError(f"La unidad {index} de unidades.yaml no es un mapa.")
        try:
            spec = UnitSpec(
                unit_id=str(raw["id"]),
                label=str(raw["label"]),
                order=int(raw["order"]),
                pdf_page=int(raw["pdf_page"]),
                position=str(raw["position"]),
            )
        except (KeyError, TypeError, ValueError) as exc:
            raise CriticalEditionError(
                f"La unidad {index} carece de id, label, order, pdf_page o position válidos."
            ) from exc
        if spec.order != index:
            raise CriticalEditionError(
                f"Orden no consecutivo en {spec.unit_id}: {spec.order}; esperado {index}."
            )
        if spec.position not in POSITION_LABELS:
            raise CriticalEditionError(
                f"Posición no válida en {spec.unit_id}: {spec.position}."
            )
        specs.append(spec)
    identifiers = [spec.unit_id for spec in specs]
    labels = [spec.label for spec in specs]
    if len(set(identifiers)) != EXPECTED_UNIT_COUNT:
        raise CriticalEditionError("Los 35 identificadores de unidad deben ser únicos.")
    if len(set(labels)) != EXPECTED_UNIT_COUNT:
        raise CriticalEditionError("Las 35 etiquetas de unidad deben ser únicas.")
    return tuple(specs)


def _transcription_region(text: str) -> str:
    start_marker = "# 3. Transcripción paleográfica"
    end_marker = "# 4. Apéndices"
    if text.count(start_marker) != 1 or text.count(end_marker) != 1:
        raise CriticalEditionError(
            "Edicion_Critica.md debe contener una sola sección 3 de transcripción "
            "y una sola sección 4 de apéndices."
        )
    start = text.index(start_marker) + len(start_marker)
    end = text.index(end_marker, start)
    return text[start:end]


def _split_unit_blocks(region: str) -> tuple[tuple[str, str], ...]:
    matches = list(re.finditer(r"^## (?P<label>[^\n]+)\s*$", region, re.MULTILINE))
    blocks: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(region)
        blocks.append((match.group("label").strip(), region[match.end():end]))
    return tuple(blocks)


def _split_sections(label: str, block: str) -> dict[str, str]:
    matches = list(re.finditer(r"^### (?P<name>[^\n]+)\s*$", block, re.MULTILINE))
    names = tuple(match.group("name").strip() for match in matches)
    if names != SECTION_NAMES:
        raise CriticalEditionError(
            f"La unidad {label} debe contener, una sola vez y en orden, las seis "
            f"secciones {', '.join(SECTION_NAMES)}; contiene {', '.join(names) or 'ninguna'}."
        )
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(block)
        content = block[match.end():end].strip("\n")
        if content.endswith("\n---"):
            content = content[:-4].rstrip("\n")
        if not content:
            raise CriticalEditionError(
                f"La sección {match.group('name')} de {label} está vacía."
            )
        sections[match.group("name").strip()] = content
    return sections


def _validate_image_locator(unit: CriticalUnit, manuscript_name: str) -> None:
    expected = (
        f"`{manuscript_name}, página {unit.spec.pdf_page} "
        f"({POSITION_LABELS[unit.spec.position]})`"
    )
    actual = unit.sections["Imagen"]
    if actual != expected:
        raise CriticalEditionError(
            f"Localizador de imagen discordante en {unit.spec.unit_id}: "
            f"{actual!r}; esperado {expected!r}."
        )


def parse_critical_edition(
    text: str,
    specs: tuple[UnitSpec, ...],
    manuscript_name: str,
) -> tuple[CriticalUnit, ...]:
    """Match all authoritative edition blocks one-to-one against unidades.yaml."""

    blocks = _split_unit_blocks(_transcription_region(text))
    labels = tuple(label for label, _ in blocks)
    expected_labels = tuple(spec.label for spec in specs)
    if len(blocks) != EXPECTED_UNIT_COUNT:
        raise CriticalEditionError(
            f"La sección 3 contiene {len(blocks)} bloques de unidad; se esperaban 35."
        )
    if labels != expected_labels:
        for index, (actual, expected) in enumerate(
            zip(labels, expected_labels, strict=False), start=1
        ):
            if actual != expected:
                raise CriticalEditionError(
                    f"Unidad editorial {index} discordante: {actual!r}; "
                    f"unidades.yaml exige {expected!r}."
                )
        raise CriticalEditionError(
            "Las etiquetas de Edicion_Critica.md no coinciden exactamente con unidades.yaml."
        )
    units = tuple(
        CriticalUnit(spec, _split_sections(label, block))
        for spec, (label, block) in zip(specs, blocks, strict=True)
    )
    for unit in units:
        _validate_image_locator(unit, manuscript_name)
    return units


def line_block(text: str) -> str:
    """Encode exact physical transcription lines as a Pandoc line block."""

    lines = text.splitlines()
    if not lines:
        raise CriticalEditionError(
            "Cada transcripción paleográfica debe contener al menos una línea física."
        )
    # Pandoc representa una línea vacía interna de un line block mediante un
    # marcador `|` sin contenido. Es necesaria en el croquis de folio 307r.
    # Pandoc's smart punctuation would otherwise turn the editorial sign
    # `[...]` into `[…]`, changing a character with textual value.
    escaped = (line.replace("[...]", r"[\.\.\.]") for line in lines)
    return "\n".join(f"| {line}" if line else "|" for line in escaped)


__all__ = [
    "CriticalEditionError",
    "CriticalUnit",
    "EXPECTED_UNIT_COUNT",
    "POSITION_LABELS",
    "SECTION_NAMES",
    "TEXT_SECTION_NAMES",
    "UnitSpec",
    "line_block",
    "load_unit_specs",
    "parse_critical_edition",
]

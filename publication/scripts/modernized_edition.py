#!/usr/bin/env python3
"""Parse and validate the authoritative modernized edition 1.3."""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


EXPECTED_VERSION = "1.3"
EXPECTED_RESPONSE_COUNT = 40
QUESTION_LABEL = "Pregunta {number} del interrogatorio de 1749 —grafía modernizada—"
RESPONSE_LABEL = "Respuesta de Sorribos y Santibáñez"
FIXED_SECTION_HEADINGS = (
    "Documentos relacionados",
    "Portada",
    "Comparecencia y juramento",
    *(f"Respuesta {number}" for number in range(1, EXPECTED_RESPONSE_COUNT + 1)),
    "Ratificación, edades y firmas",
    "Concordancia material",
    "Notas",
    "Nota de uso",
)


class ModernizedEditionError(RuntimeError):
    """Report one actionable structural or fidelity failure."""


@dataclass(frozen=True)
class ModernizedResponse:
    number: int
    title: str
    heading: str
    question_label: str
    question: str
    response_label: str
    folios: str
    body: str

    @property
    def anchor(self) -> str:
        return f"respuesta-{self.number}"


@dataclass(frozen=True)
class ConcordanceRow:
    unit_label: str
    content: str


@dataclass(frozen=True)
class ModernizedEdition:
    source_title: str
    version_heading: str
    version: str
    nature: str
    introduction: str
    related_documents: str
    portada: str
    comparecencia: str
    responses: tuple[ModernizedResponse, ...]
    ratification: str
    concordance: str
    concordance_rows: tuple[ConcordanceRow, ...]
    notes: str
    note_use: str
    note_calls: tuple[str, ...]
    note_definitions: tuple[str, ...]


def _h2_sections(text: str) -> tuple[str, dict[str, str]]:
    matches = list(re.finditer(r"^## (?P<heading>[^\n]+)\s*$", text, re.MULTILINE))
    if not matches:
        raise ModernizedEditionError("La edición modernizada no contiene secciones H2.")
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        heading = match.group("heading").strip()
        if heading in sections:
            raise ModernizedEditionError(f"Sección duplicada en la modernizada: {heading}.")
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[heading] = text[match.end():end].strip("\n")
    preamble = text[: matches[0].start()].strip("\n")
    version_heading = "Versión modernizada para lectura"
    if tuple(sections) and next(iter(sections)) == version_heading:
        version_body = sections.pop(version_heading)
        preamble = (
            f"{preamble}\n\n## {version_heading}\n\n{version_body}"
        ).strip("\n")
    return preamble, sections


def _source_headings(sections: dict[str, str]) -> tuple[str, ...]:
    normalized: list[str] = []
    for heading in sections:
        response = re.fullmatch(r"Respuesta (?P<number>\d+)\. .+", heading)
        normalized.append(
            f"Respuesta {response.group('number')}" if response is not None else heading
        )
    return tuple(normalized)


def _parse_preamble(preamble: str) -> tuple[str, str, str, str, str]:
    lines = preamble.splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ModernizedEditionError("Falta el título H1 de la edición modernizada.")
    source_title = lines[0][2:].strip()
    version_heading = next(
        (line[3:].strip() for line in lines[1:] if line.startswith("## ")), None
    )
    if version_heading != "Versión modernizada para lectura":
        raise ModernizedEditionError(
            "La edición debe declarar la sección «Versión modernizada para lectura»."
        )
    version_match = re.search(r"^\*\*Versión:\*\*\s*(\S+)\s*$", preamble, re.MULTILINE)
    nature_match = re.search(r"^\*\*Naturaleza:\*\*\s*(.+?)\s*$", preamble, re.MULTILINE)
    if version_match is None or version_match.group(1) != EXPECTED_VERSION:
        actual = version_match.group(1) if version_match else "ausente"
        raise ModernizedEditionError(
            f"Versión modernizada incorrecta: {actual}; se exige {EXPECTED_VERSION}."
        )
    if nature_match is None:
        raise ModernizedEditionError("Falta la naturaleza editorial de la modernizada.")
    introduction_match = re.search(r"^> .+(?:\n> .+)*$", preamble, re.MULTILINE)
    if introduction_match is None:
        raise ModernizedEditionError("Falta la nota introductoria de la modernizada.")
    return (
        source_title,
        version_heading,
        version_match.group(1),
        nature_match.group(1).strip(),
        introduction_match.group(0),
    )


def _parse_response(heading: str, block: str) -> ModernizedResponse:
    match = re.fullmatch(r"Respuesta (?P<number>\d+)\. (?P<title>.+)", heading)
    if match is None:
        raise ModernizedEditionError(f"Encabezado de respuesta no válido: {heading}.")
    number = int(match.group("number"))
    question_pattern = re.compile(
        rf"^\*\*(?P<label>{re.escape(QUESTION_LABEL.format(number=number))})\*\*\s*$",
        re.MULTILINE,
    )
    question_matches = list(question_pattern.finditer(block))
    response_matches = list(
        re.finditer(rf"^\*\*({re.escape(RESPONSE_LABEL)})\*\*\s*$", block, re.MULTILINE)
    )
    if len(question_matches) != 1:
        raise ModernizedEditionError(
            f"Respuesta {number}: se esperaba una pregunta y hay {len(question_matches)}."
        )
    if len(response_matches) != 1:
        raise ModernizedEditionError(
            f"Respuesta {number}: se esperaba una respuesta local y hay {len(response_matches)}."
        )
    question_match = question_matches[0]
    response_match = response_matches[0]
    if question_match.start() != 0 or response_match.start() <= question_match.end():
        raise ModernizedEditionError(
            f"Respuesta {number}: pregunta y respuesta local están desordenadas."
        )
    question = block[question_match.end():response_match.start()].strip("\n")
    local = block[response_match.end():].strip("\n")
    folio_match = re.match(r"^(?P<folios>\*\(Folios? [^\n]+\)\*)\n+", local)
    if folio_match is None:
        raise ModernizedEditionError(
            f"Respuesta {number}: falta el localizador de folio o folios."
        )
    body = local[folio_match.end():].strip("\n")
    if not question or not body:
        missing = "pregunta" if not question else "cuerpo local"
        raise ModernizedEditionError(f"Respuesta {number}: {missing} vacío.")
    return ModernizedResponse(
        number=number,
        title=match.group("title").strip(),
        heading=heading,
        question_label=question_match.group("label"),
        question=question,
        response_label=RESPONSE_LABEL,
        folios=folio_match.group("folios"),
        body=body,
    )


def _parse_concordance(block: str) -> tuple[ConcordanceRow, ...]:
    rows: list[ConcordanceRow] = []
    for line in block.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 2:
            raise ModernizedEditionError(
                f"Fila de concordancia inválida; se esperaban dos columnas: {line}"
            )
        if cells[0] == "Unidad de la Edición Crítica" or set(cells[0]) == {"-"}:
            continue
        rows.append(ConcordanceRow(cells[0], cells[1]))
    if len(rows) != 35:
        raise ModernizedEditionError(
            f"La concordancia contiene {len(rows)} unidades; se esperaban 35."
        )
    return tuple(rows)


def _footnotes(text: str) -> tuple[tuple[str, ...], tuple[str, ...]]:
    definitions = tuple(re.findall(r"^\[\^([^\]]+)\]:", text, re.MULTILINE))
    calls = tuple(re.findall(r"\[\^([^\]]+)\](?!:)", text))
    definition_counts = Counter(definitions)
    duplicates = sorted(label for label, count in definition_counts.items() if count != 1)
    if duplicates:
        raise ModernizedEditionError(
            "Definiciones de nota duplicadas: " + ", ".join(duplicates)
        )
    missing = sorted(set(calls) - set(definitions))
    orphaned = sorted(set(definitions) - set(calls))
    if missing:
        raise ModernizedEditionError(
            "Llamadas de nota sin definición: " + ", ".join(missing)
        )
    if orphaned:
        raise ModernizedEditionError(
            "Definiciones de nota nunca referidas: " + ", ".join(orphaned)
        )
    return calls, definitions


def parse_modernized_edition(text: str) -> ModernizedEdition:
    """Parse the 1.3 source and enforce the complete documentary sequence."""

    preamble, sections = _h2_sections(text)
    if _source_headings(sections) != FIXED_SECTION_HEADINGS:
        raise ModernizedEditionError(
            "Orden documental incorrecto: se exigen documentos relacionados, portada, "
            "comparecencia, respuestas 1–40, ratificación, concordancia, notas y nota de uso."
        )
    source_title, version_heading, version, nature, introduction = _parse_preamble(
        preamble
    )
    response_items = [
        (heading, block)
        for heading, block in sections.items()
        if heading.startswith("Respuesta ")
    ]
    responses = tuple(_parse_response(heading, block) for heading, block in response_items)
    numbers = tuple(response.number for response in responses)
    expected = tuple(range(1, EXPECTED_RESPONSE_COUNT + 1))
    if numbers != expected:
        raise ModernizedEditionError(
            f"Numeración de respuestas incorrecta: {numbers}; se exige 1–40."
        )
    titles = tuple(response.title for response in responses)
    if len(set(titles)) != EXPECTED_RESPONSE_COUNT:
        raise ModernizedEditionError("Los 40 títulos temáticos deben ser únicos.")
    calls, definitions = _footnotes(text)
    return ModernizedEdition(
        source_title=source_title,
        version_heading=version_heading,
        version=version,
        nature=nature,
        introduction=introduction,
        related_documents=sections["Documentos relacionados"],
        portada=sections["Portada"],
        comparecencia=sections["Comparecencia y juramento"],
        responses=responses,
        ratification=sections["Ratificación, edades y firmas"],
        concordance=sections["Concordancia material"],
        concordance_rows=_parse_concordance(sections["Concordancia material"]),
        notes=sections["Notas"],
        note_use=sections["Nota de uso"],
        note_calls=calls,
        note_definitions=definitions,
    )


def parse_verified_questions(introduction_text: str) -> tuple[str, ...]:
    """Read the authoritative numbered list embedded in Introduction 1.3."""

    start = "## 3. El interrogatorio de cuarenta preguntas"
    end = "## 4. Cómo se realizaba la averiguación"
    if introduction_text.count(start) != 1 or introduction_text.count(end) != 1:
        raise ModernizedEditionError(
            "La Introducción 1.3 no contiene una sección única de preguntas 1–40."
        )
    region = introduction_text.split(start, 1)[1].split(end, 1)[0]
    matches = re.findall(r"^(?P<number>\d+)\. (?P<question>¿.+)$", region, re.MULTILINE)
    numbers = tuple(int(number) for number, _ in matches)
    if numbers != tuple(range(1, EXPECTED_RESPONSE_COUNT + 1)):
        raise ModernizedEditionError(
            "La Introducción 1.3 no contiene las 40 preguntas consecutivas verificadas."
        )
    return tuple(question for _, question in matches)


def validate_verified_questions(
    edition: ModernizedEdition,
    introduction_text: str,
    verification_text: str,
) -> None:
    """Require exact one-to-one identity with the externally verified questionnaire."""

    required_verification_markers = (
        "Consta de **cuarenta preguntas numeradas**.",
        "La respuesta 40 corresponde a rentas o fincas del rey",
        "la forma documental local «venta» se conserva",
    )
    missing_markers = [
        marker for marker in required_verification_markers if marker not in verification_text
    ]
    if missing_markers:
        raise ModernizedEditionError(
            "El informe de verificación del interrogatorio no conserva su contrato: "
            + "; ".join(missing_markers)
        )
    verified = parse_verified_questions(introduction_text)
    actual = tuple(response.question for response in edition.responses)
    for number, (source_question, verified_question) in enumerate(
        zip(actual, verified, strict=True), start=1
    ):
        if source_question != verified_question:
            raise ModernizedEditionError(
                f"Pregunta {number} desplazada o discordante respecto de la versión verificada."
            )


def validate_concordance_units(
    edition: ModernizedEdition, unit_labels: tuple[str, ...]
) -> None:
    actual = tuple(row.unit_label for row in edition.concordance_rows)
    if actual != unit_labels:
        for index, (found, expected) in enumerate(
            zip(actual, unit_labels, strict=False), start=1
        ):
            if found != expected:
                raise ModernizedEditionError(
                    f"Concordancia material, fila {index}: {found!r}; se esperaba {expected!r}."
                )
        raise ModernizedEditionError(
            "La concordancia material no coincide con las 35 unidades canónicas."
        )


def response_unit_labels(edition: ModernizedEdition) -> dict[int, tuple[str, ...]]:
    """Derive response-to-unit navigation solely from the canonical concordance table."""

    mapping: dict[int, list[str]] = {number: [] for number in range(1, 41)}
    for row in edition.concordance_rows:
        response_part = re.search(
            r"respuestas? (?P<numbers>[0-9, y]+)", row.content, re.IGNORECASE
        )
        if response_part is None:
            continue
        for value in re.findall(r"\d+", response_part.group("numbers")):
            number = int(value)
            if 1 <= number <= 40:
                mapping[number].append(row.unit_label)
    missing = [number for number, labels in mapping.items() if not labels]
    if missing:
        raise ModernizedEditionError(
            "La concordancia no permite localizar las respuestas: "
            + ", ".join(map(str, missing))
        )
    return {number: tuple(labels) for number, labels in mapping.items()}


def load_modernized_edition(path: Path) -> ModernizedEdition:
    try:
        return parse_modernized_edition(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        raise ModernizedEditionError(f"No se pudo leer {path}: {exc}") from exc


__all__ = [
    "EXPECTED_RESPONSE_COUNT",
    "EXPECTED_VERSION",
    "ConcordanceRow",
    "ModernizedEdition",
    "ModernizedEditionError",
    "ModernizedResponse",
    "load_modernized_edition",
    "parse_modernized_edition",
    "parse_verified_questions",
    "response_unit_labels",
    "validate_concordance_units",
    "validate_verified_questions",
]

#!/usr/bin/env python3
"""Generate Phase 4C from the authoritative modernized edition 1.3."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

from critical_edition import load_unit_specs, published_unit_anchor
from modernized_edition import (
    ModernizedEdition,
    ModernizedEditionError,
    ModernizedResponse,
    load_modernized_edition,
    response_unit_labels,
    validate_concordance_units,
    validate_verified_questions,
)


MODERNIZED_QMD = "16-edicion-modernizada.qmd"
MODERNIZED_CHAPTER_ID = "edicion-modernizada"
MODERNIZED_SOURCE = Path(
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/"
    "Catastro_Sorrios_1752_Version_Modernizada.md"
)
INTRODUCTION_SOURCE = Path(
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/"
    "Introduccion_Catastro_Ensenada_Sorrios.md"
)
VERIFICATION_SOURCE = Path(
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/"
    "Verificacion_Interrogatorio_40_Preguntas.md"
)
UNITS_SOURCE = Path("project/00_CONTROL/unidades.yaml")

# The source section is repository navigation, not historical content. Its
# relative project/ links would be broken and would expose internal source
# paths in the book, so the Quarto book navigation assumes that function.
RELATED_DOCUMENTS_POLICY = "replaced_by_book_navigation"
NOTE_ID_PREFIX = "modernizada-"


class ModernizedBuildError(RuntimeError):
    """Report one actionable failure while generating Phase 4C."""


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise ModernizedBuildError(f"No se pudo leer {path}: {exc}") from exc


def _namespace_notes(text: str) -> str:
    """Avoid cross-chapter Pandoc footnote collisions without changing note text."""

    return re.sub(
        r"\[\^([^\]]+)\]",
        lambda match: f"[^{NOTE_ID_PREFIX}{match.group(1)}]",
        text,
    )


def _anchor_for_label(label: str, unit_anchors: dict[str, str]) -> str:
    try:
        return unit_anchors[label]
    except KeyError as exc:
        raise ModernizedBuildError(
            f"La concordancia remite a una unidad sin ancla canónica: {label}."
        ) from exc


def _navigation(
    response: ModernizedResponse,
    labels: tuple[str, ...],
    unit_anchors: dict[str, str],
) -> str:
    links = "; ".join(
        f"[{label}](15-transcripcion.qmd#{_anchor_for_label(label, unit_anchors)})"
        for label in labels
    )
    return (
        "::: {.material-navigation}\n"
        f"**Unidades materiales en el capítulo 15:** {links}.\n"
        ":::"
    )


def _response_qmd(
    response: ModernizedResponse,
    labels: tuple[str, ...],
    unit_anchors: dict[str, str],
) -> str:
    return f"""## {response.heading} {{#{response.anchor}}}

::: {{.question-external}}
**{response.question_label}**

{_namespace_notes(response.question)}
:::

::: {{.response-local}}
**{response.response_label}**

{_namespace_notes(response.folios)}

{_namespace_notes(response.body)}
:::

{_navigation(response, labels, unit_anchors)}"""


def modernized_qmd(
    edition: ModernizedEdition,
    unit_anchors: dict[str, str],
) -> str:
    """Render the complete chapter without changing canonical wording."""

    response_units = response_unit_labels(edition)
    chunks = [
        f'''---
title: "El Catastro en español actual"
subtitle: "Parte V. Versión íntegra de lectura"
chapter-id: {MODERNIZED_CHAPTER_ID}
publication-status: generated
sources:
  - {MODERNIZED_SOURCE.as_posix()}
  - {INTRODUCTION_SOURCE.as_posix()}
  - {VERIFICATION_SOURCE.as_posix()}
  - {UNITS_SOURCE.as_posix()}
source-title: "{edition.source_title}"
source-version: "{edition.version}"
edition-nature: "{edition.nature}"
source-related-documents: {RELATED_DOCUMENTS_POLICY}
---

{_namespace_notes(edition.introduction)}

## Portada {{#modernizada-portada}}

{_namespace_notes(edition.portada)}

## Comparecencia y juramento {{#comparecencia}}

{_namespace_notes(edition.comparecencia)}'''
    ]
    chunks.extend(
        _response_qmd(response, response_units[response.number], unit_anchors)
        for response in edition.responses
    )
    chunks.extend(
        (
            f"## Ratificación, edades y firmas {{#ratificacion-edades-firmas}}\n\n"
            f"{_namespace_notes(edition.ratification)}",
            f"## Concordancia material {{#concordancia-material}}\n\n"
            f"{_namespace_notes(edition.concordance)}",
            f"## Notas {{#notas}}\n\n{_namespace_notes(edition.notes)}",
            f"## Nota de uso {{#nota-de-uso}}\n\n{_namespace_notes(edition.note_use)}",
        )
    )
    return "\n\n".join(chunks).rstrip() + "\n"


def _front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise ModernizedBuildError("El capítulo 16 generado carece de front matter.")
    closing = text.find("\n---\n", 4)
    if closing < 0:
        raise ModernizedBuildError("Front matter incompleto en el capítulo 16 generado.")
    try:
        metadata = yaml.safe_load(text[4:closing])
    except yaml.YAMLError as exc:
        raise ModernizedBuildError(f"Front matter inválido en capítulo 16: {exc}") from exc
    if not isinstance(metadata, dict):
        raise ModernizedBuildError("El front matter del capítulo 16 debe ser un mapa.")
    return metadata, text[closing + 5 :].strip("\n")


def _generated_sections(body: str) -> tuple[str, dict[str, tuple[str, str]]]:
    matches = list(
        re.finditer(
            r"^## (?P<heading>.+?) \{#(?P<anchor>[a-z0-9-]+)\}\s*$",
            body,
            re.MULTILINE,
        )
    )
    if not matches:
        raise ModernizedBuildError("El capítulo 16 generado no contiene secciones ancladas.")
    introduction = body[: matches[0].start()].strip("\n")
    sections: dict[str, tuple[str, str]] = {}
    for index, match in enumerate(matches):
        heading = match.group("heading")
        if heading in sections:
            raise ModernizedBuildError(f"Encabezado generado duplicado: {heading}.")
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        sections[heading] = (
            match.group("anchor"),
            body[match.end():end].strip("\n"),
        )
    return introduction, sections


def _response_generated_fields(number: int, block: str) -> tuple[str, str, str]:
    pattern = re.compile(
        r"^::: \{\.question-external\}\n(?P<question>.*?)\n:::\n\n"
        r"::: \{\.response-local\}\n(?P<local>.*?)\n:::\n\n"
        r"::: \{\.material-navigation\}\n(?P<navigation>.*?)\n:::$",
        re.DOTALL,
    )
    match = pattern.fullmatch(block)
    if match is None:
        raise ModernizedBuildError(
            f"Respuesta {number}: estructura visual o de navegación generada inválida."
        )
    return match.group("question"), match.group("local"), match.group("navigation")


def validate_generated_fidelity(
    edition: ModernizedEdition,
    generated: str,
    unit_anchors: dict[str, str],
) -> None:
    """Compare source and output by semantic blocks, with actionable failures."""

    metadata, body = _front_matter(generated)
    expected_metadata = {
        "title": "El Catastro en español actual",
        "chapter-id": MODERNIZED_CHAPTER_ID,
        "publication-status": "generated",
        "source-version": edition.version,
        "edition-nature": edition.nature,
        "source-related-documents": RELATED_DOCUMENTS_POLICY,
    }
    for key, expected in expected_metadata.items():
        if metadata.get(key) != expected:
            raise ModernizedBuildError(
                f"Metadato {key} discordante: {metadata.get(key)!r}; esperado {expected!r}."
            )
    introduction, sections = _generated_sections(body)
    if introduction != _namespace_notes(edition.introduction):
        raise ModernizedBuildError("La nota introductoria perdió fidelidad textual.")
    expected_headings = (
        "Portada",
        "Comparecencia y juramento",
        *(response.heading for response in edition.responses),
        "Ratificación, edades y firmas",
        "Concordancia material",
        "Notas",
        "Nota de uso",
    )
    if tuple(sections) != expected_headings:
        raise ModernizedBuildError(
            "El capítulo 16 generado altera el orden documental de sus secciones."
        )
    fixed = {
        "Portada": ("modernizada-portada", _namespace_notes(edition.portada)),
        "Comparecencia y juramento": (
            "comparecencia",
            _namespace_notes(edition.comparecencia),
        ),
        "Ratificación, edades y firmas": (
            "ratificacion-edades-firmas",
            _namespace_notes(edition.ratification),
        ),
        "Concordancia material": (
            "concordancia-material",
            _namespace_notes(edition.concordance),
        ),
        "Notas": ("notas", _namespace_notes(edition.notes)),
        "Nota de uso": ("nota-de-uso", _namespace_notes(edition.note_use)),
    }
    for heading, (expected_anchor, expected_text) in fixed.items():
        anchor, actual = sections[heading]
        if anchor != expected_anchor:
            raise ModernizedBuildError(
                f"Sección {heading}: ancla {anchor!r}; esperada {expected_anchor!r}."
            )
        if actual != expected_text:
            raise ModernizedBuildError(
                f"Sección {heading}: discordancia textual entre fuente y capítulo generado."
            )
    response_units = response_unit_labels(edition)
    for response in edition.responses:
        anchor, block = sections[response.heading]
        if anchor != response.anchor:
            raise ModernizedBuildError(
                f"Respuesta {response.number}: ancla {anchor!r}; esperada {response.anchor!r}."
            )
        question, local, navigation = _response_generated_fields(response.number, block)
        expected_question = (
            f"**{response.question_label}**\n\n"
            f"{_namespace_notes(response.question)}"
        )
        expected_local = (
            f"**{response.response_label}**\n\n"
            f"{_namespace_notes(response.folios)}\n\n"
            f"{_namespace_notes(response.body)}"
        )
        if question != expected_question:
            raise ModernizedBuildError(
                f"Respuesta {response.number}: pregunta alterada o desplazada."
            )
        if local != expected_local:
            raise ModernizedBuildError(
                f"Respuesta {response.number}: texto local, folio, lista o cifra alterados."
            )
        expected_navigation = _navigation(
            response, response_units[response.number], unit_anchors
        ).splitlines()[1]
        if navigation != expected_navigation:
            raise ModernizedBuildError(
                f"Respuesta {response.number}: navegación material discordante."
            )
    if "project/" in body or "Documentos relacionados" in body:
        raise ModernizedBuildError(
            "El capítulo 16 expone enlaces internos de «Documentos relacionados»."
        )
    source_calls = tuple(NOTE_ID_PREFIX + label for label in edition.note_calls)
    source_definitions = tuple(
        NOTE_ID_PREFIX + label for label in edition.note_definitions
    )
    generated_calls = tuple(re.findall(r"\[\^([^\]]+)\](?!:)", body))
    generated_definitions = tuple(
        re.findall(r"^\[\^([^\]]+)\]:", body, re.MULTILINE)
    )
    if generated_calls != source_calls:
        raise ModernizedBuildError("Las llamadas de notas no coinciden con la fuente 1.3.")
    if generated_definitions != source_definitions:
        raise ModernizedBuildError(
            "Las definiciones de notas no coinciden con la fuente 1.3."
        )


def _write_qmd(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8", newline="\n")
    temporary.replace(path)


def build_modernized(repository_root: Path, publication_root: Path) -> tuple[Path, ...]:
    """Rebuild only the real Phase 4C chapter owned by this generator."""

    repository_root = repository_root.resolve()
    publication_root = publication_root.resolve()
    try:
        edition = load_modernized_edition(repository_root / MODERNIZED_SOURCE)
        specs = load_unit_specs(repository_root / UNITS_SOURCE)
        validate_concordance_units(edition, tuple(spec.label for spec in specs))
        validate_verified_questions(
            edition,
            _read_text(repository_root / INTRODUCTION_SOURCE),
            _read_text(repository_root / VERIFICATION_SOURCE),
        )
    except ModernizedEditionError as exc:
        raise ModernizedBuildError(str(exc)) from exc
    unit_anchors = {spec.label: published_unit_anchor(spec) for spec in specs}
    output = publication_root / "generated" / MODERNIZED_QMD
    generated_root = (publication_root / "generated").resolve()
    if output.resolve().parent != generated_root:
        raise ModernizedBuildError("Ruta de salida 4C insegura.")
    if output.is_file():
        output.unlink()
    content = modernized_qmd(edition, unit_anchors)
    validate_generated_fidelity(edition, content, unit_anchors)
    _write_qmd(output, content)
    return (output,)


__all__ = [
    "MODERNIZED_CHAPTER_ID",
    "MODERNIZED_QMD",
    "MODERNIZED_SOURCE",
    "NOTE_ID_PREFIX",
    "ModernizedBuildError",
    "RELATED_DOCUMENTS_POLICY",
    "build_modernized",
    "modernized_qmd",
    "validate_generated_fidelity",
]

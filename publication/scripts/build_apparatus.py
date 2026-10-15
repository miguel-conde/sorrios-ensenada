#!/usr/bin/env python3
"""Generate the four reproducible Phase 4D apparatus views."""

from __future__ import annotations

import re
import unicodedata
from collections import defaultdict
from dataclasses import dataclass
from itertools import zip_longest
from pathlib import Path

import yaml

from apparatus_sources import (
    ApparatusSourceError,
    EvidenceRegister,
    Glossary,
    git_blob_oid,
    load_evidence_register,
    load_glossary,
    validate_glossary_references,
)
from critical_edition import (
    CriticalUnit,
    UnitSpec,
    load_unit_specs,
    parse_critical_edition,
    published_unit_anchor,
)
from modernized_edition import (
    ModernizedEdition,
    load_modernized_edition,
    response_unit_labels,
    validate_concordance_units,
)


GLOSSARY_SOURCE = Path("project/20_TRABAJO_EDITORIAL/Glosario.md")
REGISTER_SOURCE = Path(
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/"
    "Registro_Afirmaciones_Calculos_v1.md"
)
STUDY_SOURCE = Path(
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md"
)
CRITICAL_SOURCE = Path("project/20_TRABAJO_EDITORIAL/Edicion_Critica.md")
MODERNIZED_SOURCE = Path(
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/"
    "Catastro_Sorrios_1752_Version_Modernizada.md"
)
UNITS_SOURCE = Path("project/00_CONTROL/unidades.yaml")
OUTPUT_NAMES = (
    "glosario.qmd",
    "cuadros-cuantitativos.qmd",
    "concordancia.qmd",
    "matriz-evidencia.qmd",
)

EVIDENCE_CITATIONS = {
    "TOP-004": ("jularconflictos",),
    "TOP-005": ("santanovalbuena2022documentos",),
    "TOP-006": ("sanchezbadiola2019nobiliario",),
    "TOP-007": ("pares1715santibanez",),
    "TOP-008": ("relacionparroquial1768",),
    "TOP-009": ("gaceta1864sorribos",),
    "TOP-010": ("alvarezbalbuenatoponimia",),
    "TOP-011": ("ayuntamientosantamariaordassantibanez",),
    "JUR-007": ("relacionparroquial1768", "alvarezbalbuenatoponimia"),
    "JUR-008": ("pousadieguez2022juzgados", "paresconde1742"),
    "JUR-009": ("parestituloabogado",),
    "DEM-005": ("camarerobullon2002catastro",),
    "DEM-006": ("relacionparroquial1768",),
    "TER-011": ("castanoalvarez2017apuntes",),
    "AGR-011": ("bartolomebartolome2001comercio",),
    "AGR-012": ("sanchezlopezdevinuesa2001cultivos",),
    "AGR-013": ("riescochueca2013lexico",),
    "GAN-008": ("cortizoalvarez1984ganado",),
    "HID-008": ("zapicogutierrez2016molinos", "hernandezcubero2018recursos"),
    "FIS-013": ("reycastelao1985voto",),
    "FIS-014": ("mazazorrilla1982pobreza",),
    "FIS-015": ("paresmesta",),
    "FIS-016": ("garciagarcia1986haciendas",),
    "FIS-017": ("caputvallis2008catastro",),
}


class ApparatusBuildError(RuntimeError):
    """Report one actionable Phase 4D generation or fidelity failure."""


@dataclass(frozen=True)
class ChapterUse:
    number: int
    title: str
    path: str
    anchor: str


@dataclass(frozen=True)
class ApparatusData:
    glossary: Glossary
    glossary_git_blob: str
    register: EvidenceRegister
    specs: tuple[UnitSpec, ...]
    critical_units: tuple[CriticalUnit, ...]
    modernized: ModernizedEdition
    evidence_usage: dict[str, tuple[ChapterUse, ...]]


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise ApparatusBuildError(f"No se pudo leer {path}: {exc}") from exc


def _front_matter_and_body(path: Path) -> tuple[dict, str]:
    text = _read_text(path)
    if not text.startswith("---\n"):
        raise ApparatusBuildError(f"{path}: falta el front matter.")
    closing = text.find("\n---\n", 4)
    if closing < 0:
        raise ApparatusBuildError(f"{path}: front matter incompleto.")
    try:
        metadata = yaml.safe_load(text[4:closing])
    except yaml.YAMLError as exc:
        raise ApparatusBuildError(f"{path}: front matter inválido: {exc}") from exc
    if not isinstance(metadata, dict):
        raise ApparatusBuildError(f"{path}: el front matter debe ser un mapa.")
    return metadata, text[closing + 5 :]


def _front_matter(path: Path) -> dict:
    return _front_matter_and_body(path)[0]


def _evidence_anchor(body: str, identifier: str) -> str:
    """Return the nearest explicit section anchor for one chapter use."""

    current = ""
    first = ""
    for line in body.splitlines():
        heading = re.match(r"^##\s+.+\{#([a-z0-9-]+)(?:\s+[^}]*)?\}\s*$", line)
        if heading:
            current = heading.group(1)
            first = first or current
        if identifier in line:
            return current or first
    return first


def _evidence_usage(
    publication_root: Path, register: EvidenceRegister
) -> dict[str, tuple[ChapterUse, ...]]:
    """Derive uses and return anchors from chapter evidence metadata and bodies."""

    matrix_ids = {entry.identifier for entry in register.entries}
    registered = matrix_ids | set(register.calculation_map)
    usage: dict[str, list[ChapterUse]] = defaultdict(list)
    study_root = publication_root / "content" / "02-estudio"
    chapter_three = (
        publication_root
        / "content/01-catastro/03-expediente-sorribos-santibanez.qmd"
    )
    chapter_paths = [
        *([chapter_three] if chapter_three.is_file() else []),
        *sorted(study_root.glob("[0-9][0-9]-*.qmd")),
    ]
    for path in chapter_paths:
        number = int(path.name[:2])
        if number != 3 and not 5 <= number <= 13:
            continue
        metadata, body = _front_matter_and_body(path)
        evidence = metadata.get("evidence")
        if not isinstance(evidence, dict):
            raise ApparatusBuildError(
                f"{path}: el capítulo {number} no declara evidencia estructurada."
            )
        for values in evidence.values():
            if not isinstance(values, list):
                raise ApparatusBuildError(
                    f"{path}: los grupos de evidencia deben ser listas."
                )
            for identifier in values:
                identifier = str(identifier)
                if identifier not in registered:
                    raise ApparatusBuildError(
                        f"{path}: uso de evidencia inexistente {identifier}."
                    )
                if identifier in matrix_ids:
                    chapter = ChapterUse(
                        number=number,
                        title=str(metadata.get("title", f"Capítulo {number}")),
                        path="../" + path.relative_to(publication_root).as_posix(),
                        anchor=_evidence_anchor(body, identifier),
                    )
                    if chapter not in usage[identifier]:
                        usage[identifier].append(chapter)
    return {identifier: tuple(chapters) for identifier, chapters in usage.items()}


def _declared_glossary_blob(publication_root: Path, actual: str) -> str:
    path = publication_root / "meta" / "publication.yml"
    try:
        data = yaml.safe_load(_read_text(path))
    except yaml.YAMLError as exc:
        raise ApparatusBuildError(f"{path}: YAML inválido: {exc}") from exc
    fields = data.get("sources", {}).get("glossary", {}) if isinstance(data, dict) else {}
    declared = fields.get("git_blob") if isinstance(fields, dict) else None
    if declared != actual:
        raise ApparatusBuildError(
            "publication.yml no declara el blob Git vigente del Glosario: "
            f"{declared!r}; esperado {actual}."
        )
    if fields.get("version"):
        raise ApparatusBuildError(
            "publication.yml no debe inventar una versión para Glosario.md."
        )
    return actual


def load_apparatus_data(
    repository_root: Path,
    publication_root: Path,
    manuscript_name: str,
) -> ApparatusData:
    repository_root = repository_root.resolve()
    publication_root = publication_root.resolve()
    glossary_path = repository_root / GLOSSARY_SOURCE
    glossary = load_glossary(glossary_path)
    if glossary.version is not None:
        raise ApparatusBuildError(
            f"{GLOSSARY_SOURCE}: se esperaba una fuente canónica sin versión explícita."
        )
    glossary_blob = _declared_glossary_blob(
        publication_root, git_blob_oid(glossary_path.read_bytes())
    )
    register = load_evidence_register(repository_root / REGISTER_SOURCE)
    specs = load_unit_specs(repository_root / UNITS_SOURCE)
    critical_units = parse_critical_edition(
        _read_text(repository_root / CRITICAL_SOURCE), specs, manuscript_name
    )
    modernized = load_modernized_edition(repository_root / MODERNIZED_SOURCE)
    validate_concordance_units(modernized, tuple(spec.label for spec in specs))
    validate_glossary_references(
        glossary,
        tuple(spec.label for spec in specs),
        source=GLOSSARY_SOURCE.as_posix(),
    )
    return ApparatusData(
        glossary=glossary,
        glossary_git_blob=glossary_blob,
        register=register,
        specs=specs,
        critical_units=critical_units,
        modernized=modernized,
        evidence_usage=_evidence_usage(publication_root, register),
    )


def _link_glossary_text(text: str, data: ApparatusData) -> str:
    term_anchors = {entry.term: entry.anchor for entry in data.glossary.entries}
    linked = text
    for term, anchor in sorted(term_anchors.items(), key=lambda item: -len(item[0])):
        linked = linked.replace(
            f"Glosario: `{term}`", f"Glosario: [`{term}`](#{anchor})"
        )
    anchors = {
        spec.label.casefold(): published_unit_anchor(spec) for spec in data.specs
    }

    def folio_link(match: re.Match[str]) -> str:
        visible = match.group(0)
        spec_anchor = anchors.get(visible.casefold())
        return (
            f"[{visible}](15-transcripcion.qmd#{spec_anchor})"
            if spec_anchor
            else visible
        )

    linked = re.sub(r"\bfolio \d{3}[rv]\b", folio_link, linked, flags=re.I)

    def response_link(match: re.Match[str]) -> str:
        number = int(match.group("number"))
        visible = match.group(0)
        if not 1 <= number <= 40:
            return visible
        return f"[{visible}](16-edicion-modernizada.qmd#respuesta-{number})"

    return re.sub(
        r"\brespuesta (?P<number>\d+)(?:\.ª)?", response_link, linked, flags=re.I
    )


def glossary_sort_key(value: str) -> tuple[tuple[tuple[str, int], ...], str]:
    """Return a deterministic, locale-independent Spanish alphabetical key.

    Case and vowel diacritics do not affect the primary order. The Spanish
    letter ñ remains distinct and sorts after every ordinary n word and before
    o. Visible spelling is retained as a deterministic tie-breaker.
    """

    normalized = unicodedata.normalize("NFC", " ".join(value.split())).casefold()
    primary: list[tuple[str, int]] = []
    for character in normalized:
        if character == "ñ":
            primary.append(("n", 1))
            continue
        decomposed = unicodedata.normalize("NFD", character)
        bases = "".join(item for item in decomposed if not unicodedata.combining(item))
        for base in bases:
            if base.isalnum():
                primary.append((base, 0))
            elif base.isspace() and primary and primary[-1] != (" ", 0):
                primary.append((" ", 0))
    while primary and primary[-1] == (" ", 0):
        primary.pop()
    return tuple(primary), normalized


def glossary_qmd(data: ApparatusData) -> str:
    entries = tuple(sorted(data.glossary.entries, key=lambda entry: glossary_sort_key(entry.term)))
    chunks = [
        f'''---
subtitle: "Parte VI. Aparatos e índices"
chapter-id: glosario-historico
publication-status: generated
numbered: false
number-sections: false
sources:
  - {GLOSSARY_SOURCE.as_posix()}
source-git-blob: "{data.glossary_git_blob}"
---

# Glosario histórico {{.unnumbered}}

Las definiciones, referencias y notas proceden íntegramente del Glosario
canónico. Los enlaces de navegación se añaden sin modificar su contenido.

## Entradas {{#glosario-entradas .unnumbered}}

''' + " · ".join(
            f"[{entry.term}](#{entry.anchor})" for entry in entries
        )
    ]
    for entry in entries:
        chunks.append(
            f"""### {entry.term} {{#{entry.anchor} .unnumbered}}

**Término documentado:** {_link_glossary_text(entry.documented_term, data)}

**Definición:** {_link_glossary_text(entry.definition, data)}

**Primera unidad:** {_link_glossary_text(entry.first_unit, data)}

**Referencias:** {_link_glossary_text(entry.references, data)}

**Notas:** {_link_glossary_text(entry.notes, data)}"""
        )
    return "\n\n".join(chunks).rstrip() + "\n"


def quantitative_qmd(data: ApparatusData) -> str:
    chunks = [
        f'''---
subtitle: "Parte VI. Aparatos e índices"
chapter-id: cuadros-cuantitativos
publication-status: generated
numbered: false
number-sections: false
sources:
  - {REGISTER_SOURCE.as_posix()}
  - {STUDY_SOURCE.as_posix()}
source-version: "{data.register.version}"
---

# Cuadros cuantitativos {{.unnumbered}}

Esta vista reúne las entradas cuyo nivel canónico es `C` y los cálculos `CAL-*`
a los que remiten. Los resultados se publican tal como figuran en el Registro:
no se recalculan, convierten ni agregan.
'''
    ]
    current_section = None
    for entry in data.register.calculated_entries:
        if entry.section != current_section:
            current_section = entry.section
            chunks.append(f"## {current_section} {{.unnumbered}}")
        calculations = data.register.associated_calculations(entry)
        rows = "\n".join(
            "| {identifier} | {operation} | {result} | {inputs} | {condition} |".format(
                identifier=calculation.identifier,
                operation=calculation.operation,
                result=calculation.result,
                inputs=calculation.inputs,
                condition=calculation.condition,
            )
            for calculation in calculations
        )
        chunks.append(
            f"""### {entry.identifier} {{#cuadro-{entry.identifier.casefold()} .unnumbered}}

**Afirmación C:** {entry.statement}

**Evidencia:** {entry.evidence}

**Estado y cautela:** {entry.status_caution}

| ID de cálculo | Operación o regla | Resultado y unidad | Entradas documentales | Condición de uso |
|---|---|---|---|---|"""
            + "\n"
            + rows
        )
    chunks.append(
        "Los cálculos `CAL-018`, `CAL-019` y `CAL-020` son controles internos "
        "asociados en el Registro a entradas documentales, no a entradas de nivel `C`; "
        "por ello no se presentan como resultados C en estos cuadros."
    )
    return "\n\n".join(chunks).rstrip() + "\n"


def _unit_response_map(data: ApparatusData) -> dict[str, tuple[int, ...]]:
    response_units = response_unit_labels(data.modernized)
    mapping: dict[str, list[int]] = {spec.label: [] for spec in data.specs}
    for number, labels in response_units.items():
        for label in labels:
            mapping[label].append(number)
    return {label: tuple(numbers) for label, numbers in mapping.items()}


def _special_modernized_links(content: str) -> tuple[tuple[str, str], ...]:
    links: list[tuple[str, str]] = []
    if content == "Portada":
        links.append(("Portada", "modernizada-portada"))
    if "Comparecencia" in content:
        links.append(("Comparecencia", "comparecencia"))
    if "ratificación" in content.casefold():
        links.append(("Ratificación", "ratificacion-edades-firmas"))
    if "firmas" in content.casefold():
        links.append(("Firmas", "ratificacion-edades-firmas"))
    return tuple(links)


def _table(value: str) -> str:
    return value.replace("|", r"\|").replace("\n", " ")


def concordance_qmd(data: ApparatusData) -> str:
    by_label = {row.unit_label: row for row in data.modernized.concordance_rows}
    unit_responses = _unit_response_map(data)
    chunks = [
        f'''---
subtitle: "Parte VI. Aparatos e índices"
chapter-id: concordancia-general
publication-status: generated
numbered: false
number-sections: false
sources:
  - {UNITS_SOURCE.as_posix()}
  - {CRITICAL_SOURCE.as_posix()}
  - {MODERNIZED_SOURCE.as_posix()}
---

# Concordancia general {{.unnumbered}}

Las dos vistas proceden de una sola relación estructurada entre las 35 unidades
materiales y las 40 respuestas. Conservan las correspondencias muchos-a-muchos.

## Vista por unidad {{#concordancia-unidades .unnumbered}}

| Orden | Unidad | Página / posición | Facsímil | Transcripción | Contenido modernizado | Respuesta(s) |
|---:|---|---|---|---|---|---|'''
    ]
    for spec in data.specs:
        row = by_label[spec.label]
        facsimile = (
            f"[p. {spec.pdf_page:02d}](14-facsimil.qmd#pagina-digital-{spec.pdf_page:02d})"
        )
        transcription = (
            f"[{spec.label}](15-transcripcion.qmd#{published_unit_anchor(spec)})"
        )
        modern_links = [
            f"[{label}](16-edicion-modernizada.qmd#{anchor})"
            for label, anchor in _special_modernized_links(row.content)
        ]
        modern_links.extend(
            f"[R{number}](16-edicion-modernizada.qmd#respuesta-{number})"
            for number in unit_responses[spec.label]
        )
        links = "; ".join(modern_links) if modern_links else "—"
        chunks.append(
            f"| {spec.order} | {_table(spec.label)} | {spec.pdf_page} / `{spec.position}` | "
            f"{facsimile} | {transcription} | {_table(row.content)} | {links} |"
        )
    chunks.append(
        """## Vista por respuesta {#concordancia-respuestas .unnumbered}

| Respuesta | Capítulo 16 | Unidad(es) del capítulo 15 | Folio(s) implicado(s) | Página(s) facsimilares |
|---:|---|---|---|---|"""
    )
    specs_by_label = {spec.label: spec for spec in data.specs}
    response_units = response_unit_labels(data.modernized)
    for number in range(1, 41):
        labels = response_units[number]
        units = "; ".join(
            f"[{label}](15-transcripcion.qmd#{published_unit_anchor(specs_by_label[label])})"
            for label in labels
        )
        pages = []
        for label in labels:
            page = specs_by_label[label].pdf_page
            if page not in pages:
                pages.append(page)
        page_links = "; ".join(
            f"[p. {page:02d}](14-facsimil.qmd#pagina-digital-{page:02d})"
            for page in pages
        )
        chunks.append(
            f"| {number} | [Respuesta {number}](16-edicion-modernizada.qmd#respuesta-{number}) "
            f"| {units} | {_table('; '.join(labels))} | {page_links} |"
        )
    return "\n".join(chunks).rstrip() + "\n"


def _status_class(status: str) -> str:
    if status.startswith("Admitida"):
        return "admitida"
    if status.startswith("Condicionada") or status.startswith("Mantener cautela"):
        return "condicionada"
    if status.startswith("Excluida"):
        return "excluida"
    return "no-especificado"


def evidence_matrix_qmd(data: ApparatusData) -> str:
    chunks = [
        f'''---
subtitle: "Parte VI. Aparatos e índices"
chapter-id: matriz-evidencia
publication-status: generated
numbered: false
number-sections: false
sources:
  - {REGISTER_SOURCE.as_posix()}
source-version: "{data.register.version}"
usage-derived-from: chapter-evidence-metadata-3-and-5-13
---

# Matriz de evidencia D/C/I/E/L {{.unnumbered}}

La matriz reproduce el Registro {data.register.version}; no convierte sus formulaciones en prosa
narrativa ni corrige sus cautelas. `D` identifica dato documental; `C`, cálculo;
`I`, interpretación; `E`, contexto externo; y `L`, límite. Los niveles compuestos
se conservan literalmente. Los estados admitido, condicionado y excluido se
distinguen visualmente; un guion indica que la tabla canónica no declara una
columna separada de estado y cautela.
'''
    ]
    current_section = None
    for entry in data.register.entries:
        section = entry.section
        if section == "Sin subsección":
            section = (
                "Interpretaciones autorizables"
                if entry.level == "I" and entry.identifier.startswith("INT-")
                else "Límites y discrepancias"
            )
        if section != current_section:
            current_section = section
            chunks.append(f"## {section} {{.unnumbered}}")
        uses = data.evidence_usage.get(entry.identifier, ())
        usage = (
            "; ".join(
                f"[cap. {chapter.number}: {chapter.title}]({chapter.path}"
                f"#{chapter.anchor if chapter.anchor else ''})"
                for chapter in uses
            )
            if uses
            else "—"
        )
        status = entry.status_caution or "—"
        citation_keys = EVIDENCE_CITATIONS.get(entry.identifier, ())
        bibliography = (
            "[" + "; ".join(f"@{key}" for key in citation_keys) + "]"
            if citation_keys
            else "—"
        )
        chunks.append(
            f"""::: {{.evidence-entry .evidence-state-{_status_class(entry.status_caution)}}}
### {entry.identifier} {{#evidencia-{entry.identifier.casefold()} .unnumbered}}

**Formulación canónica:** {entry.statement}

**Nivel:** `{entry.level}`

**Evidencia:** {entry.evidence}

**Referencia bibliográfica:** {bibliography}

**Estado y cautela:** {status}

**Uso en el libro:** {usage}
:::
""".rstrip()
        )
    return "\n\n".join(chunks).rstrip() + "\n"


def generated_apparatus(data: ApparatusData) -> dict[str, str]:
    return {
        "glosario.qmd": glossary_qmd(data),
        "cuadros-cuantitativos.qmd": quantitative_qmd(data),
        "concordancia.qmd": concordance_qmd(data),
        "matriz-evidencia.qmd": evidence_matrix_qmd(data),
    }


def _difference_context(expected: str, actual: str) -> tuple[int, str]:
    context = "documento"
    for number, (wanted, found) in enumerate(
        zip_longest(expected.splitlines(), actual.splitlines(), fillvalue=""), start=1
    ):
        if wanted.startswith(("## ", "### ")):
            context = wanted.lstrip("# ").split(" {#", 1)[0]
        elif wanted.startswith("**") and ":**" in wanted:
            field = wanted.split(":**", 1)[0].strip("*")
            context = f"{context}, campo {field}"
        if wanted != found:
            return number, context
    return 0, context


def validate_apparatus_fidelity(data: ApparatusData, actual: dict[str, str]) -> None:
    expected = generated_apparatus(data)
    if set(actual) != set(expected):
        raise ApparatusBuildError(
            "Salidas 4D incorrectas: " + ", ".join(sorted(actual))
        )
    for name in OUTPUT_NAMES:
        if actual[name] != expected[name]:
            line, context = _difference_context(expected[name], actual[name])
            raise ApparatusBuildError(
                f"{name}, {context}: discordancia con la fuente en la línea {line}."
            )


def _write_qmd(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8", newline="\n")
    temporary.replace(path)


def build_apparatus(
    repository_root: Path,
    publication_root: Path,
    manuscript_name: str,
) -> tuple[Path, ...]:
    """Rebuild only the four QMD files owned by the Phase 4D generator."""

    repository_root = repository_root.resolve()
    publication_root = publication_root.resolve()
    try:
        data = load_apparatus_data(repository_root, publication_root, manuscript_name)
    except ApparatusSourceError as exc:
        raise ApparatusBuildError(str(exc)) from exc
    contents = generated_apparatus(data)
    validate_apparatus_fidelity(data, contents)
    generated_root = (publication_root / "generated").resolve()
    outputs = tuple(generated_root / name for name in OUTPUT_NAMES)
    if any(path.parent != generated_root for path in outputs):
        raise ApparatusBuildError("Ruta de salida 4D insegura.")
    for path in outputs:
        _write_qmd(path, contents[path.name])
    return outputs


__all__ = [
    "ApparatusBuildError",
    "ApparatusData",
    "ChapterUse",
    "EVIDENCE_CITATIONS",
    "OUTPUT_NAMES",
    "build_apparatus",
    "concordance_qmd",
    "evidence_matrix_qmd",
    "generated_apparatus",
    "glossary_qmd",
    "load_apparatus_data",
    "quantitative_qmd",
    "validate_apparatus_fidelity",
]

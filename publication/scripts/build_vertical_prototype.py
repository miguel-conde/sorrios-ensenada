#!/usr/bin/env python3
"""Build the strictly bounded Phase 2B vertical prototype."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image

from check_sources import (
    ManuscriptMetadata,
    SourceCheckError,
    verify_local_manuscript,
)


MANUSCRIPT_FILE_ID = "1GgBs68iTi53ue8-TbrYFABALxadhQe5u"
MANUSCRIPT_NAME = "sorrios_ensenada_orden_lectura_calidad_original.pdf"
MANUSCRIPT_SIZE = 5_038_575
MANUSCRIPT_SHA256 = "d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24"
MANUSCRIPT_PAGES = 18
PROTOTYPE_PAGE = 12
PROTOTYPE_UNIT = "folio_315v"
PROTOTYPE_RESPONSE = 17
RENDER_DPI = 180
PALEOGRAPHIC_LINE_COUNT = 18
PALEOGRAPHIC_SECTION = "Transcripción paleográfica"
EVIDENCE_GROUPS = {
    "D": ("HID-001", "HID-003", "HID-005", "HID-006"),
    "C": ("HID-002", "HID-004", "CAL-012", "CAL-013"),
    "I": ("HID-007", "INT-005"),
    "E": ("HID-008",),
    "L": ("LIM-005", "LIM-010"),
}


class PrototypeBuildError(RuntimeError):
    """Raised when the bounded prototype cannot be generated safely."""


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise PrototypeBuildError(f"No se pudo leer {path}: {exc}") from exc


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(content.rstrip() + "\n")


def _heading_block(text: str, heading: str) -> str:
    lines = text.splitlines()
    try:
        start = lines.index(heading)
    except ValueError as exc:
        raise PrototypeBuildError(f"No se encontró la sección: {heading}") from exc
    level = len(heading) - len(heading.lstrip("#"))
    end = len(lines)
    for index in range(start + 1, len(lines)):
        candidate = lines[index]
        if candidate.startswith("#"):
            candidate_level = len(candidate) - len(candidate.lstrip("#"))
            if candidate_level <= level:
                end = index
                break
    block = lines[start:end]
    while block and block[-1].strip() in {"", "---"}:
        block.pop()
    return "\n".join(block)


def _subsections(block: str) -> dict[str, str]:
    result: dict[str, list[str]] = {}
    current: str | None = None
    for line in block.splitlines()[1:]:
        if line.startswith("### "):
            current = line[4:].strip()
            result[current] = []
        elif current is not None:
            result[current].append(line)
    return {name: "\n".join(lines).strip() for name, lines in result.items()}


def read_paleographic_lines(edition_text: str) -> tuple[str, ...]:
    """Return the authoritative physical lines for the prototype unit."""

    block = _heading_block(edition_text, "## Folio 315v")
    parts = _subsections(block)
    transcription = parts.get(PALEOGRAPHIC_SECTION)
    if transcription is None:
        raise PrototypeBuildError(
            f"Falta la sección canónica {PALEOGRAPHIC_SECTION} en folio 315v"
        )
    lines = tuple(transcription.splitlines())
    if len(lines) != PALEOGRAPHIC_LINE_COUNT or any(not line for line in lines):
        raise PrototypeBuildError(
            "La transcripción paleográfica de folio 315v debe contener exactamente "
            f"{PALEOGRAPHIC_LINE_COUNT} líneas no vacías; contiene {len(lines)}."
        )
    return lines


def _line_block(lines: tuple[str, ...]) -> str:
    """Emit one Pandoc line block shared by the HTML and PDF renderers."""

    return "\n".join(f"| {line}" for line in lines)


def read_evidence_rows(register_text: str) -> dict[str, list[str]]:
    expected = {item for items in EVIDENCE_GROUPS.values() for item in items}
    rows: dict[str, list[str]] = {}
    for line in register_text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and cells[0] in expected:
            rows[cells[0]] = cells
    missing = sorted(expected - rows.keys())
    if missing:
        raise PrototypeBuildError(
            "Faltan identificadores en el Registro vigente: " + ", ".join(missing)
        )
    return rows


def _study_table(section: str) -> str:
    lines = section.splitlines()
    start = next(
        (index for index, line in enumerate(lines) if line.startswith("| Activo |")),
        None,
    )
    if start is None:
        raise PrototypeBuildError("No se encontró el cuadro de molinos en la sección 10")
    table: list[str] = []
    for line in lines[start:]:
        if not line.startswith("|"):
            break
        table.append(line)
    if len(table) != 10:
        raise PrototypeBuildError(
            f"El cuadro de molinos debe tener cabecera y ocho filas; tiene {len(table)} líneas"
        )
    return "\n".join(table)


def _footnote(text: str, label: str) -> str:
    match = re.search(rf"^\[\^{re.escape(label)}\]: .+$", text, re.MULTILINE)
    if match is None:
        raise PrototypeBuildError(f"No se encontró la nota {label} de la respuesta 17")
    return match.group(0)


def verify_manuscript(pdf: Path, project_file: Path) -> None:
    """Compatibility wrapper; source validation now lives in check_sources.py."""

    del project_file
    metadata = ManuscriptMetadata(
        MANUSCRIPT_FILE_ID,
        MANUSCRIPT_NAME,
        MANUSCRIPT_SHA256,
        MANUSCRIPT_SIZE,
        MANUSCRIPT_PAGES,
    )
    try:
        verify_local_manuscript(pdf, metadata)
    except SourceCheckError as exc:
        raise PrototypeBuildError(str(exc)) from exc


def _load_render_unit(repository_root: Path):
    tools_dir = repository_root / "plugins" / "sorrios-ensenada" / "tools"
    if str(tools_dir) not in sys.path:
        sys.path.insert(0, str(tools_dir))
    try:
        from render_unit import find_pdftoppm, render_unit
    except (ImportError, ModuleNotFoundError) as exc:
        raise PrototypeBuildError(
            "No se pudo cargar la lógica canónica de render_unit.py"
        ) from exc
    return find_pdftoppm, render_unit


def _render_images(
    repository_root: Path,
    publication_root: Path,
    pdf: Path,
    generated_root: Path,
) -> None:
    find_pdftoppm, render_unit = _load_render_unit(repository_root)
    executable = find_pdftoppm()
    assets = generated_root / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    page_prefix = assets / "manuscript-page-12"
    try:
        subprocess.run(
            [
                executable,
                "-f",
                str(PROTOTYPE_PAGE),
                "-l",
                str(PROTOTYPE_PAGE),
                "-singlefile",
                "-r",
                str(RENDER_DPI),
                "-png",
                pdf,
                page_prefix,
            ],
            check=True,
            shell=False,
        )
        render_unit(
            pdf,
            repository_root / "project" / "00_CONTROL" / "unidades.yaml",
            PROTOTYPE_UNIT,
            assets / "folio-315v.png",
            dpi=RENDER_DPI,
            pdftoppm=executable,
        )
        prototype_crop = assets / "folio-315v.png"
        compressed_crop = assets / "folio-315v.compressed.png"
        with Image.open(prototype_crop) as image:
            image.load()
            image.save(compressed_crop, format="PNG", compress_level=9)
        compressed_crop.replace(prototype_crop)
    except (OSError, subprocess.CalledProcessError, RuntimeError) as exc:
        raise PrototypeBuildError(f"No se pudieron generar las imágenes: {exc}") from exc


def _facsimile_page() -> str:
    return """---
title: "Facsímil del prototipo"
chapter-id: facsimil-pagina-12
publication-status: prototype
sources:
  - manuscript:file_id:1GgBs68iTi53ue8-TbrYFABALxadhQe5u
lightbox: true
---

## Página digital 12 {#pagina-digital-12}

::: {.prototype-facsimile}
![Página digital 12 completa del manuscrito autoritativo: folio 315v a la izquierda y folio 316r a la derecha.](assets/manuscript-page-12.png){#fig-pagina-digital-12 fig-alt="Página manuscrita completa con dos folios: 315v a la izquierda y 316r a la derecha." fig-pos="H" width="88%"}
:::

La imagen procede exclusivamente de la página digital 12 del PDF autoritativo.
Se conserva completa para mostrar márgenes, pliegue central, foliación y
continuidad material. En HTML puede ampliarse; el recorte de lectura se ofrece
en la unidad paleográfica.

[Volver al capítulo histórico](../content/02-estudio/09-rio-molinos-recursos.qmd).
"""


def _transcription_page(edition_text: str) -> str:
    block = _heading_block(edition_text, "## Folio 315v")
    parts = _subsections(block)
    required = (
        "Imagen",
        "Transcripción paleográfica",
        "Observaciones editoriales",
        "Notas paleográficas",
        "Notas históricas",
        "Referencias cruzadas",
    )
    missing = [name for name in required if name not in parts]
    if missing:
        raise PrototypeBuildError(
            "Faltan secciones canónicas en folio 315v: " + ", ".join(missing)
        )
    paleographic_lines = read_paleographic_lines(edition_text)
    chunks = [
        """---
title: "Transcripción y aparato del prototipo"
chapter-id: transcripcion-folio-315v
publication-status: prototype
sources:
  - project/20_TRABAJO_EDITORIAL/Edicion_Critica.md#folio-315v
lightbox: true
---

## Folio 315v {#folio-315v}

### Imagen

::: {.prototype-unit}
![Recorte de folio 315v, mitad izquierda de la página digital 12 del manuscrito autoritativo.](assets/folio-315v.png){#fig-folio-315v fig-alt="Folio manuscrito 315v, recortado de la mitad izquierda de la página digital 12." fig-pos="H" width="65%"}
:::
"""
    ]
    for name in required[1:]:
        content = (
            _line_block(paleographic_lines)
            if name == PALEOGRAPHIC_SECTION
            else parts[name]
        )
        chunks.append(f"### {name}\n\n{content}\n")
    chunks.append(
        "[Volver al capítulo histórico](../content/02-estudio/09-rio-molinos-recursos.qmd)."
    )
    return "\n".join(chunks)


def _modernized_page(modernized_text: str) -> str:
    block = _heading_block(
        modernized_text, "## Respuesta 17. Minas, molinos y otros artefactos"
    )
    body = "\n".join(block.splitlines()[1:]).strip()
    return f"""---
title: "Edición modernizada del prototipo"
chapter-id: modernizada-respuesta-17
publication-status: prototype
sources:
  - project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md#respuesta-17
---

## Respuesta 17. Minas, molinos y otros artefactos {{#respuesta-17}}

{body}

{_footnote(modernized_text, "20")}

{_footnote(modernized_text, "21")}

[Volver al capítulo histórico](../content/02-estudio/09-rio-molinos-recursos.qmd).
"""


def _escape_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def _apparatus_page(study_text: str, register_text: str) -> str:
    section = _heading_block(study_text, "## 10. Río, molinos y capacidad de transformación")
    table = _study_table(section)
    rows = read_evidence_rows(register_text)
    matrix = [
        "| Nivel | ID | Formulación o regla | Estado, cautela o límite |",
        "|---|---|---|---|",
    ]
    for level, identifiers in EVIDENCE_GROUPS.items():
        for identifier in identifiers:
            cells = rows[identifier]
            formulation = cells[1]
            if identifier.startswith("CAL-") and len(cells) >= 5:
                formulation = f"{cells[1]} → {cells[2]}"
            matrix.append(
                "| "
                + " | ".join(
                    (
                        level,
                        identifier,
                        _escape_cell(formulation),
                        _escape_cell(cells[-1]),
                    )
                )
                + " |"
            )
    return f"""---
title: "Cuadro y aparato de evidencia del prototipo"
chapter-id: aparato-molinos
publication-status: prototype
sources:
  - project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md#seccion-10
  - project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md
---

## Ruedas, titulares y utilidades {{#cuadro-molinos}}

{table}

Las 26 cargas corresponden solo a las ocho ruedas descritas. Los cuatro
quartales del venturero se mantienen separados y su número de ruedas permanece
abierto.

## Fragmento D/C/I/E/L {{#matriz-molinera}}

{chr(10).join(matrix)}

La columna «Nivel» sigue la muestra fijada para este prototipo. Cuando el
Registro combina niveles —como en HID-008— la matriz conserva su formulación y
su cautela, pero lo presenta aquí por su función contextual E.

[Volver al capítulo histórico](../content/02-estudio/09-rio-molinos-recursos.qmd).
"""


def build_vertical_prototype(
    repository_root: Path,
    publication_root: Path,
    manuscript_pdf: Path,
) -> tuple[Path, ...]:
    repository_root = repository_root.resolve()
    publication_root = publication_root.resolve()
    manuscript_pdf = manuscript_pdf.expanduser().resolve()
    generated_root = publication_root / "generated"
    if generated_root.parent != publication_root or generated_root.name != "generated":
        raise PrototypeBuildError("Ruta generated insegura")
    source_paths = {
        "study": repository_root
        / "project"
        / "30_RESULTADOS"
        / "ESTUDIO_HISTORICO"
        / "Estudio_Historico.md",
        "register": repository_root
        / "project"
        / "30_RESULTADOS"
        / "ESTUDIO_HISTORICO"
        / "Registro_Afirmaciones_Calculos_v1.md",
        "edition": repository_root
        / "project"
        / "20_TRABAJO_EDITORIAL"
        / "Edicion_Critica.md",
        "modernized": repository_root
        / "project"
        / "30_RESULTADOS"
        / "EDICION_DIVULGATIVA"
        / "Catastro_Sorrios_1752_Version_Modernizada.md",
    }
    texts = {name: _read_text(path) for name, path in source_paths.items()}
    generated_root.mkdir(parents=True, exist_ok=True)
    owned_paths = (
        generated_root / "14-facsimil-prototipo.qmd",
        generated_root / "15-transcripcion-prototipo.qmd",
        generated_root / "16-modernizada-prototipo.qmd",
        generated_root / "aparato-molinos.qmd",
        generated_root / "assets" / "manuscript-page-12.png",
        generated_root / "assets" / "folio-315v.png",
    )
    for path in owned_paths:
        if path.is_file():
            path.unlink()
    _render_images(repository_root, publication_root, manuscript_pdf, generated_root)
    outputs = {
        generated_root / "14-facsimil-prototipo.qmd": _facsimile_page(),
        generated_root
        / "15-transcripcion-prototipo.qmd": _transcription_page(texts["edition"]),
        generated_root
        / "16-modernizada-prototipo.qmd": _modernized_page(texts["modernized"]),
        generated_root
        / "aparato-molinos.qmd": _apparatus_page(texts["study"], texts["register"]),
    }
    for path, content in outputs.items():
        _write_text(path, content)
    prototype_images = (
        generated_root / "assets" / "manuscript-page-12.png",
        generated_root / "assets" / "folio-315v.png",
    )
    return tuple(sorted((*outputs.keys(), *prototype_images)))


__all__ = [
    "EVIDENCE_GROUPS",
    "MANUSCRIPT_FILE_ID",
    "MANUSCRIPT_PAGES",
    "MANUSCRIPT_SHA256",
    "MANUSCRIPT_SIZE",
    "PALEOGRAPHIC_LINE_COUNT",
    "PALEOGRAPHIC_SECTION",
    "PROTOTYPE_PAGE",
    "PROTOTYPE_RESPONSE",
    "PROTOTYPE_UNIT",
    "PrototypeBuildError",
    "build_vertical_prototype",
    "read_paleographic_lines",
    "read_evidence_rows",
]

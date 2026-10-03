#!/usr/bin/env python3
"""Validate the developing publication and the bounded Phase 2B regression."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

import yaml

from build_vertical_prototype import (
    EVIDENCE_GROUPS,
    MANUSCRIPT_FILE_ID,
    PALEOGRAPHIC_LINE_COUNT,
    PALEOGRAPHIC_SECTION,
    PrototypeBuildError,
    read_paleographic_lines,
)


PUBLICATION_ROOT = Path(__file__).resolve().parent.parent
REPOSITORY_ROOT = PUBLICATION_ROOT.parent
CHAPTER_ONE = (
    PUBLICATION_ROOT / "content" / "01-catastro" / "01-catastro-ensenada.qmd"
)
CHAPTER_TWO = (
    PUBLICATION_ROOT
    / "content"
    / "01-catastro"
    / "02-respuestas-generales-interrogatorio.qmd"
)
CHAPTER_THREE = (
    PUBLICATION_ROOT
    / "content"
    / "01-catastro"
    / "03-expediente-sorribos-santibanez.qmd"
)
CHAPTER_FOUR = (
    PUBLICATION_ROOT
    / "content"
    / "01-catastro"
    / "04-manuscrito-volumen-actual.qmd"
)
CHAPTER_FIVE = (
    PUBLICATION_ROOT
    / "content"
    / "02-estudio"
    / "05-lugar-senorio-concejo-ordas.qmd"
)
CHAPTER_SIX = (
    PUBLICATION_ROOT
    / "content"
    / "02-estudio"
    / "06-vecinos-hogares-viviendas-trabajo.qmd"
)
CHAPTER_SEVEN = (
    PUBLICATION_ROOT
    / "content"
    / "02-estudio"
    / "07-tierra-sistema-agrario-medidas.qmd"
)
PROTOTYPE_CHAPTER = (
    PUBLICATION_ROOT / "content" / "02-estudio" / "09-rio-molinos-recursos.qmd"
)
GENERATED = {
    "facsimile": PUBLICATION_ROOT / "generated" / "14-facsimil-prototipo.qmd",
    "transcription": PUBLICATION_ROOT / "generated" / "15-transcripcion-prototipo.qmd",
    "modernized": PUBLICATION_ROOT / "generated" / "16-modernizada-prototipo.qmd",
    "apparatus": PUBLICATION_ROOT / "generated" / "aparato-molinos.qmd",
}
CANONICAL_EDITION = (
    REPOSITORY_ROOT / "project" / "20_TRABAJO_EDITORIAL" / "Edicion_Critica.md"
)
RENDERED_HTML = (
    PUBLICATION_ROOT / "_book" / "generated" / "15-transcripcion-prototipo.html"
)
RENDERED_CHAPTER_ONE_HTML = (
    PUBLICATION_ROOT
    / "_book"
    / "content"
    / "01-catastro"
    / "01-catastro-ensenada.html"
)
RENDERED_CHAPTER_TWO_HTML = (
    PUBLICATION_ROOT
    / "_book"
    / "content"
    / "01-catastro"
    / "02-respuestas-generales-interrogatorio.html"
)
RENDERED_CHAPTER_THREE_HTML = (
    PUBLICATION_ROOT
    / "_book"
    / "content"
    / "01-catastro"
    / "03-expediente-sorribos-santibanez.html"
)
RENDERED_CHAPTER_FOUR_HTML = (
    PUBLICATION_ROOT
    / "_book"
    / "content"
    / "01-catastro"
    / "04-manuscrito-volumen-actual.html"
)
RENDERED_CHAPTER_FIVE_HTML = (
    PUBLICATION_ROOT
    / "_book"
    / "content"
    / "02-estudio"
    / "05-lugar-senorio-concejo-ordas.html"
)
RENDERED_CHAPTER_SIX_HTML = (
    PUBLICATION_ROOT
    / "_book"
    / "content"
    / "02-estudio"
    / "06-vecinos-hogares-viviendas-trabajo.html"
)
RENDERED_CHAPTER_SEVEN_HTML = (
    PUBLICATION_ROOT
    / "_book"
    / "content"
    / "02-estudio"
    / "07-tierra-sistema-agrario-medidas.html"
)
RENDERED_PDF = (
    PUBLICATION_ROOT / "_book" / "sorribos-santibanez-ordas-1752.pdf"
)
UNIT_HEADINGS = (
    "Imagen",
    PALEOGRAPHIC_SECTION,
    "Observaciones editoriales",
    "Notas paleográficas",
    "Notas históricas",
    "Referencias cruzadas",
)
DOCUMENTARY_HYPHEN_ENDINGS = (
    "Bartho-",
    "pro-",
    "invier-",
    "respec-",
    "An-",
    "Manu-",
    "re-",
)
CANONICAL_FORMULA = (
    "ocho ruedas descritas en cuatro casas de molinos; además existe un molino "
    "venturero cuyo número de ruedas no consta"
)
CHAPTER_ONE_SOURCE_PATHS = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Introduccion_Catastro_Ensenada_Sorrios.md",
    "project/00_CONTROL/Manual_Editorial.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
}
CHAPTER_ONE_LINKS = {
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=10",
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=32",
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=33",
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=40",
    "https://www.catastro.hacienda.gob.es/es-ES/fondo_editorial.html",
}
CHAPTER_TWO_SOURCE_PATHS = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Introduccion_Catastro_Ensenada_Sorrios.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Verificacion_Interrogatorio_40_Preguntas.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/00_CONTROL/Manual_Editorial.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
}
CHAPTER_TWO_LINKS = {
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=30",
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=31b",
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=32",
    "https://www.catastro.hacienda.gob.es/documentos/publicaciones/catalogoensenada_1752_vera.pdf",
}
CHAPTER_THREE_SOURCE_PATHS = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Introduccion_Catastro_Ensenada_Sorrios.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/00_CONTROL/unidades.yaml",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
}
CHAPTER_THREE_EVIDENCE = {
    "D": ("JUR-001", "JUR-002", "JUR-003", "JUR-004", "TOP-001"),
    "I": ("TOP-002",),
    "E": (
        "TOP-004",
        "TOP-005",
        "TOP-007",
        "TOP-008",
        "TOP-009",
        "TOP-010",
        "TOP-011",
        "JUR-009",
    ),
}
CHAPTER_FOUR_SOURCE_PATHS = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Introduccion_Catastro_Ensenada_Sorrios.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/00_CONTROL/unidades.yaml",
    "project/00_CONTROL/Manual_Editorial.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Criterios_Edicion_Modernizada.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "docs/PLAN_MAESTRO_PUBLICACION_QUARTO.md",
    "publication/README.md",
}
CHAPTER_FIVE_SOURCE_PATHS = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Introduccion_Catastro_Ensenada_Sorrios.md",
}
CHAPTER_FIVE_EVIDENCE = {
    "D": ("JUR-001", "JUR-002", "JUR-005", "JUR-006", "FIS-012"),
    "E": ("JUR-007", "JUR-008"),
    "L": ("LIM-011",),
}
CHAPTER_FIVE_ANCHORS = (
    "lugar-actores",
    "lugar-concejo-municipio",
    "lugar-senorio-conde",
    "lugar-derechos",
    "lugar-termino",
    "lugar-sintesis",
)
CHAPTER_SIX_SOURCE_PATHS = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Oficios.md",
}
CHAPTER_SIX_EVIDENCE = {
    "D": (
        "DEM-001", "DEM-002", "DEM-003", "DEM-004", "GAN-007",
        "TRA-001", "TRA-002", "TRA-003", "TRA-004", "TRA-005", "FIS-007",
    ),
    "C": ("CAL-018", "CAL-019"),
    "I": ("INT-002", "INT-008", "INT-010"),
    "E": ("DEM-005", "DEM-006"),
    "L": ("LIM-001", "LIM-002", "LIM-008"),
}
CHAPTER_SIX_ANCHORS = (
    "vecinos-recuento",
    "avitadores-poblacion",
    "personas-hogares",
    "casas-viviendas",
    "trabajo-categorias",
    "trabajo-utilidades",
    "estructura-limites",
)
CHAPTER_SEVEN_SOURCE_PATHS = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Plan_Composicion_Volumen_0_5.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md",
}
CHAPTER_SEVEN_EVIDENCE = {
    "D": (
        "TER-001", "TER-002", "TER-003", "TER-004", "TER-005", "TER-006",
        "TER-010", "AGR-001", "AGR-002", "AGR-003", "AGR-007", "AGR-008",
        "AGR-010",
    ),
    "C": (
        "TER-007", "TER-008", "AGR-004", "AGR-005", "AGR-006", "AGR-009",
        "CAL-001", "CAL-002", "CAL-003", "CAL-004", "CAL-005", "CAL-006",
        "CAL-007", "CAL-008", "CAL-009",
    ),
    "I": ("INT-001", "INT-003"),
    "E": ("TER-011", "AGR-011", "AGR-012", "AGR-013"),
    "L": ("TER-009", "LIM-003", "LIM-004", "LIM-005", "LIM-006", "LIM-007", "LIM-009"),
}
CHAPTER_SEVEN_ANCHORS = (
    "tierra-clases",
    "tierra-calidades",
    "tierra-medidas",
    "tierra-cabida",
    "tierra-centeno",
    "tierra-ciclos",
    "tierra-rendimientos",
    "tierra-produccion-limites",
    "tierra-sintesis",
)
CHAPTER_TWO_THEMATIC_BLOCKS = (
    ("1–3", "Nombre, jurisdicción, término y límites"),
    ("4–14", "Tierras, árboles, medidas, cabidas, frutos y valores"),
    ("15–16", "Diezmos, primicia, voto y cuantía"),
    ("17", "Minas, salinas, molinos y otros artefactos"),
    ("18–20", "Esquileo, colmenas y ganados"),
    ("21–22", "Vecinos, casas y edificios"),
    ("23–28", "Propios, arbitrios, gastos, cargas y rentas enajenadas"),
    ("29–34", "Servicios, comercio y oficios"),
    ("35–39", "Jornaleros, pobres, embarcaciones, clérigos y conventos"),
    ("40", "Fincas o rentas del rey"),
)
QUESTIONNAIRE_MIN_DISTINCT_MARKERS = 20
QUESTIONNAIRE_MIN_CONSECUTIVE_MARKERS = 15
QUESTION_MARKER_PATTERNS = (
    re.compile(
        r"^(?:(?:pregunta|respuesta)\s+)?"
        r"(?P<number>[1-9]|[1-3]\d|40)\s*(?:[.):-]\s*|\s+|$)",
        re.IGNORECASE,
    ),
    re.compile(
        r"^\|\s*(?:(?:pregunta|respuesta)\s+)?"
        r"(?P<number>[1-9]|[1-3]\d|40)\s*\|",
        re.IGNORECASE,
    ),
)


class _LineBlockParser(HTMLParser):
    """Collect visible lines from semantic Pandoc line blocks."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.blocks: list[tuple[str, ...]] = []
        self._depth = 0
        self._lines: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        classes = (attributes.get("class") or "").split()
        if self._depth == 0 and tag == "div" and "line-block" in classes:
            self._depth = 1
            self._lines = [""]
        elif self._depth and tag == "br":
            self._lines.append("")
        elif self._depth:
            self._depth += 1

    def handle_startendtag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if self._depth and tag == "br":
            self._lines.append("")

    def handle_endtag(self, tag: str) -> None:
        if not self._depth:
            return
        self._depth -= 1
        if self._depth == 0:
            self.blocks.append(tuple(line.strip() for line in self._lines))
            self._lines = []

    def handle_data(self, data: str) -> None:
        if self._depth:
            self._lines[-1] += data


def _generated_paleographic_lines(text: str) -> tuple[str, ...]:
    match = re.search(
        rf"^### {re.escape(PALEOGRAPHIC_SECTION)}\s*$\n+(?P<body>.*?)(?=^### |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if match is None:
        return ()
    lines = [line for line in match.group("body").rstrip().splitlines() if line]
    if any(not line.startswith("| ") for line in lines):
        return ()
    return tuple(line[2:] for line in lines)


def _questionnaire_markers(text: str) -> tuple[int, ...]:
    markers: set[int] = set()
    for raw_line in text.splitlines():
        line = re.sub(r"^\s*(?:#{1,6}|>|[-+*])\s*", "", raw_line)
        line = line.translate(str.maketrans("", "", "*_`")).strip()
        for pattern in QUESTION_MARKER_PATTERNS:
            match = pattern.match(line)
            if match is not None:
                markers.add(int(match.group("number")))
                break
    return tuple(sorted(markers))


def _has_extensive_questionnaire_sequence(text: str) -> bool:
    markers = _questionnaire_markers(text)
    if len(markers) < QUESTIONNAIRE_MIN_DISTINCT_MARKERS:
        return False

    longest_run = 1
    current_run = 1
    for previous, current in zip(markers, markers[1:]):
        if current == previous + 1:
            current_run += 1
            longest_run = max(longest_run, current_run)
        else:
            current_run = 1
    return longest_run >= QUESTIONNAIRE_MIN_CONSECUTIVE_MARKERS


def _html_line_blocks(path: Path) -> list[tuple[str, ...]]:
    parser = _LineBlockParser()
    parser.feed(path.read_text(encoding="utf-8"))
    parser.close()
    return parser.blocks


def _pdf_text_lines(path: Path) -> tuple[str, ...]:
    executable = shutil.which("pdftotext")
    if executable is None:
        raise RuntimeError("No se encontró pdftotext en PATH")
    result = subprocess.run(
        [executable, "-layout", path, "-"],
        check=True,
        capture_output=True,
        text=True,
        shell=False,
    )
    return tuple(line.strip() for line in result.stdout.splitlines())


def _contains_ordered_lines(haystack: tuple[str, ...], needles: tuple[str, ...]) -> bool:
    position = 0
    for line in haystack:
        if position < len(needles) and line == needles[position]:
            position += 1
    return position == len(needles)


def validate_rendered_outputs() -> list[str]:
    """Validate lineation in the actual HTML and PDF book artifacts."""

    errors: list[str] = []
    canonical = read_paleographic_lines(CANONICAL_EDITION.read_text(encoding="utf-8"))
    if not RENDERED_CHAPTER_ONE_HTML.is_file():
        errors.append(f"Falta el HTML del capítulo 1: {RENDERED_CHAPTER_ONE_HTML}")
    else:
        chapter_html = RENDERED_CHAPTER_ONE_HTML.read_text(encoding="utf-8")
        if "El Catastro de Ensenada" not in chapter_html:
            errors.append("El HTML del capítulo 1 no contiene su título")
        if 'name="viewport"' not in chapter_html:
            errors.append("El HTML del capítulo 1 carece de metadatos adaptables")
        for url in CHAPTER_ONE_LINKS:
            encoded_url = url.replace("&", "&amp;")
            if url not in chapter_html and encoded_url not in chapter_html:
                errors.append(f"Falta el enlace institucional en HTML: {url}")

    if not RENDERED_CHAPTER_TWO_HTML.is_file():
        errors.append(f"Falta el HTML del capítulo 2: {RENDERED_CHAPTER_TWO_HTML}")
    else:
        chapter_two_html = RENDERED_CHAPTER_TWO_HTML.read_text(encoding="utf-8")
        if (
            "Las Respuestas Generales y el interrogatorio de cuarenta preguntas"
            not in chapter_two_html
        ):
            errors.append("El HTML del capítulo 2 no contiene su título")
        if 'name="viewport"' not in chapter_two_html:
            errors.append("El HTML del capítulo 2 carece de metadatos adaptables")
        for url in CHAPTER_TWO_LINKS:
            encoded_url = url.replace("&", "&amp;")
            if url not in chapter_two_html and encoded_url not in chapter_two_html:
                errors.append(f"Falta el enlace institucional de 3B en HTML: {url}")
        for question_range, subject in CHAPTER_TWO_THEMATIC_BLOCKS:
            if question_range not in chapter_two_html or subject not in chapter_two_html:
                errors.append(
                    f"Falta el bloque temático {question_range} en el HTML del capítulo 2"
                )

    rendered_chapters = (
        (
            RENDERED_CHAPTER_THREE_HTML,
            "El expediente de Sorribos y Santibáñez de Ordás",
            3,
            "04-manuscrito-volumen-actual.html",
        ),
        (
            RENDERED_CHAPTER_FOUR_HTML,
            "Del manuscrito al volumen actual",
            4,
            "03-expediente-sorribos-santibanez.html",
        ),
        (
            RENDERED_CHAPTER_FIVE_HTML,
            "Un lugar de señorío en el Concejo de Ordás",
            5,
            "04-manuscrito-volumen-actual.html",
        ),
        (
            RENDERED_CHAPTER_SIX_HTML,
            "Vecinos, hogares, viviendas y trabajo",
            6,
            "05-lugar-senorio-concejo-ordas.html",
        ),
        (
            RENDERED_CHAPTER_SEVEN_HTML,
            "Tierra, sistema agrario y medidas",
            7,
            "06-vecinos-hogares-viviendas-trabajo.html",
        ),
    )
    for path, title, number, linked_chapter in rendered_chapters:
        if not path.is_file():
            errors.append(f"Falta el HTML del capítulo {number}: {path}")
            continue
        html = path.read_text(encoding="utf-8")
        if title not in html:
            errors.append(f"El HTML del capítulo {number} no contiene su título")
        if 'name="viewport"' not in html:
            errors.append(
                f"El HTML del capítulo {number} carece de metadatos adaptables"
            )
        if linked_chapter not in html:
            errors.append(
                f"El HTML del capítulo {number} no conserva su enlace cruzado"
            )
        if number in (5, 6, 7) and not re.search(
            rf'class="chapter-number"[^>]*>\s*{number}\s*<', html
        ):
            errors.append(
                f"El capítulo {number} no aparece numerado realmente como {number}"
            )

    if not RENDERED_HTML.is_file():
        errors.append(f"Falta el HTML renderizado: {RENDERED_HTML}")
    else:
        blocks = _html_line_blocks(RENDERED_HTML)
        matching = [block for block in blocks if block == canonical]
        if len(matching) != 1:
            errors.append(
                "El HTML debe contener un único bloque semántico con las 18 líneas "
                "paleográficas exactas"
            )
        html_text = RENDERED_HTML.read_text(encoding="utf-8")
        collapsed = " ".join(canonical)
        if re.search(rf"<p[^>]*>\s*{re.escape(collapsed)}\s*</p>", html_text):
            errors.append("La transcripción HTML ha colapsado en un único párrafo")
    if not RENDERED_PDF.is_file():
        errors.append(f"Falta el PDF renderizado: {RENDERED_PDF}")
    else:
        try:
            pdf_lines = _pdf_text_lines(RENDERED_PDF)
        except (OSError, RuntimeError, subprocess.CalledProcessError) as exc:
            errors.append(f"No se pudo extraer texto del PDF: {exc}")
        else:
            if not _contains_ordered_lines(pdf_lines, canonical):
                errors.append(
                    "El PDF no conserva en orden las 18 líneas paleográficas exactas"
                )
            normalized_pdf = re.sub(r"\s+", " ", " ".join(pdf_lines))
            normalized_canonical = re.sub(r"\s+", " ", " ".join(canonical))
            if normalized_canonical not in normalized_pdf:
                errors.append("El PDF no conserva equivalencia textual con la transcripción")
            if "El Catastro de Ensenada" not in normalized_pdf:
                errors.append("El PDF no contiene el capítulo 1")
            if (
                "Las Respuestas Generales y el interrogatorio de cuarenta preguntas"
                not in normalized_pdf
            ):
                errors.append("El PDF no contiene el capítulo 2")
            if "El expediente de Sorribos y Santibáñez de Ordás" not in normalized_pdf:
                errors.append("El PDF no contiene el capítulo 3")
            if "Del manuscrito al volumen actual" not in normalized_pdf:
                errors.append("El PDF no contiene el capítulo 4")
            if "Un lugar de señorío en el Concejo de Ordás" not in normalized_pdf:
                errors.append("El PDF no contiene el capítulo 5")
            if "Vecinos, hogares, viviendas y trabajo" not in normalized_pdf:
                errors.append("El PDF no contiene el capítulo 6")
            if "Tierra, sistema agrario y medidas" not in normalized_pdf:
                errors.append("El PDF no contiene el capítulo 7")
    return errors


def _parse_document(text: str, source: str | Path) -> tuple[dict, str]:
    """Split an initial YAML front matter block from reader-facing Markdown."""

    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\r\n") != "---":
        raise ValueError(f"{source} no comienza con front matter delimitado por ---")

    closing = next(
        (
            index
            for index, line in enumerate(lines[1:], start=1)
            if line.rstrip("\r\n") == "---"
        ),
        None,
    )
    if closing is None:
        raise ValueError(f"Front matter sin delimitador de cierre en {source}")

    metadata_text = "".join(lines[1:closing])
    try:
        data = yaml.safe_load(metadata_text)
    except yaml.YAMLError as exc:
        raise ValueError(f"Front matter YAML inválido en {source}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"Front matter inválido en {source}: se esperaba un mapa YAML")
    return data, "".join(lines[closing + 1:])


def _front_matter_and_body(path: Path) -> tuple[dict, str]:
    return _parse_document(path.read_text(encoding="utf-8"), path)


def _front_matter(path: Path) -> dict:
    return _front_matter_and_body(path)[0]


def _normalized_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).casefold().strip()


def _markdown_section(body: str, anchor: str) -> str:
    heading = re.search(
        rf"^##\s+.+?\s+\{{#{re.escape(anchor)}\}}\s*$",
        body,
        re.MULTILINE,
    )
    if heading is None:
        return ""
    following = re.search(r"^##\s+", body[heading.end():], re.MULTILINE)
    end = heading.end() + following.start() if following else len(body)
    return body[heading.end():end]


def _plain_text(text: str) -> str:
    """Normalize the small Markdown subset used by controlled relations."""

    return _normalized_text(text.translate(str.maketrans("", "", "*_`")))


_RELATION_CLAUSE_BOUNDARY = re.compile(r"(?<=[.!?])\s+|;\s*")
_CONTRASTIVE_CLAUSE_BOUNDARY = re.compile(r",\s+(?=mientras\b)")


def _relation_clauses(paragraph: str) -> tuple[str, ...]:
    """Split only the controlled relation boundaries used by this validator."""

    clauses: list[str] = []
    for proposition in _RELATION_CLAUSE_BOUNDARY.split(paragraph):
        for clause in _CONTRASTIVE_CLAUSE_BOUNDARY.split(proposition):
            clause = clause.strip()
            if clause.startswith("mientras ") and "," in clause:
                contrast, remainder = clause.split(",", maxsplit=1)
                clauses.extend((contrast.strip(), remainder.strip()))
            elif clause:
                clauses.append(clause)
    return tuple(clause for clause in clauses if clause)


def _controlled_paragraphs(markdown: str) -> tuple[tuple[str, tuple[str, ...]], ...]:
    """Return normalized paragraphs and their locally bounded relation clauses.

    Full stops, semicolons, and controlled contrastive coordination delimit
    clauses. Colons deliberately do not: they can introduce the entity list
    governed by a preceding predicate.
    """

    paragraphs: list[tuple[str, tuple[str, ...]]] = []
    for block in re.split(r"\n\s*\n", markdown):
        paragraph = _plain_text(block)
        if not paragraph:
            continue
        propositions = _relation_clauses(paragraph)
        paragraphs.append((paragraph, propositions))
    return tuple(paragraphs)


def _matches_any(text: str, patterns: tuple[str, ...]) -> bool:
    return any(re.search(pattern, text) for pattern in patterns)


def _matches_groups(text: str, *groups: tuple[str, ...]) -> bool:
    return all(_matches_any(text, group) for group in groups)


_POLARITY_MARKER = re.compile(
    r"\b(?P<marker>no|ni|nunca|tampoco|sin|ningun[ao]s?|ninguna|sí)\b"
)


def _predicate_is_negated(text: str, start: int) -> bool:
    """Return the polarity attached locally to a controlled predicate."""

    prefix = text[max(0, start - 100):start]
    boundary = max(prefix.rfind(","), prefix.rfind(":"))
    if boundary >= 0:
        prefix = prefix[boundary + 1:]
    markers = tuple(_POLARITY_MARKER.finditer(prefix))
    if not markers:
        return False
    return markers[-1].group("marker") != "sí"


def _predicate_polarities(
    proposition: str,
    affirmative_patterns: tuple[str, ...],
    negative_patterns: tuple[str, ...] = (),
    ignored_spans: tuple[tuple[int, int], ...] = (),
) -> set[bool]:
    """Return True for affirmed and False for negated relation predicates."""

    polarities: set[bool] = set()
    for pattern in affirmative_patterns:
        for match in re.finditer(pattern, proposition):
            if any(
                start <= match.start() and match.end() <= end
                for start, end in ignored_spans
            ):
                continue
            polarities.add(not _predicate_is_negated(proposition, match.start()))
    for pattern in negative_patterns:
        for match in re.finditer(pattern, proposition):
            if any(
                start <= match.start() and match.end() <= end
                for start, end in ignored_spans
            ):
                continue
            polarities.add(_predicate_is_negated(proposition, match.start()))
    return polarities


_PHONETIC_ENTITY = (
    r"\b(?:secuencia|evolución|reconstrucción)\s+fonética\b",
)
_PHONETIC_COMPLETENESS = (
    r"\bcompleta\b",
    r"\bcompletamente\s+documentad\w*\b",
    r"\bpor\s+completo\b",
)
_PHONETIC_ATTRIBUTIVE_ENTITY = re.compile(
    r"\b(?:secuencia|evolución|reconstrucción)\s+fonética\s+"
    r"completamente\s+documentad\w*\b"
)
_PHONETIC_PREDICATES = (
    r"\bexist(?:e|en|ía|ió|irá|iría)\b",
    r"\bhay\b",
    r"\bdispon(?:e|en|er|ible)\b",
    r"\bproporciona\b",
    r"\b(?:documentada?|documentadas?|documentados?)\b",
    r"\breconstru(?:ir|ye|ida?|idas?|idos?)\b",
    r"\bpermite\b",
    r"\bautoriza\b",
    r"\bdemuestra\b",
    r"\bprueba\b",
    r"\bacredita\b",
)
_ECONOMIC_ENTITY = (r"\bcontinuidad\s+económica\b",)
_ECONOMIC_PREDICATES = (
    r"\bhay\b",
    r"\bdemuestr\w*\b",
    r"\bdemostrad\w*\b",
    r"\bprueb\w*\b",
    r"\bprobad\w*\b",
    r"\bacredit\w*\b",
    r"\bconfirm\w*\b",
    r"\bgarantiz\w*\b",
    r"\bestablec\w*\b",
    r"\bestablecid\w*\b",
    r"\bpermit\w*\b",
    r"\bautoriz\w*\b",
    r"\bafirm\w*\b",
)


def _phonetic_polarities(proposition: str) -> set[bool]:
    if not _matches_groups(
        proposition,
        _PHONETIC_ENTITY,
        _PHONETIC_COMPLETENESS,
    ):
        return set()
    attributive_entity_spans = tuple(
        match.span()
        for match in _PHONETIC_ATTRIBUTIVE_ENTITY.finditer(proposition)
    )
    polarities = _predicate_polarities(
        proposition,
        _PHONETIC_PREDICATES,
        ignored_spans=attributive_entity_spans,
    )
    entity = r"(?:secuencia|evolución|reconstrucción)[^.]{0,40}fonética[^.]{0,20}completa"
    if re.search(rf"\b(?:sin|ningun[ao]s?)\b[^.;:]{{0,60}}{entity}", proposition):
        polarities.add(False)
    if re.search(rf"\b(?:ausencia|falta)\s+de\b[^.;:]{{0,60}}{entity}", proposition):
        polarities.add(False)
    return polarities


def _economic_polarities(proposition: str) -> set[bool]:
    if not _matches_any(proposition, _ECONOMIC_ENTITY):
        return set()
    polarities = _predicate_polarities(proposition, _ECONOMIC_PREDICATES)
    if re.search(
        r"\b(?:sin|ningun[ao]s?)\b[^.;:]{0,70}continuidad\s+económica",
        proposition,
    ):
        polarities.add(False)
    return polarities


def _validate_chapter_three_body(body: str) -> list[str]:
    """Validate the two historical limits in their toponymic context."""

    errors: list[str] = []
    section = _markdown_section(body, "expediente-toponimo")
    if not section:
        return ["C3_TOPONYM_SECTION: falta la sección histórica del topónimo"]
    paragraphs = _controlled_paragraphs(section)

    phonetic_reversal = any(
        True in _phonetic_polarities(proposition)
        for _, propositions in paragraphs
        for proposition in propositions
    )
    if phonetic_reversal:
        errors.append(
            "C3_PHONETIC_REVERSAL: el capítulo afirma una secuencia fonética completa"
        )

    phonetic_limit = any(
        _matches_groups(
            paragraph,
            (r"\bsorrios\s+actual\b", r"\bactual(?:mente)?\b[^.]{0,80}\bsorrios\b"),
            (r"\bidentific\w*\b[^.]{0,100}\bsegur\w*\b",
             r"\bsegur\w*\b[^.]{0,100}\bidentific\w*\b"),
        )
        and any(
            False in _phonetic_polarities(proposition)
            for proposition in propositions
        )
        for paragraph, propositions in paragraphs
    )
    if not phonetic_limit:
        errors.append(
            "C3_PHONETIC_LIMIT: falta relacionar la identificación segura de Sorrios "
            "con el límite de la secuencia fonética"
        )

    economic_reversal = any(
        "1267" in paragraph
        and "1752" in paragraph
        and any(
            True in _economic_polarities(proposition)
            for proposition in propositions
        )
        for paragraph, propositions in paragraphs
    )
    if economic_reversal:
        errors.append(
            "C3_ECONOMIC_CONTINUITY_REVERSAL: el capítulo afirma continuidad "
            "económica demostrada entre 1267 y 1752"
        )

    economic_limit = any(
        "1267" in paragraph
        and "1752" in paragraph
        and re.search(r"\b(?:patrimonial|compraventa|venta|transmisión)\b", paragraph)
        and any(
            False in _economic_polarities(proposition)
            for proposition in propositions
        )
        for paragraph, propositions in paragraphs
    )
    if not economic_limit:
        errors.append(
            "C3_PATRIMONIAL_LIMIT: falta relacionar la evidencia patrimonial de "
            "1267 con el límite de continuidad económica hasta 1752"
        )
    return errors


_FACSIMILE = (r"\bfacsímil\b",)
_TRANSCRIPTION = (r"\btranscripción(?:\s+paleográfica)?\b",)
_CRITICAL_EDITION = (r"\bedición\s+crítica\b",)
_MODERNIZED_EDITION = (r"\bedición\s+modernizada\b", r"\bmodernizada\b")
_INTERPRETATION = (r"\binterpretación\b",)
_CONTENT_PATH = (r"publication/content/",)
_GENERATED_PATH = (r"publication/generated/",)
_DERIVATIVES = (r"\bderivad\w*\b", r"\bsalidas?\b", r"\bproductos?\b")
_EQUALITY_PREDICATES = (
    r"\bigual(?:es)?\b",
    r"\bequivalent(?:e|es)\b",
    r"\bindistinguible(?:s)?\b",
    r"\bintercambiable(?:s)?\b",
    r"\blo\s+mismo\b",
    r"\bla\s+misma\s+capa\b",
)


def _affirms_function(
    propositions: tuple[str, ...],
    entity: tuple[str, ...],
    predicates: tuple[str, ...],
    objects: tuple[str, ...],
) -> bool:
    return any(
        _matches_groups(proposition, entity, objects)
        and True in _predicate_polarities(proposition, predicates)
        for proposition in propositions
    )


def _layer_equality_polarities(proposition: str) -> set[bool]:
    if not _matches_groups(
        proposition,
        _FACSIMILE,
        _TRANSCRIPTION,
        _CRITICAL_EDITION,
        _MODERNIZED_EDITION,
    ):
        return set()
    return _predicate_polarities(proposition, _EQUALITY_PREDICATES)


def _pair_equality_polarities(
    proposition: str,
    first: tuple[str, ...],
    second: tuple[str, ...],
) -> set[bool]:
    if not _matches_groups(proposition, first, second):
        return set()
    return _predicate_polarities(proposition, _EQUALITY_PREDICATES)


_STORAGE_PREDICATES = (
    r"\b(?:es|son)\b",
    r"\bcontien\w*\b",
    r"\balberg\w*\b",
    r"\bguard\w*\b",
    r"\balmacen\w*\b",
    r"\bresid\w*\b",
    r"\bedit\w*\b",
    r"\bredact\w*\b",
    r"\bmanten\w*\b",
)
_OUTPUT_PREDICATES = _STORAGE_PREDICATES + (
    r"\bregener\w*\b",
    r"\breproduc\w*\b",
    r"\breconstru\w*\b",
)
_MANUAL_EDITORIAL = (
    r"\b(?:texto|contenido|fuente|redacción)\s+editorial\b",
    r"\bcapítulos?\b",
)
_HUMAN_MAINTENANCE = (
    r"\bmanual(?:mente)?\b",
    r"\bhuman\w*\b",
    r"\bpor\s+personas\b",
)
_REGENERABLE_OUTPUT = (
    r"\b(?:derivad\w*|salidas?|productos?|vistas?|directorio)\b",
)
_REGENERATION = (
    r"\b(?:regener\w*|reproduc\w*|reconstru\w*|determinista\w*|automátic\w*)\b",
)
_AUTHORITY = (
    r"\bautoridad(?:es)?(?:\s+canónica)?(?:\s+propia)?\b",
    r"\bnuevas?\s+autoridades\b",
)
_AUTHORITY_POSSESSION = (
    r"\b(?:tien\w*|adquier\w*|correspond\w*|pose\w*|goz\w*)\b",
    r"\b(?:es|son)\b(?=[^,;:.]{0,50}\bautoridad)",
    r"\bse\s+conviert\w*\b",
)
_AUTHORITY_ABSENCE = (r"\bcarec\w*\b",)


def _content_function_is_affirmed(proposition: str) -> bool:
    return (
        _matches_groups(
            proposition,
            _CONTENT_PATH,
            _MANUAL_EDITORIAL,
            _HUMAN_MAINTENANCE,
        )
        and True in _predicate_polarities(proposition, _STORAGE_PREDICATES)
    )


def _generated_function_is_affirmed(proposition: str) -> bool:
    return (
        _matches_groups(
            proposition,
            _GENERATED_PATH,
            _REGENERABLE_OUTPUT,
            _REGENERATION,
        )
        and True in _predicate_polarities(proposition, _OUTPUT_PREDICATES)
    )


def _directory_function_is_reversed(proposition: str) -> bool:
    content_is_generated = (
        _matches_groups(
            proposition,
            _CONTENT_PATH,
            _REGENERABLE_OUTPUT,
            _REGENERATION,
        )
        and True in _predicate_polarities(proposition, _OUTPUT_PREDICATES)
    )
    generated_is_manual = (
        _matches_groups(
            proposition,
            _GENERATED_PATH,
            _MANUAL_EDITORIAL,
            _HUMAN_MAINTENANCE,
        )
        and True in _predicate_polarities(proposition, _STORAGE_PREDICATES)
    )
    return content_is_generated or generated_is_manual


def _authority_polarities(proposition: str) -> set[bool]:
    if not _matches_any(proposition, _AUTHORITY):
        return set()
    if not (
        _matches_any(proposition, _GENERATED_PATH)
        or _matches_any(proposition, _DERIVATIVES)
    ):
        return set()
    return _predicate_polarities(
        proposition,
        _AUTHORITY_POSSESSION,
        _AUTHORITY_ABSENCE,
    )


def _validate_chapter_four_body(body: str) -> list[str]:
    """Validate stable distinctions between publication and documentary layers."""

    errors: list[str] = []
    paragraphs = _controlled_paragraphs(body)
    propositions = tuple(
        proposition
        for _, paragraph_propositions in paragraphs
        for proposition in paragraph_propositions
    )
    access = _markdown_section(body, "volumen-cuatro-accesos")
    evidence = _markdown_section(body, "volumen-evidencia")
    generated = _markdown_section(body, "volumen-content-generated")

    if any(True in _layer_equality_polarities(item) for item in propositions):
        errors.append(
            "C4_LAYERS_CONTRADICTED: las cuatro representaciones se presentan "
            "como iguales o indistinguibles"
        )

    access_propositions = tuple(
        proposition
        for _, paragraph_propositions in _controlled_paragraphs(access)
        for proposition in paragraph_propositions
    )
    distinct_relation = any(
        _matches_groups(
            item,
            (r"\b(?:capas?|representaciones?)\b",),
            (r"\b(?:funciones?|cometidos?)\b",),
        )
        and True in _predicate_polarities(
            item,
            (r"\bdistint\w*\b", r"\bdiferent\w*\b", r"\bseparad\w*\b"),
        )
        for item in propositions
    )
    distinct_layers = bool(access) and distinct_relation and all(
        (
            _affirms_function(
                access_propositions,
                _FACSIMILE,
                (r"\breproduc\w*\b", r"\bmuestr\w*\b", r"\bconserv\w*\b"),
                (r"\bimagen\b", r"\bmaterialidad\b", r"\baspecto\s+material\b"),
            ),
            _affirms_function(
                access_propositions,
                _TRANSCRIPTION,
                (r"\bfij\w*\b", r"\bconserv\w*\b", r"\brepresent\w*\b", r"\bregistr\w*\b"),
                (r"\btexto\b", r"\blínea\b", r"\brenglones?\b", r"\bgrafías?\b"),
            ),
            _affirms_function(
                access_propositions,
                _CRITICAL_EDITION,
                (r"\breún\w*\b", r"\bdocument\w*\b", r"\bexplic\w*\b", r"\bregistr\w*\b", r"\bcontien\w*\b"),
                (r"\bsecciones?\b", r"\baparato\b", r"\bdecisiones?\b", r"\bcriterios?\b", r"\bvariantes?\b"),
            ),
            _affirms_function(
                access_propositions,
                _MODERNIZED_EDITION,
                (r"\bofrec\w*\b", r"\bactualiz\w*\b", r"\bfacilit\w*\b", r"\bpresent\w*\b"),
                (r"\blectura\b", r"\bespañol\s+actual\b", r"\bcontemporánea\b"),
            ),
        )
    )
    if not distinct_layers:
        errors.append(
            "C4_LAYER_FUNCTIONS: falta distinguir las funciones propias de facsímil, "
            "transcripción, edición crítica y modernizada"
        )

    if any(
        True in _pair_equality_polarities(item, _TRANSCRIPTION, _INTERPRETATION)
        for item in propositions
    ):
        errors.append(
            "C4_TRANSCRIPTION_INTERPRETATION_REVERSED: transcripción e "
            "interpretación se presentan como la misma operación"
        )

    evidence_paragraphs = _controlled_paragraphs(evidence)
    separates_interpretation = any(
        _affirms_function(
            paragraph_propositions,
            _TRANSCRIPTION,
            (r"\bestablec\w*\b", r"\bfij\w*\b", r"\bregistr\w*\b", r"\bconsign\w*\b"),
            (r"\bfuente\b", r"\btexto\b", r"\btenor\b", r"\bqué\s+dice\b"),
        )
        and _affirms_function(
            paragraph_propositions,
            _INTERPRETATION,
            (r"\bpregunt\w*\b", r"\bexplic\w*\b", r"\binterpret\w*\b", r"\bsignific\w*\b", r"\bofrec\w*\b"),
            (r"\bhistóric\w*\b", r"\bsignific\w*\b", r"\blectura\b", r"\bqué\s+puede\b"),
        )
        for _, paragraph_propositions in evidence_paragraphs
    )
    if not separates_interpretation:
        errors.append(
            "C4_TRANSCRIPTION_INTERPRETATION: falta separar lo que fija la "
            "transcripción de lo que interpreta el estudio"
        )

    if any(
        True in _pair_equality_polarities(item, _CONTENT_PATH, _GENERATED_PATH)
        for item in propositions
    ):
        errors.append(
            "C4_CONTENT_GENERATED_SAME: content/ y generated/ se presentan como "
            "la misma capa"
        )

    if any(_directory_function_is_reversed(item) for item in propositions):
        errors.append(
            "C4_DIRECTORY_FUNCTIONS_REVERSED: se invierten las funciones de "
            "publication/content/ y publication/generated/"
        )

    authority_polarities = {
        polarity
        for item in propositions
        for polarity in _authority_polarities(item)
    }
    if True in authority_polarities:
        errors.append(
            "C4_GENERATED_AUTHORITY: los derivados reciben autoridad canónica propia"
        )

    generated_propositions = tuple(
        proposition
        for _, paragraph_propositions in _controlled_paragraphs(generated)
        for proposition in paragraph_propositions
    )
    separates_directories = (
        any(_content_function_is_affirmed(item) for item in generated_propositions)
        and any(
            _generated_function_is_affirmed(item)
            for item in generated_propositions
        )
    )
    generated_lacks_authority = any(
        False in _authority_polarities(item)
        for item in generated_propositions
    )
    if not separates_directories or not generated_lacks_authority:
        errors.append(
            "C4_CONTENT_GENERATED_FUNCTIONS: falta separar el contenido editorial "
            "humano de los derivados regenerables sin autoridad propia"
        )
    return errors


def _validate_chapter_five_body(body: str) -> list[str]:
    """Validate the bounded institutional and territorial claims of chapter 5."""

    errors: list[str] = []
    sections = {
        anchor: _normalized_text(_markdown_section(body, anchor))
        for anchor in CHAPTER_FIVE_ANCHORS
    }
    for anchor, section in sections.items():
        if not section:
            errors.append(f"C5_SECTION_{anchor.upper().replace('-', '_')}: falta la sección")

    required_by_section = {
        "lugar-actores": (
            "lugar de sorribos y santibáñez de ordás",
            "común del lugar",
            "vecinos",
            "concejo de ordás",
            "municipio posterior de santa maría de ordás",
            "tampoco son intercambiables",
        ),
        "lugar-concejo-municipio": (
            "1768",
            "1789",
            "cinco lugares",
            "1836",
            "1848",
            "no puede proyectarse sobre 1752",
            "no son equivalentes automáticos",
        ),
        "lugar-senorio-conde": (
            "el manuscrito",
            "conde de luna",
            "no proporciona el nombre personal",
            "francisco alfonso pimentel como xv conde de luna",
            "identificación nominal procede de documentación externa",
        ),
        "lugar-derechos": (
            "establecimiento del suelo",
            "alcabalas",
            "633 reales anuales",
            "pozo de pesca",
            "nueve reales",
            "coexiste",
            "no consta el título jurídico concreto",
            "conceptos diferenciados",
        ),
        "lugar-termino": (
            "una legua y media y 787 varas",
            "2.500 varas de oriente a poniente",
            "2.708 varas de norte a sur",
            "tapia",
            "rioseco",
            "santa maría",
            "villapodambre",
            "croquis o figura marginal",
            "no constituyen cartografía métrica moderna",
            "no se convierten en superficie moderna",
            "ni permiten reconstruir un polígono geográfico exacto",
        ),
        "lugar-sintesis": (
            "lugar",
            "comunidad",
            "jurisdicción",
            "señorío",
            "término",
            "no una única realidad",
            "capítulo 6",
            "capítulo 7",
            "capítulo 9",
            "capítulo 10",
            "capítulo 11",
        ),
    }
    for anchor, phrases in required_by_section.items():
        section = sections[anchor]
        absent = [phrase for phrase in phrases if phrase not in section]
        if absent:
            errors.append(
                f"C5_CONTENT_{anchor.upper().replace('-', '_')}: faltan relaciones "
                + ", ".join(absent)
            )

    controlled_blocks = _controlled_paragraphs(body)
    paragraphs = tuple(paragraph for paragraph, _ in controlled_blocks)
    propositions = tuple(
        proposition
        for _, block_propositions in controlled_blocks
        for proposition in block_propositions
    )
    prohibited = {
        "C5_COMMON_COUNCIL_EQUIVALENCE": (
            r"\bel común del lugar era el concejo de ordás\b",
        ),
        "C5_COUNCIL_MUNICIPALITY_EQUIVALENCE": (
            r"\bel concejo de ordás de 1752 era el municipio actual\b",
        ),
        "C5_MANUSCRIPT_IDENTIFIES_COUNT": (
            r"\bel manuscrito identifica a francisco alfonso pimentel\b",
        ),
        "C5_NO_LORDLY_RIGHTS": (
            r"\bel lugar no pagaba ningún derecho al conde\b",
        ),
        "C5_R22_ERASES_RIGHTS": (
            r"\bla respuesta 22 demuestra la ausencia de derechos señoriales\b",
            r"\bla respuesta 22 demuestra que no exist(?:en|ían) derechos señoriales\b",
        ),
        "C5_EXACT_POLYGON_RECONSTRUCTION": (
            r"\bel croquis permite reconstruir un polígono geográfico exacto\b",
        ),
    }
    for code, patterns in prohibited.items():
        if any(
            re.search(pattern, paragraph)
            for paragraph in paragraphs
            for pattern in patterns
        ):
            errors.append(f"{code}: formulación no autorizada en el capítulo 5")

    known_legal_title = re.compile(
        r"\b(?:se\s+conoce|conocemos)\s+el\s+título\s+jurídico\s+de\s+las\s+"
        r"alcabalas\s+y\s+del\s+pozo\b"
    )
    if any(
        not _predicate_is_negated(proposition, match.start())
        for proposition in propositions
        for match in known_legal_title.finditer(proposition)
    ):
        errors.append(
            "C5_KNOWN_LEGAL_TITLE: formulación no autorizada en el capítulo 5"
        )

    modern_conversion = re.compile(
        r"\b\d+(?:[.,]\d+)?\s*(?:hectáreas?|ha\b|km(?:²|2)|kilómetros? cuadrados?)"
    )
    if any(modern_conversion.search(paragraph) for paragraph in paragraphs):
        errors.append(
            "C5_MODERN_TERRITORIAL_CONVERSION: conversión territorial no autorizada"
        )
    return errors


def _validate_chapter_six_body(body: str) -> list[str]:
    """Validate the demographic, domestic and labour limits of chapter 6."""

    errors: list[str] = []
    sections = {
        anchor: _plain_text(_markdown_section(body, anchor))
        for anchor in CHAPTER_SIX_ANCHORS
    }
    for anchor, section in sections.items():
        if not section:
            errors.append(f"C6_SECTION_{anchor.upper().replace('-', '_')}: falta la sección")

    required_by_section = {
        "vecinos-recuento": (
            "vecinos | 18",
            "medios vecinos | 8",
            "«avitadores» | 26",
            "residentes no considerados vecinos | 8",
            "18 + 8 = 26",
            "ocho medios vecinos no equivalen a cuatro vecinos",
            "función fiscal de la vecindad",
        ),
        "avitadores-poblacion": (
            "forma documental de la respuesta 21",
            "no se obtiene una población total añadiendo 26 y 8",
            "unidad de observación no consta como equivalente",
            "vecinos × k",
            "137 habitantes a santibáñez de sorribos en 1768",
            "por su fecha y unidad distintas",
        ),
        "personas-hogares": (
            "persona es un individuo",
            "cabezas de casa y familias",
            "14 son hijos de familia",
            "tres son criados sirvientes",
            "indicios de convivencia y trabajo doméstico",
            "no una magnitud contada directamente",
        ),
        "casas-viviendas": (
            "casas habitables | 40",
            "casas arruinadas | 2",
            "pajares separados | 15",
            "no equivalen a 40 hogares",
            "no permite estimar cuántas personas ocupaban cada casa",
            "vivienda ocupada",
        ),
        "trabajo-categorias": (
            "jornaleros | 18",
            "14 hijos de familia + 3 criados sirvientes + 1 dedicado solo a ese ejercicio = 18",
            "labradores | 24",
            "herrero | 1",
            "no se suman para formar una población activa",
            "oficio, ocupación y condición laboral tampoco son equivalentes",
            "cinco pobres de solemnidad",
            "un cura párroco y dos capellanes",
        ),
        "trabajo-utilidades": (
            "2,5 reales por día trabajado",
            "3 reales",
            "1,5 reales",
            "medio real diario",
            "una regulación diaria no es un ingreso anual",
            "no reconstruir la renta anual de un hogar",
        ),
        "estructura-limites": (
            "trabajo familiar, servicio doméstico, jornal, labranza",
            "no consta el total de individuos",
            "no un total de unidades domésticas",
            "dato sin suma total",
            "no rentas anuales personales o familiares",
            "no son equivalentes",
        ),
    }
    for anchor, phrases in required_by_section.items():
        section = sections[anchor]
        absent = [phrase for phrase in phrases if phrase not in section]
        if absent:
            errors.append(
                f"C6_CONTENT_{anchor.upper().replace('-', '_')}: faltan relaciones "
                + ", ".join(absent)
            )

    controlled = _controlled_paragraphs(body)
    propositions = tuple(
        proposition
        for _, paragraph_propositions in controlled
        for proposition in paragraph_propositions
    )
    prohibited_predicates = {
        "C6_AVITADORES_ARE_INHABITANTS": (
            r"\b(?:los\s+)?26\s+avitadores\s+(?:son|equivalen\s+a)\s+26\s+habitantes\b",
        ),
        "C6_RESIDENT_SUM_IS_POPULATION": (
            r"\b(?:sumar|sumando|añadir|añadiendo)\b[^.;]{0,80}\b(?:26\s+y\s+8|ocho\s+residentes)\b[^.;]{0,80}\b(?:da|daría|produce|produciría|forma|formaría)\b[^.;]{0,40}\b(?:la\s+)?población\s+total\b",
            r"\b(?:la\s+)?población\s+total\s+(?:era|es|sería)\s+(?:de\s+)?34\s+habitantes\b",
        ),
        "C6_HALF_NEIGHBOUR_WEIGHTED": (
            r"\bocho\s+medios\s+vecinos\s+(?:equivalen|equivalían|son)\s+a?\s*cuatro\s+vecinos\b",
        ),
        "C6_HOUSES_ARE_HOUSEHOLDS": (
            r"\b(?:las\s+)?(?:40|cuarenta)\s+casas\s+habitables\s+(?:representan|equivalen\s+a|son)\s+(?:40|cuarenta)\s+hogares\b",
        ),
        "C6_LABOUR_CATEGORIES_ADDED": (
            r"\b(?:los\s+)?18\s+jornaleros\s+y\s+(?:los\s+)?24\s+labradores\s+(?:forman|suman|equivalen\s+a)\b[^.;]{0,50}\b(?:42|cuarenta\s+y\s+dos)\b",
        ),
        "C6_HALF_NEIGHBOUR_IS_HALF_PERSON": (
            r"\b(?:el\s+)?medio\s+vecino\s+(?:era|es|equivale\s+a)\s+(?:media\s+persona|medio\s+habitante)\b",
        ),
        "C6_DAILY_RATE_IS_ANNUAL_INCOME": (
            r"\b(?:los\s+)?2,5\s+reales\s+diarios\s+(?:permiten|permitirían)\s+calcular\b[^.;]{0,50}\b(?:el\s+)?ingreso\s+anual\b",
        ),
        "C6_SMITH_NOT_FARMER": (
            r"\bel\s+herrero\s+no\s+(?:ejercía|trabajaba)\s+como\s+labrador\b",
        ),
        "C6_POVERTY_RATE": (
            r"\b(?:los\s+)?cinco\s+pobres\s+de\s+solemnidad\s+(?:permiten|permitirían)\s+calcular\b[^.;]{0,40}\b(?:la\s+)?tasa\s+de\s+pobreza\b",
        ),
    }
    for code, patterns in prohibited_predicates.items():
        if any(
            not _predicate_is_negated(proposition, match.start())
            for proposition in propositions
            for pattern in patterns
            for match in re.finditer(pattern, proposition)
        ):
            errors.append(f"{code}: formulación no autorizada en el capítulo 6")

    normalized = _plain_text(body)
    if re.search(
        r"\bvecinos\s*[×x]\s*\d+(?:[.,]\d+)?\s*=\s*\d+(?:[.,]\d+)?\s+habitantes\b",
        normalized,
    ):
        errors.append(
            "C6_GENERIC_POPULATION_FACTOR: conversión no autorizada de vecinos en habitantes"
        )
    return errors


def _validate_chapter_seven_body(body: str) -> list[str]:
    """Validate agrarian calculations, metrology, limits, and chapter borders."""

    errors: list[str] = []
    sections = {
        anchor: _plain_text(_markdown_section(body, anchor))
        for anchor in CHAPTER_SEVEN_ANCHORS
    }
    for anchor, section in sections.items():
        if not section:
            errors.append(f"C7_SECTION_{anchor.upper().replace('-', '_')}: falta la sección")

    required_by_section = {
        "tierra-clases": (
            "trece clases de tierras y aprovechamientos",
            "ferrañales centenales de secano",
            "linares de regadío",
            "linares de secano",
            "centenales de secano",
            "prados entreparedes",
            "matorrales",
            "eras o sitios",
            "montes de robles altos y bajos",
            "soto de negrillos, alisos y fresnos",
            "funciones, no títulos de propiedad",
            "capítulo 8",
            "árboles frutales",
        ),
        "tierra-calidades": (
            "no aplica una escala uniforme",
            "prado cercado de secano",
            "solo segunda, llamada única",
            "montes",
            "no aparecen en el desglose cuantitativo",
            "sotos",
            "no armonizar ambas respuestas",
        ),
        "tierra-medidas": (
            "no se usa una medida superficial cierta reducible a varas castellanas",
            "el mismo quartal de tierra ocupa más o menos terreno según su calidad",
            "4 quartales = 1 fanega",
            "4 montones = 1 carro",
            "ninguna relación declarada con la medida principal, el quartal o la fanega",
            "no permiten encadenar",
        ),
        "tierra-cabida": (
            "3.823 medidas y un celemín",
            "3.811,5 medidas principales y siete celemines",
            "no se restan ni se reconcilian",
            "666 de primera calidad",
            "1.398 de segunda",
            "1.747,5 de tercera",
            "3.811,5 como denominador",
        ),
        "tierra-centeno": (
            "centeno, cebada, lino, linaza y yerba",
            "34 medidas de ferrañales + 149,5",
            "2.953,5 medidas de cabida cultivada comparable",
            "2.750,5 medidas centenales",
            "2.750,5 ÷ 2.953,5 × 100",
            "93,13 %",
            "2.750,5 ÷ 3.811,5 × 100",
            "72,16 %",
            "preguntas distintas",
        ),
        "tierra-ciclos": (
            "linares de regadío alternan lino y cebada",
            "linares de secano, lino y centeno",
            "producen un año y descansan otro",
            "no describen una rotación agronómica completa",
            "2.750,5 ÷ 2 + 34 + 149,5 + 19,5",
            "1.578,25 unidades activas medias",
            "1.375,25",
            "87,14 %",
            "índice analítico",
            "no superficie efectivamente sembrada",
        ),
        "tierra-rendimientos": (
            "un quartal de tierra",
            "no registra lo que se cosechó en un año concreto",
            "ferrañal / forraje",
            "linar de regadío / linaza y lino",
            "linar de secano / centeno",
            "centenal / centeno",
            "no se suman linaza en quartales y lino en libras",
            "cuatro montones que componen un carro",
        ),
        "tierra-produccion-limites": (
            "producto agrario total",
            "multiplicar cada cabida por una tasa seleccionada",
            "valores regulados por quinquenio",
            "40 fejes de lino × 4 libras = 160 libras",
            "no representa la producción total de lino",
            "no permite deducir autoconsumo",
            "suficiencia alimentaria",
            "productividad por trabajador",
            "capítulo 12",
        ),
        "tierra-sintesis": (
            "comparte unidad, base y denominador",
            "no pueden agregarse celemín y medida principal",
            "carga y quartal",
            "valor monetario y producto físico",
            "capítulo 8",
            "al 9",
            "al 10",
            "al 11",
            "al 12",
            "al 13",
        ),
    }
    for anchor, phrases in required_by_section.items():
        section = sections[anchor]
        absent = [phrase for phrase in phrases if phrase not in section]
        if absent:
            errors.append(
                f"C7_CONTENT_{anchor.upper().replace('-', '_')}: faltan relaciones "
                + ", ".join(absent)
            )

    controlled = _controlled_paragraphs(body)
    propositions = tuple(
        proposition
        for _, paragraph_propositions in controlled
        for proposition in paragraph_propositions
    )
    prohibited_predicates = {
        "C7_TOTALS_RECONCILED": (
            r"\b(?:3\.823[^.;]{0,80}3\.811,5|3\.811,5[^.;]{0,80}3\.823)\b[^.;]{0,80}\b(?:coinciden|equivalen|son\s+iguales|se\s+reconcilian)\b",
        ),
        "C7_MOUNTS_BY_RESIDUAL": (
            r"\b(?:la\s+)?(?:cabida|cantidad)\s+de\s+los\s+montes\b[^.;]{0,80}\b(?:se\s+obtiene|se\s+calcula|equivale|es)\b[^.;]{0,40}\b(?:por\s+residuo|diferencia)\b",
        ),
        "C7_FALSE_CELEMIN_EQUIVALENCE": (
            r"\b(?:un|1)\s+celem[ií]n\s+(?:equivale|corresponde|es\s+igual)\s+a\b[^.;]{0,40}\b(?:quartal|fanega|medida)\b",
        ),
        "C7_PERCENTAGES_SAME_DENOMINATOR": (
            r"\b93,13\s*%[^.;]{0,80}72,16\s*%[^.;]{0,80}\b(?:mismo|igual)\s+denominador\b",
            r"\b(?:mismo|igual)\s+denominador[^.;]{0,80}93,13\s*%[^.;]{0,80}72,16\s*%\b",
        ),
        "C7_EXACT_ROTATION": (
            r"\b(?:se\s+documenta|documenta|demuestra|consta)\b[^.;]{0,60}\brotaci[oó]n\s+(?:trienal|cuatrienal|completa|precisa)\b",
        ),
        "C7_OBSERVED_ACTIVE_SURFACE": (
            r"\b1\.578,25\b[^.;]{0,80}\b(?:superficie\s+efectivamente\s+sembrada|cosecha\s+observada)\b",
        ),
        "C7_TOTAL_PRODUCTION": (
            r"\b(?:el\s+)?producto\s+agrario\s+total\b[^.;]{0,50}\b(?:fue|era|ascend[ií]a|se\s+calcula|puede\s+calcularse)\b",
            r"\b(?:la\s+)?producci[oó]n\s+total\s+de\s+lino\b[^.;]{0,50}\b(?:fue|era|ascend[ií]a|equival(?:e|[ií]a|dr[ií]a))\b",
        ),
        "C7_INCOMPATIBLE_SUM": (
            r"\b(?:sumar|sumando|agregar|agregando)\b[^.;]{0,70}\bcargas?\b[^.;]{0,40}\b(?:fanegas?|quartales?)\b",
            r"\b(?:sumar|sumando|agregar|agregando)\b[^.;]{0,70}\bquartales?\b[^.;]{0,40}\blibras?\b",
        ),
        "C7_AUTOCONSUMPTION": (
            r"\b(?:demuestra|prueba|confirma|garantiza|documenta)\b[^.;]{0,80}\b(?:autoconsumo|suficiencia\s+alimentaria)\b",
        ),
        "C7_PRODUCTIVITY_INFERENCE": (
            r"\b(?:permite|permiten|puede|pueden)\b[^.;]{0,60}\bcalcular\b[^.;]{0,60}\bproductividad\s+por\s+(?:trabajador|hogar)\b",
        ),
    }
    for code, patterns in prohibited_predicates.items():
        if any(
            not _predicate_is_negated(proposition, match.start())
            for proposition in propositions
            for pattern in patterns
            for match in re.finditer(pattern, proposition)
        ):
            errors.append(f"{code}: formulación no autorizada en el capítulo 7")

    normalized = _plain_text(body)
    if re.search(
        r"\b\d+(?:[.,]\d+)?\s*(?:hectáreas?|ha\b|m(?:²|2)\b|km(?:²|2)\b|litros?|kilogramos?|kg\b)",
        normalized,
    ):
        errors.append("C7_MODERN_CONVERSION: conversión moderna no autorizada")
    for marker in ("ocho ruedas", "18 pies de abejas", "633 reales", "hacienda concejil detallada"):
        if marker in normalized:
            errors.append(
                "C7_CHAPTER_BOUNDARY: desarrollo sustantivo reservado a los capítulos 8–13"
            )
            break
    return errors


def _normalized_evidence(metadata: dict) -> dict[str, tuple[str, ...]]:
    evidence = metadata.get("evidence", {})
    if not isinstance(evidence, dict):
        return {}
    return {level: tuple(values or []) for level, values in evidence.items()}


def _all_publication_texts() -> list[tuple[Path, str]]:
    suffixes = {".md", ".qmd", ".yml", ".py", ".scss", ".bib"}
    return [
        (path, path.read_text(encoding="utf-8"))
        for path in PUBLICATION_ROOT.rglob("*")
        if path.is_file()
        and path.suffix in suffixes
        and "_book" not in path.parts
    ]


def validate() -> list[str]:
    errors: list[str] = []
    expected_ids = {item for group in EVIDENCE_GROUPS.values() for item in group}
    required_generated = {
        "facsimile": ("#pagina-digital-12", "lightbox: true"),
        "transcription": ("#folio-315v", "lightbox: true"),
        "modernized": ("#respuesta-17",),
        "apparatus": ("#cuadro-molinos", "#matriz-molinera"),
    }
    if not CHAPTER_ONE.is_file():
        errors.append(f"Falta el capítulo 1: {CHAPTER_ONE}")
    else:
        try:
            chapter_one_metadata = _front_matter(CHAPTER_ONE)
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(str(exc))
        else:
            for key in ("title", "chapter-id", "publication-status", "sources"):
                if key not in chapter_one_metadata:
                    errors.append(f"Falta {key} en el capítulo 1")
            if chapter_one_metadata.get("chapter-id") != "catastro-ensenada":
                errors.append("chapter-id incorrecto en el capítulo 1")
            if chapter_one_metadata.get("publication-status") != "development":
                errors.append("El capítulo 1 debe declarar publication-status: development")
            if chapter_one_metadata.get("evidence"):
                errors.append("El capítulo 1 no debe inventar identificadores de evidencia")
            sources = chapter_one_metadata.get("sources", [])
            source_paths = {
                source.get("path") for source in sources if isinstance(source, dict)
            }
            locators = [
                source.get("locator") for source in sources if isinstance(source, dict)
            ]
            if source_paths != CHAPTER_ONE_SOURCE_PATHS or not all(locators):
                errors.append("Procedencia incompleta o no autorizada en el capítulo 1")
        chapter_one_text = CHAPTER_ONE.read_text(encoding="utf-8")
        links = set(re.findall(r"\]\((https://[^)]+)\)", chapter_one_text))
        if links != CHAPTER_ONE_LINKS:
            errors.append(
                "Los enlaces externos del capítulo 1 no son los institucionales autorizados"
            )

    if not CHAPTER_TWO.is_file():
        errors.append(f"Falta el capítulo 2: {CHAPTER_TWO}")
    else:
        try:
            chapter_two_metadata = _front_matter(CHAPTER_TWO)
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(str(exc))
        else:
            for key in ("title", "chapter-id", "publication-status", "sources"):
                if key not in chapter_two_metadata:
                    errors.append(f"Falta {key} en el capítulo 2")
            if (
                chapter_two_metadata.get("title")
                != "Las Respuestas Generales y el interrogatorio de cuarenta preguntas"
            ):
                errors.append("Título incorrecto en el capítulo 2")
            if (
                chapter_two_metadata.get("chapter-id")
                != "respuestas-generales-interrogatorio"
            ):
                errors.append("chapter-id incorrecto en el capítulo 2")
            if chapter_two_metadata.get("publication-status") != "development":
                errors.append("El capítulo 2 debe declarar publication-status: development")
            if "evidence" in chapter_two_metadata:
                errors.append("El capítulo 2 no debe inventar identificadores de evidencia")
            sources = chapter_two_metadata.get("sources", [])
            source_paths = [
                source.get("path") for source in sources if isinstance(source, dict)
            ]
            locators = [
                source.get("locator") for source in sources if isinstance(source, dict)
            ]
            if (
                set(source_paths) != CHAPTER_TWO_SOURCE_PATHS
                or len(source_paths) != len(CHAPTER_TWO_SOURCE_PATHS)
                or not all(locators)
            ):
                errors.append("Procedencia incompleta o no autorizada en el capítulo 2")
            for source_path in CHAPTER_TWO_SOURCE_PATHS:
                if not (REPOSITORY_ROOT / source_path).is_file():
                    errors.append(f"Fuente declarada inexistente en el capítulo 2: {source_path}")

        chapter_two_text = CHAPTER_TWO.read_text(encoding="utf-8")
        chapter_two_links = set(
            re.findall(r"\]\((https://[^)]+)\)", chapter_two_text)
        )
        if chapter_two_links != CHAPTER_TWO_LINKS:
            errors.append(
                "Los enlaces externos del capítulo 2 no son los institucionales autorizados"
            )
        for question_range, subject in CHAPTER_TWO_THEMATIC_BLOCKS:
            row = rf"\|\s*{re.escape(question_range)}\s*\|\s*{re.escape(subject)}\s*\|"
            if not re.search(row, chapter_two_text, re.IGNORECASE):
                errors.append(
                    f"Falta el bloque temático {question_range} en el capítulo 2"
                )
        normalized_chapter_two = re.sub(r"\s+", " ", chapter_two_text).casefold()
        for phrase in (
            "pregunta 29",
            "hay en la población",
            "transmisión moderna",
            "titularidad",
            "utilidad anual",
            "formulario externo",
            "lectura paleográfica local",
        ):
            if phrase.casefold() not in normalized_chapter_two:
                errors.append(
                    f"Falta explicar {phrase!r} en el tratamiento de la pregunta 29"
                )
        if _has_extensive_questionnaire_sequence(chapter_two_text):
            errors.append(
                "El capítulo 2 contiene una secuencia extensa de preguntas o "
                "respuestas; los cuarenta pares completos pertenecen al capítulo 16"
            )

    chapter_specs = (
        (CHAPTER_THREE, "El expediente de Sorribos y Santibáñez de Ordás",
         "expediente-sorribos-santibanez", CHAPTER_THREE_SOURCE_PATHS,
         CHAPTER_THREE_EVIDENCE, 3),
        (CHAPTER_FOUR, "Del manuscrito al volumen actual",
         "manuscrito-volumen-actual", CHAPTER_FOUR_SOURCE_PATHS, None, 4),
        (CHAPTER_FIVE, "Un lugar de señorío en el Concejo de Ordás",
         "lugar-senorio-concejo-ordas", CHAPTER_FIVE_SOURCE_PATHS,
         CHAPTER_FIVE_EVIDENCE, 5),
        (CHAPTER_SIX, "Vecinos, hogares, viviendas y trabajo",
         "vecinos-hogares-viviendas-trabajo", CHAPTER_SIX_SOURCE_PATHS,
         CHAPTER_SIX_EVIDENCE, 6),
        (CHAPTER_SEVEN, "Tierra, sistema agrario y medidas",
         "tierra-sistema-agrario-medidas", CHAPTER_SEVEN_SOURCE_PATHS,
         CHAPTER_SEVEN_EVIDENCE, 7),
    )
    chapter_bodies: dict[int, str] = {}
    for path, title, chapter_id, allowed_sources, required_evidence, number in chapter_specs:
        if not path.is_file():
            errors.append(f"Falta el capítulo {number}: {path}")
            continue
        try:
            chapter_metadata, chapter_body = _front_matter_and_body(path)
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(str(exc))
            continue
        chapter_bodies[number] = chapter_body
        if chapter_metadata.get("title") != title:
            errors.append(f"Título incorrecto en el capítulo {number}")
        if chapter_metadata.get("chapter-id") != chapter_id:
            errors.append(f"chapter-id incorrecto en el capítulo {number}")
        if chapter_metadata.get("publication-status") != "development":
            errors.append(f"publication-status incorrecto en el capítulo {number}")
        sources = chapter_metadata.get("sources", [])
        source_paths = [source.get("path") for source in sources if isinstance(source, dict)]
        locators = [source.get("locator") for source in sources if isinstance(source, dict)]
        if (set(source_paths) != allowed_sources
                or len(source_paths) != len(allowed_sources) or not all(locators)):
            errors.append(f"Procedencia incompleta o no autorizada en el capítulo {number}")
        for source_path in allowed_sources:
            if not (REPOSITORY_ROOT / source_path).is_file():
                errors.append(f"Fuente inexistente en el capítulo {number}: {source_path}")
        if required_evidence is None and "evidence" in chapter_metadata:
            errors.append("El capítulo 4 no debe declarar evidencia")
        elif (required_evidence is not None
              and _normalized_evidence(chapter_metadata) != required_evidence):
            errors.append(f"Evidencia incorrecta en el capítulo {number}")

    if CHAPTER_THREE.is_file():
        chapter_three_text = chapter_bodies.get(3, "")
        normalized_three = _normalized_text(chapter_three_text)
        required_three = (
            "17 de septiembre de 1752", "joaquín aguado",
            "manuel antonio de bega", "juan álvarez", "remirio rodríguez",
            "domingo díez", "francisco de llorca", "domingo suárez",
            "manuel antonio alonso", "excepto el cura", "18 páginas digitales",
            "35 unidades documentales", "cuarenta respuestas",
            "dos rúbricas gráficas inferiores",
            "69 años", "49 años", "59 años", "52 años", "44 años",
        )
        for phrase in required_three:
            if phrase not in normalized_three:
                errors.append(f"Falta el hecho controlado {phrase!r} en el capítulo 3")
        if not all(form in chapter_three_text for form in ("Sorribios", "Sorribos", "Sorrios")):
            errors.append("Falta la secuencia toponímica positiva en el capítulo 3")
        if "sorribas" in normalized_three:
            errors.append("El capítulo 3 introduce la forma no autorizada Sorribas")
        if "(04-manuscrito-volumen-actual.qmd)" not in chapter_three_text:
            errors.append("El capítulo 3 no enlaza el capítulo 4")
        if "publication/generated/" in chapter_three_text:
            errors.append("El capítulo 3 invade la explicación técnica del capítulo 4")
        if re.search(r"<[A-Za-z][^>]*>", chapter_three_text):
            errors.append("El capítulo 3 contiene HTML crudo")
        errors.extend(_validate_chapter_three_body(chapter_three_text))

    if CHAPTER_FOUR.is_file():
        chapter_four_text = chapter_bodies.get(4, "")
        normalized_four = _normalized_text(chapter_four_text)
        required_four = (
            "pdf manuscrito autoritativo", "18 páginas digitales",
            "35 unidades documentales", "facsímil",
            "transcripción paleográfica semidiplomática", "edición crítica 3.6",
            "edición modernizada 1.3", "preguntas externas", "respuestas locales",
            "estudio histórico 1.2", "registro 1.2", "front matter",
            "libro quarto", "publication/content/", "publication/generated/",
            "referencia editorial", "no es una autoridad textual",
            "permanece fuera de github",
        )
        for phrase in required_four:
            if phrase not in normalized_four:
                errors.append(f"Falta distinguir {phrase!r} en el capítulo 4")
        for heading in UNIT_HEADINGS:
            if heading.casefold() not in normalized_four:
                errors.append(f"Falta la sección {heading!r} en el capítulo 4")
        for level in ("d — dato", "c — cálculo", "i — interpretación",
                      "e — contexto", "l — límite"):
            if level not in normalized_four:
                errors.append(f"Falta explicar el nivel {level!r} en el capítulo 4")
        if "(03-expediente-sorribos-santibanez.qmd)" not in chapter_four_text:
            errors.append("El capítulo 4 no enlaza el capítulo 3")
        for participant in ("Joaquín Aguado", "Remirio Rodríguez", "Domingo Díez"):
            if participant in chapter_four_text:
                errors.append(f"El capítulo 4 invade la narración con {participant}")
        if re.search(r"<[A-Za-z][^>]*>", chapter_four_text):
            errors.append("El capítulo 4 contiene HTML crudo")
        errors.extend(_validate_chapter_four_body(chapter_four_text))

    if CHAPTER_FIVE.is_file():
        chapter_five_text = chapter_bodies.get(5, "")
        if "(../01-catastro/03-expediente-sorribos-santibanez.qmd)" not in chapter_five_text:
            errors.append("El capítulo 5 no enlaza el capítulo 3")
        if "(../01-catastro/04-manuscrito-volumen-actual.qmd)" not in chapter_five_text:
            errors.append("El capítulo 5 no enlaza el capítulo 4")
        if re.search(r"<[A-Za-z][^>]*>", chapter_five_text):
            errors.append("El capítulo 5 contiene HTML crudo")
        errors.extend(_validate_chapter_five_body(chapter_five_text))

    if CHAPTER_SIX.is_file():
        chapter_six_text = chapter_bodies.get(6, "")
        if "(05-lugar-senorio-concejo-ordas.qmd)" not in chapter_six_text:
            errors.append("El capítulo 6 no enlaza el capítulo 5")
        if re.search(r"<[A-Za-z][^>]*>", chapter_six_text):
            errors.append("El capítulo 6 contiene HTML crudo")
        errors.extend(_validate_chapter_six_body(chapter_six_text))

    if CHAPTER_SEVEN.is_file():
        chapter_seven_text = chapter_bodies.get(7, "")
        if "(06-vecinos-hogares-viviendas-trabajo.qmd)" not in chapter_seven_text:
            errors.append("El capítulo 7 no enlaza el capítulo 6")
        if re.search(r"<[A-Za-z][^>]*>", chapter_seven_text):
            errors.append("El capítulo 7 contiene HTML crudo")
        errors.extend(_validate_chapter_seven_body(chapter_seven_text))

    if not PROTOTYPE_CHAPTER.is_file():
        return errors + [f"Falta el capítulo editorial: {PROTOTYPE_CHAPTER}"]
    try:
        metadata = _front_matter(PROTOTYPE_CHAPTER)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        return errors + [str(exc)]
    for key in ("title", "chapter-id", "publication-status", "sources", "evidence"):
        if key not in metadata:
            errors.append(f"Falta {key} en el capítulo editorial")
    if metadata.get("publication-status") != "prototype":
        errors.append("El capítulo debe declarar publication-status: prototype")
    evidence = metadata.get("evidence", {})
    normalized = {
        level: tuple(values or [])
        for level, values in evidence.items()
    } if isinstance(evidence, dict) else {}
    if normalized != EVIDENCE_GROUPS:
        errors.append("Los identificadores D/C/I/E/L del capítulo no coinciden con la muestra fijada")

    register_path = (
        REPOSITORY_ROOT
        / "project"
        / "30_RESULTADOS"
        / "ESTUDIO_HISTORICO"
        / "Registro_Afirmaciones_Calculos_v1.md"
    )
    register = register_path.read_text(encoding="utf-8")
    registered = set(
        re.findall(r"^\|\s*([A-Z]+-\d{3})\s*\|", register, re.MULTILINE)
    )
    phase_3c_ids = {
        item for group in CHAPTER_THREE_EVIDENCE.values() for item in group
    }
    phase_3d_ids = {
        item for group in CHAPTER_FIVE_EVIDENCE.values() for item in group
    }
    phase_3e_ids = {
        item for group in CHAPTER_SIX_EVIDENCE.values() for item in group
    }
    phase_3f_ids = {
        item for group in CHAPTER_SEVEN_EVIDENCE.values() for item in group
    }
    missing_registry = sorted(
        (expected_ids | phase_3c_ids | phase_3d_ids | phase_3e_ids | phase_3f_ids)
        - registered
    )
    if missing_registry:
        errors.append("Identificadores ausentes del Registro 1.2: " + ", ".join(missing_registry))

    chapter_text = PROTOTYPE_CHAPTER.read_text(encoding="utf-8")
    chapter_normalized = re.sub(r"\s+", " ", chapter_text)
    if CANONICAL_FORMULA not in chapter_normalized:
        errors.append("Falta la formulación canónica de las ocho ruedas y el venturero")
    for phrase in (
        "ocho ruedas fijas",
        "paralizaron los molinos",
        "paralizó todos los molinos",
    ):
        if phrase.casefold() in chapter_text.casefold():
            errors.append(f"Expresión de regresión en el capítulo: {phrase}")

    for name, requirements in required_generated.items():
        path = GENERATED[name]
        if not path.is_file():
            errors.append(f"Falta el derivado generado: {path.relative_to(PUBLICATION_ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for requirement in requirements:
            if requirement not in text:
                errors.append(f"Falta {requirement} en {path.name}")
    for image in (
        PUBLICATION_ROOT / "generated" / "assets" / "manuscript-page-12.png",
        PUBLICATION_ROOT / "generated" / "assets" / "folio-315v.png",
    ):
        if not image.is_file() or image.stat().st_size == 0:
            errors.append(f"Falta la imagen regenerable: {image.name}")

    if GENERATED["facsimile"].is_file():
        facsimile = GENERATED["facsimile"].read_text(encoding="utf-8")
        if not re.search(
            r"!\[[^\]]{20,}\]\(assets/manuscript-page-12\.png\)"
            r'\{[^}]*fig-alt="[^"]{20,}"[^}]*\}',
            facsimile,
        ):
            errors.append("La página facsimilar carece de texto alternativo suficiente")
    if GENERATED["transcription"].is_file():
        transcription = GENERATED["transcription"].read_text(encoding="utf-8")
        headings = tuple(
            re.findall(r"^### (.+?)\s*$", transcription, re.MULTILINE)
        )
        if headings != UNIT_HEADINGS:
            errors.append("Faltan secciones canónicas en la unidad paleográfica")
        try:
            canonical_lines = read_paleographic_lines(
                CANONICAL_EDITION.read_text(encoding="utf-8")
            )
        except (OSError, PrototypeBuildError) as exc:
            errors.append(f"No se pudo leer la transcripción canónica: {exc}")
        else:
            generated_lines = _generated_paleographic_lines(transcription)
            if generated_lines != canonical_lines:
                errors.append(
                    "Las líneas paleográficas generadas no coinciden exactamente con las "
                    "18 líneas canónicas o carecen de bloque de líneas semántico"
                )
            if len(generated_lines) != PALEOGRAPHIC_LINE_COUNT:
                errors.append(
                    f"La transcripción generada no contiene {PALEOGRAPHIC_LINE_COUNT} líneas"
                )
            hyphen_endings = tuple(
                line.rsplit(maxsplit=1)[-1]
                for line in generated_lines
                if line.endswith("-")
            )
            if hyphen_endings != DOCUMENTARY_HYPHEN_ENDINGS:
                errors.append("No se conservan los guiones documentales de final de línea")
        if not re.search(
            r"!\[[^\]]{20,}\]\(assets/folio-315v\.png\)"
            r'\{[^}]*fig-alt="[^"]{20,}"[^}]*\}',
            transcription,
        ):
            errors.append("El recorte paleográfico carece de texto alternativo suficiente")
    if GENERATED["modernized"].is_file():
        modernized = GENERATED["modernized"].read_text(encoding="utf-8")
        if "[^20]:" not in modernized or "[^21]:" not in modernized:
            errors.append("La respuesta 17 no conserva sus notas 20 y 21")
    if GENERATED["apparatus"].is_file():
        apparatus = GENERATED["apparatus"].read_text(encoding="utf-8")
        absent = sorted(identifier for identifier in expected_ids if identifier not in apparatus)
        if absent:
            errors.append("Identificadores ausentes del aparato: " + ", ".join(absent))

    assets_path = PUBLICATION_ROOT / "meta" / "assets.yml"
    assets_data = yaml.safe_load(assets_path.read_text(encoding="utf-8"))
    assets = assets_data.get("assets", []) if isinstance(assets_data, dict) else []
    if len(assets) != 2:
        errors.append("meta/assets.yml debe declarar exactamente dos derivados")
    for asset in assets:
        source = asset.get("source", {})
        if source.get("file_id") != MANUSCRIPT_FILE_ID or source.get("page") != 12:
            errors.append("Procedencia incorrecta en meta/assets.yml")
        destination = asset.get("destination", "")
        if not destination.startswith("generated/assets/"):
            errors.append("Los destinos facsimilares deben permanecer en generated/assets/")

    quarto_data = yaml.safe_load(
        (PUBLICATION_ROOT / "_quarto.yml").read_text(encoding="utf-8")
    )
    navigation = quarto_data.get("book", {}).get("chapters", [])
    expected_navigation = (
        "content/00-preliminares/00-prueba-tecnica.qmd",
        "content/01-catastro/01-catastro-ensenada.qmd",
        "content/01-catastro/02-respuestas-generales-interrogatorio.qmd",
        "content/01-catastro/03-expediente-sorribos-santibanez.qmd",
        "content/01-catastro/04-manuscrito-volumen-actual.qmd",
        "content/02-estudio/05-lugar-senorio-concejo-ordas.qmd",
        "content/02-estudio/06-vecinos-hogares-viviendas-trabajo.qmd",
        "content/02-estudio/07-tierra-sistema-agrario-medidas.qmd",
        "content/02-estudio/09-rio-molinos-recursos.qmd",
        "generated/14-facsimil-prototipo.qmd",
        "generated/15-transcripcion-prototipo.qmd",
        "generated/16-modernizada-prototipo.qmd",
        "generated/aparato-molinos.qmd",
    )
    for item in expected_navigation:
        if navigation.count(item) != 1:
            errors.append(f"La navegación debe registrar una sola vez: {item}")
    positions = [navigation.index(item) for item in expected_navigation if item in navigation]
    if positions != sorted(positions):
        errors.append(
            "Orden incorrecto de los capítulos 1–7 y del prototipo en la navegación"
        )

    chapters_data = yaml.safe_load(
        (PUBLICATION_ROOT / "meta" / "chapters.yml").read_text(encoding="utf-8")
    )
    manifest = chapters_data.get("chapters", [])
    manifest_paths = [item.get("path") for item in manifest]
    manifest_ids = [item.get("chapter_id") for item in manifest]
    if "Fase 2B" in chapters_data.get("purpose", ""):
        errors.append("meta/chapters.yml sigue limitado exclusivamente a la Fase 2B")
    for item in expected_navigation:
        if manifest_paths.count(item) != 1:
            errors.append(f"meta/chapters.yml debe registrar una sola vez: {item}")
    manifest_positions = [
        manifest_paths.index(item)
        for item in expected_navigation
        if item in manifest_paths
    ]
    if manifest_positions != sorted(manifest_positions):
        errors.append("Orden incorrecto de los capítulos 1–7 en meta/chapters.yml")
    if len(manifest_ids) != len(set(manifest_ids)):
        errors.append("Los chapter_id de meta/chapters.yml deben ser únicos")

    for path, text in _all_publication_texts():
        if path.resolve() == Path(__file__).resolve():
            continue
        if re.search(r"(?:/home/|/tmp/|[A-Za-z]:\\\\)", text):
            errors.append(f"Ruta local absoluta en {path.relative_to(PUBLICATION_ROOT)}")
        if "b64_string" in text or "download_url" in text:
            errors.append(f"Referencia sensible inesperada en {path.relative_to(PUBLICATION_ROOT)}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--rendered",
        action="store_true",
        help="valida además la lineación en los artefactos HTML y PDF renderizados",
    )
    args = parser.parse_args(argv)
    try:
        errors = validate()
        if args.rendered:
            errors.extend(validate_rendered_outputs())
    except (OSError, ValueError, yaml.YAMLError, PrototypeBuildError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    scope = " y artefactos HTML/PDF" if args.rendered else ""
    print(
        "PASS: capítulos 1–7, prototipo 2B, metadatos, anclas, evidencia y regresiones"
        f"{scope} validados"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

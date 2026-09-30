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
    return errors


def _front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path} no comienza con front matter")
    _, metadata, _ = text.split("---", 2)
    data = yaml.safe_load(metadata)
    if not isinstance(data, dict):
        raise ValueError(f"Front matter inválido en {path}")
    return data


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
    missing_registry = sorted(expected_ids - registered)
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
        "content/02-estudio/09-rio-molinos-recursos.qmd",
        "generated/14-facsimil-prototipo.qmd",
        "generated/15-transcripcion-prototipo.qmd",
        "generated/16-modernizada-prototipo.qmd",
        "generated/aparato-molinos.qmd",
    )
    for item in expected_navigation:
        if item not in navigation:
            errors.append(f"Falta en la navegación: {item}")
    positions = [navigation.index(item) for item in expected_navigation if item in navigation]
    if positions != sorted(positions):
        errors.append("Orden incorrecto del capítulo 1 y del prototipo en la navegación")

    chapters_data = yaml.safe_load(
        (PUBLICATION_ROOT / "meta" / "chapters.yml").read_text(encoding="utf-8")
    )
    manifest = chapters_data.get("chapters", [])
    manifest_paths = [item.get("path") for item in manifest]
    if "Fase 2B" in chapters_data.get("purpose", ""):
        errors.append("meta/chapters.yml sigue limitado exclusivamente a la Fase 2B")
    for item in expected_navigation[:3]:
        if item not in manifest_paths:
            errors.append(f"Falta en meta/chapters.yml: {item}")
    manifest_positions = [
        manifest_paths.index(item)
        for item in expected_navigation[:3]
        if item in manifest_paths
    ]
    if manifest_positions != sorted(manifest_positions):
        errors.append("Orden incorrecto del capítulo 1 en meta/chapters.yml")

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
        "PASS: capítulo 1, prototipo 2B, metadatos, anclas, evidencia y regresiones"
        f"{scope} validados"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

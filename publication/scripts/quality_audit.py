#!/usr/bin/env python3
"""Structural quality and accessibility checks for the Phase 5B book."""

from __future__ import annotations

import html
import hashlib
import re
import subprocess
import tempfile
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


PUBLICATION_ROOT = Path(__file__).resolve().parent.parent
BOOK_ROOT = PUBLICATION_ROOT / "_book"
PDF_PATH = BOOK_ROOT / "sorribos-santibanez-ordas-1752.pdf"
PARTS = (
    "Parte I. El Catastro y su documento",
    "Parte II. Sorribos y Santibáñez en 1752",
    "Parte III. El manuscrito original",
    "Parte IV. Transcripción y aparato crítico",
    "Parte V. El Catastro en español actual",
    "Parte VI. Aparatos e índices",
)
PRELIMINARIES = (
    "content/00-preliminares/01-creditos.html",
    "content/00-preliminares/02-prologo.html",
    "content/00-preliminares/03-introduccion.html",
    "content/00-preliminares/04-convenciones.html",
)
APPARATUS = (
    "generated/glosario.html",
    "generated/cuadros-cuantitativos.html",
    "generated/concordancia.html",
    "generated/matriz-evidencia.html",
)
NARRATIVE_APPARATUS = (
    "content/06-aparatos/cuestiones-abiertas.html",
    "content/06-aparatos/historia-intelectual-editorial.html",
    "content/06-aparatos/como-citar.html",
    "content/06-aparatos/bibliografia.html",
    "content/06-aparatos/colofon.html",
)
INDEXES = tuple(
    f"generated/indices/{number:02d}-{slug}.html"
    for number, slug in enumerate(
        (
            "indice-onomastico",
            "indice-toponimos",
            "indice-instituciones",
            "indice-oficios",
            "indice-medidas",
            "indice-productos-recursos",
            "indice-cargas-fiscalidad",
            "indice-preguntas-respuestas",
            "indice-materias",
        ),
        start=1,
    )
)
LOCAL_HOME_PREFIX = "/" + "home/"
APPROVED_MAP_SHA256 = {
    "mapa-regional.svg": "2c6f3c76293a3c67aa698b9abd8b6ad184ad35c4fae3d80de6ec2f176ce99a1d",
    "mapa-local.svg": "ebc54b6593eab73778860a41db66221e78b6b83028b51602769d02a523fd15df",
}


@dataclass
class TableAudit:
    label: str = ""
    caption: str = ""
    has_thead: bool = False
    header_scopes: list[str] = field(default_factory=list)


class PublicationHTMLParser(HTMLParser):
    """Collect the small semantic surface needed by the publication audit."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.lang = ""
        self.ids: list[str] = []
        self.headings: list[tuple[int, str]] = []
        self.h1_count = 0
        self.main_count = 0
        self.nav_count = 0
        self.images: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []
        self.buttons: list[dict[str, str]] = []
        self.tables: list[TableAudit] = []
        self.title = ""
        self.visible_text: list[str] = []
        self._active_heading: tuple[int, list[str]] | None = None
        self._active_link: dict[str, object] | None = None
        self._active_button: dict[str, object] | None = None
        self._active_table: TableAudit | None = None
        self._caption_parts: list[str] | None = None
        self._title_parts: list[str] | None = None
        self._suppressed = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if identifier := values.get("id"):
            self.ids.append(identifier)
        if tag == "html":
            self.lang = values.get("lang", "")
        elif tag == "main":
            self.main_count += 1
        elif tag == "nav":
            self.nav_count += 1
        elif tag in {"script", "style"}:
            self._suppressed += 1
        elif tag == "title":
            self._title_parts = []
        elif re.fullmatch(r"h[1-6]", tag):
            level = int(tag[1])
            self._active_heading = (level, [])
            if level == 1:
                self.h1_count += 1
        elif tag == "img":
            self.images.append(values)
            if self._active_link is not None:
                self._active_link["image_alt"] = values.get("alt", "")
        elif tag == "a":
            self._active_link = {**values, "text_parts": [], "image_alt": ""}
        elif tag == "button":
            self._active_button = {**values, "text_parts": []}
        elif tag == "table":
            self._active_table = TableAudit(label=values.get("aria-label", ""))
        elif tag == "thead" and self._active_table:
            self._active_table.has_thead = True
        elif tag == "th" and self._active_table:
            self._active_table.header_scopes.append(values.get("scope", ""))
        elif tag == "caption" and self._active_table:
            self._caption_parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"}:
            self._suppressed = max(0, self._suppressed - 1)
        elif tag == "title" and self._title_parts is not None:
            self.title = " ".join("".join(self._title_parts).split())
            self._title_parts = None
        elif re.fullmatch(r"h[1-6]", tag) and self._active_heading:
            level, parts = self._active_heading
            self.headings.append((level, " ".join("".join(parts).split())))
            self._active_heading = None
        elif tag == "a" and self._active_link is not None:
            self._active_link["text"] = " ".join(
                "".join(self._active_link.pop("text_parts")).split()
            )
            self.links.append(self._active_link)  # type: ignore[arg-type]
            self._active_link = None
        elif tag == "button" and self._active_button is not None:
            self._active_button["text"] = " ".join(
                "".join(self._active_button.pop("text_parts")).split()
            )
            self.buttons.append(self._active_button)  # type: ignore[arg-type]
            self._active_button = None
        elif tag == "caption" and self._caption_parts is not None and self._active_table:
            self._active_table.caption = " ".join("".join(self._caption_parts).split())
            self._caption_parts = None
        elif tag == "table" and self._active_table:
            self.tables.append(self._active_table)
            self._active_table = None

    def handle_data(self, data: str) -> None:
        if self._suppressed == 0:
            self.visible_text.append(data)
        if self._title_parts is not None:
            self._title_parts.append(data)
        if self._active_heading:
            self._active_heading[1].append(data)
        if self._active_link is not None:
            self._active_link["text_parts"].append(data)  # type: ignore[union-attr]
        if self._active_button is not None:
            self._active_button["text_parts"].append(data)  # type: ignore[union-attr]
        if self._caption_parts is not None:
            self._caption_parts.append(data)


def parse_html(path: Path) -> PublicationHTMLParser:
    parser = PublicationHTMLParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def navigation_paths(items: list[object]) -> list[str]:
    paths: list[str] = []
    for item in items:
        if isinstance(item, str):
            paths.append(item)
        elif isinstance(item, dict):
            paths.extend(navigation_paths(item.get("chapters", [])))
    return paths


def audit_visual_apparatus(publication_root: Path = PUBLICATION_ROOT) -> list[str]:
    """Validate the bounded, accessible visual apparatus approved for PKG-07."""

    errors: list[str] = []
    chapters = {
        "content/01-catastro/03-expediente-sorribos-santibanez.qmd": (
            "../../assets/visual/cronologia-documental.svg",
            "../../assets/cartography/mapa-local.svg",
        ),
        "content/02-estudio/05-lugar-senorio-concejo-ordas.qmd": (
            "../../assets/cartography/mapa-regional.svg",
        ),
        "content/02-estudio/13-economia-rural-integrada-vulnerabilidades-resiliencia-limites.qmd": (
            "../../assets/visual/diagrama-economia-rural.svg",
        ),
    }
    all_chapter_text = ""
    for relative, references in chapters.items():
        path = publication_root / relative
        if not path.is_file():
            errors.append(f"Falta el capítulo que integra aparato visual: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        all_chapter_text += text
        for reference in references:
            if text.count(f"]({reference})") != 1:
                errors.append(f"{relative} debe integrar una sola vez {reference}")
        for figure in re.findall(r"!\[[^\]]+\]\([^\)]+\.svg\)\{[^}]+\}", text):
            if ".visual-apparatus" not in figure or not re.search(
                r'fig-alt="[^"]{40,}"', figure
            ):
                errors.append(f"Figura SVG sin clase o texto alternativo suficiente en {relative}")

    for name, expected in APPROVED_MAP_SHA256.items():
        path = publication_root / "assets" / "cartography" / name
        if not path.is_file():
            errors.append(f"Falta el mapa aprobado: {name}")
            continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            errors.append(f"El mapa aprobado fue modificado: {name}")

    asset_paths = (
        publication_root / "assets" / "visual" / "cronologia-documental.svg",
        publication_root / "assets" / "visual" / "diagrama-economia-rural.svg",
        publication_root / "assets" / "cartography" / "mapa-regional.svg",
        publication_root / "assets" / "cartography" / "mapa-local.svg",
    )
    for path in asset_paths:
        if not path.is_file():
            errors.append(f"Falta el recurso visual: {path.name}")
            continue
        text = path.read_text(encoding="utf-8")
        if (
            'role="img"' not in text
            or "aria-labelledby=" not in text
            or "<title id=" not in text
            or "<desc id=" not in text
        ):
            errors.append(f"SVG sin estructura accesible: {path.name}")

    timeline = asset_paths[0]
    if timeline.is_file():
        text = timeline.read_text(encoding="utf-8")
        for value in ("1215", "1267", "1715", "17·09·1752", "1768", "1831 / 1864", "1836 / 1848", "Hoy"):
            if value not in text:
                errors.append(f"La cronología no conserva el hito {value}")
        if "TOP-006" in text or "TOP-006" in all_chapter_text:
            errors.append("TOP-006 no puede salir de la matriz de evidencia")

    diagram = asset_paths[1]
    if diagram.is_file():
        text = diagram.read_text(encoding="utf-8")
        for label in (
            "Tierra, cultivos y prados",
            "Ganado y aprovechamientos",
            "Trabajo y espacio doméstico",
            "Agua y molinos",
            "Común y servicios",
            "Derechos, fiscalidad y rentas",
            "Dinero, especie y servicio",
            "Conexiones exteriores",
            "No es cuenta, flujo",
        ):
            if label not in text:
                errors.append(f"El diagrama económico no conserva: {label}")
        if "marker-end" in text or "<marker" in text:
            errors.append("El diagrama económico introduce dirección causal mediante flechas")

    styles_path = publication_root / "styles" / "book.scss"
    styles = styles_path.read_text(encoding="utf-8") if styles_path.is_file() else ""
    if ".visual-apparatus" not in styles or ".visual-source" not in styles:
        errors.append("Faltan estilos responsivos del aparato visual")
    return errors


def audit_configuration(publication_root: Path = PUBLICATION_ROOT) -> list[str]:
    errors: list[str] = []
    quarto = yaml.safe_load((publication_root / "_quarto.yml").read_text(encoding="utf-8"))
    if not str(quarto.get("lang", "")).startswith("es"):
        errors.append("La configuración Quarto no declara español como idioma")
    book = quarto.get("book", {})
    for field, expected in (
        ("title", "Sorribos y Santibáñez de Ordás en 1752"),
        ("subtitle", "Estudio histórico y edición integral del Catastro de Ensenada"),
        ("author", "Miguel Conde de Simón"),
        ("date", "2026"),
        ("date-format", "YYYY"),
    ):
        if book.get(field) != expected:
            errors.append(f"Identidad editorial incorrecta en book.{field}")
    items = book.get("chapters", [])
    parts = tuple(item.get("part") for item in items if isinstance(item, dict))
    if parts != PARTS:
        errors.append("Las seis partes no coinciden con el Plan Maestro")
    paths = navigation_paths(items)
    if "content/00-preliminares/00-prueba-tecnica.qmd" in paths:
        errors.append("La prueba técnica continúa publicada")
    expected_preliminaries = tuple(
        path.replace(".html", ".qmd") for path in PRELIMINARIES
    )
    if (
        len(paths) != 39
        or tuple(paths[:5]) != ("index.qmd", *expected_preliminaries)
        or paths[-1] != "content/06-aparatos/colofon.qmd"
    ):
        errors.append(
            "La composición debe contener 39 documentos públicos, comenzar "
            "por portada, créditos, prólogo, introducción y convenciones y "
            "terminar con el colofón"
        )
    manifest = yaml.safe_load(
        (publication_root / "meta/chapters.yml").read_text(encoding="utf-8")
    )["chapters"]
    public_manifest = [item["path"] for item in manifest if item["path"] in paths]
    if public_manifest != paths:
        errors.append("El manifiesto y la navegación pública no conservan el mismo orden")
    index = (publication_root / "index.qmd").read_text(encoding="utf-8").casefold()
    for residue in (
        "prueba técnica",
        "se incorporarán en fases posteriores",
        "edición en desarrollo",
        "estado de prepublicación",
    ):
        if residue in index:
            errors.append(f"La portada conserva el residuo: {residue}")
    styles = (publication_root / "styles/book.scss").read_text(encoding="utf-8")
    if ":focus-visible" not in styles or "table-scroll" not in styles:
        errors.append("Los estilos no cubren foco visible y reflow de tablas")
    errors.extend(audit_visual_apparatus(publication_root))
    return errors


def _local_target(source: Path, href: str) -> tuple[Path, str] | None:
    parsed = urlsplit(html.unescape(href))
    if parsed.scheme or parsed.netloc or href.startswith(("mailto:", "tel:", "javascript:")):
        return None
    path = unquote(parsed.path)
    target = source if not path else (source.parent / path).resolve()
    return target, unquote(parsed.fragment)


def audit_html_book(book_root: Path = BOOK_ROOT) -> list[str]:
    errors: list[str] = []
    html_paths = sorted(book_root.rglob("*.html"))
    if len(html_paths) != 39:
        errors.append(f"Se esperaban 39 documentos HTML y existen {len(html_paths)}")
    parsed = {path.resolve(): parse_html(path) for path in html_paths}
    titles: dict[str, Path] = {}
    ids = {path: set(parser.ids) for path, parser in parsed.items()}
    numbered: list[int] = []
    for path, parser in parsed.items():
        relative = path.relative_to(book_root.resolve())
        source = path.read_text(encoding="utf-8")
        if not parser.lang.startswith("es"):
            errors.append(f"Idioma HTML incorrecto en {relative}: {parser.lang or 'ausente'}")
        if parser.h1_count != 1:
            errors.append(f"{relative} debe contener un h1 y contiene {parser.h1_count}")
        if parser.main_count != 1 or parser.nav_count < 1:
            errors.append(f"Landmarks incompletos en {relative}")
        if not parser.title:
            errors.append(f"Título HTML ausente en {relative}")
        elif parser.title in titles:
            errors.append(f"Título HTML duplicado: {parser.title}")
        else:
            titles[parser.title] = path
        if len(parser.ids) != len(set(parser.ids)):
            errors.append(f"IDs duplicados en {relative}")
        levels = [level for level, _ in parser.headings]
        if any(current > previous + 1 for previous, current in zip(levels, levels[1:])):
            errors.append(f"Salto de jerarquía de encabezados en {relative}")
        for image in parser.images:
            if "alt" not in image:
                errors.append(f"Imagen sin atributo alt en {relative}: {image.get('src', '')}")
        h1_texts = [text for level, text in parser.headings if level == 1]
        if h1_texts and (match := re.match(r"^(\d+)\s", h1_texts[0])):
            numbered.append(int(match.group(1)))
        for position, table in enumerate(parser.tables, start=1):
            if not table.has_thead or not table.header_scopes:
                errors.append(f"Tabla {position} sin cabeceras semánticas en {relative}")
            if any(scope not in {"col", "row"} for scope in table.header_scopes):
                errors.append(f"Tabla {position} con th sin scope en {relative}")
            if not (table.caption or table.label):
                errors.append(f"Tabla {position} sin nombre accesible en {relative}")
        for button in parser.buttons:
            if not (button.get("text") or button.get("aria-label") or button.get("title")):
                errors.append(f"Botón sin nombre accesible en {relative}")
        for link in parser.links:
            href = str(link.get("href", ""))
            name = link.get("text") or link.get("aria-label") or link.get("title") or link.get("image_alt")
            if href and not str(name).strip():
                errors.append(f"Enlace sin nombre accesible en {relative}: {href}")
            if ".qmd" in href or LOCAL_HOME_PREFIX in href or "project/" in href:
                errors.append(f"Enlace de desarrollo en {relative}: {href}")
            local = _local_target(path, href)
            if local is None or not href:
                continue
            target, fragment = local
            if not target.exists():
                errors.append(f"Destino local inexistente desde {relative}: {href}")
                continue
            if fragment and target.suffix == ".html" and fragment not in ids.get(target, set()):
                errors.append(f"Fragmento inexistente desde {relative}: {href}")
        visible = " ".join("".join(parser.visible_text).split()).casefold()
        for residue in (
            "prueba técnica",
            "smoke test",
            "infraestructura mínima",
            "{.unnumbered}",
        ):
            if residue in visible:
                errors.append(f"Residuo público en {relative}: {residue}")
        navigation_numbers = {
            int(value)
            for value in re.findall(r'class="chapter-number">(\d+)<', source)
        }
        if navigation_numbers - set(range(1, 17)):
            errors.append(
                f"Numeración impropia de aparato o índice en {relative}: "
                f"{sorted(navigation_numbers - set(range(1, 17)))}"
            )
    if sorted(numbered) != list(range(1, 17)):
        errors.append(f"La numeración HTML no es exactamente 1–16: {sorted(numbered)}")
    technical = book_root / "content/00-preliminares/00-prueba-tecnica.html"
    if technical.exists():
        errors.append("La salida HTML conserva el capítulo técnico")
    for relative in (*PRELIMINARIES, *APPARATUS, *NARRATIVE_APPARATUS, *INDEXES):
        if not (book_root / relative).is_file():
            errors.append(f"Falta el documento público {relative}")
    return errors


def audit_release_candidate(book_root: Path = BOOK_ROOT) -> list[str]:
    """Reject private inputs and require the validated PDF download in a 6A build."""

    errors: list[str] = []
    if not book_root.is_dir():
        return [f"Falta la salida candidata: {book_root}"]

    files = tuple(path for path in book_root.rglob("*") if path.is_file())
    pdfs = tuple(path for path in files if path.suffix.casefold() == ".pdf")
    if pdfs != (PDF_PATH,):
        rendered = ", ".join(str(path.relative_to(book_root)) for path in pdfs)
        errors.append(
            "La candidata debe contener únicamente el PDF descargable validado; "
            f"encontrados: {rendered or 'ninguno'}"
        )

    index_path = book_root / "index.html"
    if index_path.is_file():
        index = parse_html(index_path)
        expected = PDF_PATH.name
        if not any(
            unquote(urlsplit(str(link.get("href", ""))).path).endswith(expected)
            for link in index.links
        ):
            errors.append(f"La portada HTML no enlaza el PDF descargable {expected}")
    else:
        errors.append("Falta index.html en la candidata")

    forbidden_names = {
        ".env",
        ".git",
        "netlify.toml",
        "sorrios_ensenada_orden_lectura_calidad_original.pdf",
        "composition-0.6.pdf",
    }
    forbidden_suffixes = {".qmd", ".py", ".yml", ".yaml", ".toml"}
    for path in files:
        relative = path.relative_to(book_root)
        if any(part in forbidden_names for part in relative.parts):
            errors.append(f"Archivo privado o de configuración en la candidata: {relative}")
        if path.suffix.casefold() in forbidden_suffixes:
            errors.append(f"Fuente o configuración publicada accidentalmente: {relative}")

    secret_patterns = (
        re.compile(rb"ghp_[A-Za-z0-9]{20,}"),
        re.compile(rb"github_pat_[A-Za-z0-9_]{20,}"),
        re.compile(rb"(?i)authorization\s*:\s*bearer\s+[A-Za-z0-9._-]{16,}"),
    )
    local_home_prefix = b"/" + b"home/"
    text_suffixes = {".html", ".css", ".js", ".json", ".xml", ".txt"}
    for path in files:
        if path.suffix.casefold() not in text_suffixes:
            continue
        payload = path.read_bytes()
        if local_home_prefix in payload or re.search(rb"[A-Za-z]:\\\\", payload):
            errors.append(
                f"Ruta absoluta del sistema en {path.relative_to(book_root)}"
            )
        if any(pattern.search(payload) for pattern in secret_patterns):
            errors.append(
                f"Patrón de credencial en {path.relative_to(book_root)}"
            )
    return errors


def _run(*command: str) -> str:
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return result.stdout + result.stderr


def audit_pdf(pdf_path: Path = PDF_PATH, *, deep: bool = False) -> list[str]:
    errors: list[str] = []
    if not pdf_path.is_file():
        return [f"Falta el PDF: {pdf_path}"]
    try:
        info = _run("pdfinfo", str(pdf_path))
        fonts = _run("pdffonts", str(pdf_path))
        text = _run("pdftotext", "-layout", str(pdf_path), "-")
        destinations = _run("pdfinfo", "-dests", str(pdf_path))
        urls = _run("pdfinfo", "-url", str(pdf_path))
        images = _run("pdfimages", "-list", str(pdf_path))
    except (OSError, subprocess.CalledProcessError) as exc:
        return [f"No se pudo inspeccionar el PDF con Poppler: {exc}"]
    if "Title:           Sorribos y Santibáñez de Ordás en 1752" not in info:
        errors.append("Título PDF ausente o incorrecto")
    if not re.search(r"^Author:\s+Miguel Conde de Simón$", info, re.MULTILINE):
        errors.append("Autor PDF ausente o incorrecto")
    if not re.search(r"^Pages:\s+\d+$", info, re.MULTILINE):
        errors.append("Número de páginas PDF no inspeccionable")
    font_rows = [line.split() for line in fonts.splitlines()[2:] if line.strip()]
    if not font_rows or any(len(row) < 5 or row[-5] != "yes" for row in font_rows):
        errors.append("Alguna fuente PDF no aparece embebida")
    for character in "áéíóúñ†[]":
        if character not in text:
            errors.append(f"Glifo crítico no extraíble del PDF: {character}")
    if re.search(r"^# ", text, re.MULTILINE):
        errors.append("El PDF conserva un marcador Markdown en un título editorial")
    for title in (
        "El Catastro de Ensenada",
        "Facsímil íntegro del expediente",
        "Transcripción y aparato crítico de las 35 unidades",
        "El Catastro en español actual",
        "Glosario histórico",
        "Índice de materias",
    ):
        if title not in text:
            errors.append(f"Contenido editorial ausente del PDF: {title}")
    for chapter in range(1, 17):
        if f'"chapter.{chapter}"' not in destinations:
            errors.append(f"Destino PDF ausente para el capítulo {chapter}")
    if any(marker in urls for marker in (".qmd", LOCAL_HOME_PREFIX, "project/")):
        errors.append("El PDF contiene enlaces URI de desarrollo")
    if not images.strip() or "page" not in images.lower():
        errors.append("Las imágenes PDF no pudieron inventariarse")
    if deep:
        try:
            with tempfile.TemporaryDirectory(prefix="sorrios-pdf-audit-") as directory:
                prefix = str(Path(directory) / "page")
                _run("pdftoppm", "-r", "6", "-png", str(pdf_path), prefix)
                expected = int(re.search(r"^Pages:\s+(\d+)$", info, re.MULTILINE).group(1))
                actual = len(tuple(Path(directory).glob("page-*.png")))
                if actual != expected:
                    errors.append(f"Rasterización PDF incompleta: {actual}/{expected} páginas")
        except (AttributeError, OSError, subprocess.CalledProcessError) as exc:
            errors.append(f"No se pudo rasterizar cada página del PDF: {exc}")
    return errors


def _linear(value: int) -> float:
    component = value / 255
    return component / 12.92 if component <= 0.04045 else ((component + 0.055) / 1.055) ** 2.4


def contrast_ratio(foreground: str, background: str) -> float:
    def luminance(color: str) -> float:
        red, green, blue = (int(color[index : index + 2], 16) for index in (1, 3, 5))
        return 0.2126 * _linear(red) + 0.7152 * _linear(green) + 0.0722 * _linear(blue)

    first, second = sorted((luminance(foreground), luminance(background)), reverse=True)
    return (first + 0.05) / (second + 0.05)


def audit_contrast() -> list[str]:
    errors: list[str] = []
    pairs = {
        "texto": ("#242424", "#ffffff", 4.5),
        "enlace": ("#6b3f20", "#ffffff", 4.5),
        "subtítulo": ("#5f5f5f", "#ffffff", 4.5),
        "navegación material": ("#555555", "#ffffff", 4.5),
        "foco": ("#005fcc", "#ffffff", 3.0),
    }
    for name, (foreground, background, minimum) in pairs.items():
        ratio = contrast_ratio(foreground, background)
        if ratio < minimum:
            errors.append(f"Contraste insuficiente para {name}: {ratio:.2f}:1")
    return errors

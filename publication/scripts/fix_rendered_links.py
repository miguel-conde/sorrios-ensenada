#!/usr/bin/env python3
"""Repair rendered HTML links and add deterministic table semantics."""

from __future__ import annotations

import sys
import html
import re
from pathlib import Path


REPLACEMENTS = {
    "../../generated/14-facsimil-prototipo.qmd#pagina-digital-12": (
        "../../generated/14-facsimil.html#pagina-digital-12"
    ),
    "../../generated/15-transcripcion-prototipo.qmd#folio-315v": (
        "../../generated/15-transcripcion.html#folio-315v"
    ),
    "../../generated/16-modernizada-prototipo.qmd#respuesta-17": (
        "../../generated/16-edicion-modernizada.html#respuesta-17"
    ),
    "../../generated/aparato-molinos.qmd#matriz-molinera": (
        "../../generated/matriz-evidencia.html#evidencia-hid-001"
    ),
}

HEADING_RE = re.compile(r"<h[1-6]\b[^>]*>(.*?)</h[1-6]>", re.DOTALL)
TABLE_RE = re.compile(r"<table\b([^>]*)>(.*?)</table>", re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")
YEAR_ONLY_DATE_META_RE = re.compile(
    r'(<meta\s+name="dcterms\.date"\s+content=")(?P<year>\d{4})-01-01(\">)'
)


def _plain_text(fragment: str) -> str:
    """Return compact visible text from a small trusted HTML fragment."""

    return " ".join(html.unescape(TAG_RE.sub(" ", fragment)).split())


def _table_accessibility(text: str) -> str:
    """Name tables, scope column headers, and make overflow keyboard-scrollable."""

    title_match = re.search(r"<title>(.*?)</title>", text, re.DOTALL)
    document_title = _plain_text(title_match.group(1)) if title_match else "Documento"
    chunks: list[str] = []
    cursor = 0
    table_number = 0
    for match in TABLE_RE.finditer(text):
        chunks.append(text[cursor : match.start()])
        table_number += 1
        headings = list(HEADING_RE.finditer(text, 0, match.start()))
        heading = _plain_text(headings[-1].group(1)) if headings else document_title
        label = f"Tabla de {heading}" if heading else f"Tabla {table_number} de {document_title}"
        escaped_label = html.escape(label, quote=True)
        attributes = match.group(1)
        if not re.search(r"\baria-label=", attributes):
            attributes += f' aria-label="{escaped_label}"'
        body = re.sub(
            r"<th\b(?![^>]*\bscope=)([^>]*)>",
            r'<th scope="col"\1>',
            match.group(2),
        )
        table = f"<table{attributes}>{body}</table>"
        already_wrapped = re.search(
            r'<div class="table-scroll"[^>]*>\s*$', text[: match.start()]
        )
        if already_wrapped:
            chunks.append(table)
        else:
            chunks.append(
                '<div class="table-scroll" role="region" '
                f'aria-label="{escaped_label}" tabindex="0">{table}</div>'
            )
        cursor = match.end()
    chunks.append(text[cursor:])
    return "".join(chunks)


def fix_rendered_links(output_root: Path) -> int:
    """Patch only Quarto HTML derivatives and return the replacement count."""

    replacements = 0
    for path in sorted(output_root.rglob("*.html")):
        text = path.read_text(encoding="utf-8")
        updated = text
        for old, new in REPLACEMENTS.items():
            occurrences = updated.count(old)
            updated = updated.replace(old, new)
            replacements += occurrences
        # Quarto normalizes a year-only book date to 1 January in Dublin Core
        # metadata. Preserve the approved year without inventing an exact
        # publication day; the visible date is already formatted as YYYY.
        updated = YEAR_ONLY_DATE_META_RE.sub(r"\g<1>\g<year>\g<3>", updated)
        updated = _table_accessibility(updated)
        if updated != text:
            path.write_text(updated, encoding="utf-8", newline="\n")
    return replacements


def main() -> int:
    publication_root = Path(__file__).resolve().parent.parent
    output_root = publication_root / "_book"
    try:
        count = fix_rendered_links(output_root)
    except (OSError, UnicodeError) as exc:
        print(f"Error al ajustar enlaces HTML derivados: {exc}", file=sys.stderr)
        return 1
    print(f"Enlaces HTML derivados ajustados: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

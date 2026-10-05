#!/usr/bin/env python3
"""Rewrite legacy prototype links in rendered HTML to the real 4A/4B chapters."""

from __future__ import annotations

import sys
from pathlib import Path


REPLACEMENTS = {
    "../../generated/14-facsimil-prototipo.qmd#pagina-digital-12": (
        "../../generated/14-facsimil.html#pagina-digital-12"
    ),
    "../../generated/15-transcripcion-prototipo.qmd#folio-315v": (
        "../../generated/15-transcripcion.html#folio-315v"
    ),
}


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

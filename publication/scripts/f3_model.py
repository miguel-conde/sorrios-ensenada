#!/usr/bin/env python3
"""Shared approved F3 presentation and page/unit mapping rules."""

from __future__ import annotations

from dataclasses import dataclass

from critical_edition import POSITION_LABELS, UnitSpec, published_unit_anchor


HTML_CROP_WIDTH = "74%"
PDF_LOCATOR_WIDTH = "28%"


class F3ModelError(RuntimeError):
    """Report an inconsistent F3 mapping or unsupported output format."""


@dataclass(frozen=True)
class PageUnits:
    page: int
    anchor: str
    units: tuple[UnitSpec, ...]


def page_anchor(page: int) -> str:
    """Return the stable chapter-14 anchor for one digital manuscript page."""

    if page <= 0:
        raise F3ModelError(f"Página digital inválida: {page}.")
    return f"pagina-digital-{page:02d}"


def units_for_page(
    specs: tuple[UnitSpec, ...], page: int
) -> tuple[UnitSpec, ...]:
    """Return every material unit mapped explicitly to one page, in order."""

    return tuple(spec for spec in specs if spec.pdf_page == page)


def validate_f3_mapping(
    specs: tuple[UnitSpec, ...], page_count: int
) -> tuple[PageUnits, ...]:
    """Validate and return the complete canonical page-to-unit mapping."""

    if page_count <= 0:
        raise F3ModelError("El facsímil F3 necesita al menos una página.")
    invalid_pages = sorted(
        {spec.pdf_page for spec in specs if not 1 <= spec.pdf_page <= page_count}
    )
    if invalid_pages:
        raise F3ModelError(
            "Hay unidades fuera del rango facsimilar: "
            + ", ".join(str(page) for page in invalid_pages)
        )
    identifiers = [spec.unit_id for spec in specs]
    unit_anchors = [published_unit_anchor(spec) for spec in specs]
    if len(identifiers) != len(set(identifiers)):
        raise F3ModelError("El mapping F3 contiene unidades repetidas.")
    if len(unit_anchors) != len(set(unit_anchors)):
        raise F3ModelError("El mapping F3 contiene anclas de unidad repetidas.")
    pages = tuple(
        PageUnits(page, page_anchor(page), units_for_page(specs, page))
        for page in range(1, page_count + 1)
    )
    missing = [item.page for item in pages if not item.units]
    if missing:
        raise F3ModelError(
            "Hay páginas facsimilares sin unidad asociada: "
            + ", ".join(str(page) for page in missing)
        )
    page_anchors = [item.anchor for item in pages]
    if len(page_anchors) != len(set(page_anchors)):
        raise F3ModelError("El mapping F3 contiene anclas de página repetidas.")
    if sum(len(item.units) for item in pages) != len(specs):
        raise F3ModelError("El mapping F3 contiene unidades huérfanas o duplicadas.")
    return pages


def page_unit_links(
    units: tuple[UnitSpec, ...], *, transcription_target: str
) -> str:
    """Render the links from one complete facsimile page to all its units."""

    return "\n".join(
        f"- [{spec.label} — {POSITION_LABELS[spec.position]}]"
        f"({transcription_target}#{published_unit_anchor(spec)})"
        for spec in units
    )


def unit_image_markdown(
    spec: UnitSpec,
    *,
    output: str,
    asset_path: str,
    facsimile_target: str,
) -> str:
    """Render the approved HTML crop or PDF locator for one material unit."""

    anchor = published_unit_anchor(spec)
    position = POSITION_LABELS[spec.position]
    region = position if spec.position == "complete" else f"mitad {position}"
    alt = (
        f"{spec.label}, {region} de la página digital {spec.pdf_page} "
        "del manuscrito autoritativo."
    )
    if output == "html":
        return f'''::: {{.content-visible when-format="html"}}
::: {{.f3-html-crop}}
![{alt}]({asset_path}){{#fig-f3-html-{anchor} fig-alt="{alt}" width="{HTML_CROP_WIDTH}"}}

[Ampliar el recorte completo de {spec.label}]({asset_path}){{target="_blank" aria-label="Abrir el recorte completo de {spec.label} en una pestaña nueva"}}.
:::
:::'''
    if output == "pdf":
        return f'''::: {{.content-visible when-format="pdf"}}
::: {{.f3-pdf-locator}}
![Localizador documental de {spec.label}, {position} de la página digital {spec.pdf_page}.]({asset_path}){{#fig-f3-pdf-{anchor} fig-alt="Localizador de {spec.label}: {position} de la página digital {spec.pdf_page}." fig-pos="H" width="{PDF_LOCATOR_WIDTH}"}}

**Localización:** página digital {spec.pdf_page}, {position}. El localizador
sirve para reconocer la zona; la reproducción documental principal permanece
en el [facsímil de la página completa]({facsimile_target}).
:::
:::'''
    raise F3ModelError(f"Formato F3 desconocido: {output}")


__all__ = [
    "F3ModelError",
    "HTML_CROP_WIDTH",
    "PDF_LOCATOR_WIDTH",
    "PageUnits",
    "page_anchor",
    "page_unit_links",
    "unit_image_markdown",
    "units_for_page",
    "validate_f3_mapping",
]

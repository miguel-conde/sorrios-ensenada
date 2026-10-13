#!/usr/bin/env python3
"""Build the isolated PKG-04 F3 facsimile/transcription prototype."""

from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path

from check_sources import CheckedSources, SourceCheckError, check_sources
from critical_edition import (
    CriticalEditionError,
    CriticalUnit,
    POSITION_LABELS,
    TEXT_SECTION_NAMES,
    UnitSpec,
    line_block,
    load_unit_specs,
    parse_critical_edition,
    published_unit_anchor,
)
from f3_model import (
    F3ModelError,
    HTML_CROP_WIDTH,
    PDF_LOCATOR_WIDTH,
    page_unit_links,
    unit_image_markdown,
    units_for_page,
)


F3_PAGE = 12
F3_UNIT_IDS = ("folio_315v", "folio_316r")
F3_PROJECT_DIR = "f3-prototype"
CRITICAL_EDITION = Path("project/20_TRABAJO_EDITORIAL/Edicion_Critica.md")
UNITS_MANIFEST = Path("project/00_CONTROL/unidades.yaml")


class F3PrototypeBuildError(RuntimeError):
    """Report an actionable failure while generating the F3 prototype."""


def select_f3_sample(specs: tuple[UnitSpec, ...]) -> tuple[UnitSpec, ...]:
    """Select and validate the bounded left/right sample approved for PKG-04."""

    sample = units_for_page(specs, F3_PAGE)
    if tuple(spec.unit_id for spec in sample) != F3_UNIT_IDS:
        raise F3PrototypeBuildError(
            "La página 12 debe corresponder exactamente a folio_315v y folio_316r."
        )
    if tuple(spec.position for spec in sample) != ("left", "right"):
        raise F3PrototypeBuildError(
            "La muestra F3 debe conservar las posiciones izquierda/derecha declaradas."
        )
    return sample


def _facsimile_qmd(sample: tuple[UnitSpec, ...], checked: CheckedSources) -> str:
    links = page_unit_links(
        sample,
        transcription_target="transcripcion-f3.qmd",
    )
    return f'''---
title: "F3 — Facsímil de la muestra"
chapter-id: f3-facsimil-muestra
publication-status: prototype
sources:
  - manuscript:file_id:{checked.manuscript.file_id}
lightbox: true
---

## Página digital 12 {{#pagina-digital-12}}

::: {{.f3-facsimile-page}}
![Página digital 12 completa del manuscrito autoritativo, con folio 315v a la izquierda y folio 316r a la derecha.](assets/page-12.png){{#fig-f3-pagina-digital-12 fig-alt="Página digital 12 completa; folio 315v ocupa la mitad izquierda y folio 316r la derecha." fig-pos="H" width="88%"}}
:::

La página se conserva completa para mostrar márgenes, pliegue, foliación y
continuidad material. La imagen es un derivado reproducible sin autoridad
textual propia.

### Unidades transcritas en esta página

{links}
'''.rstrip() + "\n"


def _unit_image(unit: CriticalUnit, *, output: str) -> str:
    try:
        return unit_image_markdown(
            unit.spec,
            output=output,
            asset_path=f"assets/{unit.spec.unit_id}.png",
            facsimile_target="index.qmd#pagina-digital-12",
        )
    except F3ModelError as exc:
        raise F3PrototypeBuildError(str(exc)) from exc


def _transcription_qmd(
    units: tuple[CriticalUnit, ...], checked: CheckedSources
) -> str:
    chunks = [
        f'''---
title: "F3 — Transcripción y localización documental"
chapter-id: f3-transcripcion-muestra
publication-status: prototype
sources:
  - project/20_TRABAJO_EDITORIAL/Edicion_Critica.md
  - project/00_CONTROL/unidades.yaml
  - manuscript:file_id:{checked.manuscript.file_id}
lightbox: true
---

::: {{.f3-prototype}}

Esta muestra conserva literalmente la transcripción y el aparato de las dos
unidades de la página digital 12. HTML mantiene el recorte completo y ampliable;
PDF lo sustituye visualmente por un localizador subordinado.'''.rstrip()
    ]
    for unit in units:
        spec = unit.spec
        position = POSITION_LABELS[spec.position]
        chunks.append(f"## {spec.label} {{#{published_unit_anchor(spec)}}}")
        chunks.append(
            "::: {.f3-source-card}\n"
            f"**Facsímil:** página digital {spec.pdf_page}; **posición:** {position}. "
            "[Ver la página completa y sus dos unidades]"
            "(index.qmd#pagina-digital-12).\n"
            ":::"
        )
        chunks.append("### Imagen y localización documental")
        chunks.append(_unit_image(unit, output="html"))
        chunks.append(_unit_image(unit, output="pdf"))
        for name in TEXT_SECTION_NAMES:
            content = (
                line_block(unit.sections[name])
                if name == "Transcripción paleográfica"
                else unit.sections[name]
            )
            chunks.append(f"### {name}\n\n{content}")
    chunks.append(":::")
    return "\n\n".join(chunks).rstrip() + "\n"


def _quarto_config() -> str:
    return '''project:
  type: book
  output-dir: _output

lang: es

book:
  title: "PKG-04 — Prototipo F3"
  subtitle: "Facsímil y transcripción sin duplicación editorial innecesaria"
  chapters:
    - index.qmd
    - transcripcion-f3.qmd
  search: false

format:
  html:
    theme:
      - cosmo
      - styles/book.scss
  pdf:
    lang: en
    toc-title: "Índice"
    crossref:
      fig-title: "Figura"
      fig-prefix: "figura"
    pdf-engine: lualatex
    include-in-header: styles/preamble.tex
'''


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def build_f3_prototype(
    repository_root: Path,
    publication_root: Path,
    checked: CheckedSources,
) -> tuple[Path, ...]:
    """Rebuild the isolated F3 mini-book from current 4A/4B derivatives."""

    repository_root = repository_root.resolve()
    publication_root = publication_root.resolve()
    generated_root = publication_root / "generated"
    target = generated_root / F3_PROJECT_DIR
    try:
        specs = load_unit_specs(repository_root / UNITS_MANIFEST)
        sample_specs = select_f3_sample(specs)
        edition = (repository_root / CRITICAL_EDITION).read_text(encoding="utf-8")
        all_units = parse_critical_edition(edition, specs, checked.manuscript.name)
    except (OSError, UnicodeError, CriticalEditionError) as exc:
        raise F3PrototypeBuildError(str(exc)) from exc
    units_by_id = {unit.spec.unit_id: unit for unit in all_units}
    sample_units = tuple(units_by_id[spec.unit_id] for spec in sample_specs)
    source_assets = {
        "page-12.png": generated_root / "assets/facsimile/page-12.png",
        **{
            f"{spec.unit_id}.png": generated_root
            / "assets/transcription"
            / f"{spec.unit_id}.png"
            for spec in sample_specs
        },
    }
    missing = [str(path) for path in source_assets.values() if not path.is_file()]
    if missing:
        raise F3PrototypeBuildError(
            "Faltan derivados 4A/4B para construir F3: " + ", ".join(missing)
        )
    generated_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".f3-build-", dir=generated_root) as temp:
        staging = Path(temp)
        _write(staging / "_quarto.yml", _quarto_config())
        _write(staging / "index.qmd", _facsimile_qmd(sample_specs, checked))
        _write(staging / "transcripcion-f3.qmd", _transcription_qmd(sample_units, checked))
        assets = staging / "assets"
        assets.mkdir()
        for name, source in source_assets.items():
            shutil.copy2(source, assets / name)
        styles = staging / "styles"
        styles.mkdir()
        shutil.copy2(publication_root / "styles/book.scss", styles / "book.scss")
        shutil.copy2(
            publication_root / "styles/latex/preamble.tex",
            styles / "preamble.tex",
        )
        if target.exists():
            shutil.rmtree(target)
        staging.replace(target)
    outputs = (
        target / "_quarto.yml",
        target / "index.qmd",
        target / "transcripcion-f3.qmd",
        *(target / "assets" / name for name in sorted(source_assets)),
        target / "styles/book.scss",
        target / "styles/preamble.tex",
    )
    return tuple(outputs)


def main() -> int:
    publication_root = Path(__file__).resolve().parent.parent
    repository_root = publication_root.parent
    try:
        checked = check_sources(repository_root, publication_root)
        outputs = build_f3_prototype(repository_root, publication_root, checked)
    except (OSError, UnicodeError, SourceCheckError, F3PrototypeBuildError) as exc:
        print(f"Error de prototipo F3: {exc}", file=sys.stderr)
        return 1
    print(f"Prototipo F3 regenerado: {len(outputs)} salidas ignoradas.")
    return 0


__all__ = [
    "F3_PAGE",
    "F3_PROJECT_DIR",
    "F3_UNIT_IDS",
    "F3PrototypeBuildError",
    "HTML_CROP_WIDTH",
    "PDF_LOCATOR_WIDTH",
    "build_f3_prototype",
    "select_f3_sample",
    "units_for_page",
]


if __name__ == "__main__":
    raise SystemExit(main())

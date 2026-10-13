#!/usr/bin/env python3
"""Generate the complete Phase 4A facsimile from a verified manuscript PDF."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

import yaml
from PIL import Image

from check_sources import CheckedSources
from critical_edition import UnitSpec
from f3_model import F3ModelError, page_unit_links, validate_f3_mapping


FACSIMILE_ASSET_ID = "manuscript-pages-1-18"
FACSIMILE_QMD = "14-facsimil.qmd"
FACSIMILE_CHAPTER_ID = "facsimil-integro-expediente"


class FacsimileBuildError(RuntimeError):
    """Report an actionable failure while generating the complete facsimile."""


@dataclass(frozen=True)
class FacsimileConfig:
    dpi: int
    image_format: str
    page_count: int
    destination_pattern: str


def _load_config(publication_root: Path, checked: CheckedSources) -> FacsimileConfig:
    path = publication_root / "meta" / "assets.yml"
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        raise FacsimileBuildError(f"No se pudo leer {path}: {exc}") from exc
    assets = data.get("assets", []) if isinstance(data, dict) else []
    matches = [asset for asset in assets if asset.get("asset_id") == FACSIMILE_ASSET_ID]
    if len(matches) != 1:
        raise FacsimileBuildError(
            f"meta/assets.yml debe declarar una sola serie {FACSIMILE_ASSET_ID}."
        )
    asset = matches[0]
    source = asset.get("source", {})
    transformation = asset.get("transformation", {})
    expected_source = {
        "file_id": checked.manuscript.file_id,
        "name": checked.manuscript.name,
        "sha256": checked.manuscript.sha256,
        "pages": [1, checked.manuscript.pages],
    }
    mismatches = [key for key, value in expected_source.items() if source.get(key) != value]
    if mismatches:
        raise FacsimileBuildError(
            "La serie facsimilar no coincide con el manuscrito verificado: "
            + ", ".join(mismatches)
        )
    if transformation.get("kind") != "rasterize_complete_pages":
        raise FacsimileBuildError(
            "La serie facsimilar debe usar transformation.kind: rasterize_complete_pages."
        )
    dpi = transformation.get("dpi")
    image_format = transformation.get("format")
    destination = asset.get("destination_pattern")
    if not isinstance(dpi, int) or dpi <= 0:
        raise FacsimileBuildError("La resolución facsimilar debe ser un entero positivo.")
    if image_format != "png":
        raise FacsimileBuildError("4A admite únicamente el formato PNG declarado.")
    if not isinstance(destination, str) or "{page:02d}" not in destination:
        raise FacsimileBuildError(
            "destination_pattern debe contener {page:02d} para la serie facsimilar."
        )
    if asset.get("page_count") != checked.manuscript.pages:
        raise FacsimileBuildError(
            "page_count de la serie facsimilar no coincide con las 18 páginas verificadas."
        )
    return FacsimileConfig(dpi, image_format, checked.manuscript.pages, destination)


def _safe_destination(publication_root: Path, pattern: str) -> tuple[Path, str]:
    relative = PurePosixPath(pattern)
    if relative.is_absolute() or ".." in relative.parts or relative.parts[0] != "generated":
        raise FacsimileBuildError(
            f"Destino facsimilar inseguro; debe permanecer bajo generated/: {pattern}"
        )
    filename_pattern = relative.name
    output_dir = publication_root.joinpath(*relative.parent.parts).resolve()
    generated_root = (publication_root / "generated").resolve()
    if output_dir == generated_root or generated_root not in output_dir.parents:
        raise FacsimileBuildError(
            "La serie facsimilar necesita un subdirectorio propio bajo generated/."
        )
    return output_dir, filename_pattern


def _pdftoppm() -> Path:
    executable = shutil.which("pdftoppm")
    if executable is None:
        raise FacsimileBuildError(
            "No se encontró pdftoppm en PATH; instala Poppler para generar el facsímil."
        )
    return Path(executable).resolve()


def _render_pages(
    pdf: Path,
    staging_dir: Path,
    *,
    dpi: int,
    page_count: int,
    filename_pattern: str,
    pdftoppm: Path,
) -> tuple[Path, ...]:
    outputs: list[Path] = []
    for page in range(1, page_count + 1):
        filename = filename_pattern.format(page=page)
        expected = staging_dir / filename
        prefix = expected.with_suffix("")
        command = [
            str(pdftoppm),
            "-f",
            str(page),
            "-l",
            str(page),
            "-singlefile",
            "-r",
            str(dpi),
            "-png",
            str(pdf),
            str(prefix),
        ]
        try:
            subprocess.run(command, check=True, shell=False)
        except (OSError, subprocess.CalledProcessError) as exc:
            raise FacsimileBuildError(
                f"No se pudo rasterizar la página {page} completa: {exc}"
            ) from exc
        if not expected.is_file() or expected.stat().st_size == 0:
            raise FacsimileBuildError(
                f"pdftoppm no produjo la página facsimilar esperada: {expected.name}"
            )
        try:
            with Image.open(expected) as image:
                image.verify()
                if image.width <= 0 or image.height <= 0:
                    raise FacsimileBuildError(
                        f"La página {page} tiene dimensiones de imagen inválidas."
                    )
        except (OSError, SyntaxError) as exc:
            raise FacsimileBuildError(
                f"La página facsimilar {expected.name} no es un PNG válido: {exc}"
            ) from exc
        outputs.append(expected)
    if len(outputs) != page_count or len({path.name for path in outputs}) != page_count:
        raise FacsimileBuildError(
            "La rasterización no produjo una serie única y completa de páginas 1–18."
        )
    return tuple(outputs)


def _facsimile_qmd(
    checked: CheckedSources,
    config: FacsimileConfig,
    specs: tuple[UnitSpec, ...],
) -> str:
    try:
        mapping = validate_f3_mapping(specs, config.page_count)
    except F3ModelError as exc:
        raise FacsimileBuildError(str(exc)) from exc
    chunks = [
        """---
title: "Facsímil íntegro del expediente"
subtitle: "Parte III. El manuscrito original"
chapter-id: facsimil-integro-expediente
publication-status: generated
sources:
  - manuscript:file_id:{file_id}
lightbox: true
---

Las imágenes reproducen, en su orden material, las 18 páginas completas del
manuscrito autoritativo. Son derivados de publicación sin autoridad propia: no
recortan unidades, no incorporan OCR ni sustituyen la transcripción paleográfica.
""".format(file_id=checked.manuscript.file_id).rstrip()
    ]
    for item in mapping:
        page = item.page
        filename = PurePosixPath(config.destination_pattern.format(page=page)).name
        # La primera página digital es vertical; una anchura menor evita que su
        # nota de procedencia desborde a una hoja separada en la salida PDF.
        width = "62%" if page == 1 else "82%"
        chunks.append(
            f"""## Página digital {page:02d} {{#pagina-digital-{page:02d}}}

::: {{.facsimile-page}}
![Página digital {page:02d} completa del manuscrito autoritativo, conservada con todos sus márgenes y elementos materiales.](assets/facsimile/{filename}){{#fig-pagina-digital-{page:02d} fig-alt="Página digital {page:02d} completa del manuscrito autoritativo, sin recorte de márgenes ni de contenido." fig-pos="H" width="{width}"}}
:::

Página {page} de {config.page_count}; rasterización completa a {config.dpi} dpi desde el PDF autoritativo verificado.

### Unidades transcritas en esta página

{page_unit_links(item.units, transcription_target="15-transcripcion.qmd")}
""".rstrip()
        )
        if page != config.page_count:
            chunks.append("\\newpage")
    return "\n\n".join(chunks).rstrip() + "\n"


def _write_qmd(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8", newline="\n")
    temporary.replace(path)


def build_facsimile(
    publication_root: Path,
    checked: CheckedSources,
    specs: tuple[UnitSpec, ...],
    *,
    pdftoppm: Path | None = None,
) -> tuple[Path, ...]:
    """Rebuild only the outputs owned by the complete facsimile generator."""

    publication_root = publication_root.resolve()
    config = _load_config(publication_root, checked)
    output_dir, filename_pattern = _safe_destination(
        publication_root, config.destination_pattern
    )
    executable = _pdftoppm() if pdftoppm is None else pdftoppm.resolve()
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=".facsimile-build-", dir=output_dir.parent
    ) as temporary:
        staging_dir = Path(temporary)
        staged = _render_pages(
            checked.manuscript_pdf,
            staging_dir,
            dpi=config.dpi,
            page_count=config.page_count,
            filename_pattern=filename_pattern,
            pdftoppm=executable,
        )
        if output_dir.exists():
            shutil.rmtree(output_dir)
        staging_dir.replace(output_dir)
        images = tuple(output_dir / path.name for path in staged)

    qmd = publication_root / "generated" / FACSIMILE_QMD
    _write_qmd(qmd, _facsimile_qmd(checked, config, specs))
    return (qmd, *images)


__all__ = [
    "FACSIMILE_ASSET_ID",
    "FACSIMILE_CHAPTER_ID",
    "FACSIMILE_QMD",
    "FacsimileBuildError",
    "build_facsimile",
]

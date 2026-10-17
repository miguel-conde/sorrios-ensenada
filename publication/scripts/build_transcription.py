#!/usr/bin/env python3
"""Generate Phase 4B: all 35 critical-edition units and their image crops."""

from __future__ import annotations

import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

import yaml
from PIL import Image

from check_sources import CheckedSources
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
from f3_model import F3ModelError, page_anchor, unit_image_markdown
from reader_text import reader_facing_source_text


TRANSCRIPTION_ASSET_ID = "critical-edition-unit-images"
TRANSCRIPTION_QMD = "15-transcripcion.qmd"
TRANSCRIPTION_CHAPTER_ID = "transcripcion-aparato-critico"
CRITICAL_EDITION = Path("project/20_TRABAJO_EDITORIAL/Edicion_Critica.md")
UNITS_MANIFEST = Path("project/00_CONTROL/unidades.yaml")


class TranscriptionBuildError(RuntimeError):
    """Report an actionable failure while generating Phase 4B."""


@dataclass(frozen=True)
class TranscriptionConfig:
    image_format: str
    unit_count: int
    source_pattern: str
    destination_pattern: str


def _load_config(publication_root: Path, checked: CheckedSources) -> TranscriptionConfig:
    path = publication_root / "meta" / "assets.yml"
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        raise TranscriptionBuildError(f"No se pudo leer {path}: {exc}") from exc
    assets = data.get("assets", []) if isinstance(data, dict) else []
    matches = [asset for asset in assets if asset.get("asset_id") == TRANSCRIPTION_ASSET_ID]
    if len(matches) != 1:
        raise TranscriptionBuildError(
            f"meta/assets.yml debe declarar una sola serie {TRANSCRIPTION_ASSET_ID}."
        )
    asset = matches[0]
    source = asset.get("source", {})
    transformation = asset.get("transformation", {})
    expected = {
        "file_id": checked.manuscript.file_id,
        "name": checked.manuscript.name,
        "sha256": checked.manuscript.sha256,
        "pages": [1, checked.manuscript.pages],
    }
    mismatches = [key for key, value in expected.items() if source.get(key) != value]
    if mismatches:
        raise TranscriptionBuildError(
            "La serie de unidades no coincide con el manuscrito verificado: "
            + ", ".join(mismatches)
        )
    if transformation.get("kind") != "crop_units_from_facsimile_pages":
        raise TranscriptionBuildError(
            "La serie debe usar transformation.kind: crop_units_from_facsimile_pages."
        )
    if transformation.get("crop_semantics") != "render_unit.py":
        raise TranscriptionBuildError(
            "La serie debe declarar crop_semantics: render_unit.py."
        )
    image_format = transformation.get("format")
    source_pattern = transformation.get("source_pattern")
    destination_pattern = asset.get("destination_pattern")
    if image_format != "png":
        raise TranscriptionBuildError("4B admite únicamente imágenes PNG.")
    if source_pattern != "generated/assets/facsimile/page-{page:02d}.png":
        raise TranscriptionBuildError(
            "4B debe recortar exclusivamente la serie facsimilar completa de 4A."
        )
    if not isinstance(destination_pattern, str) or "{unit_id}" not in destination_pattern:
        raise TranscriptionBuildError(
            "destination_pattern debe contener {unit_id} para la serie de 35 unidades."
        )
    if asset.get("unit_count") != checked.unit_count:
        raise TranscriptionBuildError(
            "unit_count de la serie no coincide con las 35 unidades verificadas."
        )
    return TranscriptionConfig(
        image_format, checked.unit_count, source_pattern, destination_pattern
    )


def _safe_destination(publication_root: Path, pattern: str) -> tuple[Path, str]:
    relative = PurePosixPath(pattern)
    if (
        relative.is_absolute()
        or ".." in relative.parts
        or len(relative.parts) < 4
        or relative.parts[:3] != ("generated", "assets", "transcription")
    ):
        raise TranscriptionBuildError(f"Destino de transcripción inseguro: {pattern}")
    output_dir = publication_root.joinpath(*relative.parent.parts).resolve()
    expected_dir = (publication_root / "generated" / "assets" / "transcription").resolve()
    if output_dir != expected_dir:
        raise TranscriptionBuildError(
            "La serie de 4B debe poseer exactamente generated/assets/transcription/."
        )
    return output_dir, relative.name


def _crop_box(image: Image.Image, position: str) -> tuple[int, int, int, int]:
    if position == "complete":
        return (0, 0, image.width, image.height)
    if position == "left":
        return (0, 0, image.width // 2, image.height)
    if position == "right":
        return (image.width // 2, 0, image.width, image.height)
    raise TranscriptionBuildError(f"Posición de recorte desconocida: {position}")


def _crop_units(
    publication_root: Path,
    specs: tuple[UnitSpec, ...],
    config: TranscriptionConfig,
    staging_dir: Path,
    filename_pattern: str,
) -> tuple[Path, ...]:
    outputs: list[Path] = []
    for spec in specs:
        source = publication_root / config.source_pattern.format(page=spec.pdf_page)
        if not source.is_file():
            raise TranscriptionBuildError(
                f"Falta la página facsimilar de 4A necesaria para {spec.unit_id}: {source}"
            )
        destination = staging_dir / filename_pattern.format(unit_id=spec.unit_id)
        try:
            with Image.open(source) as page:
                page.load()
                crop = (
                    page.copy()
                    if spec.position == "complete"
                    else page.crop(_crop_box(page, spec.position))
                )
                # Lossless maximum DEFLATE compression materially reduces both
                # the web bundle and the embedded PDF image streams. Pixel data,
                # dimensions and the approved F3 presentation remain unchanged.
                crop.save(destination, format="PNG", compress_level=9)
                crop.close()
            with Image.open(destination) as generated:
                generated.verify()
                if generated.width <= 0 or generated.height <= 0:
                    raise TranscriptionBuildError(
                        f"El recorte {spec.unit_id} tiene dimensiones inválidas."
                    )
        except (OSError, SyntaxError) as exc:
            raise TranscriptionBuildError(
                f"No se pudo generar el recorte de {spec.unit_id}: {exc}"
            ) from exc
        outputs.append(destination)
    if len(outputs) != config.unit_count or len({path.name for path in outputs}) != config.unit_count:
        raise TranscriptionBuildError(
            "El recorte no produjo una serie única y completa de 35 unidades."
        )
    return tuple(outputs)


def _image_markdown(unit: CriticalUnit) -> str:
    spec = unit.spec
    asset_path = f"assets/transcription/{spec.unit_id}.png"
    facsimile_target = f"14-facsimil.qmd#{page_anchor(spec.pdf_page)}"
    try:
        html = unit_image_markdown(
            spec,
            output="html",
            asset_path=asset_path,
            facsimile_target=facsimile_target,
        )
        pdf = unit_image_markdown(
            spec,
            output="pdf",
            asset_path=asset_path,
            facsimile_target=facsimile_target,
        )
    except F3ModelError as exc:
        raise TranscriptionBuildError(str(exc)) from exc
    return html + "\n\n" + pdf


def transcription_qmd(units: tuple[CriticalUnit, ...], checked: CheckedSources) -> str:
    chunks = [
        """---
title: "Transcripción y aparato crítico de las 35 unidades"
subtitle: "Parte IV. Edición del expediente"
chapter-id: transcripcion-aparato-critico
publication-status: generated
sources:
  - project/20_TRABAJO_EDITORIAL/Edicion_Critica.md
  - project/00_CONTROL/unidades.yaml
  - manuscript:file_id:{file_id}
lightbox: true
---

Este capítulo reproduce las 35 unidades documentales en su orden material.
Las imágenes son ayudas de lectura sin autoridad propia; la autoridad textual
permanece en la edición crítica.
""".format(file_id=checked.manuscript.file_id).rstrip()
    ]
    for index, unit in enumerate(units):
        chunks.append(
            f"## {unit.spec.label} {{#{published_unit_anchor(unit.spec)}}}"
        )
        position = POSITION_LABELS[unit.spec.position]
        chunks.append(
            "::: {.f3-source-card}\n"
            f"**Facsímil:** página digital {unit.spec.pdf_page}; "
            f"**posición:** {position}. "
            "[Ver la página completa y sus unidades]"
            f"(14-facsimil.qmd#{page_anchor(unit.spec.pdf_page)}).\n"
            ":::"
        )
        chunks.append("### Imagen\n\n" + _image_markdown(unit))
        for name in TEXT_SECTION_NAMES:
            content = (
                line_block(unit.sections[name])
                if name == "Transcripción paleográfica"
                else reader_facing_source_text(unit.sections[name])
            )
            chunks.append(f"### {name}\n\n{content}")
        if index + 1 < len(units):
            chunks.append("\\newpage")
    return "\n\n".join(chunks).rstrip() + "\n"


def _write_qmd(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8", newline="\n")
    temporary.replace(path)


def build_transcription(
    repository_root: Path,
    publication_root: Path,
    checked: CheckedSources,
) -> tuple[Path, ...]:
    """Rebuild only the outputs owned by the complete 4B generator."""

    repository_root = repository_root.resolve()
    publication_root = publication_root.resolve()
    config = _load_config(publication_root, checked)
    output_dir, filename_pattern = _safe_destination(
        publication_root, config.destination_pattern
    )
    try:
        specs = load_unit_specs(repository_root / UNITS_MANIFEST)
        edition = (repository_root / CRITICAL_EDITION).read_text(encoding="utf-8")
        units = parse_critical_edition(edition, specs, checked.manuscript.name)
    except (OSError, UnicodeError, CriticalEditionError) as exc:
        raise TranscriptionBuildError(str(exc)) from exc
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=".transcription-build-", dir=output_dir.parent
    ) as temporary:
        staging_dir = Path(temporary)
        staged = _crop_units(
            publication_root, specs, config, staging_dir, filename_pattern
        )
        if output_dir.exists():
            shutil.rmtree(output_dir)
        staging_dir.replace(output_dir)
        images = tuple(output_dir / path.name for path in staged)
    qmd = publication_root / "generated" / TRANSCRIPTION_QMD
    try:
        content = transcription_qmd(units, checked)
    except CriticalEditionError as exc:
        raise TranscriptionBuildError(str(exc)) from exc
    _write_qmd(qmd, content)
    return (qmd, *images)


__all__ = [
    "TRANSCRIPTION_ASSET_ID",
    "TRANSCRIPTION_CHAPTER_ID",
    "TRANSCRIPTION_QMD",
    "TranscriptionBuildError",
    "build_transcription",
    "transcription_qmd",
]

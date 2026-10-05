#!/usr/bin/env python3
"""Validate publication sources and prepare generated Quarto output."""

from __future__ import annotations

import sys
from pathlib import Path

from build_facsimile import FacsimileBuildError, build_facsimile
from build_transcription import TranscriptionBuildError, build_transcription
from build_vertical_prototype import PrototypeBuildError, build_vertical_prototype
from check_sources import (
    MANUSCRIPT_ENV,
    LOCAL_MANUSCRIPT_RELATIVE,
    SourceCheckError,
    check_sources,
    resolve_manuscript_pdf,
)


PreparationError = SourceCheckError
_resolve_manuscript_pdf = resolve_manuscript_pdf


def prepare() -> tuple[Path, ...]:
    script_path = Path(__file__).resolve()
    publication_root = script_path.parent.parent
    repository_root = publication_root.parent
    checked = check_sources(repository_root, publication_root)
    facsimile_outputs = build_facsimile(publication_root, checked)
    transcription_outputs = build_transcription(
        repository_root, publication_root, checked
    )
    prototype_outputs = build_vertical_prototype(
        repository_root,
        publication_root,
        checked.manuscript_pdf,
    )
    outputs = (*facsimile_outputs, *transcription_outputs, *prototype_outputs)
    print(
        "Preparación completada: 4 fuentes, 35 unidades y manuscrito verificados; "
        f"{len(facsimile_outputs)} salidas del facsímil, "
        f"{len(transcription_outputs)} salidas de la transcripción y "
        f"{len(prototype_outputs)} derivados del prototipo regenerados."
    )
    return tuple(outputs)


def main() -> int:
    try:
        prepare()
    except (
        OSError,
        UnicodeError,
        PreparationError,
        PrototypeBuildError,
        FacsimileBuildError,
        TranscriptionBuildError,
    ) as error:
        print(f"Error de preparación: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

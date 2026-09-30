#!/usr/bin/env python3
"""Validate publication sources and prepare generated Quarto output."""

from __future__ import annotations

import os
import re
import sys
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

from build_vertical_prototype import PrototypeBuildError, build_vertical_prototype


EXPECTED_SOURCE_COUNT = 4
VERSION_PATTERN = re.compile(r"^\*\*Versión:\*\*\s*(?P<version>\S+)", re.MULTILINE)
MANUSCRIPT_ENV = "SORRIOS_MANUSCRIPT_PDF"
LOCAL_MANUSCRIPT_RELATIVE = Path("sorrios-ensenada") / "manuscript.pdf"


class PreparationError(RuntimeError):
    """Report an actionable publication precondition failure."""


@dataclass(frozen=True)
class Source:
    name: str
    path: str
    version: str


def _yaml_scalar(value: str) -> str:
    """Read the simple quoted or unquoted scalars used by this manifest."""

    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def _manifest_sources(manifest_path: Path) -> tuple[Source, ...]:
    """Extract source path/version pairs without adding a YAML dependency."""

    if not manifest_path.is_file():
        raise PreparationError(f"No existe el manifiesto requerido: {manifest_path}")

    entries: dict[str, dict[str, str]] = {}
    current: str | None = None
    in_sources = False

    for raw_line in manifest_path.read_text(encoding="utf-8").splitlines():
        if raw_line == "sources:":
            in_sources = True
            continue
        if in_sources and raw_line and not raw_line.startswith(" "):
            break
        if not in_sources or not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        source_match = re.fullmatch(r"  ([a-z][a-z0-9_]*):", raw_line)
        if source_match:
            current = source_match.group(1)
            entries[current] = {}
            continue

        field_match = re.fullmatch(r"    (path|version):\s*(.+)", raw_line)
        if field_match and current is not None:
            entries[current][field_match.group(1)] = _yaml_scalar(field_match.group(2))

    if len(entries) != EXPECTED_SOURCE_COUNT:
        raise PreparationError(
            "El manifiesto debe declarar exactamente "
            f"{EXPECTED_SOURCE_COUNT} fuentes; declara {len(entries)}."
        )

    incomplete = [name for name, fields in entries.items() if set(fields) != {"path", "version"}]
    if incomplete:
        raise PreparationError(
            "Faltan path o version en estas fuentes del manifiesto: " + ", ".join(incomplete)
        )

    return tuple(
        Source(name=name, path=fields["path"], version=fields["version"])
        for name, fields in entries.items()
    )


def _source_path(repository_root: Path, source: Source) -> Path:
    relative = PurePosixPath(source.path)
    if relative.is_absolute() or ".." in relative.parts:
        raise PreparationError(
            f"La ruta de {source.name} debe ser relativa a la raíz: {source.path}"
        )
    return repository_root.joinpath(*relative.parts)


def _validate_sources(repository_root: Path, sources: tuple[Source, ...]) -> None:
    for source in sources:
        source_path = _source_path(repository_root, source)
        if not source_path.is_file():
            raise PreparationError(
                f"No existe la fuente {source.name} declarada en el manifiesto: {source.path}"
            )

        match = VERSION_PATTERN.search(source_path.read_text(encoding="utf-8"))
        if match is None:
            raise PreparationError(
                f"No se pudo comprobar la versión de {source.name} en {source.path}."
            )
        actual_version = match.group("version")
        if actual_version != source.version:
            raise PreparationError(
                f"Versión discordante para {source.name}: el manifiesto declara "
                f"{source.version} y la fuente contiene {actual_version}."
            )


def _resolve_manuscript_pdf(
    repository_root: Path,
    environ: Mapping[str, str] | None = None,
    home: Path | None = None,
) -> Path:
    """Resolve a user-provisioned manuscript mirror outside the checkout."""

    environment = os.environ if environ is None else environ
    override = environment.get(MANUSCRIPT_ENV)
    if override:
        candidate = Path(override).expanduser()
        location = f"la variable {MANUSCRIPT_ENV}"
    else:
        xdg_data_home = environment.get("XDG_DATA_HOME")
        if xdg_data_home:
            data_home = Path(xdg_data_home).expanduser()
        else:
            data_home = (Path.home() if home is None else home) / ".local" / "share"
        candidate = data_home / LOCAL_MANUSCRIPT_RELATIVE
        location = "la ubicación local estándar"

    repository = repository_root.resolve()
    resolved = candidate.resolve()
    if resolved == repository or repository in resolved.parents:
        raise PreparationError(
            "La copia local del manuscrito debe estar fuera del checkout Git; "
            f"ruta rechazada: {resolved}"
        )
    if not resolved.is_file():
        default_path = (
            (Path.home() if home is None else home)
            / ".local"
            / "share"
            / LOCAL_MANUSCRIPT_RELATIVE
        )
        raise PreparationError(
            f"No existe el manuscrito indicado por {location}: {resolved}. "
            "Aprovisiona manualmente una réplica del PDF autoritativo de Drive "
            f"fuera del checkout, preferentemente en {default_path}, o define "
            f"{MANUSCRIPT_ENV}. No se realizará ninguna descarga automática."
        )
    return resolved


def prepare() -> tuple[Path, ...]:
    script_path = Path(__file__).resolve()
    publication_root = script_path.parent.parent
    repository_root = publication_root.parent
    project_control = repository_root / "project" / "00_CONTROL" / "proyecto.yaml"

    if not project_control.is_file():
        raise PreparationError(
            "No existe project/00_CONTROL/proyecto.yaml en la raíz esperada "
            f"del repositorio: {repository_root}"
        )

    manifest_path = publication_root / "meta" / "publication.yml"
    sources = _manifest_sources(manifest_path)
    _validate_sources(repository_root, sources)
    manuscript_pdf = _resolve_manuscript_pdf(repository_root)
    outputs = build_vertical_prototype(
        repository_root,
        publication_root,
        manuscript_pdf,
    )
    print(
        "Preparación completada: 4 fuentes y versiones verificadas; "
        f"{len(outputs)} derivados del prototipo regenerados."
    )
    return outputs


def main() -> int:
    try:
        prepare()
    except (OSError, UnicodeError, PreparationError, PrototypeBuildError) as error:
        print(f"Error de preparación: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

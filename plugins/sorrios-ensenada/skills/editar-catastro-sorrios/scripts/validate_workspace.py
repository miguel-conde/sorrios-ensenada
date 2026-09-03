#!/usr/bin/env python3
import argparse
import hashlib
import sys
from pathlib import Path, PurePosixPath

import yaml

from path_utils import (
    PathValidationError,
    normalize_logical_path,
    normalize_root,
    physical_from_logical,
)


PROJECT_FILE = Path("00_CONTROL", "proyecto.yaml")
STATE_FILE = Path("00_CONTROL", "estado.yaml")
UNITS_FILE = Path("00_CONTROL", "unidades.yaml")
SOURCE_PDF = Path(
    "10_FUENTE_PRIMARIA",
    "sorrios_ensenada_orden_lectura_calidad_original.pdf",
)
EDITION_FILE = Path("20_TRABAJO_EDITORIAL", "Edicion_Critica.md")

REQUIRED = {
    PROJECT_FILE,
    STATE_FILE,
    UNITS_FILE,
    Path("00_CONTROL", "Manual_Editorial.md"),
    Path("00_CONTROL", "INSTRUCCIONES_PROYECTO.md"),
    Path("00_CONTROL", "CAMBIOS.md"),
    SOURCE_PDF,
    EDITION_FILE,
    Path("20_TRABAJO_EDITORIAL", "Diario_Editorial.md"),
    Path("20_TRABAJO_EDITORIAL", "Glosario.md"),
    Path("20_TRABAJO_EDITORIAL", "INDICES", "Indice_Personas.md"),
    Path("20_TRABAJO_EDITORIAL", "INDICES", "Indice_Toponimos.md"),
    Path("20_TRABAJO_EDITORIAL", "INDICES", "Indice_Instituciones.md"),
    Path("20_TRABAJO_EDITORIAL", "INDICES", "Indice_Medidas.md"),
    Path("20_TRABAJO_EDITORIAL", "INDICES", "Indice_Oficios.md"),
    Path("30_RESULTADOS", "ESTUDIO_HISTORICO", "Estudio_Historico.md"),
}

SECTIONS = [
    "### Imagen",
    "### Transcripción paleográfica",
    "### Observaciones editoriales",
    "### Notas paleográficas",
    "### Notas históricas",
    "### Referencias cruzadas",
]


def read_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"El YAML no contiene un objeto: {path}")
    return data


def display_path(path: Path) -> str:
    return PurePosixPath(*path.parts).as_posix()


def validate_workspace(root: Path, *, skip_pdf_hash: bool = False) -> list[str]:
    root = normalize_root(root)
    errors = [
        f"Falta {display_path(relative)}"
        for relative in sorted(REQUIRED, key=lambda item: item.parts)
        if not root.joinpath(relative).is_file()
    ]
    if errors:
        return errors

    project = read_yaml(root.joinpath(PROJECT_FILE))
    state = read_yaml(root.joinpath(STATE_FILE))
    data = read_yaml(root.joinpath(UNITS_FILE))

    rows = data.get("units", [])
    if data.get("unit_count") != 35 or len(rows) != 35:
        errors.append("unidades.yaml no contiene 35 unidades")
    if [unit.get("order") for unit in rows] != list(range(1, 36)):
        errors.append("Orden de unidades inválido")

    ids = [unit.get("id") for unit in rows]
    if len(ids) != len(set(ids)):
        errors.append("Hay unidades duplicadas")

    current = state.get("current_unit")
    if current not in ids:
        errors.append("La unidad actual no existe")
    else:
        unit = rows[ids.index(current)]
        location = state.get("current_location", {})
        if (
            location.get("pdf_page") != unit.get("pdf_page")
            or location.get("position") != unit.get("position")
        ):
            errors.append("La ubicación actual no coincide con unidades.yaml")

    if state.get("last_closed_unit") != state.get("last_validated_unit"):
        errors.append("La última unidad validada y cerrada no coincide")
    if state.get("operation", {}).get("status") not in {"clean", "verified"}:
        errors.append("Existe una operación incompleta")

    source = project.get("authorities", {}).get("manuscript", {})
    expected_logical_path = PurePosixPath(*SOURCE_PDF.parts)
    try:
        declared_logical_path = normalize_logical_path(source.get("path", ""))
    except PathValidationError as exc:
        errors.append(str(exc))
        declared_logical_path = expected_logical_path
    if declared_logical_path != expected_logical_path:
        errors.append("La ruta lógica del PDF autoritativo es incorrecta")

    pdf = physical_from_logical(root, expected_logical_path, strict=True)
    if pdf.stat().st_size != source.get("size_bytes"):
        errors.append("Tamaño del PDF incorrecto")
    if (
        not skip_pdf_hash
        and hashlib.sha256(pdf.read_bytes()).hexdigest() != source.get("sha256")
    ):
        errors.append("Hash del PDF incorrecto")

    edition = root.joinpath(EDITION_FILE).read_text(encoding="utf-8")
    for section in SECTIONS:
        if edition.count(section) != 35:
            errors.append(f"Sección {section}: se esperaban 35")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--skip-pdf-hash", action="store_true")
    args = parser.parse_args()

    try:
        errors = validate_workspace(args.root, skip_pdf_hash=args.skip_pdf_hash)
    except (OSError, TypeError, ValueError, yaml.YAMLError) as exc:
        print(f"ERROR: {exc}")
        return 2
    if errors:
        print("\n".join(errors))
        return 1
    print("VALID: workspace coherent")
    return 0


if __name__ == "__main__":
    sys.exit(main())

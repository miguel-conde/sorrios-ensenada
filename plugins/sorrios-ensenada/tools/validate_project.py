#!/usr/bin/env python3
"""Validate the GitHub-workspace v2 project without requiring the PDF locally."""

import argparse
import re
import sys
from pathlib import Path, PurePosixPath

import yaml

from path_utils import PathValidationError, normalize_logical_path, normalize_root


PROJECT_ROOT = Path("project")
PROJECT_FILE = PROJECT_ROOT / "00_CONTROL" / "proyecto.yaml"
STATE_FILE = PROJECT_ROOT / "00_CONTROL" / "estado.yaml"
UNITS_FILE = PROJECT_ROOT / "00_CONTROL" / "unidades.yaml"
EDITION_FILE = PROJECT_ROOT / "20_TRABAJO_EDITORIAL" / "Edicion_Critica.md"

REQUIRED = {
    Path("PROJECT.md"),
    PROJECT_FILE,
    STATE_FILE,
    UNITS_FILE,
    PROJECT_ROOT / "00_CONTROL" / "Manual_Editorial.md",
    PROJECT_ROOT / "00_CONTROL" / "CAMBIOS.md",
    PROJECT_ROOT / "00_CONTROL" / "OPERACIONES",
    EDITION_FILE,
    PROJECT_ROOT / "20_TRABAJO_EDITORIAL" / "Diario_Editorial.md",
    PROJECT_ROOT / "20_TRABAJO_EDITORIAL" / "Glosario.md",
    PROJECT_ROOT / "20_TRABAJO_EDITORIAL" / "INDICES" / "Indice_Personas.md",
    PROJECT_ROOT / "20_TRABAJO_EDITORIAL" / "INDICES" / "Indice_Toponimos.md",
    PROJECT_ROOT / "20_TRABAJO_EDITORIAL" / "INDICES" / "Indice_Instituciones.md",
    PROJECT_ROOT / "20_TRABAJO_EDITORIAL" / "INDICES" / "Indice_Medidas.md",
    PROJECT_ROOT / "20_TRABAJO_EDITORIAL" / "INDICES" / "Indice_Oficios.md",
    PROJECT_ROOT / "30_RESULTADOS" / "ESTUDIO_HISTORICO" / "Estudio_Historico.md",
    PROJECT_ROOT / "90_ARCHIVO",
}

SECTIONS = [
    "### Imagen",
    "### Transcripción paleográfica",
    "### Observaciones editoriales",
    "### Notas paleográficas",
    "### Notas históricas",
    "### Referencias cruzadas",
]

ALLOWED_POSITIONS = {"complete", "left", "right"}
ALLOWED_OPERATION_STATUS = {"clean", "prepared", "failed", "verified"}
ALLOWED_PHASES = {"edicion_paleografica", "estudio_historico"}
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def read_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"El YAML no contiene un objeto: {path}")
    return data


def display_path(path: Path) -> str:
    return PurePosixPath(*path.parts).as_posix()


def walk_dicts(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk_dicts(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_dicts(child)


def validate_declared_paths(repo_root: Path, project: dict) -> list[str]:
    errors: list[str] = []
    for item in walk_dicts(project):
        if item.get("provider") != "github" or "path" not in item:
            continue
        raw = item.get("path")
        try:
            logical = normalize_logical_path(raw)
        except (PathValidationError, TypeError) as exc:
            errors.append(str(exc))
            continue
        physical = repo_root.joinpath(*logical.parts)
        if not physical.exists():
            errors.append(f"Ruta GitHub declarada inexistente: {logical.as_posix()}")
    return errors


def validate_project(repo_root: Path) -> list[str]:
    repo_root = normalize_root(repo_root)
    errors: list[str] = []

    for relative in sorted(REQUIRED, key=lambda item: item.parts):
        target = repo_root.joinpath(relative)
        if relative.name in {"OPERACIONES", "90_ARCHIVO"}:
            if not target.is_dir():
                errors.append(f"Falta {display_path(relative)}/")
        elif not target.is_file():
            errors.append(f"Falta {display_path(relative)}")
    if errors:
        return errors

    project = read_yaml(repo_root / PROJECT_FILE)
    state = read_yaml(repo_root / STATE_FILE)
    units_data = read_yaml(repo_root / UNITS_FILE)

    if project.get("schema_version") != 2:
        errors.append("proyecto.yaml no usa schema_version 2")

    repository = project.get("repository", {})
    expected_repository = {
        "provider": "github",
        "full_name": "miguel-conde/sorrios-ensenada",
        "canonical_branch": "main",
        "project_root": "project",
    }
    for key, expected in expected_repository.items():
        if repository.get(key) != expected:
            errors.append(f"repository.{key} inválido")

    if project.get("plugin", {}).get("version") != "2.0.2":
        errors.append("Versión de plugin distinta de 2.0.2")
    if project.get("skill", {}).get("version") != "2.0.2":
        errors.append("Versión de skill distinta de 2.0.2")

    phase = project.get("phase", {})
    phase_current = phase.get("current")
    historical_enabled = phase.get("historical_study_enabled")
    historical_document = project.get("documents", {}).get("historical_study", {})

    if phase_current not in ALLOWED_PHASES:
        errors.append("Fase del proyecto inválida")
    if state.get("phase") != phase_current:
        errors.append("estado.yaml.phase no coincide con proyecto.yaml phase.current")

    if phase_current == "edicion_paleografica":
        if historical_enabled is not False:
            errors.append("El Estudio Histórico no puede estar habilitado durante edicion_paleografica")
        if historical_document.get("enabled") is not False:
            errors.append("documents.historical_study.enabled debe ser false durante edicion_paleografica")
    elif phase_current == "estudio_historico":
        if historical_enabled is not True:
            errors.append("historical_study_enabled debe ser true durante estudio_historico")
        if historical_document.get("enabled") is not True:
            errors.append("documents.historical_study.enabled debe ser true durante estudio_historico")

    manuscript = project.get("authorities", {}).get("manuscript", {})
    if manuscript.get("provider") != "google_drive":
        errors.append("El manuscrito no declara Google Drive como proveedor")
    if manuscript.get("access") != "read_only":
        errors.append("El manuscrito no declara acceso read_only")
    if not isinstance(manuscript.get("file_id"), str) or not manuscript.get("file_id"):
        errors.append("Falta file_id del PDF")
    if manuscript.get("name") != "sorrios_ensenada_orden_lectura_calidad_original.pdf":
        errors.append("Nombre del PDF autoritativo inválido")
    if not isinstance(manuscript.get("size_bytes"), int) or manuscript.get("size_bytes", 0) <= 0:
        errors.append("Tamaño del PDF inválido")
    if manuscript.get("pages") != 18:
        errors.append("Número de páginas del PDF distinto de 18")
    if not isinstance(manuscript.get("sha256"), str) or not SHA256_RE.fullmatch(manuscript.get("sha256", "")):
        errors.append("SHA-256 del PDF inválido")
    if "path" in manuscript:
        errors.append("El PDF de Drive no debe declarar una ruta dentro del workspace GitHub")

    google_drive_nodes = [
        item for item in walk_dicts(project) if item.get("provider") == "google_drive"
    ]
    if len(google_drive_nodes) != 1 or google_drive_nodes[0] is not manuscript:
        errors.append("Drive debe aparecer solo como proveedor del PDF autoritativo")

    for item in walk_dicts(project):
        if item is manuscript:
            continue
        if "file_id" in item:
            errors.append("Hay un file_id heredado de Drive fuera del manuscrito")
            break

    errors.extend(validate_declared_paths(repo_root, project))

    rows = units_data.get("units", [])
    if units_data.get("unit_count") != 35 or len(rows) != 35:
        errors.append("unidades.yaml no contiene 35 unidades")
    else:
        orders = [unit.get("order") for unit in rows]
        if orders != list(range(1, 36)):
            errors.append("Orden de unidades inválido")
        ids = [unit.get("id") for unit in rows]
        if len(ids) != len(set(ids)) or any(not isinstance(value, str) for value in ids):
            errors.append("IDs de unidad inválidos o duplicados")
        for index, unit in enumerate(rows):
            if unit.get("position") not in ALLOWED_POSITIONS:
                errors.append(f"Posición inválida en unidad {unit.get('id')}")
            page = unit.get("pdf_page")
            if not isinstance(page, int) or not 1 <= page <= manuscript.get("pages", 0):
                errors.append(f"Página inválida en unidad {unit.get('id')}")
            expected_previous = None if index == 0 else rows[index - 1].get("id")
            expected_next = None if index == len(rows) - 1 else rows[index + 1].get("id")
            if unit.get("previous") != expected_previous or unit.get("next") != expected_next:
                errors.append(f"Cadena previous/next inválida en unidad {unit.get('id')}")

        current = state.get("current_unit")
        if current is None:
            final_id = ids[-1]
            if state.get("last_closed_unit") != final_id or state.get("last_validated_unit") != final_id:
                errors.append("El estado terminal no cierra la última unidad")
            if state.get("next_unit") is not None:
                errors.append("El estado terminal no puede tener unidad siguiente")
            if state.get("current_location") is not None:
                errors.append("El estado terminal no puede tener ubicación actual")
            if state.get("pending_tasks") != []:
                errors.append("El estado terminal no puede tener tareas pendientes")
        elif current not in ids:
            errors.append("La unidad actual no existe")
        else:
            current_index = ids.index(current)
            unit = rows[ids.index(current)]
            location = state.get("current_location", {})
            if location.get("pdf_page") != unit.get("pdf_page") or location.get("position") != unit.get("position"):
                errors.append("La ubicación actual no coincide con unidades.yaml")
            expected_previous = None if current_index == 0 else ids[current_index - 1]
            expected_next = None if current_index == len(ids) - 1 else ids[current_index + 1]
            if state.get("last_closed_unit") != expected_previous or state.get("last_validated_unit") != expected_previous:
                errors.append("La última unidad cerrada no precede a la unidad actual")
            if state.get("next_unit") != expected_next:
                errors.append("La unidad siguiente no coincide con unidades.yaml")

        if phase_current == "estudio_historico":
            final_id = ids[-1]
            if state.get("last_closed_unit") != final_id or state.get("last_validated_unit") != final_id:
                errors.append("No puede activarse el Estudio Histórico antes de cerrar las 35 unidades")
            if state.get("current_unit") is not None or state.get("next_unit") is not None or state.get("current_location") is not None:
                errors.append("El Estudio Histórico exige estado terminal de la edición paleográfica")
            if state.get("open_issues") != []:
                errors.append("El Estudio Histórico no puede activarse con dudas abiertas")
            if state.get("pending_tasks") != []:
                errors.append("El Estudio Histórico no puede activarse con tareas pendientes")
            if state.get("operation", {}).get("status") != "clean":
                errors.append("El Estudio Histórico no puede activarse con una operación incompleta")

    if state.get("last_closed_unit") != state.get("last_validated_unit"):
        errors.append("La última unidad validada y cerrada no coincide")
    if state.get("operation", {}).get("status") not in ALLOWED_OPERATION_STATUS:
        errors.append("Estado de operación inválido")

    edition = (repo_root / EDITION_FILE).read_text(encoding="utf-8")
    for section in SECTIONS:
        if edition.count(section) != 35:
            errors.append(f"Sección {section}: se esperaban 35")

    if any(path.suffix.lower() == ".pdf" for path in (repo_root / PROJECT_ROOT).rglob("*")):
        errors.append("Hay un PDF cometido dentro de project/")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_root", type=Path)
    args = parser.parse_args()

    try:
        errors = validate_project(args.repo_root)
    except (OSError, TypeError, ValueError, yaml.YAMLError) as exc:
        print(f"ERROR: {exc}")
        return 2
    if errors:
        print("\n".join(errors))
        return 1
    print("VALID: GitHub workspace v2 coherent")
    return 0


if __name__ == "__main__":
    sys.exit(main())

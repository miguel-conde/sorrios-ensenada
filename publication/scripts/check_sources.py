#!/usr/bin/env python3
"""Validate publication inputs without generating or modifying any output."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

import yaml

from apparatus_sources import (
    ApparatusSourceError,
    git_blob_oid,
    load_evidence_register,
    load_glossary,
    validate_glossary_references,
)
from critical_edition import (
    CriticalEditionError,
    load_unit_specs,
    parse_critical_edition,
)
from modernized_edition import (
    ModernizedEditionError,
    load_modernized_edition,
    validate_concordance_units,
    validate_verified_questions,
)
from index_sources import (
    IndexSourceError,
    load_editorial_indexes,
    load_live_indexes,
    response_index_entries,
)


EXPECTED_SOURCE_COUNT = 5
EXPECTED_UNIT_COUNT = 35
MANUSCRIPT_ENV = "SORRIOS_MANUSCRIPT_PDF"
LOCAL_MANUSCRIPT_RELATIVE = Path("sorrios-ensenada") / "manuscript.pdf"
VERSION_PATTERN = re.compile(r"^\*\*Versión:\*\*\s*(?P<version>\S+)", re.MULTILINE)
EVIDENCE_PATTERN = re.compile(r"^\|\s*([A-Z]+-\d{3})\s*\|", re.MULTILINE)


class SourceCheckError(RuntimeError):
    """Report one actionable and deterministic source validation failure."""


@dataclass(frozen=True)
class Source:
    name: str
    path: str
    version: str | None = None
    git_blob: str | None = None


@dataclass(frozen=True)
class ManuscriptMetadata:
    file_id: str
    name: str
    sha256: str
    size_bytes: int
    pages: int


@dataclass(frozen=True)
class CheckedSources:
    manuscript_pdf: Path
    manuscript: ManuscriptMetadata
    sources: tuple[Source, ...]
    unit_count: int
    glossary_count: int = 0
    evidence_count: int = 0
    calculation_count: int = 0
    index_entry_counts: tuple[int, ...] = ()


def _read_yaml(path: Path) -> dict:
    if not path.is_file():
        raise SourceCheckError(f"No existe el archivo YAML requerido: {path}")
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        raise SourceCheckError(f"No se pudo leer YAML válido en {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise SourceCheckError(f"El archivo YAML debe contener un mapa: {path}")
    return data


def _safe_repository_path(repository_root: Path, logical_path: str, label: str) -> Path:
    relative = PurePosixPath(logical_path)
    if relative.is_absolute() or ".." in relative.parts:
        raise SourceCheckError(
            f"La ruta de {label} debe ser relativa y permanecer en el repositorio: "
            f"{logical_path}"
        )
    resolved = repository_root.joinpath(*relative.parts).resolve()
    repository = repository_root.resolve()
    if resolved == repository or repository not in resolved.parents:
        raise SourceCheckError(f"La ruta de {label} sale del repositorio: {logical_path}")
    return resolved


def _manifest_sources(manifest: dict) -> tuple[Source, ...]:
    raw_sources = manifest.get("sources")
    if not isinstance(raw_sources, dict) or len(raw_sources) != EXPECTED_SOURCE_COUNT:
        count = len(raw_sources) if isinstance(raw_sources, dict) else 0
        raise SourceCheckError(
            "publication/meta/publication.yml debe declarar exactamente "
            f"{EXPECTED_SOURCE_COUNT} fuentes; declara {count}."
        )
    sources: list[Source] = []
    for name, fields in raw_sources.items():
        if not isinstance(fields, dict) or not fields.get("path"):
            raise SourceCheckError(
                f"La fuente {name} debe declarar path en publication.yml."
            )
        version = fields.get("version")
        git_blob = fields.get("git_blob")
        if bool(version) == bool(git_blob):
            raise SourceCheckError(
                f"La fuente {name} debe declarar version o git_blob, pero no ambos."
            )
        if git_blob and not re.fullmatch(r"[0-9a-f]{40}", str(git_blob)):
            raise SourceCheckError(
                f"La fuente {name} declara un git_blob inválido: {git_blob}."
            )
        sources.append(
            Source(
                str(name),
                str(fields["path"]),
                str(version) if version else None,
                str(git_blob) if git_blob else None,
            )
        )
    return tuple(sources)


def _validate_source_versions(repository_root: Path, sources: tuple[Source, ...]) -> None:
    for source in sources:
        path = _safe_repository_path(repository_root, source.path, f"la fuente {source.name}")
        if not path.is_file():
            raise SourceCheckError(
                f"No existe la fuente {source.name} declarada en publication.yml: "
                f"{source.path}"
            )
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            raise SourceCheckError(f"No se pudo leer {source.path}: {exc}") from exc
        if source.version is not None:
            match = VERSION_PATTERN.search(text)
            if match is None:
                raise SourceCheckError(
                    f"No se pudo comprobar la versión de {source.name} en {source.path}."
                )
            actual = match.group("version")
            if actual != source.version:
                raise SourceCheckError(
                    f"Versión discordante para {source.name}: publication.yml declara "
                    f"{source.version} y {source.path} contiene {actual}."
                )
        else:
            if VERSION_PATTERN.search(text):
                raise SourceCheckError(
                    f"La fuente {source.name} tiene versión explícita pero publication.yml "
                    "la identifica solo mediante git_blob."
                )
            actual_blob = git_blob_oid(path.read_bytes())
            if actual_blob != source.git_blob:
                raise SourceCheckError(
                    f"Snapshot Git discordante para {source.name}: publication.yml declara "
                    f"{source.git_blob} y {source.path} produce {actual_blob}."
                )


def _manuscript_metadata(project: dict, publication: dict) -> ManuscriptMetadata:
    project_manuscript = project.get("authorities", {}).get("manuscript")
    publication_manuscript = publication.get("manuscript")
    if not isinstance(project_manuscript, dict):
        raise SourceCheckError("proyecto.yaml no declara authorities.manuscript.")
    if not isinstance(publication_manuscript, dict):
        raise SourceCheckError("publication.yml no declara manuscript.")
    required = ("file_id", "name", "sha256", "size_bytes", "pages")
    missing = [key for key in required if key not in project_manuscript]
    if missing:
        raise SourceCheckError(
            "Faltan metadatos del manuscrito en proyecto.yaml: " + ", ".join(missing)
        )
    mismatches = [
        key
        for key in required
        if publication_manuscript.get(key) != project_manuscript.get(key)
    ]
    metadata_source = publication_manuscript.get("metadata_source")
    if metadata_source != "project/00_CONTROL/proyecto.yaml":
        mismatches.append("metadata_source")
    if mismatches:
        raise SourceCheckError(
            "Los metadatos del manuscrito en publication.yml no coinciden con "
            "proyecto.yaml: " + ", ".join(mismatches)
        )
    try:
        return ManuscriptMetadata(
            file_id=str(project_manuscript["file_id"]),
            name=str(project_manuscript["name"]),
            sha256=str(project_manuscript["sha256"]),
            size_bytes=int(project_manuscript["size_bytes"]),
            pages=int(project_manuscript["pages"]),
        )
    except (TypeError, ValueError) as exc:
        raise SourceCheckError("Los metadatos numéricos del manuscrito no son válidos.") from exc


def resolve_manuscript_pdf(
    repository_root: Path,
    environ: Mapping[str, str] | None = None,
    home: Path | None = None,
) -> Path:
    """Resolve the user-provisioned manuscript mirror outside the checkout."""

    environment = os.environ if environ is None else environ
    override = environment.get(MANUSCRIPT_ENV)
    if override:
        candidate = Path(override).expanduser()
        location = f"la variable {MANUSCRIPT_ENV}"
    else:
        xdg_data_home = environment.get("XDG_DATA_HOME")
        data_home = (
            Path(xdg_data_home).expanduser()
            if xdg_data_home
            else (Path.home() if home is None else home) / ".local" / "share"
        )
        candidate = data_home / LOCAL_MANUSCRIPT_RELATIVE
        location = "la ubicación local estándar"

    repository = repository_root.resolve()
    resolved = candidate.resolve()
    if resolved == repository or repository in resolved.parents:
        raise SourceCheckError(
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
        raise SourceCheckError(
            f"No existe el manuscrito indicado por {location}: {resolved}. "
            "Aprovisiona manualmente una réplica del PDF autoritativo de Drive "
            f"fuera del checkout, preferentemente en {default_path}, o define "
            f"{MANUSCRIPT_ENV}. No se realizará ninguna descarga automática."
        )
    return resolved


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    try:
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
    except OSError as exc:
        raise SourceCheckError(f"No se pudo leer el manuscrito local {path}: {exc}") from exc
    return digest.hexdigest()


def _pdf_pages(pdf: Path) -> int:
    executable = shutil.which("pdfinfo")
    if executable is None:
        raise SourceCheckError(
            "No se encontró pdfinfo en PATH; instala Poppler para validar el manuscrito."
        )
    try:
        result = subprocess.run(
            [executable, pdf], check=True, capture_output=True, text=True, shell=False
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise SourceCheckError(f"pdfinfo no pudo leer el manuscrito {pdf}: {exc}") from exc
    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, re.MULTILINE)
    if match is None:
        raise SourceCheckError("pdfinfo no devolvió el número de páginas del manuscrito.")
    return int(match.group(1))


def verify_local_manuscript(pdf: Path, metadata: ManuscriptMetadata) -> None:
    size = pdf.stat().st_size
    if size != metadata.size_bytes:
        raise SourceCheckError(
            f"Tamaño incorrecto del manuscrito local: {size}; esperado "
            f"{metadata.size_bytes} según proyecto.yaml."
        )
    digest = _sha256(pdf)
    if digest != metadata.sha256:
        raise SourceCheckError(
            f"SHA-256 incorrecto del manuscrito local: {digest}; esperado "
            f"{metadata.sha256}. No uses una copia recompuesta ni el PDF 0.6."
        )
    pages = _pdf_pages(pdf)
    if pages != metadata.pages:
        raise SourceCheckError(
            f"Número de páginas incorrecto del manuscrito local: {pages}; esperado "
            f"{metadata.pages}."
        )


def _validate_units(repository_root: Path, manuscript_pages: int) -> int:
    path = repository_root / "project" / "00_CONTROL" / "unidades.yaml"
    data = _read_yaml(path)
    units = data.get("units")
    if data.get("unit_count") != EXPECTED_UNIT_COUNT or not isinstance(units, list):
        raise SourceCheckError(
            "unidades.yaml debe declarar unit_count: 35 y una lista units."
        )
    if len(units) != EXPECTED_UNIT_COUNT:
        raise SourceCheckError(
            f"unidades.yaml contiene {len(units)} unidades; se esperaban 35."
        )
    identifiers = [unit.get("id") for unit in units if isinstance(unit, dict)]
    orders = [unit.get("order") for unit in units if isinstance(unit, dict)]
    if len(identifiers) != EXPECTED_UNIT_COUNT or len(set(identifiers)) != EXPECTED_UNIT_COUNT:
        raise SourceCheckError("Los 35 identificadores de unidades deben existir y ser únicos.")
    if orders != list(range(1, EXPECTED_UNIT_COUNT + 1)):
        raise SourceCheckError("Las unidades deben conservar el orden canónico consecutivo 1–35.")
    for index, unit in enumerate(units):
        page = unit.get("pdf_page")
        position = unit.get("position")
        expected_previous = identifiers[index - 1] if index else None
        expected_next = identifiers[index + 1] if index + 1 < len(units) else None
        if not isinstance(page, int) or not 1 <= page <= manuscript_pages:
            raise SourceCheckError(
                f"La unidad {unit.get('id')} declara una página PDF inválida: {page}."
            )
        if position not in {"left", "right", "complete"}:
            raise SourceCheckError(
                f"La unidad {unit.get('id')} declara una posición inválida: {position}."
            )
        if unit.get("previous") != expected_previous or unit.get("next") != expected_next:
            raise SourceCheckError(
                f"La cadena previous/next se rompe en la unidad {unit.get('id')}."
            )
    return len(units)


def _validate_critical_edition(
    repository_root: Path, manuscript: ManuscriptMetadata
) -> None:
    """Require an exact 35-unit match before Phase 4B generation."""

    units_path = repository_root / "project" / "00_CONTROL" / "unidades.yaml"
    edition_path = (
        repository_root
        / "project"
        / "20_TRABAJO_EDITORIAL"
        / "Edicion_Critica.md"
    )
    try:
        specs = load_unit_specs(units_path)
        text = edition_path.read_text(encoding="utf-8")
        parse_critical_edition(text, specs, manuscript.name)
    except (OSError, UnicodeError, CriticalEditionError) as exc:
        raise SourceCheckError(f"Edición crítica no apta para 4B: {exc}") from exc


def _validate_modernized_edition(repository_root: Path) -> None:
    """Require the complete 1.3 source contract before Phase 4C generation."""

    source_root = (
        repository_root
        / "project"
        / "30_RESULTADOS"
        / "EDICION_DIVULGATIVA"
    )
    try:
        edition = load_modernized_edition(
            source_root / "Catastro_Sorrios_1752_Version_Modernizada.md"
        )
        specs = load_unit_specs(
            repository_root / "project" / "00_CONTROL" / "unidades.yaml"
        )
        validate_concordance_units(edition, tuple(spec.label for spec in specs))
        validate_verified_questions(
            edition,
            (source_root / "Introduccion_Catastro_Ensenada_Sorrios.md").read_text(
                encoding="utf-8"
            ),
            (source_root / "Verificacion_Interrogatorio_40_Preguntas.md").read_text(
                encoding="utf-8"
            ),
        )
    except (OSError, UnicodeError, CriticalEditionError, ModernizedEditionError) as exc:
        raise SourceCheckError(f"Edición modernizada no apta para 4C: {exc}") from exc


def _validate_apparatus_sources(repository_root: Path) -> tuple[int, int, int]:
    """Validate the glossary, register and cross-document prerequisites for 4D."""

    try:
        glossary = load_glossary(
            repository_root / "project" / "20_TRABAJO_EDITORIAL" / "Glosario.md"
        )
        if glossary.version is not None:
            raise ApparatusSourceError(
                "Glosario.md no debe recibir una versión inventada en publicación."
            )
        register = load_evidence_register(
            repository_root
            / "project"
            / "30_RESULTADOS"
            / "ESTUDIO_HISTORICO"
            / "Registro_Afirmaciones_Calculos_v1.md"
        )
        specs = load_unit_specs(
            repository_root / "project" / "00_CONTROL" / "unidades.yaml"
        )
        validate_glossary_references(
            glossary,
            tuple(spec.label for spec in specs),
            source="project/20_TRABAJO_EDITORIAL/Glosario.md",
        )
        modernized = load_modernized_edition(
            repository_root
            / "project"
            / "30_RESULTADOS"
            / "EDICION_DIVULGATIVA"
            / "Catastro_Sorrios_1752_Version_Modernizada.md"
        )
        validate_concordance_units(modernized, tuple(spec.label for spec in specs))
        response_units = {
            label
            for response in modernized.responses
            for label in re.findall(r"Folio \d{3}[rv]", response.folios)
        }
        unknown = sorted(response_units - {spec.label for spec in specs})
        if unknown:
            raise ApparatusSourceError(
                "La modernizada remite a unidades desconocidas: " + ", ".join(unknown)
            )
    except (OSError, UnicodeError, CriticalEditionError, ModernizedEditionError, ApparatusSourceError) as exc:
        raise SourceCheckError(f"Fuentes no aptas para 4D: {exc}") from exc
    return len(glossary.entries), len(register.entries), len(register.calculations)


def _validate_index_sources(
    repository_root: Path, publication_root: Path
) -> tuple[int, ...]:
    """Validate the five live indexes, indexes.yml and the derived response index."""

    try:
        specs = load_unit_specs(
            repository_root / "project" / "00_CONTROL" / "unidades.yaml"
        )
        live = load_live_indexes(repository_root, specs)
        modernized = load_modernized_edition(
            repository_root
            / "project"
            / "30_RESULTADOS"
            / "EDICION_DIVULGATIVA"
            / "Catastro_Sorrios_1752_Version_Modernizada.md"
        )
        editorial = load_editorial_indexes(
            publication_root,
            specs=specs,
            modernized=modernized,
        )
        responses = response_index_entries(modernized)
    except (CriticalEditionError, ModernizedEditionError, IndexSourceError) as exc:
        raise SourceCheckError(f"Fuentes no aptas para 5A: {exc}") from exc
    live_counts = tuple(len(index.entries) for index in live)
    editorial_counts = {index.index_id: len(index.entries) for index in editorial}
    return (
        *live_counts,
        editorial_counts["productos-recursos"],
        editorial_counts["cargas-fiscalidad"],
        len(responses),
        editorial_counts["materias"],
    )


def _validate_chapters(publication_root: Path, repository_root: Path) -> None:
    data = _read_yaml(publication_root / "meta" / "chapters.yml")
    chapters = data.get("chapters")
    if not isinstance(chapters, list) or not chapters:
        raise SourceCheckError("meta/chapters.yml debe declarar una lista de capítulos.")
    ids: list[str] = []
    paths: list[str] = []
    for chapter in chapters:
        if not isinstance(chapter, dict) or not chapter.get("chapter_id") or not chapter.get("path"):
            raise SourceCheckError("Cada entrada de chapters.yml debe declarar chapter_id y path.")
        chapter_id = str(chapter["chapter_id"])
        logical_path = str(chapter["path"])
        ids.append(chapter_id)
        paths.append(logical_path)
        path = _safe_repository_path(
            repository_root, f"publication/{logical_path}", f"el capítulo {chapter_id}"
        )
        if not chapter.get("generated") and not path.is_file():
            raise SourceCheckError(
                f"No existe el capítulo no generado {chapter_id}: publication/{logical_path}"
            )
    if len(ids) != len(set(ids)):
        raise SourceCheckError("Los chapter_id de chapters.yml deben ser únicos.")
    if len(paths) != len(set(paths)):
        raise SourceCheckError("Las rutas de chapters.yml deben ser únicas.")


def _validate_evidence_ids(publication_root: Path, repository_root: Path) -> None:
    register_path = (
        repository_root
        / "project"
        / "30_RESULTADOS"
        / "ESTUDIO_HISTORICO"
        / "Registro_Afirmaciones_Calculos_v1.md"
    )
    registered = set(EVIDENCE_PATTERN.findall(register_path.read_text(encoding="utf-8")))
    referenced: set[str] = set()
    for path in sorted((publication_root / "content").rglob("*.qmd")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        closing = text.find("\n---\n", 4)
        if closing < 0:
            raise SourceCheckError(f"Front matter incompleto en {path}.")
        metadata = yaml.safe_load(text[4:closing])
        if not isinstance(metadata, dict):
            raise SourceCheckError(f"Front matter inválido en {path}.")
        evidence = metadata.get("evidence", {})
        if isinstance(evidence, dict):
            for values in evidence.values():
                if isinstance(values, list):
                    referenced.update(str(value) for value in values)
    missing = sorted(referenced - registered)
    if missing:
        raise SourceCheckError(
            "Identificadores de evidencia inexistentes en el Registro: "
            + ", ".join(missing)
        )


def _validate_assets(publication_root: Path, manuscript: ManuscriptMetadata) -> None:
    data = _read_yaml(publication_root / "meta" / "assets.yml")
    assets = data.get("assets")
    if not isinstance(assets, list) or not assets:
        raise SourceCheckError("meta/assets.yml debe declarar una lista assets.")
    identifiers = [asset.get("asset_id") for asset in assets if isinstance(asset, dict)]
    if len(identifiers) != len(assets) or len(identifiers) != len(set(identifiers)):
        raise SourceCheckError("Los asset_id deben existir y ser únicos.")
    for asset in assets:
        source = asset.get("source", {})
        for key in ("file_id", "name", "sha256"):
            if source.get(key) != getattr(manuscript, key):
                raise SourceCheckError(
                    f"El activo {asset.get('asset_id')} no conserva {key} del manuscrito."
                )
        if asset.get("versioned") is not False:
            raise SourceCheckError(
                f"El activo {asset.get('asset_id')} debe seguir marcado como no versionado."
            )
        destination = asset.get("destination") or asset.get("destination_pattern")
        if not isinstance(destination, str) or not destination.startswith("generated/"):
            raise SourceCheckError(
                f"El destino de {asset.get('asset_id')} debe permanecer bajo generated/."
            )


def check_sources(
    repository_root: Path,
    publication_root: Path,
    *,
    environ: Mapping[str, str] | None = None,
    home: Path | None = None,
) -> CheckedSources:
    """Validate every implemented Phase 4 input and return the verified manuscript."""

    repository_root = repository_root.resolve()
    publication_root = publication_root.resolve()
    project = _read_yaml(repository_root / "project" / "00_CONTROL" / "proyecto.yaml")
    publication = _read_yaml(publication_root / "meta" / "publication.yml")
    sources = _manifest_sources(publication)
    _validate_source_versions(repository_root, sources)
    manuscript = _manuscript_metadata(project, publication)
    manuscript_pdf = resolve_manuscript_pdf(repository_root, environ, home)
    verify_local_manuscript(manuscript_pdf, manuscript)
    unit_count = _validate_units(repository_root, manuscript.pages)
    _validate_critical_edition(repository_root, manuscript)
    _validate_modernized_edition(repository_root)
    glossary_count, evidence_count, calculation_count = _validate_apparatus_sources(
        repository_root
    )
    _validate_chapters(publication_root, repository_root)
    _validate_evidence_ids(publication_root, repository_root)
    _validate_assets(publication_root, manuscript)
    index_entry_counts = _validate_index_sources(repository_root, publication_root)
    return CheckedSources(
        manuscript_pdf,
        manuscript,
        sources,
        unit_count,
        glossary_count,
        evidence_count,
        calculation_count,
        index_entry_counts,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Valida las fuentes de la publicación sin generar salidas."
    )
    parser.parse_args(argv)
    publication_root = Path(__file__).resolve().parent.parent
    repository_root = publication_root.parent
    try:
        checked = check_sources(repository_root, publication_root)
    except (
        OSError,
        UnicodeError,
        SourceCheckError,
        IndexSourceError,
        yaml.YAMLError,
    ) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(
        "PASS: "
        f"{len(checked.sources)} fuentes declaradas, {checked.unit_count} unidades, "
        "40 preguntas/respuestas modernizadas, "
        f"{checked.glossary_count} entradas de glosario, "
        f"{checked.evidence_count} entradas D/C/I/E/L y "
        f"{checked.calculation_count} cálculos; nueve índices 5A con entradas "
        f"{'/'.join(map(str, checked.index_entry_counts))}; "
        f"manuscrito {checked.manuscript.name} verificado en "
        f"{checked.manuscript_pdf} ({checked.manuscript.pages} páginas; "
        f"SHA-256 {checked.manuscript.sha256})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

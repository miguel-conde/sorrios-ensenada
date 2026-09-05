"""Portable handling for physical and persisted logical paths."""

from pathlib import Path, PurePosixPath, PureWindowsPath


class PathValidationError(ValueError):
    """Raised when a path is invalid for the requested scope."""


def normalize_physical_path(path: Path, *, strict: bool = False) -> Path:
    """Normalize a physical filesystem path on the current platform."""
    return path.expanduser().resolve(strict=strict)


def normalize_root(root: Path) -> Path:
    """Normalize and validate a physical directory root."""
    normalized = normalize_physical_path(root, strict=True)
    if not normalized.is_dir():
        raise PathValidationError(f"No es un directorio: {normalized}")
    return normalized


def ensure_within_root(path: Path, root: Path, *, strict: bool = False) -> Path:
    """Normalize a physical path and ensure that it belongs to a root."""
    normalized_root = normalize_root(root)
    normalized_path = normalize_physical_path(path, strict=strict)
    try:
        normalized_path.relative_to(normalized_root)
    except ValueError as exc:
        raise PathValidationError(
            f"La ruta queda fuera de la raíz: {normalized_path}"
        ) from exc
    return normalized_path


def normalize_logical_path(value: str | PurePosixPath) -> PurePosixPath:
    """Normalize a persisted relative path to canonical POSIX form.

    Persisted YAML paths are logical identifiers rather than physical paths. Existing
    backslash-separated values remain accepted for compatibility, but the returned
    value always uses POSIX semantics.
    """
    raw = str(value)
    windows_path = PureWindowsPath(raw)
    logical_path = PurePosixPath(raw.replace("\\", "/"))

    if logical_path.is_absolute() or windows_path.is_absolute() or windows_path.drive:
        raise PathValidationError(f"La ruta lógica debe ser relativa: {raw}")
    if not logical_path.parts or ".." in logical_path.parts:
        raise PathValidationError(f"Ruta lógica inválida: {raw}")
    return logical_path


def logical_from_physical(path: Path, root: Path) -> PurePosixPath:
    """Return the canonical logical path for an existing physical path."""
    normalized_root = normalize_root(root)
    normalized_path = ensure_within_root(path, normalized_root, strict=True)
    relative = normalized_path.relative_to(normalized_root)
    return PurePosixPath(*relative.parts)


def physical_from_logical(
    root: Path, value: str | PurePosixPath, *, strict: bool = False
) -> Path:
    """Map a persisted logical path to a physical path below a root."""
    normalized_root = normalize_root(root)
    logical_path = normalize_logical_path(value)
    physical_path = normalized_root.joinpath(*logical_path.parts)
    return ensure_within_root(physical_path, normalized_root, strict=strict)

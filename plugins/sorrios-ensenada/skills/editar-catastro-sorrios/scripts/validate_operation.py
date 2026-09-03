#!/usr/bin/env python3
import argparse
import hashlib
import json
import sys
from pathlib import Path, PurePosixPath

import yaml

from path_utils import (
    PathValidationError,
    logical_from_physical,
    normalize_logical_path,
    normalize_physical_path,
    normalize_root,
)


STATE_FILE = Path("00_CONTROL", "estado.yaml")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tree(root: Path) -> dict[PurePosixPath, str]:
    root = normalize_root(root)
    result: dict[PurePosixPath, str] = {}
    for path in root.rglob("*"):
        if path.is_file():
            logical_path = logical_from_physical(path, root)
            result[logical_path] = digest(path)
    return result


def read_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"El YAML no contiene un objeto: {path}")
    return data


def validate_operation(
    before: Path, after: Path, operation: Path
) -> tuple[dict[str, object], list[str]]:
    before = normalize_root(before)
    after = normalize_root(after)
    operation = normalize_physical_path(operation, strict=True)

    operation_data = read_yaml(operation)
    allowed: set[PurePosixPath] = set()
    errors: list[str] = []
    for value in operation_data.get("allowed_changes", []):
        if not isinstance(value, str):
            errors.append("allowed_changes contiene un valor que no es texto")
            continue
        try:
            allowed.add(normalize_logical_path(value))
        except PathValidationError as exc:
            errors.append(str(exc))

    before_tree = tree(before)
    after_tree = tree(after)
    changed = {
        path
        for path in before_tree.keys() | after_tree.keys()
        if before_tree.get(path) != after_tree.get(path)
    }
    unexpected = sorted(changed - allowed, key=lambda item: item.parts)
    if unexpected:
        errors.append(
            "Cambios no previstos: "
            + ", ".join(path.as_posix() for path in unexpected)
        )

    state = read_yaml(after.joinpath(STATE_FILE))
    if state.get("operation", {}).get("status") not in {"clean", "verified"}:
        errors.append("El estado final conserva una operación abierta")

    result = {
        "changed": [
            path.as_posix() for path in sorted(changed, key=lambda item: item.parts)
        ],
        "status": "VALID" if not errors else "INVALID",
    }
    return result, errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("before", type=Path)
    parser.add_argument("after", type=Path)
    parser.add_argument("operation", type=Path)
    args = parser.parse_args()

    try:
        result, errors = validate_operation(args.before, args.after, args.operation)
    except (OSError, TypeError, ValueError, yaml.YAMLError) as exc:
        print(f"ERROR: {exc}")
        return 2
    if errors:
        print("\n".join(errors))
        return 1
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

from pathlib import Path

import yaml

from validate_operation import validate_operation


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_state(root: Path, status: str = "verified") -> None:
    path = root.joinpath("00_CONTROL", "estado.yaml")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump({"operation": {"status": status}}),
        encoding="utf-8",
    )


def write_operation(path: Path, allowed_changes: list[str]) -> None:
    path.write_text(
        yaml.safe_dump({"allowed_changes": allowed_changes}),
        encoding="utf-8",
    )


def test_expected_change_is_portable_across_separators(tmp_path):
    before = tmp_path.joinpath("before")
    after = tmp_path.joinpath("after")
    before.mkdir()
    after.mkdir()
    write_state(before)
    write_state(after)
    write(before.joinpath("content", "entry.txt"), "before")
    write(after.joinpath("content", "entry.txt"), "after")
    operation = tmp_path.joinpath("operation.yaml")
    write_operation(operation, [r"content\entry.txt"])

    result, errors = validate_operation(before, after, operation)

    assert errors == []
    assert result == {"changed": ["content/entry.txt"], "status": "VALID"}


def test_unexpected_change_is_reported_in_posix_form(tmp_path):
    before = tmp_path.joinpath("before")
    after = tmp_path.joinpath("after")
    before.mkdir()
    after.mkdir()
    write_state(before)
    write_state(after)
    write(before.joinpath("content", "entry.txt"), "before")
    write(after.joinpath("content", "entry.txt"), "after")
    operation = tmp_path.joinpath("operation.yaml")
    write_operation(operation, [])

    result, errors = validate_operation(before, after, operation)

    assert result["status"] == "INVALID"
    assert errors == ["Cambios no previstos: content/entry.txt"]


def test_open_operation_is_rejected(tmp_path):
    before = tmp_path.joinpath("before")
    after = tmp_path.joinpath("after")
    before.mkdir()
    after.mkdir()
    write_state(before, "clean")
    write_state(after, "prepared")
    operation = tmp_path.joinpath("operation.yaml")
    write_operation(operation, ["00_CONTROL/estado.yaml"])

    result, errors = validate_operation(before, after, operation)

    assert result["changed"] == ["00_CONTROL/estado.yaml"]
    assert errors == ["El estado final conserva una operación abierta"]

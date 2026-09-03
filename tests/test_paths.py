from pathlib import Path, PurePosixPath

import pytest

from path_utils import (
    PathValidationError,
    logical_from_physical,
    normalize_logical_path,
    normalize_physical_path,
    physical_from_logical,
)


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("00_CONTROL/estado.yaml", PurePosixPath("00_CONTROL/estado.yaml")),
        (r"00_CONTROL\estado.yaml", PurePosixPath("00_CONTROL/estado.yaml")),
        (
            r"20_TRABAJO_EDITORIAL\INDICES/Indice_Personas.md",
            PurePosixPath(
                "20_TRABAJO_EDITORIAL/INDICES/Indice_Personas.md"
            ),
        ),
    ],
)
def test_logical_paths_are_normalized_to_posix(value, expected):
    assert normalize_logical_path(value) == expected


@pytest.mark.parametrize(
    "value",
    [
        "/etc/passwd",
        r"C:\Users\example\file.txt",
        "../outside.txt",
        "",
    ],
)
def test_logical_paths_must_be_relative_and_contained(value):
    with pytest.raises(PathValidationError):
        normalize_logical_path(value)


def test_physical_paths_are_resolved_and_mapped_to_logical_paths(tmp_path):
    root = tmp_path.joinpath("carpeta con espacio", "Sorríos")
    physical = root.joinpath("00_CONTROL", "estado.yaml")
    physical.parent.mkdir(parents=True)
    physical.write_text("status: clean", encoding="utf-8")

    assert normalize_physical_path(root, strict=True) == root.resolve()
    assert logical_from_physical(physical, root) == PurePosixPath(
        "00_CONTROL/estado.yaml"
    )
    assert physical_from_logical(
        root, "00_CONTROL/estado.yaml", strict=True
    ) == physical.resolve()


def test_logical_path_cannot_escape_physical_root(tmp_path):
    root = tmp_path.joinpath("root")
    root.mkdir()

    with pytest.raises(PathValidationError):
        physical_from_logical(root, "../outside.txt")

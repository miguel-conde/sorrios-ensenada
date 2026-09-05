from pathlib import Path

from validate_project import validate_project


ROOT = Path(__file__).resolve().parents[1]


def test_repository_project_passes_logical_validator():
    assert validate_project(ROOT) == []

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_project_bootstrap_targets_github_workspace_and_shared_method():
    text = (ROOT / "PROJECT.md").read_text(encoding="utf-8")
    assert "miguel-conde/sorrios-ensenada" in text
    assert "project/00_CONTROL/proyecto.yaml" in text
    assert "project/00_CONTROL/estado.yaml" in text
    assert "references/task-modes.md" in text
    assert "project/" in text
    assert "Google Drive" in text and "PDF" in text
    assert "No presupone Work" in text


def test_bootstrap_does_not_duplicate_editorial_method():
    text = (ROOT / "PROJECT.md").read_text(encoding="utf-8")
    assert "Transcripción paleográfica" not in text
    assert "Abreviaturas" not in text

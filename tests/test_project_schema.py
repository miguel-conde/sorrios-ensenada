from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def test_schema_2_has_github_paths_and_pdf_metadata():
    project = yaml.safe_load((ROOT / "project" / "00_CONTROL" / "proyecto.yaml").read_text(encoding="utf-8"))
    assert project["schema_version"] == 2
    assert project["repository"] == {
        "provider": "github",
        "full_name": "miguel-conde/sorrios-ensenada",
        "canonical_branch": "main",
        "project_root": "project",
    }
    assert project["phase"] == {
        "current": "estudio_historico",
        "historical_study_enabled": True,
    }
    assert project["documents"]["historical_study"]["enabled"] is True
    manuscript = project["authorities"]["manuscript"]
    assert manuscript["provider"] == "google_drive"
    assert manuscript["access"] == "read_only"
    assert manuscript["file_id"] == "1GgBs68iTi53ue8-TbrYFABALxadhQe5u"
    assert manuscript["size_bytes"] == 5038575
    assert manuscript["pages"] == 18
    assert manuscript["sha256"] == "d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24"
    assert "path" not in manuscript

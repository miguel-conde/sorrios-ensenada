from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "plugins" / "sorrios-ensenada" / "skills" / "editar-catastro-sorrios"


def walk_dicts(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk_dicts(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_dicts(child)


def test_drive_is_only_the_manuscript_provider():
    project = yaml.safe_load((ROOT / "project" / "00_CONTROL" / "proyecto.yaml").read_text(encoding="utf-8"))
    assert project["repository"]["provider"] == "github"
    assert "drive_root_id" not in project
    drive_nodes = [item for item in walk_dicts(project) if item.get("provider") == "google_drive"]
    assert drive_nodes == [project["authorities"]["manuscript"]]
    assert project["authorities"]["manuscript"]["access"] == "read_only"


def test_legacy_drive_runtime_is_absent_from_active_skill():
    assert not (SKILL_ROOT / "references" / "drive-materialization.md").exists()
    assert not (SKILL_ROOT / "references" / "local-execution.md").exists()
    assert not (SKILL_ROOT / "scripts").exists()
    active_text = "\n".join(path.read_text(encoding="utf-8") for path in [SKILL_ROOT / "SKILL.md", *sorted((SKILL_ROOT / "references").glob("*.md"))])
    assert "materialize_drive_payload.py" not in active_text
    assert "materialize_drive_text.py" not in active_text

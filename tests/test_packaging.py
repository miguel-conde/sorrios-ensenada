from pathlib import Path
import json
import re
import shutil

import yaml


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugins" / "sorrios-ensenada"


def test_isolated_plugin_is_self_contained(tmp_path):
    isolated = tmp_path / "sorrios-ensenada"
    shutil.copytree(PLUGIN_ROOT, isolated)

    plugin = json.loads((isolated / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    skill_root = isolated / "skills" / "editar-catastro-sorrios"
    skill_text = (skill_root / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = yaml.safe_load(skill_text.split("---", 2)[1])

    assert plugin["version"] == "2.0.0"
    assert frontmatter["name"] == "editar-catastro-sorrios"
    assert not (isolated / "PROJECT.md").exists()

    expected_references = {
        "task-modes.md",
        "workspace-contract.md",
        "editorial-procedure.md",
        "document-schemas.md",
        "github-operations.md",
        "pdf-access.md",
    }
    assert {path.name for path in (skill_root / "references").glob("*.md")} == expected_references
    assert (skill_root / "assets" / "templates" / "proyecto.yaml").is_file()

    targets = re.findall(r"\[[^\]]+\]\(([^)]+)\)", skill_text)
    for target in targets:
        assert not target.startswith("/")
        assert (skill_root / target).resolve().is_file()

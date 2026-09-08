import ast
import json
from pathlib import Path, PurePosixPath, PureWindowsPath
try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10
    import tomli as tomllib

import yaml


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugins" / "sorrios-ensenada"
SKILL_ROOT = PLUGIN_ROOT / "skills" / "editar-catastro-sorrios"


def test_plugin_and_marketplace_identifiers_match():
    plugin = json.loads((PLUGIN_ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    marketplace = json.loads((ROOT / ".agents" / "plugins" / "marketplace.json").read_text(encoding="utf-8"))
    entry = marketplace["plugins"][0]

    assert plugin["name"] == PLUGIN_ROOT.name == entry["name"]
    assert plugin["skills"] == "./skills/"
    assert plugin["interface"]["capabilities"] == ["Write"]
    assert "GitHub" in plugin["interface"]["longDescription"]
    assert entry["source"]["path"] == "./plugins/sorrios-ensenada"
    install_source = ROOT.joinpath(*PurePosixPath(entry["source"]["path"]).parts).resolve()
    assert install_source == PLUGIN_ROOT.resolve()


def test_plugin_contains_exactly_one_valid_skill():
    skills = [path.parent for path in PLUGIN_ROOT.joinpath("skills").glob("*/SKILL.md")]
    assert skills == [SKILL_ROOT]
    text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = yaml.safe_load(text.split("---", 2)[1])
    assert frontmatter["name"] == SKILL_ROOT.name


def test_versions_and_project_template_are_synchronized():
    plugin = json.loads((PLUGIN_ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    pyproject = tomllib.loads((PLUGIN_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    project = yaml.safe_load((ROOT / "project" / "00_CONTROL" / "proyecto.yaml").read_text(encoding="utf-8"))
    template = yaml.safe_load((SKILL_ROOT / "assets" / "templates" / "proyecto.yaml").read_text(encoding="utf-8"))

    versions = {
        plugin["version"],
        pyproject["project"]["version"],
        project["plugin"]["version"],
        project["skill"]["version"],
        template["plugin"]["version"],
        template["skill"]["version"],
    }
    assert len(versions) == 1
    assert template["schema_version"] == 2
    assert template["repository"] == project["repository"]
    assert "drive_root_id" not in template


def test_development_python_has_no_hardcoded_absolute_paths():
    violations = []
    for path in (PLUGIN_ROOT / "tools").glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if not isinstance(node, ast.Constant) or not isinstance(node.value, str):
                continue
            value = node.value
            posix_absolute = value != "/" and PurePosixPath(value).is_absolute()
            windows_absolute = PureWindowsPath(value).is_absolute()
            if posix_absolute or windows_absolute:
                violations.append((path.name, node.lineno, value))
    assert violations == []

import ast
import json
from pathlib import Path, PurePosixPath, PureWindowsPath
try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10
    import tomli as tomllib

import yaml


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT.joinpath("plugins", "sorrios-ensenada")
SKILL_ROOT = PLUGIN_ROOT.joinpath("skills", "editar-catastro-sorrios")


def test_plugin_and_marketplace_identifiers_match():
    plugin = json.loads(
        PLUGIN_ROOT.joinpath(".codex-plugin", "plugin.json").read_text(
            encoding="utf-8"
        )
    )
    marketplace = json.loads(
        ROOT.joinpath(".agents", "plugins", "marketplace.json").read_text(
            encoding="utf-8"
        )
    )
    entry = marketplace["plugins"][0]

    assert plugin["name"] == PLUGIN_ROOT.name == entry["name"]
    assert plugin["version"] == "1.2.0"
    assert plugin["skills"] == "./skills/"
    assert entry["source"]["path"] == "./plugins/sorrios-ensenada"
    install_source = ROOT.joinpath(
        *PurePosixPath(entry["source"]["path"]).parts
    ).resolve()
    assert install_source == PLUGIN_ROOT.resolve()
    assert install_source.joinpath("pyproject.toml").is_file()


def test_plugin_contains_exactly_one_valid_skill():
    skills = [
        path.parent
        for path in PLUGIN_ROOT.joinpath("skills").glob("*/SKILL.md")
    ]
    assert skills == [SKILL_ROOT]

    text = SKILL_ROOT.joinpath("SKILL.md").read_text(encoding="utf-8")
    frontmatter = yaml.safe_load(text.split("---", 2)[1])
    assert frontmatter["name"] == SKILL_ROOT.name


def test_versions_are_synchronized():
    project_file = PLUGIN_ROOT.joinpath("pyproject.toml")
    project = tomllib.loads(project_file.read_text("utf-8"))
    template = yaml.safe_load(
        SKILL_ROOT.joinpath("assets", "templates", "proyecto.yaml").read_text(
            encoding="utf-8"
        )
    )

    assert project["project"]["version"] == "1.2.0"
    assert template["plugin"]["version"] == "1.2.0"
    assert template["skill"]["version"] == "1.2.0"
    assert project_file.is_file()
    assert not ROOT.joinpath("pyproject.toml").exists()


def test_operational_python_has_no_hardcoded_absolute_paths():
    violations = []
    scripts = SKILL_ROOT.joinpath("scripts")
    for path in scripts.glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if not isinstance(node, ast.Constant) or not isinstance(
                node.value, str
            ):
                continue
            value = node.value
            posix_absolute_path = (
                value != "/" and PurePosixPath(value).is_absolute()
            )
            windows_absolute_path = PureWindowsPath(value).is_absolute()
            if posix_absolute_path or windows_absolute_path:
                violations.append((path.name, node.lineno, value))

    assert violations == []


def test_operational_python_does_not_use_os_path():
    violations = []
    scripts = SKILL_ROOT.joinpath("scripts")
    for path in scripts.glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute) and isinstance(
                node.value, ast.Name
            ):
                if node.value.id == "os" and node.attr == "path":
                    violations.append((path.name, node.lineno))

    assert violations == []

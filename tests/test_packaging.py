import os
from pathlib import Path
import shutil
import subprocess
import sys
try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10
    import tomli as tomllib


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT.joinpath("plugins", "sorrios-ensenada")
SCRIPTS = (
    "render_unit.py",
    "validate_operation.py",
    "validate_workspace.py",
)


def test_isolated_plugin_resolves_dependencies_and_script_help(tmp_path):
    isolated_plugin = tmp_path.joinpath("sorrios-ensenada")
    shutil.copytree(PLUGIN_ROOT, isolated_plugin)

    project_file = isolated_plugin.joinpath("pyproject.toml")
    project = tomllib.loads(project_file.read_text(encoding="utf-8"))
    assert project["project"]["dependencies"] == ["PyYAML>=6.0,<7"]
    assert project["project"]["optional-dependencies"]["render"] == [
        "Pillow>=10,<13"
    ]

    environment = os.environ.copy()
    environment.pop("PYTHONPATH", None)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    resolution = subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--dry-run",
            "--no-index",
            "--no-build-isolation",
            ".[render]",
        ],
        cwd=isolated_plugin,
        env=environment,
        check=False,
        capture_output=True,
        text=True,
    )
    assert resolution.returncode == 0, resolution.stdout + resolution.stderr

    script_root = isolated_plugin.joinpath(
        "skills", "editar-catastro-sorrios", "scripts"
    )
    for script_name in SCRIPTS:
        help_result = subprocess.run(
            [sys.executable, script_root.joinpath(script_name), "--help"],
            cwd=isolated_plugin,
            env=environment,
            check=False,
            capture_output=True,
            text=True,
        )
        assert help_result.returncode == 0, (
            help_result.stdout + help_result.stderr
        )

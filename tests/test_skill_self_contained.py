from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "plugins" / "sorrios-ensenada" / "skills" / "editar-catastro-sorrios"


def test_skill_links_resolve_inside_plugin_and_not_to_project_bootstrap():
    text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    targets = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    assert targets
    assert all("PROJECT.md" not in target for target in targets)
    for target in targets:
        resolved = (SKILL_ROOT / target).resolve()
        assert SKILL_ROOT.resolve() in resolved.parents
        assert resolved.is_file()


def test_skill_declares_github_workspace_and_read_only_drive_pdf():
    text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    assert "miguel-conde/sorrios-ensenada" in text
    assert "project/" in text
    assert "solo lectura" in text
    assert "No subas el PDF a GitHub" in text

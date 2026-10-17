import json
from pathlib import Path
import re
try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10
    import tomli as tomllib

import yaml


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugins" / "sorrios-ensenada"


def test_software_license_is_standard_mit_with_approved_holder():
    text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    assert text.startswith("MIT License\n\nCopyright (c) 2026 Miguel Conde de Simón\n")
    assert "Permission is hereby granted, free of charge" in text
    assert "THE SOFTWARE IS PROVIDED \"AS IS\"" in text
    assert "Creative Commons" not in text


def test_content_license_and_notice_preserve_scope_and_exclusions():
    content = (ROOT / "LICENSE-CONTENT.md").read_text(encoding="utf-8")
    notice = (ROOT / "NOTICE").read_text(encoding="utf-8")

    for expected in (
        "© 2026 Miguel Conde de Simón",
        "CC BY 4.0",
        "publication/content/**",
        "project/20_TRABAJO_EDITORIAL/**",
        "project/30_RESULTADOS/**",
        "texto histórico de 1752",
        "datos y capas cartográficos de terceros",
    ):
        assert expected in content

    for expected in (
        "Obra derivada de BDLJE CC-BY 4.0 ign.es",
        "Obra derivada de NGBE CC-BY 4.0 ign.es",
        "Obra derivada de IGR_HIDROGRAFIA v1 2023 CC-BY 4.0 scne.es",
        "El PDF manuscrito autoritativo no forma parte de este repositorio",
    ):
        assert expected in notice


def test_plugin_and_python_package_declare_mit_without_version_drift():
    plugin = json.loads(
        (PLUGIN_ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8")
    )
    pyproject = tomllib.loads(
        (PLUGIN_ROOT / "pyproject.toml").read_text(encoding="utf-8")
    )
    assert plugin["license"] == pyproject["project"]["license"] == "MIT"
    assert plugin["version"] == pyproject["project"]["version"] == "2.0.2"


def test_portable_workflow_has_read_only_permissions_and_concurrency():
    workflow = yaml.safe_load(
        (ROOT / ".github" / "workflows" / "portable-tests.yml").read_text(
            encoding="utf-8"
        )
    )
    assert workflow["permissions"] == {"contents": "read"}
    assert workflow["concurrency"]["cancel-in-progress"] is True
    job = workflow["jobs"]["test"]
    assert job["strategy"]["matrix"]["os"] == ["windows-latest", "ubuntu-latest"]
    assert job["strategy"]["matrix"]["python-version"] == ["3.10", "3.13"]


def test_public_readme_and_issue_templates_cover_reader_routes():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    normalized = " ".join(readme.split())
    assert "Sorribos y Santibáñez de Ordás en 1752" in normalized
    assert "EMAIL DE CONTACTO — PLACEHOLDER PENDIENTE" in readme
    assert "no declara todavía publicada la edición 1.0" in readme
    assert not re.search(r"\b(?:PKG|GATE)-\d+\b", readme)

    correction = (
        ROOT / ".github" / "ISSUE_TEMPLATE" / "correccion-transcripcion.md"
    ).read_text(encoding="utf-8")
    technical = (
        ROOT / ".github" / "ISSUE_TEMPLATE" / "problema-tecnico.md"
    ).read_text(encoding="utf-8")
    for text in (correction, technical):
        frontmatter = yaml.safe_load(text.split("---", 2)[1])
        assert frontmatter["name"]
        assert frontmatter["about"]
        assert frontmatter["title"]
    for heading in ("## Capítulo o sección", "## Pasaje", "## Corrección propuesta", "## Fuente o evidencia"):
        assert heading in correction
    for term in ("repositorio", "script", "generación", "navegación"):
        assert term in technical


def test_relative_links_in_public_entry_documents_resolve():
    documents = [ROOT / "README.md", ROOT / "LICENSE-CONTENT.md"]
    for document in documents:
        text = document.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
            if target.startswith(("https://", "http://", "mailto:")):
                continue
            path = target.split("#", 1)[0]
            assert (document.parent / path).resolve().exists(), (document, target)


def test_current_normative_documents_do_not_require_a_private_repository():
    documents = (
        ROOT / "PROJECT.md",
        PLUGIN_ROOT / "skills" / "editar-catastro-sorrios" / "SKILL.md",
        ROOT / "docs" / "PLAN_MAESTRO_PUBLICACION_QUARTO.md",
        ROOT / "docs" / "ARQUITECTURA_CHATGPT_GITHUB_DRIVE.md",
        ROOT / "docs" / "CHECKPOINT_REANUDACION_PREVIEW_FINAL.md",
    )
    pattern = re.compile(r"repositorio\s+privado|repo\s+privado|private repository", re.I)
    for document in documents:
        assert not pattern.search(document.read_text(encoding="utf-8")), document

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PUBLICATION = ROOT / "publication"
SCRIPTS = PUBLICATION / "scripts"
sys.path.insert(0, str(SCRIPTS))

import check_sources  # noqa: E402
import quality_audit as quality  # noqa: E402


CURRENT_CANONICAL_COMMIT = "a162fad1792aa9b3804a5499d348ab355e5ce574"
PHASE6A_HISTORICAL_CANONICAL_COMMIT = (
    "e81dc9239ac8dbabfe77168a50ef98c4d3b79170"
)
MANUSCRIPT_SHA256 = "d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24"


def _yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _git(*arguments: str) -> str:
    return subprocess.run(
        ["git", *arguments],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def test_candidate_keeps_development_semantics_without_inventing_release_metadata():
    publication = _yaml(PUBLICATION / "meta/publication.yml")
    assert publication["publication"] == {
        "version": "0.1.0-dev",
        "status": "development",
    }
    assert publication["base"]["git_commit"] == CURRENT_CANONICAL_COMMIT
    forbidden = {"author", "editor", "license", "copyright", "isbn", "url"}
    assert forbidden.isdisjoint(publication)
    assert "published" not in (PUBLICATION / "meta/publication.yml").read_text(
        encoding="utf-8"
    ).casefold()


def test_candidate_freezes_the_exact_canonical_project_snapshot():
    canonical_tree = _git("rev-parse", f"{CURRENT_CANONICAL_COMMIT}:project")
    candidate_tree = _git("rev-parse", "HEAD:project")
    assert re.fullmatch(r"[0-9a-f]{40}", canonical_tree)
    assert canonical_tree == candidate_tree
    publication = _yaml(PUBLICATION / "meta/publication.yml")
    check_sources._validate_base_snapshot(ROOT, publication)


def test_manuscript_metadata_is_exact_and_does_not_embed_the_source_pdf():
    project = _yaml(ROOT / "project/00_CONTROL/proyecto.yaml")
    publication = _yaml(PUBLICATION / "meta/publication.yml")
    manuscript = publication["manuscript"]
    assert manuscript["metadata_source"] == "project/00_CONTROL/proyecto.yaml"
    for key in ("file_id", "name", "sha256", "size_bytes", "pages"):
        assert manuscript[key] == project["authorities"]["manuscript"][key]
    assert manuscript["sha256"] == MANUSCRIPT_SHA256
    assert manuscript["size_bytes"] == 5_038_575
    assert manuscript["pages"] == 18
    assert not tuple(ROOT.rglob(manuscript["name"]))


def test_complete_structure_and_pdf_download_contract_are_stable():
    assert quality.audit_configuration(PUBLICATION) == []
    quarto = _yaml(PUBLICATION / "_quarto.yml")
    assert quarto["book"]["downloads"] == ["pdf"]
    assert quarto["book"]["output-file"] == "sorribos-santibanez-ordas-1752"
    assert len(quality.navigation_paths(quarto["book"]["chapters"])) == 38


def test_no_preview_provider_or_deployment_has_been_chosen_by_phase6a():
    forbidden = (
        ROOT / "netlify.toml",
        ROOT / "CNAME",
        ROOT / "vercel.json",
        ROOT / "firebase.json",
        ROOT / "wrangler.toml",
    )
    assert not any(path.exists() for path in forbidden)
    workflows = "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted((ROOT / ".github/workflows").glob("*.yml"))
    ).casefold()
    assert "deploy" not in workflows
    assert "pages" not in workflows
    assert "netlify" not in workflows


def test_phase6a_has_not_created_a_1_0_tag():
    assert _git("tag", "--list", "*1.0*") == ""


def test_release_security_audit_rejects_private_inputs_and_accepts_exact_download(
    tmp_path: Path,
):
    book = tmp_path / "_book"
    book.mkdir()
    pdf = book / quality.PDF_PATH.name
    pdf.write_bytes(b"candidate")
    (book / "index.html").write_text(
        f'<html lang="es"><body><a href="{pdf.name}">PDF</a></body></html>',
        encoding="utf-8",
    )
    original = quality.PDF_PATH
    quality.PDF_PATH = pdf
    try:
        assert quality.audit_release_candidate(book) == []
        (book / ".env").write_text("TOKEN=secret", encoding="utf-8")
        assert any("privado" in error for error in quality.audit_release_candidate(book))
    finally:
        quality.PDF_PATH = original


def test_rendered_candidate_passes_release_audit_when_artifacts_exist():
    if quality.BOOK_ROOT.is_dir() and quality.PDF_PATH.is_file():
        assert quality.audit_release_candidate(quality.BOOK_ROOT) == []
    else:
        assert "audit_release_candidate" in (
            SCRIPTS / "validate_publication.py"
        ).read_text(encoding="utf-8")


def test_candidate_report_manifests_snapshot_outputs_hashes_and_limitations():
    report = (ROOT / "docs/CANDIDATA_PUBLICACION_1_0.md").read_text(encoding="utf-8")
    for value in (
        "49ab2e1b1a58ca9201efab54b42a3125de7326f8",
        PHASE6A_HISTORICAL_CANONICAL_COMMIT,
        "e32917763475ceebdfe7b54830e1fb43f6419dad",
        MANUSCRIPT_SHA256,
        "0f2a27a3294060552ee5dde8a9b4d61258e85fef049679f650e3d71465234da0",
        "f1eee2f465f554d3bf2b506d23a622967d1b4f1013ac657a774868e525688183",
        "WCAG 2.1/2.2 AA",
        "PDF/UA",
        "PDF/A",
    ):
        assert value in report
    assert "PENDIENTE DECISIÓN/CONFIGURACIÓN DE PROVEEDOR DE PREVIEW" in report
    assert not re.search(r"(?:/home/|/tmp/|[A-Za-z]:\\\\)", report)


def test_roadmap_keeps_phase6_open_and_forbids_phase6b_before_human_acceptance():
    roadmap = (ROOT / "docs/ESTADO_PUBLICACION_QUARTO.md").read_text(
        encoding="utf-8"
    )
    for expectation in (
        "**Estado global:** Fase 6 en curso;",
        "| 6A | en curso |",
        "| PKG-00 | completado |",
        "| PKG-01 | completado e integrado |",
        "| PKG-02 | completado e integrado; incidencias canónicas cerradas; "
        "propagación completada por PKG-08 |",
        "| PKG-03 | completado e integrado |",
        "| CR-V1-001 | cerrada e integrada |",
        "| PKG-04 | completado e integrado |",
        "| PKG-05 | completado e integrado |",
        "`INC-BIB-001` y `INC-BIB-002` **CERRADAS CANÓNICAMENTE**",
        "GATE-01 = PASS. PKG-06, PKG-07 Y PKG-08 INTEGRADOS. PKG-09 "
        "PENDIENTE. GATE-02 = PENDIENTE.",
        "la propagación editorial quedó completada por PKG-08",
        "| PKG-06 | completado e integrado |",
        "| PKG-07 | completado e integrado |",
        "| PKG-08 | completado e integrado |",
        "| PKG-09 | habilitado — no iniciado, sujeto a DAT |",
        "su propagación obligatoria se asignó a PKG-08 y quedó completada",
        "PLACEHOLDER CONTROLADO PENDIENTE DE REDACCIÓN PERSONAL",
        "SIGUIENTE PASO RECOMENDADO: PKG-09 — identidad final, metadatos y "
        "colofón",
        "| 6B | pendiente | publicación 1.0, etiqueta y cierre; "
        "prohibida antes de la aceptación humana del preview |",
    ):
        assert expectation in roadmap
    assert "| CR-V1-001 | ejecución pendiente |" not in roadmap
    assert "bloquea el inicio de PKG-04" not in roadmap
    assert "| PKG-04 | prototipo aprobado e integrado — despliegue global pendiente |" not in roadmap
    assert "| PKG-06 | habilitado — no iniciado |" not in roadmap
    assert "| PKG-07 | habilitado — no iniciado |" not in roadmap
    assert "PKG-07 COMPLETADO EN RAMA AISLADA" not in roadmap
    assert "GATE-02 = PENDIENTE" in roadmap

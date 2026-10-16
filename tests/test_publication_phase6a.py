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


def test_final_identity_metadata_preserves_controlled_release_deferrals():
    publication = _yaml(PUBLICATION / "meta/publication.yml")
    metadata = publication["publication"]
    assert metadata["version"] == "1.0"
    assert metadata["status"] == "prepublication"
    assert metadata["identity"]["author"] == {
        "display": "Miguel Conde de Simón",
        "bibliographic": "Conde de Simón, Miguel",
    }
    assert metadata["identity"]["year"] == 2026
    assert metadata["pending"]["at_release"] == [
        "fecha exacta de publicación",
        "URL canónica",
    ]
    assert publication["base"]["git_commit"] == CURRENT_CANONICAL_COMMIT
    assert "isbn" not in metadata
    assert "url" not in metadata


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
    assert len(quality.navigation_paths(quarto["book"]["chapters"])) == 39


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


def test_roadmap_passes_gate02_and_keeps_phase6b_forbidden_before_human_acceptance():
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
        "GATE-01 = PASS. GATE-02 = PASS. PKG-06, PKG-07, PKG-08 Y PKG-09 "
        "COMPLETADOS, INTEGRADOS Y ACEPTADOS.",
        "la propagación editorial quedó completada por PKG-08",
        "| PKG-06 | completado e integrado |",
        "| PKG-07 | completado e integrado |",
        "| PKG-08 | completado e integrado |",
        "| PKG-09 | completado e integrado |",
        "su propagación obligatoria se asignó a PKG-08 y quedó completada",
        "PLACEHOLDER CONTROLADO PENDIENTE DE REDACCIÓN PERSONAL",
        "SIGUIENTE PASO RECOMENDADO: ejecutar PKG-10 — regeneración "
        "reproducible y candidata 1.0",
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
    assert "| PKG-09 | habilitado — no iniciado, sujeto a DAT |" not in roadmap
    assert "| GATE-02 | PASS |" in roadmap
    assert "PKG-10 habilitado y no iniciado" in roadmap
    gate02 = (ROOT / "docs/GATE_02_IMPLEMENTACION_1_0_ACEPTADA.md").read_text(
        encoding="utf-8"
    )
    for criterion in (
        "PKG-06–09 integrados",
        "No quedan datos obligatorios sin resolver",
        "No quedan cambios canónicos parcheados en `publication/`",
        "El alcance coincide con `ALCANCE_APROBADO_V1_0.md`",
    ):
        assert f"| {criterion} |" in gate02
    assert "`GATE-02 = PASS`" in gate02
    assert gate02.count("PASS — diferimiento previsto") >= 4
    assert "PKG-10 queda habilitado,\npero no iniciado" in gate02

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
PUBLICATION = ROOT / "publication"
SCRIPTS = PUBLICATION / "scripts"
sys.path.insert(0, str(SCRIPTS))

import quality_audit as quality  # noqa: E402


BASE_COMMIT = "b2700e58807dda7751c26155af42971f1f8a0c83"
CHAPTER_THREE = PUBLICATION / "content/01-catastro/03-expediente-sorribos-santibanez.qmd"
CHAPTER_FIVE = PUBLICATION / "content/02-estudio/05-lugar-senorio-concejo-ordas.qmd"
CHAPTER_THIRTEEN = (
    PUBLICATION
    / "content/02-estudio/13-economia-rural-integrada-vulnerabilidades-resiliencia-limites.qmd"
)
TIMELINE = PUBLICATION / "assets/visual/cronologia-documental.svg"
DIAGRAM = PUBLICATION / "assets/visual/diagrama-economia-rural.svg"
REGIONAL = PUBLICATION / "assets/cartography/mapa-regional.svg"
LOCAL = PUBLICATION / "assets/cartography/mapa-local.svg"


def _git(*arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *arguments],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


def test_pkg07_static_visual_audit_passes():
    assert quality.audit_visual_apparatus(PUBLICATION) == []
    assert quality.audit_configuration(PUBLICATION) == []


def test_timeline_uses_only_supported_milestones_and_keeps_top006_in_matrix_only():
    text = TIMELINE.read_text(encoding="utf-8")
    for milestone in (
        "1215",
        "1267",
        "1715",
        "17·09·1752",
        "1768",
        "1831 / 1864",
        "1836 / 1848",
        "Hoy",
    ):
        assert milestone in text
    assert "TOP-006" not in text
    assert "secuencia fonética completa" in text
    chapter = CHAPTER_THREE.read_text(encoding="utf-8")
    assert "TOP-006" not in chapter
    assert "testimonios anteriores" in chapter
    assert "documento local de 1752" in chapter
    assert "contexto posterior" in chapter


def test_economic_diagram_is_a_noncausal_rendering_of_chapter_thirteen_only():
    text = DIAGRAM.read_text(encoding="utf-8")
    for label in (
        "Tierra, cultivos y prados",
        "Ganado y aprovechamientos",
        "Trabajo y espacio doméstico",
        "Agua y molinos",
        "Común y servicios",
        "Derechos, fiscalidad y rentas",
        "Dinero, especie y servicio",
        "Conexiones exteriores",
        "No es cuenta, flujo",
        "No representa producción total, renta familiar, presión fiscal total",
    ):
        assert label in text
    assert "marker-end" not in text
    assert "<marker" not in text
    assert "vulnerabilidad" not in text.casefold()
    assert "amortigu" not in text.casefold()
    assert "diagrama-economia-rural.svg" in CHAPTER_THIRTEEN.read_text(encoding="utf-8")
    all_other_chapters = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (PUBLICATION / "content").rglob("*.qmd")
        if path != CHAPTER_THIRTEEN
    )
    assert "diagrama-economia-rural.svg" not in all_other_chapters


def test_the_two_approved_maps_are_byte_identical_and_used_once_each():
    expected = {
        REGIONAL: "2c6f3c76293a3c67aa698b9abd8b6ad184ad35c4fae3d80de6ec2f176ce99a1d",
        LOCAL: "ebc54b6593eab73778860a41db66221e78b6b83028b51602769d02a523fd15df",
    }
    for path, digest in expected.items():
        assert hashlib.sha256(path.read_bytes()).hexdigest() == digest
    chapters = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (PUBLICATION / "content").rglob("*.qmd")
    )
    assert chapters.count("mapa-regional.svg") == 1
    assert chapters.count("mapa-local.svg") == 1
    assert "no representa límites históricos de 1752" in chapters.casefold()
    assert "no reconstruye límites, caminos, términos" in chapters.casefold()


def test_all_four_visuals_have_title_caption_alt_source_and_svg_accessibility():
    chapter_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (CHAPTER_THREE, CHAPTER_FIVE, CHAPTER_THIRTEEN)
    )
    for filename in (
        "cronologia-documental.svg",
        "diagrama-economia-rural.svg",
        "mapa-regional.svg",
        "mapa-local.svg",
    ):
        figure = re.search(
            rf"!\[[^\]]{{30,}}\]\([^\)]*{re.escape(filename)}\)"
            rf'\{{[^}}]*fig-alt="[^"]{{40,}}"[^}}]*\}}',
            chapter_text,
        )
        assert figure, filename
    assert chapter_text.count("::: {.visual-source}") == 4
    assert chapter_text.count("lightbox: true") == 3

    for asset in (TIMELINE, DIAGRAM, REGIONAL, LOCAL):
        root = ElementTree.parse(asset).getroot()
        assert root.attrib["role"] == "img"
        labelled = root.attrib["aria-labelledby"].split()
        ids = {element.attrib.get("id") for element in root.iter()}
        assert all(label in ids for label in labelled)
        assert any(element.tag.endswith("title") for element in root)
        assert any(element.tag.endswith("desc") for element in root)
        assert not any(element.tag.endswith("image") for element in root.iter())


def test_visual_layout_is_responsive_and_not_dependent_on_colour_alone():
    styles = (PUBLICATION / "styles/book.scss").read_text(encoding="utf-8")
    for fragment in (
        ".visual-apparatus",
        "max-width: 100%",
        "height: auto",
        ".visual-source",
        "@media (max-width: 48rem)",
    ):
        assert fragment in styles
    timeline = TIMELINE.read_text(encoding="utf-8")
    diagram = DIAGRAM.read_text(encoding="utf-8")
    assert "TESTIMONIO ANTERIOR" in timeline
    assert "DOCUMENTO LOCAL" in timeline
    assert "CONTEXTO POSTERIOR" in timeline
    assert "IDENTIFICACIÓN ACTUAL" in timeline
    assert "stroke-dasharray" in timeline
    assert "relación sin dirección causal" in diagram


def test_pkg07_preserves_canonical_generated_and_content_not_owned_by_pkg09():
    assert _git("diff", "--quiet", BASE_COMMIT, "--", "project/").returncode == 0
    assert _git(
        "diff", "--quiet", BASE_COMMIT, "--", "publication/generated/"
    ).returncode == 0
    assert _git("ls-files", "publication/_book", "publication/generated").stdout == ""
    for relative in (
        "publication/content/00-preliminares/02-prologo.qmd",
        "publication/content/01-catastro/04-manuscrito-volumen-actual.qmd",
    ):
        expected = _git("show", f"{BASE_COMMIT}:{relative}")
        assert expected.returncode == 0
        assert (ROOT / relative).read_text(encoding="utf-8") == expected.stdout


def test_pkg07_does_not_add_excluded_visuals_or_release_outputs():
    added = _git("diff", "--name-only", "--diff-filter=A", BASE_COMMIT).stdout.splitlines()
    forbidden = (
        "concejo-municipio",
        "termino-historico",
        "vulnerabilidades-amortiguadores",
        "_book/",
        "publication/generated/",
    )
    assert not any(token in path for path in added for token in forbidden)
    assert not any(Path(path).suffix.casefold() in {".pdf", ".png"} for path in added)

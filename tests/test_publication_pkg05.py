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

import apparatus_sources as apparatus  # noqa: E402
import build_apparatus as apparatus_builder  # noqa: E402
import build_indexes as index_builder  # noqa: E402


PDF = PUBLICATION / "_book" / "sorribos-santibanez-ordas-1752.pdf"
GLOSSARY = ROOT / apparatus_builder.GLOSSARY_SOURCE
EXPECTED_GLOSSARY_ORDER = (
    "alcavalas",
    "añino",
    "arbitrio",
    "arenta",
    "avitadores",
    "boto",
    "diezmos",
    "entreparedes",
    "esquilmo",
    "establecimiento del suelo",
    "fejes",
    "Ferrañales",
    "hijo de familia",
    "medio vecino",
    "molino venturero",
    "negrillos",
    "pan",
    "pelo",
    "pies de abejas",
    "pobre de solemnidad",
    "primicia",
    "propios",
    "quartal",
    "repartimiento",
    "Señorío",
    "servicio ordinario y extraordinario",
    "utilidad",
    "vecera",
)


def _generated_glossary() -> str:
    data = apparatus_builder.load_apparatus_data(
        ROOT,
        PUBLICATION,
        "sorrios_ensenada_orden_lectura_calidad_original.pdf",
    )
    return apparatus_builder.glossary_qmd(data)


def _glossary_terms(text: str) -> tuple[str, ...]:
    return tuple(re.findall(r"^### (.+?) \{#glosario-", text, re.MULTILINE))


def _pdf_text() -> str:
    return subprocess.run(
        ["pdftotext", "-layout", str(PDF), "-"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout


def test_pkg05_toc_01_pdf_toc_separates_number_and_title():
    preamble = (PUBLICATION / "styles/latex/preamble.tex").read_text(encoding="utf-8")
    assert r"\RedeclareSectionCommand[tocnumwidth=4.2em]{section}" in preamble
    if PDF.is_file():
        toc = "\f".join(_pdf_text().split("\f")[:19])
        assert not re.search(r"(?m)^\s*\d+\.\d+(?=[A-ZÁÉÍÓÚÜÑ«])", toc)


def test_pkg05_toc_02_two_digit_nested_numbers_do_not_touch_titles():
    if PDF.is_file():
        toc = "\f".join(_pdf_text().split("\f")[:19])
        assert re.search(r"16\.35\s+Respuesta 33", toc)
        assert re.search(r"14\.18\s+Página digital 18", toc)


def test_pkg05_glo_01_has_exactly_28_entries():
    assert len(_glossary_terms(_generated_glossary())) == 28


def test_pkg05_glo_02_uses_deterministic_spanish_alphabetical_order():
    assert _glossary_terms(_generated_glossary()) == EXPECTED_GLOSSARY_ORDER


def test_pkg05_glo_03_handles_case_diacritics_unicode_spaces_and_enye():
    key = apparatus_builder.glossary_sort_key
    assert key("  ÁRBOL  ")[0] == key("árbol")[0] == key("arbol")[0]
    assert sorted(("Oca", "Ñandú", "nube"), key=key) == ["nube", "Ñandú", "Oca"]
    assert sorted(("servicio", "Señorío"), key=key) == ["Señorío", "servicio"]


def test_pkg05_glo_04_preserves_every_published_field_and_hides_context():
    source = apparatus.load_glossary(GLOSSARY)
    output = _generated_glossary()
    for entry in source.entries:
        start = output.index(f"### {entry.term} {{#{entry.anchor} .unnumbered}}")
        end = output.find("\n### ", start + 1)
        block = output[start : end if end >= 0 else len(output)]
        for label in (
            "Término documentado",
            "Definición",
            "Primera unidad",
            "Referencias",
            "Notas",
        ):
            assert f"**{label}:**" in block
        assert "**Contexto histórico:**" not in block


def test_pkg05_idx_01_all_nine_indexes_receive_pdf_entry_separation():
    data = index_builder.load_index_data(ROOT, PUBLICATION)
    outputs = index_builder.generated_indexes(data)
    assert len(outputs) == 9
    assert tuple(text.count(".index-entry}") for text in outputs.values()) == (
        21,
        9,
        7,
        12,
        12,
        27,
        15,
        40,
        21,
    )
    lua = (SCRIPTS / "pdf_index_entries.lua").read_text(encoding="utf-8")
    preamble = (PUBLICATION / "styles/latex/preamble.tex").read_text(encoding="utf-8")
    assert 'div.classes:includes("index-entry")' in lua
    assert "PublicationIndexEntry" in lua and "PublicationIndexEntry" in preamble


def test_pkg05_idx_02_preserves_all_pdf_and_html_locators():
    data = index_builder.load_index_data(ROOT, PUBLICATION)
    for output in index_builder.generated_indexes(data).values():
        assert set(re.findall(r"\.qmd#([a-z0-9-]+)\)", output)) == set(
            re.findall(r"\\hyperref\[([a-z0-9-]+)\]", output)
        )


def test_pkg05_idx_03_preserves_generated_entry_order():
    data = index_builder.load_index_data(ROOT, PUBLICATION)
    first = index_builder.generated_indexes(data)
    second = index_builder.generated_indexes(data)
    assert first == second
    assert "Pregunta/Respuesta 1" in first[index_builder.OUTPUT_NAMES[7]]
    assert first[index_builder.OUTPUT_NAMES[7]].index("Pregunta/Respuesta 1") < first[
        index_builder.OUTPUT_NAMES[7]
    ].index("Pregunta/Respuesta 40")


def _sidebar_states(path: Path) -> tuple[tuple[int, bool], ...]:
    text = path.read_text(encoding="utf-8")
    return tuple(
        (int(number), "show" in classes.split())
        for number, classes in re.findall(
            r'<ul id="quarto-sidebar-section-(\d+)" class="([^"]+)"', text
        )
    )


def test_pkg05_sid_01_active_part_is_open_in_rendered_html():
    sample = PUBLICATION / "_book/generated/glosario.html"
    if sample.is_file():
        assert sum(opened for _, opened in _sidebar_states(sample)) == 1
        assert _sidebar_states(sample)[-1] == (6, True)


def test_pkg05_sid_02_inactive_parts_are_collapsed():
    sample = PUBLICATION / "_book/generated/14-facsimil.html"
    if sample.is_file():
        states = _sidebar_states(sample)
        assert states[2] == (3, True)
        assert all(not opened for number, opened in states if number != 3)


def test_pkg05_sid_03_contract_is_present_in_all_six_parts():
    samples = (
        "content/01-catastro/01-catastro-ensenada.html",
        "content/02-estudio/05-lugar-senorio-concejo-ordas.html",
        "generated/14-facsimil.html",
        "generated/15-transcripcion.html",
        "generated/16-edicion-modernizada.html",
        "generated/glosario.html",
    )
    if all((PUBLICATION / "_book" / sample).is_file() for sample in samples):
        for expected, sample in enumerate(samples, start=1):
            states = _sidebar_states(PUBLICATION / "_book" / sample)
            assert len(states) == 6
            assert states[expected - 1] == (expected, True)
            assert sum(opened for _, opened in states) == 1


def test_pkg05_sid_04_uses_native_collapse_and_minimal_local_keyboard_adapter():
    quarto = yaml.safe_load((PUBLICATION / "_quarto.yml").read_text(encoding="utf-8"))
    assert quarto["book"]["sidebar"]["collapse-level"] == 1
    include = PUBLICATION / quarto["format"]["html"]["include-after-body"]
    script = include.read_text(encoding="utf-8")
    assert "sidebar-item-toggle" in script
    assert 'event.key === "Enter"' in script and 'event.key === " "' in script
    assert "http://" not in script and "https://" not in script


def test_pkg05_rev026_uses_lossless_png_compression_for_transcription_crops():
    source = (SCRIPTS / "build_transcription.py").read_text(encoding="utf-8")
    prototype = (SCRIPTS / "build_vertical_prototype.py").read_text(encoding="utf-8")
    assert 'crop.save(destination, format="PNG", compress_level=9)' in source
    assert 'image.save(compressed_crop, format="PNG", compress_level=9)' in prototype
    assert "resize(" not in source

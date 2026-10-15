from __future__ import annotations

import hashlib
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "publication" / "scripts"
sys.path.insert(0, str(SCRIPTS))

import apparatus_sources as sources  # noqa: E402
import build_apparatus as builder  # noqa: E402
import critical_edition as critical  # noqa: E402
import modernized_edition as modernized  # noqa: E402


MANUSCRIPT_NAME = "sorrios_ensenada_orden_lectura_calidad_original.pdf"
GLOSSARY = ROOT / builder.GLOSSARY_SOURCE
REGISTER = ROOT / builder.REGISTER_SOURCE
UNITS = ROOT / builder.UNITS_SOURCE


@pytest.fixture(scope="module")
def glossary() -> sources.Glossary:
    return sources.load_glossary(GLOSSARY)


@pytest.fixture(scope="module")
def register() -> sources.EvidenceRegister:
    return sources.load_evidence_register(REGISTER)


@pytest.fixture(scope="module")
def data() -> builder.ApparatusData:
    return builder.load_apparatus_data(ROOT, ROOT / "publication", MANUSCRIPT_NAME)


@pytest.fixture(scope="module")
def generated(data) -> dict[str, str]:
    return builder.generated_apparatus(data)


def _strip_links(text: str) -> str:
    return re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text)


def _glossary_block(text: str, entry: sources.GlossaryEntry) -> str:
    start = text.index(f"### {entry.term} {{#{entry.anchor} .unnumbered}}")
    following = text.find("\n### ", start + 1)
    return text[start : following if following >= 0 else len(text)]


def _glossary_entry(
    term: str,
    *,
    historical_context: str | None = None,
) -> str:
    fields = [
        ("Término documentado", f"`{term}`"),
        ("Definición", f"Definición de {term}."),
        ("Primera unidad", "folio 307r."),
        ("Referencias", "folio 307r; respuesta 1.ª."),
    ]
    if historical_context is not None:
        fields.append(("Contexto histórico", historical_context))
    fields.append(("Notas", f"Notas de {term}."))
    return "\n".join(
        [f"### {term}", "", *(f"- **{label}:** {value}" for label, value in fields)]
    )


def _glossary_document(*entries: str) -> str:
    return "# Glosario histórico\n\n## Entradas\n\n" + "\n\n".join(entries) + "\n"


def _isolated_tree(tmp_path: Path) -> tuple[Path, Path]:
    repository = tmp_path / "repository"
    publication = repository / "publication"
    for logical in (
        builder.GLOSSARY_SOURCE,
        builder.REGISTER_SOURCE,
        builder.STUDY_SOURCE,
        builder.CRITICAL_SOURCE,
        builder.MODERNIZED_SOURCE,
        builder.UNITS_SOURCE,
    ):
        destination = repository / logical
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / logical, destination)
    (publication / "meta").mkdir(parents=True)
    shutil.copy2(
        ROOT / "publication/meta/publication.yml",
        publication / "meta/publication.yml",
    )
    shutil.copytree(
        ROOT / "publication/content/02-estudio",
        publication / "content/02-estudio",
    )
    (publication / "generated").mkdir(parents=True)
    return repository, publication


def _hashes(paths: tuple[Path, ...]) -> dict[str, str]:
    return {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}


def test_glossary_has_no_invented_version_and_all_unique_entries(glossary):
    assert glossary.version is None
    assert len(glossary.entries) == 28
    assert len({entry.term for entry in glossary.entries}) == 28
    assert len({entry.anchor for entry in glossary.entries}) == 28


def test_glossary_accepts_entry_with_five_required_fields():
    glossary = sources.parse_glossary(
        _glossary_document(_glossary_entry("cinco campos"))
    )
    assert glossary.entries[0].historical_context is None


def test_glossary_accepts_and_preserves_optional_historical_context():
    context = "Contexto canónico breve y sustentado."
    glossary = sources.parse_glossary(
        _glossary_document(
            _glossary_entry("seis campos", historical_context=context)
        )
    )
    assert glossary.entries[0].historical_context == context


def test_glossary_accepts_mixed_five_and_six_field_entries():
    glossary = sources.parse_glossary(
        _glossary_document(
            _glossary_entry("entrada base"),
            _glossary_entry(
                "entrada contextual",
                historical_context="Contexto selectivo.",
            ),
        )
    )
    assert [entry.historical_context for entry in glossary.entries] == [
        None,
        "Contexto selectivo.",
    ]


def test_glossary_rejects_missing_required_field():
    entry = _glossary_entry("sin definición").replace(
        "- **Definición:** Definición de sin definición.\n", ""
    )
    with pytest.raises(sources.ApparatusSourceError, match="cinco campos base"):
        sources.parse_glossary(_glossary_document(entry))


def test_glossary_rejects_unknown_field():
    entry = _glossary_entry("campo desconocido").replace(
        "- **Notas:**", "- **Campo desconocido:** valor\n- **Notas:**"
    )
    with pytest.raises(sources.ApparatusSourceError, match="cinco campos base"):
        sources.parse_glossary(_glossary_document(entry))


def test_glossary_rejects_duplicate_optional_field():
    entry = _glossary_entry(
        "contexto duplicado", historical_context="Primer contexto."
    ).replace(
        "- **Notas:**",
        "- **Contexto histórico:** Segundo contexto.\n- **Notas:**",
    )
    with pytest.raises(sources.ApparatusSourceError, match="Contexto histórico"):
        sources.parse_glossary(_glossary_document(entry))


def test_glossary_keeps_rejecting_duplicate_required_field():
    entry = _glossary_entry("definición duplicada").replace(
        "- **Primera unidad:**",
        "- **Definición:** Otra definición.\n- **Primera unidad:**",
    )
    with pytest.raises(sources.ApparatusSourceError, match="cinco campos base"):
        sources.parse_glossary(_glossary_document(entry))


def test_glossary_rejects_malformed_entry_heading():
    text = _glossary_document(_glossary_entry("encabezado")).replace(
        "### encabezado", "#### encabezado"
    )
    with pytest.raises(sources.ApparatusSourceError, match="encabezado.*mal formado"):
        sources.parse_glossary(text)


def test_glossary_manifest_uses_verified_git_blob_not_version(glossary):
    manifest = yaml.safe_load(
        (ROOT / "publication/meta/publication.yml").read_text(encoding="utf-8")
    )
    declared = manifest["sources"]["glossary"]
    assert "version" not in declared
    assert declared["git_blob"] == sources.git_blob_oid(GLOSSARY.read_bytes())


def test_glossary_manifest_rejects_incorrect_git_blob(tmp_path):
    repository, publication = _isolated_tree(tmp_path)
    manifest_path = publication / "meta/publication.yml"
    manifest = manifest_path.read_text(encoding="utf-8")
    actual = sources.git_blob_oid(
        (repository / builder.GLOSSARY_SOURCE).read_bytes()
    )
    manifest_path.write_text(
        manifest.replace(actual, "0" * 40),
        encoding="utf-8",
    )
    with pytest.raises(
        builder.ApparatusBuildError,
        match="no declara el blob Git vigente del Glosario",
    ):
        builder.load_apparatus_data(repository, publication, MANUSCRIPT_NAME)


def test_glossary_preserves_every_field_and_external_source(glossary, generated):
    output = generated["glosario.qmd"]
    for entry in glossary.entries:
        block = _strip_links(_glossary_block(output, entry))
        for label, value in (
            ("Término documentado", entry.documented_term),
            ("Definición", entry.definition),
            ("Primera unidad", entry.first_unit),
            ("Referencias", entry.references),
            ("Notas", entry.notes),
        ):
            assert f"**{label}:** {value}" in block, (entry.term, label)
        assert "**Contexto histórico:**" not in block
    assert "https://www.mapa.gob.es/" in output
    assert "https://dle.rae.es/negrillo" in output


def test_glossary_links_only_resolvable_references(generated):
    output = generated["glosario.qmd"]
    assert "[folio 315v](15-transcripcion.qmd#folio-315v)" in output
    assert "[respuesta 17.ª](16-edicion-modernizada.qmd#respuesta-17)" in output
    assert "Glosario: [`arbitrio`](#glosario-arbitrio)" in output
    assert "Índice de medidas: `libras`" in output
    assert "Índice de medidas](" not in output


def test_glossary_rejects_duplicate_or_missing_required_field():
    text = GLOSSARY.read_text(encoding="utf-8")
    duplicate = text + "\n### Señorío\n\n" + text.split("### Señorío", 1)[1]
    with pytest.raises(sources.ApparatusSourceError, match="duplicad"):
        sources.parse_glossary(duplicate)
    missing = text.replace("- **Definición:**", "- **Definición ausente:**", 1)
    with pytest.raises(sources.ApparatusSourceError, match="entrada 'Señorío'.*campos"):
        sources.parse_glossary(missing)


def test_register_is_complete_unique_and_preserves_compound_levels(register):
    assert register.version == "1.3"
    assert len(register.entries) == 111
    assert len(register.calculations) == 20
    assert len({entry.identifier for entry in register.entries}) == 111
    assert {component for entry in register.entries for component in entry.level_components} == {
        "D", "C", "I", "E", "L"
    }
    assert {"E/I", "E/L", "L/I"}.issubset({entry.level for entry in register.entries})


def test_register_states_are_preserved_without_silent_exclusion(register):
    counts = Counter(entry.state for entry in register.entries)
    assert counts == {"Admitida": 87, "Condicionada": 10, "Mantener cautela": 1, None: 13}
    assert not any(entry.state == "Excluida" for entry in register.entries)


def test_quantitative_view_derives_all_and_only_level_c_entries(register, generated):
    output = generated["cuadros-cuantitativos.qmd"]
    calculated = register.calculated_entries
    assert len(calculated) == 13
    assert re.findall(r"^### ([A-Z]+-\d{3}) \{#cuadro-", output, re.MULTILINE) == [
        entry.identifier for entry in calculated
    ]
    assert all(entry.level == "C" for entry in calculated)


def test_quantitative_view_preserves_all_associated_calculations(register, generated):
    output = generated["cuadros-cuantitativos.qmd"]
    associated = [
        calculation
        for entry in register.calculated_entries
        for calculation in register.associated_calculations(entry)
    ]
    assert len(associated) == len({item.identifier for item in associated}) == 17
    for calculation in associated:
        row = (
            f"| {calculation.identifier} | {calculation.operation} | "
            f"{calculation.result} | {calculation.inputs} | {calculation.condition} |"
        )
        assert output.count(row) == 1
    assert "CAL-018`, `CAL-019` y `CAL-020`" in output


@pytest.mark.parametrize(
    "marker",
    [
        "3.811,5 medidas + 7 celemines",
        "Cabida cultivada comparable",
        "93,13 %",
        "Denominador: cultivada comparable.",
        "72,16 %",
        "Denominador: total explícito principal.",
        "Índice analítico, no observación anual.",
        "160 libras",
        "36 reales",
        "72,22 %",
        "3 + 2 + 2 + 1",
        "26 cargas de centeno",
        "1.006 reales",
        "25 reales",
        "10,73 %",
        "2,49 %",
    ],
)
def test_quantitative_regressions_come_from_register(marker, register, generated):
    assert marker in REGISTER.read_text(encoding="utf-8")
    assert marker in generated["cuadros-cuantitativos.qmd"]


@pytest.mark.parametrize(
    ("old", "new", "context"),
    [
        ("Denominador: cultivada comparable.", "Denominador: total.", "AGR-005"),
        ("160 libras", "160 medidas", "AGR-009"),
    ],
)
def test_fidelity_gate_rejects_changed_denominator_or_unit(
    data, generated, old, new, context
):
    mutated = dict(generated)
    mutated["cuadros-cuantitativos.qmd"] = mutated["cuadros-cuantitativos.qmd"].replace(
        old, new, 1
    )
    with pytest.raises(builder.ApparatusBuildError, match=context):
        builder.validate_apparatus_fidelity(data, mutated)


def test_concordance_has_exactly_35_units_18_pages_and_positions(data, generated):
    output = generated["concordancia.qmd"]
    unit_region = output.split("## Vista por unidad", 1)[1].split("## Vista por respuesta", 1)[0]
    rows = re.findall(r"^\| (\d+) \|", unit_region, re.MULTILINE)
    assert rows == [str(number) for number in range(1, 36)]
    assert {spec.pdf_page for spec in data.specs} == set(range(1, 19))
    assert {spec.position for spec in data.specs} == {"complete", "left", "right"}
    assert "transcripcion-portada" in unit_region
    assert "modernizada-portada" in unit_region


def test_concordance_response_view_is_complete_and_many_to_many(data, generated):
    mapping = modernized.response_unit_labels(data.modernized)
    assert len(mapping) == 40
    assert sum(len(labels) for labels in mapping.values()) == 65
    assert mapping[17] == ("Folio 315r", "Folio 315v", "Folio 316r")
    assert any(len(labels) > 1 for labels in mapping.values())
    output = generated["concordancia.qmd"].split("## Vista por respuesta", 1)[1]
    assert re.findall(r"^\| (\d+) \|", output, re.MULTILINE) == [
        str(number) for number in range(1, 41)
    ]


def test_concordance_preserves_special_material_units(generated):
    output = generated["concordancia.qmd"]
    for marker in (
        "| 1 | Portada |",
        "| 2 | Reverso de la portada |",
        "Comparecencia",
        "Ratificación",
        "Firmas",
        "| 35 | Hoja enfrentada posterior |",
    ):
        assert marker in output


def test_concordance_links_every_target_chapter(generated):
    output = generated["concordancia.qmd"]
    assert output.count("14-facsimil.qmd#") >= 75
    assert output.count("15-transcripcion.qmd#") == 100
    assert output.count("16-edicion-modernizada.qmd#") == 110


def test_matrix_preserves_all_register_fields_and_levels(register, generated):
    output = generated["matriz-evidencia.qmd"]
    identifiers = re.findall(r"^### ([A-Z]+-\d{3}) \{#evidencia-", output, re.MULTILINE)
    assert identifiers == [entry.identifier for entry in register.entries]
    for entry in register.entries:
        assert f"**Formulación canónica:** {entry.statement}" in output
        assert f"**Nivel:** `{entry.level}`" in output
        assert f"**Evidencia:** {entry.evidence}" in output
        assert f"**Estado y cautela:** {entry.status_caution or '—'}" in output


def test_matrix_keeps_problematic_canonical_entries_as_apparatus_not_narrative(generated):
    output = generated["matriz-evidencia.qmd"]
    assert "como 26 habitantes fiscales" in output
    assert "`Sorribas` no se trata como variante histórica" in output
    assert "La matriz reproduce el Registro 1.3" in output
    assert "no convierte sus formulaciones en prosa" in output


def test_matrix_usage_is_derived_from_existing_chapter_metadata(data, generated):
    assert [use.number for use in data.evidence_usage["JUR-005"]] == [5, 10, 13]
    output = generated["matriz-evidencia.qmd"]
    assert "[cap. 5: Un lugar de señorío" in output
    assert "../content/02-estudio/05-lugar-senorio-concejo-ordas.qmd" in output


def test_matrix_fidelity_gate_rejects_reinterpretation(data, generated):
    mutated = dict(generated)
    mutated["matriz-evidencia.qmd"] = mutated["matriz-evidencia.qmd"].replace(
        "no equivale a población total", "equivale a población total", 1
    )
    with pytest.raises(builder.ApparatusBuildError, match="DEM-002.*Estado y cautela"):
        builder.validate_apparatus_fidelity(data, mutated)


def test_all_phase4_heading_anchors_are_globally_unique(generated):
    texts = [
        (ROOT / "publication/generated/14-facsimil.qmd").read_text(encoding="utf-8"),
        (ROOT / "publication/generated/15-transcripcion.qmd").read_text(encoding="utf-8"),
        (ROOT / "publication/generated/16-edicion-modernizada.qmd").read_text(encoding="utf-8"),
        *generated.values(),
    ]
    anchors = [
        anchor
        for text in texts
        for anchor in re.findall(r"^#{2,3} .+ \{#([a-z0-9-]+)\}$", text, re.MULTILINE)
    ]
    assert len(anchors) == len(set(anchors))
    assert "transcripcion-portada" in anchors
    assert "modernizada-portada" in anchors
    assert "portada" not in anchors


def test_every_generated_cross_link_has_a_real_target(generated):
    targets = {
        "14-facsimil.qmd": (ROOT / "publication/generated/14-facsimil.qmd").read_text(encoding="utf-8"),
        "15-transcripcion.qmd": (ROOT / "publication/generated/15-transcripcion.qmd").read_text(encoding="utf-8"),
        "16-edicion-modernizada.qmd": (ROOT / "publication/generated/16-edicion-modernizada.qmd").read_text(encoding="utf-8"),
    }
    for output in generated.values():
        for filename, anchor in re.findall(
            r"\((14-facsimil|15-transcripcion|16-edicion-modernizada)\.qmd#([a-z0-9-]+)\)",
            output,
        ):
            assert f"{{#{anchor}}}" in targets[f"{filename}.qmd"]
    glossary_output = generated["glosario.qmd"]
    for anchor in re.findall(r"\]\(#([a-z0-9-]+)\)", glossary_output):
        assert f"{{#{anchor} .unnumbered}}" in glossary_output


def test_apparatus_contains_no_local_or_project_file_links(generated):
    for name, output in generated.items():
        assert "/home/" not in output and "/tmp/" not in output, name
        assert not re.search(r"\]\([^)]*project/", output), name


def test_build_is_idempotent_and_owns_only_four_qmd_outputs(tmp_path):
    repository, publication = _isolated_tree(tmp_path)
    unrelated = publication / "generated/16-edicion-modernizada.qmd"
    unrelated.write_text("intacto", encoding="utf-8")
    first = builder.build_apparatus(repository, publication, MANUSCRIPT_NAME)
    first_hashes = _hashes(first)
    second = builder.build_apparatus(repository, publication, MANUSCRIPT_NAME)
    assert _hashes(second) == first_hashes
    assert tuple(path.name for path in first) == builder.OUTPUT_NAMES
    assert unrelated.read_text(encoding="utf-8") == "intacto"


def test_build_does_not_write_project_or_plugins(tmp_path):
    repository, publication = _isolated_tree(tmp_path)
    marker = repository / "plugins/marker.txt"
    marker.parent.mkdir(parents=True)
    marker.write_text("intacto", encoding="utf-8")
    protected = tuple(path for path in (repository / "project").rglob("*") if path.is_file())
    before = _hashes((*protected, marker))
    builder.build_apparatus(repository, publication, MANUSCRIPT_NAME)
    assert _hashes((*protected, marker)) == before


def test_navigation_integrates_only_the_four_phase4d_apparatus():
    quarto = yaml.safe_load((ROOT / "publication/_quarto.yml").read_text(encoding="utf-8"))
    chapters = yaml.safe_load(
        (ROOT / "publication/meta/chapters.yml").read_text(encoding="utf-8")
    )["chapters"]
    navigation = []
    for item in quarto["book"]["chapters"]:
        navigation.extend(item.get("chapters", []) if isinstance(item, dict) else [item])
    expected = [f"generated/{name}" for name in builder.OUTPUT_NAMES]
    assert navigation[17:21] == expected
    assert [item["path"] for item in chapters if item["path"] in expected] == expected
    assert len([item for item in navigation if "indices/" in item]) == 9


def test_all_four_outputs_declare_part_six_without_creating_numbered_chapters(generated):
    for output in generated.values():
        assert 'subtitle: "Parte VI. Aparatos e índices"' in output
        assert "numbered: false" in output
        assert "number-sections: false" in output
        assert not re.search(r"^title:", output, re.MULTILINE)
        assert re.search(r"^# .+ \{\.unnumbered\}$", output, re.MULTILINE)
        headings = re.findall(r"^#{2,3} .+$", output, re.MULTILINE)
        assert headings
        assert all(".unnumbered}" in heading for heading in headings)

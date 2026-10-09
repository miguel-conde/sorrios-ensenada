from __future__ import annotations

import hashlib
import re
import shutil
import sys
from pathlib import Path

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "publication" / "scripts"
sys.path.insert(0, str(SCRIPTS))

import build_modernized as builder  # noqa: E402
import critical_edition as critical  # noqa: E402
import fix_rendered_links as rendered_links  # noqa: E402
import modernized_edition as modernized  # noqa: E402
import validate_publication as validator  # noqa: E402


SOURCE = (
    ROOT
    / "project/30_RESULTADOS/EDICION_DIVULGATIVA/"
    "Catastro_Sorrios_1752_Version_Modernizada.md"
)
INTRODUCTION = (
    ROOT
    / "project/30_RESULTADOS/EDICION_DIVULGATIVA/"
    "Introduccion_Catastro_Ensenada_Sorrios.md"
)
VERIFICATION = (
    ROOT
    / "project/30_RESULTADOS/EDICION_DIVULGATIVA/"
    "Verificacion_Interrogatorio_40_Preguntas.md"
)
UNITS = ROOT / "project/00_CONTROL/unidades.yaml"


@pytest.fixture(scope="module")
def source_text() -> str:
    return SOURCE.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def edition(source_text) -> modernized.ModernizedEdition:
    return modernized.parse_modernized_edition(source_text)


@pytest.fixture(scope="module")
def specs() -> tuple[critical.UnitSpec, ...]:
    return critical.load_unit_specs(UNITS)


@pytest.fixture(scope="module")
def unit_anchors(specs) -> dict[str, str]:
    return {spec.label: critical.published_unit_anchor(spec) for spec in specs}


@pytest.fixture(scope="module")
def generated(edition, unit_anchors) -> str:
    return builder.modernized_qmd(edition, unit_anchors)


def _response_block(text: str, number: int) -> tuple[int, int, str]:
    start_match = re.search(rf"^## Respuesta {number}\. .+$", text, re.MULTILINE)
    assert start_match is not None
    end_match = re.search(r"^## ", text[start_match.end() :], re.MULTILINE)
    end = start_match.end() + end_match.start() if end_match else len(text)
    return start_match.start(), end, text[start_match.start() : end]


def _isolated_tree(tmp_path: Path) -> tuple[Path, Path]:
    repository = tmp_path / "repository"
    publication = repository / "publication"
    source_root = repository / "project/30_RESULTADOS/EDICION_DIVULGATIVA"
    source_root.mkdir(parents=True)
    control = repository / "project/00_CONTROL"
    control.mkdir(parents=True)
    shutil.copy2(SOURCE, source_root / SOURCE.name)
    shutil.copy2(INTRODUCTION, source_root / INTRODUCTION.name)
    shutil.copy2(VERIFICATION, source_root / VERIFICATION.name)
    shutil.copy2(UNITS, control / "unidades.yaml")
    (publication / "generated").mkdir(parents=True)
    return repository, publication


def _hashes(paths: tuple[Path, ...]) -> dict[str, str]:
    return {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}


def test_version_structure_and_complete_numbering(edition):
    assert edition.version == "1.3"
    assert len(edition.responses) == 40
    assert [response.number for response in edition.responses] == list(range(1, 41))
    assert len({response.number for response in edition.responses}) == 40
    assert len({response.title for response in edition.responses}) == 40


def test_fixed_documentary_blocks_are_present(edition):
    assert edition.portada.startswith("*(Portada)*")
    assert edition.comparecencia.startswith("*(Folios 306r–306v)*")
    assert "Todo lo cual dijeron ser verdad" in edition.ratification
    assert len(edition.concordance_rows) == 35
    assert len(edition.note_definitions) == 39
    assert edition.note_use.startswith("Para citar la forma exacta del manuscrito")


def test_every_response_has_one_question_one_local_response_and_folios(edition):
    assert all(response.question for response in edition.responses)
    assert all(response.response_label == modernized.RESPONSE_LABEL for response in edition.responses)
    assert all(response.folios.startswith("*(Folio") for response in edition.responses)
    assert all(response.body for response in edition.responses)


def test_questions_match_verified_list_one_to_one(edition):
    modernized.validate_verified_questions(
        edition,
        INTRODUCTION.read_text(encoding="utf-8"),
        VERIFICATION.read_text(encoding="utf-8"),
    )
    assert len(modernized.parse_verified_questions(INTRODUCTION.read_text(encoding="utf-8"))) == 40


def test_concordance_matches_all_canonical_units_in_order(edition, specs):
    modernized.validate_concordance_units(
        edition, tuple(spec.label for spec in specs)
    )
    assert edition.concordance_rows[0].unit_label == "Portada"
    assert edition.concordance_rows[-1].unit_label == "Hoja enfrentada posterior"


def test_missing_duplicate_and_reordered_responses_are_rejected(source_text):
    start_9, end_9, block_9 = _response_block(source_text, 9)
    missing = source_text[:start_9] + source_text[end_9:]
    with pytest.raises(modernized.ModernizedEditionError, match="Orden documental"):
        modernized.parse_modernized_edition(missing)
    duplicated = source_text[:end_9] + "\n" + block_9 + source_text[end_9:]
    with pytest.raises(modernized.ModernizedEditionError, match="duplicada"):
        modernized.parse_modernized_edition(duplicated)
    start_10, end_10, block_10 = _response_block(source_text, 10)
    reordered = (
        source_text[:start_9]
        + block_10
        + "\n"
        + block_9
        + source_text[end_10:]
    )
    with pytest.raises(modernized.ModernizedEditionError, match="Orden documental"):
        modernized.parse_modernized_edition(reordered)


def test_missing_question_is_rejected_actionably(source_text):
    mutated = source_text.replace(
        "**Pregunta 17 del interrogatorio de 1749 —grafía modernizada—**",
        "Pregunta eliminada",
        1,
    )
    with pytest.raises(modernized.ModernizedEditionError, match="Respuesta 17.*una pregunta"):
        modernized.parse_modernized_edition(mutated)


def test_shifted_question_is_rejected_by_external_correspondence(source_text):
    edition = modernized.parse_modernized_edition(source_text)
    first = edition.responses[0].question
    second = edition.responses[1].question
    mutated = source_text.replace(first, "__TEMP_QUESTION__", 1)
    mutated = mutated.replace(second, first, 1).replace("__TEMP_QUESTION__", second, 1)
    shifted = modernized.parse_modernized_edition(mutated)
    with pytest.raises(modernized.ModernizedEditionError, match="Pregunta 1 desplazada"):
        modernized.validate_verified_questions(
            shifted,
            INTRODUCTION.read_text(encoding="utf-8"),
            VERIFICATION.read_text(encoding="utf-8"),
        )


def test_version_and_required_closing_sections_are_rejected_when_mutated(source_text):
    with pytest.raises(modernized.ModernizedEditionError, match="Versión modernizada incorrecta"):
        modernized.parse_modernized_edition(source_text.replace("**Versión:** 1.3", "**Versión:** 1.2", 1))
    for heading in ("Ratificación, edades y firmas", "Concordancia material", "Nota de uso"):
        mutated = source_text.replace(f"## {heading}", f"## Falta {heading}", 1)
        with pytest.raises(modernized.ModernizedEditionError, match="Orden documental"):
            modernized.parse_modernized_edition(mutated)


def test_numeric_and_semantic_footnotes_are_complete_and_not_orphaned(edition):
    assert set(map(str, range(1, 36))).issubset(edition.note_definitions)
    assert {"bega-vega", "administrarse", "avitadores", "renta-venta"}.issubset(
        edition.note_definitions
    )
    assert set(edition.note_calls) == set(edition.note_definitions)


def test_broken_missing_and_orphaned_notes_are_rejected(source_text):
    undefined = source_text.replace("[^avitadores]", "[^sin-definir]", 1)
    with pytest.raises(modernized.ModernizedEditionError, match="sin definición"):
        modernized.parse_modernized_edition(undefined)
    orphaned = source_text.replace("[^avitadores]", "", 1)
    with pytest.raises(modernized.ModernizedEditionError, match="nunca referidas"):
        modernized.parse_modernized_edition(orphaned)


def test_generated_chapter_has_all_stable_unique_anchors(generated):
    anchors = re.findall(r"^## .+ \{#([^}]+)\}$", generated, re.MULTILINE)
    expected = [
        "modernizada-portada",
        "comparecencia",
        *(f"respuesta-{number}" for number in range(1, 41)),
        "ratificacion-edades-firmas",
        "concordancia-material",
        "notas",
        "nota-de-uso",
    ]
    assert anchors == expected
    assert len(anchors) == len(set(anchors)) == 46


def test_generated_fidelity_gate_accepts_exact_output(edition, generated, unit_anchors):
    builder.validate_generated_fidelity(edition, generated, unit_anchors)


@pytest.mark.parametrize(
    ("original", "replacement", "message"),
    [
        ("dos mil quinientas varas", "dos mil seiscientas varas", "Respuesta 3"),
        ("*(Folios 315r–316r)*", "*(Folio 315v)*", "Respuesta 17"),
        ("dado a renta[^modernizada-26]", "dado en renta[^modernizada-26]", "Respuesta 20"),
        ("«avitadores».[^modernizada-avitadores]", "habitantes", "Respuesta 21"),
        ("«venta»[^modernizada-renta-venta]", "«renta»[^modernizada-renta-venta]", "Respuesta 40"),
    ],
)
def test_fidelity_gate_reports_response_and_difference(
    edition, generated, unit_anchors, original, replacement, message
):
    mutated = generated.replace(original, replacement, 1)
    with pytest.raises(builder.ModernizedBuildError, match=message):
        builder.validate_generated_fidelity(edition, mutated, unit_anchors)


def test_response_17_matches_source_and_accepted_prototype(edition, generated):
    response = edition.responses[16]
    prototype = (ROOT / "publication/generated/16-modernizada-prototipo.qmd").read_text(
        encoding="utf-8"
    )
    assert response.question in prototype
    assert response.body in prototype
    assert "[^20]:" in prototype and "[^21]:" in prototype
    assert response.question in generated
    assert builder._namespace_notes(response.body) in generated


def test_response_21_preserves_avitadores_caution(edition, generated):
    response = edition.responses[20]
    assert "«avitadores».[^avitadores]" in response.body
    assert "población total" in edition.notes
    assert "«avitadores».[^modernizada-avitadores]" in generated


def test_response_40_preserves_renta_question_and_venta_answer(edition, generated):
    response = edition.responses[39]
    assert "finca o renta" in response.question
    assert "«venta»[^renta-venta]" in response.body
    assert "pregunta 40 del interrogatorio general dice «finca o renta»" in edition.notes
    assert "«venta»[^modernizada-renta-venta]" in generated


def test_historical_measures_laguna_variants_and_categories_remain(generated):
    for marker in (
        "Sorribos",
        "Bega,[^modernizada-bega-vega]",
        "Manuel Antonio de Vega",
        "en este pueblo […] medida de tierra",
        "cuartal",
        "fanega",
        "celemín",
        "libra",
        "cargas",
        "dado a renta[^modernizada-26]",
        "medios vecinos",
        "hijos de familia",
        "pobres de solemnidad",
    ):
        assert marker in generated


def test_navigation_to_chapter_15_is_derived_for_every_response(edition, generated):
    mapping = modernized.response_unit_labels(edition)
    assert len(mapping) == 40
    assert mapping[17] == ("Folio 315r", "Folio 315v", "Folio 316r")
    assert generated.count("**Unidades materiales en el capítulo 15:**") == 40
    assert "15-transcripcion.qmd#folio-315v" in generated


def test_related_documents_become_book_navigation_without_internal_links(generated):
    assert "source-related-documents: replaced_by_book_navigation" in generated
    assert "## Documentos relacionados" not in generated
    assert "](./" not in generated
    assert "](../../" not in generated


def test_post_render_replaces_4c_prototype_and_links_real_apparatus(tmp_path):
    html = tmp_path / "chapter.html"
    html.write_text(
        '<a href="../../generated/16-modernizada-prototipo.qmd#respuesta-17">'
        "respuesta 17 modernizada</a> y el "
        '<a href="../../generated/aparato-molinos.qmd#matriz-molinera">'
        "aparato D/C/I/E/L</a>",
        encoding="utf-8",
    )
    assert rendered_links.fix_rendered_links(tmp_path) == 2
    updated = html.read_text(encoding="utf-8")
    assert "16-edicion-modernizada.html#respuesta-17" in updated
    assert "matriz-evidencia.html#evidencia-hid-001" in updated
    assert ".qmd#" not in updated


def test_real_chapter_is_the_only_visible_chapter_16_and_prototype_is_regression():
    quarto = yaml.safe_load((ROOT / "publication/_quarto.yml").read_text(encoding="utf-8"))
    navigation = validator._navigation_paths(quarto["book"]["chapters"])
    assert navigation.count("generated/16-edicion-modernizada.qmd") == 1
    assert "generated/16-modernizada-prototipo.qmd" not in navigation
    assert "generated/aparato-molinos.qmd" not in navigation
    chapters = yaml.safe_load(
        (ROOT / "publication/meta/chapters.yml").read_text(encoding="utf-8")
    )["chapters"]
    assert sum(item["path"] == "generated/16-edicion-modernizada.qmd" for item in chapters) == 1
    prototype = next(
        item for item in chapters if item["path"] == "generated/16-modernizada-prototipo.qmd"
    )
    assert prototype["publication_status"] == "prototype"


def test_build_is_idempotent_and_owns_only_the_real_4c_output(tmp_path):
    repository, publication = _isolated_tree(tmp_path)
    older = publication / "generated/15-transcripcion.qmd"
    newer = publication / "generated/16-modernizada-prototipo.qmd"
    older.write_text("4B intacta", encoding="utf-8")
    newer.write_text("prototipo intacto", encoding="utf-8")
    first = builder.build_modernized(repository, publication)
    first_hash = _hashes(first)
    second = builder.build_modernized(repository, publication)
    assert _hashes(second) == first_hash
    assert older.read_text(encoding="utf-8") == "4B intacta"
    assert newer.read_text(encoding="utf-8") == "prototipo intacto"
    assert first == (publication.resolve() / "generated/16-edicion-modernizada.qmd",)


def test_build_does_not_write_project_or_plugins(tmp_path):
    repository, publication = _isolated_tree(tmp_path)
    plugin_marker = repository / "plugins/marker.txt"
    plugin_marker.parent.mkdir(parents=True)
    plugin_marker.write_text("intacto", encoding="utf-8")
    protected = tuple(path for path in (repository / "project").rglob("*") if path.is_file())
    before = _hashes((*protected, plugin_marker))
    builder.build_modernized(repository, publication)
    assert _hashes((*protected, plugin_marker)) == before


def test_generated_output_contains_no_absolute_paths_or_timestamps(generated):
    assert "/home/" not in generated
    assert "/tmp/" not in generated
    assert not re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:", generated)


def test_fidelity_gate_rejects_added_or_removed_sections(edition, generated, unit_anchors):
    removed = generated.replace("## Nota de uso {#nota-de-uso}", "", 1)
    with pytest.raises(builder.ModernizedBuildError, match="orden documental"):
        builder.validate_generated_fidelity(edition, removed, unit_anchors)
    added = generated + "\n## Sección inventada {#inventada}\n\nContenido.\n"
    with pytest.raises(builder.ModernizedBuildError, match="orden documental"):
        builder.validate_generated_fidelity(edition, added, unit_anchors)

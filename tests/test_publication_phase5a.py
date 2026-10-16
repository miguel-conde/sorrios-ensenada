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

import build_indexes as builder  # noqa: E402
import critical_edition as critical  # noqa: E402
import index_sources as sources  # noqa: E402


PUBLICATION = ROOT / "publication"
UNITS = ROOT / builder.UNITS_SOURCE


@pytest.fixture(scope="module")
def specs() -> tuple[critical.UnitSpec, ...]:
    return critical.load_unit_specs(UNITS)


@pytest.fixture(scope="module")
def data() -> builder.IndexData:
    return builder.load_index_data(ROOT, PUBLICATION)


@pytest.fixture(scope="module")
def generated(data) -> dict[str, str]:
    return builder.generated_indexes(data)


def _isolated_tree(tmp_path: Path) -> tuple[Path, Path]:
    repository = tmp_path / "repository"
    publication = repository / "publication"
    for relative in (
        *sources.LIVE_INDEX_SOURCES.values(),
        builder.UNITS_SOURCE,
        builder.MODERNIZED_SOURCE,
    ):
        destination = repository / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / relative, destination)
    shutil.copytree(PUBLICATION / "content", publication / "content")
    (publication / "meta").mkdir(parents=True)
    shutil.copy2(PUBLICATION / "meta/indexes.yml", publication / "meta/indexes.yml")
    shutil.copy2(PUBLICATION / "meta/chapters.yml", publication / "meta/chapters.yml")
    return repository, publication


def _hashes(paths: tuple[Path, ...]) -> dict[str, str]:
    return {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}


def test_five_live_indexes_are_complete_unique_and_unit_resolved(data):
    assert tuple(index.index_id for index in data.live) == (
        "onomastico",
        "toponimos",
        "instituciones",
        "oficios",
        "medidas",
    )
    assert tuple(len(index.entries) for index in data.live) == (21, 9, 7, 12, 12)
    for index in data.live:
        assert len({entry.term.casefold() for entry in index.entries}) == len(index.entries)
        assert all(entry.units for entry in index.entries)


def test_live_parser_preserves_variants_security_and_cross_references(data):
    people = {entry.term: entry for entry in data.live[0].entries}
    toponyms = {entry.term: entry for entry in data.live[1].entries}
    assert "De Vega" in people["Manuel Ant[oni]o De Bega"].fields["Variantes"]
    assert people["Conde De Luna"].fields["Grado de seguridad"].startswith("alto")
    assert "Señorío" in people["Conde De Luna"].fields["Referencias cruzadas"]
    assert toponyms["Tapia"].fields["Grado de seguridad"].startswith("medio-alto")
    assert "Sorribas" not in toponyms["Sorribos"].fields.get("Variantes", "")


def test_live_parser_rejects_duplicate_entry_and_unknown_unit(specs):
    path = ROOT / sources.LIVE_INDEX_SOURCES["oficios"]
    text = path.read_text(encoding="utf-8")
    duplicate = text + "\n" + text.split("### abogado", 1)[1].join(("### abogado", ""))
    with pytest.raises(sources.IndexSourceError, match="duplicad"):
        sources.parse_live_index(
            duplicate,
            "oficios",
            tuple(spec.label for spec in specs),
            source="fixture.md",
        )
    unknown = text.replace("- **Unidades:** folio 306r.", "- **Unidades:** folio 999r.", 1)
    with pytest.raises(sources.IndexSourceError, match="unidades inexistentes"):
        sources.parse_live_index(
            unknown,
            "oficios",
            tuple(spec.label for spec in specs),
            source="fixture.md",
        )


def test_sort_key_is_deterministic_accent_insensitive_and_keeps_visible_form():
    assert sources.sort_key("Árbol") == "arbol"
    assert sources.sort_key("D[o]n Manuel") == "don manuel"
    values = ("Yerba", "Árbol", "Boto")
    assert sorted(values, key=sources.sort_key) == ["Árbol", "Boto", "Yerba"]


def test_indexes_yml_contains_only_6_7_9_with_valid_counts_and_categories(data):
    assert tuple(index.index_id for index in data.editorial) == sources.EDITORIAL_INDEX_IDS
    assert tuple(index.order for index in data.editorial) == (6, 7, 9)
    assert tuple(len(index.entries) for index in data.editorial) == (27, 15, 21)
    for index in data.editorial:
        assert all(entry.category in sources.ALLOWED_CATEGORIES[index.index_id] for entry in index.entries)
        assert len({entry.entry_id for entry in index.entries}) == len(index.entries)
        assert len({entry.term.casefold() for entry in index.entries}) == len(index.entries)


def test_indexes_yml_uses_only_structured_existing_targets(data):
    for index in data.editorial:
        for entry in index.entries:
            assert entry.targets
            assert all(target.kind == "section" for target in entry.targets)
            assert all(target.anchor and "#" in target.html_path for target in entry.targets)


def test_indexes_yml_has_no_manual_pdf_pages_or_local_paths():
    text = (PUBLICATION / "meta/indexes.yml").read_text(encoding="utf-8")
    assert not re.search(r"(?:^|_)pdf_?pages?\s*:", text, re.MULTILINE | re.IGNORECASE)
    assert not re.search(r"^\s*pages?\s*:", text, re.MULTILINE | re.IGNORECASE)
    assert "/home/" not in text and "/tmp/" not in text


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (("anchor: recursos-colmenas", "anchor: ancla-inexistente"), "ancla inexistente"),
        (("chapter: rio-molinos-recursos", "chapter: capitulo-inexistente"), "capítulo inexistente"),
        (("category: animal", "category: categoria-inventada"), "categoría no válida"),
        (("targets:", "pdf_page: 12\n        targets:"), "páginas PDF manuales"),
        (
            (
                "{type: section, chapter: rio-molinos-recursos, anchor: recursos-colmenas}",
                "{type: unit, unit: folio_999r}",
            ),
            "unidad inexistente",
        ),
        (
            (
                "{type: section, chapter: rio-molinos-recursos, anchor: recursos-colmenas}",
                "{type: response, response: 999}",
            ),
            "respuesta inexistente",
        ),
    ],
)
def test_indexes_yml_rejects_invalid_metadata(tmp_path, mutation, message):
    _, publication = _isolated_tree(tmp_path)
    path = publication / "meta/indexes.yml"
    path.write_text(
        path.read_text(encoding="utf-8").replace(*mutation, 1),
        encoding="utf-8",
    )
    with pytest.raises(sources.IndexSourceError, match=message):
        sources.load_editorial_indexes(publication)


def test_indexes_yml_rejects_invalid_remission(tmp_path):
    _, publication = _isolated_tree(tmp_path)
    path = publication / "meta/indexes.yml"
    text = path.read_text(encoding="utf-8").replace(
        "see_also: [rio, molinos]", "see_also: [entrada-inexistente]", 1
    )
    path.write_text(text, encoding="utf-8")
    with pytest.raises(sources.IndexSourceError, match="remisiones inexistentes"):
        sources.load_editorial_indexes(publication)


def test_response_index_is_derived_and_exactly_1_to_40(data, generated):
    entries = sources.response_index_entries(data.modernized)
    assert len(entries) == 40
    assert [locator.key for _, locator in entries] == [str(number) for number in range(1, 41)]
    output = generated[builder.OUTPUT_NAMES[7]]
    assert output.count("Pregunta/Respuesta ") == 40
    assert output.count("../16-edicion-modernizada.qmd#respuesta-") == 40
    assert "Pregunta/Respuesta 17 — Minas, molinos y otros artefactos" in output


def test_exactly_nine_outputs_in_plan_order_with_correct_titles(data, generated):
    assert tuple(generated) == builder.OUTPUT_NAMES
    assert len(generated) == 9
    for name, expected_title in zip(builder.OUTPUT_NAMES, builder.INDEX_TITLES.values(), strict=True):
        assert f'# {expected_title} {{.unnumbered}}' in generated[name]
        assert not re.search(r"^title:", generated[name], re.MULTILINE)
    assert builder.index_entry_counts(data) == (21, 9, 7, 12, 12, 27, 15, 40, 21)


def test_all_index_anchors_are_unique_and_ordering_is_reproducible(generated):
    anchors = [
        anchor
        for output in generated.values()
        for anchor in re.findall(r"\{#(indice-[a-z0-9-]+)", output)
    ]
    assert len(anchors) == len(set(anchors))
    for output in generated.values():
        terms = re.findall(r"^\*\*(.+)\*\*$", output, re.MULTILINE)
        if "preguntas-respuestas" not in output.split("chapter-id:", 1)[1].splitlines()[0]:
            assert terms == sorted(terms, key=sources.sort_key)


def test_variants_are_not_duplicate_entries_and_cautions_are_preserved(generated):
    people = generated[builder.OUTPUT_NAMES[0]]
    places = generated[builder.OUTPUT_NAMES[1]]
    measures = generated[builder.OUTPUT_NAMES[4]]
    assert people.count("**Manuel Ant[oni]o De Bega**") == 1
    assert "De Vega" in people
    assert "medio-alto" in places
    assert "Sorribas" in places and "error paleográfico" in places
    assert "no se fija equivalencia moderna" in measures


def test_html_and_pdf_locators_share_one_anchor_relation(generated):
    for output in generated.values():
        html_anchors = re.findall(r"\.qmd#([a-z0-9-]+)\)", output)
        pdf_anchors = re.findall(r"\\hyperref\[([a-z0-9-]+)\]", output)
        assert sorted(set(html_anchors)) == sorted(set(pdf_anchors))
        assert "{=latex}" in output
        assert "when-format=\"html\"" in output
        assert "when-format=\"pdf\"" in output
    assert "\\getpagerefnumber" in generated[builder.OUTPUT_NAMES[8]]


def test_pdf_page_resolution_fixture_changes_with_pagination(data):
    entry = data.editorial[0].entries[7]  # Centeno, three real section targets.
    first = {target.anchor: str(index + 10) for index, target in enumerate(entry.targets)}
    second = dict(first)
    second[entry.targets[0].anchor] = "99"
    assert sources.resolve_pdf_pages(entry.targets, first) != sources.resolve_pdf_pages(
        entry.targets, second
    )
    with pytest.raises(sources.IndexSourceError, match="no produjo página"):
        sources.resolve_pdf_pages(entry.targets, {})


def test_pdf_locators_are_latex_native_not_ocr_or_absolute_paths(generated):
    joined = "\n".join(generated.values())
    assert "\\pageref*{" in joined
    assert "ocr" not in joined.casefold()
    assert "/home/" not in joined and "/tmp/" not in joined
    assert not re.search(r"\*\*Páginas:\*\*\s+\d", joined)


def test_build_is_idempotent_and_owns_only_nine_qmd_outputs(tmp_path):
    repository, publication = _isolated_tree(tmp_path)
    unrelated = publication / "generated/glosario.qmd"
    unrelated.parent.mkdir(parents=True, exist_ok=True)
    unrelated.write_text("intacto", encoding="utf-8")
    first = builder.build_indexes(repository, publication)
    first_hashes = _hashes(first)
    second = builder.build_indexes(repository, publication)
    assert _hashes(second) == first_hashes
    assert tuple(path.name for path in first) == builder.OUTPUT_NAMES
    assert unrelated.read_text(encoding="utf-8") == "intacto"


def test_navigation_integrates_exactly_nine_indexes_after_phase4d():
    quarto = yaml.safe_load((PUBLICATION / "_quarto.yml").read_text(encoding="utf-8"))
    navigation = []
    for item in quarto["book"]["chapters"]:
        navigation.extend(item.get("chapters", []) if isinstance(item, dict) else [item])
    expected = [f"generated/indices/{name}" for name in builder.OUTPUT_NAMES]
    assert navigation[-10:-1] == expected
    assert navigation[-1] == "content/06-aparatos/colofon.qmd"
    assert navigation[-15] == "generated/matriz-evidencia.qmd"
    chapters = yaml.safe_load(
        (PUBLICATION / "meta/chapters.yml").read_text(encoding="utf-8")
    )["chapters"]
    assert [item["path"] for item in chapters if item["path"] in expected] == expected


def test_generated_indexes_have_accessible_native_structure(generated):
    for output in generated.values():
        assert "numbered: false" in output
        assert "number-sections: false" in output
        assert "<img" not in output and "|---" not in output
        assert re.search(r"^## .+ \{#.+ \.unnumbered\}$", output, re.MULTILINE) or (
            "indice-preguntas-respuestas" in output
        )

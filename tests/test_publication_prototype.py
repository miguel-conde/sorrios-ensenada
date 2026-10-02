from pathlib import Path
import re
import sys

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "publication" / "scripts"
sys.path.insert(0, str(SCRIPTS))

import build_vertical_prototype as prototype  # noqa: E402
import prepare as preparation  # noqa: E402
import validate_publication as validator  # noqa: E402


EXPECTED_EVIDENCE = {
    "D": ("HID-001", "HID-003", "HID-005", "HID-006"),
    "C": ("HID-002", "HID-004", "CAL-012", "CAL-013"),
    "I": ("HID-007", "INT-005"),
    "E": ("HID-008",),
    "L": ("LIM-005", "LIM-010"),
}

CHAPTER_ONE_SOURCES = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Introduccion_Catastro_Ensenada_Sorrios.md",
    "project/00_CONTROL/Manual_Editorial.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
}
CHAPTER_TWO_SOURCES = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Introduccion_Catastro_Ensenada_Sorrios.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Verificacion_Interrogatorio_40_Preguntas.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/00_CONTROL/Manual_Editorial.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
}

CHAPTER_THREE_SOURCES = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Introduccion_Catastro_Ensenada_Sorrios.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/00_CONTROL/unidades.yaml",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
}
CHAPTER_THREE_EVIDENCE = {
    "D": ("JUR-001", "JUR-002", "JUR-003", "JUR-004", "TOP-001"),
    "I": ("TOP-002",),
    "E": (
        "TOP-004", "TOP-005", "TOP-007", "TOP-008", "TOP-009",
        "TOP-010", "TOP-011", "JUR-009",
    ),
}
CHAPTER_FOUR_SOURCES = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Introduccion_Catastro_Ensenada_Sorrios.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/00_CONTROL/unidades.yaml",
    "project/00_CONTROL/Manual_Editorial.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Criterios_Edicion_Modernizada.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "docs/PLAN_MAESTRO_PUBLICACION_QUARTO.md",
    "publication/README.md",
}
AUTHORIZED_INSTITUTIONAL_LINKS = {
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=10",
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=32",
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=33",
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=40",
    "https://www.catastro.hacienda.gob.es/es-ES/fondo_editorial.html",
}
CHAPTER_TWO_LINKS = {
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=30",
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=31b",
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=32",
    "https://www.catastro.hacienda.gob.es/documentos/publicaciones/catalogoensenada_1752_vera.pdf",
}


def read_front_matter(path: Path) -> dict:
    return validator._front_matter_and_body(path)[0]


def replace_once(text: str, pattern: str, replacement: str) -> str:
    mutated, count = re.subn(pattern, replacement, text, count=1, flags=re.IGNORECASE)
    assert count == 1, f"La mutación no encontró su objetivo: {pattern}"
    return mutated


def replace_section(text: str, anchor: str, replacement: str) -> str:
    pattern = rf"(^##[^\n]*\{{#{re.escape(anchor)}\}}[^\n]*\n).*?(?=^##\s+|\Z)"
    mutated, count = re.subn(
        pattern,
        rf"\1\n{replacement}\n\n",
        text,
        count=1,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )
    assert count == 1, f"La mutación no encontró la sección: {anchor}"
    return mutated


def error_codes(errors: list[str]) -> set[str]:
    return {error.partition(":")[0] for error in errors}


def test_vertical_sample_is_strictly_fixed():
    assert prototype.PROTOTYPE_PAGE == 12
    assert prototype.PROTOTYPE_UNIT == "folio_315v"
    assert prototype.PROTOTYPE_RESPONSE == 17
    assert prototype.EVIDENCE_GROUPS == EXPECTED_EVIDENCE


def test_all_prototype_evidence_exists_in_register_1_2():
    register = (
        ROOT
        / "project"
        / "30_RESULTADOS"
        / "ESTUDIO_HISTORICO"
        / "Registro_Afirmaciones_Calculos_v1.md"
    ).read_text(encoding="utf-8")
    rows = prototype.read_evidence_rows(register)
    assert set(rows) == {
        identifier for identifiers in EXPECTED_EVIDENCE.values() for identifier in identifiers
    }


def test_editorial_chapter_declares_required_metadata():
    metadata = read_front_matter(
        ROOT
        / "publication"
        / "content"
        / "02-estudio"
        / "09-rio-molinos-recursos.qmd"
    )
    assert metadata["chapter-id"] == "rio-molinos-recursos"
    assert metadata["publication-status"] == "prototype"
    assert metadata["sources"]
    assert {
        level: tuple(values) for level, values in metadata["evidence"].items()
    } == EXPECTED_EVIDENCE


def test_chapter_one_has_bounded_metadata_and_provenance():
    path = (
        ROOT
        / "publication"
        / "content"
        / "01-catastro"
        / "01-catastro-ensenada.qmd"
    )
    metadata = read_front_matter(path)
    text = path.read_text(encoding="utf-8")
    links = set(re.findall(r"\]\((https://[^)]+)\)", text))

    assert metadata["title"] == "El Catastro de Ensenada"
    assert metadata["chapter-id"] == "catastro-ensenada"
    assert metadata["publication-status"] == "development"
    assert {source["path"] for source in metadata["sources"]} == CHAPTER_ONE_SOURCES
    assert all(source["locator"] for source in metadata["sources"])
    assert "evidence" not in metadata
    assert links == AUTHORIZED_INSTITUTIONAL_LINKS


def test_chapter_two_has_bounded_metadata_structure_and_provenance():
    path = (
        ROOT
        / "publication"
        / "content"
        / "01-catastro"
        / "02-respuestas-generales-interrogatorio.qmd"
    )
    metadata = read_front_matter(path)
    text = path.read_text(encoding="utf-8")
    links = set(re.findall(r"\]\((https://[^)]+)\)", text))

    assert (
        metadata["title"]
        == "Las Respuestas Generales y el interrogatorio de cuarenta preguntas"
    )
    assert metadata["chapter-id"] == "respuestas-generales-interrogatorio"
    assert metadata["publication-status"] == "development"
    assert {source["path"] for source in metadata["sources"]} == CHAPTER_TWO_SOURCES
    assert len(metadata["sources"]) == len(CHAPTER_TWO_SOURCES)
    assert all(source["locator"] for source in metadata["sources"])
    assert "evidence" not in metadata
    assert links == CHAPTER_TWO_LINKS
    for question_range, subject in validator.CHAPTER_TWO_THEMATIC_BLOCKS:
        assert f"| {question_range} | {subject} |" in text


def test_chapter_two_explains_question_29_without_duplicating_the_questionnaire():
    text = (
        ROOT
        / "publication"
        / "content"
        / "01-catastro"
        / "02-respuestas-generales-interrogatorio.qmd"
    ).read_text(encoding="utf-8")
    normalized = re.sub(r"\s+", " ", text).casefold()

    for phrase in (
        "pregunta 29",
        "hay en la población",
        "transmisión moderna",
        "titularidad",
        "utilidad anual",
        "formulario externo",
        "lectura paleográfica local",
    ):
        assert phrase.casefold() in normalized
    assert not validator._has_extensive_questionnaire_sequence(text)


def test_chapter_three_has_controlled_provenance_and_registered_evidence():
    path = ROOT / "publication/content/01-catastro/03-expediente-sorribos-santibanez.qmd"
    metadata = read_front_matter(path)
    register = (
        ROOT / "project/30_RESULTADOS/ESTUDIO_HISTORICO"
        / "Registro_Afirmaciones_Calculos_v1.md"
    ).read_text(encoding="utf-8")
    registered = set(re.findall(r"^\|\s*([A-Z]+-\d{3})\s*\|", register, re.MULTILINE))

    assert metadata["title"] == "El expediente de Sorribos y Santibáñez de Ordás"
    assert metadata["chapter-id"] == "expediente-sorribos-santibanez"
    assert metadata["publication-status"] == "development"
    assert {source["path"] for source in metadata["sources"]} == CHAPTER_THREE_SOURCES
    assert len(metadata["sources"]) == len(CHAPTER_THREE_SOURCES)
    assert all(source["locator"] for source in metadata["sources"])
    evidence = {level: tuple(values) for level, values in metadata["evidence"].items()}
    assert evidence == CHAPTER_THREE_EVIDENCE
    assert {item for group in evidence.values() for item in group} <= registered


def test_chapter_three_preserves_facts_toponym_limits_and_scope():
    path = ROOT / "publication/content/01-catastro/03-expediente-sorribos-santibanez.qmd"
    _, body = validator._front_matter_and_body(path)
    normalized = re.sub(r"\s+", " ", body).casefold()

    required = (
        "17 de septiembre de 1752", "joaquín aguado", "manuel antonio de bega",
        "juan álvarez", "remirio rodríguez", "domingo díez",
        "francisco de llorca", "domingo suárez", "manuel antonio alonso",
        "excepto el cura", "18 páginas digitales", "35 unidades documentales",
        "cuarenta respuestas", "dos rúbricas gráficas inferiores",
        "69 años", "49 años", "59 años", "52 años", "44 años",
    )
    assert all(phrase in normalized for phrase in required)
    assert all(form in body for form in ("Sorribios", "Sorribos", "Sorrios"))
    assert "sorribas" not in normalized
    assert "(04-manuscrito-volumen-actual.qmd)" in body
    assert "publication/generated/" not in body
    assert not re.search(r"<[A-Za-z][^>]*>", body)
    assert validator._validate_chapter_three_body(body) == []


def test_chapter_four_separates_editorial_layers_and_provenance():
    path = ROOT / "publication/content/01-catastro/04-manuscrito-volumen-actual.qmd"
    metadata, body = validator._front_matter_and_body(path)
    normalized = re.sub(r"\s+", " ", body).casefold()

    assert metadata["title"] == "Del manuscrito al volumen actual"
    assert metadata["chapter-id"] == "manuscrito-volumen-actual"
    assert metadata["publication-status"] == "development"
    assert {source["path"] for source in metadata["sources"]} == CHAPTER_FOUR_SOURCES
    assert len(metadata["sources"]) == len(CHAPTER_FOUR_SOURCES)
    assert all(source["locator"] for source in metadata["sources"])
    assert "evidence" not in metadata
    required = (
        "pdf manuscrito autoritativo", "18 páginas digitales",
        "35 unidades documentales", "facsímil",
        "transcripción paleográfica semidiplomática", "edición crítica 3.6",
        "edición modernizada 1.3", "preguntas externas", "respuestas locales",
        "estudio histórico 1.2", "registro 1.2", "front matter",
        "libro quarto", "publication/content/", "publication/generated/", "referencia editorial",
        "no es una autoridad textual", "permanece fuera de github",
    )
    assert all(phrase in normalized for phrase in required)
    assert all(heading.casefold() in normalized for heading in validator.UNIT_HEADINGS)
    assert all(
        level in normalized
        for level in ("d — dato", "c — cálculo", "i — interpretación",
                      "e — contexto", "l — límite")
    )
    assert "(03-expediente-sorribos-santibanez.qmd)" in body
    assert not any(name in body for name in ("Joaquín Aguado", "Remirio Rodríguez"))
    assert not re.search(r"(?:/home/|/tmp/|[A-Za-z]:\\\\)", body)
    assert "base64" not in normalized
    assert not re.search(r"<[A-Za-z][^>]*>", body)
    assert validator._validate_chapter_four_body(body) == []


@pytest.mark.parametrize(
    ("document", "message"),
    (
        ("Texto sin cabecera", "no comienza con front matter"),
        ("---\ntitle: incompleto\nTexto", "sin delimitador de cierre"),
        ("---\ntitle: [\n---\nTexto", "YAML inválido"),
    ),
)
def test_document_parser_rejects_missing_incomplete_or_invalid_front_matter(
    document, message
):
    with pytest.raises(ValueError, match=message):
        validator._parse_document(document, "mutacion.qmd")


def test_relation_segmentation_keeps_colon_context_and_splits_semicolon_clauses():
    paragraphs = validator._controlled_paragraphs(
        "Son indistinguibles: facsímil y transcripción.\n\n"
        "publication/content/ contiene texto editorial; "
        "publication/generated/ contiene derivados."
    )

    assert paragraphs[0][1] == (
        "son indistinguibles: facsímil y transcripción.",
    )
    assert paragraphs[1][1] == (
        "publication/content/ contiene texto editorial",
        "publication/generated/ contiene derivados.",
    )


def test_chapter_three_cautions_in_front_matter_do_not_satisfy_body_validation():
    path = ROOT / "publication/content/01-catastro/03-expediente-sorribos-santibanez.qmd"
    _, body = validator._front_matter_and_body(path)
    body = replace_once(
        body,
        r"no\s+demuestra\s+continuidad\s+económica\s+automática\s+hasta\s+1752",
        "describe una transmisión patrimonial determinada",
    )
    body = replace_once(
        body,
        r"no\s+proporciona\s+una\s+secuencia\s+fonética\s+completa",
        "documenta varios estados del nombre",
    )
    document = (
        "---\n"
        "audit-carrier: >-\n"
        "  no demuestra continuidad económica automática hasta 1752;\n"
        "  no proporciona una secuencia fonética completa\n"
        "---\n"
        f"{body}"
    )
    _, parsed_body = validator._parse_document(document, "mutacion.qmd")

    assert error_codes(validator._validate_chapter_three_body(parsed_body)) >= {
        "C3_PHONETIC_LIMIT",
        "C3_PATRIMONIAL_LIMIT",
    }


def test_chapter_three_rejects_missing_phonetic_limit():
    path = ROOT / "publication/content/01-catastro/03-expediente-sorribos-santibanez.qmd"
    _, body = validator._front_matter_and_body(path)
    mutated = replace_once(
        body,
        r"no\s+proporciona\s+una\s+secuencia\s+fonética\s+completa",
        "documenta varios estados del nombre",
    )

    assert "C3_PHONETIC_LIMIT" in error_codes(
        validator._validate_chapter_three_body(mutated)
    )


def test_chapter_three_rejects_missing_economic_continuity_limit():
    path = ROOT / "publication/content/01-catastro/03-expediente-sorribos-santibanez.qmd"
    _, body = validator._front_matter_and_body(path)
    mutated = replace_once(
        body,
        r"no\s+demuestra\s+continuidad\s+económica\s+automática\s+hasta\s+1752",
        "describe una transmisión patrimonial determinada",
    )

    assert "C3_PATRIMONIAL_LIMIT" in error_codes(
        validator._validate_chapter_three_body(mutated)
    )


@pytest.mark.parametrize(
    "statement",
    (
        "Una secuencia fonética completa sí existe.",
        "Existe una secuencia fonética completa.",
    ),
)
def test_chapter_three_rejects_positive_complete_phonetic_sequence(statement):
    path = ROOT / "publication/content/01-catastro/03-expediente-sorribos-santibanez.qmd"
    _, body = validator._front_matter_and_body(path)
    mutated = replace_once(
        body,
        r"no\s+proporciona\s+una\s+secuencia\s+fonética\s+completa",
        "no proporciona una secuencia fonética completa. " + statement,
    )

    assert error_codes(validator._validate_chapter_three_body(mutated)) == {
        "C3_PHONETIC_REVERSAL"
    }


@pytest.mark.parametrize(
    "statement",
    (
        "Entre 1267 y 1752 está demostrada la continuidad económica.",
        "Está probada la continuidad económica desde 1267 hasta 1752.",
    ),
)
def test_chapter_three_rejects_positive_economic_continuity(statement):
    path = ROOT / "publication/content/01-catastro/03-expediente-sorribos-santibanez.qmd"
    _, body = validator._front_matter_and_body(path)
    mutated = replace_once(
        body,
        r"no\s+demuestra\s+continuidad\s+económica\s+automática\s+hasta\s+1752",
        "no demuestra continuidad económica automática hasta 1752. " + statement,
    )

    assert error_codes(validator._validate_chapter_three_body(mutated)) == {
        "C3_ECONOMIC_CONTINUITY_REVERSAL"
    }


@pytest.mark.parametrize(
    "wording",
    (
        "no existe una secuencia fonética completa",
        "una secuencia fonética completa no existe",
        "no permite reconstruir una secuencia fonética completa",
        "nunca existe una secuencia fonética completa",
        "tampoco existe una secuencia fonética completa",
        "sin disponer de una secuencia fonética completa",
    ),
)
def test_chapter_three_accepts_equivalent_phonetic_limits(wording):
    path = ROOT / "publication/content/01-catastro/03-expediente-sorribos-santibanez.qmd"
    _, body = validator._front_matter_and_body(path)
    mutated = replace_once(
        body,
        r"no\s+proporciona\s+una\s+secuencia\s+fonética\s+completa",
        wording,
    )

    assert validator._validate_chapter_three_body(mutated) == []


@pytest.mark.parametrize(
    "wording",
    (
        "no hay continuidad económica demostrada entre 1267 y 1752",
        "entre 1267 y 1752 no está demostrada la continuidad económica",
        "no autoriza a afirmar continuidad económica hasta 1752",
        "nunca demuestra continuidad económica automática hasta 1752",
        "tampoco prueba continuidad económica entre 1267 y 1752",
        "sin continuidad económica demostrada entre 1267 y 1752",
    ),
)
def test_chapter_three_accepts_equivalent_economic_limits(wording):
    path = ROOT / "publication/content/01-catastro/03-expediente-sorribos-santibanez.qmd"
    _, body = validator._front_matter_and_body(path)
    mutated = replace_once(
        body,
        r"no\s+demuestra\s+continuidad\s+económica\s+automática\s+hasta\s+1752",
        wording,
    )

    assert validator._validate_chapter_three_body(mutated) == []


@pytest.mark.parametrize(
    ("mutation", "expected_code"),
    (
        (
            "El facsímil, la transcripción paleográfica, la edición crítica y la "
            "edición modernizada son indistinguibles.",
            "C4_LAYERS_CONTRADICTED",
        ),
        (
            "Las cuatro capas son indistinguibles: el facsímil, la transcripción "
            "paleográfica, la edición crítica y la modernizada.",
            "C4_LAYERS_CONTRADICTED",
        ),
        (
            "La transcripción y la interpretación son lo mismo.",
            "C4_TRANSCRIPTION_INTERPRETATION_REVERSED",
        ),
        (
            "La interpretación y la transcripción son equivalentes.",
            "C4_TRANSCRIPTION_INTERPRETATION_REVERSED",
        ),
        (
            "publication/content/ y publication/generated/ son la misma capa.",
            "C4_CONTENT_GENERATED_SAME",
        ),
        (
            "publication/generated/ y publication/content/ son la misma capa.",
            "C4_CONTENT_GENERATED_SAME",
        ),
        (
            "publication/content/ es el directorio regenerado automáticamente.",
            "C4_DIRECTORY_FUNCTIONS_REVERSED",
        ),
        (
            "Las salidas regenerables se almacenan en publication/content/.",
            "C4_DIRECTORY_FUNCTIONS_REVERSED",
        ),
        (
            "publication/generated/ contiene el texto editorial mantenido manualmente.",
            "C4_DIRECTORY_FUNCTIONS_REVERSED",
        ),
        (
            "La fuente editorial mantenida manualmente se guarda en "
            "publication/generated/.",
            "C4_DIRECTORY_FUNCTIONS_REVERSED",
        ),
        (
            "Los derivados de publication/generated/ tienen autoridad canónica propia.",
            "C4_GENERATED_AUTHORITY",
        ),
        (
            "La autoridad canónica propia corresponde a los derivados de "
            "publication/generated/.",
            "C4_GENERATED_AUTHORITY",
        ),
    ),
)
def test_chapter_four_rejects_semantic_reversals(mutation, expected_code):
    path = ROOT / "publication/content/01-catastro/04-manuscrito-volumen-actual.qmd"
    _, body = validator._front_matter_and_body(path)

    assert error_codes(
        validator._validate_chapter_four_body(f"{body}\n\n{mutation}\n")
    ) == {expected_code}


@pytest.mark.parametrize(
    ("anchor", "replacement", "expected_code"),
    (
        (
            "volumen-cuatro-accesos",
            "El facsímil no reproduce la imagen ni conserva la materialidad.\n\n"
            "La transcripción paleográfica nunca fija ni conserva el texto línea "
            "por línea.\n\n"
            "La edición crítica tampoco contiene secciones, aparato ni decisiones.\n\n"
            "La edición modernizada no actualiza ni ofrece una lectura en español "
            "actual.",
            "C4_LAYER_FUNCTIONS",
        ),
        (
            "volumen-evidencia",
            "La transcripción no establece qué dice la fuente; la interpretación "
            "tampoco explica qué significa históricamente.",
            "C4_TRANSCRIPTION_INTERPRETATION",
        ),
        (
            "volumen-content-generated",
            "publication/content/ no contiene texto editorial mantenido de forma "
            "humana; publication/generated/ tampoco contiene derivados "
            "reproducibles que se regeneran. Esos derivados no tienen autoridad "
            "canónica propia.",
            "C4_CONTENT_GENERATED_FUNCTIONS",
        ),
    ),
)
def test_chapter_four_rejects_negated_expected_functions(
    anchor, replacement, expected_code
):
    path = ROOT / "publication/content/01-catastro/04-manuscrito-volumen-actual.qmd"
    _, body = validator._front_matter_and_body(path)
    mutated = replace_section(body, anchor, replacement)

    assert error_codes(validator._validate_chapter_four_body(mutated)) == {
        expected_code
    }


@pytest.mark.parametrize(
    "replacement",
    (
        "publication/content/ contiene texto editorial mantenido de forma humana; "
        "publication/generated/ contiene derivados reproducibles que se regeneran. "
        "Esos derivados no tienen autoridad canónica propia.",
        "publication/generated/ contiene derivados reproducibles que se regeneran; "
        "publication/content/ contiene texto editorial mantenido de forma humana. "
        "Ninguna autoridad canónica propia corresponde a los derivados.",
        "El texto editorial redactado humanamente se guarda en publication/content/; "
        "las salidas reproducibles se regeneran en publication/generated/. Los "
        "derivados carecen de autoridad canónica propia.",
        "publication/content/ contiene texto editorial mantenido de forma humana; "
        "publication/generated/ no contiene una fuente editorial mantenida "
        "manualmente, sino derivados reproducibles que se regeneran. Esos derivados "
        "no tienen autoridad canónica propia.",
    ),
)
def test_chapter_four_accepts_equivalent_directory_relations(replacement):
    path = ROOT / "publication/content/01-catastro/04-manuscrito-volumen-actual.qmd"
    _, body = validator._front_matter_and_body(path)
    mutated = replace_section(body, "volumen-content-generated", replacement)

    assert validator._validate_chapter_four_body(mutated) == []


@pytest.mark.parametrize(
    "fragment",
    (
        "\n".join(
            f"{number}. ¿Pregunta sintética {number}?"
            for number in range(1, 31)
        ),
        "\n".join(
            f"### Pregunta {number}: formulación sintética"
            for number in range(1, 31)
        ),
        "\n".join(
            f"| {number} | Respuesta sintética {number} |"
            for number in range(1, 31)
        ),
        "\n".join(
            f"- **Pregunta {number}:** formulación sintética"
            for number in range(1, 31)
        ),
    ),
)
def test_extensive_questionnaire_is_detected_across_markdown_forms(fragment):
    assert validator._has_extensive_questionnaire_sequence(fragment)


@pytest.mark.parametrize("label", ("Pregunta", "Respuesta"))
def test_bare_questionnaire_markers_are_detected_without_false_positives(label):
    bare_headings = "\n".join(
        f"### {label} {number}" for number in range(1, 41)
    )
    bare_bold_labels = "\n".join(
        f"- **{label} {number}**" for number in range(1, 41)
    )
    isolated_markers = "\n".join(
        f"- **{label} {number}**"
        for number in (6, 7, 8, 13, 29, 31, 32, 34, 37, 40)
    )

    for fragment in (bare_headings, bare_bold_labels):
        assert validator._questionnaire_markers(fragment) == tuple(range(1, 41))
        assert validator._has_extensive_questionnaire_sequence(fragment)
    assert not validator._has_extensive_questionnaire_sequence(isolated_markers)


def test_thematic_ranges_and_isolated_examples_are_not_questionnaire_duplication():
    thematic_table = "\n".join(
        f"| {question_range} | {subject} |"
        for question_range, subject in validator.CHAPTER_TWO_THEMATIC_BLOCKS
    )
    isolated_examples = "\n".join(
        f"### Pregunta {number}: ejemplo documental aislado"
        for number in (6, 7, 8, 13, 29, 31, 32, 34, 37, 40)
    )

    assert not validator._has_extensive_questionnaire_sequence(thematic_table)
    assert not validator._has_extensive_questionnaire_sequence(isolated_examples)


def test_asset_manifest_has_only_page_12_and_folio_315v():
    manifest = yaml.safe_load(
        (ROOT / "publication" / "meta" / "assets.yml").read_text(encoding="utf-8")
    )
    assert [asset["asset_id"] for asset in manifest["assets"]] == [
        "manuscript-page-12",
        "folio-315v",
    ]
    assert all(asset["source"]["page"] == 12 for asset in manifest["assets"])
    assert all(
        asset["destination"].startswith("generated/assets/")
        for asset in manifest["assets"]
    )


def test_navigation_integrates_part_one_before_the_vertical_prototype():
    quarto = yaml.safe_load(
        (ROOT / "publication" / "_quarto.yml").read_text(encoding="utf-8")
    )
    manifest = yaml.safe_load(
        (ROOT / "publication" / "meta" / "chapters.yml").read_text(encoding="utf-8")
    )
    navigation = quarto["book"]["chapters"]
    manifest_paths = [chapter["path"] for chapter in manifest["chapters"]]
    expected_order = [
        "content/00-preliminares/00-prueba-tecnica.qmd",
        "content/01-catastro/01-catastro-ensenada.qmd",
        "content/01-catastro/02-respuestas-generales-interrogatorio.qmd",
        "content/01-catastro/03-expediente-sorribos-santibanez.qmd",
        "content/01-catastro/04-manuscrito-volumen-actual.qmd",
        "content/02-estudio/09-rio-molinos-recursos.qmd",
    ]

    assert [item for item in navigation if item in expected_order] == expected_order
    assert [item for item in manifest_paths if item in expected_order] == expected_order
    assert all(navigation.count(item) == 1 for item in expected_order)
    assert all(manifest_paths.count(item) == 1 for item in expected_order)
    chapter_ids = [chapter["chapter_id"] for chapter in manifest["chapters"]]
    assert len(chapter_ids) == len(set(chapter_ids))
    assert sum(item.startswith("generated/") for item in navigation) == 4
    index_path = ROOT / "publication" / "index.qmd"
    technical_path = (
        ROOT
        / "publication"
        / "content"
        / "00-preliminares"
        / "00-prueba-tecnica.qmd"
    )
    assert (
        read_front_matter(index_path)["title"]
        == "# Sorribos y Santibáñez de Ordás en 1752 {.unnumbered}"
    )
    assert (
        read_front_matter(technical_path)["title"]
        == "# Prueba técnica de composición {.unnumbered}"
    )
    assert "number-sections" not in index_path.read_text(encoding="utf-8")
    assert "number-sections" not in technical_path.read_text(encoding="utf-8")
    assert "number-sections" not in read_front_matter(
        ROOT
        / "publication"
        / "content"
        / "01-catastro"
        / "01-catastro-ensenada.qmd"
    )
    assert "number-sections" not in read_front_matter(
        ROOT
        / "publication"
        / "content"
        / "01-catastro"
        / "02-respuestas-generales-interrogatorio.qmd"
    )
    for filename in (
        "03-expediente-sorribos-santibanez.qmd",
        "04-manuscrito-volumen-actual.qmd",
    ):
        assert "number-sections" not in read_front_matter(
            ROOT / "publication" / "content" / "01-catastro" / filename
        )
    assert "Fase 2B" not in manifest["purpose"]


def test_paleographic_transcription_uses_one_semantic_line_block():
    edition = (
        ROOT / "project" / "20_TRABAJO_EDITORIAL" / "Edicion_Critica.md"
    ).read_text(encoding="utf-8")
    canonical = prototype.read_paleographic_lines(edition)
    generated = prototype._transcription_page(edition)

    assert len(canonical) == prototype.PALEOGRAPHIC_LINE_COUNT == 18
    assert validator._generated_paleographic_lines(generated) == canonical
    assert generated.count("\n| ") == 18


def test_paleographic_transcription_keeps_sections_and_documentary_hyphens():
    edition = (
        ROOT / "project" / "20_TRABAJO_EDITORIAL" / "Edicion_Critica.md"
    ).read_text(encoding="utf-8")
    generated = prototype._transcription_page(edition)
    headings = tuple(
        line.removeprefix("### ")
        for line in generated.splitlines()
        if line.startswith("### ")
    )
    lines = validator._generated_paleographic_lines(generated)

    assert headings == validator.UNIT_HEADINGS
    assert tuple(
        line.rsplit(maxsplit=1)[-1] for line in lines if line.endswith("-")
    ) == validator.DOCUMENTARY_HYPHEN_ENDINGS


def test_html_line_block_parser_rejects_collapsed_paragraph():
    canonical = ("primera línea", "segunda línea")
    semantic = validator._LineBlockParser()
    semantic.feed('<div class="line-block">primera línea<br>segunda línea</div>')
    collapsed = validator._LineBlockParser()
    collapsed.feed("<p>primera línea segunda línea</p>")

    assert semantic.blocks == [canonical]
    assert collapsed.blocks == []


def test_local_manuscript_environment_override_has_priority(tmp_path):
    repository = tmp_path / "repository"
    repository.mkdir()
    override = tmp_path / "override" / "manuscript.pdf"
    override.parent.mkdir()
    override.write_bytes(b"override")
    xdg_copy = tmp_path / "xdg" / "sorrios-ensenada" / "manuscript.pdf"
    xdg_copy.parent.mkdir(parents=True)
    xdg_copy.write_bytes(b"xdg")

    resolved = preparation._resolve_manuscript_pdf(
        repository,
        {
            preparation.MANUSCRIPT_ENV: str(override),
            "XDG_DATA_HOME": str(tmp_path / "xdg"),
        },
        tmp_path / "home",
    )

    assert resolved == override.resolve()


def test_local_manuscript_uses_xdg_data_home(tmp_path):
    repository = tmp_path / "repository"
    repository.mkdir()
    manuscript = tmp_path / "xdg" / "sorrios-ensenada" / "manuscript.pdf"
    manuscript.parent.mkdir(parents=True)
    manuscript.write_bytes(b"xdg")

    resolved = preparation._resolve_manuscript_pdf(
        repository,
        {"XDG_DATA_HOME": str(tmp_path / "xdg")},
        tmp_path / "home",
    )

    assert resolved == manuscript.resolve()


def test_local_manuscript_uses_home_fallback(tmp_path):
    repository = tmp_path / "repository"
    repository.mkdir()
    home = tmp_path / "home"
    manuscript = home / ".local" / "share" / "sorrios-ensenada" / "manuscript.pdf"
    manuscript.parent.mkdir(parents=True)
    manuscript.write_bytes(b"home")

    resolved = preparation._resolve_manuscript_pdf(repository, {}, home)

    assert resolved == manuscript.resolve()


def test_local_manuscript_missing_fails_without_remote_fallback(tmp_path):
    repository = tmp_path / "repository"
    repository.mkdir()
    home = tmp_path / "home"

    with pytest.raises(preparation.PreparationError) as error:
        preparation._resolve_manuscript_pdf(repository, {}, home)

    message = str(error.value)
    assert "No se realizará ninguna descarga automática" in message
    assert str(home / ".local" / "share" / "sorrios-ensenada" / "manuscript.pdf") in message


def test_local_manuscript_inside_checkout_is_rejected(tmp_path):
    repository = tmp_path / "repository"
    manuscript = repository / ".local" / "manuscript.pdf"
    manuscript.parent.mkdir(parents=True)
    manuscript.write_bytes(b"inside")

    with pytest.raises(preparation.PreparationError, match="fuera del checkout Git"):
        preparation._resolve_manuscript_pdf(
            repository,
            {preparation.MANUSCRIPT_ENV: str(manuscript)},
            tmp_path / "home",
        )

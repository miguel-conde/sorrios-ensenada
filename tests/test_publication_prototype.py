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
CHAPTER_FIVE_SOURCES = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Introduccion_Catastro_Ensenada_Sorrios.md",
}
CHAPTER_FIVE_EVIDENCE = {
    "D": ("JUR-001", "JUR-002", "JUR-005", "JUR-006", "FIS-012"),
    "E": ("JUR-007", "JUR-008"),
    "L": ("LIM-011",),
}
CHAPTER_SIX_SOURCES = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Oficios.md",
}
CHAPTER_SIX_EVIDENCE = {
    "D": (
        "DEM-001", "DEM-002", "DEM-003", "DEM-004", "GAN-007",
        "TRA-001", "TRA-002", "TRA-003", "TRA-004", "TRA-005", "FIS-007",
    ),
    "C": ("CAL-018", "CAL-019"),
    "I": ("INT-002", "INT-008", "INT-010"),
    "E": ("DEM-005", "DEM-006"),
    "L": ("LIM-001", "LIM-002", "LIM-008"),
}
CHAPTER_SEVEN_SOURCES = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Plan_Composicion_Volumen_0_5.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md",
}
CHAPTER_SEVEN_EVIDENCE = {
    "D": (
        "TER-001", "TER-002", "TER-003", "TER-004", "TER-005", "TER-006",
        "TER-010", "AGR-001", "AGR-002", "AGR-003", "AGR-007", "AGR-008",
        "AGR-010",
    ),
    "C": (
        "TER-007", "TER-008", "AGR-004", "AGR-005", "AGR-006", "AGR-009",
        "CAL-001", "CAL-002", "CAL-003", "CAL-004", "CAL-005", "CAL-006",
        "CAL-007", "CAL-008", "CAL-009",
    ),
    "I": ("INT-001", "INT-003"),
    "E": ("TER-011", "AGR-011", "AGR-012", "AGR-013"),
    "L": (
        "TER-009", "LIM-003", "LIM-004", "LIM-005", "LIM-006", "LIM-007",
        "LIM-009",
    ),
}
CHAPTER_EIGHT_SOURCES = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/20_TRABAJO_EDITORIAL/Glosario.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md",
}
CHAPTER_EIGHT_EVIDENCE = {
    "D": ("TER-001", "GAN-001", "GAN-002", "GAN-007"),
    "C": (),
    "I": ("INT-002", "INT-004"),
    "E": ("AGR-012", "AGR-013", "GAN-008"),
    "L": ("TER-009", "LIM-008", "LIM-009"),
}
CHAPTER_NINE_SOURCES = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/20_TRABAJO_EDITORIAL/Glosario.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md",
}
CHAPTER_NINE_EVIDENCE = {
    "D": ("HID-001", "HID-003", "HID-005", "HID-006", "GAN-003", "GAN-004", "FIS-012"),
    "C": (
        "HID-002", "HID-004", "GAN-005", "GAN-006", "CAL-010",
        "CAL-011", "CAL-012", "CAL-013", "CAL-020",
    ),
    "I": ("HID-007", "INT-002", "INT-005"),
    "E": ("HID-008",),
    "L": ("LIM-005", "LIM-008", "LIM-009", "LIM-010", "LIM-011"),
}
CHAPTER_TEN_SOURCES = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Plan_Composicion_Volumen_0_5.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/20_TRABAJO_EDITORIAL/Glosario.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Personas.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Instituciones.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md",
}
CHAPTER_TEN_EVIDENCE = {
    "D": (
        "JUR-005", "JUR-006", "FIS-001", "FIS-002", "FIS-003",
        "FIS-004", "FIS-008", "FIS-012",
    ),
    "C": ("CAL-009",),
    "I": ("INT-010",),
    "E": ("FIS-013",),
    "L": ("LIM-001", "LIM-002", "LIM-005", "LIM-011"),
}
CHAPTER_ELEVEN_SOURCES = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Plan_Composicion_Volumen_0_5.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/20_TRABAJO_EDITORIAL/Glosario.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Instituciones.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Toponimos.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md",
}
CHAPTER_ELEVEN_EVIDENCE = {
    "D": ("FIS-005", "FIS-006", "FIS-007", "FIS-008", "GAN-002", "TRA-005"),
    "C": (),
    "I": ("INT-004", "INT-006"),
    "E": ("FIS-014", "FIS-015", "FIS-016", "FIS-017", "TRA-006"),
    "L": ("LIM-012", "LIM-013"),
}
CHAPTER_TWELVE_SOURCES = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Plan_Composicion_Volumen_0_5.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/20_TRABAJO_EDITORIAL/Glosario.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Oficios.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Personas.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Toponimos.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Instituciones.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md",
}
CHAPTER_TWELVE_EVIDENCE = {
    "D": (
        "GAN-001", "GAN-003", "HID-005", "TRA-001", "TRA-002",
        "TRA-003", "TRA-004", "TRA-005", "JUR-006", "FIS-002",
        "FIS-003", "FIS-004", "FIS-006", "FIS-007", "FIS-012",
    ),
    "C": (
        "GAN-005", "HID-004", "FIS-009", "FIS-010", "FIS-011",
        "CAL-010", "CAL-014", "CAL-015", "CAL-016", "CAL-017",
    ),
    "I": ("INT-007", "INT-008", "INT-010"),
    "E": ("JUR-009", "FIS-013", "FIS-014", "FIS-015"),
    "L": (
        "LIM-002", "LIM-005", "LIM-006", "LIM-008", "LIM-009",
        "LIM-011", "LIM-012", "LIM-013",
    ),
}
CHAPTER_THIRTEEN_SOURCES = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Plan_Composicion_Volumen_0_5.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md",
    "publication/content/02-estudio/05-lugar-senorio-concejo-ordas.qmd",
    "publication/content/02-estudio/06-vecinos-hogares-viviendas-trabajo.qmd",
    "publication/content/02-estudio/07-tierra-sistema-agrario-medidas.qmd",
    "publication/content/02-estudio/08-ganaderia-montes-aprovechamientos-comunales.qmd",
    "publication/content/02-estudio/09-rio-molinos-recursos.qmd",
    "publication/content/02-estudio/10-iglesia-senorio-fiscalidad.qmd",
    "publication/content/02-estudio/11-hacienda-concejil-servicios-colectivos.qmd",
    "publication/content/02-estudio/12-dinero-oficios-conexiones-exteriores.qmd",
}
CHAPTER_THIRTEEN_EVIDENCE = {
    "D": (
        "JUR-001", "JUR-002", "JUR-005", "JUR-006", "TER-001",
        "TER-010", "AGR-001", "AGR-002", "AGR-003", "AGR-010",
        "GAN-001", "GAN-002", "GAN-003", "GAN-007", "HID-001",
        "HID-005", "HID-006", "DEM-001", "DEM-003", "TRA-001",
        "TRA-002", "TRA-003", "TRA-004", "TRA-005", "FIS-001",
        "FIS-002", "FIS-003", "FIS-004", "FIS-005", "FIS-006",
        "FIS-007", "FIS-008", "FIS-012",
    ),
    "C": (
        "AGR-004", "AGR-005", "AGR-006", "GAN-005", "HID-002",
        "HID-004", "FIS-009", "FIS-010", "FIS-011", "CAL-003",
        "CAL-004", "CAL-005", "CAL-006", "CAL-012", "CAL-013",
        "CAL-014", "CAL-015", "CAL-016", "CAL-017",
    ),
    "I": (
        "INT-001", "INT-002", "INT-003", "INT-004", "INT-005",
        "INT-006", "INT-007", "INT-008", "INT-009", "INT-010",
    ),
    "E": (
        "TER-011", "AGR-011", "AGR-012", "AGR-013", "GAN-008",
        "HID-008", "TRA-006", "FIS-013", "FIS-014", "FIS-015",
        "FIS-016", "FIS-017",
    ),
    "L": (
        "LIM-001", "LIM-002", "LIM-003", "LIM-004", "LIM-005",
        "LIM-006", "LIM-007", "LIM-008", "LIM-009", "LIM-010",
        "LIM-011", "LIM-012", "LIM-013",
    ),
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


def test_chapter_nine_declares_development_metadata():
    metadata = read_front_matter(
        ROOT
        / "publication"
        / "content"
        / "02-estudio"
        / "09-rio-molinos-recursos.qmd"
    )
    assert metadata["chapter-id"] == "rio-molinos-recursos"
    assert metadata["publication-status"] == "development"
    assert {source["path"] for source in metadata["sources"]} == CHAPTER_NINE_SOURCES
    assert len(metadata["sources"]) == len(CHAPTER_NINE_SOURCES)
    assert all(source["locator"] for source in metadata["sources"])
    assert {
        level: tuple(values) for level, values in metadata["evidence"].items()
    } == CHAPTER_NINE_EVIDENCE


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


def test_chapter_five_has_controlled_provenance_evidence_and_structure():
    path = ROOT / "publication/content/02-estudio/05-lugar-senorio-concejo-ordas.qmd"
    metadata, body = validator._front_matter_and_body(path)
    register = (
        ROOT / "project/30_RESULTADOS/ESTUDIO_HISTORICO"
        / "Registro_Afirmaciones_Calculos_v1.md"
    ).read_text(encoding="utf-8")
    registered = set(re.findall(r"^\|\s*([A-Z]+-\d{3})\s*\|", register, re.MULTILINE))

    assert metadata["title"] == "Un lugar de señorío en el Concejo de Ordás"
    assert metadata["chapter-id"] == "lugar-senorio-concejo-ordas"
    assert metadata["publication-status"] == "development"
    assert {source["path"] for source in metadata["sources"]} == CHAPTER_FIVE_SOURCES
    assert len(metadata["sources"]) == len(CHAPTER_FIVE_SOURCES)
    assert all(source["locator"] for source in metadata["sources"])
    evidence = {level: tuple(values) for level, values in metadata["evidence"].items()}
    assert evidence == CHAPTER_FIVE_EVIDENCE
    assert "I" not in evidence
    assert {item for group in evidence.values() for item in group} <= registered
    assert all(
        validator._markdown_section(body, anchor)
        for anchor in validator.CHAPTER_FIVE_ANCHORS
    )
    assert "(../01-catastro/03-expediente-sorribos-santibanez.qmd)" in body
    assert "(../01-catastro/04-manuscrito-volumen-actual.qmd)" in body
    normalized = validator._normalized_text(body)
    assert "continuidad territorial y administrativa" not in normalized
    assert (
        "esas fuentes describen una configuración administrativa decimonónica "
        "posterior, que no puede proyectarse sobre 1752"
    ) in normalized
    assert not re.search(r"<[A-Za-z][^>]*>", body)
    assert validator._validate_chapter_five_body(body) == []


@pytest.mark.parametrize(
    ("mutation", "expected_code"),
    (
        ("El común del lugar era el Concejo de Ordás.",
         "C5_COMMON_COUNCIL_EQUIVALENCE"),
        ("El Concejo de Ordás de 1752 era el municipio actual.",
         "C5_COUNCIL_MUNICIPALITY_EQUIVALENCE"),
        ("El manuscrito identifica a Francisco Alfonso Pimentel.",
         "C5_MANUSCRIPT_IDENTIFIES_COUNT"),
        ("El lugar no pagaba ningún derecho al conde.",
         "C5_NO_LORDLY_RIGHTS"),
        ("La respuesta 22 demuestra la ausencia de derechos señoriales.",
         "C5_R22_ERASES_RIGHTS"),
        ("La respuesta 22 demuestra que no existían derechos señoriales.",
         "C5_R22_ERASES_RIGHTS"),
        ("La respuesta 22 demuestra que no existen derechos señoriales.",
         "C5_R22_ERASES_RIGHTS"),
        ("Se conoce el título jurídico de las alcabalas y del pozo.",
         "C5_KNOWN_LEGAL_TITLE"),
        ("Conocemos el título jurídico de las alcabalas y del pozo.",
         "C5_KNOWN_LEGAL_TITLE"),
        ("No consta el título jurídico concreto. Se conoce el título jurídico "
         "de las alcabalas y del pozo.",
         "C5_KNOWN_LEGAL_TITLE"),
        ("El croquis permite reconstruir un polígono geográfico exacto.",
         "C5_EXACT_POLYGON_RECONSTRUCTION"),
        ("Las dimensiones equivalen a 317 hectáreas.",
         "C5_MODERN_TERRITORIAL_CONVERSION"),
        ("La superficie era de 3,17 kilómetros cuadrados.",
         "C5_MODERN_TERRITORIAL_CONVERSION"),
    ),
)
def test_chapter_five_rejects_bounded_semantic_reversals(mutation, expected_code):
    path = ROOT / "publication/content/02-estudio/05-lugar-senorio-concejo-ordas.qmd"
    _, body = validator._front_matter_and_body(path)

    assert error_codes(
        validator._validate_chapter_five_body(f"{body}\n\n{mutation}\n")
    ) == {expected_code}


@pytest.mark.parametrize(
    "caution",
    (
        "El común del lugar y el Concejo de Ordás no son intercambiables.",
        "El Concejo histórico no es equivalente automático al municipio actual.",
        "El manuscrito no proporciona el nombre personal del titular; la "
        "identificación de Francisco Alfonso Pimentel procede de contexto externo.",
        "La falta de carga por establecimiento del suelo coexiste con las alcabalas "
        "y el pozo.",
        "No se conoce el título jurídico de las alcabalas y del pozo.",
        "No consta el título jurídico concreto de las alcabalas ni del pozo.",
        "Se desconoce el origen jurídico de las alcabalas y del pozo.",
        "Las dimensiones no se convierten en superficie moderna.",
    ),
)
def test_chapter_five_accepts_bounded_cautionary_formulations(caution):
    path = ROOT / "publication/content/02-estudio/05-lugar-senorio-concejo-ordas.qmd"
    _, body = validator._front_matter_and_body(path)

    assert validator._validate_chapter_five_body(f"{body}\n\n{caution}\n") == []


@pytest.mark.parametrize(
    ("mutation", "expected_codes"),
    (
        (
            "La respuesta 22 demuestra la ausencia de derechos señoriales.",
            {"C5_R22_ERASES_RIGHTS"},
        ),
        (
            "La respuesta 22 demuestra la ausencia de\n"
            "derechos señoriales.",
            {"C5_R22_ERASES_RIGHTS"},
        ),
        (
            "La respuesta 22 demuestra la ausencia de\n\n"
            "Derechos señoriales es el título del apartado siguiente.",
            set(),
        ),
        (
            "La respuesta 22 demuestra la ausencia de\n\n"
            "## Derechos señoriales\n\n"
            "El apartado distingue conceptos.",
            set(),
        ),
    ),
)
def test_chapter_five_prohibitions_preserve_semantic_block_boundaries(
    mutation, expected_codes
):
    path = ROOT / "publication/content/02-estudio/05-lugar-senorio-concejo-ordas.qmd"
    _, body = validator._front_matter_and_body(path)

    assert error_codes(
        validator._validate_chapter_five_body(f"{body}\n\n{mutation}\n")
    ) == expected_codes


def test_chapter_six_has_controlled_provenance_evidence_and_structure():
    path = (
        ROOT / "publication/content/02-estudio"
        / "06-vecinos-hogares-viviendas-trabajo.qmd"
    )
    metadata, body = validator._front_matter_and_body(path)
    register = (
        ROOT / "project/30_RESULTADOS/ESTUDIO_HISTORICO"
        / "Registro_Afirmaciones_Calculos_v1.md"
    ).read_text(encoding="utf-8")
    registered = set(re.findall(r"^\|\s*([A-Z]+-\d{3})\s*\|", register, re.MULTILINE))

    assert metadata["title"] == "Vecinos, hogares, viviendas y trabajo"
    assert metadata["chapter-id"] == "vecinos-hogares-viviendas-trabajo"
    assert metadata["publication-status"] == "development"
    assert {source["path"] for source in metadata["sources"]} == CHAPTER_SIX_SOURCES
    assert len(metadata["sources"]) == len(CHAPTER_SIX_SOURCES)
    assert all(source["locator"] for source in metadata["sources"])
    evidence = {level: tuple(values) for level, values in metadata["evidence"].items()}
    assert evidence == CHAPTER_SIX_EVIDENCE
    assert set(evidence) == {"D", "C", "I", "E", "L"}
    assert {item for group in evidence.values() for item in group} <= registered
    assert all(
        validator._markdown_section(body, anchor)
        for anchor in validator.CHAPTER_SIX_ANCHORS
    )
    assert "(05-lugar-senorio-concejo-ordas.qmd)" in body
    assert not re.search(r"<[A-Za-z][^>]*>", body)
    assert validator._validate_chapter_six_body(body) == []


@pytest.mark.parametrize(
    ("mutation", "expected_code"),
    (
        ("Los 26 avitadores son 26 habitantes.",
         "C6_AVITADORES_ARE_INHABITANTS"),
        ("La población total era de 34 habitantes.",
         "C6_RESIDENT_SUM_IS_POPULATION"),
        ("Ocho medios vecinos equivalen a cuatro vecinos.",
         "C6_HALF_NEIGHBOUR_WEIGHTED"),
        ("Las cuarenta casas habitables representan cuarenta hogares.",
         "C6_HOUSES_ARE_HOUSEHOLDS"),
        ("Los 18 jornaleros y los 24 labradores forman una población activa de 42.",
         "C6_LABOUR_CATEGORIES_ADDED"),
        ("El medio vecino era media persona.",
         "C6_HALF_NEIGHBOUR_IS_HALF_PERSON"),
        ("Los 2,5 reales diarios permiten calcular el ingreso anual.",
         "C6_DAILY_RATE_IS_ANNUAL_INCOME"),
        ("El herrero no ejercía como labrador.",
         "C6_SMITH_NOT_FARMER"),
        ("Los cinco pobres de solemnidad permiten calcular la tasa de pobreza.",
         "C6_POVERTY_RATE"),
        ("Vecinos × 4 = 72 habitantes.",
         "C6_GENERIC_POPULATION_FACTOR"),
    ),
)
def test_chapter_six_rejects_bounded_semantic_reversals(mutation, expected_code):
    path = (
        ROOT / "publication/content/02-estudio"
        / "06-vecinos-hogares-viviendas-trabajo.qmd"
    )
    _, body = validator._front_matter_and_body(path)

    assert error_codes(
        validator._validate_chapter_six_body(f"{body}\n\n{mutation}\n")
    ) == {expected_code}


@pytest.mark.parametrize(
    "caution",
    (
        "Los 26 avitadores no son 26 habitantes.",
        "Ocho medios vecinos no equivalen a cuatro vecinos.",
        "Las cuarenta casas habitables no representan cuarenta hogares.",
        "Los cinco pobres de solemnidad no permiten calcular la tasa de pobreza.",
        "La regulación diaria no permite calcular el ingreso anual.",
    ),
)
def test_chapter_six_accepts_bounded_cautionary_formulations(caution):
    path = (
        ROOT / "publication/content/02-estudio"
        / "06-vecinos-hogares-viviendas-trabajo.qmd"
    )
    _, body = validator._front_matter_and_body(path)

    assert validator._validate_chapter_six_body(f"{body}\n\n{caution}\n") == []


def test_chapter_seven_has_controlled_provenance_evidence_and_structure():
    path = (
        ROOT / "publication/content/02-estudio"
        / "07-tierra-sistema-agrario-medidas.qmd"
    )
    metadata, body = validator._front_matter_and_body(path)
    register = (
        ROOT / "project/30_RESULTADOS/ESTUDIO_HISTORICO"
        / "Registro_Afirmaciones_Calculos_v1.md"
    ).read_text(encoding="utf-8")
    registered = set(re.findall(r"^\|\s*([A-Z]+-\d{3})\s*\|", register, re.MULTILINE))

    assert metadata["title"] == "Tierra, sistema agrario y medidas"
    assert metadata["chapter-id"] == "tierra-sistema-agrario-medidas"
    assert metadata["publication-status"] == "development"
    assert {source["path"] for source in metadata["sources"]} == CHAPTER_SEVEN_SOURCES
    assert len(metadata["sources"]) == len(CHAPTER_SEVEN_SOURCES)
    assert all(source["locator"] for source in metadata["sources"])
    evidence = {level: tuple(values) for level, values in metadata["evidence"].items()}
    assert evidence == CHAPTER_SEVEN_EVIDENCE
    assert set(evidence) == {"D", "C", "I", "E", "L"}
    assert {item for group in evidence.values() for item in group} <= registered
    assert all(
        validator._markdown_section(body, anchor)
        for anchor in validator.CHAPTER_SEVEN_ANCHORS
    )
    assert "(06-vecinos-hogares-viviendas-trabajo.qmd)" in body
    assert not re.search(r"<[A-Za-z][^>]*>", body)
    assert validator._validate_chapter_seven_body(body) == []


@pytest.mark.parametrize(
    ("mutation", "expected_code"),
    (
        ("La cabida equivalía a 318 hectáreas.", "C7_MODERN_CONVERSION"),
        ("La cosecha pesó 900 kilogramos.", "C7_MODERN_CONVERSION"),
        (
            "3.823 medidas y un celemín y 3.811,5 medidas y siete celemines "
            "coinciden exactamente.",
            "C7_TOTALS_RECONCILED",
        ),
        (
            "La cabida de los montes se calcula por diferencia.",
            "C7_MOUNTS_BY_RESIDUAL",
        ),
        ("Un celemín equivale a un quartal.", "C7_FALSE_CELEMIN_EQUIVALENCE"),
        (
            "93,13 % y 72,16 % usan el mismo denominador.",
            "C7_PERCENTAGES_SAME_DENOMINATOR",
        ),
        (
            "Se documenta una rotación trienal.",
            "C7_EXACT_ROTATION",
        ),
        (
            "1.578,25 representa la superficie efectivamente sembrada.",
            "C7_OBSERVED_ACTIVE_SURFACE",
        ),
        (
            "El producto agrario total fue de 8.000 quartales.",
            "C7_TOTAL_PRODUCTION",
        ),
        (
            "La producción total de lino equivalía a 160 libras.",
            "C7_TOTAL_PRODUCTION",
        ),
        (
            "Se pueden sumar cargas y fanegas para obtener el cereal total.",
            "C7_INCOMPATIBLE_SUM",
        ),
        (
            "Se pueden agregar quartales y libras como una sola producción.",
            "C7_INCOMPATIBLE_SUM",
        ),
        (
            "La diversidad productiva demuestra el autoconsumo.",
            "C7_AUTOCONSUMPTION",
        ),
        (
            "El centeno confirma la suficiencia alimentaria.",
            "C7_AUTOCONSUMPTION",
        ),
        (
            "La cabida permite calcular la productividad por trabajador.",
            "C7_PRODUCTIVITY_INFERENCE",
        ),
        (
            "La sección demuestra el funcionamiento de ocho ruedas.",
            "C7_CHAPTER_BOUNDARY",
        ),
    ),
)
def test_chapter_seven_rejects_bounded_semantic_reversals(mutation, expected_code):
    path = (
        ROOT / "publication/content/02-estudio"
        / "07-tierra-sistema-agrario-medidas.qmd"
    )
    _, body = validator._front_matter_and_body(path)

    assert error_codes(
        validator._validate_chapter_seven_body(f"{body}\n\n{mutation}\n")
    ) == {expected_code}


@pytest.mark.parametrize(
    "caution",
    (
        "El quartal de Sorribos no tiene equivalencia métrica fijada.",
        "Los dos porcentajes usan denominadores distintos.",
        "Las alternancias no describen una rotación completa parcela por parcela.",
        "El índice anualizado es un escenario mecánico, no una observación.",
        "La fuente no permite deducir el destino predominante de la producción.",
    ),
)
def test_chapter_seven_accepts_bounded_cautionary_formulations(caution):
    path = (
        ROOT / "publication/content/02-estudio"
        / "07-tierra-sistema-agrario-medidas.qmd"
    )
    _, body = validator._front_matter_and_body(path)

    assert validator._validate_chapter_seven_body(f"{body}\n\n{caution}\n") == []


def test_chapter_eight_has_controlled_provenance_evidence_and_structure():
    path = (
        ROOT / "publication/content/02-estudio"
        / "08-ganaderia-montes-aprovechamientos-comunales.qmd"
    )
    metadata, body = validator._front_matter_and_body(path)
    register = (
        ROOT / "project/30_RESULTADOS/ESTUDIO_HISTORICO"
        / "Registro_Afirmaciones_Calculos_v1.md"
    ).read_text(encoding="utf-8")
    registered = set(re.findall(r"^\|\s*([A-Z]+-\d{3})\s*\|", register, re.MULTILINE))

    assert metadata["title"] == "Ganadería, montes y aprovechamientos comunales"
    assert metadata["chapter-id"] == "ganaderia-montes-aprovechamientos-comunales"
    assert metadata["publication-status"] == "development"
    assert {source["path"] for source in metadata["sources"]} == CHAPTER_EIGHT_SOURCES
    assert len(metadata["sources"]) == len(CHAPTER_EIGHT_SOURCES)
    assert all(source["locator"] for source in metadata["sources"])
    evidence = {level: tuple(values) for level, values in metadata["evidence"].items()}
    assert evidence == CHAPTER_EIGHT_EVIDENCE
    assert set(evidence) == {"D", "C", "I", "E", "L"}
    assert evidence["C"] == ()
    assert {item for group in evidence.values() for item in group} <= registered
    assert all(
        validator._markdown_section(body, anchor)
        for anchor in validator.CHAPTER_EIGHT_ANCHORS
    )
    assert "(07-tierra-sistema-agrario-medidas.qmd)" in body
    assert not re.search(r"<[A-Za-z][^>]*>", body)
    assert validator._validate_chapter_eight_body(body) == []


@pytest.mark.parametrize(
    ("mutation", "expected_code"),
    (
        (
            "El uso común demuestra la propiedad comunal de los terrenos.",
            "C8_COMMON_USE_IS_PROPERTY",
        ),
        (
            "Los bienes comunales pertenecían al común del lugar.",
            "C8_COMMON_USE_IS_PROPERTY",
        ),
        (
            "20 ovejas producían 20 libras de lana cada año.",
            "C8_HEADCOUNT_IS_OUTPUT",
        ),
        (
            "Cada hogar poseía una vaca de labranza.",
            "C8_LIVESTOCK_ASSIGNED_HOUSEHOLDS",
        ),
        (
            "Había una oveja por vivienda.",
            "C8_LIVESTOCK_ASSIGNED_HOUSEHOLDS",
        ),
        (
            "La producción ganadera total fue de 500 reales anuales.",
            "C8_UNSUPPORTED_PRODUCTION",
        ),
        (
            "Multiplicando las valoraciones por las cabezas se obtiene la renta total.",
            "C8_UNSUPPORTED_PRODUCTION",
        ),
        (
            "Las ovejas tiraban del arado durante la siembra.",
            "C8_UNSUPPORTED_SPECIES_FUNCTION",
        ),
        (
            "Los bueyes producían lana para los vecinos.",
            "C8_UNSUPPORTED_SPECIES_FUNCTION",
        ),
        (
            "Los pastos eran suficientes para alimentar a todo el ganado.",
            "C8_PASTURE_SUFFICIENCY",
        ),
        (
            "La alimentación del ganado estaba asegurada por los prados.",
            "C8_PASTURE_SUFFICIENCY",
        ),
        (
            "Existía un equilibrio ecológico entre ganado y pastos.",
            "C8_ECOLOGICAL_BALANCE",
        ),
        (
            "El sistema de aprovechamiento era sostenible.",
            "C8_ECOLOGICAL_BALANCE",
        ),
        (
            "Los montes garantizaban madera y combustible para todo el año.",
            "C8_GUARANTEED_WOOD_FUEL",
        ),
        (
            "La leña era inagotable.",
            "C8_GUARANTEED_WOOD_FUEL",
        ),
        (
            "Es un dato explícito del manuscrito que la economía era mixta.",
            "C8_INTERPRETATION_AS_DATA",
        ),
        (
            "El manuscrito declara la complementariedad agraria.",
            "C8_INTERPRETATION_AS_DATA",
        ),
        (
            "El censo ganadero completo consta en la respuesta 20.",
            "C8_EVIDENCE_LIMITS_ERASED",
        ),
        (
            "Se conoce el propietario de cada animal.",
            "C8_EVIDENCE_LIMITS_ERASED",
        ),
        (
            "Las ocho ruedas de los molinos producían 26 cargas de centeno.",
            "C8_CHAPTER_BOUNDARY",
        ),
        (
            "La taberna funcionaba por vecera entre los vecinos.",
            "C8_CHAPTER_BOUNDARY",
        ),
        (
            "La cabida de los montes se calcula por diferencia.",
            "C8_CHAPTER_SEVEN_CONTRADICTION",
        ),
        (
            "Todos los prados eran de uso común.",
            "C8_CHAPTER_SEVEN_CONTRADICTION",
        ),
        (
            "Un carro de yerba equivalía a cinco montones.",
            "C8_CHAPTER_SEVEN_CONTRADICTION",
        ),
    ),
)
def test_chapter_eight_rejects_bounded_semantic_reversals(mutation, expected_code):
    path = (
        ROOT / "publication/content/02-estudio"
        / "08-ganaderia-montes-aprovechamientos-comunales.qmd"
    )
    _, body = validator._front_matter_and_body(path)

    assert error_codes(
        validator._validate_chapter_eight_body(f"{body}\n\n{mutation}\n")
    ) == {expected_code}


@pytest.mark.parametrize(
    "caution",
    (
        "La enumeración de especies no es un censo de cabezas.",
        "Las valoraciones unitarias no permiten calcular una producción total.",
        "No consta cómo se distribuía el ganado entre los hogares.",
        "Los pastos no prueban que la alimentación del ganado estuviera asegurada.",
        "La fuente no permite evaluar equilibrio ecológico ni sostenibilidad.",
        "Los usos documentados no garantizan un suministro estable de leña.",
        "La cabida de los montes no se obtiene por diferencia.",
    ),
)
def test_chapter_eight_accepts_bounded_cautionary_formulations(caution):
    path = (
        ROOT / "publication/content/02-estudio"
        / "08-ganaderia-montes-aprovechamientos-comunales.qmd"
    )
    _, body = validator._front_matter_and_body(path)

    assert validator._validate_chapter_eight_body(f"{body}\n\n{caution}\n") == []


def test_chapter_nine_has_controlled_provenance_evidence_and_structure():
    path = (
        ROOT / "publication/content/02-estudio"
        / "09-rio-molinos-recursos.qmd"
    )
    metadata, body = validator._front_matter_and_body(path)
    register = (
        ROOT / "project/30_RESULTADOS/ESTUDIO_HISTORICO"
        / "Registro_Afirmaciones_Calculos_v1.md"
    ).read_text(encoding="utf-8")
    registered = set(re.findall(r"^\|\s*([A-Z]+-\d{3})\s*\|", register, re.MULTILINE))

    assert metadata["title"] == "Río, molinos y otros recursos productivos"
    assert metadata["chapter-id"] == "rio-molinos-recursos"
    assert metadata["publication-status"] == "development"
    assert {source["path"] for source in metadata["sources"]} == CHAPTER_NINE_SOURCES
    assert len(metadata["sources"]) == len(CHAPTER_NINE_SOURCES)
    assert all(source["locator"] for source in metadata["sources"])
    evidence = {level: tuple(values) for level, values in metadata["evidence"].items()}
    assert evidence == CHAPTER_NINE_EVIDENCE
    assert set(evidence) == {"D", "C", "I", "E", "L"}
    assert {item for group in evidence.values() for item in group} <= registered
    assert all(
        validator._markdown_section(body, anchor)
        for anchor in validator.CHAPTER_NINE_ANCHORS
    )
    assert "(08-ganaderia-montes-aprovechamientos-comunales.qmd)" in body
    assert "se reserva para el capítulo 10" in validator._normalized_text(body)
    assert not re.search(r"<[A-Za-z][^>]*>", body)
    assert validator._validate_chapter_nine_body(body) == []


@pytest.mark.parametrize(
    ("mutation", "expected_code"),
    (
        (
            "La existencia de los molinos demuestra una producción anual conocida.",
            "C9_EXISTENCE_IS_PRODUCTION",
        ),
        (
            "La utilidad de 26 cargas equivale a la producción anual.",
            "C9_UTILITY_IS_PRODUCTION",
        ),
        (
            "El valor fiscal de nueve reales era el ingreso real del conde.",
            "C9_FISCAL_IS_INCOME",
        ),
        (
            "Cada propietario era el explotador de su rueda.",
            "C9_OWNER_IS_OPERATOR",
        ),
        (
            "Cada titular era el molinero de la unidad.",
            "C9_OWNER_IS_MILLER",
        ),
        (
            "Todos los vecinos utilizaban los molinos.",
            "C9_UNDOCUMENTED_USERS",
        ),
        (
            "Los molinos funcionaban durante todo el año.",
            "C9_ANNUAL_OPERATION",
        ),
        (
            "El agua del río era suficiente para la molienda.",
            "C9_WATER_SUFFICIENCY",
        ),
        (
            "La capacidad de molienda era de cien cargas anuales.",
            "C9_MILLING_CAPACITY",
        ),
        (
            "Los molinos abastecían a toda la localidad.",
            "C9_COMPLETE_SUPPLY",
        ),
        (
            "El centeno demuestra la autosuficiencia cerealista.",
            "C9_CEREAL_SELF_SUFFICIENCY",
        ),
        (
            "La molienda generaba un excedente comercial.",
            "C9_COMMERCIAL_SURPLUS",
        ),
        (
            "Es un dato explícito del manuscrito que la economía era mixta.",
            "C9_INTERPRETATION_AS_DATA",
        ),
        (
            "Se conoce el número exacto de ruedas del venturero.",
            "C9_EVIDENCE_LIMITS_ERASED",
        ),
        (
            "El centeno ocupaba el 93,13 % de la cabida total.",
            "C9_PRIOR_CHAPTER_CONTRADICTION",
        ),
        (
            "Los nueve reales demuestran el sistema fiscal señorial.",
            "C9_CHAPTER_BOUNDARY",
        ),
    ),
)
def test_chapter_nine_rejects_sixteen_semantic_reversals(mutation, expected_code):
    path = (
        ROOT / "publication/content/02-estudio"
        / "09-rio-molinos-recursos.qmd"
    )
    _, body = validator._front_matter_and_body(path)

    assert error_codes(
        validator._validate_chapter_nine_body(f"{body}\n\n{mutation}\n")
    ) == {expected_code}


@pytest.mark.parametrize(
    "caution",
    (
        "La existencia de molinos no permite conocer su producción efectiva.",
        "La utilidad regulada no equivale a producción ni a ingreso real.",
        "El titular documentado no tiene por qué ser el molinero ni el operador.",
        "No consta cuántos usuarios acudían a las ruedas.",
        "La fuente no acredita funcionamiento anual ni caudal suficiente.",
        "Ocho ruedas no permiten calcular la capacidad de molienda.",
        "La relación con el centeno no demuestra autosuficiencia ni excedente comercial.",
        "El número de ruedas del venturero sigue siendo desconocido.",
    ),
)
def test_chapter_nine_accepts_bounded_cautionary_formulations(caution):
    path = (
        ROOT / "publication/content/02-estudio"
        / "09-rio-molinos-recursos.qmd"
    )
    _, body = validator._front_matter_and_body(path)

    assert validator._validate_chapter_nine_body(f"{body}\n\n{caution}\n") == []


def test_chapter_ten_has_controlled_provenance_evidence_and_structure():
    path = (
        ROOT / "publication/content/02-estudio"
        / "10-iglesia-senorio-fiscalidad.qmd"
    )
    metadata, body = validator._front_matter_and_body(path)
    register = (
        ROOT / "project/30_RESULTADOS/ESTUDIO_HISTORICO"
        / "Registro_Afirmaciones_Calculos_v1.md"
    ).read_text(encoding="utf-8")
    registered = set(re.findall(r"^\|\s*([A-Z]+-\d{3})\s*\|", register, re.MULTILINE))

    assert metadata["title"] == "Iglesia, señorío y fiscalidad"
    assert metadata["chapter-id"] == "iglesia-senorio-fiscalidad"
    assert metadata["publication-status"] == "development"
    assert {source["path"] for source in metadata["sources"]} == CHAPTER_TEN_SOURCES
    assert len(metadata["sources"]) == len(CHAPTER_TEN_SOURCES)
    assert all(source["locator"] for source in metadata["sources"])
    evidence = {level: tuple(values) for level, values in metadata["evidence"].items()}
    assert evidence == CHAPTER_TEN_EVIDENCE
    assert set(evidence) == {"D", "C", "I", "E", "L"}
    assert {item for group in evidence.values() for item in group} <= registered
    assert all(
        validator._markdown_section(body, anchor)
        for anchor in validator.CHAPTER_TEN_ANCHORS
    )
    assert "(09-rio-molinos-recursos.qmd#recursos-pesca)" in body
    assert "capítulo 11 estudiará la hacienda concejil" in validator._normalized_text(body)
    assert not re.search(r"<[A-Za-z][^>]*>", body)
    assert validator._validate_chapter_ten_body(body) == []


@pytest.mark.parametrize(
    ("mutation", "expected_code"),
    (
        (
            "El señorío significa que el conde era propietario de todas las tierras.",
            "C10_LORDSHIP_IS_GENERAL_PROPERTY",
        ),
        (
            "El conde de Luna percibía todos los tributos del lugar.",
            "C10_COUNT_ALL_TAXES",
        ),
        (
            "La Iglesia percibía los diezmos, la primicia y el voto.",
            "C10_CHURCH_GENERIC_RECIPIENT",
        ),
        (
            "Percibir el diezmo convertía al cura en propietario de las tierras.",
            "C10_TITHE_IS_PROPERTY",
        ),
        (
            "Los nueve reales del pozo eran un impuesto pagado por los vecinos.",
            "C10_RENT_IS_TAX",
        ),
        (
            "La utilidad del pozo constituía una carga fiscal vecinal.",
            "C10_UTILITY_IS_FISCAL_CHARGE",
        ),
        (
            "Las treinta cargas reguladas fueron efectivamente pagadas al cura.",
            "C10_REGULATION_IS_PAYMENT",
        ),
        (
            "El pueblo estaba exento de todos los impuestos.",
            "C10_EXEMPTION_GENERALIZED",
        ),
        (
            "Sumando cargas, fanegas, quartales, libras y reales se obtiene la carga fiscal.",
            "C10_INCOMPATIBLE_SUM",
        ),
        (
            "Los 773 reales eran la fiscalidad total.",
            "C10_SUBTOTAL_IS_TOTAL",
        ),
        (
            "La presión fiscal era del 25 % de la renta.",
            "C10_TAX_PRESSURE",
        ),
        (
            "Cada vecino soportaba 29 reales de alcabalas.",
            "C10_PER_CAPITA_CHARGE",
        ),
        (
            "Las 30 cargas equivalían a 500 reales.",
            "C10_SPECIE_MONEY_CONVERSION",
        ),
        (
            "La renta disponible de cada hogar era de 100 reales.",
            "C10_DISPOSABLE_INCOME",
        ),
        (
            "Se conoce el título jurídico exacto de las alcabalas.",
            "C10_EVIDENCE_LIMITS_ERASED",
        ),
        (
            "La respuesta 22 demuestra que no existían derechos señoriales.",
            "C10_CHAPTER_FIVE_CONTRADICTION",
        ),
        (
            "El presupuesto anual completo del común era de 233 reales.",
            "C10_CHAPTER_ELEVEN_BOUNDARY",
        ),
        (
            "Los pagos prueban que la economía estaba plenamente monetizada.",
            "C10_CHAPTER_TWELVE_BOUNDARY",
        ),
        (
            "La fiscalidad hizo vulnerable la economía local.",
            "C10_CHAPTER_THIRTEEN_BOUNDARY",
        ),
    ),
)
def test_chapter_ten_rejects_nineteen_semantic_reversals(mutation, expected_code):
    path = (
        ROOT / "publication/content/02-estudio"
        / "10-iglesia-senorio-fiscalidad.qmd"
    )
    _, body = validator._front_matter_and_body(path)

    assert error_codes(
        validator._validate_chapter_ten_body(f"{body}\n\n{mutation}\n")
    ) == {expected_code}


@pytest.mark.parametrize(
    "caution",
    (
        "El señorío no equivale a propiedad de todas las tierras.",
        "El conde no percibía todos los tributos del lugar.",
        "La Iglesia no percibía indistintamente diezmos, primicia y voto.",
        "El diezmo no convertía al cura en propietario de las tierras.",
        "Los nueve reales del pozo no eran un impuesto pagado por los vecinos.",
        "La regulación no demuestra que las cantidades fueran efectivamente pagadas.",
        "La exención concreta no hacía al pueblo exento de todos los impuestos.",
        "Cargas, fanegas, quartales, libras y reales no forman una suma homogénea.",
        "No puede calcularse presión fiscal, cuota por vecino ni renta disponible.",
        "No se conoce el título jurídico exacto de las alcabalas.",
        "Los pagos no prueban una economía plenamente monetizada ni una vulnerabilidad fiscal.",
    ),
)
def test_chapter_ten_accepts_bounded_cautionary_formulations(caution):
    path = (
        ROOT / "publication/content/02-estudio"
        / "10-iglesia-senorio-fiscalidad.qmd"
    )
    _, body = validator._front_matter_and_body(path)

    assert validator._validate_chapter_ten_body(f"{body}\n\n{caution}\n") == []


def test_chapter_eleven_has_controlled_provenance_evidence_and_structure():
    path = (
        ROOT / "publication/content/02-estudio"
        / "11-hacienda-concejil-servicios-colectivos.qmd"
    )
    metadata, body = validator._front_matter_and_body(path)
    register = (
        ROOT / "project/30_RESULTADOS/ESTUDIO_HISTORICO"
        / "Registro_Afirmaciones_Calculos_v1.md"
    ).read_text(encoding="utf-8")
    registered = set(re.findall(r"^\|\s*([A-Z]+-\d{3})\s*\|", register, re.MULTILINE))

    assert metadata["title"] == "Hacienda concejil y servicios colectivos"
    assert metadata["chapter-id"] == "hacienda-concejil-servicios-colectivos"
    assert metadata["publication-status"] == "development"
    assert {source["path"] for source in metadata["sources"]} == CHAPTER_ELEVEN_SOURCES
    assert len(metadata["sources"]) == len(CHAPTER_ELEVEN_SOURCES)
    assert all(source["locator"] for source in metadata["sources"])
    evidence = {level: tuple(values or []) for level, values in metadata["evidence"].items()}
    assert evidence == CHAPTER_ELEVEN_EVIDENCE
    assert set(evidence) == {"D", "C", "I", "E", "L"}
    assert evidence["C"] == ()
    assert {item for group in evidence.values() for item in group} <= registered
    assert all(
        validator._markdown_section(body, anchor)
        for anchor in validator.CHAPTER_ELEVEN_ANCHORS
    )
    assert "(10-iglesia-senorio-fiscalidad.qmd)" in body
    assert "200 + 8 + 15 + 10 = 233" in validator._normalized_text(body)
    assert "se reserva para el capítulo 12" in validator._normalized_text(body)
    assert not re.search(r"<[A-Za-z][^>]*>", body)
    assert validator._validate_chapter_eleven_body(body) == []


@pytest.mark.parametrize(
    ("mutation", "expected_code"),
    (
        (
            "El Concejo histórico era el ayuntamiento moderno de Santa María de Ordás.",
            "C11_CONCEJO_IS_MODERN_TOWN_HALL",
        ),
        (
            "El uso común convertía los montes en propiedad municipal.",
            "C11_COMMON_USE_IS_MUNICIPAL_PROPERTY",
        ),
        (
            "La administración del recurso demostraba que el concejo era propietario.",
            "C11_ADMINISTRATION_IS_PROPERTY",
        ),
        (
            "La renta regulada era un ingreso efectivamente cobrado.",
            "C11_REGULATED_RENT_IS_COLLECTION",
        ),
        (
            "La utilidad era un ingreso efectivo del común.",
            "C11_UTILITY_IS_CASH_INCOME",
        ),
        (
            "La obligación de 200 reales fue un gasto efectivamente realizado.",
            "C11_OBLIGATION_IS_REALIZED_EXPENSE",
        ),
        (
            "La existencia de fuentes demuestra un servicio permanente de abastecimiento.",
            "C11_INFRASTRUCTURE_IS_PERMANENT_SERVICE",
        ),
        (
            "La taberna daba cobertura universal a todos los habitantes.",
            "C11_UNIVERSAL_COVERAGE",
        ),
        (
            "Sumando ingresos y valores patrimoniales se obtiene la hacienda total.",
            "C11_INCOME_PROPERTY_SUM",
        ),
        (
            "Pueden sumarse gastos de periodos y naturalezas incompatibles.",
            "C11_INCOMPATIBLE_EXPENSE_SUM",
        ),
        (
            "Los 233 reales eran los ingresos totales del común.",
            "C11_SUBTOTAL_IS_TOTAL_INCOME",
        ),
        (
            "Los 233 reales eran los gastos totales del común.",
            "C11_SUBTOTAL_IS_TOTAL_EXPENSE",
        ),
        (
            "El común tuvo un superávit de cincuenta reales.",
            "C11_UNSUPPORTED_BALANCE",
        ),
        (
            "Los 233 reales formaban el presupuesto concejil completo.",
            "C11_COMPLETE_BUDGET",
        ),
        (
            "Las alcabalas eran un gasto concejil del común.",
            "C11_FISCAL_RECLASSIFICATION",
        ),
        (
            "Los montes de uso común eran patrimonio concejil.",
            "C11_COMMON_RESOURCE_IS_CONCEJO_ASSET",
        ),
        (
            "Se conoce el origen jurídico del pago al Hospital de Inocentes.",
            "C11_EVIDENCE_LIMITS_ERASED",
        ),
        (
            "Los pagos prueban que la economía estaba plenamente monetizada.",
            "C11_CHAPTER_TWELVE_BOUNDARY",
        ),
        (
            "La hacienda concejil era eficiente y resiliente.",
            "C11_CHAPTER_THIRTEEN_BOUNDARY",
        ),
    ),
)
def test_chapter_eleven_rejects_nineteen_semantic_reversals(mutation, expected_code):
    path = (
        ROOT / "publication/content/02-estudio"
        / "11-hacienda-concejil-servicios-colectivos.qmd"
    )
    _, body = validator._front_matter_and_body(path)

    assert error_codes(
        validator._validate_chapter_eleven_body(f"{body}\n\n{mutation}\n")
    ) == {expected_code}


@pytest.mark.parametrize(
    "caution",
    (
        "El Concejo histórico no era el ayuntamiento moderno.",
        "El uso común no convertía los montes en propiedad municipal.",
        "Administrar un recurso no demostraba que el concejo fuera propietario.",
        "La renta regulada no era un ingreso efectivamente cobrado.",
        "La utilidad no era un ingreso efectivo del común.",
        "Una obligación no fue necesariamente un gasto efectivamente realizado.",
        "La existencia de fuentes no demuestra un servicio permanente.",
        "La taberna no daba cobertura universal a todos los habitantes.",
        "No deben sumarse ingresos y valores patrimoniales ni gastos incompatibles.",
        "Los 233 reales no eran ingresos totales ni gastos totales.",
        "El común no tuvo un superávit o déficit calculable ni un presupuesto completo.",
        "Las alcabalas no eran un gasto concejil y los montes no eran patrimonio concejil.",
        "No se conoce el origen jurídico del pago al Hospital ni la naturaleza precisa del derecho de Mesta.",
        "Los pagos no prueban una economía plenamente monetizada.",
        "La hacienda concejil no era calificable como eficiente, frágil o resiliente.",
    ),
)
def test_chapter_eleven_accepts_bounded_cautionary_formulations(caution):
    path = (
        ROOT / "publication/content/02-estudio"
        / "11-hacienda-concejil-servicios-colectivos.qmd"
    )
    _, body = validator._front_matter_and_body(path)

    assert validator._validate_chapter_eleven_body(f"{body}\n\n{caution}\n") == []


def test_chapter_twelve_has_controlled_provenance_evidence_and_structure():
    path = (
        ROOT / "publication/content/02-estudio"
        / "12-dinero-oficios-conexiones-exteriores.qmd"
    )
    metadata, body = validator._front_matter_and_body(path)
    register = (
        ROOT / "project/30_RESULTADOS/ESTUDIO_HISTORICO"
        / "Registro_Afirmaciones_Calculos_v1.md"
    ).read_text(encoding="utf-8")
    registered = set(re.findall(r"^\|\s*([A-Z]+-\d{3})\s*\|", register, re.MULTILINE))

    assert metadata["title"] == "Dinero, oficios y conexiones exteriores"
    assert metadata["chapter-id"] == "dinero-oficios-conexiones-exteriores"
    assert metadata["publication-status"] == "development"
    assert {source["path"] for source in metadata["sources"]} == CHAPTER_TWELVE_SOURCES
    assert len(metadata["sources"]) == len(CHAPTER_TWELVE_SOURCES)
    assert all(source["locator"] for source in metadata["sources"])
    evidence = {level: tuple(values or []) for level, values in metadata["evidence"].items()}
    assert evidence == CHAPTER_TWELVE_EVIDENCE
    assert set(evidence) == {"D", "C", "I", "E", "L"}
    assert {item for group in evidence.values() for item in group} <= registered
    assert all(
        validator._markdown_section(body, anchor)
        for anchor in validator.CHAPTER_TWELVE_ANCHORS
    )
    normalized = validator._normalized_text(body)
    assert "633 + 233 + 140 = 1.006" in normalized
    assert "15 + 10 = 25" in normalized
    assert "25 \\div 233 \\times 100 = 10{,}73" in normalized
    assert "25 \\div 1.006 \\times 100 = 2{,}49" in normalized
    assert "el capítulo 13 realizará la síntesis integrada" in normalized
    assert "(11-hacienda-concejil-servicios-colectivos.qmd" in body
    assert not re.search(r"<[A-Za-z][^>]*>", body)
    assert validator._validate_chapter_twelve_body(body) == []


@pytest.mark.parametrize(
    ("mutation", "expected_code"),
    (
        (
            "La presencia de moneda demostraba una economía plenamente monetizada.",
            "C12_CURRENCY_IS_FULL_MONETIZATION",
        ),
        (
            "La valoración monetaria era un pago efectivamente realizado.",
            "C12_VALUATION_IS_EFFECTIVE_PAYMENT",
        ),
        (
            "La utilidad regulada era un ingreso real de los hogares.",
            "C12_UTILITY_IS_REAL_INCOME",
        ),
        (
            "El jornal diario era el ingreso anual del jornalero.",
            "C12_DAILY_WAGE_IS_ANNUAL_INCOME",
        ),
        (
            "El ingreso anual se obtiene multiplicando el jornal por 365 días.",
            "C12_ASSUMED_WORKDAYS",
        ),
        (
            "Todo labrador era propietario de tierras.",
            "C12_LABRADOR_IS_LANDOWNER",
        ),
        (
            "Cada jornalero era un asalariado permanente.",
            "C12_JORNALERO_IS_PERMANENT_EMPLOYEE",
        ),
        (
            "El oficio de herrero demostraba dedicación exclusiva.",
            "C12_CRAFT_IS_EXCLUSIVE_OCCUPATION",
        ),
        (
            "Los 18 jornaleros y 24 labradores sumaban 43 trabajadores.",
            "C12_OVERLAPPING_LABOR_SUM",
        ),
        (
            "Esas categorías formaban una población activa moderna.",
            "C12_MODERN_ACTIVE_POPULATION",
        ),
        (
            "Las utilidades permiten calcular la renta familiar anual.",
            "C12_UNSUPPORTED_FAMILY_INCOME",
        ),
        (
            "Las utilidades fiscales medían la riqueza y el nivel de vida.",
            "C12_FISCAL_UTILITY_IS_WEALTH",
        ),
        (
            "La presencia de Joaquín Aguado demostraba una relación comercial exterior.",
            "C12_EXTERNAL_PERSON_IS_COMMERCE",
        ),
        (
            "La mención de Valladolid demostraba un flujo económico estable.",
            "C12_PLACE_MENTION_IS_FLOW",
        ),
        (
            "En Sorribos había un mercado local regular.",
            "C12_REGULAR_MARKET",
        ),
        (
            "El lugar exportaba cereal e importaba manufacturas.",
            "C12_UNSUPPORTED_EXPORTS_IMPORTS",
        ),
        (
            "La ausencia de mercaderes demostraba la autosuficiencia del lugar.",
            "C12_ABSENCE_PROVES_SELF_SUFFICIENCY",
        ),
        (
            "Los 633 reales de alcabalas eran un ingreso laboral.",
            "C12_FISCAL_AMOUNT_IS_LABOR_INCOME",
        ),
        (
            "Los 233 reales del común eran un ingreso general de la localidad.",
            "C12_COMMON_EXPENSE_IS_LOCAL_INCOME",
        ),
        (
            "Los 1.006 reales comprendían toda la circulación monetaria.",
            "C12_EVIDENCE_LIMITS_ERASED",
        ),
        (
            "La pluriactividad hizo resiliente la economía rural.",
            "C12_CHAPTER_THIRTEEN_BOUNDARY",
        ),
    ),
)
def test_chapter_twelve_rejects_twenty_one_semantic_reversals(mutation, expected_code):
    path = (
        ROOT / "publication/content/02-estudio"
        / "12-dinero-oficios-conexiones-exteriores.qmd"
    )
    _, body = validator._front_matter_and_body(path)

    assert error_codes(
        validator._validate_chapter_twelve_body(f"{body}\n\n{mutation}\n")
    ) == {expected_code}


@pytest.mark.parametrize(
    "caution",
    (
        "La moneda no demostraba una economía plenamente monetizada.",
        "La valoración monetaria no era un pago efectivamente realizado.",
        "La utilidad regulada no era un ingreso real ni el jornal diario era ingreso anual.",
        "No se obtiene ingreso anual multiplicando el jornal por 365 días.",
        "El labrador no era necesariamente propietario de tierras.",
        "El jornalero no era necesariamente un asalariado permanente.",
        "El oficio de herrero no demostraba dedicación exclusiva.",
        "No se sostiene que 18 jornaleros y 24 labradores sumaban 43 trabajadores.",
        "Las categorías no formaban una población activa moderna.",
        "Las utilidades no permiten calcular la renta familiar anual.",
        "Las utilidades fiscales no medían riqueza ni nivel de vida.",
        "La presencia de Joaquín Aguado no demostraba una relación comercial exterior.",
        "La mención de Valladolid no demostraba un flujo económico estable.",
        "No había un mercado local regular documentado.",
        "No consta que el lugar exportaba cereal e importaba manufacturas.",
        "La ausencia de mercaderes no demostraba autosuficiencia.",
        "Los 633 reales de alcabalas no eran ingreso laboral.",
        "Los 233 reales del común no eran ingreso general de la localidad.",
        "Los 1.006 reales no comprendían toda la circulación monetaria.",
        "La pluriactividad no hizo resiliente la economía rural.",
    ),
)
def test_chapter_twelve_accepts_bounded_cautionary_formulations(caution):
    path = (
        ROOT / "publication/content/02-estudio"
        / "12-dinero-oficios-conexiones-exteriores.qmd"
    )
    _, body = validator._front_matter_and_body(path)

    assert validator._validate_chapter_twelve_body(f"{body}\n\n{caution}\n") == []


def test_chapter_thirteen_has_controlled_provenance_evidence_and_structure():
    path = (
        ROOT / "publication/content/02-estudio"
        / "13-economia-rural-integrada-vulnerabilidades-resiliencia-limites.qmd"
    )
    metadata, body = validator._front_matter_and_body(path)
    register = (
        ROOT / "project/30_RESULTADOS/ESTUDIO_HISTORICO"
        / "Registro_Afirmaciones_Calculos_v1.md"
    ).read_text(encoding="utf-8")
    registered = set(re.findall(r"^\|\s*([A-Z]+-\d{3})\s*\|", register, re.MULTILINE))

    assert metadata["title"] == (
        "Una economía rural integrada: vulnerabilidades, resiliencia y límites"
    )
    assert metadata["chapter-id"] == (
        "economia-rural-integrada-vulnerabilidades-resiliencia-limites"
    )
    assert metadata["publication-status"] == "development"
    assert {source["path"] for source in metadata["sources"]} == CHAPTER_THIRTEEN_SOURCES
    assert len(metadata["sources"]) == len(CHAPTER_THIRTEEN_SOURCES)
    assert all(source["locator"] for source in metadata["sources"])
    evidence = {level: tuple(values or []) for level, values in metadata["evidence"].items()}
    assert evidence == CHAPTER_THIRTEEN_EVIDENCE
    assert set(evidence) == {"D", "C", "I", "E", "L"}
    assert {item for group in evidence.values() for item in group} <= registered
    assert all(
        validator._markdown_section(body, anchor)
        for anchor in validator.CHAPTER_THIRTEEN_ANCHORS
    )
    normalized = validator._normalized_text(body)
    assert "2.750,5 de 2.953,5 medidas principales" in normalized
    assert "mínimo institucional de 1.006 reales" in normalized
    assert "no se afirma que el sistema fuera resiliente" in normalized
    assert "con esta síntesis concluye la parte ii" in normalized
    assert "(12-dinero-oficios-conexiones-exteriores.qmd" in body
    assert "../../generated/14-facsimil.qmd" in body
    assert not re.search(r"<[A-Za-z][^>]*>", body)
    assert validator._validate_chapter_thirteen_body(body) == []


@pytest.mark.parametrize(
    ("mutation", "expected_code"),
    (
        (
            "La integración interna demostraba una economía integrada en mercados regionales.",
            "C13_INTERNAL_IS_MARKET_INTEGRATION",
        ),
        (
            "La diversidad demostraba que el sistema era resiliente.",
            "C13_DIVERSITY_IS_RESILIENCE",
        ),
        (
            "La falta de datos demostraba la vulnerabilidad de la comunidad.",
            "C13_ABSENCE_IS_VULNERABILITY",
        ),
        (
            "La dependencia hidráulica demuestra que hubo una crisis general.",
            "C13_DEPENDENCY_IS_OBSERVED_CRISIS",
        ),
        (
            "La comunidad era autosuficiente en alimentos.",
            "C13_FOOD_SELF_SUFFICIENCY",
        ),
        (
            "La comunidad era autosuficiente en energía.",
            "C13_ENERGY_SELF_SUFFICIENCY",
        ),
        (
            "La economía era económicamente autosuficiente.",
            "C13_GENERAL_SELF_SUFFICIENCY",
        ),
        (
            "El sistema era sostenible.",
            "C13_SUSTAINABILITY",
        ),
        (
            "Existía un equilibrio ecológico entre ganado y recursos.",
            "C13_ECOLOGICAL_BALANCE",
        ),
        (
            "El expediente permite calcular la productividad total.",
            "C13_TOTAL_PRODUCTIVITY",
        ),
        (
            "El expediente permite calcular la renta por habitante.",
            "C13_PER_CAPITA_INCOME",
        ),
        (
            "El expediente permite calcular la renta por hogar.",
            "C13_HOUSEHOLD_INCOME",
        ),
        (
            "El expediente permite medir el nivel de vida.",
            "C13_LIVING_STANDARD",
        ),
        (
            "El expediente permite medir la desigualdad general.",
            "C13_INEQUALITY",
        ),
        (
            "Las valoraciones fiscales eran la producción efectiva.",
            "C13_VALUATION_IS_PRODUCTION",
        ),
        (
            "Las utilidades eran ingresos efectivos de los hogares.",
            "C13_UTILITY_IS_EFFECTIVE_INCOME",
        ),
        (
            "Las conexiones exteriores demostraban un comercio regular.",
            "C13_EXTERNAL_IS_REGULAR_TRADE",
        ),
        (
            "La variedad de oficios demostraba diversificación por hogar.",
            "C13_TRADES_ARE_HOUSEHOLD_DIVERSIFICATION",
        ),
        (
            "El predominio del centeno demostraba un monocultivo.",
            "C13_RYE_IS_MONOCULTURE",
        ),
        (
            "El uso común demostraba la propiedad comunal de los montes.",
            "C13_COMMON_USE_IS_PROPERTY",
        ),
        (
            "La presencia de molinos garantizaba suficiencia de transformación.",
            "C13_MILLS_ARE_SUFFICIENT",
        ),
        (
            "Los 1.006 reales medían la presión fiscal total.",
            "C13_PARTIAL_FISCAL_IS_TOTAL",
        ),
        (
            "Los 233 reales eran el presupuesto completo del común.",
            "C13_PARTIAL_COMMON_IS_BUDGET",
        ),
        (
            "La fiscalidad causó la caída de la producción.",
            "C13_UNSUPPORTED_CAUSALITY",
        ),
        (
            "La reconstrucción es completa y sin lagunas.",
            "C13_EVIDENCE_LIMITS_ERASED",
        ),
    ),
)
def test_chapter_thirteen_rejects_twenty_five_semantic_reversals(
    mutation, expected_code
):
    path = (
        ROOT / "publication/content/02-estudio"
        / "13-economia-rural-integrada-vulnerabilidades-resiliencia-limites.qmd"
    )
    _, body = validator._front_matter_and_body(path)

    assert error_codes(
        validator._validate_chapter_thirteen_body(f"{body}\n\n{mutation}\n")
    ) == {expected_code}


@pytest.mark.parametrize(
    "caution",
    (
        "La integración interna no demostraba una economía integrada en mercados regionales.",
        "La diversidad no demostraba que el sistema era resiliente.",
        "La falta de datos no demostraba vulnerabilidad histórica.",
        "La dependencia hidráulica no demuestra que hubo una crisis general.",
        "La comunidad no era autosuficiente en alimentos.",
        "La comunidad no era autosuficiente en energía.",
        "La economía no era económicamente autosuficiente.",
        "El sistema no era sostenible.",
        "No existía un equilibrio ecológico demostrado entre ganado y recursos.",
        "El expediente no permite calcular la productividad total.",
        "El expediente no permite calcular la renta por habitante.",
        "El expediente no permite calcular la renta por hogar.",
        "El expediente no permite medir el nivel de vida.",
        "El expediente no permite medir la desigualdad general.",
        "Las valoraciones fiscales no eran producción efectiva.",
        "Las utilidades no eran ingresos efectivos de los hogares.",
        "Las conexiones exteriores no demostraban comercio regular.",
        "La variedad de oficios no demostraba diversificación por hogar.",
        "El predominio del centeno no demostraba un monocultivo.",
        "El uso común no demostraba propiedad comunal de los montes.",
        "La presencia de molinos no garantizaba suficiencia de transformación.",
        "Los 1.006 reales no medían la presión fiscal total.",
        "Los 233 reales no eran el presupuesto completo del común.",
        "La fiscalidad no causó la caída de la producción.",
        "La reconstrucción no es completa ni está sin lagunas.",
    ),
)
def test_chapter_thirteen_accepts_twenty_five_bounded_cautions(caution):
    path = (
        ROOT / "publication/content/02-estudio"
        / "13-economia-rural-integrada-vulnerabilidades-resiliencia-limites.qmd"
    )
    _, body = validator._front_matter_and_body(path)

    assert validator._validate_chapter_thirteen_body(f"{body}\n\n{caution}\n") == []


PART_TWO_PATHS = {
    5: "05-lugar-senorio-concejo-ordas.qmd",
    6: "06-vecinos-hogares-viviendas-trabajo.qmd",
    7: "07-tierra-sistema-agrario-medidas.qmd",
    8: "08-ganaderia-montes-aprovechamientos-comunales.qmd",
    9: "09-rio-molinos-recursos.qmd",
    10: "10-iglesia-senorio-fiscalidad.qmd",
    11: "11-hacienda-concejil-servicios-colectivos.qmd",
    12: "12-dinero-oficios-conexiones-exteriores.qmd",
    13: "13-economia-rural-integrada-vulnerabilidades-resiliencia-limites.qmd",
}


def part_two_bodies() -> dict[int, str]:
    return {
        number: validator._front_matter_and_body(
            ROOT / "publication/content/02-estudio" / filename
        )[1]
        for number, filename in PART_TWO_PATHS.items()
    }


def test_part_two_cross_chapter_consistency_is_preserved():
    assert validator._validate_part_two_consistency(part_two_bodies()) == []


@pytest.mark.parametrize(
    ("number", "phrase"),
    (
        (5, "no paga cosa alguna al señor por el establecimiento del suelo"),
        (6, "no se suman para formar una población activa"),
        (7, "no permite deducir autoconsumo, suficiencia alimentaria"),
        (8, "no acreditan por sí solas titularidad"),
        (9, "ocho ruedas descritas en cuatro casas de molinos"),
        (10, "no pueden calcularse carga por vecino o por habitante, presión fiscal"),
        (11, "no son ingresos, gastos totales ni presupuesto completo"),
        (12, "tampoco demuestra una comunidad autosuficiente o cerrada"),
        (13, "esta integración interna no demuestra integración comercial"),
    ),
)
def test_part_two_cross_chapter_guard_rejects_lost_cautions(number, phrase):
    bodies = part_two_bodies()
    assert phrase in validator._normalized_text(bodies[number])
    bodies[number] = validator._normalized_text(bodies[number]).replace(
        phrase, "cautela retirada", 1
    )

    assert error_codes(validator._validate_part_two_consistency(bodies)) == {
        f"PART_TWO_C{number}_CONSISTENCY"
    }


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
        "publication/generated/ contiene derivados.\n\n"
        "El facsímil no reproduce la imagen, mientras la transcripción conserva "
        "el texto."
    )

    assert paragraphs[0][1] == (
        "son indistinguibles: facsímil y transcripción.",
    )
    assert paragraphs[1][1] == (
        "publication/content/ contiene texto editorial",
        "publication/generated/ contiene derivados.",
    )
    assert paragraphs[2][1] == (
        "el facsímil no reproduce la imagen",
        "mientras la transcripción conserva el texto.",
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
        "Está completamente documentada la evolución fonética.",
        "La evolución fonética está completamente documentada.",
        "Sí está documentada por completo la evolución fonética.",
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


def test_chapter_three_rejects_positive_phonetic_claim_in_separate_paragraph():
    path = ROOT / "publication/content/01-catastro/03-expediente-sorribos-santibanez.qmd"
    _, body = validator._front_matter_and_body(path)
    mutated = replace_once(
        body,
        r"no\s+proporciona\s+una\s+secuencia\s+fonética\s+completa",
        "No se dispone de una evolución fonética completamente documentada.\n\n"
        "La evolución fonética está completamente documentada.",
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
        "no se dispone de una evolución fonética completamente documentada",
        "de una evolución fonética completamente documentada no se dispone",
        "una evolución fonética completamente documentada no está disponible",
        "la evolución fonética no está completamente documentada",
        "no proporciona una secuencia fonética completa",
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
    "coordinated_functions",
    (
        "El facsímil no reproduce la imagen, mientras la transcripción conserva "
        "el texto línea por línea.",
        "Mientras la transcripción conserva el texto línea por línea, el facsímil "
        "no reproduce la imagen.",
        "La transcripción no fija el texto línea por línea, mientras el facsímil "
        "reproduce la imagen.",
        "Mientras el facsímil reproduce la imagen, la transcripción no fija el "
        "texto línea por línea.",
    ),
)
def test_chapter_four_does_not_cross_layer_function_subclauses(
    coordinated_functions,
):
    path = ROOT / "publication/content/01-catastro/04-manuscrito-volumen-actual.qmd"
    _, body = validator._front_matter_and_body(path)
    replacement = (
        "Las cuatro representaciones cumplen funciones distintas.\n\n"
        f"{coordinated_functions}\n\n"
        "La edición crítica reúne el aparato y documenta decisiones.\n\n"
        "La edición modernizada ofrece una lectura en español actual."
    )
    mutated = replace_section(body, "volumen-cuatro-accesos", replacement)

    assert error_codes(validator._validate_chapter_four_body(mutated)) == {
        "C4_LAYER_FUNCTIONS"
    }


@pytest.mark.parametrize(
    "coordinated_functions",
    (
        "El facsímil reproduce la imagen, mientras la transcripción fija el texto "
        "línea por línea.",
        "Mientras la transcripción fija el texto línea por línea, el facsímil "
        "reproduce la imagen.",
    ),
)
def test_chapter_four_accepts_affirmed_layer_function_subclauses(
    coordinated_functions,
):
    path = ROOT / "publication/content/01-catastro/04-manuscrito-volumen-actual.qmd"
    _, body = validator._front_matter_and_body(path)
    replacement = (
        "Las cuatro representaciones cumplen funciones distintas.\n\n"
        f"{coordinated_functions}\n\n"
        "La edición crítica reúne el aparato y documenta decisiones.\n\n"
        "La edición modernizada ofrece una lectura en español actual."
    )
    mutated = replace_section(body, "volumen-cuatro-accesos", replacement)

    assert validator._validate_chapter_four_body(mutated) == []


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
        "publication/generated/ no contiene la fuente editorial mantenida "
        "manualmente, mientras publication/content/ sí contiene texto editorial "
        "mantenido humanamente. Los derivados reproducibles se regeneran en "
        "publication/generated/. Ninguna autoridad canónica propia corresponde a "
        "esos derivados.",
        "publication/content/ sí contiene texto editorial mantenido humanamente, "
        "mientras publication/generated/ no contiene la fuente editorial mantenida "
        "manualmente. Los derivados reproducibles se regeneran en "
        "publication/generated/. Ninguna autoridad canónica propia corresponde a "
        "esos derivados.",
        "publication/content/ contiene texto editorial mantenido humanamente. "
        "publication/generated/ contiene derivados reproducibles que se regeneran. "
        "Ninguna autoridad canónica propia corresponde a esos derivados.",
    ),
)
def test_chapter_four_accepts_equivalent_directory_relations(replacement):
    path = ROOT / "publication/content/01-catastro/04-manuscrito-volumen-actual.qmd"
    _, body = validator._front_matter_and_body(path)
    mutated = replace_section(body, "volumen-content-generated", replacement)

    assert validator._validate_chapter_four_body(mutated) == []


@pytest.mark.parametrize(
    "mutation",
    (
        "publication/generated/ sí contiene la fuente editorial mantenida "
        "manualmente, mientras publication/content/ no la contiene.",
        "publication/content/ contiene salidas regenerables que se regeneran, "
        "mientras publication/generated/ no las contiene.",
    ),
)
def test_chapter_four_rejects_inverted_directory_function_subclauses(mutation):
    path = ROOT / "publication/content/01-catastro/04-manuscrito-volumen-actual.qmd"
    _, body = validator._front_matter_and_body(path)

    assert error_codes(
        validator._validate_chapter_four_body(f"{body}\n\n{mutation}\n")
    ) == {"C4_DIRECTORY_FUNCTIONS_REVERSED"}


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


def test_asset_manifest_preserves_prototype_and_adds_phase_4_series():
    manifest = yaml.safe_load(
        (ROOT / "publication" / "meta" / "assets.yml").read_text(encoding="utf-8")
    )
    assert [asset["asset_id"] for asset in manifest["assets"]] == [
        "manuscript-page-12",
        "folio-315v",
        "manuscript-pages-1-18",
        "critical-edition-unit-images",
    ]
    assert all(asset["source"]["page"] == 12 for asset in manifest["assets"][:2])
    assert manifest["assets"][2]["source"]["pages"] == [1, 18]
    assert manifest["assets"][3]["source"]["pages"] == [1, 18]
    assert all(
        (asset.get("destination") or asset.get("destination_pattern")).startswith(
            "generated/assets/"
        )
        for asset in manifest["assets"]
    )


def test_navigation_integrates_real_chapters_and_keeps_prototype_off_book():
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
        "content/02-estudio/05-lugar-senorio-concejo-ordas.qmd",
        "content/02-estudio/06-vecinos-hogares-viviendas-trabajo.qmd",
        "content/02-estudio/07-tierra-sistema-agrario-medidas.qmd",
        "content/02-estudio/08-ganaderia-montes-aprovechamientos-comunales.qmd",
        "content/02-estudio/09-rio-molinos-recursos.qmd",
        "content/02-estudio/10-iglesia-senorio-fiscalidad.qmd",
        "content/02-estudio/11-hacienda-concejil-servicios-colectivos.qmd",
        "content/02-estudio/12-dinero-oficios-conexiones-exteriores.qmd",
        "content/02-estudio/13-economia-rural-integrada-vulnerabilidades-resiliencia-limites.qmd",
        "generated/14-facsimil.qmd",
        "generated/15-transcripcion.qmd",
        "generated/16-edicion-modernizada.qmd",
        "generated/glosario.qmd",
        "generated/cuadros-cuantitativos.qmd",
        "generated/concordancia.qmd",
        "generated/matriz-evidencia.qmd",
    ]

    assert [item for item in navigation if item in expected_order] == expected_order
    assert [item for item in manifest_paths if item in expected_order] == expected_order
    assert all(navigation.count(item) == 1 for item in expected_order)
    assert all(manifest_paths.count(item) == 1 for item in expected_order)
    chapter_ids = [chapter["chapter_id"] for chapter in manifest["chapters"]]
    assert len(chapter_ids) == len(set(chapter_ids))
    assert sum(item.startswith("generated/") for item in navigation) == 7
    assert not any("prototipo" in item for item in navigation)
    assert "generated/aparato-molinos.qmd" not in navigation
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
    assert "number-sections" not in read_front_matter(
        ROOT
        / "publication"
        / "content"
        / "02-estudio"
        / "05-lugar-senorio-concejo-ordas.qmd"
    )
    assert "number-sections" not in read_front_matter(
        ROOT
        / "publication"
        / "content"
        / "02-estudio"
        / "06-vecinos-hogares-viviendas-trabajo.qmd"
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

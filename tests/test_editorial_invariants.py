from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "project"
SECTIONS = ["### Imagen", "### Transcripción paleográfica", "### Observaciones editoriales", "### Notas paleográficas", "### Notas históricas", "### Referencias cruzadas"]


def test_state_and_unit_sequence_are_preserved():
    state = yaml.safe_load((PROJECT / "00_CONTROL" / "estado.yaml").read_text(encoding="utf-8"))
    units = yaml.safe_load((PROJECT / "00_CONTROL" / "unidades.yaml").read_text(encoding="utf-8"))
    assert state["current_unit"] == "portada"
    assert state["current_location"] == {"pdf_page": 1, "position": "complete"}
    assert state["operation"]["status"] == "clean"
    assert state["last_validated_unit"] is None
    assert state["last_closed_unit"] is None
    assert units["unit_count"] == 35
    assert len(units["units"]) == 35
    assert [row["order"] for row in units["units"]] == list(range(1, 36))


def test_manual_and_edition_versions_and_structure_are_preserved():
    manual = (PROJECT / "00_CONTROL" / "Manual_Editorial.md").read_text(encoding="utf-8")
    edition = (PROJECT / "20_TRABAJO_EDITORIAL" / "Edicion_Critica.md").read_text(encoding="utf-8")
    assert "**Versión:** 1.5" in manual
    assert "**Versión:** 3.4" in edition
    for section in SECTIONS:
        assert edition.count(section) == 35


def test_diary_glossary_indexes_and_history_exist():
    required = [
        PROJECT / "20_TRABAJO_EDITORIAL" / "Diario_Editorial.md",
        PROJECT / "20_TRABAJO_EDITORIAL" / "Glosario.md",
        PROJECT / "20_TRABAJO_EDITORIAL" / "INDICES" / "Indice_Personas.md",
        PROJECT / "20_TRABAJO_EDITORIAL" / "INDICES" / "Indice_Toponimos.md",
        PROJECT / "20_TRABAJO_EDITORIAL" / "INDICES" / "Indice_Instituciones.md",
        PROJECT / "20_TRABAJO_EDITORIAL" / "INDICES" / "Indice_Medidas.md",
        PROJECT / "20_TRABAJO_EDITORIAL" / "INDICES" / "Indice_Oficios.md",
        PROJECT / "90_ARCHIVO" / "PREMIGRACION_2026-08-31",
        PROJECT / "90_ARCHIVO" / "SISTEMA_SUSTITUIDO_2026-09-01",
        PROJECT / "90_ARCHIVO" / "SISTEMA_1_2_3" / "INSTRUCCIONES_PROYECTO.md",
    ]
    assert all(path.exists() for path in required)

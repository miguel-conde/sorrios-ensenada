from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "project"
SECTIONS = ["### Imagen", "### Transcripción paleográfica", "### Observaciones editoriales", "### Notas paleográficas", "### Notas históricas", "### Referencias cruzadas"]


def test_state_and_unit_sequence_are_coherent():
    state = yaml.safe_load((PROJECT / "00_CONTROL" / "estado.yaml").read_text(encoding="utf-8"))
    units = yaml.safe_load((PROJECT / "00_CONTROL" / "unidades.yaml").read_text(encoding="utf-8"))

    assert units["unit_count"] == 35
    assert len(units["units"]) == 35
    assert [row["order"] for row in units["units"]] == list(range(1, 36))

    ids = [row["id"] for row in units["units"]]
    current = state["current_unit"]
    assert state["operation"]["status"] == "clean"
    assert state["last_validated_unit"] == state["last_closed_unit"]

    if current is None:
        assert state["last_closed_unit"] == ids[-1]
        assert state["next_unit"] is None
        assert state["current_location"] is None
        assert state["pending_tasks"] == []
    else:
        assert current in ids
        current_index = ids.index(current)
        current_row = units["units"][current_index]

        assert state["current_location"] == {
            "pdf_page": current_row["pdf_page"],
            "position": current_row["position"],
        }
        expected_previous = None if current_index == 0 else ids[current_index - 1]
        expected_next = None if current_index == len(ids) - 1 else ids[current_index + 1]
        assert state["last_closed_unit"] == expected_previous
        assert state["next_unit"] == expected_next


def test_historical_study_phase_is_active_and_coherent():
    project = yaml.safe_load((PROJECT / "00_CONTROL" / "proyecto.yaml").read_text(encoding="utf-8"))
    state = yaml.safe_load((PROJECT / "00_CONTROL" / "estado.yaml").read_text(encoding="utf-8"))
    study = (PROJECT / "30_RESULTADOS" / "ESTUDIO_HISTORICO" / "Estudio_Historico.md").read_text(encoding="utf-8")

    assert project["phase"]["current"] == "estudio_historico"
    assert project["phase"]["historical_study_enabled"] is True
    assert project["documents"]["historical_study"]["enabled"] is True
    assert state["phase"] == "estudio_historico"
    assert state["current_unit"] is None
    assert state["open_issues"] == []
    assert state["pending_tasks"] == []
    assert "**Estado:** activo" in study
    assert "base documental del Estudio Histórico es exclusivamente la edición paleográfica validada" in study


def test_manual_and_edition_versions_and_structure_are_preserved():
    project = yaml.safe_load((PROJECT / "00_CONTROL" / "proyecto.yaml").read_text(encoding="utf-8"))
    manual = (PROJECT / "00_CONTROL" / "Manual_Editorial.md").read_text(encoding="utf-8")
    edition = (PROJECT / "20_TRABAJO_EDITORIAL" / "Edicion_Critica.md").read_text(encoding="utf-8")

    manual_version = project["authorities"]["manual"]["version"]
    edition_version = project["documents"]["edition"]["version"]
    assert f"**Versión:** {manual_version}" in manual
    assert f"**Versión:** {edition_version}" in edition
    assert f"**Manual aplicable:** Manual Editorial v{manual_version}" in edition
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

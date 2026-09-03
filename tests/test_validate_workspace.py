import hashlib
from pathlib import Path, PurePosixPath

import yaml

from validate_workspace import REQUIRED, SECTIONS, SOURCE_PDF, validate_workspace


CANONICAL_DRIVE_MANUSCRIPT_PATH = (
    "10_FUENTE_PRIMARIA/"
    "sorrios_ensenada_orden_lectura_calidad_original.pdf"
)


def build_workspace(root: Path, *, source_path: str | None = None) -> None:
    root.mkdir()
    for relative in REQUIRED:
        path = root.joinpath(relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("", encoding="utf-8")

    pdf_bytes = b"portable-pdf-fixture"
    pdf = root.joinpath(SOURCE_PDF)
    pdf.write_bytes(pdf_bytes)
    logical_source = PurePosixPath(*SOURCE_PDF.parts).as_posix()
    project = {
        "authorities": {
            "manuscript": {
                "path": source_path or logical_source,
                "size_bytes": len(pdf_bytes),
                "sha256": hashlib.sha256(pdf_bytes).hexdigest(),
            }
        }
    }
    root.joinpath("00_CONTROL", "proyecto.yaml").write_text(
        yaml.safe_dump(project), encoding="utf-8"
    )

    units = [
        {
            "id": f"unit_{number}",
            "order": number,
            "pdf_page": number,
            "position": "complete",
        }
        for number in range(1, 36)
    ]
    root.joinpath("00_CONTROL", "unidades.yaml").write_text(
        yaml.safe_dump({"unit_count": 35, "units": units}),
        encoding="utf-8",
    )
    state = {
        "current_unit": "unit_1",
        "current_location": {"pdf_page": 1, "position": "complete"},
        "last_closed_unit": None,
        "last_validated_unit": None,
        "operation": {"status": "clean"},
    }
    root.joinpath("00_CONTROL", "estado.yaml").write_text(
        yaml.safe_dump(state), encoding="utf-8"
    )

    edition = "\n".join(
        section for _ in range(35) for section in SECTIONS
    )
    root.joinpath("20_TRABAJO_EDITORIAL", "Edicion_Critica.md").write_text(
        edition, encoding="utf-8"
    )


def test_complete_workspace_is_valid(tmp_path):
    root = tmp_path.joinpath("Sorríos con espacios")
    build_workspace(root)

    assert validate_workspace(root) == []


def test_existing_backslash_logical_path_is_accepted(tmp_path):
    root = tmp_path.joinpath("workspace")
    source_path = str(PurePosixPath(*SOURCE_PDF.parts)).replace("/", "\\")
    build_workspace(root, source_path=source_path)

    assert validate_workspace(root) == []


def test_canonical_drive_manuscript_path_is_accepted(tmp_path):
    root = tmp_path.joinpath("workspace")
    build_workspace(root, source_path=CANONICAL_DRIVE_MANUSCRIPT_PATH)

    assert validate_workspace(root) == []


def test_missing_required_file_is_reported_canonically(tmp_path):
    root = tmp_path.joinpath("workspace")
    build_workspace(root)
    root.joinpath("00_CONTROL", "CAMBIOS.md").unlink()

    assert validate_workspace(root) == ["Falta 00_CONTROL/CAMBIOS.md"]


def test_wrong_logical_source_path_is_rejected(tmp_path):
    root = tmp_path.joinpath("workspace")
    build_workspace(root, source_path="10_FUENTE_PRIMARIA/otro.pdf")

    assert "La ruta lógica del PDF autoritativo es incorrecta" in (
        validate_workspace(root)
    )

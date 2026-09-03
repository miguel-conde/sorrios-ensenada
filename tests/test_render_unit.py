import os
from pathlib import Path

import pytest
import yaml
from PIL import Image

import render_unit as renderer


def prepare_inputs(tmp_path: Path, position: str) -> tuple[Path, Path, Path]:
    pdf = tmp_path.joinpath("source document.pdf")
    pdf.write_bytes(b"pdf")
    units = tmp_path.joinpath("unidades.yaml")
    units.write_text(
        yaml.safe_dump(
            {
                "units": [
                    {
                        "id": "target",
                        "pdf_page": 2,
                        "position": position,
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    executable = tmp_path.joinpath("bin with spaces", "pdftoppm")
    executable.parent.mkdir()
    executable.write_text("", encoding="utf-8")
    return pdf, units, executable


def fake_pdftoppm(command, *, check, shell):
    assert check is True
    assert shell is False
    prefix = Path(command[-1])
    Image.new("RGB", (10, 4), "white").save(prefix.with_suffix(".png"))


@pytest.mark.parametrize(
    ("position", "expected_size"),
    [("left", (5, 4)), ("right", (5, 4)), ("complete", (10, 4))],
)
def test_rendering_uses_path_objects_and_crops(
    tmp_path, monkeypatch, position, expected_size
):
    pdf, units, executable = prepare_inputs(tmp_path, position)
    output = tmp_path.joinpath("nested output", f"{position}.png")
    monkeypatch.setattr(renderer.subprocess, "run", fake_pdftoppm)

    result = renderer.render_unit(
        pdf,
        units,
        "target",
        output,
        pdftoppm=executable,
    )

    assert result == output.resolve()
    with Image.open(result) as image:
        assert image.size == expected_size


def test_pdftoppm_is_detected_through_path(tmp_path, monkeypatch):
    executable = tmp_path.joinpath("pdftoppm")
    executable.write_text("", encoding="utf-8")
    monkeypatch.setattr(renderer.shutil, "which", lambda name: str(executable))

    assert renderer.find_pdftoppm() == executable.resolve()


def test_missing_pdftoppm_has_clear_error(monkeypatch):
    monkeypatch.setattr(renderer.shutil, "which", lambda name: None)

    with pytest.raises(renderer.RenderError, match="pdftoppm.*PATH"):
        renderer.find_pdftoppm()


def test_invalid_position_is_rejected(tmp_path, monkeypatch):
    pdf, units, executable = prepare_inputs(tmp_path, "diagonal")
    monkeypatch.setattr(renderer.subprocess, "run", fake_pdftoppm)

    with pytest.raises(renderer.RenderError, match="Posición inválida"):
        renderer.render_unit(
            pdf,
            units,
            "target",
            tmp_path.joinpath("output.png"),
            pdftoppm=executable,
        )


@pytest.mark.integration
def test_real_pdftoppm_pipeline_when_available(tmp_path):
    if renderer.shutil.which("pdftoppm") is None:
        if os.environ.get("REQUIRE_PDFTOPPM") == "1":
            pytest.fail("CI exige pdftoppm en PATH")
        pytest.skip("pdftoppm no está disponible en PATH")

    pdf = tmp_path.joinpath("source.pdf")
    Image.new("RGB", (40, 20), "white").save(pdf, "PDF")
    units = tmp_path.joinpath("unidades.yaml")
    units.write_text(
        yaml.safe_dump(
            {
                "units": [
                    {
                        "id": "target",
                        "pdf_page": 1,
                        "position": "left",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    output = tmp_path.joinpath("rendered.png")

    result = renderer.render_unit(pdf, units, "target", output, dpi=72)

    assert result.is_file()
    with Image.open(result) as image:
        assert image.width > 0
        assert image.height > 0

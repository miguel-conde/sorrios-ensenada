from pathlib import Path

import pytest
import yaml
from PIL import Image

import render_unit as renderer


def prepare_inputs(tmp_path: Path, position: str) -> tuple[Path, Path, Path]:
    pdf = tmp_path / "source document.pdf"
    pdf.write_bytes(b"pdf")
    units = tmp_path / "unidades.yaml"
    units.write_text(yaml.safe_dump({"units": [{"id": "target", "pdf_page": 2, "position": position}]}), encoding="utf-8")
    executable = tmp_path / "bin with spaces" / "pdftoppm"
    executable.parent.mkdir()
    executable.write_text("", encoding="utf-8")
    return pdf, units, executable


def fake_pdftoppm(command, *, check, shell):
    assert check is True
    assert shell is False
    prefix = Path(command[-1])
    Image.new("RGB", (10, 4), "white").save(prefix.with_suffix(".png"))


@pytest.mark.parametrize(("position", "expected_size"), [("left", (5, 4)), ("right", (5, 4)), ("complete", (10, 4))])
def test_rendering_crops_all_supported_positions(tmp_path, monkeypatch, position, expected_size):
    pdf, units, executable = prepare_inputs(tmp_path, position)
    output = tmp_path / "nested output" / f"{position}.png"
    monkeypatch.setattr(renderer.subprocess, "run", fake_pdftoppm)

    result = renderer.render_unit(pdf, units, "target", output, pdftoppm=executable)

    assert result == output.resolve()
    with Image.open(result) as image:
        assert image.size == expected_size


def test_pdftoppm_is_detected_through_path(tmp_path, monkeypatch):
    executable = tmp_path / "pdftoppm"
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
        renderer.render_unit(pdf, units, "target", tmp_path / "output.png", pdftoppm=executable)

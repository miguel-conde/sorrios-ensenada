#!/usr/bin/env python3
import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

from path_utils import normalize_physical_path


class RenderError(RuntimeError):
    """Raised when a unit cannot be rendered."""


def find_pdftoppm() -> Path:
    executable = shutil.which("pdftoppm")
    if executable is None:
        raise RenderError("No se encontró pdftoppm en PATH")
    return normalize_physical_path(Path(executable), strict=True)


def read_units(path: Path) -> list[dict]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("units"), list):
        raise RenderError("unidades.yaml no contiene una lista de unidades")
    return data["units"]


def render_unit(
    pdf: Path,
    units_file: Path,
    unit_id: str,
    output: Path,
    *,
    dpi: int = 220,
    pdftoppm: Path | None = None,
) -> Path:
    if dpi <= 0:
        raise RenderError("DPI debe ser mayor que cero")

    pdf = normalize_physical_path(pdf, strict=True)
    units_file = normalize_physical_path(units_file, strict=True)
    output = normalize_physical_path(output, strict=False)
    executable = (
        find_pdftoppm()
        if pdftoppm is None
        else normalize_physical_path(pdftoppm, strict=True)
    )

    unit = next(
        (item for item in read_units(units_file) if item.get("id") == unit_id),
        None,
    )
    if unit is None:
        raise RenderError(f"Unidad desconocida: {unit_id}")

    try:
        from PIL import Image
    except ModuleNotFoundError as exc:
        raise RenderError(
            "Falta Pillow; instala la dependencia opcional 'render'"
        ) from exc

    with tempfile.TemporaryDirectory() as temporary_directory:
        prefix = Path(temporary_directory).joinpath("page")
        subprocess.run(
            [
                executable,
                "-f",
                str(unit["pdf_page"]),
                "-singlefile",
                "-r",
                str(dpi),
                "-png",
                pdf,
                prefix,
            ],
            check=True,
            shell=False,
        )
        rendered_page = prefix.with_suffix(".png")
        with Image.open(rendered_page) as image:
            position = unit.get("position")
            if position == "left":
                result = image.crop((0, 0, image.width // 2, image.height))
            elif position == "right":
                result = image.crop(
                    (image.width // 2, 0, image.width, image.height)
                )
            elif position == "complete":
                result = image.copy()
            else:
                raise RenderError("Posición inválida")
            try:
                output.parent.mkdir(parents=True, exist_ok=True)
                result.save(output)
            finally:
                result.close()
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("units", type=Path)
    parser.add_argument("unit_id")
    parser.add_argument("output", type=Path)
    parser.add_argument("--dpi", type=int, default=220)
    args = parser.parse_args()

    try:
        output = render_unit(
            args.pdf,
            args.units,
            args.unit_id,
            args.output,
            dpi=args.dpi,
        )
    except (OSError, subprocess.CalledProcessError, RenderError, yaml.YAMLError) as exc:
        print(f"ERROR: {exc}")
        return 1
    print(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())

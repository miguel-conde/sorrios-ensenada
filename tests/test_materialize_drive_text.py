import hashlib
from pathlib import Path
import subprocess
import sys

import pytest

from materialize_drive_text import (
    DEFAULT_MAX_BYTES,
    TextMaterializationError,
    materialize_utf8,
)


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT.joinpath(
    "plugins",
    "sorrios-ensenada",
    "skills",
    "editar-catastro-sorrios",
    "scripts",
    "materialize_drive_text.py",
)


def test_cli_reads_utf8_from_standard_input(tmp_path):
    payload = "unidad: portada\nnota: Sorríos\n".encode()
    output = tmp_path / "unidades.yaml"

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            str(output),
            "--expected-size",
            str(len(payload)),
        ],
        input=payload,
        capture_output=True,
        check=False,
    )

    digest = hashlib.sha256(payload).hexdigest().encode()
    assert result.returncode == 0, result.stderr.decode()
    assert b"OK " in result.stdout
    assert b"size=" + str(len(payload)).encode() in result.stdout
    assert b"sha256=" + digest in result.stdout
    assert output.read_bytes() == payload


def test_rejects_invalid_utf8(tmp_path):
    output = tmp_path / "unidades.yaml"

    with pytest.raises(TextMaterializationError, match="valid UTF-8"):
        materialize_utf8(
            b"\xff",
            output,
            expected_size=1,
        )

    assert not output.exists()


def test_rejects_size_mismatch_without_partial_file(tmp_path):
    output = tmp_path / "unidades.yaml"

    with pytest.raises(TextMaterializationError, match="size mismatch"):
        materialize_utf8(
            b"unit: portada\n",
            output,
            expected_size=1,
        )

    assert not output.exists()
    assert not list(tmp_path.glob("*.partial"))


def test_rejects_declared_size_above_limit(tmp_path):
    with pytest.raises(TextMaterializationError, match="exceeds limit"):
        materialize_utf8(
            b"",
            tmp_path / "unidades.yaml",
            expected_size=DEFAULT_MAX_BYTES + 1,
        )


def test_does_not_overwrite_existing_output(tmp_path):
    output = tmp_path / "unidades.yaml"
    output.write_bytes(b"existing")

    with pytest.raises(TextMaterializationError, match="already exists"):
        materialize_utf8(
            b"replacement",
            output,
            expected_size=len(b"replacement"),
        )

    assert output.read_bytes() == b"existing"

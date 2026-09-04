import base64
import hashlib
from pathlib import Path
import subprocess
import sys

import pytest

from materialize_drive_payload import (
    DEFAULT_MAX_BYTES,
    MaterializationError,
    _expected_base64_length,
    materialize_base64,
)


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT.joinpath(
    "plugins",
    "sorrios-ensenada",
    "skills",
    "editar-catastro-sorrios",
    "scripts",
    "materialize_drive_payload.py",
)


def identity(payload):
    return len(payload), hashlib.sha256(payload).hexdigest()


def command(output, *, expected_size, expected_digest):
    return [
        sys.executable,
        str(SCRIPT),
        str(output),
        "--expected-size",
        str(expected_size),
        "--expected-sha256",
        expected_digest,
    ]


def assert_no_output_or_partials(output):
    assert not output.exists()
    assert not list(output.parent.glob(f".{output.name}.*.partial"))


def run_payload(output, encoded, *, expected_size, expected_digest):
    return subprocess.run(
        command(
            output,
            expected_size=expected_size,
            expected_digest=expected_digest,
        ),
        input=encoded,
        capture_output=True,
        check=False,
        timeout=3,
    )


@pytest.mark.parametrize(
    ("size", "encoded_length"),
    [(0, 0), (1, 4), (2, 4), (3, 4), (4, 8)],
)
def test_expected_base64_length(size, encoded_length):
    assert _expected_base64_length(size) == encoded_length


def test_materializes_verified_payload(tmp_path):
    payload = b"verified Drive payload\n"
    size, digest = identity(payload)
    output = tmp_path / "source.pdf"

    result = materialize_base64(
        base64.b64encode(payload),
        output,
        expected_size=size,
        expected_sha256=digest,
    )

    assert result == (size, digest)
    assert output.read_bytes() == payload


def test_subprocess_finishes_without_eof_when_payload_is_complete(tmp_path):
    payload = b"complete payload while stdin remains open"
    size, digest = identity(payload)
    encoded = base64.b64encode(payload)
    output = tmp_path / "source.pdf"
    process = subprocess.Popen(
        command(output, expected_size=size, expected_digest=digest),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert process.stdin is not None
    assert process.stdout is not None
    assert process.stderr is not None

    try:
        process.stdin.write(encoded)
        process.stdin.flush()
        return_code = process.wait(timeout=3)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait()
        pytest.fail("materializer waited for EOF after the complete payload")
    finally:
        process.stdin.close()

    stdout = process.stdout.read().decode("utf-8")
    stderr = process.stderr.read().decode("utf-8")
    assert return_code == 0, stderr
    assert "OK" in stdout
    assert f"size={size}" in stdout
    assert f"sha256={digest}" in stdout
    assert output.read_bytes() == payload


@pytest.mark.parametrize(
    ("expected_size", "expected_digest", "match"),
    [
        (8, hashlib.sha256(b"payload").hexdigest(), "size mismatch"),
        (7, "0" * 64, "SHA-256 mismatch"),
    ],
)
def test_rejects_identity_mismatch(
    tmp_path, expected_size, expected_digest, match
):
    output = tmp_path / "source.pdf"

    with pytest.raises(MaterializationError, match=match):
        materialize_base64(
            base64.b64encode(b"payload"),
            output,
            expected_size=expected_size,
            expected_sha256=expected_digest,
        )

    assert_no_output_or_partials(output)


def test_rejects_invalid_base64(tmp_path):
    output = tmp_path / "source.pdf"
    with pytest.raises(MaterializationError, match="invalid Base64"):
        materialize_base64(
            b"not-base64!!",
            output,
            expected_size=8,
            expected_sha256="0" * 64,
        )
    assert_no_output_or_partials(output)


def test_rejects_non_permitted_whitespace(tmp_path):
    output = tmp_path / "source.pdf"
    with pytest.raises(MaterializationError, match="Base64 length mismatch"):
        materialize_base64(
            b"YW\vJj",
            output,
            expected_size=3,
            expected_sha256=hashlib.sha256(b"abc").hexdigest(),
        )
    assert_no_output_or_partials(output)


def test_rejects_declared_size_above_limit(tmp_path):
    output = tmp_path / "source.pdf"
    with pytest.raises(MaterializationError, match="exceeds limit"):
        materialize_base64(
            b"",
            output,
            expected_size=DEFAULT_MAX_BYTES + 1,
            expected_sha256=hashlib.sha256(b"").hexdigest(),
        )
    assert_no_output_or_partials(output)


def test_does_not_overwrite_existing_output(tmp_path):
    output = tmp_path / "source.pdf"
    output.write_bytes(b"existing")
    payload = b"replacement"
    size, digest = identity(payload)

    with pytest.raises(MaterializationError, match="already exists"):
        materialize_base64(
            base64.b64encode(payload),
            output,
            expected_size=size,
            expected_sha256=digest,
        )

    assert output.read_bytes() == b"existing"
    assert not list(tmp_path.glob(f".{output.name}.*.partial"))


@pytest.mark.parametrize(
    ("encoded", "expected_size", "expected_digest", "error"),
    [
        (b"YQ", 1, hashlib.sha256(b"a").hexdigest(), "premature EOF"),
        (b"!!!!", 1, "0" * 64, "invalid Base64"),
        (
            base64.b64encode(b"abc"),
            2,
            hashlib.sha256(b"abc").hexdigest(),
            "size mismatch",
        ),
        (base64.b64encode(b"abc"), 3, "0" * 64, "SHA-256 mismatch"),
        (
            base64.b64encode(b"abc") + b"A",
            3,
            hashlib.sha256(b"abc").hexdigest(),
            "additional Base64 content",
        ),
    ],
)
def test_subprocess_rejects_invalid_inputs_without_partials(
    tmp_path, encoded, expected_size, expected_digest, error
):
    output = tmp_path / "source.pdf"
    result = run_payload(
        output,
        encoded,
        expected_size=expected_size,
        expected_digest=expected_digest,
    )

    assert result.returncode == 1
    assert error in result.stderr.decode("utf-8")
    assert_no_output_or_partials(output)


def test_subprocess_allows_ascii_spaces_tabs_and_line_breaks(tmp_path):
    payload = b"whitespace is allowed"
    size, digest = identity(payload)
    encoded = base64.b64encode(payload)
    wrapped = b" \t" + encoded[:8] + b"\r\n" + encoded[8:] + b" \n"
    output = tmp_path / "source.pdf"

    result = run_payload(
        output,
        wrapped,
        expected_size=size,
        expected_digest=digest,
    )

    assert result.returncode == 0, result.stderr.decode("utf-8")
    assert "OK" in result.stdout.decode("utf-8")
    assert output.read_bytes() == payload


def test_subprocess_rejects_declared_size_above_limit_without_partials(
    tmp_path,
):
    output = tmp_path / "source.pdf"
    result = run_payload(
        output,
        b"",
        expected_size=DEFAULT_MAX_BYTES + 1,
        expected_digest=hashlib.sha256(b"").hexdigest(),
    )

    assert result.returncode == 1
    assert "exceeds limit" in result.stderr.decode("utf-8")
    assert_no_output_or_partials(output)

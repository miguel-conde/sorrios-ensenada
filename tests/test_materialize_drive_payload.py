import base64
import hashlib

import pytest

from materialize_drive_payload import (
    DEFAULT_MAX_BYTES,
    MaterializationError,
    materialize_base64,
)


def identity(payload):
    return len(payload), hashlib.sha256(payload).hexdigest()


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


@pytest.mark.parametrize(
    ("expected_size", "expected_digest", "match"),
    [
        (1, hashlib.sha256(b"payload").hexdigest(), "size mismatch"),
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

    assert not output.exists()
    assert not list(tmp_path.glob("*.partial"))


def test_rejects_invalid_base64(tmp_path):
    with pytest.raises(MaterializationError, match="invalid Base64"):
        materialize_base64(
            b"not-base64!",
            tmp_path / "source.pdf",
            expected_size=1,
            expected_sha256="0" * 64,
        )


def test_rejects_declared_size_above_limit(tmp_path):
    with pytest.raises(MaterializationError, match="exceeds limit"):
        materialize_base64(
            b"",
            tmp_path / "source.pdf",
            expected_size=DEFAULT_MAX_BYTES + 1,
            expected_sha256=hashlib.sha256(b"").hexdigest(),
        )


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

#!/usr/bin/env python3
"""Materialize a bounded Base64 Drive payload and verify its identity."""

from __future__ import annotations

import argparse
import base64
import binascii
import hashlib
import os
from pathlib import Path
import sys
import tempfile


DEFAULT_MAX_BYTES = 8 * 1024 * 1024
MAX_WHITESPACE_BYTES = 64 * 1024


class MaterializationError(ValueError):
    """Raised when a payload cannot be materialized safely."""


def _sha256(value: str) -> str:
    normalized = value.lower()
    if len(normalized) != 64 or any(
        character not in "0123456789abcdef" for character in normalized
    ):
        raise argparse.ArgumentTypeError(
            "expected SHA-256 must contain exactly 64 hexadecimal characters"
        )
    return normalized


def materialize_base64(
    encoded: bytes,
    output: Path,
    *,
    expected_size: int,
    expected_sha256: str,
    max_bytes: int = DEFAULT_MAX_BYTES,
) -> tuple[int, str]:
    """Decode, verify, and atomically place a bounded Base64 payload."""
    if expected_size < 0:
        raise MaterializationError("expected size cannot be negative")
    if max_bytes < 1:
        raise MaterializationError("maximum size must be positive")
    if expected_size > max_bytes:
        raise MaterializationError(
            f"declared file size {expected_size} exceeds limit {max_bytes}"
        )
    if output.exists():
        raise MaterializationError(f"output already exists: {output}")

    compact = b"".join(encoded.split())
    maximum_encoded = 4 * ((max_bytes + 2) // 3)
    if len(compact) > maximum_encoded:
        raise MaterializationError("Base64 payload exceeds the configured limit")

    try:
        decoded = base64.b64decode(compact, validate=True)
    except (binascii.Error, ValueError) as error:
        raise MaterializationError("invalid Base64 payload") from error

    actual_size = len(decoded)
    if actual_size > max_bytes:
        raise MaterializationError(
            f"decoded file size {actual_size} exceeds limit {max_bytes}"
        )
    if actual_size != expected_size:
        raise MaterializationError(
            f"size mismatch: expected {expected_size}, got {actual_size}"
        )

    actual_sha256 = hashlib.sha256(decoded).hexdigest()
    if actual_sha256 != expected_sha256.lower():
        raise MaterializationError(
            f"SHA-256 mismatch: expected {expected_sha256.lower()}, "
            f"got {actual_sha256}"
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            dir=output.parent,
            prefix=f".{output.name}.",
            suffix=".partial",
            delete=False,
        ) as temporary:
            temporary.write(decoded)
            temporary.flush()
            temporary_path = Path(temporary.name)
        try:
            os.link(temporary_path, output)
        except FileExistsError as error:
            raise MaterializationError(
                f"output already exists: {output}"
            ) from error
        temporary_path.unlink()
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()

    return actual_size, actual_sha256


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Read a Base64 payload from standard input, verify it, and write "
            "the decoded file atomically."
        )
    )
    parser.add_argument("output", type=Path)
    parser.add_argument("--expected-size", type=int, required=True)
    parser.add_argument("--expected-sha256", type=_sha256, required=True)
    parser.add_argument(
        "--max-bytes",
        type=int,
        default=DEFAULT_MAX_BYTES,
        help=f"maximum decoded size (default: {DEFAULT_MAX_BYTES})",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        maximum_encoded = 4 * ((args.max_bytes + 2) // 3)
        maximum_input = maximum_encoded + MAX_WHITESPACE_BYTES
        encoded = sys.stdin.buffer.read(maximum_input + 1)
        if len(encoded) > maximum_input:
            raise MaterializationError(
                "Base64 input exceeds the configured limit"
            )
        actual_size, actual_sha256 = materialize_base64(
            encoded,
            args.output,
            expected_size=args.expected_size,
            expected_sha256=args.expected_sha256,
            max_bytes=args.max_bytes,
        )
    except MaterializationError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        f"OK {args.output} size={actual_size} sha256={actual_sha256}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

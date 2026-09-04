#!/usr/bin/env python3
"""Materialize bounded UTF-8 text received from an authenticated Drive read."""

from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path
import sys
import tempfile


DEFAULT_MAX_BYTES = 1024 * 1024


class TextMaterializationError(ValueError):
    """Raised when authenticated text cannot be materialized safely."""


def materialize_utf8(
    payload: bytes,
    output: Path,
    *,
    expected_size: int,
    max_bytes: int = DEFAULT_MAX_BYTES,
) -> tuple[int, str]:
    """Validate UTF-8 bytes and atomically place them without overwriting."""
    if expected_size < 0:
        raise TextMaterializationError("expected size cannot be negative")
    if max_bytes < 1:
        raise TextMaterializationError("maximum size must be positive")
    if expected_size > max_bytes:
        raise TextMaterializationError(
            f"declared file size {expected_size} exceeds limit {max_bytes}"
        )
    if output.exists():
        raise TextMaterializationError(f"output already exists: {output}")

    actual_size = len(payload)
    if actual_size > max_bytes:
        raise TextMaterializationError(
            f"text size {actual_size} exceeds limit {max_bytes}"
        )
    if actual_size != expected_size:
        raise TextMaterializationError(
            f"size mismatch: expected {expected_size}, got {actual_size}"
        )
    try:
        payload.decode("utf-8")
    except UnicodeDecodeError as error:
        raise TextMaterializationError("input is not valid UTF-8") from error

    actual_sha256 = hashlib.sha256(payload).hexdigest()
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
            temporary.write(payload)
            temporary.flush()
            temporary_path = Path(temporary.name)
        try:
            os.link(temporary_path, output)
        except FileExistsError as error:
            raise TextMaterializationError(
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
            "Read authenticated UTF-8 text from standard input, verify its "
            "size, and write it atomically."
        )
    )
    parser.add_argument("output", type=Path)
    parser.add_argument("--expected-size", type=int, required=True)
    parser.add_argument(
        "--max-bytes",
        type=int,
        default=DEFAULT_MAX_BYTES,
        help=f"maximum input size (default: {DEFAULT_MAX_BYTES})",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        payload = sys.stdin.buffer.read(args.max_bytes + 1)
        if len(payload) > args.max_bytes:
            raise TextMaterializationError(
                "text input exceeds the configured limit"
            )
        actual_size, actual_sha256 = materialize_utf8(
            payload,
            args.output,
            expected_size=args.expected_size,
            max_bytes=args.max_bytes,
        )
    except TextMaterializationError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        f"OK {args.output} size={actual_size} sha256={actual_sha256}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

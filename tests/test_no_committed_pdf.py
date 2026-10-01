import os
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_IGNORED_PDF_PREFIXES = ("publication/_book/",)
PROHIBITED_CHECKOUT_PDF_NAMES = {
    "manuscript.pdf",
    "sorrios_ensenada_orden_lectura_calidad_original.pdf",
}


def _git_pdf_paths(root: Path, *selectors: str) -> tuple[str, ...]:
    result = subprocess.run(
        ["git", "-C", root, "ls-files", "-z", *selectors, "--", "*.pdf"],
        check=True,
        stdout=subprocess.PIPE,
    )
    return tuple(
        sorted(
            os.fsdecode(entry)
            for entry in result.stdout.split(b"\0")
            if entry
        )
    )


def pdf_policy_violations(root: Path) -> dict[str, tuple[str, ...]]:
    tracked_or_staged = _git_pdf_paths(root, "--cached")
    untracked_and_not_ignored = _git_pdf_paths(
        root, "--others", "--exclude-standard"
    )
    ignored = _git_pdf_paths(
        root, "--others", "--ignored", "--exclude-standard"
    )
    ignored_outside_reproducible_outputs = tuple(
        path
        for path in ignored
        if not path.startswith(ALLOWED_IGNORED_PDF_PREFIXES)
    )
    prohibited_manuscript_replicas = tuple(
        path
        for path in ignored
        if Path(path).name.casefold() in PROHIBITED_CHECKOUT_PDF_NAMES
    )

    candidates = {
        "tracked_or_staged": tracked_or_staged,
        "untracked_and_not_ignored": untracked_and_not_ignored,
        "ignored_outside_reproducible_outputs": ignored_outside_reproducible_outputs,
        "prohibited_manuscript_replicas": prohibited_manuscript_replicas,
    }
    return {category: paths for category, paths in candidates.items() if paths}


def _init_repository(path: Path) -> None:
    subprocess.run(
        ["git", "init", "--quiet", path],
        check=True,
    )


def _write_pdf(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(b"%PDF-1.4\n% synthetic test fixture\n%%EOF\n")


def test_repository_pdf_policy():
    assert pdf_policy_violations(ROOT) == {}


def test_ignored_pdf_in_reproducible_output_is_allowed(tmp_path):
    _init_repository(tmp_path)
    (tmp_path / ".gitignore").write_text(
        "/publication/_book/\n", encoding="utf-8"
    )
    _write_pdf(tmp_path / "publication" / "_book" / "future-output.pdf")

    assert pdf_policy_violations(tmp_path) == {}


def test_tracked_or_staged_pdf_is_rejected(tmp_path):
    _init_repository(tmp_path)
    pdf = tmp_path / "staged.pdf"
    _write_pdf(pdf)
    subprocess.run(["git", "-C", tmp_path, "add", pdf.name], check=True)

    assert pdf_policy_violations(tmp_path)["tracked_or_staged"] == ("staged.pdf",)


def test_untracked_nonignored_pdf_is_rejected(tmp_path):
    _init_repository(tmp_path)
    _write_pdf(tmp_path / "untracked.pdf")

    assert pdf_policy_violations(tmp_path)["untracked_and_not_ignored"] == (
        "untracked.pdf",
    )


def test_ignored_manuscript_replica_in_checkout_is_rejected(tmp_path):
    _init_repository(tmp_path)
    (tmp_path / ".gitignore").write_text(
        "/publication/_book/\n", encoding="utf-8"
    )
    manuscript = tmp_path / "publication" / "_book" / "manuscript.pdf"
    _write_pdf(manuscript)

    violations = pdf_policy_violations(tmp_path)
    assert violations["prohibited_manuscript_replicas"] == (
        "publication/_book/manuscript.pdf",
    )

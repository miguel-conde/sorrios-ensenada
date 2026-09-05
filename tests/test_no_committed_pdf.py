from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_repository_contains_no_pdf_files():
    pdfs = [path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*.pdf") if ".git" not in path.parts]
    assert pdfs == []

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
OPERATIONS = ROOT / "project" / "00_CONTROL" / "OPERACIONES"


def test_all_operation_records_have_a_known_status():
    records = sorted(OPERATIONS.glob("*.md"))
    assert records
    for record in records:
        text = record.read_text(encoding="utf-8")
        match = re.search(r"\*\*Estado:\*\*\s*(clean|prepared|failed|verified)\b", text)
        assert match, f"Estado ausente o inválido en {record.name}"

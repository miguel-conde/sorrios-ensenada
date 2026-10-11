from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "publication/scripts/build_cartography.py"
CARTOGRAPHY = ROOT / "publication/assets/cartography"

spec = importlib.util.spec_from_file_location("build_cartography", SCRIPT)
assert spec and spec.loader
cartography = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cartography)


def _data() -> dict:
    return json.loads((CARTOGRAPHY / "cartography.json").read_text(encoding="utf-8"))


def test_pkg03_snapshot_passes_geographic_and_legal_metadata_validation():
    assert cartography.validate_data(_data()) == []


def test_pkg03_svgs_pass_accessibility_and_structure_validation():
    assert cartography.validate_svgs() == []


def test_pkg03_contains_exactly_the_six_justified_local_places():
    assert set(_data()["places"]) == {
        "sorrios",
        "santibanez_de_ordas",
        "santa_maria_de_ordas",
        "rioseco_de_tapia",
        "villapodambre",
        "tapia_de_la_ribera",
    }


def test_pkg03_uses_current_sorrios_label_without_erasing_source_name():
    data = _data()["places"]["sorrios"]
    assert data["display_name"] == "Sorrios"
    assert data["source_name"] == "Sorrios de Ordás"
    local = (CARTOGRAPHY / "mapa-local.svg").read_text(encoding="utf-8")
    assert "Sorrios" in local
    assert "Sorribos en el expediente de 1752" in local
    assert "Sorribas" not in local


def test_pkg03_uses_only_current_boundaries_and_declares_them_as_current():
    data = _data()
    assert {item["level"] for item in data["boundaries"].values()} == {
        "País",
        "Provincia",
        "Municipio",
    }
    for name in ("mapa-regional.svg", "mapa-local.svg"):
        text = (CARTOGRAPHY / name).read_text(encoding="utf-8")
        assert "actual" in text
        assert "No constituye una reconstrucción" in text


def test_pkg03_svg_assets_are_vector_only_and_contain_no_remote_images():
    for name in ("mapa-regional.svg", "mapa-local.svg"):
        text = (CARTOGRAPHY / name).read_text(encoding="utf-8")
        assert "<image" not in text
        assert "data:image" not in text
        assert "google" not in text.casefold()
        assert "bing" not in text.casefold()


def test_pkg03_attributions_are_visible_in_the_relevant_assets():
    regional = (CARTOGRAPHY / "mapa-regional.svg").read_text(encoding="utf-8")
    local = (CARTOGRAPHY / "mapa-local.svg").read_text(encoding="utf-8")
    assert "Obra derivada de BDLJE CC-BY 4.0 ign.es" in regional
    assert "Obra derivada de NGBE CC-BY 4.0 ign.es" in regional
    assert "IGR_HIDROGRAFIA v1 2023 CC-BY 4.0 scne.es" in local


def test_pkg03_assets_remain_small_enough_for_source_versioning():
    limits = {
        "cartography.json": 500_000,
        "mapa-regional.svg": 100_000,
        "mapa-local.svg": 100_000,
    }
    for name, maximum in limits.items():
        assert (CARTOGRAPHY / name).stat().st_size < maximum


def test_pkg03_does_not_publish_roads_relief_or_historical_polygons():
    data = _data()
    exclusions = " ".join(data["editorial"]["excluded_layers"])
    assert "red viaria" in exclusions
    assert "relieve" in exclusions
    assert "1752" in exclusions
    assert set(data) == {
        "boundaries",
        "coordinate_reference_system",
        "editorial",
        "hydrography",
        "places",
        "schema_version",
        "snapshot_date",
        "sources",
        "title",
    }

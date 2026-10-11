#!/usr/bin/env python3
"""Build the two PKG-03 orientation maps from a compact official-data snapshot.

The default mode is offline and deterministic.  ``--refresh`` downloads only
the required features from IGN/CNIG WFS services, rewrites the compact JSON
snapshot and then rebuilds both SVG files.
"""

from __future__ import annotations

import argparse
import html
import json
import math
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[2]
PUBLICATION = ROOT / "publication"
CARTOGRAPHY = PUBLICATION / "assets" / "cartography"
DATA_PATH = CARTOGRAPHY / "cartography.json"
REGIONAL_PATH = CARTOGRAPHY / "mapa-regional.svg"
LOCAL_PATH = CARTOGRAPHY / "mapa-local.svg"
CONSULTED = "2026-10-11"
DISCLAIMER = (
    "Mapa contemporáneo de orientación. No constituye una reconstrucción de "
    "los límites ni de la organización territorial de 1752."
)

ADMIN_WFS = "https://www.ign.es/wfs-inspire/unidades-administrativas"
NGBE_WFS = "https://www.ign.es/wfs-inspire/ngbe"
HYDRO_WFS = "https://servicios.idee.es/wfs-inspire/hidrografia"
LICENSE_URL = "https://www.ign.es/resources/licencia/Condiciones_licenciaUso_IGN.pdf"

ADMIN_FEATURES = {
    "spain": ("34000000000", "España", "País", 0.010),
    "leon": ("34072400000", "León", "Provincia", 0.002),
    "santa_maria_de_ordas": (
        "34072424158",
        "Santa María de Ordás",
        "Municipio",
        0.00015,
    ),
    "rioseco_de_tapia": ("34072424133", "Rioseco de Tapia", "Municipio", 0.00015),
}

PLACE_SPECS = {
    "sorrios": {
        "source_name": "Sorrios de Ordás",
        "display_name": "Sorrios",
        "preferred_type": "Entidad menor de población",
        "municipality": "Santa María de Ordás",
    },
    "santibanez_de_ordas": {
        "source_name": "Santibáñez de Ordás",
        "display_name": "Santibáñez de Ordás",
        "preferred_type": "Capital de EATIM",
        "municipality": "Santa María de Ordás",
    },
    "santa_maria_de_ordas": {
        "source_name": "Santa María de Ordás",
        "display_name": "Santa María de Ordás",
        "preferred_type": "Capital de municipio",
        "municipality": "Santa María de Ordás",
    },
    "rioseco_de_tapia": {
        "source_name": "Rioseco de Tapia",
        "display_name": "Rioseco de Tapia",
        "preferred_type": "Capital de municipio",
        "municipality": "Rioseco de Tapia",
    },
    "villapodambre": {
        "source_name": "Villapodambre",
        "display_name": "Villapodambre",
        "preferred_type": "Capital de EATIM",
        "municipality": "Santa María de Ordás",
    },
    "tapia_de_la_ribera": {
        "source_name": "Tapia de la Ribera",
        "display_name": "Tapia de la Ribera",
        "preferred_type": "Capital de EATIM",
        "municipality": "Rioseco de Tapia",
    },
}

NGBE_BBOX = (-5.90, 42.68, -5.74, 42.78)
HYDRO_BBOX = NGBE_BBOX


class CartographyError(RuntimeError):
    """An actionable PKG-03 cartography failure."""


def _url(base: str, **parameters: str) -> str:
    return base + "?" + urllib.parse.urlencode(parameters)


def _download(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "sorrios-ensenada-pkg03/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            payload = response.read()
    except OSError as exc:
        raise CartographyError(f"No se pudo descargar {url}: {exc}") from exc
    if not payload:
        raise CartographyError(f"La fuente devolvió una respuesta vacía: {url}")
    return payload


def _rdp(points: list[list[float]], tolerance: float) -> list[list[float]]:
    if len(points) <= 2:
        return points
    keep = {0, len(points) - 1}
    stack = [(0, len(points) - 1)]
    while stack:
        start, end = stack.pop()
        ax, ay = points[start]
        bx, by = points[end]
        dx, dy = bx - ax, by - ay
        denominator = dx * dx + dy * dy
        farthest = -1.0
        index = -1
        for position in range(start + 1, end):
            px, py = points[position]
            if denominator == 0:
                distance = math.hypot(px - ax, py - ay)
            else:
                t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / denominator))
                distance = math.hypot(px - (ax + t * dx), py - (ay + t * dy))
            if distance > farthest:
                farthest, index = distance, position
        if farthest > tolerance and index > start:
            keep.add(index)
            stack.extend(((start, index), (index, end)))
    return [points[index] for index in sorted(keep)]


def _simplify_line(points: list[list[float]], tolerance: float) -> list[list[float]]:
    rounded = [[round(float(x), 6), round(float(y), 6)] for x, y in points]
    return _rdp(rounded, tolerance)


def _simplify_ring(points: list[list[float]], tolerance: float) -> list[list[float]]:
    open_ring = points[:-1] if points and points[0] == points[-1] else points
    if len(open_ring) < 4:
        return _simplify_line(points, tolerance)
    # A closed ring normally begins and ends at neighbouring vertices.  Running
    # RDP on that ordering makes the baseline almost zero and preserves far too
    # many points.  Split the ring at two distant vertices and simplify both
    # arcs independently before joining them again.
    start = min(range(len(open_ring)), key=lambda index: (open_ring[index][0], open_ring[index][1]))
    rotated = open_ring[start:] + open_ring[:start]
    ax, ay = rotated[0]
    opposite = max(
        range(1, len(rotated)),
        key=lambda index: (rotated[index][0] - ax) ** 2 + (rotated[index][1] - ay) ** 2,
    )
    first_arc = _simplify_line(rotated[: opposite + 1], tolerance)
    second_arc = _simplify_line(rotated[opposite:] + [rotated[0]], tolerance)
    simplified = first_arc[:-1] + second_arc[:-1]
    if len(simplified) < 3:
        simplified = _simplify_line(open_ring, 0)
    return simplified + [simplified[0]]


def _simplify_geometry(geometry: dict[str, Any], tolerance: float) -> dict[str, Any]:
    kind = geometry.get("type")
    coordinates = geometry.get("coordinates")
    if kind == "Polygon":
        result = [_simplify_ring(ring, tolerance) for ring in coordinates]
    elif kind == "MultiPolygon":
        result = [
            [_simplify_ring(ring, tolerance) for ring in polygon]
            for polygon in coordinates
        ]
    elif kind == "LineString":
        result = _simplify_line(coordinates, tolerance)
    else:
        raise CartographyError(f"Geometría no admitida: {kind}")
    return {"type": kind, "coordinates": result}


def _ring_area(ring: list[list[float]]) -> float:
    return abs(
        sum(
            ring[index][0] * ring[(index + 1) % len(ring)][1]
            - ring[(index + 1) % len(ring)][0] * ring[index][1]
            for index in range(len(ring))
        )
        / 2
    )


def _filter_small_polygons(geometry: dict[str, Any], minimum_area: float) -> dict[str, Any]:
    if geometry["type"] != "MultiPolygon":
        return geometry
    polygons = [
        polygon
        for polygon in geometry["coordinates"]
        if polygon and _ring_area(polygon[0]) >= minimum_area
    ]
    if not polygons:
        raise CartographyError("El filtrado por escala eliminó todos los polígonos.")
    return {"type": "MultiPolygon", "coordinates": polygons}


def _admin_url(code: str) -> str:
    return _url(
        ADMIN_WFS,
        service="WFS",
        version="2.0.0",
        request="GetFeature",
        typeNames="au:AdministrativeUnit",
        resourceId=f"AU_ADMINISTRATIVEUNIT_{code}",
        outputFormat="application/geo+json",
        srsName="EPSG:4326",
    )


def _fetch_boundaries() -> dict[str, Any]:
    boundaries: dict[str, Any] = {}
    for key, (code, expected_name, expected_level, tolerance) in ADMIN_FEATURES.items():
        url = _admin_url(code)
        parsed = json.loads(_download(url))
        features = parsed.get("features", [])
        if len(features) != 1:
            raise CartographyError(f"Se esperaba una unidad administrativa para {code}.")
        feature = features[0]
        properties = feature["properties"]
        name = properties["name"]["GeographicalName"]["spelling"]["SpellingOfName"]["text"]
        level = properties["nationalLevelName"]["LocalisedCharacterString"]
        if (name, level) != (expected_name, expected_level):
            raise CartographyError(
                f"Unidad {code} inesperada: {name!r}, {level!r}; "
                f"se esperaba {expected_name!r}, {expected_level!r}."
            )
        geometry = _simplify_geometry(feature["geometry"], tolerance)
        minimum_polygon_area = 0.001 if key == "spain" else 0
        if minimum_polygon_area:
            geometry = _filter_small_polygons(geometry, minimum_polygon_area)
        boundaries[key] = {
            "name": name,
            "level": level,
            "national_code": code,
            "feature_id": feature["id"],
            "source_url": url,
            "simplification_tolerance_degrees": tolerance,
            "minimum_polygon_area_degrees_squared": minimum_polygon_area,
            "geometry": geometry,
        }
    return boundaries


def _name_record(feature: dict[str, Any]) -> Iterable[tuple[str, str, str, str]]:
    raw_names = feature["properties"].get("name", [])
    names = raw_names if isinstance(raw_names, list) else [raw_names]
    local = feature["properties"].get("localType", {}).get("LocalisedCharacterString", {})
    local_type = local.get("value", "") if isinstance(local, dict) else str(local)
    for raw in names:
        name = raw.get("GeographicalName", {})
        source = name.get("sourceOfName", "")
        spelling = name.get("spelling", {}).get("SpellingOfName", {}).get("text", "")
        status = name.get("nameStatus", {}).get("href", "").rsplit("/", 1)[-1]
        yield spelling, local_type, source, status


def _fetch_places() -> tuple[dict[str, Any], str]:
    bbox = ",".join(str(value) for value in NGBE_BBOX) + ",EPSG:4326"
    url = _url(
        NGBE_WFS,
        service="WFS",
        version="2.0.0",
        request="GetFeature",
        typeNames="gn:NamedPlace",
        outputFormat="application/geo+json",
        srsName="EPSG:4326",
        bbox=bbox,
    )
    parsed = json.loads(_download(url))
    found: dict[str, Any] = {}
    for feature in parsed.get("features", []):
        for spelling, local_type, source, status in _name_record(feature):
            for key, spec in PLACE_SPECS.items():
                if spelling == spec["source_name"] and local_type == spec["preferred_type"]:
                    found[key] = {
                        **spec,
                        "longitude": round(float(feature["geometry"]["coordinates"][0]), 9),
                        "latitude": round(float(feature["geometry"]["coordinates"][1]), 9),
                        "source_dataset": source,
                        "name_status": status,
                        "feature_id": feature["id"],
                    }
    missing = sorted(set(PLACE_SPECS) - set(found))
    if missing:
        raise CartographyError("No se localizaron los puntos requeridos: " + ", ".join(missing))
    return found, url


def _fetch_hydrography() -> tuple[list[dict[str, Any]], str]:
    bbox = ",".join(str(value) for value in HYDRO_BBOX) + ",EPSG:4326"
    url = _url(
        HYDRO_WFS,
        service="WFS",
        version="2.0.0",
        request="GetFeature",
        typeNames="hy-p:Watercourse",
        srsName="EPSG:4326",
        bbox=bbox,
    )
    root = ET.fromstring(_download(url))
    namespaces = {
        "gml": "http://www.opengis.net/gml/3.2",
        "gn": "http://inspire.ec.europa.eu/schemas/gn/4.0",
        "hy": "http://inspire.ec.europa.eu/schemas/hy-p/4.0",
    }
    features: list[dict[str, Any]] = []
    for watercourse in root.findall(".//hy:Watercourse", namespaces):
        if watercourse.findtext(".//gn:text", default="", namespaces=namespaces) != "Río Luna":
            continue
        pos_list = watercourse.find(".//gml:posList", namespaces)
        if pos_list is None or not pos_list.text:
            continue
        values = [float(value) for value in pos_list.text.split()]
        points = [[values[index], values[index + 1]] for index in range(0, len(values), 2)]
        features.append(
            {
                "feature_id": watercourse.attrib.get(
                    "{http://www.opengis.net/gml/3.2}id", ""
                ),
                "geometry": {
                    "type": "LineString",
                    "coordinates": _simplify_line(points, 0.00004),
                },
            }
        )
    if not features:
        raise CartographyError("El recorte oficial no devolvió segmentos del Río Luna.")
    features.sort(key=lambda feature: feature["feature_id"])
    return features, url


def refresh_snapshot() -> dict[str, Any]:
    boundaries = _fetch_boundaries()
    places, places_url = _fetch_places()
    watercourses, hydro_url = _fetch_hydrography()
    data = {
        "schema_version": 1,
        "title": "Datos mínimos de cartografía de orientación PKG-03",
        "snapshot_date": CONSULTED,
        "coordinate_reference_system": "EPSG:4326",
        "sources": {
            "bdlje": {
                "provider": "Instituto Geográfico Nacional / CNIG",
                "dataset": "Límites y Unidades Administrativas Actuales (BDLJE)",
                "catalog_url": "https://centrodedescargas.cnig.es/CentroDescargas/detalleArchivo?sec=9000029",
                "service_url": ADMIN_WFS,
                "license": "CC BY 4.0 compatible conforme a la licencia de uso del IGN",
                "license_url": LICENSE_URL,
                "attribution": "Obra derivada de BDLJE CC-BY 4.0 ign.es",
                "dataset_date": "2026-07-28",
                "consulted": CONSULTED,
            },
            "ngbe": {
                "provider": "Instituto Geográfico Nacional / CNIG",
                "dataset": "Nomenclátor Geográfico Básico de España (NGBE)",
                "catalog_url": "https://centrodedescargas.cnig.es/CentroDescargas/detalleArchivo?sec=9000001",
                "service_url": NGBE_WFS,
                "query_url": places_url,
                "license": "CC BY 4.0 compatible conforme a la licencia de uso del IGN",
                "license_url": LICENSE_URL,
                "attribution": "Obra derivada de NGBE CC-BY 4.0 ign.es",
                "dataset_date": "2026",
                "consulted": CONSULTED,
            },
            "igr_hidrografia": {
                "provider": "Sistema Cartográfico Nacional / IGN",
                "dataset": "IGR_HIDROGRAFIA v1 2023",
                "catalog_url": "https://centrodedescargas.cnig.es/CentroDescargas/detalleArchivo?sec=12633136",
                "service_url": HYDRO_WFS,
                "query_url": hydro_url,
                "license": "CC BY 4.0",
                "license_url": LICENSE_URL,
                "attribution": "Obra derivada de IGR_HIDROGRAFIA v1 2023 CC-BY 4.0 scne.es",
                "dataset_date": "2023",
                "consulted": CONSULTED,
            },
            "municipal_name_check": {
                "provider": "Ayuntamiento de Santa María de Ordás",
                "purpose": "Contraste de la denominación contemporánea Sorrios",
                "url": "https://www.aytosantamariadeordas.es/los-pueblos/santibanez-de-ordas/",
                "consulted": CONSULTED,
                "incorporated_geometry": False,
            },
        },
        "boundaries": boundaries,
        "places": places,
        "hydrography": {
            "name": "Río Luna",
            "features": watercourses,
            "simplification_tolerance_degrees": 0.00004,
        },
        "editorial": {
            "historical_name": "Sorribos",
            "current_map_label": "Sorrios",
            "mandatory_disclaimer": DISCLAIMER,
            "excluded_layers": [
                "límites o términos de 1752",
                "jurisdicciones y propiedades históricas",
                "red viaria, por no añadir orientación suficiente a esta escala",
                "relieve, por no ser necesario para identificar los lugares y reducir la legibilidad",
            ],
        },
    }
    CARTOGRAPHY.mkdir(parents=True, exist_ok=True)
    DATA_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return data


def load_snapshot() -> dict[str, Any]:
    try:
        data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise CartographyError(f"No se pudo leer {DATA_PATH}: {exc}") from exc
    if data.get("schema_version") != 1:
        raise CartographyError("La versión del snapshot cartográfico no es compatible.")
    return data


def _rings(geometry: dict[str, Any]) -> Iterable[list[list[float]]]:
    if geometry["type"] == "Polygon":
        yield from geometry["coordinates"]
    elif geometry["type"] == "MultiPolygon":
        for polygon in geometry["coordinates"]:
            yield from polygon


def _point_in_ring(point: tuple[float, float], ring: list[list[float]]) -> bool:
    x, y = point
    inside = False
    previous = ring[-1]
    for current in ring:
        x1, y1 = previous
        x2, y2 = current
        intersects = (y1 > y) != (y2 > y)
        if intersects and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            inside = not inside
        previous = current
    return inside


def _point_in_geometry(point: tuple[float, float], geometry: dict[str, Any]) -> bool:
    if geometry["type"] == "Polygon":
        polygons = [geometry["coordinates"]]
    else:
        polygons = geometry["coordinates"]
    for polygon in polygons:
        if polygon and _point_in_ring(point, polygon[0]):
            if not any(_point_in_ring(point, hole) for hole in polygon[1:]):
                return True
    return False


def _haversine(a: tuple[float, float], b: tuple[float, float]) -> float:
    lon1, lat1 = map(math.radians, a)
    lon2, lat2 = map(math.radians, b)
    delta_lon, delta_lat = lon2 - lon1, lat2 - lat1
    value = math.sin(delta_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2) ** 2
    return 6371.0088 * 2 * math.asin(math.sqrt(value))


def validate_data(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required_boundaries = set(ADMIN_FEATURES)
    required_places = set(PLACE_SPECS)
    if set(data.get("boundaries", {})) != required_boundaries:
        errors.append("El snapshot no contiene exactamente las cuatro unidades administrativas requeridas.")
    if set(data.get("places", {})) != required_places:
        errors.append("El snapshot no contiene exactamente los seis lugares requeridos.")
    places = data.get("places", {})
    boundaries = data.get("boundaries", {})
    for key, spec in PLACE_SPECS.items():
        place = places.get(key, {})
        if place.get("source_name") != spec["source_name"]:
            errors.append(f"Topónimo fuente inesperado para {key}.")
        lon, lat = place.get("longitude"), place.get("latitude")
        if not isinstance(lon, (int, float)) or not isinstance(lat, (int, float)):
            errors.append(f"Coordenadas inválidas para {key}.")
            continue
        if not (-5.90 <= lon <= -5.74 and 42.68 <= lat <= 42.78):
            errors.append(f"{key} queda fuera del recorte local previsto.")
        municipality_key = (
            "santa_maria_de_ordas"
            if spec["municipality"] == "Santa María de Ordás"
            else "rioseco_de_tapia"
        )
        geometry = boundaries.get(municipality_key, {}).get("geometry")
        if geometry and not _point_in_geometry((lon, lat), geometry):
            errors.append(f"{key} no cae dentro de su municipio actual declarado.")
        province = boundaries.get("leon", {}).get("geometry")
        if province and not _point_in_geometry((lon, lat), province):
            errors.append(f"{key} no cae dentro de la provincia actual de León.")
    if required_places <= set(places):
        sorrios = (places["sorrios"]["longitude"], places["sorrios"]["latitude"])
        santibanez = (
            places["santibanez_de_ordas"]["longitude"],
            places["santibanez_de_ordas"]["latitude"],
        )
        if _haversine(sorrios, santibanez) > 2:
            errors.append("Sorrios y Santibáñez aparecen separados por más de 2 km.")
        relative = {
            "villapodambre": (-1, 1),
            "tapia_de_la_ribera": (1, 1),
            "rioseco_de_tapia": (1, -1),
            "santibanez_de_ordas": (-1, -1),
            "santa_maria_de_ordas": (-1, -1),
        }
        for key, (east_west, north_south) in relative.items():
            point = places[key]
            if east_west * (point["longitude"] - sorrios[0]) <= 0:
                errors.append(f"Orientación este/oeste inesperada para {key} respecto a Sorrios.")
            if north_south * (point["latitude"] - sorrios[1]) <= 0:
                errors.append(f"Orientación norte/sur inesperada para {key} respecto a Sorrios.")
    sources = data.get("sources", {})
    for key in ("bdlje", "ngbe", "igr_hidrografia"):
        source = sources.get(key, {})
        for field in ("provider", "dataset", "license", "license_url", "attribution", "consulted"):
            if not source.get(field):
                errors.append(f"Falta {field} en la fuente {key}.")
    if not data.get("hydrography", {}).get("features"):
        errors.append("No hay geometría del Río Luna.")
    return errors


def _project(
    longitude: float,
    latitude: float,
    bbox: tuple[float, float, float, float],
    frame: tuple[float, float, float, float],
) -> tuple[float, float]:
    xmin, ymin, xmax, ymax = bbox
    x, y, width, height = frame
    return (
        x + (longitude - xmin) / (xmax - xmin) * width,
        y + (ymax - latitude) / (ymax - ymin) * height,
    )


def _geometry_path(
    geometry: dict[str, Any],
    bbox: tuple[float, float, float, float],
    frame: tuple[float, float, float, float],
) -> str:
    commands: list[str] = []
    for ring in _rings(geometry):
        for index, (longitude, latitude) in enumerate(ring):
            x, y = _project(longitude, latitude, bbox, frame)
            commands.append(("M" if index == 0 else "L") + f"{x:.1f},{y:.1f}")
        commands.append("Z")
    return " ".join(commands)


def _line_path(
    geometry: dict[str, Any],
    bbox: tuple[float, float, float, float],
    frame: tuple[float, float, float, float],
) -> str:
    commands: list[str] = []
    for index, (longitude, latitude) in enumerate(geometry["coordinates"]):
        x, y = _project(longitude, latitude, bbox, frame)
        commands.append(("M" if index == 0 else "L") + f"{x:.1f},{y:.1f}")
    return " ".join(commands)


def _scale_bar(
    bbox: tuple[float, float, float, float],
    frame: tuple[float, float, float, float],
    kilometres: float,
    x: float,
    y: float,
) -> str:
    mean_latitude = (bbox[1] + bbox[3]) / 2
    km_per_degree = 111.320 * math.cos(math.radians(mean_latitude))
    pixels = kilometres / ((bbox[2] - bbox[0]) * km_per_degree) * frame[2]
    return (
        f'<g class="scale"><path d="M{x:.1f},{y:.1f} h{pixels:.1f}"/>'
        f'<path d="M{x:.1f},{y - 5:.1f} v10 M{x + pixels:.1f},{y - 5:.1f} v10"/>'
        f'<text x="{x + pixels / 2:.1f}" y="{y - 10:.1f}" text-anchor="middle">{kilometres:g} km</text></g>'
    )


def _north(x: float, y: float) -> str:
    return (
        f'<g class="north" transform="translate({x:.1f} {y:.1f})">'
        '<text x="0" y="-28" text-anchor="middle">N</text>'
        '<path d="M0,-21 L-8,2 L0,-3 L8,2 Z"/></g>'
    )


def _svg_start(width: int, height: int, title_id: str, desc_id: str, title: str, description: str) -> list[str]:
    return [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="{title_id} {desc_id}">',
        f'<title id="{title_id}">{html.escape(title)}</title>',
        f'<desc id="{desc_id}">{html.escape(description)}</desc>',
        "<style>",
        "text{font-family:'Noto Sans','DejaVu Sans',sans-serif;fill:#20252a}",
        ".title{font-size:30px;font-weight:700}.subtitle{font-size:19px;fill:#4b5157}",
        ".panel-title{font-size:21px;font-weight:700}.label{font-size:18px;font-weight:650;paint-order:stroke;stroke:#fff;stroke-width:5px;stroke-linejoin:round}",
        ".small{font-size:16px}.tiny{font-size:14px}.footer{font-size:15px;fill:#343a40}.disclaimer{font-size:17px;font-weight:700}",
        ".frame{fill:#fbfaf7;stroke:#4d5358;stroke-width:1.5}.country{fill:#e5e1d8;stroke:#30363b;stroke-width:1.8;fill-rule:evenodd}",
        ".province{fill:url(#provinceHatch);stroke:#6b3f20;stroke-width:2.4;fill-rule:evenodd}.municipality{fill:url(#municipalHatch);stroke:#174d5f;stroke-width:2.2;fill-rule:evenodd}",
        ".municipality-other{fill:url(#municipalHatch2);stroke:#63676b;stroke-width:2;stroke-dasharray:8 6;fill-rule:evenodd}",
        ".hydro{fill:none;stroke:#256783;stroke-width:3.2;stroke-linecap:round}.place{fill:#fff;stroke:#24282c;stroke-width:2.5}.focus{fill:#6b3f20;stroke:#fff;stroke-width:2}.focus-ring{fill:none;stroke:#6b3f20;stroke-width:3}",
        ".scale path{stroke:#20252a;stroke-width:2;fill:none}.scale text,.north text{font-size:16px;font-weight:700}.north path{fill:#20252a}",
        ".legend{fill:#fff;fill-opacity:.94;stroke:#74787c;stroke-width:1}.leader{stroke:#555b60;stroke-width:1.4}.river-label{font-size:17px;font-style:italic;fill:#174d5f;paint-order:stroke;stroke:#fff;stroke-width:4px}",
        "</style>",
        "<defs>",
        '<pattern id="provinceHatch" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="9" height="9" fill="#d5b894"/><path d="M0 0 V9" stroke="#8c623f" stroke-width="2"/></pattern>',
        '<pattern id="municipalHatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="10" height="10" fill="#cbdfe3"/><path d="M0 0 V10" stroke="#598392" stroke-width="2"/></pattern>',
        '<pattern id="municipalHatch2" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)"><rect width="10" height="10" fill="#e4e4e1"/><path d="M0 0 V10" stroke="#939595" stroke-width="2"/></pattern>',
        "</defs>",
    ]


def _write_svg(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def build_regional(data: dict[str, Any]) -> None:
    width, height = 1200, 800
    title = "Situación regional de Sorrios y Santibáñez de Ordás"
    description = (
        "Mapa contemporáneo de orientación con dos escalas: España con la provincia "
        "de León destacada, y la provincia de León con el municipio actual de Santa "
        "María de Ordás y el ámbito de Sorrios y Santibáñez señalado. No representa "
        "límites históricos de 1752."
    )
    lines = _svg_start(width, height, "regional-title", "regional-desc", title, description)
    left_frame = (55.0, 125.0, 500.0, 430.0)
    right_frame = (645.0, 125.0, 500.0, 430.0)
    spain_bbox = (-18.5, 27.4, 4.5, 44.5)
    leon_bbox = (-7.20, 41.78, -4.65, 43.30)
    boundaries = data["boundaries"]
    places = data["places"]
    lines.extend(
        [
            '<text class="title" x="55" y="48">Situación regional</text>',
            '<text class="subtitle" x="55" y="79">España · provincia de León · área de Ordás · ámbito local del volumen</text>',
            f'<rect class="frame" x="{left_frame[0]}" y="{left_frame[1]}" width="{left_frame[2]}" height="{left_frame[3]}" rx="3"/>',
            f'<rect class="frame" x="{right_frame[0]}" y="{right_frame[1]}" width="{right_frame[2]}" height="{right_frame[3]}" rx="3"/>',
            '<text class="panel-title" x="72" y="115">España y León</text>',
            '<text class="panel-title" x="662" y="115">Provincia de León y área de Ordás</text>',
            f'<path class="country" d="{_geometry_path(boundaries["spain"]["geometry"], spain_bbox, left_frame)}"/>',
            f'<path class="province" d="{_geometry_path(boundaries["leon"]["geometry"], spain_bbox, left_frame)}"/>',
            f'<path class="country" d="{_geometry_path(boundaries["leon"]["geometry"], leon_bbox, right_frame)}"/>',
            f'<path class="municipality" d="{_geometry_path(boundaries["santa_maria_de_ordas"]["geometry"], leon_bbox, right_frame)}"/>',
        ]
    )
    sorrios = places["sorrios"]
    sx, sy = _project(sorrios["longitude"], sorrios["latitude"], leon_bbox, right_frame)
    lines.extend(
        [
            f'<circle class="focus-ring" cx="{sx:.1f}" cy="{sy:.1f}" r="10"/>',
            f'<circle class="focus" cx="{sx:.1f}" cy="{sy:.1f}" r="5"/>',
            f'<path class="leader" d="M{sx:.1f},{sy - 11:.1f} L{sx:.1f},{sy - 37:.1f}"/>',
            f'<text class="label" x="{sx:.1f}" y="{sy - 47:.1f}" text-anchor="middle">Área de Ordás</text>',
            f'<text class="small" x="{sx:.1f}" y="{sy - 25:.1f}" text-anchor="middle">Sorrios y Santibáñez</text>',
            _scale_bar(spain_bbox, left_frame, 200, 80, 520),
            _scale_bar(leon_bbox, right_frame, 25, 675, 520),
            _north(515, 170),
            _north(1100, 170),
            '<g transform="translate(70 585)"><rect class="legend" width="1060" height="58" rx="4"/>',
            '<rect x="22" y="18" width="28" height="20" fill="url(#provinceHatch)" stroke="#6b3f20" stroke-width="2"/><text class="small" x="62" y="34">Provincia actual de León</text>',
            '<rect x="330" y="18" width="28" height="20" fill="url(#municipalHatch)" stroke="#174d5f" stroke-width="2"/><text class="small" x="370" y="34">Municipio actual de Santa María de Ordás</text>',
            '<circle class="focus-ring" cx="805" cy="28" r="9"/><circle class="focus" cx="805" cy="28" r="4"/><text class="small" x="825" y="34">Ámbito local del volumen</text></g>',
            '<text class="disclaimer" x="55" y="681">Mapa contemporáneo de orientación.</text>',
            '<text class="disclaimer" x="55" y="706">No constituye una reconstrucción de los límites ni de la organización territorial de 1752.</text>',
            '<text class="footer" x="55" y="738">Límites administrativos actuales. Obra derivada de BDLJE CC-BY 4.0 ign.es · Obra derivada de NGBE CC-BY 4.0 ign.es.</text>',
            '<text class="footer" x="55" y="765">Datos consultados el 11-10-2026. Elaboración editorial reproducible; coordenadas ETRS89/WGS84 (EPSG:4326).</text>',
            "</svg>",
        ]
    )
    _write_svg(REGIONAL_PATH, lines)


LOCAL_LABELS = {
    "sorrios": (18, -24, "start"),
    "santibanez_de_ordas": (18, 34, "start"),
    "santa_maria_de_ordas": (-18, 32, "end"),
    "rioseco_de_tapia": (18, 10, "start"),
    "villapodambre": (-18, -18, "end"),
    "tapia_de_la_ribera": (18, -16, "start"),
}


def build_local(data: dict[str, Any]) -> None:
    width, height = 1200, 940
    title = "Entorno local de Sorrios y Santibáñez de Ordás"
    description = (
        "Mapa contemporáneo del entorno de Ordás con Sorrios, identificado como "
        "Sorribos en el expediente de 1752, Santibáñez de Ordás, Santa María de "
        "Ordás, Villapodambre, Rioseco de Tapia y Tapia de la Ribera. Incluye el "
        "río Luna y límites municipales actuales; no representa límites históricos."
    )
    lines = _svg_start(width, height, "local-title", "local-desc", title, description)
    frame = (55.0, 115.0, 1090.0, 610.0)
    bbox = (-5.89, 42.705, -5.755, 42.775)
    boundaries = data["boundaries"]
    lines.extend(
        [
            '<text class="title" x="55" y="48">Entorno local</text>',
            '<text class="subtitle" x="55" y="79">Sorrios, Santibáñez de Ordás y lugares relacionados por el expediente</text>',
            f'<rect class="frame" x="{frame[0]}" y="{frame[1]}" width="{frame[2]}" height="{frame[3]}" rx="3"/>',
            '<clipPath id="localClip"><rect x="55" y="115" width="1090" height="610"/></clipPath>',
            '<g clip-path="url(#localClip)">',
            f'<path class="municipality" d="{_geometry_path(boundaries["santa_maria_de_ordas"]["geometry"], bbox, frame)}"/>',
            f'<path class="municipality-other" d="{_geometry_path(boundaries["rioseco_de_tapia"]["geometry"], bbox, frame)}"/>',
        ]
    )
    for feature in data["hydrography"]["features"]:
        lines.append(f'<path class="hydro" d="{_line_path(feature["geometry"], bbox, frame)}"/>')
    lines.append("</g>")
    places = data["places"]
    for key in (
        "villapodambre",
        "tapia_de_la_ribera",
        "santa_maria_de_ordas",
        "santibanez_de_ordas",
        "rioseco_de_tapia",
        "sorrios",
    ):
        place = places[key]
        x, y = _project(place["longitude"], place["latitude"], bbox, frame)
        dx, dy, anchor = LOCAL_LABELS[key]
        if key == "sorrios":
            lines.extend(
                [
                    f'<circle class="focus-ring" cx="{x:.1f}" cy="{y:.1f}" r="12"/>',
                    f'<circle class="focus" cx="{x:.1f}" cy="{y:.1f}" r="6"/>',
                    f'<path class="leader" d="M{x + 9:.1f},{y - 8:.1f} L{x + dx - 4:.1f},{y + dy + 4:.1f}"/>',
                    f'<text class="label" x="{x + dx:.1f}" y="{y + dy:.1f}" text-anchor="{anchor}">Sorrios</text>',
                    f'<text class="small" x="{x + dx:.1f}" y="{y + dy + 23:.1f}" text-anchor="{anchor}">(Sorribos en el expediente de 1752)</text>',
                ]
            )
        else:
            lines.extend(
                [
                    f'<circle class="place" cx="{x:.1f}" cy="{y:.1f}" r="6"/>',
                    f'<path class="leader" d="M{x:.1f},{y:.1f} L{x + dx * .72:.1f},{y + dy * .72:.1f}"/>',
                    f'<text class="label" x="{x + dx:.1f}" y="{y + dy:.1f}" text-anchor="{anchor}">{html.escape(place["display_name"])}</text>',
                ]
            )
    river_x, river_y = _project(-5.792, 42.758, bbox, frame)
    lines.extend(
        [
            f'<text class="river-label" x="{river_x:.1f}" y="{river_y:.1f}" transform="rotate(-18 {river_x:.1f} {river_y:.1f})">Río Luna</text>',
            _north(1090, 175),
            _scale_bar(bbox, frame, 2, 85, 690),
            '<g transform="translate(65 748)"><rect class="legend" width="1070" height="58" rx="4"/>',
            '<circle class="focus-ring" cx="28" cy="29" r="10"/><circle class="focus" cx="28" cy="29" r="5"/><text class="small" x="49" y="35">Núcleo principal del volumen</text>',
            '<circle class="place" cx="333" cy="29" r="6"/><text class="small" x="350" y="35">Otros lugares relevantes</text>',
            '<path class="hydro" d="M565,29 h42"/><text class="small" x="620" y="35">Curso actual del río Luna</text>',
            '<rect x="850" y="19" width="28" height="20" fill="url(#municipalHatch)" stroke="#174d5f" stroke-width="2"/><text class="small" x="890" y="35">Límites municipales actuales</text></g>',
            '<text class="disclaimer" x="55" y="842">Mapa contemporáneo de orientación.</text>',
            '<text class="disclaimer" x="55" y="867">No constituye una reconstrucción de los límites ni de la organización territorial de 1752.</text>',
            '<text class="footer" x="55" y="899">Obra derivada de BDLJE CC-BY 4.0 ign.es · Obra derivada de NGBE CC-BY 4.0 ign.es.</text>',
            '<text class="footer" x="55" y="924">Obra derivada de IGR_HIDROGRAFIA v1 2023 CC-BY 4.0 scne.es · Consulta: 11-10-2026.</text>',
            "</svg>",
        ]
    )
    _write_svg(LOCAL_PATH, lines)


def validate_svgs() -> list[str]:
    errors: list[str] = []
    expected = {
        REGIONAL_PATH: (1200, 800, "regional-title", "regional-desc"),
        LOCAL_PATH: (1200, 940, "local-title", "local-desc"),
    }
    for path, (width, height, title_id, desc_id) in expected.items():
        try:
            root = ET.parse(path).getroot()
        except (OSError, ET.ParseError) as exc:
            errors.append(f"SVG inválido {path.name}: {exc}")
            continue
        if root.attrib.get("width") != str(width) or root.attrib.get("height") != str(height):
            errors.append(f"Dimensiones inesperadas en {path.name}.")
        if root.attrib.get("aria-labelledby") != f"{title_id} {desc_id}":
            errors.append(f"Falta etiquetado accesible en {path.name}.")
        text = path.read_text(encoding="utf-8")
        for required in (
            "Mapa contemporáneo de orientación.",
            "No constituye una reconstrucción de los límites ni de la organización territorial de 1752.",
            "CC-BY 4.0",
            "N</text>",
        ):
            if required not in text:
                errors.append(f"Falta {required!r} en {path.name}.")
        if "http://www.google" in text or "openstreetmap" in text.casefold():
            errors.append(f"Fuente no autorizada detectada en {path.name}.")
    return errors


def build(data: dict[str, Any]) -> None:
    errors = validate_data(data)
    if errors:
        raise CartographyError("Validación geográfica fallida:\n- " + "\n- ".join(errors))
    build_regional(data)
    build_local(data)
    svg_errors = validate_svgs()
    if svg_errors:
        raise CartographyError("Validación SVG fallida:\n- " + "\n- ".join(svg_errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true", help="Actualizar desde los WFS oficiales antes de construir.")
    parser.add_argument("--check", action="store_true", help="Validar snapshot y SVG existentes sin reescribirlos.")
    arguments = parser.parse_args()
    try:
        if arguments.check:
            errors = validate_data(load_snapshot()) + validate_svgs()
            if errors:
                raise CartographyError("\n- ".join(errors))
            print("PKG-03: datos geográficos y SVG en PASS.")
            return 0
        data = refresh_snapshot() if arguments.refresh else load_snapshot()
        build(data)
    except CartographyError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Generados: {REGIONAL_PATH.relative_to(ROOT)}, {LOCAL_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate the developing publication and the bounded Phase 2B regression."""

from __future__ import annotations

import argparse
import html as html_module
import re
import shutil
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from PIL import Image

from critical_edition import (
    CriticalEditionError,
    SECTION_NAMES,
    load_unit_specs,
    parse_critical_edition,
    published_unit_anchor,
)
from build_apparatus import (
    OUTPUT_NAMES as APPARATUS_OUTPUT_NAMES,
    ApparatusBuildError,
    load_apparatus_data,
    validate_apparatus_fidelity,
)
from apparatus_sources import ApparatusSourceError

from build_vertical_prototype import (
    EVIDENCE_GROUPS,
    MANUSCRIPT_FILE_ID,
    PALEOGRAPHIC_LINE_COUNT,
    PALEOGRAPHIC_SECTION,
    PrototypeBuildError,
    read_paleographic_lines,
)
from build_modernized import (
    ModernizedBuildError,
    validate_generated_fidelity,
)
from modernized_edition import (
    ModernizedEditionError,
    load_modernized_edition,
    validate_concordance_units,
    validate_verified_questions,
)
from build_indexes import (
    OUTPUT_NAMES as INDEX_OUTPUT_NAMES,
    INDEX_TITLES,
    IndexBuildError,
    index_entry_counts,
    load_index_data,
    validate_index_fidelity,
)
from index_sources import IndexSourceError
from index_sources import response_index_entries, sort_key, unit_locator


PUBLICATION_ROOT = Path(__file__).resolve().parent.parent
REPOSITORY_ROOT = PUBLICATION_ROOT.parent
CHAPTER_ONE = (
    PUBLICATION_ROOT / "content" / "01-catastro" / "01-catastro-ensenada.qmd"
)
CHAPTER_TWO = (
    PUBLICATION_ROOT
    / "content"
    / "01-catastro"
    / "02-respuestas-generales-interrogatorio.qmd"
)
CHAPTER_THREE = (
    PUBLICATION_ROOT
    / "content"
    / "01-catastro"
    / "03-expediente-sorribos-santibanez.qmd"
)
CHAPTER_FOUR = (
    PUBLICATION_ROOT
    / "content"
    / "01-catastro"
    / "04-manuscrito-volumen-actual.qmd"
)
CHAPTER_FIVE = (
    PUBLICATION_ROOT
    / "content"
    / "02-estudio"
    / "05-lugar-senorio-concejo-ordas.qmd"
)
CHAPTER_SIX = (
    PUBLICATION_ROOT
    / "content"
    / "02-estudio"
    / "06-vecinos-hogares-viviendas-trabajo.qmd"
)
CHAPTER_SEVEN = (
    PUBLICATION_ROOT
    / "content"
    / "02-estudio"
    / "07-tierra-sistema-agrario-medidas.qmd"
)
CHAPTER_EIGHT = (
    PUBLICATION_ROOT
    / "content"
    / "02-estudio"
    / "08-ganaderia-montes-aprovechamientos-comunales.qmd"
)
CHAPTER_NINE = (
    PUBLICATION_ROOT / "content" / "02-estudio" / "09-rio-molinos-recursos.qmd"
)
CHAPTER_TEN = (
    PUBLICATION_ROOT
    / "content"
    / "02-estudio"
    / "10-iglesia-senorio-fiscalidad.qmd"
)
CHAPTER_ELEVEN = (
    PUBLICATION_ROOT
    / "content"
    / "02-estudio"
    / "11-hacienda-concejil-servicios-colectivos.qmd"
)
CHAPTER_TWELVE = (
    PUBLICATION_ROOT
    / "content"
    / "02-estudio"
    / "12-dinero-oficios-conexiones-exteriores.qmd"
)
CHAPTER_THIRTEEN = (
    PUBLICATION_ROOT
    / "content"
    / "02-estudio"
    / "13-economia-rural-integrada-vulnerabilidades-resiliencia-limites.qmd"
)
GENERATED = {
    "facsimile": PUBLICATION_ROOT / "generated" / "14-facsimil-prototipo.qmd",
    "facsimile_full": PUBLICATION_ROOT / "generated" / "14-facsimil.qmd",
    "transcription": PUBLICATION_ROOT / "generated" / "15-transcripcion-prototipo.qmd",
    "transcription_full": PUBLICATION_ROOT / "generated" / "15-transcripcion.qmd",
    "modernized": PUBLICATION_ROOT / "generated" / "16-modernizada-prototipo.qmd",
    "modernized_full": PUBLICATION_ROOT / "generated" / "16-edicion-modernizada.qmd",
    "glossary_full": PUBLICATION_ROOT / "generated" / "glosario.qmd",
    "quantitative_full": PUBLICATION_ROOT / "generated" / "cuadros-cuantitativos.qmd",
    "concordance_full": PUBLICATION_ROOT / "generated" / "concordancia.qmd",
    "evidence_matrix_full": PUBLICATION_ROOT / "generated" / "matriz-evidencia.qmd",
    "apparatus": PUBLICATION_ROOT / "generated" / "aparato-molinos.qmd",
}
CANONICAL_EDITION = (
    REPOSITORY_ROOT / "project" / "20_TRABAJO_EDITORIAL" / "Edicion_Critica.md"
)
RENDERED_HTML = (
    PUBLICATION_ROOT / "_book" / "generated" / "15-transcripcion.html"
)
RENDERED_MODERNIZED_HTML = (
    PUBLICATION_ROOT / "_book" / "generated" / "16-edicion-modernizada.html"
)
RENDERED_APPARATUS_HTML = {
    "glosario.qmd": PUBLICATION_ROOT / "_book" / "generated" / "glosario.html",
    "cuadros-cuantitativos.qmd": (
        PUBLICATION_ROOT / "_book" / "generated" / "cuadros-cuantitativos.html"
    ),
    "concordancia.qmd": (
        PUBLICATION_ROOT / "_book" / "generated" / "concordancia.html"
    ),
    "matriz-evidencia.qmd": (
        PUBLICATION_ROOT / "_book" / "generated" / "matriz-evidencia.html"
    ),
}
RENDERED_INDEX_HTML = {
    name: PUBLICATION_ROOT / "_book" / "generated" / "indices" / name.replace(".qmd", ".html")
    for name in INDEX_OUTPUT_NAMES
}
RENDERED_FACSIMILE_HTML = (
    PUBLICATION_ROOT / "_book" / "generated" / "14-facsimil.html"
)
RENDERED_CHAPTER_ONE_HTML = (
    PUBLICATION_ROOT
    / "_book"
    / "content"
    / "01-catastro"
    / "01-catastro-ensenada.html"
)
RENDERED_CHAPTER_TWO_HTML = (
    PUBLICATION_ROOT
    / "_book"
    / "content"
    / "01-catastro"
    / "02-respuestas-generales-interrogatorio.html"
)
RENDERED_CHAPTER_THREE_HTML = (
    PUBLICATION_ROOT
    / "_book"
    / "content"
    / "01-catastro"
    / "03-expediente-sorribos-santibanez.html"
)
RENDERED_CHAPTER_FOUR_HTML = (
    PUBLICATION_ROOT
    / "_book"
    / "content"
    / "01-catastro"
    / "04-manuscrito-volumen-actual.html"
)
RENDERED_CHAPTER_FIVE_HTML = (
    PUBLICATION_ROOT
    / "_book"
    / "content"
    / "02-estudio"
    / "05-lugar-senorio-concejo-ordas.html"
)
RENDERED_CHAPTER_SIX_HTML = (
    PUBLICATION_ROOT
    / "_book"
    / "content"
    / "02-estudio"
    / "06-vecinos-hogares-viviendas-trabajo.html"
)
RENDERED_CHAPTER_SEVEN_HTML = (
    PUBLICATION_ROOT
    / "_book"
    / "content"
    / "02-estudio"
    / "07-tierra-sistema-agrario-medidas.html"
)
RENDERED_CHAPTER_EIGHT_HTML = (
    PUBLICATION_ROOT
    / "_book"
    / "content"
    / "02-estudio"
    / "08-ganaderia-montes-aprovechamientos-comunales.html"
)
RENDERED_CHAPTER_NINE_HTML = (
    PUBLICATION_ROOT
    / "_book"
    / "content"
    / "02-estudio"
    / "09-rio-molinos-recursos.html"
)
RENDERED_CHAPTER_TEN_HTML = (
    PUBLICATION_ROOT
    / "_book"
    / "content"
    / "02-estudio"
    / "10-iglesia-senorio-fiscalidad.html"
)
RENDERED_CHAPTER_ELEVEN_HTML = (
    PUBLICATION_ROOT
    / "_book"
    / "content"
    / "02-estudio"
    / "11-hacienda-concejil-servicios-colectivos.html"
)
RENDERED_CHAPTER_TWELVE_HTML = (
    PUBLICATION_ROOT
    / "_book"
    / "content"
    / "02-estudio"
    / "12-dinero-oficios-conexiones-exteriores.html"
)
RENDERED_CHAPTER_THIRTEEN_HTML = (
    PUBLICATION_ROOT
    / "_book"
    / "content"
    / "02-estudio"
    / "13-economia-rural-integrada-vulnerabilidades-resiliencia-limites.html"
)
RENDERED_PDF = (
    PUBLICATION_ROOT / "_book" / "sorribos-santibanez-ordas-1752.pdf"
)
UNIT_HEADINGS = (
    "Imagen",
    PALEOGRAPHIC_SECTION,
    "Observaciones editoriales",
    "Notas paleográficas",
    "Notas históricas",
    "Referencias cruzadas",
)
DOCUMENTARY_HYPHEN_ENDINGS = (
    "Bartho-",
    "pro-",
    "invier-",
    "respec-",
    "An-",
    "Manu-",
    "re-",
)
CANONICAL_FORMULA = (
    "ocho ruedas descritas en cuatro casas de molinos; además existe un molino "
    "venturero cuyo número de ruedas no consta"
)
CHAPTER_ONE_SOURCE_PATHS = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Introduccion_Catastro_Ensenada_Sorrios.md",
    "project/00_CONTROL/Manual_Editorial.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
}
CHAPTER_ONE_LINKS = {
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=10",
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=32",
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=33",
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=40",
    "https://www.catastro.hacienda.gob.es/es-ES/fondo_editorial.html",
}
CHAPTER_TWO_SOURCE_PATHS = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Introduccion_Catastro_Ensenada_Sorrios.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Verificacion_Interrogatorio_40_Preguntas.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/00_CONTROL/Manual_Editorial.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
}
CHAPTER_TWO_LINKS = {
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=30",
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=31b",
    "https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=32",
    "https://www.catastro.hacienda.gob.es/documentos/publicaciones/catalogoensenada_1752_vera.pdf",
}
CHAPTER_THREE_SOURCE_PATHS = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Introduccion_Catastro_Ensenada_Sorrios.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/00_CONTROL/unidades.yaml",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
}
CHAPTER_THREE_EVIDENCE = {
    "D": ("JUR-001", "JUR-002", "JUR-003", "JUR-004", "TOP-001"),
    "I": ("TOP-002",),
    "E": (
        "TOP-004",
        "TOP-005",
        "TOP-007",
        "TOP-008",
        "TOP-009",
        "TOP-010",
        "TOP-011",
        "JUR-009",
    ),
}
CHAPTER_FOUR_SOURCE_PATHS = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Introduccion_Catastro_Ensenada_Sorrios.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/00_CONTROL/unidades.yaml",
    "project/00_CONTROL/Manual_Editorial.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Criterios_Edicion_Modernizada.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "docs/PLAN_MAESTRO_PUBLICACION_QUARTO.md",
    "publication/README.md",
}
CHAPTER_FIVE_SOURCE_PATHS = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Introduccion_Catastro_Ensenada_Sorrios.md",
}
CHAPTER_FIVE_EVIDENCE = {
    "D": ("JUR-001", "JUR-002", "JUR-005", "JUR-006", "FIS-012"),
    "E": ("JUR-007", "JUR-008"),
    "L": ("LIM-011",),
}
CHAPTER_FIVE_ANCHORS = (
    "lugar-actores",
    "lugar-concejo-municipio",
    "lugar-senorio-conde",
    "lugar-derechos",
    "lugar-termino",
    "lugar-sintesis",
)
CHAPTER_SIX_SOURCE_PATHS = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Oficios.md",
}
CHAPTER_SIX_EVIDENCE = {
    "D": (
        "DEM-001", "DEM-002", "DEM-003", "DEM-004", "GAN-007",
        "TRA-001", "TRA-002", "TRA-003", "TRA-004", "TRA-005", "FIS-007",
    ),
    "C": ("CAL-018", "CAL-019"),
    "I": ("INT-002", "INT-008", "INT-010"),
    "E": ("DEM-005", "DEM-006"),
    "L": ("LIM-001", "LIM-002", "LIM-008"),
}
CHAPTER_SIX_ANCHORS = (
    "vecinos-recuento",
    "avitadores-poblacion",
    "personas-hogares",
    "casas-viviendas",
    "trabajo-categorias",
    "trabajo-utilidades",
    "estructura-limites",
)
CHAPTER_SEVEN_SOURCE_PATHS = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Plan_Composicion_Volumen_0_5.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md",
}
CHAPTER_SEVEN_EVIDENCE = {
    "D": (
        "TER-001", "TER-002", "TER-003", "TER-004", "TER-005", "TER-006",
        "TER-010", "AGR-001", "AGR-002", "AGR-003", "AGR-007", "AGR-008",
        "AGR-010",
    ),
    "C": (
        "TER-007", "TER-008", "AGR-004", "AGR-005", "AGR-006", "AGR-009",
        "CAL-001", "CAL-002", "CAL-003", "CAL-004", "CAL-005", "CAL-006",
        "CAL-007", "CAL-008", "CAL-009",
    ),
    "I": ("INT-001", "INT-003"),
    "E": ("TER-011", "AGR-011", "AGR-012", "AGR-013"),
    "L": ("TER-009", "LIM-003", "LIM-004", "LIM-005", "LIM-006", "LIM-007", "LIM-009"),
}
CHAPTER_SEVEN_ANCHORS = (
    "tierra-clases",
    "tierra-calidades",
    "tierra-medidas",
    "tierra-cabida",
    "tierra-centeno",
    "tierra-ciclos",
    "tierra-rendimientos",
    "tierra-produccion-limites",
    "tierra-sintesis",
)
CHAPTER_EIGHT_SOURCE_PATHS = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/20_TRABAJO_EDITORIAL/Glosario.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md",
}
CHAPTER_EIGHT_EVIDENCE = {
    "D": ("TER-001", "GAN-001", "GAN-002", "GAN-007"),
    "C": (),
    "I": ("INT-002", "INT-004"),
    "E": ("AGR-012", "AGR-013", "GAN-008"),
    "L": ("TER-009", "LIM-008", "LIM-009"),
}
CHAPTER_EIGHT_ANCHORS = (
    "ganado-alcance",
    "ganado-valores",
    "ganado-funciones",
    "pastos-recursos",
    "montes-arbolado",
    "uso-comun",
    "articulacion-agraria",
    "ganado-limites",
    "ganado-sintesis",
)
CHAPTER_NINE_SOURCE_PATHS = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/20_TRABAJO_EDITORIAL/Glosario.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md",
}
CHAPTER_NINE_EVIDENCE = {
    "D": ("HID-001", "HID-003", "HID-005", "HID-006", "GAN-003", "GAN-004", "FIS-012"),
    "C": (
        "HID-002", "HID-004", "GAN-005", "GAN-006", "CAL-010",
        "CAL-011", "CAL-012", "CAL-013", "CAL-020",
    ),
    "I": ("HID-007", "INT-002", "INT-005"),
    "E": ("HID-008",),
    "L": ("LIM-005", "LIM-008", "LIM-009", "LIM-010", "LIM-011"),
}
CHAPTER_NINE_ANCHORS = (
    "rio-espacio-productivo",
    "molinos-recuento",
    "molinos-titulares",
    "molinos-utilidades",
    "molinos-estacionalidad",
    "molinos-cereal",
    "recursos-colmenas",
    "recursos-pesca",
    "recursos-limites",
    "recursos-sintesis",
)
CHAPTER_TEN_SOURCE_PATHS = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Plan_Composicion_Volumen_0_5.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/20_TRABAJO_EDITORIAL/Glosario.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Personas.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Instituciones.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md",
}
CHAPTER_TEN_EVIDENCE = {
    "D": (
        "JUR-005", "JUR-006", "FIS-001", "FIS-002", "FIS-003",
        "FIS-004", "FIS-008", "FIS-012",
    ),
    "C": ("CAL-009",),
    "I": ("INT-010",),
    "E": ("FIS-013",),
    "L": ("LIM-001", "LIM-002", "LIM-005", "LIM-011"),
}
CHAPTER_TEN_ANCHORS = (
    "fiscal-marco-senorial",
    "fiscal-perceptores-eclesiasticos",
    "fiscal-diezmos",
    "fiscal-primicia-voto",
    "fiscal-derechos-senoriales",
    "fiscal-exenciones",
    "fiscal-sujetos-bases",
    "fiscal-magnitudes",
    "fiscal-limites",
    "fiscal-sintesis",
)
CHAPTER_ELEVEN_SOURCE_PATHS = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Plan_Composicion_Volumen_0_5.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/20_TRABAJO_EDITORIAL/Glosario.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Instituciones.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Toponimos.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md",
}
CHAPTER_ELEVEN_EVIDENCE = {
    "D": ("FIS-005", "FIS-006", "FIS-007", "FIS-008", "GAN-002", "TRA-005"),
    "C": (),
    "I": ("INT-004", "INT-006"),
    "E": ("FIS-014", "FIS-015", "FIS-016", "FIS-017", "TRA-006"),
    "L": ("LIM-012", "LIM-013"),
}
CHAPTER_ELEVEN_ANCHORS = (
    "hacienda-sujetos",
    "hacienda-recursos",
    "hacienda-partidas",
    "hacienda-repartimiento",
    "hacienda-destinos",
    "hacienda-ausencias",
    "hacienda-servicios",
    "hacienda-infraestructuras",
    "hacienda-presupuesto-limites",
    "hacienda-sintesis",
)
CHAPTER_TWELVE_SOURCE_PATHS = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Plan_Composicion_Volumen_0_5.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/20_TRABAJO_EDITORIAL/Glosario.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Oficios.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Personas.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Toponimos.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Instituciones.md",
    "project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md",
}
CHAPTER_TWELVE_EVIDENCE = {
    "D": (
        "GAN-001", "GAN-003", "HID-005", "TRA-001", "TRA-002",
        "TRA-003", "TRA-004", "TRA-005", "JUR-006", "FIS-002",
        "FIS-003", "FIS-004", "FIS-006", "FIS-007", "FIS-012",
    ),
    "C": (
        "GAN-005", "HID-004", "FIS-009", "FIS-010", "FIS-011",
        "CAL-010", "CAL-014", "CAL-015", "CAL-016", "CAL-017",
    ),
    "I": ("INT-007", "INT-008", "INT-010"),
    "E": ("JUR-009", "FIS-013", "FIS-014", "FIS-015"),
    "L": (
        "LIM-002", "LIM-005", "LIM-006", "LIM-008", "LIM-009",
        "LIM-011", "LIM-012", "LIM-013",
    ),
}
CHAPTER_TWELVE_ANCHORS = (
    "dinero-formas",
    "dinero-precios-valores",
    "dinero-naturalezas",
    "dinero-minimo-institucional",
    "oficios-categorias",
    "oficios-jornales",
    "oficios-servicios-ausencias",
    "conexiones-exteriores",
    "dinero-mercado-limites",
    "dinero-sintesis",
)
CHAPTER_THIRTEEN_SOURCE_PATHS = {
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Plan_Composicion_Volumen_0_5.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md",
    "project/20_TRABAJO_EDITORIAL/Edicion_Critica.md",
    "project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md",
    "project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md",
    "publication/content/02-estudio/05-lugar-senorio-concejo-ordas.qmd",
    "publication/content/02-estudio/06-vecinos-hogares-viviendas-trabajo.qmd",
    "publication/content/02-estudio/07-tierra-sistema-agrario-medidas.qmd",
    "publication/content/02-estudio/08-ganaderia-montes-aprovechamientos-comunales.qmd",
    "publication/content/02-estudio/09-rio-molinos-recursos.qmd",
    "publication/content/02-estudio/10-iglesia-senorio-fiscalidad.qmd",
    "publication/content/02-estudio/11-hacienda-concejil-servicios-colectivos.qmd",
    "publication/content/02-estudio/12-dinero-oficios-conexiones-exteriores.qmd",
}
CHAPTER_THIRTEEN_EVIDENCE = {
    "D": (
        "JUR-001", "JUR-002", "JUR-005", "JUR-006", "TER-001",
        "TER-010", "AGR-001", "AGR-002", "AGR-003", "AGR-010",
        "GAN-001", "GAN-002", "GAN-003", "GAN-007", "HID-001",
        "HID-005", "HID-006", "DEM-001", "DEM-003", "TRA-001",
        "TRA-002", "TRA-003", "TRA-004", "TRA-005", "FIS-001",
        "FIS-002", "FIS-003", "FIS-004", "FIS-005", "FIS-006",
        "FIS-007", "FIS-008", "FIS-012",
    ),
    "C": (
        "AGR-004", "AGR-005", "AGR-006", "GAN-005", "HID-002",
        "HID-004", "FIS-009", "FIS-010", "FIS-011", "CAL-003",
        "CAL-004", "CAL-005", "CAL-006", "CAL-012", "CAL-013",
        "CAL-014", "CAL-015", "CAL-016", "CAL-017",
    ),
    "I": (
        "INT-001", "INT-002", "INT-003", "INT-004", "INT-005",
        "INT-006", "INT-007", "INT-008", "INT-009", "INT-010",
    ),
    "E": (
        "TER-011", "AGR-011", "AGR-012", "AGR-013", "GAN-008",
        "HID-008", "TRA-006", "FIS-013", "FIS-014", "FIS-015",
        "FIS-016", "FIS-017",
    ),
    "L": (
        "LIM-001", "LIM-002", "LIM-003", "LIM-004", "LIM-005",
        "LIM-006", "LIM-007", "LIM-008", "LIM-009", "LIM-010",
        "LIM-011", "LIM-012", "LIM-013",
    ),
}
CHAPTER_THIRTEEN_ANCHORS = (
    "economia-integrada-alcance",
    "economia-base-agraria",
    "economia-agua-transformacion",
    "economia-trabajo-instituciones",
    "economia-dependencias",
    "economia-diversidad-amortiguadores",
    "economia-vulnerabilidades",
    "economia-resiliencia-limites",
    "economia-limites-reconstruccion",
    "economia-sintesis",
    "economia-transicion-manuscrito",
)
CHAPTER_TWO_THEMATIC_BLOCKS = (
    ("1–3", "Nombre, jurisdicción, término y límites"),
    ("4–14", "Tierras, árboles, medidas, cabidas, frutos y valores"),
    ("15–16", "Diezmos, primicia, voto y cuantía"),
    ("17", "Minas, salinas, molinos y otros artefactos"),
    ("18–20", "Esquileo, colmenas y ganados"),
    ("21–22", "Vecinos, casas y edificios"),
    ("23–28", "Propios, arbitrios, gastos, cargas y rentas enajenadas"),
    ("29–34", "Servicios, comercio y oficios"),
    ("35–39", "Jornaleros, pobres, embarcaciones, clérigos y conventos"),
    ("40", "Fincas o rentas del rey"),
)
QUESTIONNAIRE_MIN_DISTINCT_MARKERS = 20
QUESTIONNAIRE_MIN_CONSECUTIVE_MARKERS = 15
QUESTION_MARKER_PATTERNS = (
    re.compile(
        r"^(?:(?:pregunta|respuesta)\s+)?"
        r"(?P<number>[1-9]|[1-3]\d|40)\s*(?:[.):-]\s*|\s+|$)",
        re.IGNORECASE,
    ),
    re.compile(
        r"^\|\s*(?:(?:pregunta|respuesta)\s+)?"
        r"(?P<number>[1-9]|[1-3]\d|40)\s*\|",
        re.IGNORECASE,
    ),
)


class _LineBlockParser(HTMLParser):
    """Collect visible lines from semantic Pandoc line blocks."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.blocks: list[tuple[str, ...]] = []
        self._depth = 0
        self._lines: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        classes = (attributes.get("class") or "").split()
        if self._depth == 0 and tag == "div" and "line-block" in classes:
            self._depth = 1
            self._lines = [""]
        elif self._depth and tag == "br":
            self._lines.append("")
        elif self._depth:
            self._depth += 1

    def handle_startendtag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if self._depth and tag == "br":
            self._lines.append("")

    def handle_endtag(self, tag: str) -> None:
        if not self._depth:
            return
        self._depth -= 1
        if self._depth == 0:
            self.blocks.append(tuple(line.strip() for line in self._lines))
            self._lines = []

    def handle_data(self, data: str) -> None:
        if self._depth:
            # Pandoc may use a non-breaking sentence space in HTML. It is a
            # layout character, not a textual difference from the source.
            self._lines[-1] += data.replace("\xa0", " ")


def _generated_paleographic_lines(text: str) -> tuple[str, ...]:
    match = re.search(
        rf"^### {re.escape(PALEOGRAPHIC_SECTION)}\s*$\n+(?P<body>.*?)(?=^### |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if match is None:
        return ()
    lines = [line for line in match.group("body").rstrip().splitlines() if line]
    if any(not line.startswith("| ") for line in lines):
        return ()
    return tuple(line[2:] for line in lines)


def _generated_transcription_units(text: str) -> tuple[tuple[str, str, dict[str, str]], ...]:
    """Parse the generated 4B units for explicit source/output comparison."""

    _, body = _parse_document(text, GENERATED["transcription_full"])
    matches = list(
        re.finditer(
            r"^## (?P<label>.+?) \{#(?P<anchor>[a-z0-9-]+)\}\s*$",
            body,
            re.MULTILINE,
        )
    )
    units: list[tuple[str, str, dict[str, str]]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        block = body[match.end():end]
        section_matches = list(
            re.finditer(r"^### (?P<name>[^\n]+)\s*$", block, re.MULTILINE)
        )
        sections: dict[str, str] = {}
        for section_index, section_match in enumerate(section_matches):
            section_end = (
                section_matches[section_index + 1].start()
                if section_index + 1 < len(section_matches)
                else len(block)
            )
            content = block[section_match.end():section_end].strip("\n")
            if content.endswith("\n\\newpage"):
                content = content[:-9].rstrip("\n")
            sections[section_match.group("name").strip()] = content
        units.append((match.group("label"), match.group("anchor"), sections))
    return tuple(units)


def _decode_line_block(text: str) -> str:
    decoded: list[str] = []
    for line in text.splitlines():
        if line == "|":
            decoded.append("")
        elif line.startswith("| "):
            decoded.append(line[2:])
        else:
            return ""
    return "\n".join(decoded).replace(r"[\.\.\.]", "[...]")


def _questionnaire_markers(text: str) -> tuple[int, ...]:
    markers: set[int] = set()
    for raw_line in text.splitlines():
        line = re.sub(r"^\s*(?:#{1,6}|>|[-+*])\s*", "", raw_line)
        line = line.translate(str.maketrans("", "", "*_`")).strip()
        for pattern in QUESTION_MARKER_PATTERNS:
            match = pattern.match(line)
            if match is not None:
                markers.add(int(match.group("number")))
                break
    return tuple(sorted(markers))


def _has_extensive_questionnaire_sequence(text: str) -> bool:
    markers = _questionnaire_markers(text)
    if len(markers) < QUESTIONNAIRE_MIN_DISTINCT_MARKERS:
        return False

    longest_run = 1
    current_run = 1
    for previous, current in zip(markers, markers[1:]):
        if current == previous + 1:
            current_run += 1
            longest_run = max(longest_run, current_run)
        else:
            current_run = 1
    return longest_run >= QUESTIONNAIRE_MIN_CONSECUTIVE_MARKERS


def _html_line_blocks(path: Path) -> list[tuple[str, ...]]:
    parser = _LineBlockParser()
    parser.feed(path.read_text(encoding="utf-8"))
    parser.close()
    return parser.blocks


def _pdf_text_lines(path: Path) -> tuple[str, ...]:
    executable = shutil.which("pdftotext")
    if executable is None:
        raise RuntimeError("No se encontró pdftotext en PATH")
    result = subprocess.run(
        [executable, "-layout", path, "-"],
        check=True,
        capture_output=True,
        text=True,
        shell=False,
    )
    return tuple(line.strip() for line in result.stdout.splitlines())


def _contains_ordered_lines(haystack: tuple[str, ...], needles: tuple[str, ...]) -> bool:
    def comparable(line: str) -> str:
        # LuaLaTeX preserves these editorial brackets visually, but pdftotext
        # may extract the linked abbreviation expansion before its brackets.
        return re.sub(r"\[([A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+)\]", r"\1", line)

    position = 0
    for line in haystack:
        if position < len(needles) and (
            line == needles[position]
            or comparable(line) == comparable(needles[position])
        ):
            position += 1
    return position == len(needles)


def _pdf_page_texts(path: Path) -> tuple[str, ...]:
    executable = shutil.which("pdftotext")
    if executable is None:
        raise RuntimeError("No se encontró pdftotext en PATH")
    result = subprocess.run(
        [executable, "-layout", path, "-"],
        check=True,
        capture_output=True,
        text=True,
        shell=False,
    )
    return tuple(result.stdout.split("\f"))


def _index_pdf_locator_errors(path: Path) -> list[str]:
    """Compare a distributed sample of printed index pages with target pages."""

    errors: list[str] = []
    pages = _pdf_page_texts(path)
    data = load_index_data(REPOSITORY_ROOT, PUBLICATION_ROOT)
    by_label = {spec.label: spec for spec in data.specs}
    samples: list[tuple[str, str, object]] = []
    for index in data.live:
        ordered = sorted(index.entries, key=lambda entry: sort_key(entry.term))
        entry = ordered[len(ordered) // 2]
        samples.append(
            (
                INDEX_TITLES[index.index_id],
                entry.term,
                unit_locator(by_label[entry.units[0]]),
            )
        )
    editorial = {index.index_id: index for index in data.editorial}
    for index_id in ("productos-recursos", "cargas-fiscalidad"):
        ordered = sorted(editorial[index_id].entries, key=lambda entry: sort_key(entry.term))
        entry = ordered[len(ordered) // 2]
        samples.append((INDEX_TITLES[index_id], entry.term, entry.targets[0]))
    response_term, response_target = response_index_entries(data.modernized)[16]
    samples.append((INDEX_TITLES["preguntas-respuestas"], response_term, response_target))
    matter = sorted(
        editorial["materias"].entries, key=lambda entry: sort_key(entry.term)
    )
    matter_entry = matter[len(matter) // 2]
    samples.append((INDEX_TITLES["materias"], matter_entry.term, matter_entry.targets[0]))

    index_starts: dict[str, int] = {}
    for title in INDEX_TITLES.values():
        matches = [
            position
            for position, page in enumerate(pages, start=1)
            if title in " ".join(page.split())
            and "Parte VI. Aparatos e índices" in " ".join(page.split())
        ]
        if len(matches) != 1:
            errors.append(f"No se pudo delimitar en PDF el índice {title!r}")
        else:
            index_starts[title] = matches[0]
    if errors:
        return errors
    first_index_page = min(index_starts.values())

    for title, term, locator in samples:
        start = index_starts[title]
        following = [page for page in index_starts.values() if page > start]
        end = min(following) - 1 if following else len(pages)
        lines = [
            line.strip()
            for page in pages[start - 1 : end]
            for line in page.splitlines()
        ]
        printed: tuple[int, ...] = ()
        for position, line in enumerate(lines):
            if line != term:
                continue
            for candidate in lines[position + 1 : position + 45]:
                match = re.fullmatch(r"Páginas:\s*([0-9][0-9, ]*)", candidate)
                if match:
                    printed = tuple(
                        int(value.strip()) for value in match.group(1).split(",")
                    )
                    break
            if printed:
                break
        if not printed:
            errors.append(f"No se pudo leer el localizador PDF de {term!r}")
            continue
        if locator.kind == "unit":
            pattern = re.compile(rf"^15\.\d+\s+{re.escape(locator.label)}$")
            target_pages = [
                position
                for position, page in enumerate(pages[: first_index_page - 1], start=1)
                if any(pattern.match(line.strip()) for line in page.splitlines())
            ]
        elif locator.kind == "response":
            pattern = re.compile(rf"^16\.\d+\s+Respuesta {re.escape(locator.key)}\.")
            target_pages = [
                position
                for position, page in enumerate(pages[: first_index_page - 1], start=1)
                if any(pattern.match(line.strip()) for line in page.splitlines())
            ]
        else:
            heading = locator.label.split(": ", 1)[1]
            target_pages = [
                position
                for position, page in enumerate(pages[: first_index_page - 1], start=1)
                if any(heading == line.strip().split(" ", 1)[-1] for line in page.splitlines())
            ]
        if not target_pages:
            errors.append(f"No se pudo hallar en PDF el destino de {term!r}: {locator.key}")
        elif target_pages[-1] not in printed:
            errors.append(
                f"Localizador PDF discordante para {term!r}: imprime {printed}, "
                f"destino real {target_pages[-1]}"
            )
    return errors


def _rendered_link_and_id_errors(book_root: Path) -> list[str]:
    """Audit duplicate IDs and every rendered local fragment link in the HTML book."""

    errors: list[str] = []
    html_paths = sorted(book_root.rglob("*.html"))
    ids_by_path: dict[Path, set[str]] = {}
    texts: dict[Path, str] = {}
    for path in html_paths:
        text = path.read_text(encoding="utf-8")
        texts[path] = text
        identifiers = re.findall(r'(?:^|\s)id="([^"]+)"', text)
        duplicates = sorted(
            identifier for identifier in set(identifiers) if identifiers.count(identifier) > 1
        )
        if duplicates:
            errors.append(
                f"IDs HTML duplicados en {path.relative_to(book_root)}: "
                + ", ".join(duplicates)
            )
        ids_by_path[path.resolve()] = set(identifiers)
    for source, text in texts.items():
        for raw_href in re.findall(r'href="([^"]+)"', text):
            href = html_module.unescape(raw_href)
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc or not parsed.fragment:
                continue
            if parsed.path.startswith("/"):
                continue
            target = (
                source.resolve()
                if not parsed.path
                else (source.parent / unquote(parsed.path)).resolve()
            )
            if target.suffix != ".html":
                continue
            if target not in ids_by_path:
                errors.append(
                    f"Enlace HTML a documento inexistente desde {source.relative_to(book_root)}: {href}"
                )
                continue
            fragment = unquote(parsed.fragment)
            if fragment not in ids_by_path[target]:
                errors.append(
                    f"Enlace HTML a ancla inexistente desde {source.relative_to(book_root)}: {href}"
                )
    return errors


def validate_rendered_outputs() -> list[str]:
    """Validate lineation in the actual HTML and PDF book artifacts."""

    errors: list[str] = []
    edition_text = CANONICAL_EDITION.read_text(encoding="utf-8")
    canonical = read_paleographic_lines(edition_text)
    specs = load_unit_specs(
        REPOSITORY_ROOT / "project" / "00_CONTROL" / "unidades.yaml"
    )
    canonical_units = parse_critical_edition(
        edition_text,
        specs,
        "sorrios_ensenada_orden_lectura_calidad_original.pdf",
    )
    if not RENDERED_CHAPTER_ONE_HTML.is_file():
        errors.append(f"Falta el HTML del capítulo 1: {RENDERED_CHAPTER_ONE_HTML}")
    else:
        chapter_html = RENDERED_CHAPTER_ONE_HTML.read_text(encoding="utf-8")
        if "El Catastro de Ensenada" not in chapter_html:
            errors.append("El HTML del capítulo 1 no contiene su título")
        if 'name="viewport"' not in chapter_html:
            errors.append("El HTML del capítulo 1 carece de metadatos adaptables")
        for url in CHAPTER_ONE_LINKS:
            encoded_url = url.replace("&", "&amp;")
            if url not in chapter_html and encoded_url not in chapter_html:
                errors.append(f"Falta el enlace institucional en HTML: {url}")

    if not RENDERED_CHAPTER_TWO_HTML.is_file():
        errors.append(f"Falta el HTML del capítulo 2: {RENDERED_CHAPTER_TWO_HTML}")
    else:
        chapter_two_html = RENDERED_CHAPTER_TWO_HTML.read_text(encoding="utf-8")
        if (
            "Las Respuestas Generales y el interrogatorio de cuarenta preguntas"
            not in chapter_two_html
        ):
            errors.append("El HTML del capítulo 2 no contiene su título")
        if 'name="viewport"' not in chapter_two_html:
            errors.append("El HTML del capítulo 2 carece de metadatos adaptables")
        for url in CHAPTER_TWO_LINKS:
            encoded_url = url.replace("&", "&amp;")
            if url not in chapter_two_html and encoded_url not in chapter_two_html:
                errors.append(f"Falta el enlace institucional de 3B en HTML: {url}")
        for question_range, subject in CHAPTER_TWO_THEMATIC_BLOCKS:
            if question_range not in chapter_two_html or subject not in chapter_two_html:
                errors.append(
                    f"Falta el bloque temático {question_range} en el HTML del capítulo 2"
                )

    rendered_chapters = (
        (
            RENDERED_CHAPTER_THREE_HTML,
            "El expediente de Sorribos y Santibáñez de Ordás",
            3,
            "04-manuscrito-volumen-actual.html",
        ),
        (
            RENDERED_CHAPTER_FOUR_HTML,
            "Del manuscrito al volumen actual",
            4,
            "03-expediente-sorribos-santibanez.html",
        ),
        (
            RENDERED_CHAPTER_FIVE_HTML,
            "Un lugar de señorío en el Concejo de Ordás",
            5,
            "04-manuscrito-volumen-actual.html",
        ),
        (
            RENDERED_CHAPTER_SIX_HTML,
            "Vecinos, hogares, viviendas y trabajo",
            6,
            "05-lugar-senorio-concejo-ordas.html",
        ),
        (
            RENDERED_CHAPTER_SEVEN_HTML,
            "Tierra, sistema agrario y medidas",
            7,
            "06-vecinos-hogares-viviendas-trabajo.html",
        ),
        (
            RENDERED_CHAPTER_EIGHT_HTML,
            "Ganadería, montes y aprovechamientos comunales",
            8,
            "07-tierra-sistema-agrario-medidas.html",
        ),
        (
            RENDERED_CHAPTER_NINE_HTML,
            "Río, molinos y otros recursos productivos",
            9,
            "08-ganaderia-montes-aprovechamientos-comunales.html",
        ),
        (
            RENDERED_CHAPTER_TEN_HTML,
            "Iglesia, señorío y fiscalidad",
            10,
            "09-rio-molinos-recursos.html",
        ),
        (
            RENDERED_CHAPTER_ELEVEN_HTML,
            "Hacienda concejil y servicios colectivos",
            11,
            "10-iglesia-senorio-fiscalidad.html",
        ),
        (
            RENDERED_CHAPTER_TWELVE_HTML,
            "Dinero, oficios y conexiones exteriores",
            12,
            "11-hacienda-concejil-servicios-colectivos.html",
        ),
        (
            RENDERED_CHAPTER_THIRTEEN_HTML,
            "Una economía rural integrada: vulnerabilidades, resiliencia y límites",
            13,
            "12-dinero-oficios-conexiones-exteriores.html",
        ),
    )
    for path, title, number, linked_chapter in rendered_chapters:
        if not path.is_file():
            errors.append(f"Falta el HTML del capítulo {number}: {path}")
            continue
        html = path.read_text(encoding="utf-8")
        if title not in html:
            errors.append(f"El HTML del capítulo {number} no contiene su título")
        if 'name="viewport"' not in html:
            errors.append(
                f"El HTML del capítulo {number} carece de metadatos adaptables"
            )
        if linked_chapter not in html:
            errors.append(
                f"El HTML del capítulo {number} no conserva su enlace cruzado"
            )
        if number in (5, 6, 7, 8, 9, 10, 11, 12, 13) and not re.search(
            rf'class="chapter-number"[^>]*>\s*{number}\s*<', html
        ):
            errors.append(
                f"El capítulo {number} no aparece numerado realmente como {number}"
            )

    if not RENDERED_FACSIMILE_HTML.is_file():
        errors.append(f"Falta el HTML del capítulo 14: {RENDERED_FACSIMILE_HTML}")
    else:
        facsimile_html = RENDERED_FACSIMILE_HTML.read_text(encoding="utf-8")
        if "Facsímil íntegro del expediente" not in facsimile_html:
            errors.append("El HTML del capítulo 14 no contiene su título")
        if 'name="viewport"' not in facsimile_html:
            errors.append("El HTML del capítulo 14 carece de metadatos adaptables")
        if not re.search(r'class="chapter-number"[^>]*>\s*14\s*<', facsimile_html):
            errors.append("El facsímil no aparece numerado realmente como capítulo 14")
        anchors = re.findall(
            r'<section id="pagina-digital-(\d{2})"', facsimile_html
        )
        if anchors != [f"{page:02d}" for page in range(1, 19)]:
            errors.append("El HTML facsimilar no conserva las 18 anclas en orden")
        images = re.findall(r'src="assets/facsimile/page-(\d{2})\.png"', facsimile_html)
        if images != [f"{page:02d}" for page in range(1, 19)]:
            errors.append("El HTML facsimilar no contiene las 18 páginas en orden")
        alt_pages = re.findall(
            r'<img[^>]+src="assets/facsimile/page-\d{2}\.png"[^>]+'
            r'alt="Página digital (\d{2}) completa[^>]+>',
            facsimile_html,
        )
        if alt_pages != [f"{page:02d}" for page in range(1, 19)]:
            errors.append("Las 18 páginas HTML deben conservar texto alternativo")

    if RENDERED_CHAPTER_NINE_HTML.is_file():
        chapter_nine_html = RENDERED_CHAPTER_NINE_HTML.read_text(encoding="utf-8")
        for target in (
            "../../generated/14-facsimil.html#pagina-digital-12",
            "../../generated/15-transcripcion.html#folio-315v",
            "../../generated/16-edicion-modernizada.html#respuesta-17",
            "../../generated/matriz-evidencia.html#evidencia-hid-001",
        ):
            if target not in chapter_nine_html:
                errors.append(
                    f"El capítulo 9 no enlaza el capítulo real correspondiente: {target}"
                )
        if ".qmd#" in chapter_nine_html:
            errors.append("El HTML conserva un enlace roto hacia un QMD no renderizado")

    if not RENDERED_HTML.is_file():
        errors.append(f"Falta el HTML renderizado: {RENDERED_HTML}")
    else:
        blocks = _html_line_blocks(RENDERED_HTML)
        expected_blocks = [
            tuple(unit.sections[PALEOGRAPHIC_SECTION].splitlines())
            for unit in canonical_units
        ]
        if blocks != expected_blocks:
            errors.append(
                "El HTML del capítulo 15 no conserva los 35 bloques paleográficos exactos"
            )
        matching = [block for block in blocks if block == canonical]
        if len(matching) != 1:
            errors.append(
                "El HTML debe contener un único bloque semántico con las 18 líneas "
                "paleográficas exactas"
            )
        html_text = RENDERED_HTML.read_text(encoding="utf-8")
        anchors = re.findall(r'<section id="([a-z0-9-]+)"', html_text)
        expected_anchors = [published_unit_anchor(spec) for spec in specs]
        unit_anchors = [anchor for anchor in anchors if anchor in expected_anchors]
        if unit_anchors != expected_anchors:
            errors.append("El HTML del capítulo 15 no conserva las 35 anclas en orden")
        images = re.findall(
            r'src="assets/transcription/([a-z0-9_]+)\.png"', html_text
        )
        if images != [spec.unit_id for spec in specs]:
            errors.append("El HTML del capítulo 15 no contiene los 35 recortes en orden")
        if html_text.count('data-gallery="quarto-lightbox-gallery-') < 35:
            errors.append("Los 35 recortes HTML deben admitir ampliación")
        if "/home/" in html_text:
            errors.append("El HTML del capítulo 15 contiene una ruta local absoluta")
        collapsed = " ".join(canonical)
        if re.search(rf"<p[^>]*>\s*{re.escape(collapsed)}\s*</p>", html_text):
            errors.append("La transcripción HTML ha colapsado en un único párrafo")
    if not RENDERED_MODERNIZED_HTML.is_file():
        errors.append(
            f"Falta el HTML del capítulo 16: {RENDERED_MODERNIZED_HTML}"
        )
    else:
        modernized_html = RENDERED_MODERNIZED_HTML.read_text(encoding="utf-8")
        if "El Catastro en español actual" not in modernized_html:
            errors.append("El HTML del capítulo 16 no contiene su título")
        if not re.search(
            r'class="chapter-number"[^>]*>\s*16\s*<', modernized_html
        ):
            errors.append("La edición modernizada no aparece como capítulo 16")
        expected_anchors = (
            "modernizada-portada",
            "comparecencia",
            *(f"respuesta-{number}" for number in range(1, 41)),
            "ratificacion-edades-firmas",
            "concordancia-material",
            "notas",
            "nota-de-uso",
        )
        actual_anchors = tuple(
            anchor
            for anchor in re.findall(r'<section id="([a-z0-9-]+)"', modernized_html)
            if anchor in expected_anchors
        )
        if actual_anchors != expected_anchors:
            errors.append("El HTML del capítulo 16 no conserva sus 46 anclas en orden")
        if modernized_html.count('class="question-external"') != 40:
            errors.append("El HTML del capítulo 16 no separa visualmente las 40 preguntas")
        if modernized_html.count('class="response-local"') != 40:
            errors.append("El HTML del capítulo 16 no separa las 40 respuestas locales")
        if modernized_html.count("15-transcripcion.html#") < 40:
            errors.append(
                "El HTML del capítulo 16 no conserva la navegación material hacia el 15"
            )
        for marker in (
            "en este pueblo […] medida de tierra",
            "avitadores",
            "venta",
            "renta",
            "dado a renta",
        ):
            if marker not in modernized_html:
                errors.append(f"El HTML del capítulo 16 pierde la cautela: {marker}")
        if "/home/" in modernized_html or "project/" in modernized_html:
            errors.append("El HTML del capítulo 16 expone una ruta fuente local")
    rendered_apparatus = {
        name: path.read_text(encoding="utf-8")
        for name, path in RENDERED_APPARATUS_HTML.items()
        if path.is_file()
    }
    missing_apparatus = [
        str(path) for name, path in RENDERED_APPARATUS_HTML.items() if name not in rendered_apparatus
    ]
    if missing_apparatus:
        errors.append("Faltan HTML de aparatos 4D: " + ", ".join(missing_apparatus))
    else:
        glossary_html = rendered_apparatus["glosario.qmd"]
        glossary_anchors = re.findall(
            r'<section id="(glosario-[a-z0-9-]+)"', glossary_html
        )
        glossary_anchors = [
            anchor for anchor in glossary_anchors if anchor != "glosario-entradas"
        ]
        if len(glossary_anchors) != 22 or len(set(glossary_anchors)) != 22:
            errors.append("El HTML del glosario no conserva 22 anclas únicas")
        if glossary_html.count("15-transcripcion.html#") < 22:
            errors.append("El glosario HTML pierde enlaces al capítulo 15")
        if glossary_html.count("16-edicion-modernizada.html#") < 10:
            errors.append("El glosario HTML pierde enlaces al capítulo 16")
        for url in ("https://dle.rae.es/negrillo", "https://www.mapa.gob.es/"):
            if url not in glossary_html:
                errors.append(f"El glosario HTML pierde la fuente externa {url}")

        quantitative_html = rendered_apparatus["cuadros-cuantitativos.qmd"]
        if len(
            re.findall(r'<section id="cuadro-[a-z]+-\d{3}"', quantitative_html)
        ) != 13:
            errors.append("El HTML cuantitativo no contiene sus 13 entradas C")
        for marker in (
            "93,13 %",
            "72,16 %",
            "Denominador: cultivada comparable",
            "Denominador: total explícito principal",
            "1.006 reales",
            "2,49 %",
        ):
            if marker not in quantitative_html:
                errors.append(f"El HTML cuantitativo pierde {marker}")

        concordance_html = rendered_apparatus["concordancia.qmd"]
        if concordance_html.count("14-facsimil.html#") < 75:
            errors.append("La concordancia HTML pierde enlaces al capítulo 14")
        if concordance_html.count("15-transcripcion.html#") != 100:
            errors.append("La concordancia HTML pierde enlaces al capítulo 15")
        if concordance_html.count("16-edicion-modernizada.html#") != 110:
            errors.append("La concordancia HTML pierde enlaces al capítulo 16")
        for marker in (
            "Portada",
            "Reverso de la portada",
            "Comparecencia",
            "Ratificación",
            "Firmas",
            "Hoja enfrentada posterior",
        ):
            if marker not in concordance_html:
                errors.append(f"La concordancia HTML pierde la unidad {marker}")

        matrix_html = rendered_apparatus["matriz-evidencia.qmd"]
        matrix_anchors = re.findall(
            r'<section id="evidencia-([a-z]+-\d{3})"', matrix_html
        )
        if len(matrix_anchors) != 112 or len(set(matrix_anchors)) != 112:
            errors.append("La matriz HTML no conserva 112 identificadores únicos")
        for level in ("D", "C", "I", "E", "L"):
            if f"<code>{level}</code>" not in matrix_html:
                errors.append(f"La matriz HTML no muestra el nivel {level}")
        for marker in ("Admitida", "Condicionada", "Sorribas", "habitantes fiscales"):
            if marker not in matrix_html:
                errors.append(f"La matriz HTML pierde {marker}")
        for name, html in rendered_apparatus.items():
            if "header-section-number" in html:
                errors.append(f"El aparato 4D se ha numerado indebidamente: {name}")
            if ".qmd#" in html:
                errors.append(f"El HTML 4D conserva un enlace QMD roto: {name}")
            if "/home/" in html or "project/" in html:
                errors.append(f"El HTML 4D expone una ruta fuente local: {name}")
    rendered_indexes = {
        name: path.read_text(encoding="utf-8")
        for name, path in RENDERED_INDEX_HTML.items()
        if path.is_file()
    }
    missing_indexes = [
        str(path) for name, path in RENDERED_INDEX_HTML.items() if name not in rendered_indexes
    ]
    if missing_indexes:
        errors.append("Faltan HTML de índices 5A: " + ", ".join(missing_indexes))
    else:
        expected_counts = (21, 9, 7, 12, 12, 27, 15, 40, 21)
        for (name, html), title, expected_count in zip(
            rendered_indexes.items(), INDEX_TITLES.values(), expected_counts, strict=True
        ):
            if title not in html:
                errors.append(f"El HTML 5A no contiene su título: {name}")
            anchors = re.findall(
                r'<div id="(indice-[a-z0-9-]+)" class="index-entry', html
            )
            entry_anchors = [anchor for anchor in anchors if "-letra-" not in anchor]
            if len(entry_anchors) != expected_count or len(set(entry_anchors)) != expected_count:
                errors.append(
                    f"El HTML 5A {name} no conserva {expected_count} entradas únicas"
                )
            if ".qmd#" in html:
                errors.append(f"El HTML 5A conserva un enlace QMD roto: {name}")
            if "/home/" in html or "project/" in html:
                errors.append(f"El HTML 5A expone una ruta fuente local: {name}")
            if "Páginas:" in html:
                errors.append(f"El HTML 5A muestra el localizador exclusivo de PDF: {name}")
            if "Localizadores:" not in html:
                errors.append(f"El HTML 5A no muestra localizadores enlazados: {name}")
        response_html = rendered_indexes[INDEX_OUTPUT_NAMES[7]]
        if response_html.count("16-edicion-modernizada.html#respuesta-") != 40:
            errors.append("El índice 8 HTML no enlaza exactamente las 40 respuestas")
    errors.extend(_rendered_link_and_id_errors(PUBLICATION_ROOT / "_book"))
    if not RENDERED_PDF.is_file():
        errors.append(f"Falta el PDF renderizado: {RENDERED_PDF}")
    else:
        try:
            pdf_lines = _pdf_text_lines(RENDERED_PDF)
        except (OSError, RuntimeError, subprocess.CalledProcessError) as exc:
            errors.append(f"No se pudo extraer texto del PDF: {exc}")
        else:
            errors.extend(_index_pdf_locator_errors(RENDERED_PDF))
            if not _contains_ordered_lines(pdf_lines, canonical):
                errors.append(
                    "El PDF no conserva en orden las 18 líneas paleográficas exactas"
                )
            normalized_pdf = re.sub(r"\s+", " ", " ".join(pdf_lines))
            normalized_canonical = re.sub(r"\s+", " ", " ".join(canonical))
            if normalized_canonical not in normalized_pdf:
                errors.append("El PDF no conserva equivalencia textual con la transcripción")
            if "El Catastro de Ensenada" not in normalized_pdf:
                errors.append("El PDF no contiene el capítulo 1")
            if (
                "Las Respuestas Generales y el interrogatorio de cuarenta preguntas"
                not in normalized_pdf
            ):
                errors.append("El PDF no contiene el capítulo 2")
            if "El expediente de Sorribos y Santibáñez de Ordás" not in normalized_pdf:
                errors.append("El PDF no contiene el capítulo 3")
            if "Del manuscrito al volumen actual" not in normalized_pdf:
                errors.append("El PDF no contiene el capítulo 4")
            if "Un lugar de señorío en el Concejo de Ordás" not in normalized_pdf:
                errors.append("El PDF no contiene el capítulo 5")
            if "Vecinos, hogares, viviendas y trabajo" not in normalized_pdf:
                errors.append("El PDF no contiene el capítulo 6")
            if "Tierra, sistema agrario y medidas" not in normalized_pdf:
                errors.append("El PDF no contiene el capítulo 7")
            if "Ganadería, montes y aprovechamientos comunales" not in normalized_pdf:
                errors.append("El PDF no contiene el capítulo 8")
            if "Facsímil íntegro del expediente" not in normalized_pdf:
                errors.append("El PDF no contiene el capítulo 14")
            if "Transcripción y aparato crítico de las 35 unidades" not in normalized_pdf:
                errors.append("El PDF no contiene el capítulo 15")
            if "El Catastro en español actual" not in normalized_pdf:
                errors.append("El PDF no contiene el capítulo 16")
            for title in (
                "Glosario histórico",
                "Cuadros cuantitativos",
                "Concordancia general",
                "Matriz de evidencia D/C/I/E/L",
            ):
                if title not in normalized_pdf:
                    errors.append(f"El PDF no contiene el aparato 4D: {title}")
            for title in INDEX_TITLES.values():
                if title not in normalized_pdf:
                    errors.append(f"El PDF no contiene el índice 5A: {title}")
            if "??" in normalized_pdf:
                errors.append("El PDF contiene localizadores o referencias sin resolver")
            for heading in (
                "Entradas",
                "3.2. Territorio, medidas y usos agrarios",
                "Vista por unidad",
                "3.1. Localidad, jurisdicción y producción del expediente",
            ):
                if re.search(
                    rf"\b16\.\d+(?:\.\d+)?\s+{re.escape(heading)}",
                    normalized_pdf,
                ):
                    errors.append(
                        f"El PDF numera indebidamente un encabezado 4D: {heading}"
                    )
            for marker in ("avitadores", "venta", "dado a renta"):
                if marker not in normalized_pdf:
                    errors.append(
                        f"El PDF no conserva la cautela modernizada: {marker}"
                    )
            for unit in canonical_units:
                lines = tuple(unit.sections[PALEOGRAPHIC_SECTION].splitlines())
                if not _contains_ordered_lines(pdf_lines, lines):
                    errors.append(
                        "El PDF no conserva la lineación paleográfica de "
                        f"{unit.spec.unit_id}"
                    )
    return errors


def _parse_document(text: str, source: str | Path) -> tuple[dict, str]:
    """Split an initial YAML front matter block from reader-facing Markdown."""

    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\r\n") != "---":
        raise ValueError(f"{source} no comienza con front matter delimitado por ---")

    closing = next(
        (
            index
            for index, line in enumerate(lines[1:], start=1)
            if line.rstrip("\r\n") == "---"
        ),
        None,
    )
    if closing is None:
        raise ValueError(f"Front matter sin delimitador de cierre en {source}")

    metadata_text = "".join(lines[1:closing])
    try:
        data = yaml.safe_load(metadata_text)
    except yaml.YAMLError as exc:
        raise ValueError(f"Front matter YAML inválido en {source}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"Front matter inválido en {source}: se esperaba un mapa YAML")
    return data, "".join(lines[closing + 1:])


def _front_matter_and_body(path: Path) -> tuple[dict, str]:
    return _parse_document(path.read_text(encoding="utf-8"), path)


def _front_matter(path: Path) -> dict:
    return _front_matter_and_body(path)[0]


def _normalized_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).casefold().strip()


def _markdown_section(body: str, anchor: str) -> str:
    heading = re.search(
        rf"^##\s+.+?\s+\{{#{re.escape(anchor)}\}}\s*$",
        body,
        re.MULTILINE,
    )
    if heading is None:
        return ""
    following = re.search(r"^##\s+", body[heading.end():], re.MULTILINE)
    end = heading.end() + following.start() if following else len(body)
    return body[heading.end():end]


def _plain_text(text: str) -> str:
    """Normalize the small Markdown subset used by controlled relations."""

    return _normalized_text(text.translate(str.maketrans("", "", "*_`")))


_RELATION_CLAUSE_BOUNDARY = re.compile(r"(?<=[.!?])\s+|;\s*")
_CONTRASTIVE_CLAUSE_BOUNDARY = re.compile(r",\s+(?=mientras\b)")


def _relation_clauses(paragraph: str) -> tuple[str, ...]:
    """Split only the controlled relation boundaries used by this validator."""

    clauses: list[str] = []
    for proposition in _RELATION_CLAUSE_BOUNDARY.split(paragraph):
        for clause in _CONTRASTIVE_CLAUSE_BOUNDARY.split(proposition):
            clause = clause.strip()
            if clause.startswith("mientras ") and "," in clause:
                contrast, remainder = clause.split(",", maxsplit=1)
                clauses.extend((contrast.strip(), remainder.strip()))
            elif clause:
                clauses.append(clause)
    return tuple(clause for clause in clauses if clause)


def _controlled_paragraphs(markdown: str) -> tuple[tuple[str, tuple[str, ...]], ...]:
    """Return normalized paragraphs and their locally bounded relation clauses.

    Full stops, semicolons, and controlled contrastive coordination delimit
    clauses. Colons deliberately do not: they can introduce the entity list
    governed by a preceding predicate.
    """

    paragraphs: list[tuple[str, tuple[str, ...]]] = []
    for block in re.split(r"\n\s*\n", markdown):
        paragraph = _plain_text(block)
        if not paragraph:
            continue
        propositions = _relation_clauses(paragraph)
        paragraphs.append((paragraph, propositions))
    return tuple(paragraphs)


def _matches_any(text: str, patterns: tuple[str, ...]) -> bool:
    return any(re.search(pattern, text) for pattern in patterns)


def _matches_groups(text: str, *groups: tuple[str, ...]) -> bool:
    return all(_matches_any(text, group) for group in groups)


_POLARITY_MARKER = re.compile(
    r"\b(?P<marker>no|ni|nunca|tampoco|sin|ningun[ao]s?|ninguna|sí)\b"
)


def _predicate_is_negated(text: str, start: int) -> bool:
    """Return the polarity attached locally to a controlled predicate."""

    prefix = text[max(0, start - 100):start]
    boundary = max(prefix.rfind(","), prefix.rfind(":"))
    if boundary >= 0:
        prefix = prefix[boundary + 1:]
    markers = tuple(_POLARITY_MARKER.finditer(prefix))
    if not markers:
        return False
    return markers[-1].group("marker") != "sí"


def _predicate_polarities(
    proposition: str,
    affirmative_patterns: tuple[str, ...],
    negative_patterns: tuple[str, ...] = (),
    ignored_spans: tuple[tuple[int, int], ...] = (),
) -> set[bool]:
    """Return True for affirmed and False for negated relation predicates."""

    polarities: set[bool] = set()
    for pattern in affirmative_patterns:
        for match in re.finditer(pattern, proposition):
            if any(
                start <= match.start() and match.end() <= end
                for start, end in ignored_spans
            ):
                continue
            polarities.add(not _predicate_is_negated(proposition, match.start()))
    for pattern in negative_patterns:
        for match in re.finditer(pattern, proposition):
            if any(
                start <= match.start() and match.end() <= end
                for start, end in ignored_spans
            ):
                continue
            polarities.add(_predicate_is_negated(proposition, match.start()))
    return polarities


_PHONETIC_ENTITY = (
    r"\b(?:secuencia|evolución|reconstrucción)\s+fonética\b",
)
_PHONETIC_COMPLETENESS = (
    r"\bcompleta\b",
    r"\bcompletamente\s+documentad\w*\b",
    r"\bpor\s+completo\b",
)
_PHONETIC_ATTRIBUTIVE_ENTITY = re.compile(
    r"\b(?:secuencia|evolución|reconstrucción)\s+fonética\s+"
    r"completamente\s+documentad\w*\b"
)
_PHONETIC_PREDICATES = (
    r"\bexist(?:e|en|ía|ió|irá|iría)\b",
    r"\bhay\b",
    r"\bdispon(?:e|en|er|ible)\b",
    r"\bproporciona\b",
    r"\b(?:documentada?|documentadas?|documentados?)\b",
    r"\breconstru(?:ir|ye|ida?|idas?|idos?)\b",
    r"\bpermite\b",
    r"\bautoriza\b",
    r"\bdemuestra\b",
    r"\bprueba\b",
    r"\bacredita\b",
)
_ECONOMIC_ENTITY = (r"\bcontinuidad\s+económica\b",)
_ECONOMIC_PREDICATES = (
    r"\bhay\b",
    r"\bdemuestr\w*\b",
    r"\bdemostrad\w*\b",
    r"\bprueb\w*\b",
    r"\bprobad\w*\b",
    r"\bacredit\w*\b",
    r"\bconfirm\w*\b",
    r"\bgarantiz\w*\b",
    r"\bestablec\w*\b",
    r"\bestablecid\w*\b",
    r"\bpermit\w*\b",
    r"\bautoriz\w*\b",
    r"\bafirm\w*\b",
)


def _phonetic_polarities(proposition: str) -> set[bool]:
    if not _matches_groups(
        proposition,
        _PHONETIC_ENTITY,
        _PHONETIC_COMPLETENESS,
    ):
        return set()
    attributive_entity_spans = tuple(
        match.span()
        for match in _PHONETIC_ATTRIBUTIVE_ENTITY.finditer(proposition)
    )
    polarities = _predicate_polarities(
        proposition,
        _PHONETIC_PREDICATES,
        ignored_spans=attributive_entity_spans,
    )
    entity = r"(?:secuencia|evolución|reconstrucción)[^.]{0,40}fonética[^.]{0,20}completa"
    if re.search(rf"\b(?:sin|ningun[ao]s?)\b[^.;:]{{0,60}}{entity}", proposition):
        polarities.add(False)
    if re.search(rf"\b(?:ausencia|falta)\s+de\b[^.;:]{{0,60}}{entity}", proposition):
        polarities.add(False)
    return polarities


def _economic_polarities(proposition: str) -> set[bool]:
    if not _matches_any(proposition, _ECONOMIC_ENTITY):
        return set()
    polarities = _predicate_polarities(proposition, _ECONOMIC_PREDICATES)
    if re.search(
        r"\b(?:sin|ningun[ao]s?)\b[^.;:]{0,70}continuidad\s+económica",
        proposition,
    ):
        polarities.add(False)
    return polarities


def _validate_chapter_three_body(body: str) -> list[str]:
    """Validate the two historical limits in their toponymic context."""

    errors: list[str] = []
    section = _markdown_section(body, "expediente-toponimo")
    if not section:
        return ["C3_TOPONYM_SECTION: falta la sección histórica del topónimo"]
    paragraphs = _controlled_paragraphs(section)

    phonetic_reversal = any(
        True in _phonetic_polarities(proposition)
        for _, propositions in paragraphs
        for proposition in propositions
    )
    if phonetic_reversal:
        errors.append(
            "C3_PHONETIC_REVERSAL: el capítulo afirma una secuencia fonética completa"
        )

    phonetic_limit = any(
        _matches_groups(
            paragraph,
            (r"\bsorrios\s+actual\b", r"\bactual(?:mente)?\b[^.]{0,80}\bsorrios\b"),
            (r"\bidentific\w*\b[^.]{0,100}\bsegur\w*\b",
             r"\bsegur\w*\b[^.]{0,100}\bidentific\w*\b"),
        )
        and any(
            False in _phonetic_polarities(proposition)
            for proposition in propositions
        )
        for paragraph, propositions in paragraphs
    )
    if not phonetic_limit:
        errors.append(
            "C3_PHONETIC_LIMIT: falta relacionar la identificación segura de Sorrios "
            "con el límite de la secuencia fonética"
        )

    economic_reversal = any(
        "1267" in paragraph
        and "1752" in paragraph
        and any(
            True in _economic_polarities(proposition)
            for proposition in propositions
        )
        for paragraph, propositions in paragraphs
    )
    if economic_reversal:
        errors.append(
            "C3_ECONOMIC_CONTINUITY_REVERSAL: el capítulo afirma continuidad "
            "económica demostrada entre 1267 y 1752"
        )

    economic_limit = any(
        "1267" in paragraph
        and "1752" in paragraph
        and re.search(r"\b(?:patrimonial|compraventa|venta|transmisión)\b", paragraph)
        and any(
            False in _economic_polarities(proposition)
            for proposition in propositions
        )
        for paragraph, propositions in paragraphs
    )
    if not economic_limit:
        errors.append(
            "C3_PATRIMONIAL_LIMIT: falta relacionar la evidencia patrimonial de "
            "1267 con el límite de continuidad económica hasta 1752"
        )
    return errors


_FACSIMILE = (r"\bfacsímil\b",)
_TRANSCRIPTION = (r"\btranscripción(?:\s+paleográfica)?\b",)
_CRITICAL_EDITION = (r"\bedición\s+crítica\b",)
_MODERNIZED_EDITION = (r"\bedición\s+modernizada\b", r"\bmodernizada\b")
_INTERPRETATION = (r"\binterpretación\b",)
_CONTENT_PATH = (r"publication/content/",)
_GENERATED_PATH = (r"publication/generated/",)
_DERIVATIVES = (r"\bderivad\w*\b", r"\bsalidas?\b", r"\bproductos?\b")
_EQUALITY_PREDICATES = (
    r"\bigual(?:es)?\b",
    r"\bequivalent(?:e|es)\b",
    r"\bindistinguible(?:s)?\b",
    r"\bintercambiable(?:s)?\b",
    r"\blo\s+mismo\b",
    r"\bla\s+misma\s+capa\b",
)


def _affirms_function(
    propositions: tuple[str, ...],
    entity: tuple[str, ...],
    predicates: tuple[str, ...],
    objects: tuple[str, ...],
) -> bool:
    return any(
        _matches_groups(proposition, entity, objects)
        and True in _predicate_polarities(proposition, predicates)
        for proposition in propositions
    )


def _layer_equality_polarities(proposition: str) -> set[bool]:
    if not _matches_groups(
        proposition,
        _FACSIMILE,
        _TRANSCRIPTION,
        _CRITICAL_EDITION,
        _MODERNIZED_EDITION,
    ):
        return set()
    return _predicate_polarities(proposition, _EQUALITY_PREDICATES)


def _pair_equality_polarities(
    proposition: str,
    first: tuple[str, ...],
    second: tuple[str, ...],
) -> set[bool]:
    if not _matches_groups(proposition, first, second):
        return set()
    return _predicate_polarities(proposition, _EQUALITY_PREDICATES)


_STORAGE_PREDICATES = (
    r"\b(?:es|son)\b",
    r"\bcontien\w*\b",
    r"\balberg\w*\b",
    r"\bguard\w*\b",
    r"\balmacen\w*\b",
    r"\bresid\w*\b",
    r"\bedit\w*\b",
    r"\bredact\w*\b",
    r"\bmanten\w*\b",
)
_OUTPUT_PREDICATES = _STORAGE_PREDICATES + (
    r"\bregener\w*\b",
    r"\breproduc\w*\b",
    r"\breconstru\w*\b",
)
_MANUAL_EDITORIAL = (
    r"\b(?:texto|contenido|fuente|redacción)\s+editorial\b",
    r"\bcapítulos?\b",
)
_HUMAN_MAINTENANCE = (
    r"\bmanual(?:mente)?\b",
    r"\bhuman\w*\b",
    r"\bpor\s+personas\b",
)
_REGENERABLE_OUTPUT = (
    r"\b(?:derivad\w*|salidas?|productos?|vistas?|directorio)\b",
)
_REGENERATION = (
    r"\b(?:regener\w*|reproduc\w*|reconstru\w*|determinista\w*|automátic\w*)\b",
)
_AUTHORITY = (
    r"\bautoridad(?:es)?(?:\s+canónica)?(?:\s+propia)?\b",
    r"\bnuevas?\s+autoridades\b",
)
_AUTHORITY_POSSESSION = (
    r"\b(?:tien\w*|adquier\w*|correspond\w*|pose\w*|goz\w*)\b",
    r"\b(?:es|son)\b(?=[^,;:.]{0,50}\bautoridad)",
    r"\bse\s+conviert\w*\b",
)
_AUTHORITY_ABSENCE = (r"\bcarec\w*\b",)


def _content_function_is_affirmed(proposition: str) -> bool:
    return (
        _matches_groups(
            proposition,
            _CONTENT_PATH,
            _MANUAL_EDITORIAL,
            _HUMAN_MAINTENANCE,
        )
        and True in _predicate_polarities(proposition, _STORAGE_PREDICATES)
    )


def _generated_function_is_affirmed(proposition: str) -> bool:
    return (
        _matches_groups(
            proposition,
            _GENERATED_PATH,
            _REGENERABLE_OUTPUT,
            _REGENERATION,
        )
        and True in _predicate_polarities(proposition, _OUTPUT_PREDICATES)
    )


def _directory_function_is_reversed(proposition: str) -> bool:
    content_is_generated = (
        _matches_groups(
            proposition,
            _CONTENT_PATH,
            _REGENERABLE_OUTPUT,
            _REGENERATION,
        )
        and True in _predicate_polarities(proposition, _OUTPUT_PREDICATES)
    )
    generated_is_manual = (
        _matches_groups(
            proposition,
            _GENERATED_PATH,
            _MANUAL_EDITORIAL,
            _HUMAN_MAINTENANCE,
        )
        and True in _predicate_polarities(proposition, _STORAGE_PREDICATES)
    )
    return content_is_generated or generated_is_manual


def _authority_polarities(proposition: str) -> set[bool]:
    if not _matches_any(proposition, _AUTHORITY):
        return set()
    if not (
        _matches_any(proposition, _GENERATED_PATH)
        or _matches_any(proposition, _DERIVATIVES)
    ):
        return set()
    return _predicate_polarities(
        proposition,
        _AUTHORITY_POSSESSION,
        _AUTHORITY_ABSENCE,
    )


def _validate_chapter_four_body(body: str) -> list[str]:
    """Validate stable distinctions between publication and documentary layers."""

    errors: list[str] = []
    paragraphs = _controlled_paragraphs(body)
    propositions = tuple(
        proposition
        for _, paragraph_propositions in paragraphs
        for proposition in paragraph_propositions
    )
    access = _markdown_section(body, "volumen-cuatro-accesos")
    evidence = _markdown_section(body, "volumen-evidencia")
    generated = _markdown_section(body, "volumen-content-generated")

    if any(True in _layer_equality_polarities(item) for item in propositions):
        errors.append(
            "C4_LAYERS_CONTRADICTED: las cuatro representaciones se presentan "
            "como iguales o indistinguibles"
        )

    access_propositions = tuple(
        proposition
        for _, paragraph_propositions in _controlled_paragraphs(access)
        for proposition in paragraph_propositions
    )
    distinct_relation = any(
        _matches_groups(
            item,
            (r"\b(?:capas?|representaciones?)\b",),
            (r"\b(?:funciones?|cometidos?)\b",),
        )
        and True in _predicate_polarities(
            item,
            (r"\bdistint\w*\b", r"\bdiferent\w*\b", r"\bseparad\w*\b"),
        )
        for item in propositions
    )
    distinct_layers = bool(access) and distinct_relation and all(
        (
            _affirms_function(
                access_propositions,
                _FACSIMILE,
                (r"\breproduc\w*\b", r"\bmuestr\w*\b", r"\bconserv\w*\b"),
                (r"\bimagen\b", r"\bmaterialidad\b", r"\baspecto\s+material\b"),
            ),
            _affirms_function(
                access_propositions,
                _TRANSCRIPTION,
                (r"\bfij\w*\b", r"\bconserv\w*\b", r"\brepresent\w*\b", r"\bregistr\w*\b"),
                (r"\btexto\b", r"\blínea\b", r"\brenglones?\b", r"\bgrafías?\b"),
            ),
            _affirms_function(
                access_propositions,
                _CRITICAL_EDITION,
                (r"\breún\w*\b", r"\bdocument\w*\b", r"\bexplic\w*\b", r"\bregistr\w*\b", r"\bcontien\w*\b"),
                (r"\bsecciones?\b", r"\baparato\b", r"\bdecisiones?\b", r"\bcriterios?\b", r"\bvariantes?\b"),
            ),
            _affirms_function(
                access_propositions,
                _MODERNIZED_EDITION,
                (r"\bofrec\w*\b", r"\bactualiz\w*\b", r"\bfacilit\w*\b", r"\bpresent\w*\b"),
                (r"\blectura\b", r"\bespañol\s+actual\b", r"\bcontemporánea\b"),
            ),
        )
    )
    if not distinct_layers:
        errors.append(
            "C4_LAYER_FUNCTIONS: falta distinguir las funciones propias de facsímil, "
            "transcripción, edición crítica y modernizada"
        )

    if any(
        True in _pair_equality_polarities(item, _TRANSCRIPTION, _INTERPRETATION)
        for item in propositions
    ):
        errors.append(
            "C4_TRANSCRIPTION_INTERPRETATION_REVERSED: transcripción e "
            "interpretación se presentan como la misma operación"
        )

    evidence_paragraphs = _controlled_paragraphs(evidence)
    separates_interpretation = any(
        _affirms_function(
            paragraph_propositions,
            _TRANSCRIPTION,
            (r"\bestablec\w*\b", r"\bfij\w*\b", r"\bregistr\w*\b", r"\bconsign\w*\b"),
            (r"\bfuente\b", r"\btexto\b", r"\btenor\b", r"\bqué\s+dice\b"),
        )
        and _affirms_function(
            paragraph_propositions,
            _INTERPRETATION,
            (r"\bpregunt\w*\b", r"\bexplic\w*\b", r"\binterpret\w*\b", r"\bsignific\w*\b", r"\bofrec\w*\b"),
            (r"\bhistóric\w*\b", r"\bsignific\w*\b", r"\blectura\b", r"\bqué\s+puede\b"),
        )
        for _, paragraph_propositions in evidence_paragraphs
    )
    if not separates_interpretation:
        errors.append(
            "C4_TRANSCRIPTION_INTERPRETATION: falta separar lo que fija la "
            "transcripción de lo que interpreta el estudio"
        )

    if any(
        True in _pair_equality_polarities(item, _CONTENT_PATH, _GENERATED_PATH)
        for item in propositions
    ):
        errors.append(
            "C4_CONTENT_GENERATED_SAME: content/ y generated/ se presentan como "
            "la misma capa"
        )

    if any(_directory_function_is_reversed(item) for item in propositions):
        errors.append(
            "C4_DIRECTORY_FUNCTIONS_REVERSED: se invierten las funciones de "
            "publication/content/ y publication/generated/"
        )

    authority_polarities = {
        polarity
        for item in propositions
        for polarity in _authority_polarities(item)
    }
    if True in authority_polarities:
        errors.append(
            "C4_GENERATED_AUTHORITY: los derivados reciben autoridad canónica propia"
        )

    generated_propositions = tuple(
        proposition
        for _, paragraph_propositions in _controlled_paragraphs(generated)
        for proposition in paragraph_propositions
    )
    separates_directories = (
        any(_content_function_is_affirmed(item) for item in generated_propositions)
        and any(
            _generated_function_is_affirmed(item)
            for item in generated_propositions
        )
    )
    generated_lacks_authority = any(
        False in _authority_polarities(item)
        for item in generated_propositions
    )
    if not separates_directories or not generated_lacks_authority:
        errors.append(
            "C4_CONTENT_GENERATED_FUNCTIONS: falta separar el contenido editorial "
            "humano de los derivados regenerables sin autoridad propia"
        )
    return errors


def _validate_chapter_five_body(body: str) -> list[str]:
    """Validate the bounded institutional and territorial claims of chapter 5."""

    errors: list[str] = []
    sections = {
        anchor: _normalized_text(_markdown_section(body, anchor))
        for anchor in CHAPTER_FIVE_ANCHORS
    }
    for anchor, section in sections.items():
        if not section:
            errors.append(f"C5_SECTION_{anchor.upper().replace('-', '_')}: falta la sección")

    required_by_section = {
        "lugar-actores": (
            "lugar de sorribos y santibáñez de ordás",
            "común del lugar",
            "vecinos",
            "concejo de ordás",
            "municipio posterior de santa maría de ordás",
            "tampoco son intercambiables",
        ),
        "lugar-concejo-municipio": (
            "1768",
            "1789",
            "cinco lugares",
            "1836",
            "1848",
            "no puede proyectarse sobre 1752",
            "no son equivalentes automáticos",
        ),
        "lugar-senorio-conde": (
            "el manuscrito",
            "conde de luna",
            "no proporciona el nombre personal",
            "francisco alfonso pimentel como xv conde de luna",
            "identificación nominal procede de documentación externa",
        ),
        "lugar-derechos": (
            "establecimiento del suelo",
            "alcabalas",
            "633 reales anuales",
            "pozo de pesca",
            "nueve reales",
            "coexiste",
            "no consta el título jurídico concreto",
            "conceptos diferenciados",
        ),
        "lugar-termino": (
            "una legua y media y 787 varas",
            "2.500 varas de oriente a poniente",
            "2.708 varas de norte a sur",
            "tapia",
            "rioseco",
            "santa maría",
            "villapodambre",
            "croquis o figura marginal",
            "no constituyen cartografía métrica moderna",
            "no se convierten en superficie moderna",
            "ni permiten reconstruir un polígono geográfico exacto",
        ),
        "lugar-sintesis": (
            "lugar",
            "comunidad",
            "jurisdicción",
            "señorío",
            "término",
            "no una única realidad",
            "capítulo 6",
            "capítulo 7",
            "capítulo 9",
            "capítulo 10",
            "capítulo 11",
        ),
    }
    for anchor, phrases in required_by_section.items():
        section = sections[anchor]
        absent = [phrase for phrase in phrases if phrase not in section]
        if absent:
            errors.append(
                f"C5_CONTENT_{anchor.upper().replace('-', '_')}: faltan relaciones "
                + ", ".join(absent)
            )

    controlled_blocks = _controlled_paragraphs(body)
    paragraphs = tuple(paragraph for paragraph, _ in controlled_blocks)
    propositions = tuple(
        proposition
        for _, block_propositions in controlled_blocks
        for proposition in block_propositions
    )
    prohibited = {
        "C5_COMMON_COUNCIL_EQUIVALENCE": (
            r"\bel común del lugar era el concejo de ordás\b",
        ),
        "C5_COUNCIL_MUNICIPALITY_EQUIVALENCE": (
            r"\bel concejo de ordás de 1752 era el municipio actual\b",
        ),
        "C5_MANUSCRIPT_IDENTIFIES_COUNT": (
            r"\bel manuscrito identifica a francisco alfonso pimentel\b",
        ),
        "C5_NO_LORDLY_RIGHTS": (
            r"\bel lugar no pagaba ningún derecho al conde\b",
        ),
        "C5_R22_ERASES_RIGHTS": (
            r"\bla respuesta 22 demuestra la ausencia de derechos señoriales\b",
            r"\bla respuesta 22 demuestra que no exist(?:en|ían) derechos señoriales\b",
        ),
        "C5_EXACT_POLYGON_RECONSTRUCTION": (
            r"\bel croquis permite reconstruir un polígono geográfico exacto\b",
        ),
    }
    for code, patterns in prohibited.items():
        if any(
            re.search(pattern, paragraph)
            for paragraph in paragraphs
            for pattern in patterns
        ):
            errors.append(f"{code}: formulación no autorizada en el capítulo 5")

    known_legal_title = re.compile(
        r"\b(?:se\s+conoce|conocemos)\s+el\s+título\s+jurídico\s+de\s+las\s+"
        r"alcabalas\s+y\s+del\s+pozo\b"
    )
    if any(
        not _predicate_is_negated(proposition, match.start())
        for proposition in propositions
        for match in known_legal_title.finditer(proposition)
    ):
        errors.append(
            "C5_KNOWN_LEGAL_TITLE: formulación no autorizada en el capítulo 5"
        )

    modern_conversion = re.compile(
        r"\b\d+(?:[.,]\d+)?\s*(?:hectáreas?|ha\b|km(?:²|2)|kilómetros? cuadrados?)"
    )
    if any(modern_conversion.search(paragraph) for paragraph in paragraphs):
        errors.append(
            "C5_MODERN_TERRITORIAL_CONVERSION: conversión territorial no autorizada"
        )
    return errors


def _validate_chapter_six_body(body: str) -> list[str]:
    """Validate the demographic, domestic and labour limits of chapter 6."""

    errors: list[str] = []
    sections = {
        anchor: _plain_text(_markdown_section(body, anchor))
        for anchor in CHAPTER_SIX_ANCHORS
    }
    for anchor, section in sections.items():
        if not section:
            errors.append(f"C6_SECTION_{anchor.upper().replace('-', '_')}: falta la sección")

    required_by_section = {
        "vecinos-recuento": (
            "vecinos | 18",
            "medios vecinos | 8",
            "«avitadores» | 26",
            "residentes no considerados vecinos | 8",
            "18 + 8 = 26",
            "ocho medios vecinos no equivalen a cuatro vecinos",
            "función fiscal de la vecindad",
        ),
        "avitadores-poblacion": (
            "forma documental de la respuesta 21",
            "no se obtiene una población total añadiendo 26 y 8",
            "unidad de observación no consta como equivalente",
            "vecinos × k",
            "137 habitantes a santibáñez de sorribos en 1768",
            "por su fecha y unidad distintas",
        ),
        "personas-hogares": (
            "persona es un individuo",
            "cabezas de casa y familias",
            "14 son hijos de familia",
            "tres son criados sirvientes",
            "indicios de convivencia y trabajo doméstico",
            "no una magnitud contada directamente",
        ),
        "casas-viviendas": (
            "casas habitables | 40",
            "casas arruinadas | 2",
            "pajares separados | 15",
            "no equivalen a 40 hogares",
            "no permite estimar cuántas personas ocupaban cada casa",
            "vivienda ocupada",
        ),
        "trabajo-categorias": (
            "jornaleros | 18",
            "14 hijos de familia + 3 criados sirvientes + 1 dedicado solo a ese ejercicio = 18",
            "labradores | 24",
            "herrero | 1",
            "no se suman para formar una población activa",
            "oficio, ocupación y condición laboral tampoco son equivalentes",
            "cinco pobres de solemnidad",
            "un cura párroco y dos capellanes",
        ),
        "trabajo-utilidades": (
            "2,5 reales por día trabajado",
            "3 reales",
            "1,5 reales",
            "medio real diario",
            "una regulación diaria no es un ingreso anual",
            "no reconstruir la renta anual de un hogar",
        ),
        "estructura-limites": (
            "trabajo familiar, servicio doméstico, jornal, labranza",
            "no consta el total de individuos",
            "no un total de unidades domésticas",
            "dato sin suma total",
            "no rentas anuales personales o familiares",
            "no son equivalentes",
        ),
    }
    for anchor, phrases in required_by_section.items():
        section = sections[anchor]
        absent = [phrase for phrase in phrases if phrase not in section]
        if absent:
            errors.append(
                f"C6_CONTENT_{anchor.upper().replace('-', '_')}: faltan relaciones "
                + ", ".join(absent)
            )

    controlled = _controlled_paragraphs(body)
    propositions = tuple(
        proposition
        for _, paragraph_propositions in controlled
        for proposition in paragraph_propositions
    )
    prohibited_predicates = {
        "C6_AVITADORES_ARE_INHABITANTS": (
            r"\b(?:los\s+)?26\s+avitadores\s+(?:son|equivalen\s+a)\s+26\s+habitantes\b",
        ),
        "C6_RESIDENT_SUM_IS_POPULATION": (
            r"\b(?:sumar|sumando|añadir|añadiendo)\b[^.;]{0,80}\b(?:26\s+y\s+8|ocho\s+residentes)\b[^.;]{0,80}\b(?:da|daría|produce|produciría|forma|formaría)\b[^.;]{0,40}\b(?:la\s+)?población\s+total\b",
            r"\b(?:la\s+)?población\s+total\s+(?:era|es|sería)\s+(?:de\s+)?34\s+habitantes\b",
        ),
        "C6_HALF_NEIGHBOUR_WEIGHTED": (
            r"\bocho\s+medios\s+vecinos\s+(?:equivalen|equivalían|son)\s+a?\s*cuatro\s+vecinos\b",
        ),
        "C6_HOUSES_ARE_HOUSEHOLDS": (
            r"\b(?:las\s+)?(?:40|cuarenta)\s+casas\s+habitables\s+(?:representan|equivalen\s+a|son)\s+(?:40|cuarenta)\s+hogares\b",
        ),
        "C6_LABOUR_CATEGORIES_ADDED": (
            r"\b(?:los\s+)?18\s+jornaleros\s+y\s+(?:los\s+)?24\s+labradores\s+(?:forman|suman|equivalen\s+a)\b[^.;]{0,50}\b(?:42|cuarenta\s+y\s+dos)\b",
        ),
        "C6_HALF_NEIGHBOUR_IS_HALF_PERSON": (
            r"\b(?:el\s+)?medio\s+vecino\s+(?:era|es|equivale\s+a)\s+(?:media\s+persona|medio\s+habitante)\b",
        ),
        "C6_DAILY_RATE_IS_ANNUAL_INCOME": (
            r"\b(?:los\s+)?2,5\s+reales\s+diarios\s+(?:permiten|permitirían)\s+calcular\b[^.;]{0,50}\b(?:el\s+)?ingreso\s+anual\b",
        ),
        "C6_SMITH_NOT_FARMER": (
            r"\bel\s+herrero\s+no\s+(?:ejercía|trabajaba)\s+como\s+labrador\b",
        ),
        "C6_POVERTY_RATE": (
            r"\b(?:los\s+)?cinco\s+pobres\s+de\s+solemnidad\s+(?:permiten|permitirían)\s+calcular\b[^.;]{0,40}\b(?:la\s+)?tasa\s+de\s+pobreza\b",
        ),
    }
    for code, patterns in prohibited_predicates.items():
        if any(
            not _predicate_is_negated(proposition, match.start())
            for proposition in propositions
            for pattern in patterns
            for match in re.finditer(pattern, proposition)
        ):
            errors.append(f"{code}: formulación no autorizada en el capítulo 6")

    normalized = _plain_text(body)
    if re.search(
        r"\bvecinos\s*[×x]\s*\d+(?:[.,]\d+)?\s*=\s*\d+(?:[.,]\d+)?\s+habitantes\b",
        normalized,
    ):
        errors.append(
            "C6_GENERIC_POPULATION_FACTOR: conversión no autorizada de vecinos en habitantes"
        )
    return errors


def _validate_chapter_seven_body(body: str) -> list[str]:
    """Validate agrarian calculations, metrology, limits, and chapter borders."""

    errors: list[str] = []
    sections = {
        anchor: _plain_text(_markdown_section(body, anchor))
        for anchor in CHAPTER_SEVEN_ANCHORS
    }
    for anchor, section in sections.items():
        if not section:
            errors.append(f"C7_SECTION_{anchor.upper().replace('-', '_')}: falta la sección")

    required_by_section = {
        "tierra-clases": (
            "trece clases de tierras y aprovechamientos",
            "ferrañales centenales de secano",
            "linares de regadío",
            "linares de secano",
            "centenales de secano",
            "prados entreparedes",
            "matorrales",
            "eras o sitios",
            "montes de robles altos y bajos",
            "soto de negrillos, alisos y fresnos",
            "funciones, no títulos de propiedad",
            "capítulo 8",
            "árboles frutales",
        ),
        "tierra-calidades": (
            "no aplica una escala uniforme",
            "prado cercado de secano",
            "solo segunda, llamada única",
            "montes",
            "no aparecen en el desglose cuantitativo",
            "sotos",
            "no armonizar ambas respuestas",
        ),
        "tierra-medidas": (
            "no se usa una medida superficial cierta reducible a varas castellanas",
            "el mismo quartal de tierra ocupa más o menos terreno según su calidad",
            "4 quartales = 1 fanega",
            "4 montones = 1 carro",
            "ninguna relación declarada con la medida principal, el quartal o la fanega",
            "no permiten encadenar",
        ),
        "tierra-cabida": (
            "3.823 medidas y un celemín",
            "3.811,5 medidas principales y siete celemines",
            "no se restan ni se reconcilian",
            "666 de primera calidad",
            "1.398 de segunda",
            "1.747,5 de tercera",
            "3.811,5 como denominador",
        ),
        "tierra-centeno": (
            "centeno, cebada, lino, linaza y yerba",
            "34 medidas de ferrañales + 149,5",
            "2.953,5 medidas de cabida cultivada comparable",
            "2.750,5 medidas centenales",
            "2.750,5 ÷ 2.953,5 × 100",
            "93,13 %",
            "2.750,5 ÷ 3.811,5 × 100",
            "72,16 %",
            "preguntas distintas",
        ),
        "tierra-ciclos": (
            "linares de regadío alternan lino y cebada",
            "linares de secano, lino y centeno",
            "producen un año y descansan otro",
            "no describen una rotación agronómica completa",
            "2.750,5 ÷ 2 + 34 + 149,5 + 19,5",
            "1.578,25 unidades activas medias",
            "1.375,25",
            "87,14 %",
            "índice analítico",
            "no superficie efectivamente sembrada",
        ),
        "tierra-rendimientos": (
            "un quartal de tierra",
            "no registra lo que se cosechó en un año concreto",
            "ferrañal / forraje",
            "linar de regadío / linaza y lino",
            "linar de secano / centeno",
            "centenal / centeno",
            "no se suman linaza en quartales y lino en libras",
            "cuatro montones que componen un carro",
        ),
        "tierra-produccion-limites": (
            "producto agrario total",
            "multiplicar cada cabida por una tasa seleccionada",
            "valores regulados por quinquenio",
            "40 fejes de lino × 4 libras = 160 libras",
            "no representa la producción total de lino",
            "no permite deducir autoconsumo",
            "suficiencia alimentaria",
            "productividad por trabajador",
            "capítulo 12",
        ),
        "tierra-sintesis": (
            "comparte unidad, base y denominador",
            "no pueden agregarse celemín y medida principal",
            "carga y quartal",
            "valor monetario y producto físico",
            "capítulo 8",
            "al 9",
            "al 10",
            "al 11",
            "al 12",
            "al 13",
        ),
    }
    for anchor, phrases in required_by_section.items():
        section = sections[anchor]
        absent = [phrase for phrase in phrases if phrase not in section]
        if absent:
            errors.append(
                f"C7_CONTENT_{anchor.upper().replace('-', '_')}: faltan relaciones "
                + ", ".join(absent)
            )

    controlled = _controlled_paragraphs(body)
    propositions = tuple(
        proposition
        for _, paragraph_propositions in controlled
        for proposition in paragraph_propositions
    )
    prohibited_predicates = {
        "C7_TOTALS_RECONCILED": (
            r"\b(?:3\.823[^.;]{0,80}3\.811,5|3\.811,5[^.;]{0,80}3\.823)\b[^.;]{0,80}\b(?:coinciden|equivalen|son\s+iguales|se\s+reconcilian)\b",
        ),
        "C7_MOUNTS_BY_RESIDUAL": (
            r"\b(?:la\s+)?(?:cabida|cantidad)\s+de\s+los\s+montes\b[^.;]{0,80}\b(?:se\s+obtiene|se\s+calcula|equivale|es)\b[^.;]{0,40}\b(?:por\s+residuo|diferencia)\b",
        ),
        "C7_FALSE_CELEMIN_EQUIVALENCE": (
            r"\b(?:un|1)\s+celem[ií]n\s+(?:equivale|corresponde|es\s+igual)\s+a\b[^.;]{0,40}\b(?:quartal|fanega|medida)\b",
        ),
        "C7_PERCENTAGES_SAME_DENOMINATOR": (
            r"\b93,13\s*%[^.;]{0,80}72,16\s*%[^.;]{0,80}\b(?:mismo|igual)\s+denominador\b",
            r"\b(?:mismo|igual)\s+denominador[^.;]{0,80}93,13\s*%[^.;]{0,80}72,16\s*%\b",
        ),
        "C7_EXACT_ROTATION": (
            r"\b(?:se\s+documenta|documenta|demuestra|consta)\b[^.;]{0,60}\brotaci[oó]n\s+(?:trienal|cuatrienal|completa|precisa)\b",
        ),
        "C7_OBSERVED_ACTIVE_SURFACE": (
            r"\b1\.578,25\b[^.;]{0,80}\b(?:superficie\s+efectivamente\s+sembrada|cosecha\s+observada)\b",
        ),
        "C7_TOTAL_PRODUCTION": (
            r"\b(?:el\s+)?producto\s+agrario\s+total\b[^.;]{0,50}\b(?:fue|era|ascend[ií]a|se\s+calcula|puede\s+calcularse)\b",
            r"\b(?:la\s+)?producci[oó]n\s+total\s+de\s+lino\b[^.;]{0,50}\b(?:fue|era|ascend[ií]a|equival(?:e|[ií]a|dr[ií]a))\b",
        ),
        "C7_INCOMPATIBLE_SUM": (
            r"\b(?:sumar|sumando|agregar|agregando)\b[^.;]{0,70}\bcargas?\b[^.;]{0,40}\b(?:fanegas?|quartales?)\b",
            r"\b(?:sumar|sumando|agregar|agregando)\b[^.;]{0,70}\bquartales?\b[^.;]{0,40}\blibras?\b",
        ),
        "C7_AUTOCONSUMPTION": (
            r"\b(?:demuestra|prueba|confirma|garantiza|documenta)\b[^.;]{0,80}\b(?:autoconsumo|suficiencia\s+alimentaria)\b",
        ),
        "C7_PRODUCTIVITY_INFERENCE": (
            r"\b(?:permite|permiten|puede|pueden)\b[^.;]{0,60}\bcalcular\b[^.;]{0,60}\bproductividad\s+por\s+(?:trabajador|hogar)\b",
        ),
    }
    for code, patterns in prohibited_predicates.items():
        if any(
            not _predicate_is_negated(proposition, match.start())
            for proposition in propositions
            for pattern in patterns
            for match in re.finditer(pattern, proposition)
        ):
            errors.append(f"{code}: formulación no autorizada en el capítulo 7")

    normalized = _plain_text(body)
    if re.search(
        r"\b\d+(?:[.,]\d+)?\s*(?:hectáreas?|ha\b|m(?:²|2)\b|km(?:²|2)\b|litros?|kilogramos?|kg\b)",
        normalized,
    ):
        errors.append("C7_MODERN_CONVERSION: conversión moderna no autorizada")
    for marker in ("ocho ruedas", "18 pies de abejas", "633 reales", "hacienda concejil detallada"):
        if marker in normalized:
            errors.append(
                "C7_CHAPTER_BOUNDARY: desarrollo sustantivo reservado a los capítulos 8–13"
            )
            break
    return errors


def _validate_chapter_eight_body(body: str) -> list[str]:
    """Validate livestock semantics, common use, resources, and chapter borders."""

    errors: list[str] = []
    sections = {
        anchor: _plain_text(_markdown_section(body, anchor))
        for anchor in CHAPTER_EIGHT_ANCHORS
    }
    for anchor, section in sections.items():
        if not section:
            errors.append(f"C8_SECTION_{anchor.upper().replace('-', '_')}: falta la sección")

    required_by_section = {
        "ganado-alcance": (
            "ganado vacuno, lanar y de cerda",
            "yeguas y crías mulares",
            "no constituyen un recuento de existencias",
            "efectivos ganaderos documentados son indeterminados",
            "stock ganadero",
            "reparto de cabezas",
        ),
        "ganado-valores": (
            "flujos anuales moderados",
            "valores de una cría",
            "prestación en centeno",
            "no es número de crías observado",
            "no es precio de venta ni cantidad de ganado",
            "no los multiplica por cabezas inexistentes",
        ),
        "ganado-funciones": (
            "función de labor solo se atribuye expresamente a bueyes y vacas",
            "no había casa destinada al esquileo",
            "no demuestra que todas las viviendas acogieran esquileo",
            "dado arenta",
            "cinco quartales de centeno por buey y cuatro por vaca",
            "no constan titular, receptor, plazo",
        ),
        "pastos-recursos": (
            "ferrañales de forraje",
            "el otoño se pasta en común",
            "no se declara uso común",
            "cuatro montones componen un carro",
            "no como base para calcular alimentación disponible",
        ),
        "montes-arbolado": (
            "montes de robles altos y bajos",
            "soto de negrillos, alisos y fresnos",
            "leña se destina a quemar",
            "reparar puentes y puertas del río",
            "no proporciona volumen cortado",
            "no se resuelve por residuo",
            "capítulo 9",
        ),
        "uso-comun": (
            "acreditan disfrute colectivo",
            "no acreditan por sí solas titularidad",
            "derecho de aprovechamiento",
            "administración",
            "no una conclusión automática sobre el dominio",
            "capítulo 11",
        ),
        "articulacion-agraria": (
            "los ferrañales producen forraje",
            "bueyes y vacas aparecen valorados para la labranza",
            "no componen un balance de entradas y salidas",
            "no mide cuánta yerba consumía cada especie",
            "no se publica un nuevo cálculo editorial",
            "conservan la definición y los denominadores del capítulo 7",
        ),
        "ganado-limites": (
            "stock ganadero total o por especie",
            "distribución de animales entre titulares, vecinos, hogares o viviendas",
            "producción total o neta",
            "suficiencia de pastos, forraje, leña o madera",
            "presión, conservación, equilibrio o sostenibilidad",
            "titularidad y las reglas de reparto o administración",
        ),
        "ganado-sintesis": (
            "calla el número de cabezas",
            "el otoño de un tipo concreto de prado se pastaba en común",
            "no prueba de su suficiencia",
            "no estima producción",
            "el capítulo 9",
            "los capítulos 10–12",
            "el 13",
        ),
    }
    for anchor, phrases in required_by_section.items():
        section = sections[anchor]
        absent = [phrase for phrase in phrases if phrase not in section]
        if absent:
            errors.append(
                f"C8_CONTENT_{anchor.upper().replace('-', '_')}: faltan relaciones "
                + ", ".join(absent)
            )

    normalized = _plain_text(body)
    propositions = tuple(
        proposition
        for _, paragraph_propositions in _controlled_paragraphs(body)
        for proposition in paragraph_propositions
    )

    if re.search(r"\b(?:bienes comunales|propiedad comunal|monte comunal)\b", normalized):
        errors.append(
            "C8_COMMON_USE_IS_PROPERTY: el uso común recibe un título jurídico no probado"
        )
    common_property_patterns = (
        r"\b(?:demuestr\w*|prueb\w*|implic\w*|equival\w*|acredit\w*|confirm\w*)\b[^.;]{0,90}\b(?:propiedad|titularidad|dominio)\s+comunal\b",
        r"\b(?:pertenec\w*|era\w*\s+propiedad)\b[^.;]{0,70}\bcom[uú]n\b",
    )
    if any(
        not _predicate_is_negated(proposition, match.start())
        for proposition in propositions
        for pattern in common_property_patterns
        for match in re.finditer(pattern, proposition)
    ):
        errors.append(
            "C8_COMMON_USE_IS_PROPERTY: el uso común recibe un título jurídico no probado"
        )

    prohibited_predicates = {
        "C8_HEADCOUNT_IS_OUTPUT": (
            r"\b\d+(?:[.,]\d+)?\s+(?:vacas?|ovejas?|yeguas?|cerdas?|bueyes?|carneros?|corderos?)\b[^.;]{0,90}\b(?:produc(?:en|ían)|dan|daban|generan)\b[^.;]{0,80}\b(?:reales|libras|cr[ií]as?|lana|leche)\b",
        ),
        "C8_LIVESTOCK_ASSIGNED_HOUSEHOLDS": (
            r"\bcada\s+(?:hogar|vecino|vivienda)\b[^.;]{0,60}\b(?:ten[ií]a|pose[ií]a|recib[ií]a)\b[^.;]{0,50}\b(?:ganado|vaca|oveja|buey|yegua|cerda)\b",
            r"\b(?:una|un)\s+(?:vaca|oveja|buey|yegua|cerda)\s+por\s+(?:hogar|vecino|vivienda)\b",
            r"\b(?:ganado|cabezas?|animales?)\b[^.;]{0,70}\b(?:repartid\w*|distribuid\w*|asignad\w*)\b[^.;]{0,60}\bhogares?\b",
        ),
        "C8_UNSUPPORTED_PRODUCTION": (
            r"\bproducci[oó]n\s+(?:ganadera|anual\s+de\s+(?:lana|leche|carne|cr[ií]as?))\s+total\b[^.;]{0,60}\b(?:fue|era|ascend[ií]a|se\s+calcula|puede\s+calcularse)\b",
            r"\b(?:multiplicar|multiplicando)\b[^.;]{0,80}\b(?:valoraciones?|productos?)\s+por\s+(?:las\s+)?cabezas\b[^.;]{0,60}\b(?:total|producci[oó]n|renta)\b",
        ),
        "C8_UNSUPPORTED_SPECIES_FUNCTION": (
            r"\b(?:ovejas?|cerdas?|yeguas?)\b[^.;]{0,60}\b(?:araban|tiraban\s+del\s+arado|transportaban\s+cargas)\b",
            r"\b(?:cerdas?|bueyes?|yeguas?)\b[^.;]{0,60}\bproduc[ií]an\s+lana\b",
            r"\b(?:ovejas?|carneros?)\b[^.;]{0,60}\bproduc[ií]an\s+leche\s+para\s+el\s+consumo\b",
        ),
        "C8_PASTURE_SUFFICIENCY": (
            r"\b(?:pastos?|prados?|forraje)\b[^.;]{0,80}\b(?:bastaban|eran\s+suficientes|garantizaban|cubr[ií]an)\b[^.;]{0,70}\b(?:ganado|necesidades|alimentaci[oó]n)\b",
            r"\b(?:alimentaci[oó]n|mantenimiento)\s+del\s+ganado\b[^.;]{0,70}\b(?:estaba\s+asegurad\w*|quedaba\s+garantizad\w*)\b",
        ),
        "C8_ECOLOGICAL_BALANCE": (
            r"\b(?:exist[ií]a|hab[ií]a|demuestr\w*|prueb\w*)\b[^.;]{0,80}\b(?:equilibrio|desequilibrio)\s+ecol[oó]gico\b",
            r"\b(?:sistema|aprovechamiento)\b[^.;]{0,60}\b(?:era|fue)\s+(?:sostenible|insostenible)\b",
            r"\b(?:montes?|pastos?)\b[^.;]{0,70}\b(?:estaban|fueron)\s+sobreexplotad\w*\b",
        ),
        "C8_GUARANTEED_WOOD_FUEL": (
            r"\b(?:montes?|soto)\b[^.;]{0,90}\b(?:garantizaban|aseguraban|proporcionaban\s+siempre)\b[^.;]{0,60}\b(?:madera|leña|combustible)\b",
            r"\b(?:madera|leña|combustible)\b[^.;]{0,70}\b(?:era\s+inagotable|estaba\s+garantizad\w*|era\s+suficiente)\b",
        ),
        "C8_INTERPRETATION_AS_DATA": (
            r"\bes\s+un\s+dato\s+(?:expl[ií]cito\s+)?del\s+manuscrito\s+que\b[^.;]{0,100}\b(?:econom[ií]a\s+(?:era\s+)?mixta|funciones\s+complementarias|soporte\s+material)\b",
            r"\bel\s+manuscrito\s+declara\b[^.;]{0,100}\b(?:econom[ií]a\s+mixta|complementariedad\s+agraria)\b",
        ),
        "C8_EVIDENCE_LIMITS_ERASED": (
            r"\b(?:censo|stock)\s+ganadero\s+(?:completo|exacto)\b[^.;]{0,60}\b(?:consta|se\s+conoce|puede\s+reconstruirse)\b",
            r"\b(?:se\s+conoce|consta)\b[^.;]{0,80}\b(?:titular|propietario)\s+de\s+cada\s+(?:animal|cabeza)\b",
            r"\bla\s+fuente\s+permite\b[^.;]{0,90}\b(?:reparto\s+completo|producci[oó]n\s+total|presi[oó]n\s+sobre\s+los\s+recursos)\b",
        ),
        "C8_CHAPTER_SEVEN_CONTRADICTION": (
            r"\b(?:cabida|superficie)\s+de\s+los\s+montes\b(?![^.;]{0,40}\bno\b)[^.;]{0,70}\b(?:se\s+calcula|se\s+obtiene|resulta)\b[^.;]{0,40}\b(?:por\s+residuo|diferencia)\b",
            r"\btodos\s+los\s+prados\b[^.;]{0,50}\b(?:eran|son|se\s+usaban)\b[^.;]{0,30}\bcom[uú]n\b",
            r"\b(?:un|1)\s+carro\s+de\s+yerba\b[^.;]{0,40}\b(?:equivale|equival[ií]a)\b[^.;]{0,20}\b(?:tres|cinco|\d+)\s+montones\b",
        ),
    }
    for code, patterns in prohibited_predicates.items():
        if any(
            not _predicate_is_negated(proposition, match.start())
            for proposition in propositions
            for pattern in patterns
            for match in re.finditer(pattern, proposition)
        ):
            errors.append(f"{code}: formulación no autorizada en el capítulo 8")

    boundary_patterns = (
        r"\bocho\s+ruedas\b",
        r"\b633\s+reales\b",
        r"\btaberna\b[^.;]{0,50}\bvecera\b",
        r"\b30\s+cargas\s+de\s+centeno\b[^.;]{0,50}\bdiezmos\b",
        r"\b[ií]ndice\s+(?:global\s+)?de\s+vulnerabilidad\b",
    )
    if any(re.search(pattern, normalized) for pattern in boundary_patterns):
        errors.append(
            "C8_CHAPTER_BOUNDARY: desarrollo sustantivo reservado a los capítulos 9–13"
        )
    return errors


def _validate_chapter_nine_body(body: str) -> list[str]:
    """Validate hydraulic resources without inventing operation or output."""

    errors: list[str] = []
    sections = {
        anchor: _plain_text(_markdown_section(body, anchor))
        for anchor in CHAPTER_NINE_ANCHORS
    }
    for anchor, section in sections.items():
        if not section:
            errors.append(f"C9_SECTION_{anchor.upper().replace('-', '_')}: falta la sección")

    required_by_section = {
        "rio-espacio-productivo": (
            "cuatro casas de molinos harineros",
            "un pozo de pesca",
            "no localiza los artefactos dentro del cauce",
            "no mide su caudal",
            "no implica que todas las unidades tuvieran idéntico régimen",
        ),
        "molinos-recuento": (
            CANONICAL_FORMULA,
            "3 + 2 + 2 + 1 = 8",
            "no incluye una rueda supuesta para el venturero",
            "algunos meses de invierno",
            "casa es el edificio",
        ),
        "molinos-titulares": (
            "don manuel antonio, cura",
            "manuel garcía y consortes",
            "otro don manuel",
            "propietario, partícipe, molinero, operador y usuario son funciones distintas",
            "no identifica al molinero",
        ),
        "molinos-utilidades": (
            "tres ruedas valoradas en dos cargas y cinco en cuatro",
            "utilidades declaradas",
            "no mide grano molido",
            "no se agregan a las 26 cargas",
            "equivalencia segura entre carga y quartal",
        ),
        "molinos-estacionalidad": (
            "esas ruedas muelen solo la mitad del año",
            "algunos meses de invierno",
            "no enumera los meses",
            "no demuestra que cada avenida paralizara todos los molinos",
            "no asigna a sorribos caudales, meses, rendimientos ni capacidad",
        ),
        "molinos-cereal": (
            "carácter harinero de los molinos",
            "utilidades en centeno",
            "capítulo 7",
            "no permite, sin embargo, convertir cabidas y rendimientos regulados en volumen molido",
            "excedente comercializable",
        ),
        "recursos-colmenas": (
            "registra 18 «pies de abejas»",
            "7 + 6 + 3 + 1 + 1 = 18",
            "a dos reales de utilidad anual regulada por pie",
            "los dos mayores titulares reúnen",
            "no es una medida de riqueza general",
        ),
        "recursos-pesca": (
            "pozo de pesca en el río",
            "propio del conde de luna",
            "arrendado entonces",
            "nueve reales de utilidad",
            "no se conoce el nombre del arrendatario",
            "capítulo 10",
        ),
        "recursos-limites": (
            "existencia",
            "titularidad o participación",
            "explotación",
            "usuarios",
            "utilidad",
            "producción y capacidad",
            "autosuficiencia, excedente, rentabilidad comparada",
        ),
        "recursos-sintesis": (
            "26 cargas entre las ocho ruedas",
            "cuatro quartales para el venturero",
            "36 reales para los pies de abejas",
            "nueve reales para el pozo",
            "no forman entre sí una producción agregada",
            "capítulos 11–13",
        ),
    }
    for anchor, phrases in required_by_section.items():
        section = sections[anchor]
        absent = [phrase for phrase in phrases if phrase.casefold() not in section]
        if absent:
            errors.append(
                f"C9_CONTENT_{anchor.upper().replace('-', '_')}: faltan relaciones "
                + ", ".join(absent)
            )

    propositions = tuple(
        proposition
        for _, paragraph_propositions in _controlled_paragraphs(body)
        for proposition in paragraph_propositions
    )
    prohibited_predicates = {
        "C9_EXISTENCE_IS_PRODUCTION": (
            r"\b(?:existencia|presencia)\s+de\s+(?:los\s+)?molinos?\b[^.;]{0,90}\b(?:demuestr\w*|prueb\w*|implic\w*|acredit\w*)\b[^.;]{0,70}\bproducci[oó]n\s+(?:conocida|anual|efectiva)\b",
        ),
        "C9_UTILITY_IS_PRODUCTION": (
            r"\b(?:utilidad|renta)\b(?![^.;]{0,70}\bno\b)[^.;]{0,70}\b(?:equivale|corresponde|es\s+igual)\b[^.;]{0,70}\bproducci[oó]n\b",
            r"\b26\s+cargas\b[^.;]{0,70}\b(?:eran|representan|miden)\b[^.;]{0,50}\b(?:grano\s+molido|producci[oó]n)\b",
        ),
        "C9_FISCAL_IS_INCOME": (
            r"\b(?:valor|estimaci[oó]n)\s+fiscal\b[^.;]{0,70}\b(?:era|equivale|representa)\b[^.;]{0,50}\bingreso\s+real\b",
        ),
        "C9_OWNER_IS_OPERATOR": (
            r"\b(?:propietario|titular)\b[^.;]{0,60}\b(?:era|actuaba\s+como|explotaba)\b[^.;]{0,40}\b(?:explotador|operador)\b",
        ),
        "C9_OWNER_IS_MILLER": (
            r"\b(?:propietario|titular)\b[^.;]{0,70}\b(?:era|trabajaba\s+como)\b[^.;]{0,30}\bmolinero\b",
            r"\b(?:todos\s+los\s+)?titulares\b[^.;]{0,50}\bmol[ií]an\b",
        ),
        "C9_UNDOCUMENTED_USERS": (
            r"\b(?:todos\s+los\s+vecinos|cada\s+hogar|la\s+poblaci[oó]n\s+entera)\b[^.;]{0,60}\b(?:us\w*|utiliz\w*|acud\w*|se\s+abastec\w*)\b[^.;]{0,40}\bmolinos?\b",
            r"\b(?:se\s+conoce|consta)\b[^.;]{0,60}\bn[uú]mero\s+de\s+usuarios\b",
        ),
        "C9_ANNUAL_OPERATION": (
            r"\b(?:molinos?|ruedas?)\b[^.;]{0,60}\b(?:funcionaban|mol[ií]an|operaban)\b[^.;]{0,50}\b(?:todo\s+el\s+a[nñ]o|durante\s+todo\s+el\s+a[nñ]o|sin\s+interrupci[oó]n)\b",
        ),
        "C9_WATER_SUFFICIENCY": (
            r"\b(?:r[ií]o|agua|caudal)\b[^.;]{0,80}\b(?:era\s+suficiente|bastaba|garantizaba|era\s+permanente|no\s+ten[ií]a\s+estiaje)\b",
        ),
        "C9_MILLING_CAPACITY": (
            r"\b(?:capacidad\s+de\s+molienda|capacidad\s+t[eé]cnica)\b[^.;]{0,70}\b(?:era|fue|ascend[ií]a|se\s+calcula|puede\s+calcularse)\b",
            r"\b(?:ocho\s+ruedas|26\s+cargas)\b(?![^.;]{0,80}\bno\b)[^.;]{0,80}\bpermit(?:e|en)\s+calcular\b[^.;]{0,50}\bcapacidad\b",
        ),
        "C9_COMPLETE_SUPPLY": (
            r"\b(?:molinos?|ruedas?)\b[^.;]{0,80}\b(?:abastec[ií]an|cubr[ií]an|garantizaban)\b[^.;]{0,60}\b(?:toda\s+la\s+localidad|toda\s+la\s+poblaci[oó]n|necesidades\s+locales)\b",
        ),
        "C9_CEREAL_SELF_SUFFICIENCY": (
            r"\b(?:centeno|sistema\s+cerealista|cultivos?)\b(?![^.;]{0,90}\bno\b)[^.;]{0,90}\b(?:demuestr\w*|prueb\w*|garantiz\w*|asegur\w*)\b[^.;]{0,60}\bautosuficiencia\s+cerealista\b",
        ),
        "C9_COMMERCIAL_SURPLUS": (
            r"\b(?:molinos?|molienda|26\s+cargas|centeno)\b(?![^.;]{0,90}\bno\b)[^.;]{0,90}\b(?:demuestr\w*|prueb\w*|gener\w*|confirma\w*)\b[^.;]{0,60}\bexcedente\s+comercial\b",
        ),
        "C9_INTERPRETATION_AS_DATA": (
            r"\b(?:es\s+un\s+dato\s+(?:expl[ií]cito\s+)?del\s+manuscrito|el\s+manuscrito\s+declara)\b[^.;]{0,100}\b(?:econom[ií]a\s+(?:rural\s+)?(?:era\s+)?mixta|diversificaci[oó]n\s+productiva|sistema\s+integrado)\b",
        ),
        "C9_EVIDENCE_LIMITS_ERASED": (
            r"\b(?:se\s+conoce|consta)\b[^.;]{0,70}\bn[uú]mero\s+(?:exacto\s+)?de\s+ruedas\s+del\s+venturero\b",
            r"\b(?:se\s+conocen|constan)\b[^.;]{0,80}\b(?:producci[oó]n|capacidad|usuarios)\s+(?:exacta|completa|totales?)\b",
        ),
        "C9_PRIOR_CHAPTER_CONTRADICTION": (
            r"\bcenteno\b[^.;]{0,70}\b(?:ocupaba|representaba)\b[^.;]{0,30}\b93,13\s*%[^.;]{0,40}\b(?:cabida\s+total|todas\s+las\s+tierras)\b",
            r"\btodos\s+los\s+prados\b[^.;]{0,50}\b(?:eran|se\s+usaban)\b[^.;]{0,30}\bcom[uú]n\b",
        ),
        "C9_CHAPTER_BOUNDARY": (
            r"\b(?:nueve|9)\s+reales\b[^.;]{0,90}\b(?:demuestr\w*|prueb\w*|permit\w*)\b[^.;]{0,80}\b(?:sistema\s+fiscal|fiscalidad\s+se[nñ]orial|ingresos?\s+del\s+se[nñ]or[ií]o)\b",
            r"\b(?:sistema|econom[ií]a)\b[^.;]{0,60}\b(?:era|fue)\b[^.;]{0,30}\b(?:resiliente|fr[aá]gil|eficiente|integrado)\b",
        ),
    }
    for code, patterns in prohibited_predicates.items():
        if any(
            not _predicate_is_negated(proposition, match.start())
            for proposition in propositions
            for pattern in patterns
            for match in re.finditer(pattern, proposition)
        ):
            errors.append(f"{code}: formulación no autorizada en el capítulo 9")
    return errors


def _validate_chapter_ten_body(body: str) -> list[str]:
    """Validate fiscal relations without merging rights, payers, or measures."""

    errors: list[str] = []
    sections = {
        anchor: _plain_text(_markdown_section(body, anchor))
        for anchor in CHAPTER_TEN_ANCHORS
    }
    for anchor, section in sections.items():
        if not section:
            errors.append(f"C10_SECTION_{anchor.upper().replace('-', '_')}: falta la sección")

    required_by_section = {
        "fiscal-marco-senorial": (
            "marco institucional documentado",
            "beneficiario de las alcabalas",
            "titular del pozo de pesca",
            "no describe un dominio general",
            "compartir perceptor no vuelve idéntica su naturaleza",
        ),
        "fiscal-perceptores-eclesiasticos": (
            "don manuel antonio de vega, cura del lugar",
            "la primicia, a la iglesia local",
            "el voto, a la fábrica del apóstol santiago",
            "perceptor indiferenciado",
            "no hace al cura propietario",
        ),
        "fiscal-diezmos": (
            "30 cargas",
            "2 cargas",
            "5 fanegas",
            "40 fejes de 4 libras cada uno",
            "160 libras",
            "140 reales",
            "no son recibos, cuentas de cobro ni comprobantes de pago efectivo",
        ),
        "fiscal-primicia-voto": (
            "26 quartales de centeno",
            "24 quartales",
            "la respuesta omite el producto",
            "renta eclesiástica de origen medieval",
            "no autoriza a reunirlos en una sola cifra",
        ),
        "fiscal-derechos-senoriales": (
            "los vecinos pagaban por ellas 633 reales cada año",
            "no el título jurídico concreto ni el reparto individual",
            "nueve reales de utilidad",
            "no un impuesto pagado por los vecinos",
            "sumarlos fabricaría una categoría",
        ),
        "fiscal-exenciones": (
            "establecimiento del suelo",
            "tampoco acredita una exención fiscal general",
            "el común no estaba cargado con servicio ordinario ni extraordinario",
            "el sujeto es aquí el común",
            "pertenecen al capítulo 11",
        ),
        "fiscal-sujetos-bases": (
            "sujeto o base documentada",
            "magnitud y periodicidad",
            "pago efectivo no comprobado",
            "título y reparto desconocidos",
            "utilidad de un recurso, no carga vecinal",
        ),
        "fiscal-magnitudes": (
            "no forman un subtotal material",
            "sus bases y naturalezas difieren",
            "no pueden calcularse carga por vecino o por habitante, presión fiscal",
            "renta disponible o desigualdad",
            "capítulo 12",
        ),
        "fiscal-limites": (
            "reparto de cada obligación entre contribuyentes",
            "producto omitido del voto",
            "diferencia entre regulación y cobro",
            "renta anual completa",
            "incidencia distributiva ni vulnerabilidad",
        ),
        "fiscal-sintesis": (
            "cada relación tiene sujeto, base y naturaleza propios",
            "ni el señorío equivale a propiedad universal",
            "cantidades reguladas que no demuestran pagos efectivos",
            "son específicas, no generales",
            "capítulo 11 estudiará la hacienda concejil",
        ),
    }
    for anchor, phrases in required_by_section.items():
        section = sections[anchor]
        absent = [phrase for phrase in phrases if phrase.casefold() not in section]
        if absent:
            errors.append(
                f"C10_CONTENT_{anchor.upper().replace('-', '_')}: faltan relaciones "
                + ", ".join(absent)
            )

    propositions = tuple(
        proposition
        for _, paragraph_propositions in _controlled_paragraphs(body)
        for proposition in paragraph_propositions
    )
    prohibited_predicates = {
        "C10_LORDSHIP_IS_GENERAL_PROPERTY": (
            r"\b(?:significa|implica|equivale)\b[^.;]{0,80}\bel\s+conde\b[^.;]{0,60}\bpropietario\b[^.;]{0,40}\btodas\s+las\s+tierras\b",
        ),
        "C10_COUNT_ALL_TAXES": (
            r"\bpercib[ií]a\b[^.;]{0,40}\btodos\s+los\s+tributos\b",
        ),
        "C10_CHURCH_GENERIC_RECIPIENT": (
            r"\bpercib[ií]a\b[^.;]{0,40}\blos\s+diezmos\b[^.;]{0,40}\bla\s+primicia\b[^.;]{0,40}\bel\s+voto\b",
        ),
        "C10_TITHE_IS_PROPERTY": (
            r"\bconvert[ií]a\b[^.;]{0,50}\bcura\b[^.;]{0,40}\bpropietario\b[^.;]{0,40}\btierras\b",
        ),
        "C10_RENT_IS_TAX": (
            r"\beran\s+un\s+impuesto\b[^.;]{0,60}\bpagado\b[^.;]{0,40}\bvecinos\b",
        ),
        "C10_UTILITY_IS_FISCAL_CHARGE": (
            r"\bconstitu[ií]a\b[^.;]{0,30}\buna\s+carga\s+fiscal\s+vecinal\b",
        ),
        "C10_REGULATION_IS_PAYMENT": (
            r"\bfueron\s+efectivamente\s+pagad[ao]s\b[^.;]{0,50}\bcura\b",
        ),
        "C10_EXEMPTION_GENERALIZED": (
            r"\bestaba\s+exento\b[^.;]{0,40}\btodos\s+los\s+impuestos\b",
        ),
        "C10_INCOMPATIBLE_SUM": (
            r"\bsumando\b[^.;]{0,80}\bcargas\b[^.;]{0,60}\bfanegas\b[^.;]{0,60}\bquartales\b[^.;]{0,60}\blibras\b[^.;]{0,60}\breales\b",
        ),
        "C10_SUBTOTAL_IS_TOTAL": (
            r"\b(?:773|seiscientos\s+setenta\s+y\s+tres)\s+reales\b[^.;]{0,40}\beran\b[^.;]{0,30}\bfiscalidad\s+total\b",
        ),
        "C10_TAX_PRESSURE": (
            r"\bpresi[oó]n\s+fiscal\b[^.;]{0,30}\bera\b[^.;]{0,30}\b\d+(?:[,.]\d+)?\s*%",
        ),
        "C10_PER_CAPITA_CHARGE": (
            r"\bcada\s+(?:vecino|habitante|hogar)\b[^.;]{0,50}\bsoportaba\b[^.;]{0,40}\breales\b",
        ),
        "C10_SPECIE_MONEY_CONVERSION": (
            r"\bcargas\b[^.;]{0,40}\bequival[ií]an\b[^.;]{0,40}\breales\b",
        ),
        "C10_DISPOSABLE_INCOME": (
            r"\brenta\s+disponible\b[^.;]{0,40}\b(?:era|ascend[ií]a)\b[^.;]{0,40}\breales\b",
        ),
        "C10_EVIDENCE_LIMITS_ERASED": (
            r"\bse\s+conoce\b[^.;]{0,60}\bt[ií]tulo\s+jur[ií]dico\s+exacto\b[^.;]{0,40}\balcabalas\b",
        ),
        "C10_CHAPTER_FIVE_CONTRADICTION": (
            r"\brespuesta\s+22\b[^.;]{0,50}\bdemuestra\b[^.;]{0,50}\bno\s+exist[ií]an\s+derechos\s+se[nñ]oriales\b",
        ),
        "C10_CHAPTER_ELEVEN_BOUNDARY": (
            r"\bpresupuesto\s+anual\s+completo\s+del\s+com[uú]n\b[^.;]{0,40}\bera\b[^.;]{0,30}\b233\s+reales\b",
        ),
        "C10_CHAPTER_TWELVE_BOUNDARY": (
            r"\bprueban\b[^.;]{0,60}\beconom[ií]a\b[^.;]{0,30}\bplenamente\s+monetizada\b",
        ),
        "C10_CHAPTER_THIRTEEN_BOUNDARY": (
            r"\bfiscalidad\b[^.;]{0,40}\bhizo\b[^.;]{0,50}\bvulnerable\b[^.;]{0,40}\beconom[ií]a\s+local\b",
        ),
    }
    for code, patterns in prohibited_predicates.items():
        if any(
            not _predicate_is_negated(proposition, match.start())
            for proposition in propositions
            for pattern in patterns
            for match in re.finditer(pattern, proposition)
        ):
            errors.append(f"{code}: formulación no autorizada en el capítulo 10")
    return errors


def _validate_chapter_eleven_body(body: str) -> list[str]:
    """Validate collective finances without inventing ownership or a budget."""

    errors: list[str] = []
    sections = {
        anchor: _plain_text(_markdown_section(body, anchor))
        for anchor in CHAPTER_ELEVEN_ANCHORS
    }
    for anchor, section in sections.items():
        if not section:
            errors.append(f"C11_SECTION_{anchor.upper().replace('-', '_')}: falta la sección")

    required_by_section = {
        "hacienda-sujetos": (
            "el común es el sujeto",
            "los vecinos intervienen mediante repartimiento",
            "marco jurisdiccional declarado",
            "ayuntamiento o municipio moderno",
            "no se reclasifican aquí como ingresos o gastos concejiles",
        ),
        "hacienda-recursos": (
            "el común no tiene propios",
            "no disfruta arbitrio ni renta alguna",
            "no prueban pobreza absoluta",
            "no equivale a «propiedad comunal»",
            "aprovechamiento, no propiedad, administración, renta ni ingreso",
        ),
        "hacienda-partidas": (
            "festividad del corpus",
            "limpieza de las fuentes",
            "hospital de inocentes de valladolid",
            "derecho de mesta en león",
            "200 + 8 + 15 + 10 = 233",
            "otras cantidades cuyo importe no ofrece",
        ),
        "hacienda-repartimiento": (
            "obligaciones del común → repartimiento → vecinos",
            "mecanismo de financiación declarado",
            "no la cuota individual",
            "no significa aquí todos los habitantes ni cada vivienda",
            "no aporta padrones de cobro, recibos ni cuentas",
        ),
        "hacienda-destinos": (
            "receptor de quince reales",
            "no explica el origen jurídico",
            "no permite decidir si el concepto local era tasa, servicio, reparto",
            "comparación tipológica",
            "no autoriza a comparar importes",
        ),
        "hacienda-ausencias": (
            "no tiene cargo alguno de justicia",
            "no está cargado de servicio ordinario ni extraordinario",
            "no anulan los gastos de la respuesta 25",
            "no había hospital local ni convento",
            "institución receptora exterior",
        ),
        "hacienda-servicios": (
            "funcionaba por vecera entre los vecinos",
            "no producía utilidad al común ni a particular",
            "no la propiedad del local",
            "no extiende el turno a otras actividades",
            "no basta para definir un sistema general de servicios públicos",
        ),
        "hacienda-infraestructuras": (
            "ocho reales para limpiar las fuentes",
            "existencia, mantenimiento, financiación, prestación y cobertura",
            "no identifican aquí un pagador, administrador o gasto concejil",
            "no se incorporan al subtotal",
            "supuesto patrimonio del concejo",
        ),
        "hacienda-presupuesto-limites": (
            "no ofrece un universo exhaustivo de entradas y salidas",
            "otras cantidades sin importe",
            "no puede calcularse, por tanto, un total de ingresos, un total de gastos",
            "no se agregan a valores patrimoniales",
            "se reserva para el capítulo 12",
            "eficiente, frágil, insolvente o resiliente",
        ),
        "hacienda-sintesis": (
            "carecer de propios, arbitrios y renta",
            "subtotal conocido, no una cuenta completa",
            "prestación rotatoria sin utilidad declarada",
            "no se convierten en propiedad o patrimonio concejil",
            "sin proyectar un municipio moderno",
        ),
    }
    for anchor, phrases in required_by_section.items():
        section = sections[anchor]
        absent = [phrase for phrase in phrases if phrase.casefold() not in section]
        if absent:
            errors.append(
                f"C11_CONTENT_{anchor.upper().replace('-', '_')}: faltan relaciones "
                + ", ".join(absent)
            )

    propositions = tuple(
        proposition
        for _, paragraph_propositions in _controlled_paragraphs(body)
        for proposition in paragraph_propositions
    )
    prohibited_predicates = {
        "C11_CONCEJO_IS_MODERN_TOWN_HALL": (
            r"\bera\b[^.;]{0,60}\bel\s+ayuntamiento\s+moderno\b",
            r"\bequival[ií]a\b[^.;]{0,60}\bmunicipio\s+moderno\b",
        ),
        "C11_COMMON_USE_IS_MUNICIPAL_PROPERTY": (
            r"\bconvert[ií]a\b[^.;]{0,80}\b(?:montes?|recursos?|espacios?)\b[^.;]{0,60}\bpropiedad\s+municipal\b",
        ),
        "C11_ADMINISTRATION_IS_PROPERTY": (
            r"\bdemostraba\b[^.;]{0,80}\bconcejo\b[^.;]{0,40}\b(?:era\s+)?propietario\b",
        ),
        "C11_REGULATED_RENT_IS_COLLECTION": (
            r"\bera\b[^.;]{0,40}\bingreso\s+efectivamente\s+cobrado\b",
        ),
        "C11_UTILITY_IS_CASH_INCOME": (
            r"\bera\b[^.;]{0,40}\bingreso\s+efectivo\b[^.;]{0,40}\bcom[uú]n\b",
        ),
        "C11_OBLIGATION_IS_REALIZED_EXPENSE": (
            r"\bfue\b[^.;]{0,50}\bgasto\s+efectivamente\s+realizado\b",
        ),
        "C11_INFRASTRUCTURE_IS_PERMANENT_SERVICE": (
            r"\bdemuestr[ae]\b[^.;]{0,80}\bservicio\s+permanente\b",
        ),
        "C11_UNIVERSAL_COVERAGE": (
            r"\bdaba\b[^.;]{0,30}\bcobertura\s+universal\b[^.;]{0,50}\b(?:habitantes|vecinos|poblaci[oó]n)\b",
        ),
        "C11_INCOME_PROPERTY_SUM": (
            r"\bsumando\b[^.;]{0,60}\bingresos\b[^.;]{0,60}\bvalores\s+patrimoniales\b",
        ),
        "C11_INCOMPATIBLE_EXPENSE_SUM": (
            r"\bpueden\s+sumarse\b[^.;]{0,80}\bgastos\b[^.;]{0,70}\b(?:periodos|naturalezas)\s+incompatibles\b",
        ),
        "C11_SUBTOTAL_IS_TOTAL_INCOME": (
            r"\beran\b[^.;]{0,40}\bingresos\s+totales\b",
        ),
        "C11_SUBTOTAL_IS_TOTAL_EXPENSE": (
            r"\beran\b[^.;]{0,40}\bgastos\s+totales\b",
        ),
        "C11_UNSUPPORTED_BALANCE": (
            r"\btuvo\b[^.;]{0,30}\b(?:super[aá]vit|d[eé]ficit)\b",
        ),
        "C11_COMPLETE_BUDGET": (
            r"\bformaban\b[^.;]{0,50}\bpresupuesto\s+concejil\s+completo\b",
        ),
        "C11_FISCAL_RECLASSIFICATION": (
            r"\beran\b[^.;]{0,40}\bgasto\s+concejil\b",
        ),
        "C11_COMMON_RESOURCE_IS_CONCEJO_ASSET": (
            r"\beran\b[^.;]{0,40}\bpatrimonio\s+concejil\b",
        ),
        "C11_EVIDENCE_LIMITS_ERASED": (
            r"\bse\s+conoce\b[^.;]{0,80}\borigen\s+jur[ií]dico\b[^.;]{0,80}\bhospital\b",
            r"\bse\s+conoce\b[^.;]{0,80}\bnaturaleza\s+precisa\b[^.;]{0,80}\bmesta\b",
        ),
        "C11_CHAPTER_TWELVE_BOUNDARY": (
            r"\bprueban\b[^.;]{0,70}\beconom[ií]a\b[^.;]{0,30}\bplenamente\s+monetizada\b",
        ),
        "C11_CHAPTER_THIRTEEN_BOUNDARY": (
            r"\bera\b[^.;]{0,40}\b(?:eficiente|fr[aá]gil|resiliente)\b",
        ),
    }
    for code, patterns in prohibited_predicates.items():
        if any(
            not _predicate_is_negated(proposition, match.start())
            for proposition in propositions
            for pattern in patterns
            for match in re.finditer(pattern, proposition)
        ):
            errors.append(f"{code}: formulación no autorizada en el capítulo 11")
    return errors


def _validate_chapter_twelve_body(body: str) -> list[str]:
    """Validate money and work without manufacturing a market economy."""

    errors: list[str] = []
    sections = {
        anchor: _plain_text(_markdown_section(body, anchor))
        for anchor in CHAPTER_TWELVE_ANCHORS
    }
    for anchor, section in sections.items():
        if not section:
            errors.append(f"C12_SECTION_{anchor.upper().replace('-', '_')}: falta la sección")

    required_by_section = {
        "dinero-formas": (
            "precio o valor ordinario",
            "valor o producto regulado",
            "pago declarado",
            "dinero, especie y servicio coexisten",
            "no demuestra por sí sola una economía plenamente monetizada",
        ),
        "dinero-precios-valores": (
            "2 reales y 25 maravedís",
            "1 real y 6 maravedís",
            "valoraciones catastrales, no registros de compraventa",
            "no declara la equivalencia entre real y maravedí",
            "no demuestra que esa cabeza existiera en un censo",
        ),
        "dinero-naturalezas": (
            "18 \\times 2 = 36",
            "nueve reales del pozo de pesca",
            "633 reales de alcabalas",
            "pago, obligación y regulación siguen siendo categorías diferentes",
            "no se suman a esos importes los valores de animales",
        ),
        "dinero-minimo-institucional": (
            "633 + 233 + 140 = 1.006",
            "mínimo institucional explícito, no cuenta total",
            "no es presión fiscal total",
            "omite partidas comunes no cuantificadas",
            "deja fuera prestaciones en especie",
        ),
        "oficios-categorias": (
            "18 jornaleros",
            "24 labradores",
            "herrero que pasa la mayor parte del año como labrador",
            "no forman una clasificación profesional moderna",
            "no se suman 18 jornaleros, 24 labradores y un herrero",
        ),
        "oficios-jornales": (
            "2,5 reales por día trabajado",
            "comida, valorada en 1,5 reales",
            "medio real diario por el oficio",
            "no puede multiplicarse el jornal por 365",
            "no es ingreso anual, salario anual, renta familiar",
        ),
        "oficios-servicios-ausencias": (
            "funcionaba por turno entre vecinos",
            "las respuestas 31, 32 y 34 niegan",
            "no prueban ausencia de todo intercambio",
            "su conexión es administrativa y documental",
            "no un flujo económico del lugar",
        ),
        "conexiones-exteriores": (
            "15 + 10 = 25",
            "25 \\div 233 \\times 100 = 10{,}73",
            "25 \\div 1.006 \\times 100 = 2{,}49",
            "no demuestra desplazamiento habitual",
            "no pruebas automáticas de importación, exportación o movilidad habitual",
        ),
        "dinero-mercado-limites": (
            "no documenta un mercado o feria regular",
            "tampoco demuestra una comunidad autosuficiente o cerrada",
            "no pueden calcularse importaciones, exportaciones",
            "monetización parcial",
            "el capítulo 13 realizará la síntesis integrada",
        ),
        "dinero-sintesis": (
            "lenguaje de valoración",
            "no mide toda la circulación",
            "no un sector comercial",
            "las categorías no se suman ni producen ingresos anuales",
            "sin probar aislamiento o autosuficiencia",
        ),
    }
    for anchor, phrases in required_by_section.items():
        section = sections[anchor]
        absent = [phrase for phrase in phrases if phrase.casefold() not in section]
        if absent:
            errors.append(
                f"C12_CONTENT_{anchor.upper().replace('-', '_')}: faltan relaciones "
                + ", ".join(absent)
            )

    propositions = tuple(
        proposition
        for _, paragraph_propositions in _controlled_paragraphs(body)
        for proposition in paragraph_propositions
    )
    prohibited_predicates = {
        "C12_CURRENCY_IS_FULL_MONETIZATION": (
            r"\bdemostraba\b[^.;]{0,60}\beconom[ií]a\s+plenamente\s+monetizada\b",
        ),
        "C12_VALUATION_IS_EFFECTIVE_PAYMENT": (
            r"\bera\b[^.;]{0,40}\bpago\s+efectiv(?:o|amente)\b",
        ),
        "C12_UTILITY_IS_REAL_INCOME": (
            r"\bera\b[^.;]{0,45}\bingreso\s+(?:real|efectivo)\b",
        ),
        "C12_DAILY_WAGE_IS_ANNUAL_INCOME": (
            r"\bera\b[^.;]{0,45}\bingreso\s+anual\b",
        ),
        "C12_ASSUMED_WORKDAYS": (
            r"\bmultiplicando\b[^.;]{0,45}\bjornal\b[^.;]{0,35}\b365\s+d[ií]as\b",
        ),
        "C12_LABRADOR_IS_LANDOWNER": (
            r"\bera\b[^.;]{0,35}\bpropietario\s+de\s+tierras\b",
        ),
        "C12_JORNALERO_IS_PERMANENT_EMPLOYEE": (
            r"\bera\b[^.;]{0,35}\basalariado\s+permanente\b",
        ),
        "C12_CRAFT_IS_EXCLUSIVE_OCCUPATION": (
            r"\bdemostraba\b[^.;]{0,40}\bdedicaci[oó]n\s+exclusiva\b",
        ),
        "C12_OVERLAPPING_LABOR_SUM": (
            r"\b18\s+jornaleros\b[^.;]{0,45}\b24\s+labradores\b[^.;]{0,45}\bsumaban\s+43\s+trabajadores\b",
        ),
        "C12_MODERN_ACTIVE_POPULATION": (
            r"\bformaban\b[^.;]{0,45}\bpoblaci[oó]n\s+activa\s+moderna\b",
        ),
        "C12_UNSUPPORTED_FAMILY_INCOME": (
            r"\bpermiten\s+calcular\b[^.;]{0,35}\brenta\s+familiar\b",
        ),
        "C12_FISCAL_UTILITY_IS_WEALTH": (
            r"\bmed[ií]an\b[^.;]{0,35}\briqueza\b",
        ),
        "C12_EXTERNAL_PERSON_IS_COMMERCE": (
            r"\bdemostraba\b[^.;]{0,50}\brelaci[oó]n\s+comercial\b",
        ),
        "C12_PLACE_MENTION_IS_FLOW": (
            r"\bdemostraba\b[^.;]{0,45}\bflujo\s+econ[oó]mico\s+estable\b",
        ),
        "C12_REGULAR_MARKET": (
            r"\bhab[ií]a\b[^.;]{0,25}\bmercado\s+local\s+regular\b",
        ),
        "C12_UNSUPPORTED_EXPORTS_IMPORTS": (
            r"\bexportaba\b[^.;]{0,60}\be\s+importaba\b",
        ),
        "C12_ABSENCE_PROVES_SELF_SUFFICIENCY": (
            r"\bdemostraba\b[^.;]{0,45}\bautosuficiencia\b",
        ),
        "C12_FISCAL_AMOUNT_IS_LABOR_INCOME": (
            r"\beran\b[^.;]{0,35}\bingreso\s+laboral\b",
        ),
        "C12_COMMON_EXPENSE_IS_LOCAL_INCOME": (
            r"\beran\b[^.;]{0,35}\bingreso\s+general\b",
        ),
        "C12_EVIDENCE_LIMITS_ERASED": (
            r"\bcomprend[ií]an\b[^.;]{0,50}\btoda\s+la\s+circulaci[oó]n\s+monetaria\b",
        ),
        "C12_CHAPTER_THIRTEEN_BOUNDARY": (
            r"\bhizo\b[^.;]{0,35}\bresiliente\b[^.;]{0,35}\beconom[ií]a\b",
        ),
    }
    for code, patterns in prohibited_predicates.items():
        if any(
            not _predicate_is_negated(proposition, match.start())
            for proposition in propositions
            for pattern in patterns
            for match in re.finditer(pattern, proposition)
        ):
            errors.append(f"{code}: formulación no autorizada en el capítulo 12")
    return errors


def _validate_chapter_thirteen_body(body: str) -> list[str]:
    """Validate the synthesis without turning exposures into outcomes."""

    errors: list[str] = []
    sections = {
        anchor: _plain_text(_markdown_section(body, anchor))
        for anchor in CHAPTER_THIRTEEN_ANCHORS
    }
    for anchor, section in sections.items():
        if not section:
            errors.append(f"C13_SECTION_{anchor.upper().replace('-', '_')}: falta la sección")

    required_by_section = {
        "economia-integrada-alcance": (
            "conjunto local de actividades, recursos y obligaciones relacionados entre sí",
            "no significa una economía integrada en mercados regionales",
            "el señorío forma parte de esta arquitectura",
            "valor no equivale a producción",
        ),
        "economia-base-agraria": (
            "2.750,5 de 2.953,5 medidas principales",
            "sobre el subtotal más amplio de 3.811,5 medidas principales representan el 72,16 %",
            "no un monocultivo probado",
            "uso común no equivale a propiedad comunal",
        ),
        "economia-agua-transformacion": (
            "ocho ruedas descritas",
            "molino venturero cuyo número de ruedas no consta",
            "utilidades reguladas, no volumen molido",
            "no una paralización simultánea ni una crisis de abastecimiento observada",
        ),
        "economia-trabajo-instituciones": (
            "no se suman como población activa",
            "sus utilidades diarias no son ingresos anuales",
            "mínimo institucional de 1.006 reales",
            "repartimiento y turno son mecanismos operativos documentados",
        ),
        "economia-dependencias": (
            "dependencia documentada",
            "exposición plausible derivada de ella",
            "crisis o daño observado",
            "no documenta una crisis económica general en 1752",
            "la ausencia de datos sobre reservas, crédito, cosechas efectivas o distribución doméstica no constituye por sí misma vulnerabilidad histórica",
        ),
        "economia-diversidad-amortiguadores": (
            "no demuestra diversificación de ingresos en cada hogar",
            "redundancia potencial de unidades",
            "mecanismos potencialmente amortiguadores, no garantías de estabilidad",
        ),
        "economia-vulnerabilidades": (
            "cuatro exposiciones estructurales y acotadas",
            "no se usa la falta de una cifra como prueba de fragilidad",
            "tampoco los 1.006 reales parciales permiten medir presión fiscal",
        ),
        "economia-resiliencia-limites": (
            "un choque, una respuesta, una recuperación o una adaptación observables",
            "no se afirma que el sistema fuera resiliente",
            "posibilidades de amortiguación cuya eficacia no puede medirse",
        ),
        "economia-limites-reconstruccion": (
            "no pueden afirmarse autosuficiencia alimentaria",
            "celemín y medida principal no se convierten",
            "las fuentes externas aclaran vocabulario, contexto regional e instituciones",
            "siguen abiertas la base jurídica concreta de las alcabalas y del pozo",
        ),
        "economia-sintesis": (
            "esta integración interna no demuestra integración comercial",
            "la variedad no demuestra resiliencia",
            "la dependencia no prueba crisis",
            "no un balance total ni una teoría general de la economía campesina",
        ),
        "economia-transicion-manuscrito": (
            "con esta síntesis concluye la parte ii",
            "la parte iii vuelve al soporte material",
            "sin convertir la imagen en sustituto de la transcripción o del aparato crítico",
        ),
    }
    for anchor, phrases in required_by_section.items():
        section = sections[anchor]
        absent = [phrase for phrase in phrases if phrase.casefold() not in section]
        if absent:
            errors.append(
                f"C13_CONTENT_{anchor.upper().replace('-', '_')}: faltan relaciones "
                + ", ".join(absent)
            )

    propositions = tuple(
        proposition
        for _, paragraph_propositions in _controlled_paragraphs(body)
        for proposition in paragraph_propositions
    )
    prohibited_predicates = {
        "C13_INTERNAL_IS_MARKET_INTEGRATION": (
            r"\bdemostraba\b[^.;]{0,70}\bintegrad[ao]\b[^.;]{0,45}\bmercados?\s+regionales?\b",
        ),
        "C13_DIVERSITY_IS_RESILIENCE": (
            r"\bdiversidad\b[^.;]{0,50}\b(?P<predicate>demostraba)\b[^.;]{0,45}\bresiliente\b",
        ),
        "C13_ABSENCE_IS_VULNERABILITY": (
            r"\bfalta\s+de\s+datos\b[^.;]{0,55}\b(?P<predicate>demostraba)\b[^.;]{0,35}\bvulnerabilidad\b",
        ),
        "C13_DEPENDENCY_IS_OBSERVED_CRISIS": (
            r"\bdependencia\b[^.;]{0,55}\b(?P<predicate>demuestra)\b[^.;]{0,35}\b(?:hubo|ocurri[oó])\b[^.;]{0,30}\bcrisis\b",
        ),
        "C13_FOOD_SELF_SUFFICIENCY": (
            r"\bera\b[^.;]{0,35}\bautosuficiente\s+en\s+alimentos\b",
        ),
        "C13_ENERGY_SELF_SUFFICIENCY": (
            r"\bera\b[^.;]{0,35}\bautosuficiente\s+en\s+energ[ií]a\b",
        ),
        "C13_GENERAL_SELF_SUFFICIENCY": (
            r"\bera\b[^.;]{0,35}\becon[oó]micamente\s+autosuficiente\b",
        ),
        "C13_SUSTAINABILITY": (
            r"\bel\s+sistema\b[^.;]{0,35}\b(?P<predicate>era)\s+sostenible\b",
        ),
        "C13_ECOLOGICAL_BALANCE": (
            r"\bexist[ií]a\b[^.;]{0,40}\bequilibrio\s+ecol[oó]gico\b",
        ),
        "C13_TOTAL_PRODUCTIVITY": (
            r"\bpermite\s+calcular\b[^.;]{0,45}\bproductividad\s+total\b",
        ),
        "C13_PER_CAPITA_INCOME": (
            r"\bpermite\s+calcular\b[^.;]{0,45}\brenta\s+por\s+habitante\b",
        ),
        "C13_HOUSEHOLD_INCOME": (
            r"\bpermite\s+calcular\b[^.;]{0,45}\brenta\s+por\s+hogar\b",
        ),
        "C13_LIVING_STANDARD": (
            r"\bpermite\s+(?:medir|deducir)\b[^.;]{0,45}\bnivel\s+de\s+vida\b",
        ),
        "C13_INEQUALITY": (
            r"\bpermite\s+(?:medir|deducir)\b[^.;]{0,45}\bdesigualdad\b",
        ),
        "C13_VALUATION_IS_PRODUCTION": (
            r"\bvaloraciones?\s+fiscales?\b[^.;]{0,45}\b(?P<predicate>eran)\b[^.;]{0,25}\bproducci[oó]n\b",
        ),
        "C13_UTILITY_IS_EFFECTIVE_INCOME": (
            r"\butilidades?\b[^.;]{0,45}\b(?P<predicate>eran)\b[^.;]{0,35}\bingresos?\s+efectivos?\b",
        ),
        "C13_EXTERNAL_IS_REGULAR_TRADE": (
            r"\bconexiones?\s+exteriores?\b[^.;]{0,55}\b(?P<predicate>demostraban)\b[^.;]{0,35}\bcomercio\s+regular\b",
        ),
        "C13_TRADES_ARE_HOUSEHOLD_DIVERSIFICATION": (
            r"\bvariedad\s+de\s+oficios\b[^.;]{0,55}\b(?P<predicate>demostraba)\b[^.;]{0,40}\bdiversificaci[oó]n\s+por\s+hogar\b",
        ),
        "C13_RYE_IS_MONOCULTURE": (
            r"\bpredominio\s+(?:del\s+)?centen(?:o|al)\b[^.;]{0,55}\b(?P<predicate>demostraba)\b[^.;]{0,30}\bmonocultivo\b",
        ),
        "C13_COMMON_USE_IS_PROPERTY": (
            r"\buso\s+com[uú]n\b[^.;]{0,45}\b(?P<predicate>demostraba)\b[^.;]{0,35}\bpropiedad\s+comunal\b",
        ),
        "C13_MILLS_ARE_SUFFICIENT": (
            r"\bpresencia\s+de\s+molinos\b[^.;]{0,55}\b(?P<predicate>garantizaba)\b[^.;]{0,40}\bsuficiencia\s+de\s+transformaci[oó]n\b",
        ),
        "C13_PARTIAL_FISCAL_IS_TOTAL": (
            r"\b1\.006\s+reales\b[^.;]{0,45}\b(?P<predicate>med[ií]an)\b[^.;]{0,35}\bpresi[oó]n\s+fiscal\s+total\b",
        ),
        "C13_PARTIAL_COMMON_IS_BUDGET": (
            r"\b233\s+reales\b[^.;]{0,45}\b(?P<predicate>eran)\b[^.;]{0,35}\bpresupuesto\s+completo\b",
        ),
        "C13_UNSUPPORTED_CAUSALITY": (
            r"\bfiscalidad\b[^.;]{0,45}\b(?P<predicate>caus[oó])\b[^.;]{0,35}\bca[ií]da\s+de\s+la\s+producci[oó]n\b",
        ),
        "C13_EVIDENCE_LIMITS_ERASED": (
            r"\bla\s+reconstrucci[oó]n\b[^.;]{0,40}\b(?P<predicate>es)\s+completa\b[^.;]{0,45}\bsin\s+lagunas\b",
        ),
    }
    for code, patterns in prohibited_predicates.items():
        if any(
            not _predicate_is_negated(
                proposition,
                match.start("predicate")
                if "predicate" in match.groupdict()
                else match.start(),
            )
            for proposition in propositions
            for pattern in patterns
            for match in re.finditer(pattern, proposition)
        ):
            errors.append(f"{code}: formulación no autorizada en el capítulo 13")
    return errors


def _validate_part_two_consistency(chapter_bodies: dict[int, str]) -> list[str]:
    """Keep accepted Part II meanings stable across chapters 5–13."""

    required = {
        5: "no paga cosa alguna al señor por el establecimiento del suelo",
        6: "no se suman para formar una población activa",
        7: "no permite deducir autoconsumo, suficiencia alimentaria",
        8: "no acreditan por sí solas titularidad",
        9: "ocho ruedas descritas en cuatro casas de molinos",
        10: "no pueden calcularse carga por vecino o por habitante, presión fiscal",
        11: "no son ingresos, gastos totales ni presupuesto completo",
        12: "tampoco demuestra una comunidad autosuficiente o cerrada",
        13: "esta integración interna no demuestra integración comercial",
    }
    errors: list[str] = []
    for number, phrase in required.items():
        body = chapter_bodies.get(number, "")
        if phrase.casefold() not in _normalized_text(body):
            errors.append(
                f"PART_TWO_C{number}_CONSISTENCY: se ha perdido una cautela aceptada"
            )
    return errors


def _normalized_evidence(metadata: dict) -> dict[str, tuple[str, ...]]:
    evidence = metadata.get("evidence", {})
    if not isinstance(evidence, dict):
        return {}
    return {level: tuple(values or []) for level, values in evidence.items()}


def _all_publication_texts() -> list[tuple[Path, str]]:
    suffixes = {".md", ".qmd", ".yml", ".py", ".scss", ".bib"}
    return [
        (path, path.read_text(encoding="utf-8"))
        for path in PUBLICATION_ROOT.rglob("*")
        if path.is_file()
        and path.suffix in suffixes
        and "_book" not in path.parts
    ]


def validate() -> list[str]:
    errors: list[str] = []
    expected_ids = {item for group in EVIDENCE_GROUPS.values() for item in group}
    required_generated = {
        "facsimile": ("#pagina-digital-12", "lightbox: true"),
        "facsimile_full": (
            "#pagina-digital-01",
            "#pagina-digital-18",
            "lightbox: true",
        ),
        "transcription": ("#folio-315v", "lightbox: true"),
        "transcription_full": (
            "#transcripcion-portada",
            "#folio-315v",
            "#hoja-enfrentada-posterior",
            "lightbox: true",
        ),
        "modernized": ("#respuesta-17",),
        "modernized_full": (
            "#modernizada-portada",
            "#comparecencia",
            "#respuesta-1",
            "#respuesta-40",
            "#ratificacion-edades-firmas",
            "#concordancia-material",
            "#notas",
            "#nota-de-uso",
        ),
        "glossary_full": ("#glosario-entradas", "#glosario-senorio"),
        "quantitative_full": ("#cuadro-ter-007", "#cuadro-fis-011"),
        "concordance_full": (
            "#concordancia-unidades",
            "#concordancia-respuestas",
        ),
        "evidence_matrix_full": (
            "#evidencia-jur-001",
            "#evidencia-lim-013",
        ),
        "apparatus": ("#cuadro-molinos", "#matriz-molinera"),
    }
    if not CHAPTER_ONE.is_file():
        errors.append(f"Falta el capítulo 1: {CHAPTER_ONE}")
    else:
        try:
            chapter_one_metadata = _front_matter(CHAPTER_ONE)
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(str(exc))
        else:
            for key in ("title", "chapter-id", "publication-status", "sources"):
                if key not in chapter_one_metadata:
                    errors.append(f"Falta {key} en el capítulo 1")
            if chapter_one_metadata.get("chapter-id") != "catastro-ensenada":
                errors.append("chapter-id incorrecto en el capítulo 1")
            if chapter_one_metadata.get("publication-status") != "development":
                errors.append("El capítulo 1 debe declarar publication-status: development")
            if chapter_one_metadata.get("evidence"):
                errors.append("El capítulo 1 no debe inventar identificadores de evidencia")
            sources = chapter_one_metadata.get("sources", [])
            source_paths = {
                source.get("path") for source in sources if isinstance(source, dict)
            }
            locators = [
                source.get("locator") for source in sources if isinstance(source, dict)
            ]
            if source_paths != CHAPTER_ONE_SOURCE_PATHS or not all(locators):
                errors.append("Procedencia incompleta o no autorizada en el capítulo 1")
        chapter_one_text = CHAPTER_ONE.read_text(encoding="utf-8")
        links = set(re.findall(r"\]\((https://[^)]+)\)", chapter_one_text))
        if links != CHAPTER_ONE_LINKS:
            errors.append(
                "Los enlaces externos del capítulo 1 no son los institucionales autorizados"
            )

    if not CHAPTER_TWO.is_file():
        errors.append(f"Falta el capítulo 2: {CHAPTER_TWO}")
    else:
        try:
            chapter_two_metadata = _front_matter(CHAPTER_TWO)
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(str(exc))
        else:
            for key in ("title", "chapter-id", "publication-status", "sources"):
                if key not in chapter_two_metadata:
                    errors.append(f"Falta {key} en el capítulo 2")
            if (
                chapter_two_metadata.get("title")
                != "Las Respuestas Generales y el interrogatorio de cuarenta preguntas"
            ):
                errors.append("Título incorrecto en el capítulo 2")
            if (
                chapter_two_metadata.get("chapter-id")
                != "respuestas-generales-interrogatorio"
            ):
                errors.append("chapter-id incorrecto en el capítulo 2")
            if chapter_two_metadata.get("publication-status") != "development":
                errors.append("El capítulo 2 debe declarar publication-status: development")
            if "evidence" in chapter_two_metadata:
                errors.append("El capítulo 2 no debe inventar identificadores de evidencia")
            sources = chapter_two_metadata.get("sources", [])
            source_paths = [
                source.get("path") for source in sources if isinstance(source, dict)
            ]
            locators = [
                source.get("locator") for source in sources if isinstance(source, dict)
            ]
            if (
                set(source_paths) != CHAPTER_TWO_SOURCE_PATHS
                or len(source_paths) != len(CHAPTER_TWO_SOURCE_PATHS)
                or not all(locators)
            ):
                errors.append("Procedencia incompleta o no autorizada en el capítulo 2")
            for source_path in CHAPTER_TWO_SOURCE_PATHS:
                if not (REPOSITORY_ROOT / source_path).is_file():
                    errors.append(f"Fuente declarada inexistente en el capítulo 2: {source_path}")

        chapter_two_text = CHAPTER_TWO.read_text(encoding="utf-8")
        chapter_two_links = set(
            re.findall(r"\]\((https://[^)]+)\)", chapter_two_text)
        )
        if chapter_two_links != CHAPTER_TWO_LINKS:
            errors.append(
                "Los enlaces externos del capítulo 2 no son los institucionales autorizados"
            )
        for question_range, subject in CHAPTER_TWO_THEMATIC_BLOCKS:
            row = rf"\|\s*{re.escape(question_range)}\s*\|\s*{re.escape(subject)}\s*\|"
            if not re.search(row, chapter_two_text, re.IGNORECASE):
                errors.append(
                    f"Falta el bloque temático {question_range} en el capítulo 2"
                )
        normalized_chapter_two = re.sub(r"\s+", " ", chapter_two_text).casefold()
        for phrase in (
            "pregunta 29",
            "hay en la población",
            "transmisión moderna",
            "titularidad",
            "utilidad anual",
            "formulario externo",
            "lectura paleográfica local",
        ):
            if phrase.casefold() not in normalized_chapter_two:
                errors.append(
                    f"Falta explicar {phrase!r} en el tratamiento de la pregunta 29"
                )
        if _has_extensive_questionnaire_sequence(chapter_two_text):
            errors.append(
                "El capítulo 2 contiene una secuencia extensa de preguntas o "
                "respuestas; los cuarenta pares completos pertenecen al capítulo 16"
            )

    chapter_specs = (
        (CHAPTER_THREE, "El expediente de Sorribos y Santibáñez de Ordás",
         "expediente-sorribos-santibanez", CHAPTER_THREE_SOURCE_PATHS,
         CHAPTER_THREE_EVIDENCE, 3),
        (CHAPTER_FOUR, "Del manuscrito al volumen actual",
         "manuscrito-volumen-actual", CHAPTER_FOUR_SOURCE_PATHS, None, 4),
        (CHAPTER_FIVE, "Un lugar de señorío en el Concejo de Ordás",
         "lugar-senorio-concejo-ordas", CHAPTER_FIVE_SOURCE_PATHS,
         CHAPTER_FIVE_EVIDENCE, 5),
        (CHAPTER_SIX, "Vecinos, hogares, viviendas y trabajo",
         "vecinos-hogares-viviendas-trabajo", CHAPTER_SIX_SOURCE_PATHS,
         CHAPTER_SIX_EVIDENCE, 6),
        (CHAPTER_SEVEN, "Tierra, sistema agrario y medidas",
         "tierra-sistema-agrario-medidas", CHAPTER_SEVEN_SOURCE_PATHS,
         CHAPTER_SEVEN_EVIDENCE, 7),
        (CHAPTER_EIGHT, "Ganadería, montes y aprovechamientos comunales",
         "ganaderia-montes-aprovechamientos-comunales",
         CHAPTER_EIGHT_SOURCE_PATHS, CHAPTER_EIGHT_EVIDENCE, 8),
        (CHAPTER_NINE, "Río, molinos y otros recursos productivos",
         "rio-molinos-recursos", CHAPTER_NINE_SOURCE_PATHS,
         CHAPTER_NINE_EVIDENCE, 9),
        (CHAPTER_TEN, "Iglesia, señorío y fiscalidad",
         "iglesia-senorio-fiscalidad", CHAPTER_TEN_SOURCE_PATHS,
         CHAPTER_TEN_EVIDENCE, 10),
        (CHAPTER_ELEVEN, "Hacienda concejil y servicios colectivos",
         "hacienda-concejil-servicios-colectivos", CHAPTER_ELEVEN_SOURCE_PATHS,
         CHAPTER_ELEVEN_EVIDENCE, 11),
        (CHAPTER_TWELVE, "Dinero, oficios y conexiones exteriores",
         "dinero-oficios-conexiones-exteriores", CHAPTER_TWELVE_SOURCE_PATHS,
         CHAPTER_TWELVE_EVIDENCE, 12),
        (CHAPTER_THIRTEEN,
         "Una economía rural integrada: vulnerabilidades, resiliencia y límites",
         "economia-rural-integrada-vulnerabilidades-resiliencia-limites",
         CHAPTER_THIRTEEN_SOURCE_PATHS, CHAPTER_THIRTEEN_EVIDENCE, 13),
    )
    chapter_bodies: dict[int, str] = {}
    for path, title, chapter_id, allowed_sources, required_evidence, number in chapter_specs:
        if not path.is_file():
            errors.append(f"Falta el capítulo {number}: {path}")
            continue
        try:
            chapter_metadata, chapter_body = _front_matter_and_body(path)
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(str(exc))
            continue
        chapter_bodies[number] = chapter_body
        if chapter_metadata.get("title") != title:
            errors.append(f"Título incorrecto en el capítulo {number}")
        if chapter_metadata.get("chapter-id") != chapter_id:
            errors.append(f"chapter-id incorrecto en el capítulo {number}")
        if chapter_metadata.get("publication-status") != "development":
            errors.append(f"publication-status incorrecto en el capítulo {number}")
        sources = chapter_metadata.get("sources", [])
        source_paths = [source.get("path") for source in sources if isinstance(source, dict)]
        locators = [source.get("locator") for source in sources if isinstance(source, dict)]
        if (set(source_paths) != allowed_sources
                or len(source_paths) != len(allowed_sources) or not all(locators)):
            errors.append(f"Procedencia incompleta o no autorizada en el capítulo {number}")
        for source_path in allowed_sources:
            if not (REPOSITORY_ROOT / source_path).is_file():
                errors.append(f"Fuente inexistente en el capítulo {number}: {source_path}")
        if required_evidence is None and "evidence" in chapter_metadata:
            errors.append("El capítulo 4 no debe declarar evidencia")
        elif (required_evidence is not None
              and _normalized_evidence(chapter_metadata) != required_evidence):
            errors.append(f"Evidencia incorrecta en el capítulo {number}")

    if CHAPTER_THREE.is_file():
        chapter_three_text = chapter_bodies.get(3, "")
        normalized_three = _normalized_text(chapter_three_text)
        required_three = (
            "17 de septiembre de 1752", "joaquín aguado",
            "manuel antonio de bega", "juan álvarez", "remirio rodríguez",
            "domingo díez", "francisco de llorca", "domingo suárez",
            "manuel antonio alonso", "excepto el cura", "18 páginas digitales",
            "35 unidades documentales", "cuarenta respuestas",
            "dos rúbricas gráficas inferiores",
            "69 años", "49 años", "59 años", "52 años", "44 años",
        )
        for phrase in required_three:
            if phrase not in normalized_three:
                errors.append(f"Falta el hecho controlado {phrase!r} en el capítulo 3")
        if not all(form in chapter_three_text for form in ("Sorribios", "Sorribos", "Sorrios")):
            errors.append("Falta la secuencia toponímica positiva en el capítulo 3")
        if "sorribas" in normalized_three:
            errors.append("El capítulo 3 introduce la forma no autorizada Sorribas")
        if "(04-manuscrito-volumen-actual.qmd)" not in chapter_three_text:
            errors.append("El capítulo 3 no enlaza el capítulo 4")
        if "publication/generated/" in chapter_three_text:
            errors.append("El capítulo 3 invade la explicación técnica del capítulo 4")
        if re.search(r"<[A-Za-z][^>]*>", chapter_three_text):
            errors.append("El capítulo 3 contiene HTML crudo")
        errors.extend(_validate_chapter_three_body(chapter_three_text))

    if CHAPTER_FOUR.is_file():
        chapter_four_text = chapter_bodies.get(4, "")
        normalized_four = _normalized_text(chapter_four_text)
        required_four = (
            "pdf manuscrito autoritativo", "18 páginas digitales",
            "35 unidades documentales", "facsímil",
            "transcripción paleográfica semidiplomática", "edición crítica 3.6",
            "edición modernizada 1.3", "preguntas externas", "respuestas locales",
            "estudio histórico 1.2", "registro 1.2", "front matter",
            "libro quarto", "publication/content/", "publication/generated/",
            "referencia editorial", "no es una autoridad textual",
            "permanece fuera de github",
        )
        for phrase in required_four:
            if phrase not in normalized_four:
                errors.append(f"Falta distinguir {phrase!r} en el capítulo 4")
        for heading in UNIT_HEADINGS:
            if heading.casefold() not in normalized_four:
                errors.append(f"Falta la sección {heading!r} en el capítulo 4")
        for level in ("d — dato", "c — cálculo", "i — interpretación",
                      "e — contexto", "l — límite"):
            if level not in normalized_four:
                errors.append(f"Falta explicar el nivel {level!r} en el capítulo 4")
        if "(03-expediente-sorribos-santibanez.qmd)" not in chapter_four_text:
            errors.append("El capítulo 4 no enlaza el capítulo 3")
        for participant in ("Joaquín Aguado", "Remirio Rodríguez", "Domingo Díez"):
            if participant in chapter_four_text:
                errors.append(f"El capítulo 4 invade la narración con {participant}")
        if re.search(r"<[A-Za-z][^>]*>", chapter_four_text):
            errors.append("El capítulo 4 contiene HTML crudo")
        errors.extend(_validate_chapter_four_body(chapter_four_text))

    if CHAPTER_FIVE.is_file():
        chapter_five_text = chapter_bodies.get(5, "")
        if "(../01-catastro/03-expediente-sorribos-santibanez.qmd)" not in chapter_five_text:
            errors.append("El capítulo 5 no enlaza el capítulo 3")
        if "(../01-catastro/04-manuscrito-volumen-actual.qmd)" not in chapter_five_text:
            errors.append("El capítulo 5 no enlaza el capítulo 4")
        if re.search(r"<[A-Za-z][^>]*>", chapter_five_text):
            errors.append("El capítulo 5 contiene HTML crudo")
        errors.extend(_validate_chapter_five_body(chapter_five_text))

    if CHAPTER_SIX.is_file():
        chapter_six_text = chapter_bodies.get(6, "")
        if "(05-lugar-senorio-concejo-ordas.qmd)" not in chapter_six_text:
            errors.append("El capítulo 6 no enlaza el capítulo 5")
        if re.search(r"<[A-Za-z][^>]*>", chapter_six_text):
            errors.append("El capítulo 6 contiene HTML crudo")
        errors.extend(_validate_chapter_six_body(chapter_six_text))

    if CHAPTER_SEVEN.is_file():
        chapter_seven_text = chapter_bodies.get(7, "")
        if "(06-vecinos-hogares-viviendas-trabajo.qmd)" not in chapter_seven_text:
            errors.append("El capítulo 7 no enlaza el capítulo 6")
        if re.search(r"<[A-Za-z][^>]*>", chapter_seven_text):
            errors.append("El capítulo 7 contiene HTML crudo")
        errors.extend(_validate_chapter_seven_body(chapter_seven_text))

    if CHAPTER_EIGHT.is_file():
        chapter_eight_text = chapter_bodies.get(8, "")
        if "(07-tierra-sistema-agrario-medidas.qmd)" not in chapter_eight_text:
            errors.append("El capítulo 8 no enlaza el capítulo 7")
        if re.search(r"<[A-Za-z][^>]*>", chapter_eight_text):
            errors.append("El capítulo 8 contiene HTML crudo")
        errors.extend(_validate_chapter_eight_body(chapter_eight_text))

    if CHAPTER_NINE.is_file():
        chapter_nine_text = chapter_bodies.get(9, "")
        if "(08-ganaderia-montes-aprovechamientos-comunales.qmd)" not in chapter_nine_text:
            errors.append("El capítulo 9 no enlaza el capítulo 8")
        if re.search(r"<[A-Za-z][^>]*>", chapter_nine_text):
            errors.append("El capítulo 9 contiene HTML crudo")
        errors.extend(_validate_chapter_nine_body(chapter_nine_text))

    if CHAPTER_TEN.is_file():
        chapter_ten_text = chapter_bodies.get(10, "")
        if "(09-rio-molinos-recursos.qmd#recursos-pesca)" not in chapter_ten_text:
            errors.append("El capítulo 10 no enlaza el capítulo 9")
        if re.search(r"<[A-Za-z][^>]*>", chapter_ten_text):
            errors.append("El capítulo 10 contiene HTML crudo")
        errors.extend(_validate_chapter_ten_body(chapter_ten_text))

    if CHAPTER_ELEVEN.is_file():
        chapter_eleven_text = chapter_bodies.get(11, "")
        if "(10-iglesia-senorio-fiscalidad.qmd)" not in chapter_eleven_text:
            errors.append("El capítulo 11 no enlaza el capítulo 10")
        if re.search(r"<[A-Za-z][^>]*>", chapter_eleven_text):
            errors.append("El capítulo 11 contiene HTML crudo")
        errors.extend(_validate_chapter_eleven_body(chapter_eleven_text))

    if CHAPTER_TWELVE.is_file():
        chapter_twelve_text = chapter_bodies.get(12, "")
        if "(11-hacienda-concejil-servicios-colectivos.qmd" not in chapter_twelve_text:
            errors.append("El capítulo 12 no enlaza el capítulo 11")
        if re.search(r"<[A-Za-z][^>]*>", chapter_twelve_text):
            errors.append("El capítulo 12 contiene HTML crudo")
        errors.extend(_validate_chapter_twelve_body(chapter_twelve_text))

    if CHAPTER_THIRTEEN.is_file():
        chapter_thirteen_text = chapter_bodies.get(13, "")
        if "(12-dinero-oficios-conexiones-exteriores.qmd" not in chapter_thirteen_text:
            errors.append("El capítulo 13 no enlaza el capítulo 12")
        if "../../generated/14-facsimil.qmd" not in chapter_thirteen_text:
            errors.append("El capítulo 13 no prepara la transición a la Parte III")
        if re.search(r"<[A-Za-z][^>]*>", chapter_thirteen_text):
            errors.append("El capítulo 13 contiene HTML crudo")
        errors.extend(_validate_chapter_thirteen_body(chapter_thirteen_text))

    errors.extend(_validate_part_two_consistency(chapter_bodies))

    register_path = (
        REPOSITORY_ROOT
        / "project"
        / "30_RESULTADOS"
        / "ESTUDIO_HISTORICO"
        / "Registro_Afirmaciones_Calculos_v1.md"
    )
    register = register_path.read_text(encoding="utf-8")
    registered = set(
        re.findall(r"^\|\s*([A-Z]+-\d{3})\s*\|", register, re.MULTILINE)
    )
    phase_3c_ids = {
        item for group in CHAPTER_THREE_EVIDENCE.values() for item in group
    }
    phase_3d_ids = {
        item for group in CHAPTER_FIVE_EVIDENCE.values() for item in group
    }
    phase_3e_ids = {
        item for group in CHAPTER_SIX_EVIDENCE.values() for item in group
    }
    phase_3f_ids = {
        item for group in CHAPTER_SEVEN_EVIDENCE.values() for item in group
    }
    phase_3g_ids = {
        item for group in CHAPTER_EIGHT_EVIDENCE.values() for item in group
    }
    phase_3h_ids = {
        item for group in CHAPTER_NINE_EVIDENCE.values() for item in group
    }
    phase_3i_ids = {
        item for group in CHAPTER_TEN_EVIDENCE.values() for item in group
    }
    phase_3j_ids = {
        item for group in CHAPTER_ELEVEN_EVIDENCE.values() for item in group
    }
    phase_3k_ids = {
        item for group in CHAPTER_TWELVE_EVIDENCE.values() for item in group
    }
    phase_3l_ids = {
        item for group in CHAPTER_THIRTEEN_EVIDENCE.values() for item in group
    }
    missing_registry = sorted(
        (expected_ids | phase_3c_ids | phase_3d_ids | phase_3e_ids | phase_3f_ids
         | phase_3g_ids | phase_3h_ids | phase_3i_ids | phase_3j_ids
         | phase_3k_ids | phase_3l_ids)
        - registered
    )
    if missing_registry:
        errors.append("Identificadores ausentes del Registro 1.2: " + ", ".join(missing_registry))

    chapter_text = CHAPTER_NINE.read_text(encoding="utf-8")
    chapter_normalized = re.sub(r"\s+", " ", chapter_text)
    if CANONICAL_FORMULA not in chapter_normalized:
        errors.append("Falta la formulación canónica de las ocho ruedas y el venturero")
    for phrase in (
        "ocho ruedas fijas",
        "paralizaron los molinos",
        "paralizó todos los molinos",
    ):
        if phrase.casefold() in chapter_text.casefold():
            errors.append(f"Expresión de regresión en el capítulo: {phrase}")

    for name, requirements in required_generated.items():
        path = GENERATED[name]
        if not path.is_file():
            errors.append(f"Falta el derivado generado: {path.relative_to(PUBLICATION_ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for requirement in requirements:
            if requirement not in text:
                errors.append(f"Falta {requirement} en {path.name}")
    for image in (
        PUBLICATION_ROOT / "generated" / "assets" / "manuscript-page-12.png",
        PUBLICATION_ROOT / "generated" / "assets" / "folio-315v.png",
    ):
        if not image.is_file() or image.stat().st_size == 0:
            errors.append(f"Falta la imagen regenerable: {image.name}")

    if GENERATED["facsimile"].is_file():
        facsimile = GENERATED["facsimile"].read_text(encoding="utf-8")
        if not re.search(
            r"!\[[^\]]{20,}\]\(assets/manuscript-page-12\.png\)"
            r'\{[^}]*fig-alt="[^"]{20,}"[^}]*\}',
            facsimile,
        ):
            errors.append("La página facsimilar carece de texto alternativo suficiente")
    if GENERATED["facsimile_full"].is_file():
        complete_facsimile = GENERATED["facsimile_full"].read_text(encoding="utf-8")
        try:
            metadata, body = _parse_document(
                complete_facsimile, GENERATED["facsimile_full"]
            )
        except ValueError as exc:
            errors.append(str(exc))
        else:
            if metadata.get("title") != "Facsímil íntegro del expediente":
                errors.append("Título incorrecto en el capítulo 14 generado")
            if metadata.get("chapter-id") != "facsimil-integro-expediente":
                errors.append("chapter-id incorrecto en el capítulo 14 generado")
            if metadata.get("publication-status") != "generated":
                errors.append("El capítulo 14 debe declarar publication-status: generated")
            anchors = re.findall(r"^## Página digital (\d{2}) \{#pagina-digital-\d{2}\}$", body, re.MULTILINE)
            images = re.findall(r"\]\(assets/facsimile/page-(\d{2})\.png\)", body)
            expected_pages = [f"{page:02d}" for page in range(1, 19)]
            if anchors != expected_pages:
                errors.append("El capítulo 14 no contiene las 18 anclas en orden 01–18")
            if images != expected_pages:
                errors.append("El capítulo 14 no contiene las 18 imágenes en orden 01–18")
            if body.count('fig-alt="Página digital') != 18:
                errors.append("Las 18 páginas facsimilares necesitan texto alternativo")
            if "### Transcripción" in body or "Transcripción paleográfica" in body:
                errors.append("El capítulo 14 no debe anticipar la transcripción del capítulo 15")
        facsimile_dir = PUBLICATION_ROOT / "generated" / "assets" / "facsimile"
        expected_images = [facsimile_dir / f"page-{page:02d}.png" for page in range(1, 19)]
        actual_images = sorted(facsimile_dir.glob("*.png")) if facsimile_dir.is_dir() else []
        if actual_images != expected_images:
            errors.append("La serie facsimilar debe contener exactamente page-01.png–page-18.png")
        for page, image in enumerate(expected_images, start=1):
            if not image.is_file() or image.stat().st_size == 0:
                errors.append(f"Falta la página facsimilar completa {page:02d}")
                continue
            try:
                with Image.open(image) as opened:
                    opened.verify()
                    if opened.width <= 0 or opened.height <= 0:
                        errors.append(f"Dimensiones inválidas en la página facsimilar {page:02d}")
            except (OSError, SyntaxError) as exc:
                errors.append(f"PNG inválido en la página facsimilar {page:02d}: {exc}")
    if GENERATED["transcription"].is_file():
        transcription = GENERATED["transcription"].read_text(encoding="utf-8")
        headings = tuple(
            re.findall(r"^### (.+?)\s*$", transcription, re.MULTILINE)
        )
        if headings != UNIT_HEADINGS:
            errors.append("Faltan secciones canónicas en la unidad paleográfica")
        try:
            canonical_lines = read_paleographic_lines(
                CANONICAL_EDITION.read_text(encoding="utf-8")
            )
        except (OSError, PrototypeBuildError) as exc:
            errors.append(f"No se pudo leer la transcripción canónica: {exc}")
        else:
            generated_lines = _generated_paleographic_lines(transcription)
            if generated_lines != canonical_lines:
                errors.append(
                    "Las líneas paleográficas generadas no coinciden exactamente con las "
                    "18 líneas canónicas o carecen de bloque de líneas semántico"
                )
            if len(generated_lines) != PALEOGRAPHIC_LINE_COUNT:
                errors.append(
                    f"La transcripción generada no contiene {PALEOGRAPHIC_LINE_COUNT} líneas"
                )
            hyphen_endings = tuple(
                line.rsplit(maxsplit=1)[-1]
                for line in generated_lines
                if line.endswith("-")
            )
            if hyphen_endings != DOCUMENTARY_HYPHEN_ENDINGS:
                errors.append("No se conservan los guiones documentales de final de línea")
        if not re.search(
            r"!\[[^\]]{20,}\]\(assets/folio-315v\.png\)"
            r'\{[^}]*fig-alt="[^"]{20,}"[^}]*\}',
            transcription,
        ):
            errors.append("El recorte paleográfico carece de texto alternativo suficiente")
    if GENERATED["transcription_full"].is_file():
        complete_transcription = GENERATED["transcription_full"].read_text(
            encoding="utf-8"
        )
        try:
            metadata, _ = _parse_document(
                complete_transcription, GENERATED["transcription_full"]
            )
            specs = load_unit_specs(
                REPOSITORY_ROOT / "project" / "00_CONTROL" / "unidades.yaml"
            )
            canonical_units = parse_critical_edition(
                CANONICAL_EDITION.read_text(encoding="utf-8"),
                specs,
                "sorrios_ensenada_orden_lectura_calidad_original.pdf",
            )
            generated_units = _generated_transcription_units(complete_transcription)
        except (OSError, ValueError, CriticalEditionError) as exc:
            errors.append(f"No se pudo validar el capítulo 15 completo: {exc}")
        else:
            if metadata.get("title") != "Transcripción y aparato crítico de las 35 unidades":
                errors.append("Título incorrecto en el capítulo 15 generado")
            if metadata.get("chapter-id") != "transcripcion-aparato-critico":
                errors.append("chapter-id incorrecto en el capítulo 15 generado")
            if metadata.get("publication-status") != "generated":
                errors.append("El capítulo 15 debe declarar publication-status: generated")
            if len(generated_units) != 35:
                errors.append(
                    f"El capítulo 15 contiene {len(generated_units)} unidades; se esperaban 35"
                )
            for canonical, generated in zip(
                canonical_units, generated_units, strict=False
            ):
                label, anchor, sections = generated
                if (
                    label != canonical.spec.label
                    or anchor != published_unit_anchor(canonical.spec)
                ):
                    errors.append(
                        f"Unidad o ancla discordante en {canonical.spec.unit_id}"
                    )
                    continue
                if tuple(sections) != SECTION_NAMES:
                    errors.append(
                        f"Secciones incompletas o desordenadas en {canonical.spec.unit_id}"
                    )
                    continue
                expected_image = f"assets/transcription/{canonical.spec.unit_id}.png"
                if expected_image not in sections["Imagen"]:
                    errors.append(
                        f"Imagen discordante en la unidad {canonical.spec.unit_id}"
                    )
                for section_name in SECTION_NAMES[1:]:
                    actual = sections[section_name]
                    if section_name == PALEOGRAPHIC_SECTION:
                        actual = _decode_line_block(actual)
                    if actual != canonical.sections[section_name]:
                        errors.append(
                            "Fidelidad textual rota en "
                            f"{canonical.spec.unit_id} / {section_name}"
                        )
            transcription_dir = (
                PUBLICATION_ROOT / "generated" / "assets" / "transcription"
            )
            expected_images = [
                transcription_dir / f"{spec.unit_id}.png" for spec in specs
            ]
            actual_images = (
                sorted(transcription_dir.glob("*.png"))
                if transcription_dir.is_dir()
                else []
            )
            if set(actual_images) != set(expected_images):
                errors.append("La serie 4B debe contener exactamente los 35 PNG canónicos")
            for image in expected_images:
                if not image.is_file() or image.stat().st_size == 0:
                    errors.append(f"Falta el recorte 4B: {image.name}")
                    continue
                try:
                    with Image.open(image) as opened:
                        opened.verify()
                        if opened.width <= 0 or opened.height <= 0:
                            errors.append(f"Dimensiones inválidas en {image.name}")
                except (OSError, SyntaxError) as exc:
                    errors.append(f"PNG inválido en {image.name}: {exc}")
    if GENERATED["modernized"].is_file():
        modernized = GENERATED["modernized"].read_text(encoding="utf-8")
        if "[^20]:" not in modernized or "[^21]:" not in modernized:
            errors.append("La respuesta 17 no conserva sus notas 20 y 21")
    if GENERATED["modernized_full"].is_file():
        complete_modernized = GENERATED["modernized_full"].read_text(
            encoding="utf-8"
        )
        modernized_source_root = (
            REPOSITORY_ROOT
            / "project"
            / "30_RESULTADOS"
            / "EDICION_DIVULGATIVA"
        )
        try:
            source_edition = load_modernized_edition(
                modernized_source_root
                / "Catastro_Sorrios_1752_Version_Modernizada.md"
            )
            modernized_specs = load_unit_specs(
                REPOSITORY_ROOT / "project" / "00_CONTROL" / "unidades.yaml"
            )
            validate_concordance_units(
                source_edition,
                tuple(spec.label for spec in modernized_specs),
            )
            validate_verified_questions(
                source_edition,
                (
                    modernized_source_root
                    / "Introduccion_Catastro_Ensenada_Sorrios.md"
                ).read_text(encoding="utf-8"),
                (
                    modernized_source_root
                    / "Verificacion_Interrogatorio_40_Preguntas.md"
                ).read_text(encoding="utf-8"),
            )
            validate_generated_fidelity(
                source_edition,
                complete_modernized,
                {
                    spec.label: published_unit_anchor(spec)
                    for spec in modernized_specs
                },
            )
        except (
            OSError,
            UnicodeError,
            CriticalEditionError,
            ModernizedEditionError,
            ModernizedBuildError,
        ) as exc:
            errors.append(f"Capítulo 16 no apto: {exc}")
        else:
            if len(source_edition.responses) != 40:
                errors.append("El capítulo 16 no deriva exactamente 40 respuestas")
            if len(source_edition.note_definitions) != 39:
                errors.append("El capítulo 16 no conserva las 39 notas de la fuente 1.3")
            for marker in (
                "[^modernizada-bega-vega]",
                "[^modernizada-administrarse]",
                "[^modernizada-avitadores]",
                "[^modernizada-renta-venta]",
            ):
                if marker not in complete_modernized:
                    errors.append(f"El capítulo 16 pierde la nota semántica {marker}")
    apparatus_paths = {
        name: PUBLICATION_ROOT / "generated" / name
        for name in APPARATUS_OUTPUT_NAMES
    }
    if all(path.is_file() for path in apparatus_paths.values()):
        try:
            project_data = yaml.safe_load(
                (
                    REPOSITORY_ROOT / "project" / "00_CONTROL" / "proyecto.yaml"
                ).read_text(encoding="utf-8")
            )
            manuscript_name = project_data["authorities"]["manuscript"]["name"]
            apparatus_data = load_apparatus_data(
                REPOSITORY_ROOT,
                PUBLICATION_ROOT,
                manuscript_name,
            )
            actual_apparatus = {
                name: path.read_text(encoding="utf-8")
                for name, path in apparatus_paths.items()
            }
            validate_apparatus_fidelity(apparatus_data, actual_apparatus)
        except (
            KeyError,
            TypeError,
            ApparatusSourceError,
            ApparatusBuildError,
        ) as exc:
            errors.append(f"Aparatos 4D no aptos: {exc}")
        else:
            if len(apparatus_data.glossary.entries) != 22:
                errors.append("El glosario 4D no contiene sus 22 entradas canónicas")
            if len(apparatus_data.register.calculated_entries) != 13:
                errors.append("Los cuadros 4D no derivan las 13 entradas de nivel C")
            associated = {
                calculation.identifier
                for entry in apparatus_data.register.calculated_entries
                for calculation in apparatus_data.register.associated_calculations(entry)
            }
            if len(associated) != 17:
                errors.append("Los cuadros 4D no conservan los 17 CAL asociados")
            if len(apparatus_data.register.entries) != 112:
                errors.append("La matriz 4D no contiene las 112 entradas D/C/I/E/L")
            concordance = actual_apparatus["concordancia.qmd"]
            if concordance.count("15-transcripcion.qmd#") != 100:
                errors.append("La concordancia no conserva sus enlaces al capítulo 15")
            if concordance.count("16-edicion-modernizada.qmd#") != 110:
                errors.append("La concordancia no conserva sus enlaces al capítulo 16")
            for name, text in actual_apparatus.items():
                if re.search(r"\]\([^)]*project/", text):
                    errors.append(f"{name} enlaza directamente una fuente local project/")

            phase_four_texts = (
                GENERATED["facsimile_full"].read_text(encoding="utf-8"),
                GENERATED["transcription_full"].read_text(encoding="utf-8"),
                GENERATED["modernized_full"].read_text(encoding="utf-8"),
                *actual_apparatus.values(),
            )
            phase_four_anchors = [
                anchor
                for text in phase_four_texts
                for anchor in re.findall(
                    r"^#{2,3} .+ \{#([a-z0-9-]+)\}$", text, re.MULTILINE
                )
            ]
            if len(phase_four_anchors) != len(set(phase_four_anchors)):
                errors.append("La Fase 4 conserva identificadores globales duplicados")
            if "portada" in phase_four_anchors:
                errors.append("La Fase 4 conserva el identificador ambiguo portada")
    index_paths = {
        name: PUBLICATION_ROOT / "generated" / "indices" / name
        for name in INDEX_OUTPUT_NAMES
    }
    if all(path.is_file() for path in index_paths.values()):
        try:
            index_data = load_index_data(REPOSITORY_ROOT, PUBLICATION_ROOT)
            actual_indexes = {
                name: path.read_text(encoding="utf-8")
                for name, path in index_paths.items()
            }
            validate_index_fidelity(index_data, actual_indexes)
        except (IndexSourceError, IndexBuildError) as exc:
            errors.append(f"Índices 5A no aptos: {exc}")
        else:
            if index_entry_counts(index_data) != (21, 9, 7, 12, 12, 27, 15, 40, 21):
                errors.append("Los nueve índices 5A no conservan sus recuentos esperados")
            if len(actual_indexes) != 9:
                errors.append("La Fase 5A debe generar exactamente nueve índices")
            anchors = [
                anchor
                for text in actual_indexes.values()
                for anchor in re.findall(r"\{#(indice-[a-z0-9-]+)", text)
            ]
            if len(anchors) != len(set(anchors)):
                errors.append("Los índices 5A contienen identificadores duplicados")
            for name, text in actual_indexes.items():
                html_targets = set(re.findall(r"\.qmd#([a-z0-9-]+)\)", text))
                pdf_targets = set(re.findall(r"\\hyperref\[([a-z0-9-]+)\]", text))
                if html_targets != pdf_targets:
                    errors.append(
                        f"{name} no comparte destinos entre localizadores HTML y PDF"
                    )
                if re.search(r"\*\*Páginas:\*\*\s+\d", text):
                    errors.append(f"{name} contiene una página PDF manual")
                if re.search(r"\]\([^)]*project/", text):
                    errors.append(f"{name} enlaza directamente una fuente project/")
                if "/home/" in text or "/tmp/" in text:
                    errors.append(f"{name} contiene una ruta local absoluta")
    else:
        missing = [str(path) for path in index_paths.values() if not path.is_file()]
        errors.append("Faltan índices generados 5A: " + ", ".join(missing))
    if GENERATED["apparatus"].is_file():
        apparatus = GENERATED["apparatus"].read_text(encoding="utf-8")
        absent = sorted(identifier for identifier in expected_ids if identifier not in apparatus)
        if absent:
            errors.append("Identificadores ausentes del aparato: " + ", ".join(absent))

    assets_path = PUBLICATION_ROOT / "meta" / "assets.yml"
    assets_data = yaml.safe_load(assets_path.read_text(encoding="utf-8"))
    assets = assets_data.get("assets", []) if isinstance(assets_data, dict) else []
    if len(assets) != 4:
        errors.append(
            "meta/assets.yml debe declarar dos activos del prototipo y las series 4A/4B"
        )
    for asset in assets[:2]:
        source = asset.get("source", {})
        if source.get("file_id") != MANUSCRIPT_FILE_ID or source.get("page") != 12:
            errors.append("Procedencia incorrecta en meta/assets.yml")
        destination = asset.get("destination", "")
        if not destination.startswith("generated/assets/"):
            errors.append("Los destinos facsimilares deben permanecer en generated/assets/")
    series = [asset for asset in assets if asset.get("asset_id") == "manuscript-pages-1-18"]
    if len(series) != 1:
        errors.append("meta/assets.yml debe declarar una única serie manuscript-pages-1-18")
    else:
        series_asset = series[0]
        if series_asset.get("source", {}).get("pages") != [1, 18]:
            errors.append("La serie 4A debe declarar las páginas fuente 1–18")
        if series_asset.get("page_count") != 18:
            errors.append("La serie 4A debe declarar page_count: 18")
        if series_asset.get("versioned") is not False:
            errors.append("Las imágenes completas de 4A deben permanecer no versionadas")
        if series_asset.get("versioning_policy") != "generated_ignored":
            errors.append("La serie 4A debe conservar la política generated_ignored")
    transcription_series = [
        asset
        for asset in assets
        if asset.get("asset_id") == "critical-edition-unit-images"
    ]
    if len(transcription_series) != 1:
        errors.append(
            "meta/assets.yml debe declarar una única serie critical-edition-unit-images"
        )
    else:
        unit_asset = transcription_series[0]
        if unit_asset.get("unit_count") != 35:
            errors.append("La serie 4B debe declarar unit_count: 35")
        if unit_asset.get("versioned") is not False:
            errors.append("Los 35 recortes de 4B deben permanecer no versionados")
        if unit_asset.get("versioning_policy") != "generated_ignored":
            errors.append("La serie 4B debe conservar la política generated_ignored")

    quarto_data = yaml.safe_load(
        (PUBLICATION_ROOT / "_quarto.yml").read_text(encoding="utf-8")
    )
    navigation = quarto_data.get("book", {}).get("chapters", [])
    expected_navigation = (
        "content/00-preliminares/00-prueba-tecnica.qmd",
        "content/01-catastro/01-catastro-ensenada.qmd",
        "content/01-catastro/02-respuestas-generales-interrogatorio.qmd",
        "content/01-catastro/03-expediente-sorribos-santibanez.qmd",
        "content/01-catastro/04-manuscrito-volumen-actual.qmd",
        "content/02-estudio/05-lugar-senorio-concejo-ordas.qmd",
        "content/02-estudio/06-vecinos-hogares-viviendas-trabajo.qmd",
        "content/02-estudio/07-tierra-sistema-agrario-medidas.qmd",
        "content/02-estudio/08-ganaderia-montes-aprovechamientos-comunales.qmd",
        "content/02-estudio/09-rio-molinos-recursos.qmd",
        "content/02-estudio/10-iglesia-senorio-fiscalidad.qmd",
        "content/02-estudio/11-hacienda-concejil-servicios-colectivos.qmd",
        "content/02-estudio/12-dinero-oficios-conexiones-exteriores.qmd",
        "content/02-estudio/13-economia-rural-integrada-vulnerabilidades-resiliencia-limites.qmd",
        "generated/14-facsimil.qmd",
        "generated/15-transcripcion.qmd",
        "generated/16-edicion-modernizada.qmd",
        "generated/glosario.qmd",
        "generated/cuadros-cuantitativos.qmd",
        "generated/concordancia.qmd",
        "generated/matriz-evidencia.qmd",
        *(f"generated/indices/{name}" for name in INDEX_OUTPUT_NAMES),
    )
    for item in expected_navigation:
        if navigation.count(item) != 1:
            errors.append(f"La navegación debe registrar una sola vez: {item}")
    positions = [navigation.index(item) for item in expected_navigation if item in navigation]
    if positions != sorted(positions):
        errors.append(
            "Orden incorrecto de los capítulos 1–16, aparatos 4D e índices 5A en la navegación"
        )
    explicit_anchors: list[str] = []
    for item in navigation:
        chapter_path = PUBLICATION_ROOT / str(item)
        if not chapter_path.is_file():
            continue
        explicit_anchors.extend(
            re.findall(
                r"\{#([a-z0-9-]+)(?:\s+[^}]*)?\}",
                chapter_path.read_text(encoding="utf-8"),
            )
        )
    duplicated_anchors = sorted(
        anchor for anchor in set(explicit_anchors) if explicit_anchors.count(anchor) > 1
    )
    if duplicated_anchors:
        errors.append(
            "Identificadores explícitos duplicados en el libro: "
            + ", ".join(duplicated_anchors)
        )
    for prototype_path in (
        "generated/14-facsimil-prototipo.qmd",
        "generated/15-transcripcion-prototipo.qmd",
        "generated/16-modernizada-prototipo.qmd",
        "generated/aparato-molinos.qmd",
    ):
        if prototype_path in navigation:
            errors.append(
                f"El prototipo no debe aparecer en la navegación principal: {prototype_path}"
            )

    chapters_data = yaml.safe_load(
        (PUBLICATION_ROOT / "meta" / "chapters.yml").read_text(encoding="utf-8")
    )
    manifest = chapters_data.get("chapters", [])
    manifest_paths = [item.get("path") for item in manifest]
    manifest_ids = [item.get("chapter_id") for item in manifest]
    if "Fase 2B" in chapters_data.get("purpose", ""):
        errors.append("meta/chapters.yml sigue limitado exclusivamente a la Fase 2B")
    for item in expected_navigation:
        if manifest_paths.count(item) != 1:
            errors.append(f"meta/chapters.yml debe registrar una sola vez: {item}")
    manifest_positions = [
        manifest_paths.index(item)
        for item in expected_navigation
        if item in manifest_paths
    ]
    if manifest_positions != sorted(manifest_positions):
        errors.append(
            "Orden incorrecto de los capítulos 1–16, aparatos 4D e índices 5A en meta/chapters.yml"
        )
    if len(manifest_ids) != len(set(manifest_ids)):
        errors.append("Los chapter_id de meta/chapters.yml deben ser únicos")

    for path, text in _all_publication_texts():
        if path.resolve() == Path(__file__).resolve():
            continue
        if re.search(r"(?:/home/|/tmp/|[A-Za-z]:\\\\)", text):
            errors.append(f"Ruta local absoluta en {path.relative_to(PUBLICATION_ROOT)}")
        if "b64_string" in text or "download_url" in text:
            errors.append(f"Referencia sensible inesperada en {path.relative_to(PUBLICATION_ROOT)}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--rendered",
        action="store_true",
        help="valida además la lineación en los artefactos HTML y PDF renderizados",
    )
    args = parser.parse_args(argv)
    try:
        errors = validate()
        if args.rendered:
            errors.extend(validate_rendered_outputs())
    except (
        OSError,
        ValueError,
        yaml.YAMLError,
        PrototypeBuildError,
        CriticalEditionError,
        ModernizedEditionError,
        ModernizedBuildError,
        ApparatusSourceError,
        ApparatusBuildError,
        IndexSourceError,
        IndexBuildError,
    ) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    scope = " y artefactos HTML/PDF" if args.rendered else ""
    print(
        "PASS: capítulos 1–16, facsímil 4A, transcripción 4B, modernizada 4C, "
        "aparatos reproducibles 4D, nueve índices reproducibles 5A, "
        "prototipo 2B, "
        "metadatos, anclas, "
        "evidencia y regresiones"
        f"{scope} validados"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

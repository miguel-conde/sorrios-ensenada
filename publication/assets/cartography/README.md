# Cartografía de orientación de PKG-03

Este directorio contiene dos mapas vectoriales contemporáneos preparados para
revisión humana antes de su eventual integración en PKG-07:

- `mapa-regional.svg`: España → provincia de León → área de Ordás;
- `mapa-local.svg`: Sorrios, Santibáñez de Ordás y los lugares del entorno que
  la documentación editorial identifica como necesarios;
- `cartography.json`: snapshot mínimo de datos oficiales, metadatos y
  transformaciones.

Los mapas no reconstruyen límites, caminos, jurisdicciones, términos ni
propiedades de 1752. Los límites dibujados son administrativos y actuales; el
curso del río y los puntos son referencias contemporáneas de orientación.

## Generación

Desde la raíz del repositorio:

```bash
.venv/bin/python publication/scripts/build_cartography.py
.venv/bin/python publication/scripts/build_cartography.py --check
```

La primera orden reconstruye los SVG sin conexión a partir del snapshot
versionado. La segunda valida nombres, coordenadas, pertenencia administrativa,
orientaciones relativas, atribuciones y estructura accesible de los SVG.

La actualización de fuentes necesita red y es una operación deliberada:

```bash
.venv/bin/python publication/scripts/build_cartography.py --refresh
```

`--refresh` consulta por identificador únicamente España, León, Santa María de
Ordás y Rioseco de Tapia; recorta el NGBE y la hidrografía al entorno local;
selecciona seis lugares y los segmentos denominados `Río Luna`; simplifica las
geometrías; descarta del mapa nacional polígonos inferiores a 0,001 grados
cuadrados, invisibles a su escala; y reescribe de forma determinista el snapshot
y los dos SVG.

## Fuentes, licencia y atribución

- Límites y Unidades Administrativas Actuales (BDLJE), IGN/CNIG:
  `Obra derivada de BDLJE CC-BY 4.0 ign.es`.
- Nomenclátor Geográfico Básico de España (NGBE), IGN/CNIG:
  `Obra derivada de NGBE CC-BY 4.0 ign.es`.
- IGR_HIDROGRAFIA v1 2023, Sistema Cartográfico Nacional/IGN:
  `Obra derivada de IGR_HIDROGRAFIA v1 2023 CC-BY 4.0 scne.es`.

La licencia de uso del IGN permite reutilización, modificación y redistribución
bajo CC BY 4.0, con reconocimiento visible. Las atribuciones están incorporadas
en los SVG y deben conservarse al integrarlos o adaptarlos. La licencia CC BY
4.0 del contenido original del volumen no borra la procedencia externa de estas
capas.

La página oficial del Ayuntamiento de Santa María de Ordás se usa solo para
contrastar que `Sorrios` es la denominación contemporánea del barrio de
Santibáñez. No se reproduce geometría, texto ni imagen municipal.

Consulta y snapshot: 11 de octubre de 2026. CRS de trabajo: EPSG:4326.

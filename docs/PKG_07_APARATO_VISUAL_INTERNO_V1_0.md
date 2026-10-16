# PKG-07 — Aparato visual interno

**Estado:** `COMPLETADO EN RAMA AISLADA — PENDIENTE DE REVISIÓN E INTEGRACIÓN`<br>
**Base:** `b2700e58807dda7751c26155af42971f1f8a0c83`<br>
**Rama:** `pkg-07/visual-apparatus-v1`<br>
**Tipo:** T4 — maquetación y aparato visual multiformato

## Resultado

Se han integrado exactamente los cuatro recursos aprobados por DEC-020–024:

| Recurso | Inserción | Criterio editorial |
|---|---|---|
| Cronología documental | capítulo 3, figura 3.1 | ocho hitos sustentados; diferencia fecha exacta, intervalo y contexto; `TOP-006` permanece solo en la matriz |
| Mapa local | capítulo 3, figura 3.2 | asset aprobado de PKG-03, sin modificación; orientación contemporánea y límites declarados |
| Mapa regional | capítulo 5, figura 5.1 | asset aprobado de PKG-03, sin modificación; orientación contemporánea y límites declarados |
| Diagrama de relaciones de la economía rural | capítulo 13, figura 13.1 | síntesis exclusiva del capítulo 13, sin cifras, flechas, causalidad, balance ni intensidad añadidos |

La cronología no pretende reconstruir una secuencia fonética completa. El
diagrama relaciona tierra y producción, ganadería, trabajo, agua y molinos,
común/servicios/repartimiento, fiscalidad/rentas, conexiones exteriores y los
límites documentales aceptados. No se han creado el esquema Concejo/municipio,
el esquema histórico del término, la antigua red de
vulnerabilidades/amortiguadores ni gráficos que requieran datos o inferencias
nuevas.

## Procedencia, accesibilidad e integridad

- Los mapas conservan exactamente los SVG aprobados por PKG-03:
  - regional: `2c6f3c76293a3c67aa698b9abd8b6ad184ad35c4fae3d80de6ec2f176ce99a1d`;
  - local: `ebc54b6593eab73778860a41db66221e78b6b83028b51602769d02a523fd15df`.
- Cada recurso tiene título, pie, texto alternativo y fuente/procedencia. Los
  SVG propios incluyen `role="img"`, `title`, `desc` y metadatos.
- Formas, tramas, estilos de línea y rótulos evitan depender solo del color.
  La presentación es adaptable y los cuatro recursos ofrecen ampliación
  mediante lightbox en HTML.
- `project/`, el capítulo 4 y el placeholder controlado del prólogo permanecen
  intactos. No se ha iniciado PKG-09 ni se han añadido datos humanos.
- `publication/generated/`, `_book/`, PDF, capturas y otros productos de render
  permanecen sin versionar.

## Validación

- Pruebas focales PKG-03/06/07: `28 passed`.
- Suite completa: `669 passed`, 0 fallos y 0 errores.
- Validadores del proyecto, fuentes, cartografía y publicación renderizada:
  PASS. `git diff --check`: PASS.
- HTML completo: 38 documentos.
- PDF completo: 353 páginas, 71.016.360 bytes, SHA-256
  `d1c16b88cdbfbbcaa2559c86fa91ea7a13395f0a97b0a255e8ecaae93568a4e0`.
- Revisión visual: cronología (PDF 36), mapa local (37), mapa regional (44) y
  diagrama económico (92); los cuatro se comprobaron también en HTML estrecho,
  con ampliación y navegación operativas.
- El render PDF utilizó `rsvg-convert` 2.58.0 como dependencia de conversión
  SVG del entorno, sin incorporar binarios ni artefactos al repositorio.

## Límites y continuación

La candidata formal no se regenera en PKG-07. `GATE-02` permanece pendiente y
PKG-09 no se inicia. El siguiente paso es la revisión independiente del commit
único de esta rama y, si resulta APTO, su integración por avance rápido en
`feature/quarto-book`.

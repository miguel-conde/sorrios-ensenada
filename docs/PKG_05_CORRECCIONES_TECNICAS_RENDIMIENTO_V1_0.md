# PKG-05 — Correcciones técnicas y rendimiento

## 1. Estado inicial

- Rama de partida: `feature/quarto-book`.
- Base exacta: `53979945eede54b7a10cd151bc92b71926b7fadc`.
- Rama aislada: `pkg-05/technical-fixes-performance-v1`, sin upstream.
- Árbol inicial limpio; `feature/quarto-book` estaba 4 commits por delante y 0
  por detrás de `origin/feature/quarto-book` (`5d90b280af8a2fe7185737f3342245cde8e6fac8`).
- `main == origin/main == e81dc9239ac8dbabfe77168a50ef98c4d3b79170`.
- Baseline técnica previa: `616 passed`; validadores del proyecto, fuentes,
  publicación estática y cartografía en PASS.
- Render baseline multiformato: 30 HTML; PDF de 335 páginas, 74.041.686 bytes y
  SHA-256 `df3d3b62d8f44fb566f0c4c02c3494cc0558ef17db9ebb1d1e011de310d10b26`.
- La intervención se limita a composición, navegación, ordenación derivada y
  optimización reproducible. No altera contenido histórico canónico.

## 2. REV-023 — TOC PDF

### Defecto

El índice general ocupa las páginas físicas 2–19. La caja numérica de las
secciones resultaba insuficiente desde numeraciones de dos cifras. Se
reprodujeron, entre otros, `10.10Síntesis` (página 4), `14.18Página digital 18`
(página 6), `15.35Hoja enfrentada posterior` (página 12) y
`16.35Respuesta 33` (página 13).

### Causa

El ancho predeterminado de la caja numérica `section` de KOMA-Script no admite
de forma estable esas numeraciones largas.

### Solución

Se fija `tocnumwidth=4.2em` exclusivamente para el nivel `section` mediante
`\RedeclareSectionCommand`. La numeración conserva su semántica, alineación y
enlaces; los títulos reciben una separación estable incluso en `16.46`.

### Pruebas

- `PKG05-TOC-01`: comprueba que el preámbulo contiene la regla de anchura.
- `PKG05-TOC-02`: inspecciona las 18 páginas físicas del TOC renderizado y
  rechaza un número de sección pegado al comienzo de su título.

### Evidencia visual

- Revisión visual final de las páginas 4 y 13, además de recorrido textual de
  las páginas 2–19: sin colisiones ni cambios en los enlaces.
- Capturas temporales baseline y finales en `/tmp/pkg05-baseline/` y
  `/tmp/pkg05-final/`; no se versionan.

**Resultado: REV-023 RESUELTA.**

## 3. REV-024 — glosario alfabético

### Regla de orden

La clave explícita y testeable aplica NFC, compacta espacios y usa `casefold`.
En la clave primaria ignora diacríticos vocálicos y conserva `ñ` como letra
española diferenciada, después de `n` y antes de `o`. La forma visible
normalizada actúa como desempate. El resultado no depende del locale del sistema.

### 28 términos en orden final

`alcavalas`; `añino`; `arbitrio`; `arenta`; `avitadores`; `boto`; `diezmos`;
`entreparedes`; `esquilmo`; `establecimiento del suelo`; `fejes`; `Ferrañales`;
`hijo de familia`; `medio vecino`; `molino venturero`; `negrillos`; `pan`;
`pelo`; `pies de abejas`; `pobre de solemnidad`; `primicia`; `propios`;
`quartal`; `repartimiento`; `Señorío`; `servicio ordinario y extraordinario`;
`utilidad`; `vecera`.

### Paridad HTML/PDF

- HTML y PDF proceden del mismo QMD derivado y muestran exactamente la secuencia
  anterior, tanto en el resumen como en los cuerpos de entrada.
- `PKG05-GLO-01` a `PKG05-GLO-04` verifican la función, la independencia del
  locale, la secuencia completa y su presencia en ambos formatos.

### Fidelidad de contenido

- Se conservan 28/28 lemas, definiciones, fuentes y anclas. Solo cambia el orden
  de presentación.
- `project/20_TRABAJO_EDITORIAL/Glosario.md` permanece intacto.

**Resultado: REV-024 RESUELTA.**

## 4. REV-025 — índices PDF

### Defecto

Los nueve índices carecían del equivalente PDF de `.index-entry`: título,
detalle y localizador de entradas contiguas se percibían pegados, especialmente
en el índice de preguntas y respuestas.

### Solución

Un filtro Lua mínimo envuelve cada
`Div.index-entry` en el entorno LaTeX común `PublicationIndexEntry`. El entorno
añade `0.65\baselineskip` entre entradas y usa una `minipage` para impedir que
una entrada se fragmente dejando campos o localizadores huérfanos.

Una primera corrección con `samepage` fue descartada durante la revisión
intermedia porque aún permitió cuatro comienzos de página huérfanos. La solución
final con `minipage` elimina esos casos y, a la vez, compacta el apéndice.

### 9/9 índices

| Índice | Páginas físicas finales | Estado |
|---|---:|---|
| Onomástico | 298–303 | Conforme |
| Topónimos | 304–306 | Conforme |
| Instituciones | 307–309 | Conforme |
| Oficios | 310–313 | Conforme |
| Medidas | 314–317 | Conforme |
| Productos | 318–322 | Conforme |
| Cargas | 323–325 | Conforme |
| Preguntas y respuestas | 326–329 | Conforme |
| Materias | 330–333 | Conforme |

### Cortes y localizadores

Se revisaron inicio, página intermedia y final de cada índice, así como la
primera entrada de todas sus páginas de continuación. No quedan títulos,
detalles ni localizadores separados de su entrada. Se preservan anclas,
hipervínculos y orden numérico de localizadores.

- `PKG05-IDX-01`: registra el filtro en el formato PDF.
- `PKG05-IDX-02`: comprueba el envoltorio de las nueve clases de entrada.
- `PKG05-IDX-03`: exige el entorno final indivisible y su separación vertical.

**Resultado: REV-025 RESUELTA.**

## 5. DEC-014 / REV-018 — sidebar HTML

### Comportamiento previo

La baseline mostraba las seis partes con clase `show` y
`aria-expanded="true"` en todas las páginas muestreadas. Los alternadores
nativos eran elementos `a` sin `href`: Chrome no podía enfocarlos ni activarlos
con Enter.

### Comportamiento final

`collapse-level: 1` deja abierta solo la parte que contiene la página activa y
colapsa las otras cinco. La entrada activa sigue visible. Se conserva el
componente Bootstrap generado por Quarto y se incorpora un adaptador local de
teclado que dota a sus alternadores de `role="button"`, `tabindex="0"` y
activación por Enter o Espacio.

La revisión real con Chrome abarcó una página de cada una de las seis partes.

### Desktop

- Escritorio, 1440 px: exactamente 1/6 partes abiertas, la activa; ancho de
  desbordamiento global igual a cero.

### 390 px

- Móvil, 390 × 844 px: exactamente el mismo estado, entrada activa visible y
  menú operativo; ancho de desbordamiento global igual a cero.
- Las reglas móviles de corte de URI y código en línea eliminan el
  desbordamiento encontrado durante la revisión, sin cambiar texto ni enlaces.

### Teclado

- El alternador recibe foco; Enter abre y Espacio cierra.
- El foco visible conserva el tratamiento global `:focus-visible` de la
  publicación.

`PKG05-SID-01` a `PKG05-SID-04` comprueban configuración, inclusión del
adaptador, estado de las seis partes y comportamiento responsive/teclado.

**Resultado: DEC-014 / REV-018 RESUELTA.**

## 6. REV-026 — auditoría de peso

### PDF baseline

El render intermedio ya contenía las cuatro correcciones obligatorias:

PDF: 341 páginas; 74.039.786 bytes; SHA-256
`2f7028fb6c0e77144d9db0f3d8539d2a28a94a9322a2e702db1138580652d8c4`.

### Web baseline

30 documentos HTML; 77.144.770 bytes sin PDF: imágenes 73.290.652; HTML
2.097.354; CSS 616.877; JavaScript 393.315; fuentes 176.200; otros 570.372.

### Desglose gráfico y tipográfico

- 53 imágenes PNG en PDF: 18 facsímiles completos y 35 recortes F3.
- Peso aproximado de objetos de imagen PDF antes de optimizar: 73.228.288
  bytes; facsímiles 35.009.536 y recortes 38.218.752.
- Peso exacto web antes de optimizar: facsímiles 35.063.833 bytes y recortes
  38.226.819 bytes.
- Resolución efectiva: facsímiles completos, aproximadamente 308–427 ppp;
  recortes al 28 %, aproximadamente 591–682 ppp.
- 14 fuentes, todas embebidas y subseteadas.
- No hay mapas insertados ni otros gráficos. No existen grupos duplicados por
  SHA-256 entre los 53 PNG publicados.

## 7. Ensayos de optimización

| ID | Técnica | PDF antes | PDF después | Web antes | Web después | Calidad | Reproducible | Decisión |
|---|---|---:|---:|---:|---:|---|---|---|
| OPT-01 | Pillow `optimize=True` en las 53 imágenes | 74.039.786 | N/E: rechazada en puerta de activos | 77.144.770 | 73.956.075 en árbol experimental | Sin pérdida, identidad de píxeles | Sí | RECHAZAR: empeora los 18 facsímiles en 46.308 bytes y añade búsqueda/coste innecesarios |
| OPT-02 | PNG `compress_level=9` solo en los 35 recortes | 74.039.786 | 70.802.128 | 77.144.770 | 73.910.522 | Sin pérdida, identidad de píxeles | Sí | ACEPTAR |

OPT-01 redujo el conjunto temporal de imágenes de 73.290.652 a 70.101.957
bytes (−3.188.695; −4,3508 %), pero se detuvo antes del render PDF. OPT-02
reduce aisladamente los recortes de 38.226.819 a 34.992.490 bytes
(−3.234.329; −8,4609 %). En la comparación PDF completa de OPT-02 también
interviene la sustitución final de `samepage` por `minipage`; el A/B exacto de
activos y del bundle web aísla la ganancia de compresión.

No se aplican reducciones de resolución, conversión con pérdida ni mutaciones
posteriores al render. El entorno no ofrece `qpdf`, Ghostscript, MuPDF ni
optimizadores PNG externos; no se incorpora una dependencia nueva para una
ganancia especulativa. DEC-034 se cumple deteniendo la optimización cuando queda
una mejora simple, segura, medible y reproducible.

## 8. Optimización aceptada

Los generadores guardan únicamente los 35 recortes PNG con nivel de compresión
9. El prototipo vertical usa la misma regla, por lo que conserva la igualdad
binaria exigida por F3 entre el recorte aprobado y el global. `PKG05-REV026-01`
verifica la regla. Las dimensiones, color, alpha y matriz de píxeles no cambian.

## 9. Peso final

- PDF final: 333 páginas; **70.802.128 bytes**; SHA-256
  `c966f68784c9a3426ef451bf3ef679073ebb4891cac294e7d4174032f541e1c4`.
- Reducción frente a la baseline corregida: 3.237.658 bytes (4,3729 %).
- Reducción frente al PDF de partida PKG-04/F3: 3.239.558 bytes (4,3753 %).
- Web final sin PDF: **73.910.522 bytes**, 3.234.248 bytes menos (4,1924 %).
- Desglose web final: imágenes 70.056.323; HTML 2.097.354; CSS 616.958;
  JavaScript 393.315; fuentes 176.200; otros 570.372 bytes.
- Imágenes PDF finales, aproximación por objetos: 69.991.424 bytes; facsímiles
  35.009.536 y recortes 34.981.888.
- Árbol `_book` completo: 144.712.650 bytes.

Este render de validación no constituye candidata formal.

La diferencia de 341 a 333 páginas procede de la corrección final del modelo de
entradas de índices (`samepage` intermedio frente a `minipage` final), no de una
supresión de contenido.

## 10. Reproducibilidad

Dos preparaciones consecutivas anteriores a la última adaptación del prototipo
ya produjeron 83 salidas con el mismo manifiesto SHA-256
`8c7bf0d89f442fd2b5f35a9fd61d3d4dc2b2d967213ebbeefbbbb391394be3b2`.
Tras armonizar la compresión del prototipo se repitió la preparación y se
comparó el árbol derivado completo antes/después: 111 archivos, manifiesto
SHA-256 `3d2e76872d1028c5407d742cf62609047af36f6d8ca531e30eee3b8850f6aa82`,
idéntico byte a byte. Los directorios temporales ocultos preexistentes quedan
fuera del manifiesto y no se publican.

## 11. Tests

- Suite baseline: `616 passed`.
- Se añaden 14 pruebas PKG-05 con identificadores explícitos: 2 TOC, 4 glosario,
  3 índices, 4 sidebar y 1 rendimiento.
- Suite específica final: `14 passed in 3.96s`.
- Suite focal final de publicación: `175 passed in 54.81s`.
- Suite completa final: `630 passed in 57.00s`.
- No se añaden omisiones, `xfail` ni excepciones.

## 12. Validadores

- `validate_project.py .`: PASS, workspace GitHub v2 coherente.
- `check_sources.py`: PASS; 5 fuentes, 35 unidades, 40 respuestas, 28 lemas,
  conteos D/C/I/E/L, 20 cálculos y nueve índices coherentes; hash manuscrito
  verificado.
- `validate_publication.py`: PASS estático.
- `validate_publication.py --rendered`: PASS sobre artefactos HTML y PDF.
- Comprobador de cartografía: PASS; no se introduce cartografía.
- `quarto check`: Quarto 1.7.31, Pandoc 3.6.3, TinyTeX 2026 y Chrome disponibles.
- `compileall` y `git diff --check`: PASS.

## 13. Integridad y alcance

- `project/` permanece byte a byte fuera del diff.
- No se modifican bibliografía, contenido histórico, cartografía ni documentos
  generales de estado.
- No se incorporan PDF, credenciales, manuscritos ni fuentes restringidas al
  control de versiones.
- `publication/generated/` sigue sin archivos rastreados; sus salidas se
  regeneran mediante la preparación.
- No se abren INC-BIB-001/002, Contexto histórico, PKG-06, despliegue global ni
  fase 6B.
- No se integra, publica, etiqueta ni crea release. Esta rama no constituye una
  candidata formal.

## 14. Resultado

- REV-023: **RESUELTA**.
- REV-024: **RESUELTA**.
- REV-025: **RESUELTA**.
- REV-018 / DEC-014: **RESUELTA**.
- REV-026 / DEC-034: **RESUELTA CON OPTIMIZACIÓN**.

PKG-05 queda técnicamente cerrado en su rama aislada y pendiente únicamente de
revisión e integración por la autoridad correspondiente.

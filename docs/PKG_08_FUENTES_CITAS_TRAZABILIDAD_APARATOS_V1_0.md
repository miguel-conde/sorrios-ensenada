# PKG-08 — Fuentes, citas, trazabilidad y aparatos

## 1. Estado inicial

PKG-08 parte de `feature/quarto-book` en
`8a532bc4f7f576d8855c66d946247122ebd3fa38`, con `GATE-01 = PASS` y la suite
en `585 passed, 9 failed, 36 errors`. Los fallos y errores no eran una
regresión aceptada: expresaban la desincronización deliberada entre el estado
canónico posterior a INC-BIB-001/002 y `publication/`, asignada
contractualmente a este paquete.

La operación se ejecuta en la rama aislada
`pkg-08/sources-traceability-apparatus-v1`, sin upstream y sin publicación
remota.

## 2. SYNC-08

`SYNC-08 = PASS`.

### Canonical commit

El árbol `project/` de
`a162fad1792aa9b3804a5499d348ab355e5ce574` coincide exactamente con el árbol
`project/` de la base de PKG-08. Ese commit es, por tanto, la procedencia
canónica que representa las fuentes vigentes.

### Provenance

`publication/meta/publication.yml` declara `a162fad...` como commit base. Se
actualizaron también el blob del Glosario y las versiones de las fuentes sin
relajar la comprobación de procedencia.

### Versiones

- Estudio Histórico: 1.3.
- Registro de afirmaciones y cálculos: 1.3.
- Parser del Registro: 1.3.
- Glosario: 28 entradas; `Contexto histórico` continúa fuera de la vista
  publicada.

### TRA-006

La entrada retirada desaparece de los capítulos 11 y 13, del front matter, de
los validadores, de los tests y de la matriz vigente. `TRA-005` y el dato local
de R29 permanecen intactos.

### DEM-005

El capítulo 6, el parser y la matriz adoptan la formulación canónica limitada
a libros personales, cabezas de casa o familias, composición doméstica y
viudas con casa abierta como posibles cabezas de casa. No se deriva de ello
una equivalencia entre viuda y medio vecino ni un coeficiente demográfico.

### Suite recuperada

Tras la sincronización, antes de añadir el aparato de PKG-08, la suite quedó en
`630 passed, 0 failed, 0 errors`. Los cuatro derivados de Fase 4D se
regeneraron y `publication/generated/` permaneció ignorado.

## 3. Universo bibliográfico

El universo activo se obtuvo de las 24 entradas E/E-I vigentes del Registro,
sus usos en los capítulos 3 y 5–13 y la matriz. La clase A entra en la
bibliografía; la C permanece como enlace técnico o institucional en su lugar
de uso; la D queda retirada. No se identificó una fuente de clase B que
debiera conservarse en la bibliografía pública sin uso vigente.

| Fuente / clave estable | Uso vigente | E-ID | Capítulo o aparato | Datos usados | Clase / bibliografía |
|---|---|---|---|---|---|
| `jularconflictos` | contexto medieval del topónimo | TOP-004 | cap. 3, matriz | repositorio | A / sí |
| `santanovalbuena2022documentos` | forma documental medieval | TOP-005 | cap. 3, matriz | PKG-02 | A / sí |
| `sanchezbadiola2019nobiliario` | testimonio de 1601 | TOP-006 | solo matriz | PKG-02 | A / sí |
| `pares1715santibanez` | testimonio de 1715 | TOP-007 | cap. 3, matriz | repositorio | A / sí |
| `relacionparroquial1768` | topónimo, jurisdicción y demografía | TOP-008, JUR-007, DEM-006 | caps. 3, 5, 6; matriz | repositorio | A / sí |
| `gaceta1864sorribos` | forma de 1831 publicada en 1864 | TOP-009 | cap. 3, matriz | repositorio | A / sí |
| `alvarezbalbuenatoponimia` | serie toponímica y marco territorial | TOP-010, JUR-007 | caps. 3, 5; matriz | repositorio | A / sí |
| `ayuntamientosantamariaordassantibanez` | forma administrativa actual | TOP-011 | cap. 3, matriz | repositorio | A / sí |
| `pousadieguez2022juzgados` | señorío y realengo | JUR-008 | cap. 5, matriz | PKG-02 | A / sí |
| `paresconde1742` | identificación del conde de Luna | JUR-008 | cap. 5, matriz | repositorio | A / sí |
| `parestituloabogado` | identificación del escribano | JUR-009 | cap. 12, matriz | repositorio | A / sí |
| `camarerobullon2002catastro` | organización de libros personales | DEM-005 | cap. 6, matriz | PKG-02 | A / sí |
| `castanoalvarez2017apuntes` | metrología agraria | TER-011 | cap. 7, matriz | PKG-02 | A / sí |
| `bartolomebartolome2001comercio` | contexto regional del lino | AGR-011 | cap. 7, matriz | PKG-02 | A / sí |
| `sanchezlopezdevinuesa2001cultivos` | cultivos de ribera | AGR-012 | caps. 7–8, matriz | PKG-02 | A / sí |
| `riescochueca2013lexico` | léxico agrario | AGR-013 | caps. 7–8, matriz | PKG-02 | A / sí |
| `cortizoalvarez1984ganado` | contexto ganadero | GAN-008 | cap. 8, matriz | PKG-02 | A / sí |
| `zapicogutierrez2016molinos` | molinos leoneses | HID-008 | cap. 9, matriz | PKG-02 | A / sí |
| `hernandezcubero2018recursos` | molienda y recursos | HID-008 | cap. 9, matriz | PKG-02 | A / sí |
| `reycastelao1985voto` | Voto de Santiago | FIS-013 | cap. 10, matriz | PKG-02 | A / sí |
| `mazazorrilla1982pobreza` | hospitalidad vallisoletana | FIS-014 | caps. 11–12, matriz | PKG-02 | A / sí |
| `paresmesta` | institución de la Mesta | FIS-015 | caps. 11–12, matriz | repositorio | A / sí |
| `garciagarcia1986haciendas` | haciendas municipales | FIS-016 | cap. 11, matriz | PKG-02 | A / sí |
| `caputvallis2008catastro` | comparación de hacienda concejil | FIS-017 | cap. 11, matriz | PKG-02 | A / sí |
| URLs de navegación, catálogo o ayuda documental | acceso institucional directo | — | caps. 1–4, glosario y transcripción | repositorio | C / no autónoma |
| BIB-012, antigua fuente de la vecera | ningún uso vigente legítimo | TRA-006 retirada | dossiers históricos de PKG-02 | PKG-02 | D / no |

## 4. references.bib

`publication/references.bib` contiene 24 registros con claves legibles y
estables: 12 `article`, 8 `online`, 2 `thesis`, 1 `book` y 1 `misc`. Quince
registros verificados en PKG-02 incorporan la fecha real de consulta
`2026-10-11`; los otros nueve no reciben una fecha inventada. Títulos,
autorías, fechas, contenedores, páginas, DOI y URL proceden exclusivamente de
los dossiers de PKG-02 o de metadatos ya presentes en el repositorio.

## 5. BIB-012

BIB-012 queda fuera de `references.bib`: tras retirar TRA-006 no conserva un
uso activo legítimo. No se cita, no respalda `vecera` y solo permanece en los
dossiers históricos y técnicos que documentan PKG-02.

## 6. BIB-015

BIB-015 se publica como `camarerobullon2002catastro` y se cita junto a
DEM-005. Su alcance queda limitado a la organización de los libros
personales, las cabezas de casa o familias, la composición doméstica y las
viudas con casa abierta como cabezas de casa. El capítulo y los tests excluyen
expresamente su uso para `medio vecino`, viuda = medio vecino, coeficientes
demográficos o una regla general aplicable a Sorribos.

## 7. CIT-B/C

Se implementa la política híbrida aprobada: las afirmaciones externas
relevantes reciben una cita bibliográfica próxima; el ID E enlaza con la
matriz cuando mejora la lectura; la matriz conserva declaración, evidencia,
cautela, referencia normalizada y retorno al capítulo; la bibliografía pública
identifica la fuente desde una única base BibTeX. No se añaden citas a cada D,
C o frase editorial.

## 8. Citas próximas

| Capítulo | Cobertura añadida |
|---|---|
| 3 | TOP-004, TOP-005 y TOP-007–TOP-011; TOP-006 excluida deliberadamente |
| 5 | JUR-007 y JUR-008 |
| 6 | DEM-005 y DEM-006 |
| 7 | TER-011 y AGR-011–AGR-013 |
| 8 | GAN-008, AGR-012 y AGR-013 |
| 9 | HID-008 |
| 10 | FIS-013 |
| 11 | FIS-014–FIS-017 |
| 12 | JUR-009, FIS-014 y FIS-015 |
| 13 | síntesis acotada de las E de contexto ya introducidas |

## 9. D/C/I/E/L

La matriz contiene 111 anchors únicos derivados directamente de los IDs
canónicos (`evidencia-<id-en-minúsculas>`). El filtro Lua compartido convierte
las marcas D/C/I/E/L ya visibles en enlaces hacia esos anchors en HTML y PDF.
Los usos se derivan del front matter `evidence` de los capítulos 3 y 5–13; el
generador localiza la sección pertinente y produce retornos compactos con
fragmento real. Las 24 entradas externas vigentes tienen mapeo bibliográfico.
No se creó una tabla manual paralela de más de cien destinos.

## 10. TOP-006

`TOP-006 = SOLO MATRIZ`. Conserva su referencia bibliográfica dentro de la
matriz, muestra `Uso en el libro: —` como excepción deliberada y no aparece en
la narrativa ni en la secuencia cronológica del capítulo 3.

## 11. QA1

El aparato «Cuestiones abiertas» contiene exactamente nueve cuestiones:
QA-001, QA-002, QA-003, QA-004, QA-005, QA-009, QA-011, QA-012 y QA-013. Se
agrupan en población y hogares, producción y mercado, metrología, y derechos y
obligaciones pendientes. Cada una distingue qué se sabe y qué no, y enlaza al
capítulo y a su entrada LIM en la matriz. No incorpora QA0, QA2 ni QA3.

## 12. Historia intelectual/editorial

La pieza breve «Historia intelectual y editorial», situada en la Parte VI,
explica al lector la relación entre manuscrito, transcripción, Edición Crítica
3.6, modernización 1.3, Estudio y Registro 1.3, composición 0.6 y edición
Quarto. Separa fuente, edición, interpretación y publicación; no presenta 0.6
como autoridad y no contiene ramas, commits, tests ni historia técnica.

## 13. Modelos de cita

| Objeto | Familia |
|---|---|
| Volumen completo | Volumen |
| Facsímil | Localización documental |
| Página del manuscrito | Localización documental |
| Folio | Localización documental |
| Unidad | Localización documental |
| Respuesta | Localización documental |
| Transcripción paleográfica | Transcripción |
| Edición modernizada | Modernizada |
| Capítulo histórico | Estudio |
| Entrada D/C/I/E/L | Matriz |
| Fuente externa | Bibliográfica |

La cobertura es 11/11 mediante siete familias. La autoría usa «Miguel Conde
de Simón» y la forma bibliográfica «Conde de Simón, Miguel». Fecha final,
versión aceptada y URL canónica permanecen como marcadores explícitos; no se
inventa ISBN.

## 14. Bibliografía pública

La página «Bibliografía» está en la Parte VI y usa `nocite: @*` y el
contenedor nativo `#refs`. HTML y PDF consumen el mismo
`publication/references.bib`; no existe lista manual, JavaScript ni sistema
paralelo.

## 15. Tests

Se añadieron pruebas específicas SYNC-01–07, BIB-01–07, TRACE-01–06, QA1,
modelos de cita, historia editorial y diferimiento del `Contexto histórico`.
Se actualizaron, sin relajar contratos, las pruebas afectadas de Fase 4D, 5A,
5B, 6A y prototipo.

- Suite focal (Fase 4D, 5A, 5B, 6A, PKG-04, GF3, PKG-05, PKG-08 y
  prototipo): `538 passed, 0 failed, 0 errors`.
- Suite completa: `650 passed, 0 failed, 0 errors`.
- No se añadieron skips ni xfails para ocultar incidencias.

## 16. Render HTML

El libro HTML completo consta de 34 documentos y pasa el validador renderizado
y la auditoría de calidad. Se revisaron los capítulos 3, 6, 11 y 13, la matriz,
QA1, «Cómo citar» y la bibliografía. La emulación real por Chrome DevTools a
390 × 844 px confirmó en las ocho vistas `innerWidth = documentScrollWidth =
bodyScrollWidth = 390`, un solo H1, ninguna numeración posterior al capítulo 16
y desbordamiento horizontal cero. La regla responsive específica de `#refs`
evita que las URL bibliográficas largas expandan el viewport.

## 17. Render PDF

La composición técnica no es una candidata formal. El PDF definitivo tiene
345 páginas, 70.861.784 bytes y SHA-256
`734818090b7671b3fb395e02e29144178d4b1e5df9c6a91e77bc2421ba2fbd22`.
La inspección visual cubrió los capítulos 3, 6, 11 y 13, la matriz, las dos
páginas de QA1, los modelos de cita, la bibliografía y sus entradas largas;
también se comprobaron índices, TOC, cruces internos y la regresión F3. Los
nuevos aparatos comienzan en las páginas 303, 305, 306 y 308.

## 18. Reproducibilidad

Dos preparaciones consecutivas del estado final produjeron hashes idénticos
para los 83 archivos relevantes de `publication/generated/`. El directorio
continúa ignorado y ninguno de sus archivos se versiona.

## 19. Integridad canónica

PKG-08 consume la autoridad vigente sin modificarla. El diff de `project/`
contra `8a532bc...` es vacío. F3 y PKG-05 permanecen cubiertos por sus tests;
los mapas de PKG-03 no se insertan; no se inicia PKG-06 ni PKG-09; no se
versionan PDF, HTML, `_book/`, derivados ni capturas.

## 20. Limitaciones/pendientes

- La fecha, versión final, URL canónica e identidad final siguen diferidas a
  PKG-09/13.
- `Contexto histórico` del Glosario continúa sin presentación editorial.
- Los mapas aprobados siguen pendientes de PKG-07.
- Este render es técnico y no sustituye la candidata formal de PKG-10.
- La rama requiere revisión e integración separada; no se publica ni integra
  durante PKG-08.

## 21. Resultado

`APTO`.

PKG-08 queda técnicamente apto para revisión e integración. La publicación
está resincronizada con `project/`; bibliografía, CIT-B/C, trazabilidad y
aparatos están implementados; los validadores, el render multiformato y las
suites focal y completa están en PASS.

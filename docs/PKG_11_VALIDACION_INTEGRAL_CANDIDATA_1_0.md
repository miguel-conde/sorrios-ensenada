# PKG-11 — Validación integral independiente de la candidata 1.0

**Estado:** `PKG-11: CANDIDATA 1.0 VALIDADA INTEGRALMENTE`<br>
**Rama de auditoría:** `pkg-11/integral-candidate-validation-v1`<br>
**Base de la auditoría:** `a9f0e206c665e9251f20abc7741c754ceebad38b`<br>
**Fecha técnica de auditoría:** 17 de octubre de 2026<br>
**Naturaleza:** validación independiente; no es aceptación humana, tag ni release

## 1. Candidata auditada

| Elemento | Valor comprobado |
|---|---|
| Commit fuente de la candidata | `a666e878eb6672bee337ac4a2b6f0410ae8e0872` |
| Commit PKG-10 | `d02b9fbf0e17625f87d19ebe12bf36c1ce633c80` |
| Provenance canónico | `a162fad1792aa9b3804a5499d348ab355e5ce574` |
| Árbol `project/` | `a8ccb6d783e51aafb6493fed9791097d0a678086` |
| Manifest HTML PKG-10 | `74b49ecd3f9261bf8153a499ef0bbe59ffd78d24935b7647c3e65be0d37f047e` |
| PDF PKG-10 | 355 páginas; 71.020.397 bytes; `7361b491c8095f55a6bb6add3445924b52db6518f49610342cfbbf5a946f4771` |

El dossier y el cierre de PKG-10 son coherentes entre sí. Entre el commit
fuente y la base de PKG-11 solo hay manifest, dossiers, tests y estado
documental: `project/` y las fuentes renderizables de `publication/` son
idénticos.

## 2. Contrato

Se aplicó literalmente el alcance de PKG-11 fijado en
`PLAN_EJECUCION_V1_0.md`: suite completa; integridad canónica;
reproducibilidad; enlaces, citas, bibliografía y anclas; D/C/I/E/L; glosario,
índices y TOC; HTML y PDF; teclado y vista estrecha; imágenes y equivalentes
accesibles; mapas, cronología y diagrama; facsímil, transcripción y F3; peso;
no regresión histórica; y ausencia de identidad de desarrollo.

La decisión se limita a PASS/FAIL. No se corrigió la candidata ni se amplió
su alcance.

## 3. Independencia y reconstrucción

La auditoría eliminó previamente `_book/`, `generated/` y la caché local de
Quarto. La reconstrucción partió del entorno virtual del repositorio y de la
réplica local verificada del manuscrito, exterior al checkout.

- Python 3.12.10; pytest 9.1.1; Quarto 1.7.31; Pandoc 3.6.3;
- preparación completa: 5 fuentes, 35 unidades y manuscrito verificados;
- derivados: 83 archivos, 78.448.397 bytes;
- manifest ordenado de derivados:
  `f4e50559edd884bcbd106f32ffa494c9ca373c68f490aec06474f62ff5623e9e`;
- suite completa autoritativa tras la preparación: `678 passed`, 0 fallos y
  0 errores;
- reconstrucción completa HTML/PDF: PASS.

No se reutilizó como objeto de validación ningún artefacto de PKG-10.

## 4. Comparación con el manifest de PKG-10

| Magnitud | PKG-10 | Reconstrucción PKG-11 | Resultado |
|---|---:|---:|---|
| Documentos HTML | 39 | 39 | PASS |
| Archivos del bundle sin PDF | 117 | 117 | PASS |
| Bytes del bundle sin PDF | 74.567.798 | 74.567.798 | PASS |
| Bytes de documentos HTML | 2.638.399 | 2.638.399 | PASS |
| Páginas PDF | 355 | 355 | PASS |
| Bytes PDF | 71.020.397 | 71.020.397 | PASS |

El conjunto y tamaño de artefactos, la estructura, el contenido visible y la
paginación coinciden. Los hashes brutos de HTML y PDF difieren por
nondeterminismo técnico no semántico, analizado en las secciones siguientes.

## 5. Reproducibilidad HTML

El manifest ordenado de la salida auditada es
`86f32e8b48e6ee46ebd30feb0d96bc85439f034485cbbd6a00db3ebd7b55b9d9`,
frente a `74b49ecd…` en PKG-10. La diferencia quedó acotada a la serialización
del orden de atributos HTML en dos documentos; por ejemplo, `alt` y
`data-fig-pos` intercambian posición sin cambiar nombre, valor, DOM, recurso,
texto alternativo ni comportamiento. Ejecuciones diagnósticas produjeron las
combinaciones de orden posibles conservando exactamente los 117 archivos y
74.567.798 bytes.

La estructura, enlaces, anchors, DOM funcional, contenido, assets y salida
visual son equivalentes. Los validadores estático, renderizado, de release y
de calidad HTML pasan sin incidencias. Se clasifica como nondeterminismo de
serialización inocuo, no como diferencia editorial ni defecto bloqueante.

## 6. Reproducibilidad PDF

La reconstrucción auditada produce 355 páginas y 71.020.397 bytes, con
SHA-256
`8862d2e3020f23b57e79b7331a7d6f5ba69d829455e5076f8058d2701020c1fb`,
frente a `7361b491…` en PKG-10.

La clasificación se demostró mediante dos construcciones diagnósticas:

- extracción `pdftotext -layout` idéntica byte a byte;
- 53 imágenes extraídas con manifest idéntico;
- 23 variantes de fuente idénticas, embebidas y con Unicode;
- páginas representativas 1, 22, 23, 25, 36, 37, 44, 90, 99, 120, 221,
  247, 270, 317, 319 y 355 rasterizadas con hashes idénticos;
- dimensiones, paginación, enlaces y estructura validados;
- diferencias binarias limitadas a timestamps de construcción e IDs del
  tráiler PDF.

No existe diferencia visible, textual, gráfica, tipográfica, estructural ni
editorial. El SHA distinto es exclusivamente metadata técnica no semántica y
cumple la excepción de reproducibilidad prevista por el contrato de PKG-11.

## 7. Canonical y trazabilidad

- `project/` coincide exactamente con el árbol declarado y permanece intacto;
- Registro, Estudio, Glosario y publicación son compatibles con sus snapshots;
- 111 anchors D/C/I/E/L son únicos y sus retornos son válidos;
- 24 fuentes activas corresponden a 24 registros BibTeX, sin claves huérfanas;
- CIT-B/C es coherente y resoluble;
- `TOP-006` aparece solo en la matriz;
- `TRA-006` está ausente de la publicación vigente;
- `DEM-005` conserva el estado canónico;
- BIB-012 no se usa como autoridad;
- BIB-015 solo sostiene el contexto doméstico autorizado;
- QA1: 9/9; objetos de cita: 11/11.

Resultado: PASS.

## 8. Cobertura documental

La reconstrucción contiene 18/18 páginas de facsímil, 35/35 unidades, 40
respuestas, transcripción completa, edición modernizada, glosario de 28
entradas, matriz de evidencia, cuadros y concordancia. Están presentes los
nueve índices previstos, la bibliografía, cuestiones abiertas, historia
intelectual/editorial, «Cómo citar» y colofón.

Los validadores confirman los recuentos de índices vigentes: 21/9/7/12/12/27/
15/40/21. Resultado: PASS.

## 9. F3

HTML conserva el facsímil completo, los crops aprobados, lightbox y navegación
bidireccional. PDF conserva el facsímil completo, localizadores al 28 %,
página/posición y navegación prevista. REV-023–026 siguen intactas. No se
reabre la aprobación humana H1–H5/P1–P8. Resultado: PASS.

## 10. Aparato visual

Cronología, diagrama económico, mapa regional y mapa local están presentes,
legibles y acompañados de captions, textos alternativos, procedencia y
atribución. Los mapas no añaden interpretación histórica; el diagrama deriva
del capítulo 13; `TOP-006` no entra en la cronología. Se preservan las
exclusiones DEC-023/024. Resultado: PASS.

## 11. HTML

Navegación, sidebar, búsqueda, retornos, enlaces internos, matriz, citas,
bibliografía, anchors, imágenes, captions, alt, tablas e índices pasan los
validadores. La emulación efectiva a 390 px dio `scrollWidth = clientWidth =
375` para el viewport útil, sin overflow horizontal, tanto en la landing como
en una página de facsímil. La navegación por teclado representativa es
operativa y no aparece la identidad «edición en desarrollo».

Revisión visual representativa: PASS.

## 12. PDF

Se validaron estructuralmente las 355 páginas y se inspeccionaron portada,
TOC, preliminares, cronología, mapas, diagrama, facsímil, F3, transcripción,
modernización, glosario, matriz, QA1, modelos de cita, bibliografía, índice de
materias y colofón. No hay cortes, colisiones, páginas anómalas, imágenes
ausentes ni regresiones de composición. Texto seleccionable, tablas, entradas
largas y jerarquía son legibles. Resultado: PASS.

## 13. Accesibilidad

Estructura de encabezados, enlaces comprensibles, textos alternativos,
captions, sidebar, navegación por teclado, contraste, uso no exclusivo del
color y responsive básico satisfacen las comprobaciones existentes. La
auditoría no atribuye una certificación externa no contratada. Resultado:
PASS.

## 14. Diferimientos

- Prólogo: **PLACEHOLDER CONTROLADO PENDIENTE DE REDACCIÓN PERSONAL**; sigue
  inequívocamente marcado y no se presenta como definitivo.
- Fecha exacta: diferida y no inventada; el año visible es 2026.
- URL canónica: diferida y no inventada.
- ISBN: ausente y no bloqueante mientras no exista.

Resultado: PASS — diferimientos autorizados.

## 15. Matriz integral

| Área | Prueba | Resultado | Evidencia | Bloqueante |
|---|---|---|---|---|
| Reproducibilidad | Reconstrucción limpia y comparación de manifests | PASS | Mismo conjunto/tamaño; nondeterminismo no semántico demostrado | No |
| Canonical | Árbol `project/` y snapshots | PASS | `a8ccb6d…`; validadores de proyecto y fuentes | No |
| Contenido | Recuentos y aparatos | PASS | 18 páginas, 35 unidades, 40 respuestas, 28 términos, 9 índices | No |
| F3 | HTML/PDF y REV-023–026 | PASS | Facsímil, crops/localizadores y navegación | No |
| Bibliografía/trazabilidad | CIT-B/C, BibTeX y D/C/I/E/L | PASS | 24/24 fuentes; 111 anchors; 11/11 citas | No |
| Aparato visual | Cronología, diagrama y mapas | PASS | Validadores y revisión visual | No |
| Preliminares | Landing, portada, créditos y rutas | PASS | Revisión multiformato | No |
| Identidad/licencia | Metadatos, terceros, IA y colofón | PASS | Validación PKG-09 preservada | No |
| HTML | Estructura, navegación, enlaces y responsive | PASS | 39 documentos; checks integrales; viewport 390 px | No |
| PDF | Estructura, contenido y composición | PASS | 355 páginas; validación profunda y muestra visual | No |
| Accesibilidad | Alt, captions, teclado, contraste | PASS | Auditorías existentes y revisión representativa | No |
| Diferimientos | Prólogo, fecha, URL e ISBN | PASS — diferimiento autorizado | Marcadores explícitos y ausencia de datos inventados | No |
| Integridad Git | Fuentes, derivados y estado | PASS | Fuentes intactas; derivados ignorados | No |

## 16. Incidencias

No se detectaron defectos bloqueantes. Se registran dos observaciones técnicas
no editoriales:

1. `OBS-PKG11-HTML-01`: orden no estable de atributos equivalentes en dos
   documentos HTML; no cambia DOM, contenido, accesibilidad ni presentación.
2. `OBS-PKG11-PDF-01`: timestamps e IDs de tráiler variables; texto, imágenes,
   fuentes, páginas y rasterización son equivalentes.

Ninguna observación requiere corregir fuentes o candidata para autorizar
PKG-12. No se creó operación `CR-V1-*`.

## 17. Decisión

`PKG-11: CANDIDATA 1.0 VALIDADA INTEGRALMENTE`

La candidata presenta 0 defectos bloqueantes; suite y validadores están en
PASS; la reconstrucción es editorial y estructuralmente equivalente; HTML y
PDF son aptos; la integridad canónica se conserva; y solo permanecen los
diferimientos autorizados.

Los artefactos reconstruidos permanecen locales e ignorados. No se versionan
`publication/generated/`, `_book/`, PDF, HTML ni capturas. PKG-12 no se inició
y no hubo push, tag, release ni Fase 6B.

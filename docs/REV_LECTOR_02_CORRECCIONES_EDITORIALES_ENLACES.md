# REV-LECTOR-02 — Correcciones editoriales y de enlaces

## 1. Baseline

- Operación: E3 — REV-LECTOR-02.
- Base: `a9ffe2cd67238323f152d7c709e81176d3f673a0`.
- Rama: `rev-lector-02/reader-link-corrections-v1`.
- Autoridades canónicas bajo `project/`: intactas.
- Resultado: corrección conjunta y localizada de los hallazgos E1 y E2.

## 2. Resolución de RL-001–RL-023

| ID | Hallazgo | Resolución |
|---|---|---|
| RL-001 | Repetición del autor en Créditos | Un único bloque autoral reúne las cuatro responsabilidades aprobadas. |
| RL-002 | Declaración extensa de IA duplicada en Créditos | Créditos remite al colofón; la declaración HUM-01B permanece íntegra allí. |
| RL-003 | «Dos operaciones» | Sustituido por «dos líneas de trabajo». |
| RL-004 | Versión visible de la edición crítica | Retirada de la prosa pública; permanece en metadata técnica. |
| RL-005 | Versión visible de la edición modernizada | Retirada de la prosa y de los modelos de cita; permanece en metadata técnica. |
| RL-006 | Versiones visibles del estudio y el Registro | Retiradas de la prosa; D/C/I/E/L y su autoridad se conservan. |
| RL-007 | «Quarto» fuera de su contexto técnico | Retirado del discurso metodológico e histórico; se conserva en el colofón. |
| RL-008 | Rutas `publication/content/` y `publication/generated/` | Sustituidas por la distinción conceptual entre contenido editorial y derivados reproducibles. |
| RL-009 | `front matter` como explicación al lector | Sustituido por una declaración de fuentes e identificadores de evidencia. |
| RL-010 | Detalles de Git/GitHub en el capítulo metodológico | Retirados; no se publica URL del repositorio privado. |
| RL-011 | Composición/PDF 0.6 en la historia pública | Retirada; la historia intelectual describe la evolución editorial. |
| RL-012 | «Fuentes canónicas del proyecto» | Reformulado como jerarquía de autoridad de esta edición. |
| RL-013 | «El proyecto adoptó» y «futuro capítulo 16» | Reformulado en presente editorial. |
| RL-014 | Introducción técnica de la transcripción | Sustituida por una presentación de 35 unidades, ayudas visuales y autoridad textual. |
| RL-015 | Versiones del Manual, incidencias e instrucciones internas en la transcripción | Transformadas en criterios editoriales legibles sin alterar la transcripción paleográfica. |
| RL-016 | Rasterización repetida dieciocho veces | Resolución indicada una sola vez; cada página conserva solo su posición en la serie. |
| RL-017 | `casefold`/NFKD en los índices | Sustituido por una explicación alfabética dirigida al lector; la ordenación no cambia. |
| RL-018 | Nombre interno `references.bib` | Sustituido por una descripción bibliográfica pública. |
| RL-019 | Clase interna QA1 | Retirada del discurso; se conservan los nueve IDs `QA-*`. |
| RL-020 | `Registro 1.3` y «nivel canónico» en matriz/cuadros | Sustituidos por «formulación controlada» y clasificación `C`; D/C/I/E/L permanece intacto. |
| RL-021 | Estados temporales «en esta fase» | Retirados de glosario e índices generados mediante adaptación pública reproducible. |
| RL-022 | Versiones internas en «Cómo citar» | Retiradas; se conserva únicamente la versión bibliográfica pública 1.0. |
| RL-023 | Lenguaje de candidata/release y falta de canal de corrección | Colofón reformulado y nueva sección «Correcciones y contacto» incorporada. |

## 3. Correcciones E2

- El DOI inválido `10.17811/er.0.1984.71-94` se sustituyó por el destino
  institucional documentado de la Universidad de Oviedo.
- Las seis URLs antiguas de PARES bajo `mcu.es` se normalizan a
  `pares.cultura.gob.es`: cuatro en `references.bib` y dos procedentes de
  fuentes canónicas mediante la adaptación reproducible de publicación.
- El bitstream directo de GREDOS `10366/151409` se sustituyó en la matriz por
  la ficha institucional; el handle persistente continúa en la bibliografía.
- Los cuatro enlaces del capítulo 9 apuntan ya en la fuente a los capítulos
  14–16 y a `HID-001` en la matriz; se retiró su dependencia del postprocesado.
- Se mantienen 24 fuentes activas y 24 registros BibTeX, sin reintroducir
  BIB-012 ni TRA-006; BIB-015 y TOP-006 conservan su alcance aprobado.

## 4. Enlaces conservados por bloqueo o timeout

- La referencia del MAPA se conserva: LINK-01 registró error TLS y no acreditó
  un reemplazo institucional.
- Bulería, GREDOS y ResearchGate no se sustituyen por bloqueos de automatización.
- Los handles de Salamanca, UvaDoc y otros destinos con timeout se conservan
  cuando no existe sustituto documentado.

Estas limitaciones quedan pendientes de una comprobación posterior; no se han
convertido en diagnósticos falsos de enlace roto.

## 5. Correcciones y contacto

La Parte VI incorpora `Correcciones y contacto` después de `Cómo citar` y antes
de `Bibliografía`. Mantiene literalmente:

`EMAIL DE CONTACTO — PLACEHOLDER PENDIENTE`

GitHub Issues aparece solo como canal futuro y complementario. La dirección y
la referencia al repositorio deberán activarse antes de la publicación cuando
R1–R5 hayan dejado el repositorio apto; no se publica ninguna URL ahora.

## 6. Tratamiento del repositorio

`AUD-REPO-01 = REPO NO APTO TODAVÍA PARA APERTURA PÚBLICA` sigue vigente. El
libro no afirma que el repositorio esté disponible. La línea R1–R5 permanece
independiente de E3.

## 7. Cambios en generadores

- `build_transcription.py`: introducción pública y adaptación de notas
  editoriales sin modificar la paleografía.
- `build_facsimile.py`: una declaración global de resolución y localizadores
  de página concisos.
- `build_indexes.py`: explicación alfabética pública y retirada de estados
  temporales.
- `build_apparatus.py`: glosario, cuadros y matriz con lenguaje de lector.
- `reader_text.py`: normalización determinista y acotada de URLs y residuos de
  workflow en texto derivado.

`prepare.py` se completó una vez para regenerar e inspeccionar los derivados.
`publication/generated/` permanece ignorado y no se versiona.

## 8. Validación focal

- Tests focales de contenido, preliminares, aparatos, generadores, navegación,
  bibliografía y enlaces internos: `193 passed`.
- `check_sources.py`: PASS.
- `validate_publication.py`: PASS.
- Cartografía `--check`: PASS.
- Comprobación focal de las URLs modificadas: el PDF institucional de Uniovi y
  la ficha GREDOS respondieron correctamente; PARES limitó la comprobación
  automatizada, por lo que se conservó la normalización acreditada por LINK-01.
- `quarto check` con caché temporal escribible: PASS.
- Auditoría de jerga pública: sin defectos residuales; las coincidencias
  restantes se limitan a metadata invisible o documentación técnica. Quarto en
  el colofón es legítimo.
- `git diff --check`: PASS.

No se ejecutaron suite completa ni renders completos; la validación integral y
la reproducibilidad final corresponden a E4.

## 9. Pendientes

- Sustituir el email placeholder antes de la publicación.
- Incorporar fecha exacta y URL canónica cuando existan.
- Mantener ausente el ISBN mientras no exista.
- Resolver la línea R1–R5 antes de afirmar que el repositorio es público.
- Revisar posteriormente los enlaces preservados por limitaciones de red.

## 10. Resultado

**E3: APTO PARA REVISIÓN E INTEGRACIÓN.**

Los 23 hallazgos de E1 y las correcciones localizadas de E2 quedan resueltos o
explícitamente diferidos sin modificar `project/`, sin abrir el repositorio y
sin iniciar E4.

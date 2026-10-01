# Estado y roadmap de la publicación Quarto

**Actualizado:** 1 de octubre de 2026<br>
**Estado global:** Fase 3 en curso; Fases 3A y 3B completadas<br>
**Fase actual:** 3C — capítulos 3 y 4 (siguiente; no iniciada)<br>
**Base documental auditada:** `6b49be848c92c4772b37c46495135352821d50f8`  
**Operación canónica al auditar:** `clean`

## Lectura de entrada

Una sesión nueva de Copilot debe leer, en este orden:

1. `PROJECT.md`;
2. `project/00_CONTROL/proyecto.yaml` y `estado.yaml`;
3. `.github/copilot-instructions.md`;
4. `docs/PLAN_MAESTRO_PUBLICACION_QUARTO.md`;
5. este roadmap;
6. `.github/instructions/publication.instructions.md`;
7. `publication/README.md`;
8. `docs/ESPECIFICACION_BOOTSTRAP_PUBLICATION.md` como registro de aceptación de la Fase 2A.

## Estado comprobado

- `main` y `origin/main` comprobados en `e81dc9239ac8dbabfe77168a50ef98c4d3b79170`; permanecen intactos.
- Edición Crítica 3.6, Estudio Histórico 1.2, Registro 1.2 y edición modernizada 1.3 vigentes.
- Índice rector 1.5 y Plan de composición 0.5 vigentes.
- Manuscrito: PDF autoritativo de 18 páginas en Drive, solo lectura; no está en GitHub.
- PDF completo 0.6: referencia editorial externa, no autoridad ni archivo del repositorio.
- Bootstrap mínimo de `publication/` publicado en `e9c3991ed72d9abf0469c11d87958bf934720f92`.
- Prototipo vertical 2B implementado, corregido y validado en los commits registrados en este roadmap.
- Capítulo 1 implementado en `030ea7e51fc42d23bf32d914df0bf6b0d7ddfda7` y aceptado mediante auditoría independiente con veredicto `APTO`.
- Capítulo 2 implementado en `3b07bdf0a4c22bfe0e97015005f087125328c484`, corregido técnicamente y aceptado mediante auditoría independiente final con veredicto `APTO`.
- HTML y PDF técnicos renderizados correctamente; ninguna salida de render está versionada.
- No hay migración de capítulos en bloque ni configuración de despliegue.

## Fases

| Fase | Estado | Resultado / puerta |
|---|---|---|
| 0. Auditoría de viabilidad y volumen 0.6 | completada | inventario, procedencia y problemas de regresión identificados |
| 1. Diseño editorial y técnico v0.1 | completada | 16 capítulos, árbol objetivo, matriz manual/generado y estrategia de facsímil fijados |
| 1B. Contexto autosuficiente para Copilot | completada | instrucciones, plan, especificación y roadmap versionados |
| 2A. Bootstrap y smoke test | completada | implementación `e9c3991ed72d9abf0469c11d87958bf934720f92`; HTML, PDF y tests en PASS; `project/` intacto |
| 2B. Prototipo vertical | completada | muestra vertical multiformato validada; trazabilidad, facsímil, paleografía, modernización y aparato integrados |
| 3. Contenido editorial | en curso | Fases 3A y 3B completadas; capítulos 1 y 2 aceptados; Fase 3C como única tarea siguiente |
| 4. Generación documental | pendiente | capítulos 14–16, glosario, cuadros, concordancia y matriz reproducibles |
| 5. Índices y calidad integral | pendiente | nueve índices; HTML/PDF completos; accesibilidad y revisión visual |
| 6. Preview y publicación 1.0 | pendiente | snapshot, validación, preview aceptada, etiqueta y publicación con puerta editorial |

## Siguiente tarea exacta

Fase 3C: crear y validar conjuntamente los capítulos 3, «El expediente de Sorribos y Santibáñez de Ordás», y 4, «Del manuscrito al volumen actual», como cierre de la Parte I, manteniendo separadas la descripción histórica del expediente y la explicación del proceso editorial, sin modificar fuentes canónicas ni iniciar la Parte II.

### Cierre comprobado de 2A

- Implementación atómica publicada: `e9c3991ed72d9abf0469c11d87958bf934720f92`.
- `prepare.py`: dos ejecuciones directas en PASS; mismo estado y escrituras limitadas a `generated/`.
- Tests existentes: 34 en PASS.
- `quarto check`: PASS con Quarto 1.7.31 y TinyTeX 2026.
- HTML: PASS; portada, capítulo técnico, navegación y búsqueda generados.
- PDF: PASS con LuaHBTeX 1.24.0; 4 páginas, texto seleccionable e inspección visual correcta.
- Dependencias bloqueantes: ninguna; Quarto resolvió LuaLaTeX desde TinyTeX aunque no estaba en el `PATH` de la shell.
- `project/`, `plugins/`, `tests/` y las instrucciones permanecieron intactos en el commit de implementación.
- Ningún PDF, `_book/` ni contenido de `generated/` quedó versionado.

## Cierre comprobado de 2B

- Implementación 2B: `a5dd318203fad847b6429e47ccd10b6b5b6c165b`.
- Corrección de lineación: `ad70d0bbfc08e9c59abe57ede8c5f8440fef7c01`.
- Formalización del flujo local-first: `88286ef68642811daada1841bd5757dfc7adc117`.
- Paleografía: 18 líneas y siete guiones documentales conservados.
- Generación: seis derivados idempotentes.
- Tests existentes: 47 en PASS.
- `quarto check`: PASS.
- Render multiformato HTML/PDF: PASS.
- Validador estricto: PASS.
- PDF: 15 páginas; inspección visual aceptada.
- `project/`, `plugins/` y `main` permanecieron intactos.
- Ningún PDF ni derivado quedó versionado.

## Cierre comprobado de 3A

- Implementación: `030ea7e51fc42d23bf32d914df0bf6b0d7ddfda7` (`feat(publication): add chapter 1`).
- Auditoría independiente: `APTO`; ninguna corrección pendiente antes del cierre.
- Capítulo 1 creado como primer capítulo editorial real de la Parte I; fuentes, límites con los capítulos 2–4 y separación entre dato local y contexto externo aceptados.
- Composición: preliminares no numerados y capítulo nuevo numerado correctamente como capítulo 1; prototipo 2B conservado sin regresiones.
- Generación: dos preparaciones idempotentes y seis derivados con SHA-256 idénticos.
- Validación: validador estático y renderizado en PASS; 48 tests en PASS; `quarto check` y render multiformato HTML/PDF en PASS.
- HTML: ocho páginas, con el capítulo navegable y numerado como 1. PDF: 19 páginas, con el capítulo 1 en las páginas 6–8; inspección visual de esas páginas en PASS.
- Regresión 2B: 18 líneas paleográficas y siete guiones documentales conservados.
- Integridad: `project/`, `plugins/`, fuentes canónicas y `main` intactos; ningún PDF, `_book/` ni derivado versionado; ninguna dependencia bloqueante.

## Cierre comprobado de 3B

- Implementación: `3b07bdf0a4c22bfe0e97015005f087125328c484` (`feat(publication): add chapter 2`).
- Primera corrección técnica: `096c24830eb1ec207e20cdf6e5538f01cffeb60c` (`fix(publication): align validation with render workflow`).
- Segunda corrección técnica: `2322ea31d285fd25534d61890da5532a15da03aa` (`fix(publication): detect bare questionnaire markers`).
- Auditorías independientes: editorial inicial `APTO CON AJUSTES`, sin defectos de contenido; primera corrección `APTO CON AJUSTES`, por el marcador sin sufijo; auditoría final `APTO`, sin correcciones pendientes.
- Resultado editorial: capítulo 2, «Las Respuestas Generales y el interrogatorio de cuarenta preguntas», incorporado como segundo capítulo editorial real de la Parte I. No duplica las cuarenta preguntas: las organiza mediante un cuadro de diez bloques temáticos; la pregunta 29 conserva su incidencia de transmisión documentada; formulario externo y respuesta local mantienen autoridades separadas.
- Fronteras: preservadas con los capítulos 1, 3, 4 y 16. El capítulo 2 no fue modificado durante las correcciones técnicas.
- Generación: preparación ejecutada dos veces; seis derivados con SHA-256 idénticos. Se conservaron 18 líneas paleográficas y siete guiones documentales.
- Validación: validador estático y renderizado en PASS; `quarto check`, render multiformato HTML/PDF y regresiones 3A/2B en PASS; suite final de 61 tests en PASS, también con el PDF ignorado todavía presente.
- Composición: nueve páginas HTML; PDF de 22 páginas, con el capítulo 2 en las páginas 9–11; ninguna dependencia bloqueante.
- Política de PDFs: los PDFs seguidos o no ignorados se rechazan; el PDF reproducible de `_book/` se permite y permanece ignorado. Ningún PDF, `_book/` ni derivado quedó versionado.
- Integridad: `project/`, `plugins/`, fuentes canónicas y `main` permanecieron intactos.

## Reglas para actualizar este roadmap

- Solo marcar una fase como completada cuando cumpla todos sus criterios.
- Registrar el commit de cierre y los resultados de validación.
- Mantener una sola `siguiente tarea exacta`.
- No convertir este archivo en diario detallado; los razonamientos estables van al plan maestro y los informes de validación tendrán documentos propios cuando sean necesarios.
- Si cambian fuentes canónicas, reauditar versiones y actualizar `meta/publication.yml` en una operación específica.

## Prompt recomendado para la siguiente sesión

> Lee `PROJECT.md`, `.github/copilot-instructions.md`, `docs/PLAN_MAESTRO_PUBLICACION_QUARTO.md`, `docs/ESTADO_PUBLICACION_QUARTO.md`, `.github/instructions/publication.instructions.md` y `publication/README.md`. Ejecuta únicamente la Fase 3C: crea y valida conjuntamente los capítulos 3, «El expediente de Sorribos y Santibáñez de Ordás», y 4, «Del manuscrito al volumen actual», como cierre de la Parte I, manteniendo separadas la descripción histórica del expediente y la explicación del proceso editorial, sin modificar fuentes canónicas ni iniciar la Parte II. Revisa el diff y publica un único commit atómico solo si la rama sigue en el mismo `base_sha`.

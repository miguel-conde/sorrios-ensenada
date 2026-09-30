# Estado y roadmap de la publicación Quarto

**Actualizado:** 30 de septiembre de 2026<br>
**Estado global:** Fase 2B completada; preparado para iniciar la Fase 3A<br>
**Fase actual:** 3A — capítulo 1 (siguiente; no iniciada)<br>
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

- `main` auditado en `6b49be848c92c4772b37c46495135352821d50f8` antes de esta operación documental.
- Edición Crítica 3.6, Estudio Histórico 1.2, Registro 1.2 y edición modernizada 1.3 vigentes.
- Índice rector 1.5 y Plan de composición 0.5 vigentes.
- Manuscrito: PDF autoritativo de 18 páginas en Drive, solo lectura; no está en GitHub.
- PDF completo 0.6: referencia editorial externa, no autoridad ni archivo del repositorio.
- Bootstrap mínimo de `publication/` publicado en `e9c3991ed72d9abf0469c11d87958bf934720f92`.
- Prototipo vertical 2B implementado, corregido y validado en los commits registrados en este roadmap.
- HTML y PDF técnicos renderizados correctamente; ninguna salida de render está versionada.
- No hay migración de capítulos ni configuración de despliegue.

## Fases

| Fase | Estado | Resultado / puerta |
|---|---|---|
| 0. Auditoría de viabilidad y volumen 0.6 | completada | inventario, procedencia y problemas de regresión identificados |
| 1. Diseño editorial y técnico v0.1 | completada | 16 capítulos, árbol objetivo, matriz manual/generado y estrategia de facsímil fijados |
| 1B. Contexto autosuficiente para Copilot | completada | instrucciones, plan, especificación y roadmap versionados |
| 2A. Bootstrap y smoke test | completada | implementación `e9c3991ed72d9abf0469c11d87958bf934720f92`; HTML, PDF y tests en PASS; `project/` intacto |
| 2B. Prototipo vertical | completada | muestra vertical multiformato validada; trazabilidad, facsímil, paleografía, modernización y aparato integrados |
| 3. Contenido editorial | pendiente | capítulos 1–13 refundidos y trazables; regresiones 0.6 resueltas |
| 4. Generación documental | pendiente | capítulos 14–16, glosario, cuadros, concordancia y matriz reproducibles |
| 5. Índices y calidad integral | pendiente | nueve índices; HTML/PDF completos; accesibilidad y revisión visual |
| 6. Preview y publicación 1.0 | pendiente | snapshot, validación, preview aceptada, etiqueta y publicación con puerta editorial |

## Siguiente tarea exacta

Fase 3A: crear y validar exclusivamente el capítulo 1, «El Catastro de Ensenada», como primer capítulo editorial real de la Parte I, sin iniciar otros capítulos ni modificar fuentes canónicas.

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

## Reglas para actualizar este roadmap

- Solo marcar una fase como completada cuando cumpla todos sus criterios.
- Registrar el commit de cierre y los resultados de validación.
- Mantener una sola `siguiente tarea exacta`.
- No convertir este archivo en diario detallado; los razonamientos estables van al plan maestro y los informes de validación tendrán documentos propios cuando sean necesarios.
- Si cambian fuentes canónicas, reauditar versiones y actualizar `meta/publication.yml` en una operación específica.

## Prompt recomendado para la siguiente sesión

> Lee `PROJECT.md`, `.github/copilot-instructions.md`, `docs/PLAN_MAESTRO_PUBLICACION_QUARTO.md`, `docs/ESTADO_PUBLICACION_QUARTO.md`, `.github/instructions/publication.instructions.md` y `publication/README.md`. Ejecuta únicamente la Fase 3A: crea y valida exclusivamente el capítulo 1, «El Catastro de Ensenada», como primer capítulo editorial real de la Parte I, sin iniciar otros capítulos ni modificar fuentes canónicas. Revisa el diff y publica un único commit atómico solo si la rama sigue en el mismo `base_sha`.


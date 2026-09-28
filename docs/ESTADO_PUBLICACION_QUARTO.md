# Estado y roadmap de la publicación Quarto

**Actualizado:** 28 de septiembre de 2026  
**Estado global:** preparado para bootstrap técnico  
**Fase actual:** 2A — infraestructura mínima y primer render  
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
7. `docs/ESPECIFICACION_BOOTSTRAP_PUBLICATION.md` para la tarea actual;
8. `publication/README.md` cuando exista.

## Estado comprobado

- `main` auditado en `6b49be848c92c4772b37c46495135352821d50f8` antes de esta operación documental.
- Edición Crítica 3.6, Estudio Histórico 1.2, Registro 1.2 y edición modernizada 1.3 vigentes.
- Índice rector 1.5 y Plan de composición 0.5 vigentes.
- Manuscrito: PDF autoritativo de 18 páginas en Drive, solo lectura; no está en GitHub.
- PDF completo 0.6: referencia editorial externa, no autoridad ni archivo del repositorio.
- `publication/`: todavía no existe.
- No hay migración de capítulos ni configuración de despliegue.

## Fases

| Fase | Estado | Resultado / puerta |
|---|---|---|
| 0. Auditoría de viabilidad y volumen 0.6 | completada | inventario, procedencia y problemas de regresión identificados |
| 1. Diseño editorial y técnico v0.1 | completada | 16 capítulos, árbol objetivo, matriz manual/generado y estrategia de facsímil fijados |
| 1B. Contexto autosuficiente para Copilot | completada con este commit | instrucciones, plan, especificación y roadmap versionados |
| 2A. Bootstrap y smoke test | **siguiente** | HTML mínimo PASS; prueba PDF; `project/` intacto |
| 2B. Prototipo vertical | pendiente | un capítulo histórico, una página facsimilar, una unidad paleográfica, una respuesta modernizada y un aparato |
| 3. Contenido editorial | pendiente | capítulos 1–13 refundidos y trazables; regresiones 0.6 resueltas |
| 4. Generación documental | pendiente | capítulos 14–16, glosario, cuadros, concordancia y matriz reproducibles |
| 5. Índices y calidad integral | pendiente | nueve índices; HTML/PDF completos; accesibilidad y revisión visual |
| 6. Preview y publicación 1.0 | pendiente | snapshot, validación, preview aceptada, etiqueta y publicación con puerta editorial |

## Siguiente tarea exacta

Ejecutar únicamente la Fase 2A definida en `docs/ESPECIFICACION_BOOTSTRAP_PUBLICATION.md`: crear el armazón mínimo de `publication/`, actualizar `.gitignore`, realizar el primer render HTML y probar PDF. No migrar contenido real, no añadir facsímiles y no modificar `project/`.

### Criterios de cierre de 2A

- `publication/README.md`, `_quarto.yml`, manifiestos, página inicial, capítulo técnico, estilo mínimo y `prepare.py` presentes;
- `prepare.py` idempotente y limitado a `generated/`;
- HTML renderizado correctamente;
- resultado real de `quarto check` y del intento PDF registrado;
- tests existentes aplicables en PASS;
- ninguna modificación bajo `project/`, `plugins/`, `tests/` o `docs/`;
- ningún PDF ni salida `_book/` versionados;
- operación publicada en un commit atómico.

## Contenido de la Fase 2B

No iniciar hasta cerrar 2A. El prototipo vertical seleccionará material suficiente para forzar las decisiones difíciles:

- un capítulo histórico de la Parte II con identificadores D/C/I/E/L;
- una página completa del facsímil como derivado temporal o local;
- una unidad con recorte, transcripción y aparato;
- una respuesta modernizada;
- un cuadro o fragmento de matriz;
- navegación equivalente en HTML y PDF.

La aceptación decidirá tipografía, densidad, tratamiento de notas, estrategia de imágenes y límite de personalización LaTeX antes de la migración masiva.

## Reglas para actualizar este roadmap

- Solo marcar una fase como completada cuando cumpla todos sus criterios.
- Registrar el commit de cierre y los resultados de validación.
- Mantener una sola `siguiente tarea exacta`.
- No convertir este archivo en diario detallado; los razonamientos estables van al plan maestro y los informes de validación tendrán documentos propios cuando sean necesarios.
- Si cambian fuentes canónicas, reauditar versiones y actualizar `meta/publication.yml` en una operación específica.

## Prompt recomendado para la siguiente sesión

> Lee `PROJECT.md`, `.github/copilot-instructions.md`, `docs/PLAN_MAESTRO_PUBLICACION_QUARTO.md`, `docs/ESTADO_PUBLICACION_QUARTO.md`, `.github/instructions/publication.instructions.md` y `docs/ESPECIFICACION_BOOTSTRAP_PUBLICATION.md`. Ejecuta únicamente la Fase 2A: crea la infraestructura mínima de `publication/` y actualiza `.gitignore` según la especificación. No modifiques `project/`, `plugins/`, `tests/` ni `docs/`; no migres contenido histórico ni añadas PDFs o facsímiles. Ejecuta los tests aplicables, `quarto check`, el render HTML y la prueba PDF; registra con precisión cualquier dependencia ausente. Antes de terminar, revisa el diff, confirma que `project/` está intacto e informa de archivos y validaciones. Publica el conjunto como un único commit atómico solo si la rama sigue en el mismo `base_sha`.


# AGENTS.md

## Finalidad

Este archivo contiene instrucciones duraderas para trabajar en este repositorio con Codex.

No registrar aquí el estado coyuntural del proyecto: fase actual, siguiente tarea, rama activa, SHA de partida o versiones vigentes. Esa información debe obtenerse de los documentos de estado, del repositorio y del encargo del usuario.

## Inicio de una tarea

1. Confirmar el repositorio, la rama activa, el estado del árbol de trabajo y el historial reciente.
2. Leer `PROJECT.md` antes de modificar archivos.
3. Consultar `proyecto.yaml`, `estado.yaml` y los documentos de control que correspondan al trabajo solicitado.
4. No asumir que se debe trabajar en `main`.
5. No cambiar de rama, crear commits, publicar cambios ni modificar sistemas externos salvo que la tarea lo autorice.

## Trabajo sobre la publicación Quarto

Cuando la tarea afecte al libro Quarto, leer:

1. `.github/copilot-instructions.md`
2. `docs/PLAN_MAESTRO_PUBLICACION_QUARTO.md`
3. `docs/ESTADO_PUBLICACION_QUARTO.md`
4. `.github/instructions/publication.instructions.md`
5. `publication/README.md`, cuando exista.

`docs/ESTADO_PUBLICACION_QUARTO.md` es la referencia para conocer la fase vigente, el trabajo ya realizado y la siguiente tarea prevista.

## Límites de autoridad

- `project/` contiene las fuentes y datos canónicos del expediente.
- `publication/content/` contendrá texto editorial propio del libro.
- `publication/generated/` contendrá derivados reproducibles y no se editará manualmente.
- El PDF manuscrito autoritativo permanece en Google Drive y no debe subirse al repositorio.
- La composición PDF 0.6 es una referencia editorial, no una autoridad textual.
- No modificar contenido histórico canónico durante tareas de infraestructura o publicación, salvo autorización expresa y mediante una operación separada.

## Operaciones atómicas

- Respetar las reglas de operaciones atómicas definidas en `PROJECT.md`.
- Mantener separados los cambios canónicos, editoriales, técnicos y de documentación cuando tengan distinta autoridad.
- No mezclar una modificación de `project/` con infraestructura de `publication/` sin justificación y autorización explícitas.
- No reescribir historial ni forzar actualizaciones remotas.
- Preservar los cambios existentes del usuario.

## Validación

Antes de dar una tarea por terminada:

- ejecutar las validaciones exigidas por `PROJECT.md`;
- ejecutar las pruebas o comprobaciones específicas de los archivos modificados;
- verificar que no se han incorporado PDFs, credenciales ni fuentes externas restringidas;
- comprobar que los archivos generados son reproducibles;
- confirmar que `project/` permanece intacto cuando la tarea solo afecta a la publicación;
- actualizar `docs/ESTADO_PUBLICACION_QUARTO.md` si cambia el estado real del plan.

## Entrega

El informe final debe indicar:

- archivos creados o modificados;
- validaciones realizadas y sus resultados;
- decisiones o supuestos relevantes;
- límites o trabajo pendiente;
- siguiente paso recomendado, cuando corresponda.
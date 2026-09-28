# Instrucciones de GitHub Copilot

Este repositorio contiene dos capas con funciones diferentes:

- `project/` es el workspace canónico de investigación y edición del Catastro de Ensenada de Sorribos y Santibáñez de Ordás.
- `publication/` será la capa de composición y publicación del libro Quarto. No es una nueva fuente histórica ni editorial.

## Lectura obligatoria al iniciar una sesión

1. Lee `PROJECT.md`.
2. Lee `project/00_CONTROL/proyecto.yaml` y `project/00_CONTROL/estado.yaml` desde la rama o commit de la tarea.
3. Comprueba que `operation.status` sea `clean`. Si no lo es, no escribas hasta auditar la operación pendiente.
4. Lee `plugins/sorrios-ensenada/skills/editar-catastro-sorrios/references/task-modes.md` y determina el modo de trabajo.
5. Para trabajo de publicación, lee además, en este orden:
   - `docs/PLAN_MAESTRO_PUBLICACION_QUARTO.md`;
   - `docs/ESTADO_PUBLICACION_QUARTO.md`;
   - `.github/instructions/publication.instructions.md`;
   - `publication/README.md`, cuando exista.
6. Ejecuta únicamente la tarea marcada como siguiente en el roadmap, salvo instrucción expresa del usuario.

No uses una conversación, una descarga, una copia local ni el PDF de composición 0.6 como estado canónico.

## Autoridades

- El PDF manuscrito declarado en `project/00_CONTROL/proyecto.yaml`, conservado en Google Drive, manda sobre la materialidad y lectura del original. Drive es de solo lectura.
- `project/00_CONTROL/Manual_Editorial.md` manda sobre el método editorial.
- `proyecto.yaml`, `estado.yaml` y `unidades.yaml` mandan sobre identidad, estado y secuencia.
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md` manda sobre la transcripción y el aparato.
- El Estudio Histórico, el Registro D/C/I/E/L, la edición modernizada, el Glosario y los cinco índices vivos mandan en sus ámbitos declarados.
- Los análisis 0.1–0.6 son auxiliares: sirven para formular y localizar análisis, pero no tienen autoridad documental autónoma.
- `publication/content/` contendrá texto editorial propio del libro.
- `publication/generated/` y `_book/` serán derivados regenerables y no tendrán autoridad.
- El PDF completo 0.6 es una referencia editorial externa de la composición alcanzada, no autoridad textual ni archivo que deba incorporarse al repositorio.

Ante un conflicto, aplica la jerarquía anterior y documenta la decisión. Una fuente externa nunca corrige por sí sola el dato local.

## Límites de escritura

- No subas el PDF manuscrito ni el PDF 0.6 a GitHub.
- No escribas en Google Drive.
- No modifiques `project/` durante una tarea de publicación salvo autorización expresa y una operación canónica separada.
- No corrijas un dato histórico silenciosamente en `publication/`. Localiza primero su fuente autoritativa; corrígela allí mediante el procedimiento del proyecto y propaga después el cambio.
- No edites a mano `publication/generated/` ni `_book/`.
- No uses `project/90_ARCHIVO/` como fuente viva salvo auditoría o consulta histórica expresa.
- No inventes equivalencias, cifras, identificaciones, relaciones causales, licencias, fuentes o metadatos ausentes.
- No introduzcas filtros Lua, automatización de despliegue ni infraestructura compleja antes de que el roadmap los solicite.

## Reglas editoriales esenciales

Mantén separadas las capas D/C/I/E/L:

- D: dato explícito de la Edición Crítica.
- C: cálculo reproducible con operandos y regla declarados.
- I: interpretación compatible con la evidencia y formulada con cautela.
- E: contexto externo identificado; no crea datos locales.
- L: límite, discrepancia o pregunta abierta que debe seguir visible.

Conserva las cuatro formas de acceso al documento: facsímil, transcripción paleográfica y aparato, edición modernizada e interpretación histórica. No permitas que una sustituya a otra.

## Trabajo con Git

- Parte de la rama o commit indicado por el usuario; en trabajo normal usa la rama canónica de `proyecto.yaml`.
- Para cualquier cambio multiarchivo fija un único `base_sha`, prepara y valida todo contra ese estado, vuelve a comprobar el SHA de la rama y publica un solo commit atómico sin `force`.
- Si la rama cambia, detén la publicación, relee y reconcilia.
- Respeta cambios ajenos y no reformatees ni reescribas archivos fuera del alcance.
- Informa siempre de archivos cambiados, comprobaciones ejecutadas y bloqueos reales.

## Validación

La validación es proporcional a la fase, pero debe incluir como mínimo:

- comprobar que `project/` no ha cambiado en tareas de publicación;
- ejecutar los tests existentes aplicables;
- comprobar que no se ha añadido ningún PDF al repositorio;
- validar metadatos y referencias a identificadores de evidencia;
- renderizar HTML y PDF cuando la fase lo exija;
- distinguir un fallo del contenido de la ausencia local de Quarto, Python o LaTeX;
- no declarar completada una fase con incidencias críticas o altas abiertas.

El plan maestro define la arquitectura y los criterios; el roadmap define el estado y la siguiente tarea. No dupliques ambos documentos en nuevos planes paralelos.


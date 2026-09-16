# Esquemas

## `project/00_CONTROL/proyecto.yaml`

Debe usar `schema_version: 2` e incluir:

- `project_id` y `title`;
- `repository.provider: github`, `full_name`, `canonical_branch` y `project_root`;
- nombre, versión y ruta del plugin y de la skill;
- fase actual y `historical_study_enabled`;
- `authorities.manuscript` con `provider: google_drive`, `access: read_only`, `file_id`, nombre, SHA-256, tamaño y páginas;
- `authorities.manual` con ruta GitHub y versión;
- rutas GitHub de controles, documentos e histórico.

Los controles y documentos vivos no llevan IDs de Drive. Los valores `path` son rutas lógicas POSIX relativas a la raíz del repositorio.

### Fases

`phase.current` admite:

- `edicion_paleografica`;
- `estudio_historico`.

Durante `edicion_paleografica`, `phase.historical_study_enabled` y `documents.historical_study.enabled` son `false`.

Durante `estudio_historico`, ambos indicadores son `true` y `estado.yaml.phase` debe ser también `estudio_historico`.

La activación del Estudio Histórico solo es válida cuando las 35 unidades están validadas y cerradas, el estado es terminal, `open_issues` y `pending_tasks` están vacíos y `operation.status` es `clean`. La activación no modifica por sí misma la edición paleográfica ni amplía el corpus documental definido por el Manual.

## `project/00_CONTROL/estado.yaml`

Debe incluir fase, última unidad validada y cerrada, unidad actual y siguiente, ubicación, dudas, tareas y operación. `operation.status` admite `clean`, `prepared`, `failed` o `verified`.

`phase` debe coincidir con `project/00_CONTROL/proyecto.yaml: phase.current`.

Mientras queden unidades por cerrar, `current_unit` debe identificar una unidad de `unidades.yaml`, `current_location` debe coincidir con ella, `last_closed_unit` y `last_validated_unit` deben identificar la unidad inmediatamente anterior y `next_unit` debe coincidir con la unidad siguiente.

Cuando estén cerradas las 35 unidades se usa el estado terminal: `last_validated_unit` y `last_closed_unit` identifican la última unidad de `unidades.yaml`; `current_unit`, `next_unit` y `current_location` son `null`; `pending_tasks` es una lista vacía. El cierre de la secuencia no cambia por sí solo la fase ni activa el Estudio Histórico.

Si una operación usa `allowed_changes`, sus elementos son rutas lógicas relativas y se normalizan a POSIX antes de comparar.

## `project/00_CONTROL/unidades.yaml`

Debe declarar `unit_count: 35`. Cada unidad tiene id, etiqueta, orden, página, posición, anterior y siguiente. Las posiciones válidas son `complete`, `left` y `right`.

## Edición

Cada unidad de `Edicion_Critica.md` contiene exactamente estas seis secciones:

1. Imagen.
2. Transcripción paleográfica.
3. Observaciones editoriales.
4. Notas paleográficas.
5. Notas históricas.
6. Referencias cruzadas.

## Operaciones

Los registros de `project/00_CONTROL/OPERACIONES/` documentan la operación editorial y el commit que la publica. Git es el historial técnico; el registro conserva el sentido editorial de la operación.

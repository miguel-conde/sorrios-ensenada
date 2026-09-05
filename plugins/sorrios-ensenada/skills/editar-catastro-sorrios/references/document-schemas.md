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

## `project/00_CONTROL/estado.yaml`

Debe incluir fase, última unidad validada y cerrada, unidad actual y siguiente, ubicación, dudas, tareas y operación. `operation.status` admite `clean`, `prepared`, `failed` o `verified`.

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

# Esquemas

## proyecto.yaml

Debe incluir `schema_version`, `project_id`, `drive_root_id`, versiones de plugin y skill, fase, carpetas, autoridades y documentos. Cada archivo vivo debe tener `file_id` y `path`.

## estado.yaml

Debe incluir fase, última unidad validada y cerrada, unidad actual y siguiente, ubicación, dudas, tareas y operación. `operation.status` admite `clean`, `prepared`, `failed` o `verified`.

## unidades.yaml

Debe declarar `unit_count: 35`. Cada unidad tiene id, etiqueta, orden, página, posición, anterior y siguiente. Posiciones: `complete`, `left` o `right`.

## Edición

Cada unidad contiene Imagen, Transcripción paleográfica, Observaciones editoriales, Notas paleográficas, Notas históricas y Referencias cruzadas.

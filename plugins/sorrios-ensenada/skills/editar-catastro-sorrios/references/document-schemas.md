# Esquemas

## proyecto.yaml

Debe incluir `schema_version`, `project_id`, `drive_root_id`, versiones de plugin y skill, fase, carpetas, autoridades y documentos. Cada archivo vivo debe tener `file_id` y `path`.

Los valores `path` persistidos son rutas lógicas relativas y usan `/` como forma
canónica. No son rutas físicas y no se les aplica `Path.resolve()`. Los validadores
aceptan también `\` por compatibilidad con datos existentes y normalizan antes de
comparar.

## estado.yaml

Debe incluir fase, última unidad validada y cerrada, unidad actual y siguiente, ubicación, dudas, tareas y operación. `operation.status` admite `clean`, `prepared`, `failed` o `verified`.

Los elementos de `allowed_changes` siguen siendo cadenas. Se interpretan como rutas
lógicas relativas y se normalizan al formato POSIX canónico antes de compararlos.

## unidades.yaml

Debe declarar `unit_count: 35`. Cada unidad tiene id, etiqueta, orden, página, posición, anterior y siguiente. Posiciones: `complete`, `left` o `right`.

## Edición

Cada unidad contiene Imagen, Transcripción paleográfica, Observaciones editoriales, Notas paleográficas, Notas históricas y Referencias cruzadas.

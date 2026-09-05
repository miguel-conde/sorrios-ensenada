# Acceso al PDF autoritativo

## Autoridad y límites

El único archivo de Drive usado en el flujo normal es el PDF declarado en `project/00_CONTROL/proyecto.yaml` bajo `authorities.manuscript`.

Drive es de solo lectura. No se suben controles, edición, resultados ni históricos a Drive y no se modifica el PDF.

## Obtención

1. Lee en `proyecto.yaml` el `file_id`, nombre, SHA-256, tamaño y número de páginas esperados.
2. Obtén el archivo directamente mediante la conexión de Google Drive como archivo real, sin Base64.
3. Comprueba al menos identidad, nombre, MIME y tamaño antes de usarlo; cuando el entorno permita calcular el hash, comprueba también SHA-256.
4. Mantén cualquier copia del runtime como temporal. No la añadas al repositorio ni la conviertas en estado del proyecto.

Si el conector no puede entregar el PDF como archivo utilizable, detén esa parte de la tarea. El flujo normal no usa un fallback Base64 ni exige materialización local.

## Selección de unidad

1. Lee `project/00_CONTROL/unidades.yaml` desde el mismo ref que el estado del proyecto.
2. Resuelve `unit_id` a `pdf_page` y `position`.
3. Renderiza la página en el runtime disponible.
4. Para `complete`, usa la página completa; para `left` o `right`, recorta la mitad correspondiente sin alterar el original.
5. Lee visualmente la unidad. OCR puede servir como ayuda excepcional, pero nunca sustituye la lectura visual del manuscrito.

## Entornos

El uso normal no requiere Work, checkout local, WSL, Python local, Poppler, Git local, VS Code ni Codex CLI. Si un entorno de desarrollo conserva herramientas de render, son ayudas de desarrollo y no parte del contrato de uso.

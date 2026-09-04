# Materialización local desde Google Drive

Este protocolo se aplica cuando una ayuda local necesita los bytes de un archivo
almacenado en Drive, en especial el PDF autoritativo. No se aplica a documentos
nativos de Google ni autoriza escrituras en Drive.

## Límite autorizado

El propietario del proyecto autoriza el fallback Base64 solo cuando se cumplen
todas estas condiciones:

- el archivo se localizó por el identificador declarado en `proyecto.yaml`;
- el tamaño declarado no supera 8 MiB (8.388.608 bytes);
- se conocen el tamaño exacto y el SHA-256 esperado;
- la copia se crea en un directorio temporal nuevo, fuera del repositorio;
- el contenido Base64 no se muestra, registra ni incluye en una línea de comandos.

Si falta una condición, detén la operación. No amplíes el límite sin aprobación
expresa.

## Orden de materialización

1. Lee los metadatos del archivo y comprueba ID, nombre, MIME y tamaño.
2. Solicita la descarga completa sin Base64 para obtener una referencia de archivo.
3. Si el entorno proporciona una ruta local materializada, úsala.
4. Si proporciona una URL HTTPS temporal utilizable por el ejecutor local,
   descárgala directamente a un directorio temporal nuevo.
5. Si solo proporciona una referencia interna no materializable, solicita de nuevo
   la descarga completa con Base64 y aplica el fallback autorizado.

No abras referencias internas con el navegador. No uses una URL pública o
construida a mano de Drive. No uses `curl` o `wget` con la URL canónica de Drive.

## Fallback Base64

Usa `scripts/materialize_drive_payload.py`. Inícialo con el nombre de salida,
tamaño y SHA-256 declarados, y entrega el Base64 directamente por la entrada
estándar del proceso:

```bash
python scripts/materialize_drive_payload.py "$TEMP_DIR/manuscript.pdf" \
  --expected-size 5038575 \
  --expected-sha256 d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24
```

No interpoles el Base64 en el comando ni lo guardes en el historial de la shell.
Cuando se proporciona `--expected-size`, la ayuda calcula la longitud Base64
estándar como `4 × ceil(expected_size / 3)`. Lee los bytes disponibles por bloques,
ignorando únicamente espacios ASCII, tabuladores y saltos de línea, y termina en
cuanto recibe ese número de caracteres Base64: no necesita esperar a EOF. Un EOF
anterior a esa longitud produce `ERROR` y no crea el destino. Si el bloque que
completa la carga contiene caracteres Base64 adicionales, también se rechaza;
solo se permiten espacios o saltos de línea tras el contenido esperado dentro de
ese bloque.

Cuando el ejecutor use una terminal interactiva, desactiva el eco antes de enviar
el contenido. No cierres ni reutilices el canal hasta que la ayuda haya informado
`OK` o `ERROR` y terminado.

La ayuda:

- rechaza entradas que excedan el límite;
- valida sintaxis Base64, tamaño exacto y SHA-256;
- no sobrescribe un destino existente;
- publica la salida solo después de verificarla;
- elimina el archivo parcial cuando falla.

Continúa únicamente si termina con código cero e informa `OK`, el tamaño esperado
y el SHA-256 esperado.

## Archivos de texto auxiliares

Para `unidades.yaml` y otros archivos de texto, confirma primero el ID, la ruta
lógica, el MIME y el tamaño exacto que devuelve Drive. El límite es 1 MiB
(1.048.576 bytes).

Usa `scripts/materialize_drive_text.py` y entrega el texto UTF-8 autenticado por
la entrada estándar:

```bash
python scripts/materialize_drive_text.py "$TEMP_DIR/unidades.yaml" \
  --expected-size 4950
```

No uses `python -` como escritor, porque consume la misma entrada estándar que
debe recibir el texto. No improvises otro proceso ni calcules un hash previo
analizando la salida visible del terminal.

La ayuda valida UTF-8, tamaño exacto y límite, no sobrescribe destinos y publica
el archivo de forma atómica. También calcula el SHA-256 para el informe. Continúa
solo si termina con código cero e informa `OK`. No conviertas una referencia
interna del PDF en texto.

## Limpieza

Después de ejecutar y comprobar `render_unit.py`, elimina el PDF temporal, el YAML
temporal y cualquier Base64 intermedio. Conserva únicamente el resultado que el
usuario haya pedido. No añadas copias temporales al repositorio.

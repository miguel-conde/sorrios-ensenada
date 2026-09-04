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
2. Solicita primero el archivo con `google_drive_fetch`, usando la URL canónica y:

   - `download_raw_file=true`;
   - `include_base64=false`.

3. Si el conector entrega un `workspace_path` accesible al ejecutor local, úsalo
   y valida su tamaño y SHA-256 antes de continuar.
4. Si solo entrega una referencia interna `sediment://` que WSL no puede abrir,
   aplica el fallback Base64 limitado.

No abras referencias internas con el navegador. No uses una URL pública o
construida a mano de Drive. No uses `curl` o `wget` con la URL canónica de Drive.

## Fallback Base64 limitado

Usa `scripts/materialize_drive_payload.py` dentro de una única ejecución en modo
código que coordine Drive y la terminal. Inicia la ayuda antes de solicitar el
Base64. Mantén `b64_string` en una variable interna de esa ejecución: no lo
muestres, registres, incluyas en órdenes ni guardes en un archivo auxiliar.

### Windows a WSL

Inicia la ayuda con `exec_command`, `tty=true` y esta única orden:

```text
wsl.exe -e bash -c 'stty -echo -icanon min 1 time 0 && exec <PYTHON> <SCRIPT> <DESTINO> --expected-size <TAMAÑO> --expected-sha256 <HASH>'
```

El shell solo desactiva el eco y el modo canónico antes de reemplazarse por
Python. No uses `bash -lc`, no añadas `exit` ni encadenes más órdenes.

### Ejecutor dentro de WSL

Usa la misma TTY y la misma orden, sin el prefijo `wsl.exe -e`:

```text
bash -c 'stty -echo -icanon min 1 time 0 && exec <PYTHON> <SCRIPT> <DESTINO> --expected-size <TAMAÑO> --expected-sha256 <HASH>'
```

Sustituye todos los marcadores `<...>` por valores ya comprobados antes de
ejecutar la orden; no los uses de forma literal.

### Coordinación de Drive y la TTY

1. Exige que `exec_command` devuelva un `session_id` y que la ayuda siga activa.
2. Solo entonces llama a `google_drive_fetch` con la URL canónica,
   `download_raw_file=true` e `include_base64=true`.
3. Antes de enviar datos, comprueba el ID, MIME y tamaño devueltos. Comprueba
   también que la longitud de `b64_string` sin espacios ASCII, tabuladores ni
   saltos de línea sea `4 × ceil(expected_size / 3)`.
4. Envía `b64_string` al `session_id` mediante `write_stdin`, en bloques
   consecutivos de 32.768 caracteres como máximo. No añadas saltos, EOF, Ctrl-D,
   `exit` ni ningún otro contenido.
5. Tras el último bloque, no escribas más en el canal. Espera el mensaje `OK` y
   el fin autónomo del proceso.

Detente antes de enviar el Base64 si no existe `session_id`, si no pueden
desactivarse el eco y el modo canónico, o si no puede usarse `write_stdin`.

Si falla la descarga, una comprobación o el envío después de abrir la TTY,
termina el proceso mediante el control de la sesión del ejecutor, espera su
cierre y elimina el destino y cualquier archivo parcial. No envíes `exit`,
Ctrl-D ni otras órdenes por stdin para cerrarlo.

Cuando se proporciona `--expected-size`, la ayuda calcula la longitud Base64
estándar como `4 × ceil(expected_size / 3)`. Lee los bytes disponibles por bloques,
ignorando únicamente espacios ASCII, tabuladores y saltos de línea, y termina en
cuanto recibe ese número de caracteres Base64: no necesita esperar a EOF. Un EOF
anterior a esa longitud produce `ERROR` y no crea el destino. Si el bloque que
completa la carga contiene caracteres Base64 adicionales, también se rechaza;
solo se permiten espacios o saltos de línea tras el contenido esperado dentro de
ese bloque.

La ayuda:

- rechaza entradas que excedan el límite;
- valida sintaxis Base64, tamaño exacto y SHA-256;
- no sobrescribe un destino existente;
- publica la salida solo después de verificarla;
- elimina el archivo parcial cuando falla.

Continúa únicamente si termina con código cero e informa `OK`, el tamaño esperado
y el SHA-256 esperado. Comprueba de nuevo el tamaño y el SHA-256 del archivo
materializado antes de usarlo.

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

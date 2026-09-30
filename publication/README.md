# Publicación Quarto

`publication/` es la capa de composición del libro en HTML y PDF. No es una
fuente histórica ni editorial: las autoridades permanecen bajo `project/` y
el manuscrito autoritativo permanece en Google Drive, en modo de solo lectura.

## Qué se edita y qué se genera

- `content/` contiene texto editorial del libro revisado por personas.
- `meta/` congela el snapshot y describe capítulos, índices y recursos.
- `scripts/` prepara y valida derivados sin escribir en `project/`.
- `generated/` contiene derivados reproducibles y nunca se edita a mano.
- `_book/` contiene la salida de Quarto.

`generated/` y `_book/` están ignorados por Git. Tampoco se confirma en el
repositorio ningún PDF fuente, PDF de referencia ni derivado facsimilar.

## Requisitos

- Quarto;
- una versión compatible de Python 3;
- PyYAML y Pillow, ya declarados por el plugin para el render de unidades;
- Poppler (`pdftoppm` y `pdfinfo`);
- una distribución LaTeX con LuaLaTeX para generar el PDF.

No se deben instalar dependencias desde los scripts. Si falta alguna, hay que
diagnosticar el componente ausente y obtener autorización antes de instalarlo.

El entorno Python recomendado se crea una vez desde la raíz:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -e 'plugins/sorrios-ensenada[render,test]'
source .venv/bin/activate
```

`.venv/` está ignorado. No actualices dependencias fuera de las restricciones
declaradas por el repositorio.

## Réplica local del manuscrito

La composición utiliza una réplica persistente y verificada del PDF autoritativo
fuera del checkout. La ubicación predeterminada es:

```text
~/.local/share/sorrios-ensenada/manuscript.pdf
```

Puede cambiarse para una sesión mediante `SORRIOS_MANUSCRIPT_PDF`; en sistemas
con `XDG_DATA_HOME`, se usa `$XDG_DATA_HOME/sorrios-ensenada/manuscript.pdf`.
`prepare.py` rechaza rutas dentro del checkout y comprueba tamaño, SHA-256 y 18
páginas antes de generar derivados. No descarga Drive ni escribe en `project/`.
Si la copia falta o no coincide, debe renovarla manualmente el usuario.

Drive conserva la autoridad. La réplica local solo evita transferencias repetidas
durante la composición y nunca se incorpora a Git. El PDF completo 0.6 puede
guardarse en el mismo directorio con el nombre `composition-0.6.pdf`, únicamente
como referencia visual y sin conexión automática con los generadores.

## Comandos desde la raíz del repositorio

```sh
source .venv/bin/activate
.venv/bin/python publication/scripts/prepare.py
.venv/bin/python publication/scripts/prepare.py
.venv/bin/python publication/scripts/validate_publication.py
quarto check
quarto preview publication
quarto render publication --to html
quarto render publication --to pdf
quarto render publication
.venv/bin/python publication/scripts/validate_publication.py --rendered
```

La salida se escribe en `publication/_book/`. Si falla el HTML, se debe revisar
primero `quarto check`, el manifiesto y la preparación. Si falla el PDF, se
debe comprobar LuaLaTeX sin cambiar fuentes canónicas.

La página facsimilar y el recorte son derivados regenerables: deben permanecer
bajo `publication/generated/` y no se versionan. La réplica local del manuscrito
puede conservarse fuera del checkout para las siguientes sesiones.

La arquitectura estable se documenta en el
[plan maestro](../docs/PLAN_MAESTRO_PUBLICACION_QUARTO.md) y la única tarea
vigente se mantiene en el
[roadmap](../docs/ESTADO_PUBLICACION_QUARTO.md).

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

## Entrada temporal del manuscrito

La Fase 2B exige una copia temporal verificada del PDF autoritativo fuera del
repositorio. Su ruta se entrega solo mediante la variable de entorno:

```sh
export SORRIOS_MANUSCRIPT_PDF="<PDF_TEMPORAL_VERIFICADO>"
```

`prepare.py` comprueba tamaño, SHA-256 y 18 páginas antes de generar la página
12, el recorte `folio_315v` y las páginas Quarto del prototipo. No descarga
Drive, no escribe en `project/` y reconstruye por completo `generated/`.

## Comandos desde la raíz del repositorio

```sh
publication/scripts/prepare.py
publication/scripts/prepare.py
python publication/scripts/validate_publication.py
quarto check
quarto preview publication
quarto render publication --to html
quarto render publication --to pdf
```

La salida se escribe en `publication/_book/`. Si falla el HTML, se debe revisar
primero `quarto check`, el manifiesto y la preparación. Si falla el PDF, se
debe comprobar LuaLaTeX sin cambiar fuentes canónicas.

La página facsimilar y el recorte son derivados temporales: deben permanecer
bajo `publication/generated/`, no se versionan y se eliminan junto con la copia
temporal del manuscrito después de la validación.

La arquitectura estable se documenta en el
[plan maestro](../docs/PLAN_MAESTRO_PUBLICACION_QUARTO.md) y la única tarea
vigente se mantiene en el
[roadmap](../docs/ESTADO_PUBLICACION_QUARTO.md).

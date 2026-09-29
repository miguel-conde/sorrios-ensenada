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
- una distribución LaTeX con LuaLaTeX para generar el PDF.

No se deben instalar dependencias desde los scripts. Si falta Quarto o LaTeX,
hay que diagnosticar el componente ausente y obtener autorización antes de
instalarlo.

## Comandos desde la raíz del repositorio

```sh
quarto check
quarto preview publication
quarto render publication --to html
quarto render publication --to pdf
```

La salida se escribe en `publication/_book/`. El script de pre-render
`publication/scripts/prepare.py` comprueba el manifiesto y crea
`publication/generated/` cuando es necesario.

Si falla el HTML, se debe revisar primero la salida de `quarto check` y las
rutas declaradas en `meta/publication.yml`. Si falla el PDF, se debe comprobar
la disponibilidad de LuaLaTeX y de la distribución LaTeX sin cambiar las
fuentes canónicas. La descarga PDF del HTML solo es utilizable después de un
render PDF correcto; no se debe publicar una salida HTML que apunte a un PDF
ausente.

La arquitectura estable se documenta en el
[plan maestro](../docs/PLAN_MAESTRO_PUBLICACION_QUARTO.md) y la única tarea
vigente se mantiene en el
[roadmap](../docs/ESTADO_PUBLICACION_QUARTO.md).

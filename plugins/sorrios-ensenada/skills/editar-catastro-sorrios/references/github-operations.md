# Operaciones GitHub

## Principios

- GitHub es el workspace de lectura y escritura.
- Toda lectura que forme parte de una operación debe quedar ligada a un mismo `base_sha`.
- Una operación multiarchivo se publica como un solo commit.
- No se usa `force=true` en el flujo normal.
- Si la rama objetivo cambia antes de publicar, se aborta la publicación y se reconcilia desde el nuevo SHA.

## Operación multiarchivo

1. Lee la rama objetivo y fija `base_sha`.
2. Lee controles y todos los archivos afectados desde `base_sha`.
3. Prepara todos los contenidos nuevos sin modificar la rama.
4. Valida estructura, invariantes editoriales y conjunto de rutas que cambiarán.
5. Crea los blobs necesarios.
6. Crea un árbol basado en el árbol de `base_sha`.
7. Crea un único commit cuyo padre sea `base_sha`.
8. Vuelve a leer la rama objetivo.
9. Si su SHA ya no es `base_sha`, no muevas el ref; relee y reconcilia.
10. Si sigue siendo `base_sha`, mueve el ref al nuevo commit con actualización no forzada.
11. Vuelve a leer la rama y verifica el commit y todos los archivos afectados.

El commit puede prepararse antes del paso 8 porque todavía no es visible desde ninguna rama. Publicar significa mover el ref.

## Cambio de un solo archivo

Puede usarse la API de contenidos si:

- solo cambia un archivo;
- se leyó su SHA actual desde la rama objetivo;
- la actualización exige ese SHA previo;
- el cambio no forma parte de una operación que deba ser atómica con otros archivos.

## Concurrencia

Si dos sesiones parten de `X`, ambas pueden preparar commits con padre `X`. Tras publicar una de ellas, la otra debe detectar que la rama ya no apunta a `X` y no publicar su commit. Debe releer y reconciliar.

## Verificación

Tras publicar, comprueba como mínimo:

- SHA de la rama;
- padre del commit;
- lista exacta de archivos cambiados;
- contenido o blob SHA de cada archivo crítico;
- invariantes de `estado.yaml` y `unidades.yaml`;
- ausencia de PDF en el repositorio.

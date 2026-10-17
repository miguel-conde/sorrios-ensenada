# Sorríos — Catastro de Ensenada

Este repositorio reúne las fuentes y las herramientas del proyecto editorial
**Sorríos — Catastro de Ensenada** y del libro en preparación *Sorribos y
Santibáñez de Ordás en 1752. Estudio histórico y edición integral del Catastro
de Ensenada*.

Sorríos es el nombre actual del lugar que el expediente de 1752 denomina
*Sorribos*. El proyecto estudia ese expediente y ofrece su edición para hacer
accesible tanto el documento como el contexto histórico que permite
interpretarlo.

## Qué contiene el repositorio

- las fuentes editoriales y la edición del expediente;
- el estudio histórico y sus aparatos de consulta;
- scripts de preparación, comprobación y generación;
- documentación metodológica y registros de decisiones y validaciones;
- recursos reproducibles de la publicación, incluida su cartografía.

La organización técnica y las reglas de autoridad se explican en
[`PROJECT.md`](PROJECT.md). La construcción del libro se documenta en
[`publication/README.md`](publication/README.md).

## Qué no contiene

El repositorio no incluye el PDF manuscrito autoritativo, facsímiles o recortes
derivados de él, salidas HTML/PDF renderizadas, secretos ni credenciales. El
manuscrito se mantiene como fuente externa y no se redistribuye mediante Git.

## Reproducibilidad

La preparación y la validación emplean Python; la composición del libro emplea
Quarto. Las fuentes versionadas se mantienen separadas de los derivados
generados. Los controles locales permiten comprobar esa separación y regenerar
los componentes para los que se disponga de las entradas autorizadas.

La reproducción integral del libro requiere acceso legítimo al manuscrito
externo y, por tanto, no puede obtenerse únicamente clonando este repositorio.
Las instrucciones técnicas están en [`publication/README.md`](publication/README.md).

## Licencias

- El software, los scripts, los tests, las herramientas y la configuración
  ejecutable se ofrecen bajo [licencia MIT](LICENSE).
- El contenido y la documentación originales se ofrecen, con el alcance allí
  definido, bajo [CC BY 4.0](LICENSE-CONTENT.md).
- Las atribuciones, los materiales de terceros y las exclusiones se detallan
  en [`NOTICE`](NOTICE).

GitHub puede mostrar MIT como licencia del repositorio porque `LICENSE`
corresponde al software. Esa indicación no implica que todos los componentes
estén bajo MIT.

## Correcciones y contacto

Las erratas, propuestas de corrección y problemas técnicos pueden comunicarse
mediante GitHub Issues, usando las plantillas disponibles. El canal principal
de contacto es:

`miguelco2000@gmail.com`

## Estado

El proyecto se encuentra en preparación y cierre editorial. Este repositorio
no declara todavía publicada la edición 1.0.

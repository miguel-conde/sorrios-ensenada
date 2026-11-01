# Sorríos — Catastro de Ensenada

Este repositorio reúne las fuentes, el código y la documentación del **Proyecto
Sorríos — Catastro de Ensenada** y de la obra:

> Miguel Conde de Simón, *Sorribos y Santibáñez de Ordás en 1752: Estudio
> histórico y edición integral del Catastro de Ensenada*, versión 1.0, 2026.

La edición estudia el expediente de Sorribos y Santibáñez de Ordás levantado en
1752 para el Catastro de Ensenada. Presenta conjuntamente el facsímil, la
transcripción paleográfica revisada, una edición en español actual, el estudio
histórico y los aparatos que permiten comprobar las fuentes y la evidencia.

La URL canónica de la obra es
<https://sorribos-santibanez-1752.netlify.app/>. El repositorio corresponde a
la versión 1.0 y al año editorial 2026; el estado operativo vigente se registra
en [el checkpoint editorial](docs/CHECKPOINT_REANUDACION_PREVIEW_FINAL.md). La
versión 1.0 está publicada desde el **1 de noviembre de 2026** y su URL
canónica vigente es <https://sorribos-santibanez-1752.netlify.app/>.

La edición 1.0 es una publicación digital no comercial, de libre acceso en
HTML y PDF. Por decisión editorial no se solicitará ISBN para esta versión. La
decisión solo se reconsiderará si una edición futura entra en un circuito
comercial.

## Objetivo y alcance

El proyecto busca hacer accesible el documento de 1752 sin separar su lectura
de la posibilidad de comprobarla. Para ello conserva distintas capas con
funciones propias:

- el manuscrito como fuente material autoritativa;
- la edición crítica y la transcripción paleográfica;
- la modernización para facilitar la lectura;
- el estudio histórico, con separación explícita entre datos, cálculos,
  interpretaciones, contexto externo y límites;
- el facsímil y los aparatos de consulta, citas, concordancias e índices.

`Sorribos` es la forma documentada en el expediente de 1752; `Sorríos` es el
nombre actual del lugar y da nombre al proyecto.

## Estructura del repositorio

- [`project/`](project/) contiene las fuentes canónicas de investigación y
  edición: controles, método, edición crítica, estudio histórico, registro de
  evidencia, edición modernizada, glosario e índices.
- [`publication/`](publication/) contiene la capa de composición Quarto: texto
  editorial, metadatos, estilos, recursos, generadores y validadores.
- [`docs/`](docs/) conserva planes, decisiones, auditorías y evidencia técnica
  y editorial.
- [`plugins/sorrios-ensenada/`](plugins/sorrios-ensenada/) contiene las
  herramientas portables del expediente.
- [`tests/`](tests/) verifica los contratos canónicos, editoriales y de
  publicación.
- [`.github/`](.github/) reúne instrucciones de contribución y plantillas de
  incidencias.

`project/` y `publication/` no son capas intercambiables. Los hechos, lecturas
y datos canónicos se corrigen primero en su autoridad bajo `project/`; la capa
de publicación los compone para el lector sin sustituirlos.

## Qué contiene y qué no contiene

El repositorio contiene las fuentes textuales versionadas, el código de
generación y validación, la configuración de la publicación, la cartografía
reproducible y la documentación de trazabilidad.

No contiene:

- el PDF manuscrito autoritativo, conservado fuera de Git;
- las páginas y recortes facsimilares generados desde ese PDF;
- `publication/generated/`, que se reconstruye automáticamente;
- `publication/_book/`, que contiene las salidas HTML y PDF;
- credenciales, secretos ni otros binarios externos no redistribuibles.

La ausencia de estos derivados es deliberada. Clonar el repositorio no basta
para reconstruir el facsímil sin disponer legítimamente del manuscrito externo
declarado por el proyecto.

## Reproducir la publicación

La guía operativa detallada está en
[`publication/README.md`](publication/README.md). Las dependencias principales
son:

- Python 3.10 o posterior;
- Quarto;
- LuaLaTeX, normalmente mediante TinyTeX;
- Poppler (`pdftoppm`, `pdfinfo` y `pdftotext`);
- `rsvg-convert` para la conversión de cartografía SVG durante el PDF.

Desde la raíz del repositorio puede prepararse el entorno Python con:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -e 'plugins/sorrios-ensenada[render,test]'
source .venv/bin/activate
```

La réplica autorizada del manuscrito debe residir fuera del checkout y coincidir
con los metadatos de `project/00_CONTROL/proyecto.yaml`. La ruta predeterminada
es `$XDG_DATA_HOME/sorrios-ensenada/manuscript.pdf` o, si esa variable no está
definida, `~/.local/share/sorrios-ensenada/manuscript.pdf`.

Cuando `publication/generated/` no existe, debe ejecutarse el bootstrap antes
de invocar Quarto:

```sh
source .venv/bin/activate
python publication/scripts/prepare.py
quarto check
quarto render publication
python publication/scripts/validate_publication.py --rendered
```

`prepare.py` verifica el manuscrito y reconstruye los derivados ignorados.
Quarto ejecuta de nuevo esa preparación mediante su `pre-render`, lo que
permite comprobar que la generación es reproducible. Ningún paso escribe en
`project/` ni incorpora el manuscrito o `_book/` al historial Git.

## Cómo citar

Para el volumen completo:

> Conde de Simón, Miguel. *Sorribos y Santibáñez de Ordás en 1752: Estudio
> histórico y edición integral del Catastro de Ensenada*. Versión 1.0, 2026.
> <https://sorribos-santibanez-1752.netlify.app/>.

La obra contiene modelos específicos para citar el facsímil, folios, unidades,
respuestas, capítulos y entradas de la matriz de evidencia. Los modelos
vigentes están en la sección «Cómo citar» de la publicación.

## Licencias y materiales de terceros

- El contenido y la documentación originales se ofrecen, dentro del alcance
  definido, bajo [CC BY 4.0](LICENSE-CONTENT.md).
- El software, los scripts, los tests y la configuración ejecutable se ofrecen
  bajo [licencia MIT](LICENSE).
- El facsímil, las reproducciones documentales, la cartografía, las imágenes,
  las citas y otros materiales de terceros conservan sus propias condiciones.
  Las atribuciones y exclusiones se detallan en [`NOTICE`](NOTICE).

GitHub puede identificar MIT como licencia principal porque `LICENSE`
corresponde al software; esa indicación no extiende MIT al contenido editorial
ni a materiales de terceros.

## Correcciones y contacto

Las erratas, propuestas de corrección y problemas técnicos pueden comunicarse
mediante [GitHub Issues](https://github.com/miguel-conde/sorrios-ensenada/issues).
El canal principal de contacto es <miguelco2000@gmail.com>.

Las lecturas, interpretaciones y decisiones editoriales son responsabilidad
final de Miguel Conde de Simón.

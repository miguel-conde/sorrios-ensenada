# PKG-04 — Prototipo F3

## 1. Problema editorial

La composición vigente presenta el manuscrito completo en la Parte III y vuelve a
mostrar, en la Parte IV, un recorte documental grande por cada una de las 35
unidades paleográficas. Las dos vistas cumplen funciones distintas, pero en PDF
la segunda reproducción adquiere un peso visual cercano al del facsímil y produce
una repetición extensa.

F3 no elimina ninguna de las dos funciones. Conserva la página completa como
reproducción documental principal y mantiene cada unidad vinculada a su imagen,
su localización y su transcripción. La economía se aplica solo a la presentación
PDF de la unidad.

## 2. Hipótesis F3

- **HTML:** página completa en el facsímil; recorte completo al 74 % en la
  transcripción; ampliación mediante el lightbox nativo de Quarto y un enlace
  local alternativo; navegación directa en ambos sentidos.
- **PDF:** página completa en el facsímil; localizador derivado al 28 % en la
  transcripción; página y posición expresadas en texto; enlaces internos al
  facsímil; transcripción y aparato completos.

La semántica documental es única. La selección de la variante visual se realiza
por formato en el mismo QMD generado.

## 3. Muestra seleccionada

| Página | Unidad | Posición | Razón de selección |
|---:|---|---|---|
| 12 | `folio_315v` (orden 22) | izquierda | Reutiliza la infraestructura trazable de Phase 2B y ofrece texto suficientemente denso. |
| 12 | `folio_316r` (orden 23) | derecha | Completa el par real de la misma página y permite probar la relación página 1 → N unidades. |

La selección deriva de `project/00_CONTROL/unidades.yaml`. No responde a una
nueva interpretación histórica ni altera el mapeo canónico.

## 4. Baseline actual

En el HTML productivo, la Parte III muestra la página completa y la Parte IV
repite cada mitad como imagen al 62 % antes de su transcripción. El PDF aplica
la misma pauta visual. Para la muestra, la candidata existente sitúa
`folio_315v` en la página PDF 171, `folio_316r` en la 174 y la unidad siguiente
en la 177: las dos unidades ocupan seis páginas de transcripción (171–176).

La candidata de referencia tiene 334 páginas y 73.994.496 bytes. Estas cifras
describen el volumen completo y no deben compararse como tamaño absoluto con un
mini-libro de dos unidades.

## 5. Prototipo HTML

El mini-libro conserva la página digital 12 completa al 88 % y enumera sus dos
unidades. Cada enlace abre directamente el anchor de la unidad correspondiente.

La transcripción presenta el recorte completo al 74 %, caption y texto de
localización. La imagen activa el lightbox local incluido por Quarto; además se
ofrece el enlace accesible `Ampliar el recorte completo…`, que abre el PNG local
sin depender de JavaScript. Cada unidad enlaza de vuelta a la página 12.

La inspección de escritorio y la emulación móvil a 390 × 844 px fueron
satisfactorias. En la emulación, `innerWidth`, `document.scrollWidth` y
`body.scrollWidth` fueron 390 px; no hubo desbordamiento horizontal. El primer
intento con `--window-size=390` no era representativo porque Chrome headless
impone un viewport mínimo de 500 px; se comprobó mediante el protocolo de
depuración y se repitió con emulación real.

## 6. Prototipo PDF

El PDF conserva la página completa como reproducción principal. En cada unidad
la imagen grande se sustituye por un localizador al 28 %, seguido de la
identificación textual de la página y la posición izquierda/derecha. La
transcripción y todas sus secciones permanecen completas.

El render final tiene 10 páginas, formato letter, 4.746.893 bytes y SHA-256
`b1a7b7a7a6d4c2a86ca2a94434157ba834d3cf847d5cc1dddca49474b6dab2fc`.
La inspección de las páginas 3, 5 y 8 confirmó que la página completa, ambos
localizadores, la transcripción y los pies no colisionan. El localizador es
reconocible, pero queda claramente subordinado al texto.

La extracción de anotaciones del PDF compilado verificó enlaces desde el
facsímil a `folio_315v` (página PDF 5) y `folio_316r` (página PDF 7), y enlaces
de retorno desde ambas unidades al facsímil (página PDF 3). No se da por válida
la navegación solo por la presencia de enlaces en QMD.

## 7. Anchors y relaciones

Se reutilizan las convenciones estables existentes:

- página: `pagina-digital-12`;
- unidad izquierda: `folio-315v`;
- unidad derecha: `folio-316r`.

La página consulta todas las unidades asociadas en el manifiesto y genera dos
enlaces salientes. Cada unidad conserva `pdf_page=12` y su posición declarada, y
genera al menos un enlace de retorno. No se fuerza una relación 1:1.

## 8. Reproducibilidad

`publication/scripts/build_f3_prototype.py` construye el mini-libro dentro de
`publication/generated/f3-prototype/`. Primero lee las unidades y la edición
crítica; después reutiliza los derivados reproducibles de 4A y 4B. La escritura
se realiza en un directorio temporal y se sustituye como una unidad. No hay
recortes manuales, rutas absolutas, CDN ni dependencia nueva.

`publication/scripts/prepare.py` ejecuta F3 después del facsímil y de la
transcripción, por lo que sus tres imágenes siempre proceden de esos generadores.
Produce ocho salidas ignoradas: configuración, dos QMD, tres PNG y dos archivos
de estilo.

Comandos de evaluación:

```bash
.venv/bin/python publication/scripts/build_f3_prototype.py
quarto render publication/generated/f3-prototype --to html
quarto render publication/generated/f3-prototype --to pdf
```

Hashes de los derivados principales:

| Derivado | SHA-256 |
|---|---|
| `_quarto.yml` | `975223f8b354326079ce3aa8d1cb86e2c093cdd667d415fcce9fa18105140032` |
| `index.qmd` | `7450fb4a47beb79a337d4188a507107585b1eb5cfb262fd4bc5314102c038b30` |
| `transcripcion-f3.qmd` | `0e6f18d09eea0aa8845389e67cc5846d1ac23f6c79716439f354c860c57c960f` |
| `page-12.png` | `c56d83bbaa826ae2f253aaa2d1fb0b0be4095c3a56c32c15ce24041037de4083` |
| `folio_315v.png` | `5e3779962ef5180bab36ff7dc132c641484e55e8b772a4accc31db157220e0cc` |
| `folio_316r.png` | `a3fc272812e430d039a5e77da7b269873b14e0d062b4d0f04dd5631b347a4d50` |

El manuscrito de entrada sigue siendo la réplica verificada de 18 páginas, file
ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u` y SHA-256
`d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`.

La baseline previa fue de 585 tests. El cierre del prototipo registra 46 tests
focales de PKG-04 y Phase 4A/4B, y una suite completa de 597 tests, todos en
PASS. También finalizaron en PASS `validate_project.py`, `check_sources.py`,
`validate_publication.py`, la cartografía con `--check`, la compilación Python y
`git diff --check`.

## 9. Accesibilidad

HTML incluye textos alternativos, captions, página y posición expresadas en
texto, nombres accesibles para los enlaces de ampliación y un acceso directo a
la imagen que no depende del lightbox. La ampliación usa el componente nativo de
Quarto, con controles de teclado, sin librería externa adicional. Esta revisión
no constituye una declaración formal de conformidad WCAG.

El PDF incluye captions, referencias textuales y enlaces comprensibles; la
identificación no depende solo de la miniatura. Sigue sin ser PDF/UA y
`pdfinfo` informa `Tagged: no`, limitación conocida que PKG-04 no reabre.

## 10. Comparación

| Criterio | Actual | F3 HTML | F3 PDF |
|---|---|---|---|
| Fidelidad | Página y crop completo | Igual; crop completo | Página completa y localizador derivado |
| Comprobabilidad | Alta, sin enlace directo entre vistas | Alta y ampliable, con ida y vuelta | Conservada mediante localizador, texto y enlace |
| Redundancia | Crop grande al 62 % también en PDF | Deliberada para consulta en pantalla | Reducida: localizador al 28 % |
| Legibilidad | Buena, con alto peso de imagen | Mejor superficie de comprobación (74 %) | Texto dominante; localizador reconocible |
| Navegación | Separación por partes | Un clic en ambos sentidos | Enlaces internos compilados en ambos sentidos |
| Tamaño/ocupación | Dos crops grandes; seis páginas para la muestra | Dos crops completos | Dos localizadores; seis páginas para la transcripción de la muestra |
| Accesibilidad | Alt/captions existentes | Añade contexto, ampliación nombrada y retorno | Texto suficiente; conserva la limitación de PDF no etiquetado |
| Complejidad técnica | Un tratamiento para ambos formatos | Visibilidad condicional nativa | Misma capa semántica, sin dependencia nueva |

F3 gana jerarquía visual, orientación y navegación. En PDF pierde detalle
inmediato en el localizador, pero el detalle completo permanece en el facsímil
y se alcanza con un enlace interno. No reduce el número de páginas de esta
muestra: el beneficio observado es editorial, no una compresión forzada.

## 11. Métricas

- **Imágenes asociadas a la página:** el modelo actual y F3 muestran una página
  y dos derivados. En el modelo actual los dos derivados son reproducciones
  grandes; en F3 PDF hay una sola reproducción principal y dos localizadores.
- **Anchura en transcripción:** actual 62 %; F3 HTML 74 %; F3 PDF 28 %.
- **Área visual aproximada del localizador:** a igual proporción de imagen,
  `(28 / 62)² = 20,4 %` del área del crop actual, una reducción aproximada del
  79,6 %. Es una estimación de maquetación, no de píxeles fuente.
- **Páginas PDF de transcripción de la muestra:** seis en la candidata actual
  (171–176) y seis en el prototipo (5–10). F3 no optimiza el paginado a costa de
  la lectura.
- **Navegación:** dos enlaces directos desde la página a sus unidades; retorno
  desde cada unidad en un clic. El PDF incluye además la referencia del
  localizador.
- **Archivos:** candidata completa, 73.994.496 bytes; mini-libro F3,
  4.746.893 bytes. No son magnitudes comparables por alcance y no se usan como
  criterio decisorio.

## 12. Limitaciones

- La muestra cubre dos de las 35 unidades y una de las 18 páginas; no demuestra
  por sí sola todos los extremos de longitud del libro.
- El localizador reutiliza el crop reproducible de media página reducido, sin
  superponer una geometría nueva sobre la página completa.
- El 28 % funcionó con ambas mitades de la muestra; otros casos podrían requerir
  una regla tipográfica parametrizada durante el despliegue global.
- El PDF no está etiquetado formalmente.
- La candidata completa no se regeneró: la comparación utiliza el PDF 1.0
  existente y el mini-libro autorizado.
- Los outputs HTML, PDF y capturas son temporales e ignorados; no constituyen
  artefactos versionados.

## 13. Decisión propuesta

`F3-APROBAR`

La propuesta satisface los criterios del paquete: preserva facsímil y texto,
mantiene o mejora la comprobabilidad HTML, reduce de forma clara la duplicación
visual en PDF, ofrece un localizador útil, compila navegación bidireccional,
conserva mapeos y anchors, no modifica `project/`, no añade dependencias y se
regenera mediante `prepare.py`. La decisión definitiva y el despliegue sobre las
35 unidades quedan expresamente pendientes de revisión humana.

# PKG-09 — Identidad final, metadatos y colofón

## Estado y alcance

**Estado:** `COMPLETADO EN RAMA AISLADA — PENDIENTE DE REVISIÓN E
INTEGRACIÓN`<br>
**Base:** `61f91b1a6b378fb66c31fdecb4628815efec9b1d`<br>
**Rama:** `pkg-09/final-identity-metadata-colophon-v1`

El paquete consolida exclusivamente la identidad visible y bibliográfica, los
metadatos editoriales, los créditos, los derechos, los modelos de cita y el
colofón. No modifica `project/`, contenido histórico, el aparato visual de
PKG-07 ni los aparatos de PKG-08; tampoco inicia GATE-02, PKG-10 o el release.

## Identidad consolidada

- Título: *Sorribos y Santibáñez de Ordás en 1752*.
- Subtítulo: *Estudio histórico y edición integral del Catastro de Ensenada*.
- Autor: Miguel Conde de Simón.
- Forma bibliográfica: Conde de Simón, Miguel.
- Identidad visible: Proyecto Sorríos — Catastro de Ensenada.
- Versión editorial: 1.0, con estado de prepublicación.

La landing HTML, la portada PDF, los créditos, los modelos de cita, el
manifiesto de publicación y el colofón emplean esta misma identidad.

## Créditos, derechos y licencia

Los cuatro roles aprobados —autoría, investigación y dirección editorial;
edición crítica; transcripción paleográfica y revisión; edición modernizada y
revisión— corresponden a Miguel Conde de Simón. No se añaden colaboradores ni
datos humanos no declarados.

El aviso es `© 2026 Miguel Conde de Simón` para el contenido original. La
licencia Creative Commons Attribution 4.0 International (CC BY 4.0) se aplica
solo al contenido original que el autor puede licenciar. No se extiende
automáticamente al facsímil, las reproducciones documentales, la cartografía,
las imágenes, las citas ni otros materiales de terceros, que conservan sus
condiciones propias.

## Elaboración digital y responsabilidad

Créditos y colofón declaran de forma proporcionada el uso de herramientas
digitales y sistemas de inteligencia artificial como apoyo en transcripción,
revisión, análisis, estructuración, comprobación y preparación editorial. No
les atribuyen autoría. Miguel Conde de Simón revisa y asume las decisiones
históricas, paleográficas, editoriales y de publicación y la responsabilidad
final de la obra.

## Diferimientos controlados

- Prólogo definitivo: pendiente de redacción personal antes de la candidata;
  el placeholder controlado permanece intacto.
- Fecha exacta de publicación: se fijará en el release; el año visible es
  2026.
- URL canónica: se fijará en el release.
- ISBN: no es requisito de 1.0 y solo se consignará si llega a existir.

Los once objetos de cita conservan modelos utilizables con marcadores
explícitos para la URL pendiente, sin inventar fecha exacta, URL o ISBN.

## Validación

- Suite focal PKG-09/PKG-06/PKG-08: `40 passed`, 0 fallos y 0 errores.
- Suite completa: `678 passed`, 0 fallos y 0 errores.
- Validadores de proyecto, fuentes, cartografía y publicación renderizada:
  PASS.
- `git diff --check`: PASS.
- HTML completo: 39 documentos.
- PDF completo: 355 páginas, 71.020.397 bytes, SHA-256
  `ca6e1eac7ee0b71e6a2b8d013d394f4b591d9074b58d4dd6e2cfe41da7f4d796`.
- Metadatos PDF: título y autor exactos; año 2026 visible en portada. Los
  metadatos Dublin Core de HTML conservan solo `2026`, sin inventar día o mes.
- Revisión visual representativa: landing, créditos, modelos de cita y
  colofón en HTML; portada y páginas 22, 314 y 355 en PDF. Resultado: APTO.

Los renders son artefactos locales de validación ignorados; no constituyen una
nueva candidata formal y no se versionan.

## Integridad y estado siguiente

`project/` permanece intacto. El prólogo, los mapas aprobados, los capítulos y
los aparatos previos no se han reabierto. No hay PDF, capturas, `_book/` ni
contenido de `publication/generated/` versionado. La rama queda preparada para
revisión independiente e integración por avance rápido. `GATE-02` sigue
pendiente.

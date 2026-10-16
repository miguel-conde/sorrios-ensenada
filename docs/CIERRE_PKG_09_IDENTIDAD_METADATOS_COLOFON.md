# Cierre de PKG-09 — Identidad, metadatos y colofón

**Estado:** `COMPLETADO E INTEGRADO`<br>
**Implementación integrada:** `25fb7dcf9a477efe74c178d108d6f182d33a406e`<br>
**Base:** `61f91b1a6b378fb66c31fdecb4628815efec9b1d`<br>
**Integración:** avance rápido estricto en `feature/quarto-book`

## Resultado

La revisión independiente confirmó el título, subtítulo, autor, identidad del
proyecto y roles aprobados. El año visible es 2026; la fecha exacta y la URL
canónica no se han inventado y permanecen diferidas. El ISBN sigue ausente y
no es bloqueante mientras no exista.

El contenido original queda bajo CC BY 4.0. El facsímil, las reproducciones
documentales, la cartografía, las imágenes, las citas y los materiales de
terceros conservan sus condiciones propias. Las herramientas digitales y los
sistemas de inteligencia artificial se declaran como apoyo sin autoría; la
responsabilidad humana final corresponde a Miguel Conde de Simón.

El prólogo permanece como **PLACEHOLDER CONTROLADO PENDIENTE DE REDACCIÓN
PERSONAL**.

## Evidencia e integración

Se reutilizó la evidencia del SHA exacto, con inputs, configuración y entorno
relevante sin cambios:

- focal: `40 passed`;
- smoke poscommit: `9 passed`;
- suite completa: `678 passed`, 0 fallos y 0 errores;
- validadores y `git diff --check`: PASS;
- HTML: 39 documentos;
- PDF: 355 páginas, 71.020.397 bytes, SHA-256
  `ca6e1eac7ee0b71e6a2b8d013d394f4b591d9074b58d4dd6e2cfe41da7f4d796`;
- revisión visual representativa HTML/PDF: APTO.

Tras el fast-forward se ejecutaron el smoke mínimo de PKG-09 y roadmap
(`2 passed`), el validador estático principal y `git diff --check`: PASS. No
se repitieron la suite completa, los renders ni la revisión visual.

## Integridad y estado siguiente

`project/`, el prólogo, la bibliografía, los mapas y los paquetes anteriores
permanecen sin cambios indebidos. No se versionaron `publication/generated/`,
`_book/`, PDF, HTML ni capturas. PKG-06, PKG-07, PKG-08 y PKG-09 están
integrados. `GATE-02` queda pendiente de evaluación formal y PKG-10 no se ha
iniciado.

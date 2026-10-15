# PKG-06 — Preliminares y arquitectura editorial

## Estado

**COMPLETADO EN RAMA AISLADA — PENDIENTE DE REVISIÓN E INTEGRACIÓN.**

- Base: `dc4982714a39f5ac9839d016090a8510bb727f29`.
- Rama: `pkg-06/preliminaries-editorial-architecture-v1`.
- Tipo de operación: T3.
- Sin push, tag, release ni integración.

## Implementación editorial

La composición adopta la arquitectura P3 aprobada: landing HTML breve y
portada PDF propia, seguidas por créditos, prólogo, introducción general y
convenciones de lectura. El macroorden de las seis partes y los capítulos
1–16 permanece intacto.

La identidad pública queda fijada como:

- **Título:** *Sorribos y Santibáñez de Ordás en 1752*.
- **Subtítulo:** *Estudio histórico y edición integral del Catastro de
  Ensenada*.
- **Autor:** Miguel Conde de Simón.
- **Línea de proyecto:** Proyecto Sorríos — Catastro de Ensenada.

La landing ofrece rutas histórica y documental. La introducción explica el
contenido y la relación entre facsímil, transcripción, edición modernizada,
estudio y aparatos, y remite al capítulo 4 para el método detallado. Las
convenciones resumen grafías, páginas y folios, preguntas y respuestas,
D/C/I/E/L y enlaces.

## Créditos, derechos y prólogo

Los créditos atribuyen exclusivamente a Miguel Conde de Simón la autoría,
investigación, dirección editorial, edición crítica, transcripción
paleográfica, modernización y revisión. CC BY 4.0 se limita al contenido
original que el autor puede licenciar; facsímil, reproducciones documentales,
cartografía y otros materiales conservan su régimen propio.

El prólogo mantiene el placeholder explícito
`PENDIENTE DE REDACCIÓN PERSONAL DEL AUTOR`, sin voz autoral ficticia, con el
guion aprobado de seis asuntos. Debe sustituirse antes de `GATE-02` y de una
candidata formal.

## Cierres de capítulos

Los capítulos 9–12 sustituyen el rótulo genérico «Síntesis» por cierres
informativos. Se preservan los anchors `recursos-sintesis`, `fiscal-sintesis`,
`hacienda-sintesis` y `dinero-sintesis`; no se incorporan hechos ni
interpretaciones nuevos. Los capítulos 5–8 y 13 ya conservaban cierres
informativos adecuados.

## Límites e integridad

- El capítulo 4 permanece idéntico byte a byte a la base.
- El árbol canónico `project/` conserva el tree
  `a8ccb6d783e51aafb6493fed9791097d0a678086`.
- `publication/generated/` y `_book/` siguen ignorados y no versionados.
- No se insertan mapas ni se inicia PKG-07.
- No se fija fecha, URL, versión final, ISBN ni metadatos reservados a PKG-09.
- DEC-010 conserva su estructura prevista y sus valores finales diferidos; no
  se crea un colofón incompleto.
- Se preservan PKG-08, F3, PKG-05, la navegación lateral y las 111 entradas
  D/C/I/E/L.

## Validación

- Focal PKG-06 y regresiones modificadas: `14 passed`.
- Suite completa: `661 passed, 0 failed, 0 errors`.
- Validadores estáticos de proyecto, fuentes y publicación: PASS.
- Publicación renderizada y auditoría HTML/PDF: PASS.
- HTML: 38 documentos.
- PDF: 349 páginas; 70.874.656 bytes; SHA-256
  `fed271554628062147f9b5efea9a54468d152e72b298c90176d402525af7be07`.
- Inspección representativa: landing, portada PDF, créditos, prólogo,
  introducción y cierres de capítulos conformes.
- `git diff --check`: PASS.

## Pendientes deliberados

Antes de `GATE-02` debe incorporarse el prólogo personal definitivo y deben
resolverse los diferimientos de derechos y metadatos ya asignados a sus
paquetes. PKG-06 no inicia PKG-07 ni PKG-09 y queda listo únicamente para
revisión independiente e integración posterior.

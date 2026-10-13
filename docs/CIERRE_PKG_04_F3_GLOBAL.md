# PKG-04 — Cierre definitivo F3

## 1. Estado

`COMPLETADO E INTEGRADO`

## 2. Decisión editorial

`F3-APROBAR`

La decisión humana mantiene sin cambios los parámetros aprobados: H1–H5 y
P1–P8 obtuvieron **Sí**.

## 3. Prototipo

- commit: `7c6d6870214cac19b799d57b392bb1b9d347edd1`;
- muestra: página digital 12, `folio_315v` y `folio_316r`;
- HTML H1–H5: **Sí**;
- PDF P1–P8: **Sí**.

## 4. Despliegue global

El commit `61a50987a4ce3d05721834043d4e1c5c6c611a39` desplegó el modelo
aprobado sobre:

- 18/18 páginas digitales;
- 35/35 unidades documentales;
- 35/35 relaciones página ↔ unidad.

## 5. Modelo HTML final aprobado

- facsímil completo;
- crop al 74 % para las 35 unidades;
- lightbox nativo y fallback directo accesible;
- navegación bidireccional página ↔ unidad.

## 6. Modelo PDF final aprobado

- facsímil completo como reproducción documental principal;
- localizador al 28 % para las 35 unidades;
- página digital y posición expresadas en texto;
- navegación interna bidireccional.

## 7. Mapping

La matriz se reconstruye desde `project/00_CONTROL/unidades.yaml`: la página 1
contiene una unidad y las páginas 2–18 contienen dos unidades cada una. Son 18
páginas, 35 unidades y 35 relaciones, sin huérfanas, duplicados ni anchors
duplicados. Se preservan los anchors estables de las unidades.

## 8. Fidelidad documental

La comparación completa de las 35 unidades confirmó identidad de texto,
lineación paleográfica, notas, observaciones, referencias, orden e
identificadores. F3 modifica exclusivamente presentación y navegación. El
manuscrito conserva 18 páginas y SHA-256
`d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`.

## 9. Reproducibilidad

Dos ejecuciones de `publication/scripts/prepare.py` produjeron 141 archivos y
manifiestos SHA-256 idénticos. `publication/generated/` continúa ignorado y no
contiene archivos versionados.

## 10. Render global de validación

- HTML: 30 documentos, 18 páginas facsimilares y 35 unidades, con enlaces,
  assets, lightboxes y fallbacks validados;
- PDF: 335 páginas, 74.041.686 bytes y SHA-256 de esta revisión
  `32652082d64b46fcf97aeea292f1ac3d9fb56bb12569876483ac7f93282b527c`;
- comparación con la candidata anterior: +1 página y +47.190 bytes.

El PDF conserva exactamente páginas y bytes respecto del render global previo.
Su SHA cambia porque LuaLaTeX incorpora `CreationDate` y `ModDate`: el render
previo fue creado el 12 de octubre y el de revisión el 13 de octubre de 2026.

**No constituye nueva candidata formal.** La candidata consolidada se
regenerará posteriormente en PKG-10.

## 11. Tests

- GF3 + PKG-04 + Phase 4A/4B/4D/6A: **126 passed**;
- suite completa: **616 passed**, 0 failed y 0 errors;
- proyecto, fuentes, publicación estática y renderizada, cartografía,
  compilación Python y `git diff --check`: **PASS**.

## 12. Integración Git

La rama `pkg-04/f3-global-v1` partió exactamente de
`18e596bac4047b3cc162236e73fec1917a76eb63`. Su único commit global,
`61a50987a4ce3d05721834043d4e1c5c6c611a39`, se revisó y se integró en
`feature/quarto-book` mediante fast-forward estricto. No se creó commit de
merge y no se hizo push.

## 13. Integridad canónica

Permanecen intactos `project/`, el Glosario, la Edición Crítica, el Estudio
Histórico, el Registro D/C/I/E/L, la cartografía y la bibliografía. El PDF
autoritativo continúa fuera del checkout. Ni `publication/generated/` ni
`publication/_book/` contienen archivos versionados.

## 14. Pendientes no pertenecientes a PKG-04

- `INC-BIB-001`;
- `INC-BIB-002`;
- `REV-024`;
- presentación editorial de `Contexto histórico`;
- cartografía todavía no insertada;
- bibliografía final;
- preliminares y metadata;
- candidata consolidada.

## 15. Siguiente paso

`PKG-05`

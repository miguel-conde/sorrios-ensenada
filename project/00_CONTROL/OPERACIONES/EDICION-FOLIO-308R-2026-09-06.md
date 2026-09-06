# Operación EDICION-FOLIO-308R-2026-09-06

- **Tipo:** edición, validación y cierre documental de unidad
- **Estado:** verified
- **Fecha:** 6 de septiembre de 2026
- **Unidad editorial:** `folio_308r`
- **Rama canónica:** `main`
- **Base SHA:** `d6df4b118c670fddd40e682837314f6ea9af17e8`
- **Manual aplicado:** Manual Editorial v1.6
- **Edición vigente:** v3.5
- **PDF autoritativo:** Drive file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`, página 4 derecha, 5.038.575 bytes, 18 páginas, SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- **Acceso al PDF:** lectura directa del archivo autoritativo obtenido de Google Drive como PDF real; Drive no modificado; sin Base64 y sin OCR

## Resultado editorial

- Leída visualmente la mitad derecha de la página 4 del PDF autoritativo.
- Continuada la cuarta respuesta con las especies sexta a duodécima.
- Se transcriben prados cercados de secano; prados abiertos de regadio; prados abiertos de secano; `Prados entreparedes`; tierras matorrales; `Eras o sitios`; y montes de robles altos y bajos.
- Se conservan las grafías históricas `vn`, `intermision`, `regadio`, `entreparedes`, `comun` y las mayúsculas del manuscrito.
- Se conservan las divisiones visibles `produ-` / `cen`, `pro-` / `ducen`, `pas-` / `to`, `resguar-` / `dar` y `ba-` / `xos`, incluidos los guiones de final de línea.
- `p[o]r` desarrolla la abreviatura visible de la preposición en la décima especie.
- La lectura `Prados entreparedes` se comprueba paleográficamente con la aparición auxiliar `prados De entre paredes` en folio 309r; el cotejo sirve solo para fijar la lectura de 308r y no valida por anticipado 309r.
- La inspección auxiliar del comienzo de folio 308v confirma que la duodécima especie continúa con `reparar los puentes de el Rio`; esta comprobación sirve solo para delimitar la unidad.
- Los puntos y trazos de relleno que prolongan varios renglones carecen de valor verbal y se omiten conforme al criterio vigente para signos no verbales.
- No aparece ningún criterio metodológico nuevo y no quedan dudas abiertas.

## Derivados

- Glosario: actualización de `pelo` con la nueva aparición en folio 308r y alta de `entreparedes`, con definición estrictamente contextual.
- Índices de personas, topónimos, instituciones, medidas y oficios: sin cambios justificados por esta unidad.
- Diario Editorial: registro de la validación, cierre, cotejos auxiliares, continuidad y aplicación de criterios vigentes.

## Archivos de la operación

Modificados:

- `project/00_CONTROL/estado.yaml`
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`
- `project/20_TRABAJO_EDITORIAL/Glosario.md`

Creado:

- `project/00_CONTROL/OPERACIONES/EDICION-FOLIO-308R-2026-09-06.md`

No se modifican el Manual Editorial, `proyecto.yaml`, `unidades.yaml`, `CAMBIOS.md`, ninguno de los cinco índices ni el PDF autoritativo.

## Estado resultante esperado

- `last_validated_unit: folio_308r`
- `last_closed_unit: folio_308r`
- `current_unit: folio_308v`
- `next_unit: folio_309r`
- `current_location.pdf_page: 5`
- `current_location.position: left`
- `open_issues: []`
- `operation.status: clean`

## Criterio de verificación

La operación solo se publica si `main` continúa exactamente en el Base SHA indicado. Tras publicar se verifican el padre del commit, la lista exacta de archivos afectados, el contenido de folio 308r y del Glosario, la coherencia de `estado.yaml` con `unidades.yaml`, la ausencia de PDF en GitHub y el CI completo.

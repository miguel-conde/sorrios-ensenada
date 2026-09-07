# Operación EDICION-FOLIO-308V-2026-09-07

- **Tipo:** edición, validación y cierre documental de unidad
- **Estado:** verified
- **Fecha:** 7 de septiembre de 2026
- **Unidad editorial:** `folio_308v`
- **Rama canónica:** `main`
- **Base SHA:** `cc6c9332dc6aeee260519347f8a65592ef4bfce1`
- **Manual aplicado:** Manual Editorial v1.6
- **Edición vigente:** v3.5
- **PDF autoritativo:** Drive file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`, página 5 izquierda, 5.038.575 bytes, 18 páginas, SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- **Acceso al PDF:** lectura directa del archivo autoritativo obtenido de Google Drive como PDF real; Drive no modificado; sin Base64 y sin OCR

## Resultado editorial

- Leída visualmente la mitad izquierda de la página 5 del PDF autoritativo.
- La unidad continúa la especie duodécima de la cuarta respuesta con `reparar los puentes de el Rio`.
- La especie decimotercera se transcribe como `Soto De negrillos alisos, y fres-` / `nos`, destinado a pasto y aprovechamiento de leña para reparar los puentes y `Puertas` del río del lugar.
- La cuarta respuesta concluye en esta unidad.
- Comienza la quinta respuesta, que clasifica por calidades varias de las especies de tierras ya declaradas, y queda abierta al final de la cara en `prados cercados De secano De segunda, y`.
- La inspección auxiliar del comienzo de folio 309r confirma la continuidad inmediata de la quinta respuesta; este cotejo se utiliza solo para delimitar folio 308v y no valida por anticipado folio 309r.
- Se conservan los puntos tras `13ª.` y `5ª.`, visibles en el manuscrito.
- Se conservan las divisiones visibles `fres-` / `nos`, `decla-` / `radas` y `espli-` / `can`.
- Se conservan las grafías `Ala`, `ay`, `esplican` y `regadio`, así como las mayúsculas y minúsculas del manuscrito.
- Las series de puntos que prolongan los cierres de la cuarta respuesta carecen de valor verbal y se omiten conforme al criterio vigente para signos no verbales.
- No aparece ningún criterio metodológico nuevo y no quedan dudas abiertas.

## Derivados

- Glosario: alta de `negrillos`, con definición estrictamente contextual y sin identificación botánica moderna.
- Índices de personas, topónimos, instituciones, medidas y oficios: sin cambios justificados por esta unidad.
- Diario Editorial: registro de la validación, cierre, continuidad y aplicación de criterios vigentes.

## Archivos de la operación

Modificados:

- `project/00_CONTROL/estado.yaml`
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`
- `project/20_TRABAJO_EDITORIAL/Glosario.md`

Creado:

- `project/00_CONTROL/OPERACIONES/EDICION-FOLIO-308V-2026-09-07.md`

No se modifican el Manual Editorial, `proyecto.yaml`, `unidades.yaml`, `CAMBIOS.md`, ninguno de los cinco índices ni el PDF autoritativo.

## Estado resultante esperado

- `last_validated_unit: folio_308v`
- `last_closed_unit: folio_308v`
- `current_unit: folio_309r`
- `next_unit: folio_309v`
- `current_location.pdf_page: 5`
- `current_location.position: right`
- `open_issues: []`
- `operation.status: clean`

## Criterio de verificación

La operación solo se publica si `main` continúa exactamente en el Base SHA indicado. Tras publicar se verifican el padre del commit, la lista exacta de archivos afectados, el contenido de folio 308v y del Glosario, la coherencia de `estado.yaml` con `unidades.yaml`, la ausencia de PDF en GitHub y el CI completo.

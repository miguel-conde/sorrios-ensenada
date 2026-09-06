# Operación EDICION-REVERSO-PORTADA-2026-09-06

- **Tipo:** edición, validación y cierre documental de unidad
- **Estado:** verified
- **Fecha:** 6 de septiembre de 2026
- **Unidad editorial:** `reverso_portada`
- **Rama canónica:** `main`
- **Base SHA:** `160d81ad2d28b6dc2ea75e7d6b7beb285b03d3b5`
- **Manual aplicado:** Manual Editorial v1.5
- **PDF autoritativo:** Drive file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`, página 2 izquierda, 5.038.575 bytes, 18 páginas, SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- **Acceso al PDF:** lectura directa desde Google Drive como archivo real, sin Base64; Drive no modificado
- **Publicación:** este registro forma parte del mismo commit Git atómico que el resto de la operación; el SHA técnico queda determinado por el historial Git

## Resultado editorial

- Leída visualmente la mitad izquierda de la página 2, sin OCR.
- Confirmada la ausencia de escritura significativa propia.
- Transcripción fijada como `[En blanco]` conforme al Manual Editorial v1.5, § 12.
- Se observan formas débiles en la mitad superior compatibles con transparencia o traspaso de tinta de la portada; carecen de valor textual propio y no se transcriben.
- No aparecen foliación, signaturas o marcas propias que requieran tratamiento adicional.
- No quedan dudas abiertas de la unidad.
- No ha sido necesario introducir ningún criterio editorial nuevo.

## Derivados

- Glosario: sin altas justificadas.
- Índice de personas: sin altas.
- Índice de topónimos: sin altas.
- Índice de instituciones: sin altas.
- Índice de medidas: sin altas.
- Índice de oficios: sin altas.

## Archivos de la operación

Modificados:

- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`
- `project/00_CONTROL/estado.yaml`

Creado:

- `project/00_CONTROL/OPERACIONES/EDICION-REVERSO-PORTADA-2026-09-06.md`

No se modifican `proyecto.yaml`, `unidades.yaml`, el Manual, el Glosario ni ninguno de los cinco índices.

## Estado resultante esperado

- `last_validated_unit: reverso_portada`
- `last_closed_unit: reverso_portada`
- `current_unit: folio_306r`
- `next_unit: folio_306v`
- `current_location.pdf_page: 2`
- `current_location.position: right`
- `open_issues: []`
- `operation.status: clean`

## Criterio de verificación

La operación solo se publica si `main` continúa exactamente en el Base SHA indicado. Tras publicar se verifican el padre del commit, la lista exacta de archivos afectados, los contenidos críticos, la coherencia de `estado.yaml` con `unidades.yaml`, la ausencia de PDF en GitHub y, cuando corresponda, el CI completo.

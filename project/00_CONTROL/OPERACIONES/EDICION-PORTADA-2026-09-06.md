# Operación EDICION-PORTADA-2026-09-06

- **Tipo:** edición, validación y cierre documental de unidad
- **Estado:** verified
- **Fecha:** 6 de septiembre de 2026
- **Unidad editorial:** `portada`
- **Rama canónica:** `main`
- **Base SHA:** `53b7d17940e8d5a84728624237fdf8a2f2b030c6`
- **Manual aplicado:** Manual Editorial v1.5
- **PDF autoritativo:** Drive file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`, página 1 completa, 5.038.575 bytes, 18 páginas, SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- **Acceso al PDF:** lectura directa desde Google Drive como archivo real, sin Base64; Drive no modificado
- **Publicación:** este registro forma parte del mismo commit Git atómico que el resto de la operación; el SHA técnico queda determinado por el historial Git

## Resultado editorial

- Leída visualmente la página completa, sin OCR.
- Transcritos los tres renglones de la portada conservando grafías, mayúsculas, puntuación y saltos de línea.
- Desarrolladas las abreviaturas `resp[ues]tas.` y `G[enera]les.` conforme al Manual.
- Resuelta D-001: el signo aislado superior se identifica como cruz invocativa reconocible y se representa `†`.
- La comparación con el signo análogo al inicio del folio 306r se emplea solo como apoyo paleográfico; no valida por anticipado esa unidad.
- El subrayado y trazo ornamental final se describen como elementos gráficos sin valor verbal.
- No quedan dudas abiertas de la Portada.

## Derivados

- Índice de topónimos: altas de `Sorribas` y `Santibañez De Ordas`.
- Glosario: sin altas justificadas.
- Índice de personas: sin altas.
- Índice de instituciones: sin altas.
- Índice de medidas: sin altas.
- Índice de oficios: sin altas.

## Archivos de la operación

Modificados:

- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Toponimos.md`
- `project/00_CONTROL/estado.yaml`

Creado:

- `project/00_CONTROL/OPERACIONES/EDICION-PORTADA-2026-09-06.md`

No se modifican `proyecto.yaml`, `unidades.yaml`, el Manual, el Glosario ni los otros cuatro índices.

## Estado resultante esperado

- `last_validated_unit: portada`
- `last_closed_unit: portada`
- `current_unit: reverso_portada`
- `next_unit: folio_306r`
- `current_location.pdf_page: 2`
- `current_location.position: left`
- `open_issues: []`
- `operation.status: clean`

## Criterio de verificación

La operación solo se publica si `main` continúa exactamente en el Base SHA indicado. Tras publicar se verifican el padre del commit, la lista exacta de archivos afectados, los contenidos críticos, la coherencia de `estado.yaml` con `unidades.yaml`, la ausencia de PDF en GitHub y el CI completo.


## Errata posterior — 18 de septiembre de 2026

La lectura paleográfica `Sorribas` utilizada en este registro queda rectificada a `Sorribos` tras la relectura visual completa del manuscrito. La división `Sorri-` / `bos` de folio 306r confirma la lectura. Este registro se conserva como testimonio de la operación original; la rectificación canónica consta en Edición Crítica v3.6 y en la operación `RECTIFICACION-TOPONIMO-SORRIBOS-2026-09-18`.

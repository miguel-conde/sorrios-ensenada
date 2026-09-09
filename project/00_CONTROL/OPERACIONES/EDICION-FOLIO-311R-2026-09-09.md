# Operación EDICION-FOLIO-311R-2026-09-09

- **Tipo:** edición, validación y cierre documental de unidad
- **Estado:** verified
- **Fecha:** 9 de septiembre de 2026
- **Unidad editorial:** `folio_311r`
- **Rama canónica:** `main`
- **Base SHA:** `1f16ad2a530172b4b49886453515315fb8321697`
- **Manual aplicado:** Manual Editorial v1.6
- **Edición vigente:** v3.5
- **PDF autoritativo:** Drive file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`, página 7 derecha, 5.038.575 bytes, 18 páginas, SHA-256 declarado `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- **Acceso al PDF:** lectura directa del archivo autoritativo obtenido de Google Drive como PDF real; Drive no modificado; sin Base64 y sin OCR

## Resultado editorial

- Leída visualmente la mitad derecha de la página 7 del PDF autoritativo.
- El folio 311r continúa la respuesta décima desde `tierras Ferrañales cercadas centenales De secano, que prod[uc]en / sin intermision forrage...` y prosigue el desglose cuantitativo por especies y calidades de tierra.
- Para los Ferrañales se consignan cantidades de primera, segunda y tercera calidad, con referencias explícitas a `celemin` y `celemines`.
- Continúa con las tierras linares de regadio, las tierras linares de secano y las tierras centenales de secano, manteniendo las distinciones de calidad y de régimen productivo declaradas en respuestas anteriores.
- La unidad termina en `quatroz[ienta]s setenta, y tres, y media`; la inspección auxiliar del comienzo de folio 311v confirma la continuación `de segunda mill cinquenta, y cinco, y medio celemin...`, solo para delimitar folio 311r y sin validar por anticipado folio 311v.
- Se desarrollan `terz[er]a` y `quatroz[ienta]s` conforme al criterio vigente de abreviaturas; se conservan las grafías `forrage`, `regadio`, `vn`, `vna`, `zevada`, `centeno`, `haverla`, `celemin` y `celemines`.
- Se conservan las divisiones visibles `inter-` / `mision` y `se-` / `gunda`.
- La foliación `311`, visible en el margen superior derecho, se usa solo como identificación editorial y no se incorpora al cuerpo de la transcripción.
- No aparece ningún criterio metodológico nuevo y no quedan dudas abiertas.

## Control de Notas históricas A/B/C/D

- **A. Sin nota necesaria:** las especies de tierra, los cultivos y las referencias a primera, segunda y tercera calidad son comprensibles dentro de la propia respuesta y de las unidades precedentes.
- **B. Glosario o índice:** `celemin` / `celemines` actualiza el Índice de medidas con la nueva aparición y la variante plural.
- **C. Nota histórica puntual:** no aparecen candidatos.
- **D. Diario o futuro Estudio Histórico:** el reparto cuantitativo de la cabida por especie y calidad de tierra constituye material relevante para un futuro estudio agrario de conjunto.
- **Decisión:** la sección `Notas históricas` queda justificadamente vacía. No se realiza investigación externa para esta unidad.

## Derivados

- Índice de medidas: actualización de `celemin` con la variante `celemines`, la referencia a folio 311r y su uso como fracción o complemento de cantidades de cabida, sin fijar equivalencia con otras medidas.
- Glosario e índices de personas, topónimos, instituciones y oficios: sin cambios justificados por esta unidad.
- Diario Editorial: registro de la validación, cierre, continuidad, clasificación A/B/C/D y derivados.

## Archivos de la operación

Modificados:

- `project/00_CONTROL/estado.yaml`
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md`

Creado:

- `project/00_CONTROL/OPERACIONES/EDICION-FOLIO-311R-2026-09-09.md`

No se modifican el Manual Editorial, `proyecto.yaml`, `unidades.yaml`, `CAMBIOS.md`, el Glosario, los índices de personas, topónimos, instituciones u oficios ni el PDF autoritativo.

## Estado resultante esperado

- `last_validated_unit: folio_311r`
- `last_closed_unit: folio_311r`
- `current_unit: folio_311v`
- `next_unit: folio_312r`
- `current_location.pdf_page: 8`
- `current_location.position: left`
- `open_issues: []`
- `operation.status: clean`

## Criterio de verificación

La operación solo se publica si `main` continúa exactamente en el Base SHA indicado. Tras publicar se verifican el padre del commit, la lista exacta de archivos afectados, el contenido de folio 311r, el Índice de medidas, la coherencia de `estado.yaml` con `unidades.yaml`, la ausencia de PDF en GitHub y el estado de CI.

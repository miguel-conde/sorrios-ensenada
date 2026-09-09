# Operación EDICION-FOLIO-311V-2026-09-09

- **Tipo:** edición, validación y cierre documental de unidad
- **Estado:** verified
- **Fecha:** 9 de septiembre de 2026
- **Unidad editorial:** `folio_311v`
- **Rama canónica:** `main`
- **Base SHA:** `ce6354f0d6af7c299781d568fc7a0717a6587ef9`
- **Manual aplicado:** Manual Editorial v1.6
- **Edición vigente:** v3.5
- **PDF autoritativo:** Drive file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`, página 8 izquierda, 5.038.575 bytes, 18 páginas, SHA-256 declarado `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- **Acceso al PDF:** lectura directa del archivo autoritativo obtenido de Google Drive como PDF real; Drive no modificado; sin Base64 y sin OCR

## Resultado editorial

- Leída visualmente la mitad izquierda de la página 8 del PDF autoritativo.
- El folio 311v continúa la respuesta décima desde la cantidad de primera calidad de las tierras centenales de secano y completa las cantidades de segunda y tercera calidad.
- La respuesta prosigue con prados cercados de regadio, prados cercados de secano, prados abiertos de regadio y prados abiertos de secano, distinguiendo calidades y regímenes productivos como `pelo, y otoño` o `solo vn pelo`.
- En la unidad aparecen de nuevo `celemin` y `celemines` dentro de las cantidades declaradas.
- La unidad termina en `no haverla De primera ciento siete, y`; la inspección auxiliar del comienzo de folio 312r confirma la continuación `medio, y de terz[er]a cinquenta...`, solo para delimitar folio 311v y sin validar por anticipado folio 312r.
- Se desarrollan `terz[er]a` y `doz[iento]s` conforme al criterio vigente de abreviaturas; se conservan las grafías `mill`, `cinquenta`, `regadio`, `vnica`, `nobenta`, `vn`, `celemin` y `celemines`.
- Se conservan las divisiones visibles `re-` / `gadio`, `Cin-` / `quenta` e `intermisi-` / `on`.
- No aparece ningún criterio metodológico nuevo y no quedan dudas abiertas.

## Control de Notas históricas A/B/C/D

- **A. Sin nota necesaria:** las categorías de prados, sus calidades y los regímenes `pelo, y otoño` y `solo vn pelo` son comprensibles por continuidad con las respuestas cuarta, quinta y décima ya editadas.
- **B. Glosario o índice:** `pelo` actualiza el Glosario con la nueva aparición; `celemin` / `celemines` actualiza el Índice de medidas.
- **C. Nota histórica puntual:** no aparecen candidatos.
- **D. Diario o futuro Estudio Histórico:** el reparto cuantitativo por categoría y calidad de prado y su asociación con regímenes de aprovechamiento constituye material para un futuro estudio agrario de conjunto.
- **Decisión:** la sección `Notas históricas` queda justificadamente vacía. No se realiza investigación externa para esta unidad.

## Derivados

- Glosario: actualización de `pelo` con la referencia a folio 311v y la nueva evidencia interna que distingue prados de `pelo, y otoño` y de `solo vn pelo`.
- Índice de medidas: actualización de `celemin` / `celemines` con la referencia a folio 311v, sin fijar equivalencias no declaradas.
- Índices de personas, topónimos, instituciones y oficios: sin cambios justificados por esta unidad.
- Diario Editorial: registro de la validación, cierre, continuidad, clasificación A/B/C/D y derivados.

## Archivos de la operación

Modificados:

- `project/00_CONTROL/estado.yaml`
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`
- `project/20_TRABAJO_EDITORIAL/Glosario.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md`

Creado:

- `project/00_CONTROL/OPERACIONES/EDICION-FOLIO-311V-2026-09-09.md`

No se modifican el Manual Editorial, `proyecto.yaml`, `unidades.yaml`, `CAMBIOS.md`, los índices de personas, topónimos, instituciones u oficios ni el PDF autoritativo.

## Estado resultante esperado

- `last_validated_unit: folio_311v`
- `last_closed_unit: folio_311v`
- `current_unit: folio_312r`
- `next_unit: folio_312v`
- `current_location.pdf_page: 8`
- `current_location.position: right`
- `open_issues: []`
- `operation.status: clean`

## Criterio de verificación

La operación solo se publica si `main` continúa exactamente en el Base SHA indicado. Tras publicar se verifican el padre del commit, la lista exacta de archivos afectados, el contenido de folio 311v, el Glosario, el Índice de medidas, la coherencia de `estado.yaml` con `unidades.yaml`, la ausencia de PDF en GitHub y el estado de CI.

# Operación EDICION-FOLIO-309V-2026-09-08

- **Tipo:** edición, validación y cierre documental de unidad
- **Estado:** verified
- **Fecha:** 8 de septiembre de 2026
- **Unidad editorial:** `folio_309v`
- **Rama canónica:** `main`
- **Base SHA:** `2e110c8949cef831774ba69220ec55eb86a75d7e`
- **Manual aplicado:** Manual Editorial v1.6
- **Edición vigente:** v3.5
- **PDF autoritativo:** Drive file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`, página 6 izquierda, 5.038.575 bytes, 18 páginas, SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- **Acceso al PDF:** lectura directa del archivo autoritativo obtenido de Google Drive como PDF real; Drive no modificado; sin Base64 y sin OCR

## Resultado editorial

- Leída visualmente la mitad izquierda de la página 6 del PDF autoritativo.
- La séptima respuesta se contiene íntegramente en la unidad y remite a lo declarado en la pregunta antecedente.
- La octava respuesta se contiene íntegramente en la unidad y remite a lo que resulta de la sexta pregunta.
- La novena respuesta comienza en esta unidad. Declara que no se usa una medida cierta de tierra reducible a `baras castellanas`; las tierras de pan llevar se entienden por el `quartal De grano` que puede caber en ellas, y los prados de guadaña por los `quartales` que pudieren llevar en sembradura. Para tierras de matorral, eras, sitios, montes y sotos se remite al juicio de peritos.
- Un breve tramo de la segunda línea de la novena respuesta queda materialmente oculto por interferencia de tinta y se representa mediante `[...]`, conforme al signo editorial ya vigente; no se fuerza una lectura.
- La novena respuesta queda abierta al final de la cara en `siempre, que se-`; la inspección auxiliar del comienzo de folio 310r confirma la continuación `ofrece...`, solo a efectos de delimitar folio 309v y sin validar por anticipado folio 310r.
- Se conservan las grafías `Ala`, `septima`, `octaba`, `nobena`, `baras`, `quartal`, `quartales`, `caver`, `cuias` y `cavida`, así como las mayúsculas y la disposición lineal del manuscrito.
- Se conservan las divisiones visibles `re-` / `miten`, `pre-` / `gunta`, `en-` / `tienden`, `pue-` / `de`, `Mon-` / `tes` y `se-` / `ofrece`.
- La serie de puntos que cierra la séptima respuesta se omite como relleno gráfico sin valor verbal, conforme al criterio ya vigente.
- Se aplicó el control A/B/C/D de Notas históricas: las remisiones de las respuestas séptima y octava se clasifican A; `baras castellanas`, `quartal`/`quartales` y `pan` se clasifican B y se remiten al Índice de medidas o al Glosario; no aparecen candidatos C ni D. La sección `Notas históricas` queda justificadamente vacía.
- No aparece ningún criterio metodológico nuevo y no quedan dudas abiertas.

## Derivados

- Glosario: actualización de `pan` con la nueva aparición `tierras De pan llevar` en folio 309v.
- Índice de medidas: actualización de `baras` con la nueva aparición `baras castellanas` y alta de `quartal`, con variante `quartales`, sin fijar equivalencia moderna.
- Índices de personas, topónimos, instituciones y oficios: sin cambios justificados por esta unidad.
- Diario Editorial: registro de la validación, cierre, continuidad, tratamiento del tramo oculto, clasificación A/B/C/D y derivados.

## Archivos de la operación

Modificados:

- `project/00_CONTROL/estado.yaml`
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`
- `project/20_TRABAJO_EDITORIAL/Glosario.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md`

Creado:

- `project/00_CONTROL/OPERACIONES/EDICION-FOLIO-309V-2026-09-08.md`

No se modifican el Manual Editorial, `proyecto.yaml`, `unidades.yaml`, `CAMBIOS.md`, los índices de personas, topónimos, instituciones u oficios ni el PDF autoritativo.

## Estado resultante esperado

- `last_validated_unit: folio_309v`
- `last_closed_unit: folio_309v`
- `current_unit: folio_310r`
- `next_unit: folio_310v`
- `current_location.pdf_page: 6`
- `current_location.position: right`
- `open_issues: []`
- `operation.status: clean`

## Criterio de verificación

La operación solo se publica si `main` continúa exactamente en el Base SHA indicado. Tras publicar se verifican el padre del commit, la lista exacta de archivos afectados, el contenido de folio 309v, el Glosario, el Índice de medidas, la coherencia de `estado.yaml` con `unidades.yaml`, la ausencia de PDF en GitHub y el estado de CI.

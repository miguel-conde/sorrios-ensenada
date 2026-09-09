# Operación EDICION-FOLIO-312R-2026-09-09

- **Tipo:** edición, validación y cierre documental de unidad
- **Estado:** verified
- **Fecha:** 9 de septiembre de 2026
- **Unidad editorial:** `folio_312r`
- **Rama canónica:** `main`
- **Base SHA:** `a9f495ac9942beddf7a0b93187e951823d622e24`
- **Base de contenido:** árbol `9208b4c7e0e5667a48bc8f1e6484813a3da8fc7a`, idéntico al estado canónico previo de `6e15f174ac27f5a6bc90c068f5316da6280336fb` tras la reparación operativa prepublicación.
- **Manual aplicado:** Manual Editorial v1.6
- **Edición vigente:** v3.5
- **PDF autoritativo:** Drive file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`, página 8 derecha, 5.038.575 bytes, 18 páginas, SHA-256 declarado `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- **Acceso al PDF:** lectura directa del archivo autoritativo obtenido de Google Drive como PDF real; Drive no modificado; sin Base64 y sin OCR

## Resultado editorial

- Leída visualmente la mitad derecha de la página 8 del PDF autoritativo.
- El folio 312r continúa la décima respuesta desde `no haverla De primera ciento siete, y / medio, y de terz[er]a cinquenta...` y completa el desglose de cabida con prados `De entre pares`, tierras matorrales, `Eras, ô sitios` y `Sotos De Ne- / grillos, y alisos`.
- La décima respuesta concluye en `nobenta, y seis medidas De tt[ierr]as.`.
- La undécima respuesta se contiene íntegramente en la unidad y declara las especies de frutos `centeno, Cebada, lino, Linaza, y yerba`.
- La duodécima respuesta comienza al final de la cara y queda abierta en `Ala duodecima dijeron: que cada`; la inspección auxiliar del comienzo de folio 312v confirma `medida De tierra De las De este termino...`, solo para delimitar folio 312r y sin validar por anticipado folio 312v.
- Se desarrollan `terz[er]a`, `doz[iento]s`, `term[ino].` y `tt[ierr]as.` conforme al criterio vigente de abreviaturas; se conserva `De entre pares` exactamente como está escrito y la división `Ne-` / `grillos`.
- Los rellenos de puntos tras la abreviatura de `tt[ierr]as.` y tras `yerba` se omiten como signos no verbales sin valor textual, conforme al criterio vigente.
- No aparece ningún criterio metodológico nuevo y no quedan dudas abiertas.

## Control de Notas históricas A/B/C/D

- **A. Sin nota necesaria:** las categorías agrarias, calidades y nombres de cultivos son comprensibles por el propio expediente y las respuestas precedentes.
- **B. Glosario o índice:** `entreparedes` incorpora la variante documental `entre pares`; `negrillos` incorpora la nueva aparición de folio 312r.
- **C. Nota histórica puntual:** no aparecen candidatos.
- **D. Diario o futuro Estudio Histórico:** el cierre cuantitativo de la cabida y la relación de especies productivas de la undécima respuesta constituyen material para un futuro estudio agrario de conjunto.
- **Decisión:** la sección `Notas históricas` queda justificadamente vacía. No se realiza investigación externa para esta unidad.

## Derivados

- Glosario: actualización de `entreparedes` con la variante `entre pares` y folio 312r; actualización de `negrillos` con la nueva aparición.
- Índices de personas, topónimos, instituciones, medidas y oficios: sin cambios justificados por esta unidad.
- Diario Editorial: registro de la validación, cierre, continuidad, clasificación A/B/C/D y derivados.

## Archivos de la operación

Modificados:

- `project/00_CONTROL/estado.yaml`
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`
- `project/20_TRABAJO_EDITORIAL/Glosario.md`

Creado:

- `project/00_CONTROL/OPERACIONES/EDICION-FOLIO-312R-2026-09-09.md`

No se modifican el Manual Editorial, `proyecto.yaml`, `unidades.yaml`, `CAMBIOS.md`, los cinco índices ni el PDF autoritativo.

## Estado resultante esperado

- `last_validated_unit: folio_312r`
- `last_closed_unit: folio_312r`
- `current_unit: folio_312v`
- `next_unit: folio_313r`
- `current_location.pdf_page: 9`
- `current_location.position: left`
- `open_issues: []`
- `operation.status: clean`

## Criterio de verificación

La operación solo se publica si `main` continúa exactamente en el Base SHA indicado. Tras publicar se verifican el padre del commit, la lista exacta de archivos afectados, el contenido de folio 312r, el Glosario, la coherencia de `estado.yaml` con `unidades.yaml`, la ausencia de PDF en GitHub y el estado de CI.

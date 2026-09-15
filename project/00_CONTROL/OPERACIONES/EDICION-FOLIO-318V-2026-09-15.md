# Operación EDICION-FOLIO-318V-2026-09-15

- **Tipo:** edición, validación y cierre documental de unidad
- **Estado:** verified
- **Fecha:** 15 de septiembre de 2026
- **Unidad editorial:** `folio_318v`
- **Rama canónica:** `main`
- **Base SHA:** `76ef431596ae9d64d8f9dad060fae73365dfa6a2`
- **Manual aplicado:** Manual Editorial v1.6
- **Edición vigente:** v3.5
- **PDF autoritativo:** `sorrios_ensenada_orden_lectura_calidad_original.pdf`, página 15 izquierda; Drive file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`; 18 páginas; tamaño 5038575 bytes; SHA-256 declarado `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- **Acceso al PDF:** lectura visual directa del PDF autoritativo; sin OCR; Drive no modificado

## Resultado editorial

- Leída visualmente la mitad izquierda de la página 15 del PDF autoritativo.
- Se continúa y concluye la respuesta 22.ª con `por el establecim[ien]to. De el suelo.`.
- La respuesta 23.ª se contiene íntegramente en la unidad y declara que el común no tiene `propios`.
- La respuesta 24.ª se contiene íntegramente en la unidad y declara que el común no disfruta `arbitrio, ni renta alguna`.
- La respuesta 25.ª comienza declarando que el común debe satisfacer `dozientos Reales` cada año y desglosa gastos en la festividad del Corpus, ocho reales para limpiar las fuentes, quince reales pagados al `hospital De Ynocentes De la ciudad De Valladolid` y diez reales por el `derecho De Mesta en la ciudad De León`, además de otras cantidades.
- La cara termina en `por no tener`.
- El comienzo de folio 319r se consulta únicamente para confirmar la continuación `propias las pagan por repartimi- / ento entre los vecinos` y no valida por anticipado esa unidad.
- Se desarrollan `establecim[ien]to.` y `p[o]r` conforme al criterio vigente.
- Se conservan `Ala`, `quatro`, `comun`, `deve`, `vn`, `dozientos`, `Reales`, `Ynocentes`, `Mesta`, `León`, `Cantidades` y las divisiones visibles `quin-` / `ce` y `Val-` / `ladolid`.
- Los puntos y trazos terminales tras palabras completas se omiten como relleno gráfico sin valor verbal conforme al criterio ya vigente.
- No aparece ningún criterio metodológico nuevo y no quedan dudas abiertas.

## Control de Notas históricas A/B/C/D

- **A. Sin nota necesaria:** formulaciones ordinarias de las respuestas, festividad del Corpus y limpieza de fuentes.
- **B. Glosario o índices:** `propios`; `arbitrio`; `Hospital De Ynocentes`; `Mesta`; `Valladolid`; `León`; `real` / `Reales`.
- **C. Nota histórica puntual:** no aparecen candidatos que requieran investigación externa.
- **D. Diario o futuro Estudio Histórico:** estructura del gasto comunal, pagos, ausencia de propios y arbitrios y repartimiento por falta de recursos propios.
- **Decisión:** la sección `Notas históricas` queda justificadamente sin notas puntuales. No se realiza investigación externa.

## Derivados

- Glosario: altas de `propios` y `arbitrio`.
- Índice de instituciones: altas de `Hospital De Ynocentes` y `Mesta`.
- Índice de topónimos: altas de `Valladolid` y `León`.
- Índice de medidas: actualización de `real` / `Reales`.
- Índices de personas y oficios: sin cambios justificados.
- Diario Editorial: registro de validación, cierre, continuidad, clasificación A/B/C/D y derivados.

## Archivos de la operación

Modificados:

- `project/00_CONTROL/estado.yaml`
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`
- `project/20_TRABAJO_EDITORIAL/Glosario.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Instituciones.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Toponimos.md`

Creado:

- `project/00_CONTROL/OPERACIONES/EDICION-FOLIO-318V-2026-09-15.md`

No se modifican el Manual Editorial, `proyecto.yaml`, `unidades.yaml`, `CAMBIOS.md`, los índices de personas u oficios ni el PDF autoritativo.

## Estado resultante esperado

- `last_validated_unit: folio_318v`
- `last_closed_unit: folio_318v`
- `current_unit: folio_319r`
- `next_unit: folio_319v`
- `current_location.pdf_page: 15`
- `current_location.position: right`
- `open_issues: []`
- `operation.status: clean`

## Criterio de verificación

La operación solo se publica si `main` continúa exactamente en el Base SHA indicado. Tras publicar se verifican el padre del commit, la lista exacta de archivos afectados, el contenido de folio 318v, los derivados, la coherencia de `estado.yaml` con `unidades.yaml`, la ausencia del PDF en GitHub y el estado de CI.

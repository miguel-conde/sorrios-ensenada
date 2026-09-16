# Operación EDICION-FOLIO-320R-2026-09-16

- **Tipo:** edición, validación y cierre documental de unidad
- **Estado:** verified
- **Fecha:** 16 de septiembre de 2026
- **Unidad editorial:** `folio_320r`
- **Rama canónica:** `main`
- **Base SHA:** `07255c64351fc85946ae97bf08cbd274ee6b5f60`
- **Manual aplicado:** Manual Editorial v1.6
- **Edición vigente:** v3.5
- **PDF autoritativo:** `sorrios_ensenada_orden_lectura_calidad_original.pdf`, página 16 derecha; Drive file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`; 18 páginas; tamaño 5038575 bytes; SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- **Acceso al PDF:** lectura visual directa del PDF autoritativo; sin OCR; Drive no modificado
- **Verificación previa heredada:** comprobado antes de iniciar esta unidad que el workflow `Portable Python tests` del commit `07255c64351fc85946ae97bf08cbd274ee6b5f60` concluyó con `success` y que su árbol recursivo no contiene el PDF autoritativo.

## Resultado editorial

- Leída visualmente la mitad derecha de la página 16 del PDF autoritativo.
- Se continúa y concluye la respuesta 32.ª con `no ai cosa alguna De las que contiene / la pregunta.`.
- La respuesta 33.ª se contiene íntegramente: declara un solo `herrero`, que ocupa la mayor parte del año en el `exercicio De labrador`; se le considera `medio real` de ganancia diaria por el oficio de herrero, además de lo que gana como labrador.
- La respuesta 34.ª se contiene íntegramente y declara que no hay cosa alguna de las que contiene la pregunta correspondiente.
- La respuesta 35.ª comienza declarando dieciocho `jornaleros`: catorce `hijos De familia` que están en `comp[añí]a.` de sus padres y tres `criados servi[ent]es.`; continúa materialmente en folio 320v.
- El comienzo de folio 320v se consulta únicamente para delimitar la respuesta 35.ª y no valida por anticipado la unidad siguiente.
- Se desarrollan `p[o]r`, `comp[añí]a.` y `servi[ent]es.` conforme al criterio vigente.
- Se conserva la división `ocupar-` / `se`; los rellenos gráficos se omiten conforme al criterio vigente.
- No aparece ningún criterio metodológico nuevo y no quedan dudas abiertas.

## Control de Notas históricas A/B/C/D

- **A. Sin nota necesaria:** fórmulas negativas de las respuestas 32.ª y 34.ª y formulación ordinaria.
- **B. Glosario o índices:** `hijo de familia`; `herrero`; `labrador`; `jornalero`; `criado sirviente`; `real` / `Reales`.
- **C. Nota histórica puntual:** no aparecen candidatos que requieran investigación externa nueva.
- **D. Diario o futuro Estudio Histórico:** combinación ocupacional herrero/labrador, ganancia diaria del herrero y estructura del trabajo jornalero.
- **Decisión:** la sección `Notas históricas` queda justificadamente sin notas puntuales. No se realiza investigación externa nueva.

## Derivados

- Glosario: alta de `hijo de familia`.
- Índice de oficios: altas de `herrero`, `labrador`, `jornalero` y `criado sirviente`.
- Índice de medidas: actualización de `real` / `Reales` con `medio real` en la respuesta 33.ª.
- Diario Editorial: registro del cierre y de las comprobaciones heredadas.
- Índices de personas, topónimos e instituciones: sin cambios justificados.

## Archivos de la operación

Modificados:

- `project/00_CONTROL/estado.yaml`
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`
- `project/20_TRABAJO_EDITORIAL/Glosario.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Oficios.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md`

Creado:

- `project/00_CONTROL/OPERACIONES/EDICION-FOLIO-320R-2026-09-16.md`

No se modifican el Manual Editorial, `proyecto.yaml`, `unidades.yaml`, los índices de personas, topónimos o instituciones ni el PDF autoritativo.

## Estado resultante esperado

- `last_validated_unit: folio_320r`
- `last_closed_unit: folio_320r`
- `current_unit: folio_320v`
- `next_unit: folio_321r`
- `current_location.pdf_page: 17`
- `current_location.position: left`
- `open_issues: []`
- `operation.status: clean`

## Criterio de verificación

La operación solo se publica si `main` continúa exactamente en el Base SHA indicado. Tras publicar se verifican el padre del commit, la lista exacta de archivos afectados, el contenido de folio 320r, los derivados, la coherencia de `estado.yaml` con `unidades.yaml`, la ausencia del PDF en GitHub y el estado de CI.

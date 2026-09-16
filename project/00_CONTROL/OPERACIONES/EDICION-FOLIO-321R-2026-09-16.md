# Operación EDICION-FOLIO-321R-2026-09-16

- **Tipo:** edición, validación y cierre documental de unidad
- **Estado:** verified
- **Fecha:** 16 de septiembre de 2026
- **Unidad editorial:** `folio_321r`
- **Rama canónica:** `main`
- **Base SHA:** `15366a8a8cd5ab09f7240906e2a08d51ce254b4a`
- **Manual aplicado:** Manual Editorial v1.6
- **Edición vigente:** v3.5
- **PDF autoritativo:** `sorrios_ensenada_orden_lectura_calidad_original.pdf`, página 17 derecha; Drive file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`; 18 páginas; tamaño 5038575 bytes; SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- **Acceso al PDF:** lectura visual directa del PDF autoritativo; consulta auxiliar del comienzo de folio 321v para delimitar la firma final; relectura de folio 306v para resolver una identificación personal; sin OCR; Drive no modificado.

## Comprobaciones previas pendientes

Antes de comenzar la unidad se completaron las dos verificaciones pospublicación pendientes del cierre de folio 320v, commit `15366a8a8cd5ab09f7240906e2a08d51ce254b4a`:

- workflow `Portable Python tests`, run 123: `completed` / `success`;
- árbol recursivo del commit: ausencia del PDF autoritativo.

## Resultado editorial

- La respuesta 39.ª, comenzada en folio 320v, se completa con `no ai convento alguno.`.
- La respuesta 40.ª se contiene íntegramente en folio 321r y declara que no hay `venta, ni finca alguna` de las comprendidas en la pregunta.
- El cierre declara que todo lo dicho es verdad bajo el juramento ya prestado, que los declarantes se afirman y ratifican, y consigna sus edades aproximadas.
- Edades declaradas: `Remirio Rodriguez`, sesenta y nueve; `Juan Alvarez`, cuarenta y nueve; `Dom[ing]o Suarez`, cincuenta y nueve; `Fran[cis]co De Llorca`, cincuenta y dos; `Dom[ing]o Diez`, cuarenta y cuatro años, poco más o menos.
- El texto declara que firmaron quienes supieron, junto con `su m[erce]d.`. En esta cara quedan las firmas `Liz[encia]do D[o]n Joachin Aguado` y `Dom[ing]o Diez`; el último `Dom[ing]o` continúa materialmente en folio 321v con `Suarez:`.
- La inspección del comienzo de folio 321v se usa solo para delimitar la firma final y no valida por anticipado la unidad siguiente.

## Rectificación paleográfica de folio 306v

- La lectura previamente validada `Dom[ing]o Vicarez` en folio 306v se rectifica a `Dom[ing]o Suarez`.
- La rectificación se apoya en tres evidencias internas concordantes: relectura directa de folio 306v, la declaración de edad `Dom[ing]o Suarez` en folio 321r y la firma `Dom[ing]o` / `Suarez:` repartida entre folios 321r y 321v.
- Se aplica el criterio ya vigente del Manual Editorial § 15 de comparar otras apariciones y firmas; no se introduce un criterio metodológico nuevo.
- Se corrigen los documentos vivos afectados: Edición crítica, Índice de personas e Índice de oficios. El registro histórico de la operación de 306v no se reescribe; el Diario deja constancia de la rectificación posterior.

## Criterios paleográficos

- Se desarrollan `Juram[en]to.`, `d[ic]hos.`, `Dom[ing]o`, `Fran[cis]co`, `m[erce]d.`, `Liz[encia]do` y `D[o]n` conforme al criterio general vigente.
- Se conservan las grafías y formas documentales `ai`, `ay`, `socargo`, `hedad`, `echo`, `quarenta`, `fé` y las variantes de mayúsculas/minúsculas visibles.
- Se conservan las divisiones visibles `Jura-` / `m[en]to.`, `afirma-` / `ron`, `sesen-` / `ta`, `qua-` / `renta`, `Cin-` / `quenta`, `su-` / `pieron` y `Joac-` / `hin`.
- Los puntos y trazos de relleno tras `alguno` se omiten conforme al criterio vigente para signos no verbales.
- No aparece ningún criterio metodológico nuevo y no quedan dudas abiertas.

## Control de Notas históricas A/B/C/D

- **A. Sin nota necesaria:** las respuestas negativas 39.ª y 40.ª; la fórmula ordinaria de cierre, juramento y ratificación.
- **B. Glosario o índices:** personas nominalmente declaradas y sus edades; rectificación de `Dom[ing]o Suarez`; actualización del Índice de personas y de la referencia de `perito` en el Índice de oficios.
- **C. Nota histórica puntual:** no aparecen candidatos que requieran investigación externa nueva.
- **D. Diario o futuro Estudio Histórico:** perfil de edades de los declarantes, práctica de firma de `los que supieron` y forma documental de cierre y ratificación.
- **Decisión:** la sección `Notas históricas` queda justificadamente sin notas puntuales. No se realiza investigación externa nueva.

## Derivados

- Índice de personas: nuevas apariciones de `Joachin Aguado`, `Remirio Rodriguez`, `Juan Alv[are]z` / `Juan Alvarez`, `Dom[ing]o Diez` y `Fran[cis]co de Llorca` / `Fran[cis]co De Llorca`; rectificación y nueva aparición de `Dom[ing]o Suarez`.
- Índice de oficios: rectificación de la persona vinculada a `perito`, de `Dom[ing]o Vicarez` a `Dom[ing]o Suarez`.
- Diario Editorial: registro del cierre, del control A/B/C/D, de las comprobaciones pendientes de folio 320v y de la rectificación de folio 306v.
- Glosario e índices de topónimos, instituciones y medidas: sin cambios justificados.

## Archivos de la operación

Modificados:

- `project/00_CONTROL/estado.yaml`
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Personas.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Oficios.md`

Creado:

- `project/00_CONTROL/OPERACIONES/EDICION-FOLIO-321R-2026-09-16.md`

No se modifican el Manual Editorial, `proyecto.yaml`, `unidades.yaml`, Glosario, los índices de topónimos, instituciones o medidas ni el PDF autoritativo.

## Estado resultante esperado

- `last_validated_unit: folio_321r`
- `last_closed_unit: folio_321r`
- `current_unit: folio_321v`
- `next_unit: hoja_enfrentada_posterior`
- `current_location.pdf_page: 18`
- `current_location.position: left`
- `open_issues: []`
- `operation.status: clean`

## Criterio de verificación

La operación solo se publica si `main` continúa exactamente en el Base SHA indicado. Tras publicar se verifican el padre del commit, la lista exacta de archivos afectados, el contenido de folio 321r y la rectificación de folio 306v, los derivados, la coherencia de `estado.yaml` con `unidades.yaml`, la ausencia del PDF en GitHub y el estado de CI.

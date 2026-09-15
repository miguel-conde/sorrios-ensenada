# Operación EDICION-FOLIO-316V-2026-09-15

- **Tipo:** edición, validación y cierre documental de unidad
- **Estado:** verified
- **Fecha:** 15 de septiembre de 2026
- **Unidad editorial:** `folio_316v`
- **Rama canónica:** `main`
- **Base SHA:** `2b02b6eb11abf16f1df21d7156276846381682a6`
- **Manual aplicado:** Manual Editorial v1.6
- **Edición vigente:** v3.5
- **PDF autoritativo:** `sorrios_ensenada_orden_lectura_calidad_original.pdf`, página 13 izquierda; Drive file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`; 18 páginas; tamaño 5038575 bytes; SHA-256 declarado `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- **Acceso al PDF:** lectura visual directa del PDF autoritativo obtenido de Google Drive como archivo real, sin OCR; Drive no modificado

## Resultado editorial

- Leída visualmente la mitad izquierda de la página 13 del PDF autoritativo.
- La respuesta 19.ª se contiene íntegramente en la unidad: se declaran dieciocho `p[ie]s. De abejas`, distribuidos entre `D[o]n Agustin G[arci]a Ordas Presbitero`, `Fran[cis]co Diez`, `Manuel G[arci]a`, `Juan F[ernande]z` y `Margarita G[arci]a`, todos vecinos del lugar.
- Se regula una utilidad anual de `dos Reales vellon` para cada `p[ie] De abejas`.
- La respuesta 20.ª comienza enumerando las especies de ganado `Bacuno`, `Lanar`, `De Zerda`, `Yeguas, y crias mulares` y abre la regulación de los `esquilmos` por cabeza.
- La unidad termina en `en esta forma: El De cada baca por el`; la inspección auxiliar del comienzo de folio 317r se utiliza únicamente para confirmar continuidad y no valida por anticipado esa unidad.
- Se desarrollan `term[ino].`, `p[ie]s.`, `D[o]n`, `G[arci]a`, `Fran[cis]co`, `F[ernande]z`, `vez[ino]s.` y `p[o]r` conforme al criterio vigente.
- Se conservan las grafías y formas documentales `nobena`, `annual`, `vellon`, `pu-` / `eblo`, `gana-` / `dos`, `Bacuno`, `Lanar`, `De Zerda`, `cavezas` y `baca`, así como la división `Ma-` / `nuel`.
- No aparece ningún criterio metodológico nuevo y no quedan dudas abiertas.

## Control de Notas históricas A/B/C/D

- **A. Sin nota necesaria:** formulación de las respuestas y enumeración ordinaria de las especies de ganado.
- **B. Glosario o índices:** `p[ie]s. De abejas`; propietarios; `Presbitero`; `Reales vellon`; `esquilmo` / `esquilmos`.
- **C. Nota histórica puntual:** no aparecen candidatos que requieran investigación externa.
- **D. Diario o futuro Estudio Histórico:** distribución de los pies de abejas, utilidad anual por pie y comienzo de la regulación del rendimiento pecuario por especie y cabeza.
- **Decisión:** la sección `Notas históricas` queda justificadamente sin notas puntuales. No se realiza investigación externa.

## Derivados

- Glosario: alta de `pies de abejas` y actualización de `esquilmo`.
- Índice de personas: altas de `Agustin G[arci]a Ordas` y `Juan F[ernande]z`; actualización de `Fran[cis]co Diez`, `Manuel G[arci]a` y `Margarita G[arci]a`.
- Índice de oficios: alta de `Presbitero`.
- Índice de medidas: actualización de `real` con `Reales vellon` y folio 316v.
- Índices de topónimos e instituciones: sin cambios justificados.
- Diario Editorial: registro de validación, cierre, continuidad, clasificación A/B/C/D y derivados.

## Archivos de la operación

Modificados:

- `project/00_CONTROL/estado.yaml`
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`
- `project/20_TRABAJO_EDITORIAL/Glosario.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Personas.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Oficios.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md`

Creado:

- `project/00_CONTROL/OPERACIONES/EDICION-FOLIO-316V-2026-09-15.md`

No se modifican el Manual Editorial, `proyecto.yaml`, `unidades.yaml`, `CAMBIOS.md`, los índices de topónimos e instituciones ni el PDF autoritativo.

## Estado resultante esperado

- `last_validated_unit: folio_316v`
- `last_closed_unit: folio_316v`
- `current_unit: folio_317r`
- `next_unit: folio_317v`
- `current_location.pdf_page: 13`
- `current_location.position: right`
- `open_issues: []`
- `operation.status: clean`

## Criterio de verificación

La operación solo se publica si `main` continúa exactamente en el Base SHA indicado. Tras publicar se verifican el padre del commit, la lista exacta de archivos afectados, el contenido de folio 316v, los derivados, la coherencia de `estado.yaml` con `unidades.yaml`, la ausencia del PDF en GitHub y el estado de CI.

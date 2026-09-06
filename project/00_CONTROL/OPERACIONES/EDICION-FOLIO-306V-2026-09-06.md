# Operación EDICION-FOLIO-306V-2026-09-06

- **Tipo:** edición, validación y cierre documental de unidad
- **Estado:** verified
- **Fecha:** 6 de septiembre de 2026
- **Unidad editorial:** `folio_306v`
- **Rama canónica:** `main`
- **Base SHA:** `1eaf24eb13537993609c1154a02e04ba203251fd`
- **Manual aplicado:** Manual Editorial v1.5
- **PDF autoritativo:** Drive file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`, página 3 izquierda, 5.038.575 bytes, 18 páginas, SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- **Acceso al PDF:** lectura directa del archivo autoritativo obtenido de Google Drive; Drive no modificado; archivo entregado como PDF real, sin Base64
- **Publicación:** este registro forma parte del mismo commit Git atómico que el resto de la operación; el SHA técnico queda determinado por el historial Git

## Resultado editorial

- Leída visualmente la mitad izquierda de la página 3, sin OCR.
- Transcritas dieciocho líneas, conservando saltos de línea, mayúsculas, puntuación, grafías históricas y las divisiones visibles `parro-` / `cho`, `ha-` / `viendolo` y `pre-` / `guntas`.
- Desarrolladas las abreviaturas `Justiz[i]a`, `Dom[ing]o`, `Fran[cis]co`, `p[o]r`, `excepz[i]on`, `ss[criba]no`, `Juram[en]to`, `n[omb]re`, `D[io]s`, `n[uest]ro` y `poblaz[i]on`.
- Conservadas las grafías históricas `vnicos`, `Justizia`, `excepzion`, `Recivió`, `thenor`, `acada`, `vna` y `poblazion`, así como las formas unidas `socargo` y `Ala`.
- La cara no presenta número de folio independiente; su identificación como 306v deriva de la secuencia material y del recto 306r precedente.
- La continuidad sintáctica con folio 306r identifica a `Juan Alv[are]z` y `Remirio Rodriguez` como `vnicos oficiales de Justiz[i]a`.
- Se documentan `Dom[ing]o Diez` y `Fran[cis]co de Llorca` como peritos nombrados por el Concejo, y `Dom[ing]o Vicarez` como perito nombrado de oficio.
- La serie de puntos tras `Santibañez` ocupa el resto del renglón como relleno gráfico sin valor verbal y no se transcribe, aplicando el criterio vigente para signos no verbales; no ha sido necesario introducir un criterio editorial nuevo.
- La primera respuesta concluye en esta unidad; folio 307r comienza la segunda respuesta.
- No quedan dudas abiertas de folio 306v.

## Derivados

- Glosario: sin altas; se normaliza el mensaje de vacío obsoleto a `*(Sin entradas.)*`.
- Índice de personas: se actualizan `Manuel Ant[oni]o De Bega`, `Juan Alv[are]z` y `Remirio Rodriguez`; se dan de alta `Dom[ing]o Diez`, `Fran[cis]co de Llorca` y `Dom[ing]o Vicarez`.
- Índice de topónimos: se añade folio 306v a `Sorribas` y `Santibañez De Ordas`.
- Índice de instituciones: se añade folio 306v y la variante `Concejo` a `Concejo de Ordas`.
- Índice de medidas: sin altas; se normaliza el mensaje de vacío obsoleto a `*(Sin entradas.)*`.
- Índice de oficios: se actualiza `cura parrocho` y se dan de alta `oficial de Justiz[i]a`, `perito` y `escribano`.

## Archivos de la operación

Modificados:

- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`
- `project/20_TRABAJO_EDITORIAL/Glosario.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Personas.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Toponimos.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Instituciones.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Oficios.md`
- `project/00_CONTROL/estado.yaml`

Creado:

- `project/00_CONTROL/OPERACIONES/EDICION-FOLIO-306V-2026-09-06.md`

No se modifican `proyecto.yaml`, `unidades.yaml` ni el Manual Editorial.

## Estado resultante esperado

- `last_validated_unit: folio_306v`
- `last_closed_unit: folio_306v`
- `current_unit: folio_307r`
- `next_unit: folio_307v`
- `current_location.pdf_page: 3`
- `current_location.position: right`
- `open_issues: []`
- `operation.status: clean`

## Criterio de verificación

La operación solo se publica si `main` continúa exactamente en el Base SHA indicado. Tras publicar se verifican el padre del commit, la lista exacta de archivos afectados, los contenidos críticos, la coherencia de `estado.yaml` con `unidades.yaml`, la ausencia de PDF en GitHub y el CI completo cuando corresponda.

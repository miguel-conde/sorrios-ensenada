# Operación EDICION-FOLIO-307R-2026-09-06

- **Tipo:** cambio metodológico aprobado, edición, validación y cierre documental de unidad
- **Estado:** verified
- **Fecha:** 6 de septiembre de 2026
- **Unidad editorial:** `folio_307r`
- **Rama canónica:** `main`
- **Base SHA:** `2994efc960c896579fe00c3e46bed4c08d5b5092`
- **Manual previo:** Manual Editorial v1.5
- **Manual resultante:** Manual Editorial v1.6
- **Edición resultante:** v3.5
- **PDF autoritativo:** Drive file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`, página 3 derecha, 5.038.575 bytes, 18 páginas, SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- **Acceso al PDF:** lectura directa del archivo autoritativo obtenido de Google Drive como PDF real; Drive no modificado; sin Base64 y sin OCR

## Aprobación metodológica

Durante la lectura de folio 307r apareció un croquis del término con texto documental integrado en disposición no lineal. El Manual v1.5 no regulaba este caso. La operación se detuvo antes de publicar y se consultó al usuario.

El usuario aprobó incorporar al Manual el criterio siguiente: conservar todo el texto verbal legible; señalar el elemento gráfico mediante una indicación editorial; transcribir los rótulos del gráfico mediante un orden explícito y reproducible; no intentar reproducir la geometría mediante caracteres; y documentar en nota la relación espacial relevante. Las porciones ilegibles se rigen por los signos editoriales ya existentes.

El criterio se incorpora en Manual Editorial v1.6, § 11.1, y se aplica por primera vez en folio 307r.

## Resultado editorial

- Leída visualmente la mitad derecha de la página 3, sin OCR.
- Transcrita la respuesta 2.ª y la parte de la respuesta 3.ª contenida en la unidad.
- La segunda respuesta declara que el concejo es de `Señorío`, pertenece al `Ex[celentísi]mo S[eño]r Conde De Luna` y que por esa razón no pagan derechos algunos.
- La tercera respuesta expresa la circunferencia del término y sus dimensiones Oriente-Poniente y Norte-Sur, y comienza la enumeración de linderos.
- Se documentan `Tapia`, `Rioseco` y `Santa Maria` como topónimos de los linderos presentes en esta unidad.
- Se documentan `legua` y `baras` como medidas históricas, sin fijar equivalencia moderna.
- El croquis del término se marca editorialmente y sus rótulos se linealizan en un bloque separado; un segmento sin lectura responsable se representa mediante `[...]`.
- La serie de puntos tras `algunos` se trata como relleno gráfico sin valor verbal conforme al criterio vigente para signos no verbales.
- La tercera respuesta continúa materialmente en folio 307v.
- No quedan dudas abiertas.

## Derivados

- Glosario: alta de `Señorío`.
- Índice de personas: alta de `Conde De Luna`.
- Índice de topónimos: altas de `Tapia`, `Rioseco` y `Santa Maria`.
- Índice de instituciones: actualización de `Concejo de Ordas` y alta de `Señorío`.
- Índice de medidas: altas de `legua` y `baras`.
- Índice de oficios: sin cambios.
- Diario Editorial: registro del criterio aprobado y del cierre de folio 307r.
- `CAMBIOS.md`: registro de Manual v1.6, Edición v3.5 y cierre de folio 307r.

## Archivos de la operación

Modificados:

- `project/00_CONTROL/Manual_Editorial.md`
- `project/00_CONTROL/CAMBIOS.md`
- `project/00_CONTROL/proyecto.yaml`
- `project/00_CONTROL/estado.yaml`
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`
- `project/20_TRABAJO_EDITORIAL/Glosario.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Personas.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Toponimos.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Instituciones.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md`

Creado:

- `project/00_CONTROL/OPERACIONES/EDICION-FOLIO-307R-2026-09-06.md`

No se modifican `unidades.yaml`, el Índice de oficios ni el PDF autoritativo.

## Estado resultante esperado

- `last_validated_unit: folio_307r`
- `last_closed_unit: folio_307r`
- `current_unit: folio_307v`
- `next_unit: folio_308r`
- `current_location.pdf_page: 4`
- `current_location.position: left`
- `open_issues: []`
- `operation.status: clean`

## Criterio de verificación

La operación solo se publica si `main` continúa exactamente en el Base SHA indicado. Tras publicar se verifican el padre del commit, la lista exacta de archivos afectados, los contenidos críticos, la coherencia de `estado.yaml` con `unidades.yaml`, la ausencia de PDF en GitHub y el CI completo.
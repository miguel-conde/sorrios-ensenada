# Operación EDICION-FOLIO-321V-2026-09-16

- **Tipo:** edición, validación y cierre documental de unidad
- **Estado:** verified
- **Fecha:** 16 de septiembre de 2026
- **Unidad editorial:** `folio_321v`
- **Rama canónica:** `main`
- **Base SHA:** `f0839855725f5cf2c734d84731ace35f54693bdb`
- **Manual aplicado:** Manual Editorial v1.6
- **Edición vigente:** v3.5
- **PDF autoritativo:** `sorrios_ensenada_orden_lectura_calidad_original.pdf`, página 18 izquierda; Drive file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`; 18 páginas; tamaño 5038575 bytes; SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- **Acceso al PDF:** lectura visual directa del PDF autoritativo; sin OCR; Drive no modificado.

## Resultado editorial

- La unidad continúa directamente el último `Dom[ing]o` de folio 321r con `Suarez:` y prosigue `Remirio Rodriguez= an- / te mi Manuel Ant[oni]o Alonso==`.
- Con esta fórmula se completa el cierre textual de las Respuestas generales.
- La forma abreviada `Antº` se desarrolla como `Ant[oni]o` conforme al criterio general vigente.
- Se conserva la división visible `an-` / `te`, así como los signos `=`, `==` y los dos puntos visibles.
- Bajo la fórmula lineal aparecen dos firmas o rúbricas autógrafas de validación. Conforme al Manual Editorial v1.6, § 11, se describen en nota paleográfica y no se fuerza una transcripción lineal de sus trazos gráficos.
- Las formas débiles visibles en la mitad inferior se interpretan como transparencia o traspaso de tinta y no como texto propio de la unidad.
- No aparece ningún criterio metodológico nuevo y no quedan dudas abiertas en esta unidad.

## Control de Notas históricas A/B/C/D

- **A. Sin nota necesaria:** fórmula ordinaria de cierre y elementos gráficos de firma/rúbrica.
- **B. Glosario o índices:** `Dom[ing]o Suarez`, `Remirio Rodriguez`, `Manuel Ant[oni]o Alonso` y la función de `escribano`.
- **C. Nota histórica puntual:** no aparecen candidatos que requieran investigación externa nueva.
- **D. Diario o futuro Estudio Histórico:** práctica de firma, validación y cierre notarial del expediente.
- **Decisión:** la sección `Notas históricas` queda justificadamente sin notas puntuales. No se realiza investigación externa nueva.

## Derivados

- Índice de personas: se añaden las nuevas apariciones de `Dom[ing]o Suarez` y `Remirio Rodriguez` en folio 321v y se incorpora `Manuel Ant[oni]o Alonso`.
- Índice de oficios: se actualiza `escribano` con la identificación funcional de `Manuel Ant[oni]o Alonso` y la nueva aparición de folio 321v.
- Diario Editorial: registro del cierre y del control A/B/C/D.
- Glosario e índices de topónimos, instituciones y medidas: sin cambios justificados.

## Archivos de la operación

Modificados:

- `project/00_CONTROL/estado.yaml`
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Personas.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Oficios.md`

Creado:

- `project/00_CONTROL/OPERACIONES/EDICION-FOLIO-321V-2026-09-16.md`

No se modifican el Manual Editorial, `proyecto.yaml`, `unidades.yaml`, Glosario, los índices de topónimos, instituciones o medidas ni el PDF autoritativo.

## Estado resultante esperado

- `last_validated_unit: folio_321v`
- `last_closed_unit: folio_321v`
- `current_unit: hoja_enfrentada_posterior`
- `next_unit: null`
- `current_location.pdf_page: 18`
- `current_location.position: right`
- `open_issues: []`
- `operation.status: clean`

## Criterio de verificación

La operación solo se publica si `main` continúa exactamente en el Base SHA indicado. Tras publicar se verifican el padre del commit, la lista exacta de archivos afectados, el contenido de folio 321v, los derivados, la coherencia de `estado.yaml` con `unidades.yaml`, la ausencia del PDF en GitHub y el estado de CI.

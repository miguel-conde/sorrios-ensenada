# Operación EDICION-HOJA-ENFRENTADA-POSTERIOR-2026-09-16

- **Tipo:** edición, validación y cierre documental de unidad final; aplicación del criterio terminal aprobado
- **Estado:** verified
- **Fecha:** 16 de septiembre de 2026
- **Unidad editorial:** `hoja_enfrentada_posterior`
- **Rama canónica:** `main`
- **Base SHA:** `63bf22cf78bff7f09d8abe9399036bde6f59c1e1`
- **Manual aplicado:** Manual Editorial v1.6
- **Edición vigente:** v3.5
- **PDF autoritativo:** `sorrios_ensenada_orden_lectura_calidad_original.pdf`, página 18 derecha; Drive file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`; 18 páginas; tamaño 5038575 bytes; SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- **Acceso al PDF:** lectura visual directa del PDF autoritativo; sin OCR; Drive no modificado.
- **Aprobación:** criterio terminal aprobado expresamente por el usuario antes de publicar.

## Resultado editorial

- La mitad derecha de la página 18 no contiene escritura significativa propia y se transcribe `[En blanco]` conforme al Manual Editorial v1.6, § 12.
- Solo se perciben formas muy débiles compatibles con transparencia o traspaso de tinta y alguna mota, sin valor textual ni función documental identificable.
- No se observan foliación, signaturas ni otras marcas propias que requieran tratamiento adicional.
- La unidad anterior es `folio_321v`; no existe unidad posterior.
- No quedan dudas abiertas.

## Control de Notas históricas A/B/C/D

- **A. Sin nota necesaria:** condición material de cara en blanco y huellas sin valor textual.
- **B. Glosario o índices:** no aparecen elementos.
- **C. Nota histórica puntual:** no aparecen candidatos.
- **D. Diario o futuro Estudio Histórico:** no aparecen materiales.
- **Decisión:** la sección `Notas históricas` queda justificadamente sin notas puntuales. No se realiza investigación externa.

## Criterio terminal aprobado

- `last_validated_unit` y `last_closed_unit` pasan a `hoja_enfrentada_posterior`.
- `current_unit`, `next_unit` y `current_location` pasan a `null`.
- `pending_tasks` pasa a una lista vacía y `operation.status` queda en `clean`.
- Se mantienen `phase: edicion_paleografica` y `historical_study_enabled: false`; finalizar las unidades no activa automáticamente el Estudio Histórico.
- El esquema documental, el validador y el test de invariantes admiten explícitamente este estado terminal y conservan las comprobaciones del estado activo.
- El Manual Editorial no cambia: el criterio nuevo afecta a la representación técnica del estado al terminar la secuencia, no al método de transcripción.

## Derivados

- Diario Editorial: registro del cierre, del control A/B/C/D y del estado terminal.
- Glosario e índices: sin cambios justificados.

## Archivos de la operación

Modificados:

- `plugins/sorrios-ensenada/skills/editar-catastro-sorrios/references/document-schemas.md`
- `plugins/sorrios-ensenada/tools/validate_project.py`
- `project/00_CONTROL/estado.yaml`
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`
- `tests/test_editorial_invariants.py`

Creado:

- `project/00_CONTROL/OPERACIONES/EDICION-HOJA-ENFRENTADA-POSTERIOR-2026-09-16.md`

No se modifican el Manual Editorial, `proyecto.yaml`, `unidades.yaml`, Glosario, los índices ni el PDF autoritativo.

## Estado resultante esperado

- `phase: edicion_paleografica`
- `last_validated_unit: hoja_enfrentada_posterior`
- `last_closed_unit: hoja_enfrentada_posterior`
- `current_unit: null`
- `next_unit: null`
- `current_location: null`
- `open_issues: []`
- `pending_tasks: []`
- `operation.status: clean`
- `historical_study_enabled: false`

## Criterio de verificación

La operación solo se publica si `main` continúa exactamente en el Base SHA indicado. Antes de publicar se ejecutan el validador y la suite completa de tests sobre el conjunto preparado. Tras publicar se verifican el padre del commit, la lista exacta de archivos afectados, la transcripción `[En blanco]`, el estado terminal, las 35 unidades con sus seis secciones, la ausencia del PDF en GitHub y el resultado del workflow de CI.

# Operación ACTIVACION-ESTUDIO-HISTORICO-2026-09-16

- **Tipo:** transición formal de fase y activación del Estudio Histórico
- **Estado:** verified
- **Fecha:** 16 de septiembre de 2026
- **Rama canónica:** `main`
- **Base SHA:** `905c5b3ad456ab2ad4425544bb3ad45ea7f38cbd`
- **Manual aplicado:** Manual Editorial v1.6
- **Edición vigente:** v3.5
- **Aprobación:** activación autorizada expresamente por el usuario tras revisar el estado y el Manual.

## Condiciones previas comprobadas

- Las 35 unidades están validadas y cerradas.
- `last_validated_unit` y `last_closed_unit` son `hoja_enfrentada_posterior`.
- `current_unit`, `next_unit` y `current_location` son `null`.
- `open_issues` y `pending_tasks` están vacíos.
- `operation.status` es `clean`.
- El Estudio Histórico seguía desactivado y su documento estaba reservado para la segunda fase.
- El Manual Editorial v1.6 define el Estudio Histórico como obra independiente basada exclusivamente en la edición paleográfica validada.

## Decisión de fase

Se activa formalmente la segunda fase del proyecto:

- `phase.current: estudio_historico`;
- `phase.historical_study_enabled: true`;
- `documents.historical_study.enabled: true`;
- `estado.yaml.phase: estudio_historico`.

El estado terminal de la edición paleográfica se conserva sin cambios en sus 35 unidades.

## Alcance del Estudio Histórico

- La base documental sigue siendo exclusivamente la edición paleográfica validada.
- Glosario, índices y Diario Editorial pueden servir como instrumentos de apoyo, pero no sustituyen a la edición como base documental.
- Las fuentes externas utilizadas durante la edición para identificaciones o equivalencias no pasan a ser fuentes autónomas del Estudio Histórico.
- Esta activación no amplía el corpus documental ni modifica el Manual Editorial.
- El Estudio Histórico nunca modifica la transcripción paleográfica.

## Refuerzo técnico de la transición

Se amplía `document-schemas.md` para definir las fases admitidas y las condiciones de activación.

`validate_project.py` comprueba desde esta operación:

- concordancia entre `proyecto.yaml` y `estado.yaml`;
- concordancia de los dos indicadores de activación del Estudio Histórico;
- cierre de las 35 unidades antes de activar la segunda fase;
- ausencia de dudas y tareas pendientes;
- `operation.status: clean` durante la fase histórica.

Los tests incorporan comprobaciones expresas de la nueva fase y conservan las invariantes de la edición paleográfica.

## Archivos de la operación

Modificados:

- `project/00_CONTROL/proyecto.yaml`
- `project/00_CONTROL/estado.yaml`
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md`
- `plugins/sorrios-ensenada/skills/editar-catastro-sorrios/references/document-schemas.md`
- `plugins/sorrios-ensenada/tools/validate_project.py`
- `tests/test_editorial_invariants.py`
- `tests/test_project_schema.py`

Creado:

- `project/00_CONTROL/OPERACIONES/ACTIVACION-ESTUDIO-HISTORICO-2026-09-16.md`

No se modifican:

- `project/00_CONTROL/Manual_Editorial.md`;
- `project/00_CONTROL/unidades.yaml`;
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`;
- `project/20_TRABAJO_EDITORIAL/Glosario.md`;
- los cinco índices;
- el PDF autoritativo de Drive.

## Estado resultante esperado

- `phase: estudio_historico` en `estado.yaml`;
- `phase.current: estudio_historico` en `proyecto.yaml`;
- `historical_study_enabled: true`;
- `documents.historical_study.enabled: true`;
- `last_validated_unit: hoja_enfrentada_posterior`;
- `last_closed_unit: hoja_enfrentada_posterior`;
- `current_unit: null`;
- `next_unit: null`;
- `current_location: null`;
- `open_issues: []`;
- `pending_tasks: []`;
- `operation.status: clean`.

## Verificación

La operación se publica solo si `main` continúa exactamente en el Base SHA indicado. Tras publicar se comprobarán el padre y la lista exacta de archivos del commit, los controles de fase, la conservación de la edición paleográfica, la ausencia del PDF en GitHub y el resultado del workflow de CI.

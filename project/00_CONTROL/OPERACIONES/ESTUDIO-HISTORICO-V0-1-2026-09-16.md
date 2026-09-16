# Operación ESTUDIO-HISTORICO-V0-1-2026-09-16

- **Tipo:** elaboración de la primera síntesis sistemática del Estudio Histórico
- **Estado:** prepared
- **Fecha:** 16 de septiembre de 2026
- **Rama canónica:** `main`
- **Base SHA:** `7838bc0ca4bb5fb313e7488d08c1a92125bf1640`
- **Manual aplicado:** Manual Editorial v1.6
- **Edición base:** Edición Crítica v3.5
- **Aprobación:** el usuario ordenó continuar con el Estudio Histórico una vez activada formalmente la fase.

## Condiciones previas comprobadas

- `phase.current: estudio_historico`.
- `historical_study_enabled: true`.
- `documents.historical_study.enabled: true`.
- Las 35 unidades están validadas y cerradas.
- `last_validated_unit` y `last_closed_unit` son `hoja_enfrentada_posterior`.
- `current_unit`, `next_unit` y `current_location` son `null`.
- `open_issues` y `pending_tasks` están vacíos.
- `operation.status` es `clean`.

## Alcance de esta versión

Se sustituye el documento de activación mínima del Estudio Histórico por una primera síntesis analítica de conjunto, trazable a la Edición Crítica validada.

La versión 0.1 estudia:

- unidad local, señorío y organización del concejo;
- término y linderos;
- tipos y calidades de tierra;
- rotaciones, simiente y rendimientos;
- precios, diezmos, primicia y voto;
- río y molinos;
- ganadería y apicultura;
- vecindad, vivienda y categorías de población fiscal;
- hacienda del común, alcabalas y repartimientos;
- taberna, pozo de pesca y servicios;
- trabajo, jornaleros, labradores, oficio de herrero, pobres y clero;
- papel de declarantes, peritos y escribano;
- síntesis interpretativa y líneas de análisis posteriores.

## Regla documental aplicada

- La base local exclusiva es `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`, v3.5.
- Glosario, índices y Diario solo actúan como apoyo.
- No se incorpora en esta operación un corpus histórico externo autónomo.
- Las inferencias se distinguen de los datos documentales.
- No se convierten medidas históricas a unidades modernas cuando el expediente no establece equivalencia.
- No se modifica la transcripción paleográfica ni su aparato.

## Archivos de la operación

Modificado:

- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md`

Creado:

- `project/00_CONTROL/OPERACIONES/ESTUDIO-HISTORICO-V0-1-2026-09-16.md`

No se modifican:

- `project/00_CONTROL/proyecto.yaml`;
- `project/00_CONTROL/estado.yaml`;
- `project/00_CONTROL/unidades.yaml`;
- `project/00_CONTROL/Manual_Editorial.md`;
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`;
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`;
- `project/20_TRABAJO_EDITORIAL/Glosario.md`;
- los índices;
- el PDF autoritativo de Drive.

## Invariantes que deben conservarse

- fase `estudio_historico` activa;
- 35 unidades validadas y cerradas;
- estado terminal sin unidad corriente;
- `open_issues: []`;
- `pending_tasks: []`;
- `operation.status: clean`;
- Edición Crítica v3.5 intacta;
- PDF ausente del repositorio.

## Verificación prevista

La operación solo se publicará si `main` continúa exactamente en el Base SHA indicado. Después de publicar se comprobarán:

1. padre del commit;
2. lista exacta de dos archivos cambiados;
3. contenido y SHA de `Estudio_Historico.md`;
4. conservación de `estado.yaml` y `proyecto.yaml`;
5. ausencia de cambios en la Edición Crítica;
6. estado de CI asociado al commit.

Tras la publicación y verificación, este registro representa una operación completada aunque su texto interno conserve `Estado: prepared` como fotografía del paquete previo a publicar; el historial Git y la verificación posterior determinan el estado técnico efectivo.
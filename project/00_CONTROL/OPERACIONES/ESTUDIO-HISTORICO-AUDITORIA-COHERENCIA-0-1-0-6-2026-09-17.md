# Operación — Auditoría final de coherencia del Estudio Histórico 0.1–0.6

**Fecha:** 17 de septiembre de 2026  
**Estado:** prepared  
**Modo:** auditoría / estudio histórico  
**Proyecto:** `sorrios-ensenada-1752`  
**Rama:** `main`  
**Base SHA:** `7d50e87645b0ae483d3557b1c68267eaab23daff`  
**Edición base:** Edición Crítica v3.5, blob `52b10fdc0b280e5fe4dd5d27e72dd08fed7c0bb8`  
**Manual aplicado:** Manual Editorial v1.6

## Objeto

Auditar la coherencia completa de las capas 0.1–0.6 del Estudio Histórico contra la Edición Crítica v3.5, sin modificar el documento canónico, y publicar un informe trazable con severidad, evidencia y propuesta de resolución.

## Condiciones previas comprobadas

- `phase.current: estudio_historico`;
- `historical_study_enabled: true`;
- 35 unidades validadas y cerradas;
- `last_validated_unit` y `last_closed_unit`: `hoja_enfrentada_posterior`;
- sin unidad corriente ni siguiente;
- `open_issues: []`;
- `pending_tasks: []`;
- `operation.status: clean`;
- rama canónica fijada en el Base SHA indicado;
- CI de la base: `Portable Python tests` ejecución 156, `completed/success`.

## Corpus auditado

- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md`;
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md`;
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Reconstruccion_Economica_Integrada.md`;
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Matriz_Contabilidad_Social_y_Grafo_Economico.md`;
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Mapa_Vulnerabilidades_Economicas.md`;
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Sintesis_Socioeconomica_Integral.md`;
- sus seis registros de operación;
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`, v3.5;
- `project/00_CONTROL/proyecto.yaml`, `estado.yaml` y `unidades.yaml`;
- Manual Editorial v1.6.

## Método

1. contraste de datos con respuestas y folios de la Edición Crítica;
2. recomputación independiente de cálculos;
3. comparación transversal de cifras, términos y relaciones;
4. revisión de la separación `D/C/I`;
5. auditoría de trazabilidad, registros y secuencia técnica;
6. comprobación de estructura, controles, ausencia de PDF y CI.

## Entregables de la operación

Se crean:

- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Auditoria_Coherencia_0_1_0_6.md`;
- `project/00_CONTROL/OPERACIONES/ESTUDIO-HISTORICO-AUDITORIA-COHERENCIA-0-1-0-6-2026-09-17.md`.

## Resultado resumido

- 0 contradicciones numéricas críticas;
- 2 hallazgos de severidad alta;
- 7 hallazgos de severidad media;
- 6 hallazgos de severidad baja;
- cálculos nucleares recomputados sin discrepancias;
- propuesta de arquitectura y terminología para una futura versión canónica;
- recomendación expresa de no corregir parcialmente `Estudio_Historico.md` antes de la consolidación integral.

## Archivos no modificados

- `project/00_CONTROL/proyecto.yaml`;
- `project/00_CONTROL/estado.yaml`;
- `project/00_CONTROL/unidades.yaml`;
- `project/00_CONTROL/Manual_Editorial.md`;
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`;
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`;
- `project/20_TRABAJO_EDITORIAL/Glosario.md`;
- los índices;
- los seis documentos históricos 0.1–0.6;
- el PDF autoritativo de Google Drive.

## Publicación y verificación prevista

Los dos archivos se publicarán en un único commit atómico basado en el Base SHA. Antes de mover `main` se comprobará de nuevo que la rama no haya cambiado. Después se verificarán:

1. SHA y padre del commit;
2. lista exacta de dos archivos añadidos;
3. contenido y blob de ambos archivos;
4. conservación de controles y Edición Crítica;
5. ausencia de PDF;
6. resultado del workflow `Portable Python tests`.

Este registro conserva `Estado: prepared` como fotografía del paquete previo a la publicación. El commit, la comparación y la verificación posterior determinan el cierre técnico efectivo.


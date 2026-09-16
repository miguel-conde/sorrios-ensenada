# Operación — Mapa de vulnerabilidades económicas

**Fecha:** 16 de septiembre de 2026  
**Proyecto:** `sorrios-ensenada-1752`  
**Fase:** `estudio_historico`  
**Base:** `main@a612df60e5e4f079f6d9aa9a97f810e86805fcca`  
**Estado de preparación:** `prepared`

## 1. Objeto

Publicar un análisis derivado que formalice las vulnerabilidades económicas, dependencias, mecanismos de propagación y amortiguadores identificables dentro del corpus histórico vigente.

## 2. Fuentes usadas

Fuente documental exclusiva:

- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`, v3.5.

Derivados de apoyo, sin rango de fuente autónoma:

- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md`, v0.2;
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Reconstruccion_Economica_Integrada.md`, v0.3;
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Matriz_Contabilidad_Social_y_Grafo_Economico.md`, v0.4.

No se amplía el corpus y no se incorporan fuentes externas.

## 3. Entregable

Se crea:

- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Mapa_Vulnerabilidades_Economicas.md`

Versión prevista: v0.5.

## 4. Método

El documento separa:

- fragilidad observada;
- dependencia estructural latente;
- mecanismos de propagación;
- amortiguadores documentados.

No se asignan probabilidades ni puntuaciones agregadas de riesgo. Las clases descriptivas se justifican por exposición, centralidad, sustitución y materialización documental.

Se preservan las restricciones metodológicas vigentes:

- sin conversiones a unidades modernas;
- sin equivalencias externas entre unidades históricas;
- sin cierre artificial de cuentas;
- sin completar cabidas por residuo;
- sin estimar producto, renta, autoconsumo, deuda o presión fiscal total;
- sin convertir escenarios analíticos en crisis efectivamente observadas.

## 5. Vulnerabilidades formalizadas

El análisis incluye doce vulnerabilidades principales:

1. concentración cerealista en centeno;
2. barbecho estructural del centenal;
3. peso elevado de tercera calidad;
4. dependencia de bienes comunales;
5. riesgo hidráulico observado;
6. dependencia molinera de un factor hidráulico común;
7. hacienda común sin propios, arbitrios ni renta;
8. interacción entre cargas institucionales y base productiva;
9. trabajo incrustado en hogares;
10. servicios colectivos y pluriactividad;
11. concentración sectorial de determinados activos;
12. apertura supralocal incompletamente observable.

Se modelan además cuatro escenarios de propagación:

- mala cosecha cerealista;
- crecida y daño hidráulico;
- restricción de recursos comunales;
- aumento de necesidad colectiva.

Solo el riesgo hidráulico tiene materialización explícita en el expediente; los demás escenarios se identifican expresamente como contrafactuales analíticos cuando corresponda.

## 6. Hallazgos metodológicos relevantes

- La propiedad molinera está distribuida, pero el riesgo físico presenta causa común hidráulica.
- Los bienes comunales son simultáneamente amortiguadores y nodos de dependencia.
- El común carece de ingresos propios declarados y financia sus gastos mediante repartimiento.
- La fiscalidad hace visibles algunos riesgos monetarios, pero oculta parte del valor resiliente de comunes, trabajo familiar y organización vecinal.
- Los cuatro nodos de mayor centralidad funcional dentro del modelo son hogares, centeno, comunes y sistema hidráulico.

## 7. Integridad del proyecto

Esta operación no debe modificar:

- `project/00_CONTROL/proyecto.yaml`;
- `project/00_CONTROL/estado.yaml`;
- unidades editoriales;
- Manual Editorial;
- Edición Crítica;
- Diario Editorial;
- Glosario;
- índices;
- PDF autoritativo;
- documentos históricos v0.1–v0.4.

El estado esperado al terminar sigue siendo:

- `phase: estudio_historico`;
- `open_issues: []`;
- `pending_tasks: []`;
- `operation.status: clean`.

## 8. Publicación

El cierre técnico de la operación queda determinado por:

1. commit de publicación;
2. comparación base → head;
3. conservación del estado canónico;
4. resultado de CI `Portable Python tests`.

Este registro describe el paquete preparado antes de conocer el SHA final de publicación.
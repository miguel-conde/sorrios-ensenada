# Operación ESTUDIO-HISTORICO-ANALISIS-CUANTITATIVO-2026-09-16

- **Tipo:** elaboración del análisis cuantitativo sistemático del expediente
- **Estado:** prepared
- **Fecha:** 16 de septiembre de 2026
- **Rama canónica:** `main`
- **Base SHA:** `a88577c0cb6b3249a11bee379067f24f45eeaaa3`
- **Manual aplicado:** Manual Editorial v1.6
- **Edición base:** Edición Crítica v3.5
- **Fase:** `estudio_historico`
- **Aprobación:** el usuario ordenó avanzar con la matriz respuesta→dato→interpretación, tierras y calidades, rendimientos, precios, cargas, red de propietarios y estructura fiscal.

## Alcance

Se crea un anexo cuantitativo autónomo dentro del Estudio Histórico, basado exclusivamente en la Edición Crítica validada.

Incluye:

- matriz de las 40 respuestas;
- cuadro de las trece clases de tierra;
- contraste entre calidades de las respuestas 5 y 10;
- desglose completo de la cabida cuantificada;
- subtotales comparables sin convertir celemínes;
- simiente y rendimientos;
- ratios internos producto/simiente cuando las unidades coinciden;
- precios y valores derivados mediante equivalencias internas del expediente;
- ganadería y apicultura;
- red de propietarios de molinos, colmenas y derechos económicos;
- cargas eclesiásticas, comunales y señoriales;
- flujos monetarios mínimos agregables;
- trabajo y utilidad diaria;
- auditoría de consistencia cuantitativa.

## Reglas metodológicas

- No se amplía el corpus documental.
- No se usan equivalencias externas para medidas o moneda.
- Solo se aplican las relaciones internas `4 quartales = 1 fanega` y `4 montones = 1 carro`.
- Se mantienen separadas las medidas principales y los celemínes de la respuesta 10.
- No se completa por residuo la cabida de los montes.
- No se corrigen las discordancias entre las respuestas 5 y 10.
- No se suman categorías demográficas o laborales potencialmente solapadas.
- Los cálculos derivados se etiquetan como tales y no se presentan como cifras manuscritas.

## Hallazgos de consistencia de la fuente

Se registran sin alterar la Edición Crítica:

1. R5 declara primera y segunda calidad para prados cercados de secano; R10 declara solo segunda y la llama única.
2. R5 declara primera y tercera calidad para montes; R10 no los cuantifica.
3. R5 declara primera y tercera calidad para sotos; R10 cuantifica solo tercera y la llama única.
4. El total declarado de cabida no se reconcilia con las partidas sin una equivalencia interna entre medida principal y celemín.
5. La simiente de linaza en linar de regadío no se explicita por separado para todas las calidades.

Estas diferencias se consideran propiedades del testimonio documental, no incidencias editoriales abiertas.

## Archivos de la operación

Creado:

- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md`
- `project/00_CONTROL/OPERACIONES/ESTUDIO-HISTORICO-ANALISIS-CUANTITATIVO-2026-09-16.md`

No se modifican:

- `project/00_CONTROL/proyecto.yaml`;
- `project/00_CONTROL/estado.yaml`;
- `project/00_CONTROL/unidades.yaml`;
- `project/00_CONTROL/Manual_Editorial.md`;
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`;
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`;
- `project/20_TRABAJO_EDITORIAL/Glosario.md`;
- los índices;
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md`;
- el PDF autoritativo de Drive.

## Verificación prevista

La operación solo se publicará si `main` continúa exactamente en el Base SHA indicado. Tras publicar se comprobarán:

1. padre del commit;
2. lista exacta de dos archivos añadidos;
3. contenido y SHA del análisis cuantitativo;
4. conservación de la Edición Crítica v3.5;
5. conservación de `operation.status: clean`;
6. resultado del workflow de CI.

El registro conserva `Estado: prepared` como fotografía del paquete previo a la publicación; el commit, la comparación y CI determinan después el estado técnico efectivo.
# Operación ESTUDIO-HISTORICO-MCSH-GRAFO-ECONOMICO-2026-09-16

- **Tipo:** formalización de matriz de contabilidad social histórica y grafo económico
- **Estado:** prepared
- **Fecha:** 16 de septiembre de 2026
- **Rama canónica:** `main`
- **Base SHA:** `de3dd43bd65191222971da89d22101f3399c0514`
- **Manual aplicado:** Manual Editorial v1.6
- **Edición base:** Edición Crítica v3.5
- **Fase:** `estudio_historico`
- **Aprobación:** el usuario ordenó avanzar tras proponerse formalizar la matriz de contabilidad social histórica y el grafo económico.

## Alcance

Se crea una formalización derivada que integra:

- cuentas institucionales principales;
- cuentas satélite productivas;
- libro mayor de flujos con identificadores F01–F27;
- matriz institucional origen→destino;
- submatriz monetaria observada;
- cuenta parcial del común;
- cuentas satélite de agricultura, molinos, apicultura y trabajo;
- grafo general del sistema económico;
- grafo de personas, activos y derechos;
- tabla de nodos multiplex;
- circuitos de circulación;
- controles de cierre posibles;
- mapa explícito de información faltante.

## Reglas metodológicas

- No se amplía el corpus documental.
- La base primaria continúa siendo exclusivamente la Edición Crítica validada.
- `Analisis_Cuantitativo.md` v0.2 y `Reconstruccion_Economica_Integrada.md` v0.3 se usan como productos derivados de apoyo, no como fuentes autónomas.
- No se construye una SAM moderna cerrada artificialmente.
- No se crean partidas de equilibrio.
- Una celda vacía de la matriz significa `no documentado`, no cero económico.
- Se conservan las unidades originales.
- No se convierten cargas a quartales o fanegas.
- No se convierten reales y maravedís a una unidad única.
- No se trata a propietarios de activos como sector independiente de los hogares; molinos y abejas se presentan como cuentas satélite.
- Los flujos funcionales que no tienen magnitud total explícita se marcan como interpretación apoyada en datos.
- No se infiere la residencia geográfica de receptores cuando el expediente no la proporciona.

## Criterios de modelización

La MCSH emplea ocho cuentas institucionales:

- HOG: hogares / vecinos productores;
- COM: común / concejo;
- CUR: cura Manuel Antonio de Bega/Vega;
- IGL: iglesia local;
- SAN: fábrica del Apóstol Santiago;
- CON: Conde de Luna;
- EXT: instituciones externas inequívocas;
- NID: contraparte no identificada.

Las actividades productivas se mantienen en cuentas satélite para evitar doble cómputo social:

- AGR;
- TRA;
- COMR;
- MOL;
- API;
- TAB;
- RIO.

`NID` no es residual de balance: solo representa contrapartes que el expediente deja sin identificar.

## Cálculos incorporados

Se reutilizan, con trazabilidad, cálculos ya validados en los documentos derivados precedentes:

- mínimo monetario institucional: 1.006 reales/año;
- gasto común explícito: 233 reales/año;
- salida geográfica externa inequívoca del común: 25/233 = 10,73%;
- suelo externo respecto del mínimo institucional: 25/1.006 = 2,49%;
- utilidad apícola total: 36 reales/año;
- utilidad de ruedas fijas: 26 cargas de centeno;
- cierres internos de jornaleros, abejas, molinos, gastos comunes, lino, cerda, vaca y yegua.

No se suman flujos sucesivos del mismo circuito para construir un tamaño económico total.

## Archivos de la operación

Creados:

- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Matriz_Contabilidad_Social_y_Grafo_Economico.md`
- `project/00_CONTROL/OPERACIONES/ESTUDIO-HISTORICO-MCSH-GRAFO-ECONOMICO-2026-09-16.md`

La publicación técnica se realiza en dos commits secuenciales del mismo avance: primero el documento analítico y después este registro de operación. La verificación se hace sobre la comparación completa `Base SHA → HEAD`, que debe contener exactamente estos dos archivos añadidos.

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
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md`;
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Reconstruccion_Economica_Integrada.md`;
- el PDF autoritativo de Drive.

## Verificación prevista

Tras publicar se comprobarán:

1. continuidad desde el Base SHA;
2. lista exacta de dos archivos añadidos en la comparación completa;
3. conservación de la Edición Crítica v3.5;
4. conservación de los análisis v0.2 y v0.3;
5. conservación de `phase: estudio_historico` y `operation.status: clean`;
6. resultado del workflow de CI sobre el HEAD final.

El registro conserva `Estado: prepared` como fotografía del paquete anterior a la verificación final; la comparación y CI determinan el resultado técnico efectivo.
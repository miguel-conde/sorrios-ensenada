# Operación — Síntesis socioeconómica integral del Estudio Histórico

**Fecha:** 17 de septiembre de 2026  
**Estado:** prepared  
**Modo:** estudio histórico  
**Proyecto:** `sorrios-ensenada-1752`  
**Rama:** `main`  
**Base técnica:** `4cec9c417b15352f361f970604ca45b84031dad3`

## Objeto

Consolidar en un único documento interpretativo los resultados obtenidos en las versiones 0.1–0.5 del Estudio Histórico, manteniendo como base documental exclusiva la Edición Crítica v3.5.

## Archivo creado

- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Sintesis_Socioeconomica_Integral.md`

## Fuentes internas utilizadas

### Fuente documental exclusiva

- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`, v3.5.

### Instrumentos derivados de apoyo

- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md`, v0.1;
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md`, v0.2;
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Reconstruccion_Economica_Integrada.md`, v0.3;
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Matriz_Contabilidad_Social_y_Grafo_Economico.md`, v0.4;
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Mapa_Vulnerabilidades_Economicas.md`, v0.5.

Los instrumentos derivados no se tratan como nuevas fuentes históricas y no amplían el corpus.

## Criterios aplicados

1. Mantener los niveles `D` — dato documental, `C` — cálculo interno e `I` — interpretación.
2. No convertir medidas históricas a unidades modernas.
3. No introducir equivalencias externas entre medida principal y celemín, cargas y quartales, ni reales y maravedís.
4. Conservar la discordancia entre el total declarado de cabida y la suma de partidas explícitas.
5. No reconstruir por residuo la cabida omitida de montes.
6. No sumar categorías vecinales, residenciales, laborales o eclesiásticas como si fueran conjuntos demográficos disjuntos.
7. No estimar población total, renta por hogar, producto total, desigualdad general ni nivel de vida.
8. No convertir utilidad fiscal nula en ausencia de valor económico.
9. No convertir vulnerabilidades estructurales en crisis históricas no documentadas.
10. Mantener separados los circuitos doméstico-productivo, ganadero, hidráulico, eclesiástico, señorial-fiscal y concejil-comunal.

## Contenido consolidado

La síntesis integra:

- escala local y jurisdicción;
- población fiscal, residencia y vivienda;
- estructura social y hogar;
- territorio, clases y calidades de tierra;
- centralidad del centeno y barbecho;
- lino, cebada y especialización complementaria;
- prados, ganadería y reproducción material;
- recursos comunales;
- río y molinos;
- apicultura;
- trabajo, dependencia familiar y pluriactividad;
- propiedad productiva y derechos institucionales;
- fiscalidad, Iglesia y hacienda del común;
- servicios colectivos;
- monetización y conexiones exteriores;
- vulnerabilidad y resiliencia;
- límites sobre bienestar, población y desigualdad;
- modelo socioeconómico integrado;
- cuestiones abiertas dentro del corpus vigente.

## Cálculos reutilizados

No se introduce ninguna equivalencia nueva. Se reutilizan cálculos ya auditados en las capas anteriores, entre ellos:

- 3.811,5 medidas principales explícitas + 7 celemínes frente a 3.823 medidas + 1 celemín declarados;
- distribución de las medidas principales explícitas por calidad: 17,47% / 36,68% / 45,85%;
- subtotal cultivado comparable: 2.953,5 medidas principales;
- centenales dentro de ese subtotal: 2.750,5 y 93,13%;
- índice anualizado analítico: 1.578,25, con 87,14% correspondiente a centenales;
- 18 pies de abejas y 36 reales/año de utilidad regulada;
- 13/18 pies en los dos mayores titulares, 72,2%;
- 233 reales de gasto común explícito;
- 25 reales de destino exterior inequívoco dentro de ese subtotal, 10,73%;
- mínimo monetario institucional de 1.006 reales, sin interpretarlo como presión fiscal total;
- 18 jornaleros = 14 hijos de familia + 3 criados + 1 jornalero exclusivo.

## Decisión metodológica

No apareció ningún problema que exigiera un criterio histórico nuevo. La operación permanece dentro del corpus y de las reglas ya aprobadas.

Las comparaciones externas, equivalencias históricas externas, reconstrucciones demográficas o monetarias y estimaciones de nivel de vida quedan expresamente fuera de alcance y requerirían aprobación previa.

## Efectos sobre archivos canónicos

- No se modifica `Edicion_Critica.md`.
- No se modifica `Estudio_Historico.md` v0.1.
- No se modifica `Analisis_Cuantitativo.md` v0.2.
- No se modifica `Reconstruccion_Economica_Integrada.md` v0.3.
- No se modifica `Matriz_Contabilidad_Social_y_Grafo_Economico.md` v0.4.
- No se modifica `Mapa_Vulnerabilidades_Economicas.md` v0.5.
- No se modifica `estado.yaml`.
- No se modifica el PDF autoritativo de Google Drive.

## Validación prevista

Tras la publicación se comprobará:

1. que la rama `main` avance por fast-forward desde la base indicada;
2. que el diff contenga únicamente este registro y la nueva síntesis;
3. que `estado.yaml` continúe `clean` y sin incidencias;
4. que `Portable Python tests` termine correctamente en la matriz Ubuntu/Windows y Python 3.10/3.13.

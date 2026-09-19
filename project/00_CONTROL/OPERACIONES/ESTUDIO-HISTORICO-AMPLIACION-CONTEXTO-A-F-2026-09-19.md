# Operación: ampliación externa A–F del Estudio Histórico

**Fecha:** 19 de septiembre de 2026  
**Estado:** verified  
**Modo:** estudio histórico  
**Rama:** main  
**Base SHA:** `19eca221b173427f2ec5d9d2be771219ec7563bc`  
**Estado inicial:** `operation.status: clean`  
**Fase:** `estudio_historico`

## Objeto

Incorporar al Estudio Histórico la investigación externa aprobada sobre los bloques A–F, ampliar la trazabilidad de sus afirmaciones y mantener sin cambios la Edición Crítica y el método editorial.

## Alcance documental

- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md`: v1.1 → v1.2.
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md`: v1.1 → v1.2.
- `project/00_CONTROL/CAMBIOS.md`: alta de la operación.
- `project/00_CONTROL/OPERACIONES/ESTUDIO-HISTORICO-AMPLIACION-CONTEXTO-A-F-2026-09-19.md`: alta de este registro.

## Contenido incorporado

### A. Lugar y territorio

- Serie documental 1215–actualidad.
- Contexto patrimonial de 1215.
- Venta de 1267 con partes, precio, comprador y bienes enumerados.
- Testimonios de 1601, 1715, 1768, 1831, 1836, 1848 y actualidad.
- Distinción entre Concejo de Ordás histórico y municipio posterior.

### B. Poder, jurisdicción y señorío

- Ordás como jurisdicción del conde de Luna.
- Identificación externa del titular en 1752 con Francisco Alfonso Pimentel, XV conde de Luna.
- `Abogado de los Reales Consejos` como título o habilitación profesional.
- Cautela expresa sobre el fundamento de las alcabalas y el pozo de pesca.

### C. Población y sociedad

- Diferencia entre vecino, medio vecino, residente, individuo y categoría laboral.
- Dato parroquial de 1768 conservado como observación posterior no convertible en población de 1752.

### D. Sistema agrario

- Medida por sembradura sin conversión moderna.
- Contexto regional del lino, los prados de uno y dos pelos, el ferrañal y el ganado `arenta`.

### E. Molinos y servicios

- Contexto provincial del molino hidráulico y de la molienda estacional.
- Explicación institucional de la taberna por vecera.

### F. Derechos, cargas y hacienda común

- Voto de Santiago, Hospital de Inocentes, Mesta, propios y arbitrios, repartimiento y Corpus.
- Permanecen abiertas la causa jurídica del pago al Hospital y la naturaleza exacta del derecho de Mesta.

## Reglas aplicadas

- La Edición Crítica conserva autoridad sobre el expediente.
- Cada dato externo se marca con nivel E y cita su fuente.
- Se distinguen dato manuscrito, contexto externo, interpretación y límite.
- Ninguna comparación regional genera una cifra, conversión, contrato o circuito comercial para Sorribos.
- Los tres asuntos no resueltos quedan registrados como `LIM-011`–`LIM-013`.

## Fuentes externas

Se incorporan las fuentes enlazadas en `Estudio_Historico.md` y en las entradas `TOP-004`–`FIS-017` del registro. Incluyen documentación o estudios de la Catedral de León, AHN, PARES, Real Chancillería, B.R.A.H.M., `Gaceta de Madrid`, Ayuntamiento de Santa María de Ordás y bibliografía sobre jurisdicción, población, metrología, lino, prados, léxico rural, ganadería, molinos, Voto de Santiago, Hospital de Inocentes, Mesta y haciendas locales.

## Estado y exclusiones

- La Edición Crítica permanece en v3.6.
- El Manual Editorial permanece en v1.6.
- No cambian `proyecto.yaml`, `estado.yaml` ni `unidades.yaml`.
- No cambian Diario, Glosario, índices, análisis 0.2–0.6 ni PDF autoritativo.
- La operación no reabre unidades ni altera transcripciones.

## Validación

- Unicidad de IDs definidos: PASS.
- Resolución de todos los IDs citados por el Estudio: PASS.
- Estructura regular de tablas Markdown: PASS.
- 25 entradas contextuales E y tres límites nuevos: PASS.
- Las tres cuestiones abiertas figuran en texto y registro: PASS.
- `estado.yaml` conserva `operation.status: clean`: PASS.
- El conjunto de publicación contiene exactamente los cuatro archivos declarados: pendiente de verificación tras mover el ref.
- Commit, padre, rutas y contenido: pendiente de verificación tras mover el ref.

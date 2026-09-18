# Auditoría final de coherencia del Estudio Histórico 0.1–0.6

## Sorribos y Santibáñez de Ordás (1752)

**Tipo:** auditoría documental, cuantitativa, interpretativa y de trazabilidad  
**Fecha:** 17 de septiembre de 2026  
**Base técnica auditada:** `main@7d50e87645b0ae483d3557b1c68267eaab23daff`  
**Autoridad documental:** `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`, versión 3.5, blob `52b10fdc0b280e5fe4dd5d27e72dd08fed7c0bb8`  
**Manual aplicable:** Manual Editorial v1.6  
**Alcance:** versiones analíticas 0.1–0.6 y sus seis registros de operación  
**Efecto:** este informe no modifica `Estudio_Historico.md`, la Edición Crítica, los controles, el Diario, el Glosario ni los índices.

## 0. Resultado ejecutivo

La serie 0.1–0.6 es globalmente coherente con la Edición Crítica v3.5. No se ha encontrado ninguna cifra nuclear incompatible entre capas ni ningún cálculo aritmético incorrecto en los conjuntos que estructuran la interpretación: cabida, distribución por calidades, concentración centenal, abejas, ruedas, utilidades, gastos del común, mínimo monetario institucional, jornaleros y porcentajes derivados.

La auditoría sí identifica problemas que deben resolverse antes de convertir la síntesis en una versión canónica:

- **2 hallazgos de severidad alta**, ambos relacionados con la atribución de propiedad, administración o identidad institucional a los aprovechamientos de uso común;
- **7 hallazgos de severidad media**, relacionados con una contradicción metodológica aislada, causalidad hidráulica, introducción de nodos o funciones no documentados, clasificación `D/C/I`, pérdida de trazabilidad y protocolo de versiones/operaciones;
- **6 hallazgos de severidad baja**, principalmente terminológicos o de presentación;
- **0 contradicciones numéricas críticas** y **0 alteraciones detectadas** en la Edición Crítica v3.5.

La futura versión canónica puede construirse con seguridad a partir de v0.6, siempre que se corrijan primero los hallazgos A-01 y A-02, se rebajen las inferencias señaladas en M-02 y M-03 y se incorpore un registro único de afirmaciones, cálculos y referencias.

## 1. Criterio de severidad

| Severidad | Criterio |
|---|---|
| Alta | Puede atribuir a una persona o institución una propiedad, función o relación histórica no demostrada y afectar la tesis de conjunto. |
| Media | No altera por sí sola los datos básicos, pero debilita la inferencia, la trazabilidad o el control de versiones. |
| Baja | Problema terminológico, comparativo o de presentación que puede inducir lecturas equívocas. |
| Oportunidad | Reorganización que reduce duplicidad y mejora la futura versión canónica sin corregir un error factual. |

## 2. Corpus y método de contraste

Se han contrastado, contra la Edición Crítica v3.5:

1. `Estudio_Historico.md`, v0.1;
2. `Analisis_Cuantitativo.md`, v0.2;
3. `Reconstruccion_Economica_Integrada.md`, v0.3;
4. `Matriz_Contabilidad_Social_y_Grafo_Economico.md`, v0.4;
5. `Mapa_Vulnerabilidades_Economicas.md`, v0.5;
6. `Sintesis_Socioeconomica_Integral.md`, v0.6;
7. los seis registros de operación correspondientes.

El contraste se realizó en cinco planos:

- correspondencia de cada dato con la unidad y respuesta de la Edición Crítica;
- recomputación independiente de los cálculos principales;
- comparación transversal de cifras y terminología entre 0.1–0.6;
- revisión de la frontera entre dato documental, cálculo e interpretación;
- comprobación de controles, secuencia de commits, ausencia de PDF y CI.

## 3. Hallazgos de severidad alta

### A-01 — Uso común convertido repetidamente en propiedad o administración comunal

**Ámbito:** v0.3, v0.4, v0.5 y v0.6.  
**Tipo:** inferencia jurídica e institucional demasiado fuerte.

**Evidencia derivada:**

- v0.3 denomina el conjunto `bienes comunales`, lo trata como `capital económico` y afirma que el común administra o utiliza esos recursos (líneas 15, 49, 61, 178, 345, 637, 676 y 682);
- v0.4 crea la cuenta `COMR — Recursos comunales` y la conecta con hogares y producción (líneas 60, 129, 260 y 410);
- v0.5 habla de `madera comunal`, bienes comunales y del común como sostén de ganadería e infraestructura (líneas 112, 215–240, 490, 498, 555–581, 674 y 731);
- v0.6 consolida `bienes comunales como infraestructura económica` y presenta su organización colectiva como dato en algunos pasajes (líneas 55, 227–242, 381, 422, 578 y 597).

**Evidencia de autoridad:** la Edición Crítica declara que eras o sitios sirven de pasto a los `ganados de el Comun` y de resguardo del cereal; montes y soto sirven de pasto, leña y reparación de puentes o puertas del río (folios 308r–308v; edición, líneas 378–384 y 425–429). La respuesta 12 vuelve a negar utilidad particular porque sirven al pasto de los ganados del común (folio 312r; edición, líneas 843–848). Estos pasajes documentan funciones y aprovechamiento común; no declaran por sí solos título de propiedad, titularidad del común ni régimen de administración.

**Diagnóstico:** se ha producido un desplazamiento desde `uso común documentado` a `bienes propiedad/administración del común`. La interpretación económica de su función es sólida; la calificación jurídica no lo es.

**Resolución propuesta:** usar en la versión canónica `espacios y aprovechamientos de uso común documentado` o `recursos de aprovechamiento común`. Reservar `bien comunal`, `propiedad comunal`, `administrado por el común` y `madera comunal` para los casos en que una fuente declare expresamente titularidad o gestión. En grafos, sustituir `COMR` por `AUC — Aprovechamientos de uso común` y marcar sus aristas como `D+I`.

### A-02 — Conflación entre el común del lugar y el Concejo de Ordás

**Ámbito:** v0.3, v0.4 y v0.6; afecta también a algunos circuitos de v0.5.  
**Tipo:** cambio de escala institucional.

**Evidencia derivada:**

- v0.3 agrupa `Común / concejo` en una misma cuenta (línea 61);
- v0.4 define `COM | Común / concejo` (línea 44) y mantiene esa identidad en matriz y grafo;
- v0.6 afirma que `el concejo` administra necesidades colectivas sin propios, arbitrios ni rentas (línea 578).

**Evidencia de autoridad:** la edición distingue el `Concejo de Ordas`, descrito como circunscripción histórica, del `este comun` al que las respuestas 23–27 atribuyen ausencia de propios, arbitrio, renta, cargo de justicia y servicio ordinario o extraordinario (edición, líneas 150, 1637–1647 y 1702–1707). El expediente no autoriza a tratar automáticamente ambos términos como la misma persona institucional.

**Diagnóstico:** al fusionarlos, el estudio puede desplazar al Concejo de Ordás —escala jurisdiccional— obligaciones y recursos que el tenor atribuye al común del lugar.

**Resolución propuesta:** mantener dos nodos distintos: `COM — común del lugar` y `CONC — Concejo de Ordás`. Solo crear aristas entre ellos cuando el expediente las documente. En la narrativa, atribuir las respuestas 23–27 al `común del lugar` y reservar `Concejo de Ordás` para el encuadre territorial, el nombramiento de peritos y las menciones expresas.

## 4. Hallazgos de severidad media

### M-01 — Contradicción metodológica interna en v0.1 sobre quartal, fanega y celemín

**Evidencia:** v0.1 afirma que el expediente `no establece una relación interna entre celemín, quartal y fanega` (línea 88). La misma versión y la Edición Crítica registran, sin embargo, que cuatro quartales componen una fanega; la edición lo declara expresamente en folio 310v (líneas 666–673 y 688–690).

**Alcance:** el cálculo posterior no resulta dañado: v0.2–v0.6 emplean correctamente `4 quartales = 1 fanega` y solo niegan la equivalencia entre el celemín y la medida principal.

**Resolución propuesta:** sustituir la frase por: `El expediente establece 4 quartales = 1 fanega, pero no declara una equivalencia entre el celemín y la medida principal usada en el desglose de la respuesta 10`.

### M-02 — La relación río–puentes–molienda se presenta como cadena causal observada

**Evidencia derivada:** v0.5 titula `Cadena causal observada` y formula `río / crecida → daño o pérdida de puentes → interrupción / reducción de servicio → menor capacidad molinera` (líneas 257–260); el escenario hidráulico repite esa secuencia (líneas 473–490).

**Evidencia de autoridad:** la respuesta 17 regula dos cargas a las tres ruedas de la primera casa `a causa De llevar el rio los Puentes, y moler solo la mitad De el año` (folio 316r; edición, líneas 1327–1330 y nota editorial 1348). El tenor liga ambas circunstancias a la regulación, pero no demuestra que la pérdida de puentes sea la causa mecánica de la reducción del tiempo de molienda.

**Diagnóstico:** el riesgo hidráulico es directo y sólido; el eslabón `puente dañado → molino parado` es una lectura posible, no un dato observado.

**Resolución propuesta:** formular dos hechos paralelos —`el río arrastra puentes` y `las tres ruedas muelen medio año`— y una inferencia separada: `ambos hechos revelan una dependencia hidráulica e infraestructural común`. Reservar la cadena causal fuerte para una futura fuente que documente la conexión operacional.

### M-03 — Incorporación de nodos o funciones no documentados como si pertenecieran al modelo interno

**Evidencia:**

- el grafo de v0.5 introduce `Condiciones agro-hidrológicas → tierra / río` (líneas 66–67), aunque el corpus no identifica clima ni una causa común concreta;
- v0.5 afirma que `el cereal necesita molienda para usos alimentarios ordinarios` (línea 286);
- v0.3 concluye con `autoconsumo presumible` (línea 684);
- v0.6 representa `cereal → molienda → harina / servicio de molienda` (línea 254), correctamente marcado como interpretación, pero sin una cita específica.

**Diagnóstico:** son inferencias históricamente plausibles, pero no deben aparecer en un análisis de corpus exclusivo con el mismo estatuto visual que los datos declarados.

**Resolución propuesta:** eliminar el nodo climático del grafo interno o dibujarlo con línea discontinua y etiqueta `hipótesis externa no documentada`; sustituir la necesidad alimentaria por `los molinos harineros documentan transformación local de cereal`; marcar el autoconsumo como posibilidad no cuantificada, no como componente presumido del modelo.

### M-04 — Etiquetado `D/C/I` demasiado grueso en flujos y afirmaciones modelizadas

**Evidencia:** en v0.4, F18 presenta `COMR → HOG / ganado / AGR` como `D`, y F19 presenta `TRA / hogares → AGR` como `D` (líneas 91–92), aunque origen, destino y agregación son construcciones del modelo. En v0.6, la organización colectiva del mantenimiento mediante `madera comunal` aparece como `[D]` (línea 381), cuando la función de la leña está documentada pero la titularidad y el mecanismo organizativo son interpretaciones.

**Diagnóstico:** el contenido elemental puede ser documental, pero el empaquetado en cuentas, sectores, actores agregados o causalidad ya es interpretación.

**Resolución propuesta:** etiquetar por componente: `dato de base: D; agregación de actor/cuenta: I; suma: C`. En tablas de flujos usar una columna para `estatus del dato` y otra para `estatus de la relación modelizada`.

### M-05 — Pérdida progresiva de trazabilidad directa en las capas 0.3–0.6

**Evidencia:** v0.1 remite con frecuencia a folios; v0.2 crea la matriz respuesta–folio; v0.4 recupera trazabilidad mediante F01–F27; v0.5 desarrolla numerosas relaciones y escenarios sin repetir respuesta/folio; v0.6 combina citas directas, etiquetas `[D/C/I]` y afirmaciones que dependen de capas anteriores.

**Diagnóstico:** una afirmación puede seguir siendo correcta, pero para auditarla hay que recorrer varias capas. Esto incumple de forma débil el objetivo del Manual de que las afirmaciones puedan remitirse a unidades de la edición.

**Resolución propuesta:** crear en la futura versión canónica un `Registro de afirmaciones` con identificadores estables, por ejemplo `AF-AGR-001`, y campos `texto canónico`, `D/C/I`, `respuesta`, `folio`, `líneas o unidad`, `cálculo`, `versiones de origen` y `estado`. Reutilizar esos IDs en cuerpo, tablas y grafos.

### M-06 — Las designaciones 0.1–0.6 mezclan revisiones y anexos distintos

**Evidencia:** `Estudio_Historico.md` permanece en v0.1, mientras v0.2–v0.6 son archivos independientes y acumulativos. La expresión `versiones 0.1–0.6` sugiere una sucesión del mismo documento, pero en realidad combina una síntesis inicial, tres anexos analíticos, un mapa temático y una nueva síntesis.

**Riesgo:** dificulta determinar qué texto es canónico, qué capa sustituye a otra y qué elementos deben mantenerse como anexos.

**Resolución propuesta:** reservar la versión para el documento canónico (`Estudio_Historico.md` v1.0) y convertir las capas en anexos con identidad propia: `Anexo cuantitativo`, `Modelo económico`, `MCSH y grafo`, `Mapa de vulnerabilidades` y `Auditoría 0.1–0.6`. Registrar para cada uno si está vigente, incorporado, supersedido o archivado.

### M-07 — Excepciones al protocolo atómico y cierre técnico insuficientemente visible en los registros

**Evidencia:** el registro de v0.4 declara expresamente que documento y operación se publicaron en dos commits secuenciales; el historial confirma `dd8ea930…` y `a612df60…`. v0.1 y v0.5 también requirieron commits de corrección posteriores (`a88577c0…` y `4cec9c41…`). Los registros conservan `Estado: prepared` y, por diseño, no incorporan el SHA final ni el resultado efectivo de CI.

**Diagnóstico:** el historial permite reconstruir lo ocurrido, pero el registro semántico no cierra por sí solo la operación. El caso v0.4 contradice el protocolo actual de commit multiarchivo atómico.

**Resolución propuesta:** para futuras operaciones, publicar entregable y registro en un único commit; añadir en un bloque final inmutable o en un registro de verificación separado el `publication_sha`, padre, archivos, blobs críticos y CI. No reescribir retroactivamente los registros históricos: documentar la excepción en esta auditoría.

## 5. Hallazgos de severidad baja

### B-01 — `Ruedas fijas` es una etiqueta analítica no documental

Se usa desde v0.2 para distinguir las ocho ruedas de las cuatro casas del molino venturero. Puede entenderse erróneamente como descripción constructiva u operativa. Usar `ocho ruedas descritas en las cuatro casas` y mantener aparte `molino venturero, número de ruedas no declarado`.

### B-02 — `Boto` y `voto` alternan sin regla explícita

v0.1 usa `boto` en los datos y `voto` en la síntesis (líneas 110–112 y 206); las capas posteriores conservan `boto`. Adoptar `boto` para la forma documental y, si se normaliza, `voto de Santiago` con nota terminológica.

### B-03 — El nombre del cura alterna entre Bega, Vega y Bega/Vega

La variación procede del expediente y está correctamente reconocida desde v0.2, pero debe fijarse una forma de cita estable: `Manuel Antonio de Bega (var. Vega)` o la forma canónica que establezca el índice de personas.

### B-04 — Léxico comparativo sin referente aprobado

Expresiones como `pequeña comunidad`, `baja especialización`, `rico en funciones` o `mayor titular` son comprensibles, pero solo la última puede apoyarse en un universo interno definido. Mantenerlas como interpretación y evitar que sugieran comparación regional no realizada.

### B-05 — El índice anualizado de tierra activa es correcto pero muy dependiente de su supuesto

El cálculo `2.750,5 / 2 + 34 + 149,5 + 19,5 = 1.578,25`, con 87,14% centenal, es aritméticamente correcto. No representa superficie anual observada ni prueba escalonamiento real del barbecho. Debe permanecer en el anexo cuantitativo, con una etiqueta visible de `índice contrafactual/analítico`, y no funcionar como cifra descriptiva principal.

### B-06 — `Redundancia operativa` y efecto amortiguador de la copropiedad exceden la evidencia

Varias ruedas y titulares documentan pluralidad de activos y derechos. No se conocen capacidad, sustituibilidad efectiva, acceso de usuarios ni reglas de copropiedad. La versión canónica debe hablar de `redundancia potencial de unidades` y `dispersión patrimonial`, no de amortiguación operativa demostrada.

## 6. Auditoría de cifras y relaciones

### 6.1. Cálculos recomputados sin discrepancias

| Magnitud | Resultado auditado | Estado | Restricción interpretativa |
|---|---:|---|---|
| Suma de partidas principales de R10 | 3.811,5 | coherente | no equivale a superficie moderna |
| Celemínes adicionales explícitos | 7 | coherente | no se agregan a la unidad principal |
| Total declarado | 3.823 + 1 celemín | coherente con la transcripción | no se reconcilia por residuo |
| Primera / segunda / tercera calidad | 666 / 1.398 / 1.747,5 | coherente | omite montes y conserva discordancias |
| Porcentajes por calidad | 17,47% / 36,68% / 45,85% | coherente | denominador: 3.811,5 |
| Subtotal cultivado comparable | 2.953,5 | coherente | cuatro clases cultivadas explícitas |
| Centenales | 2.750,5 | coherente | unidad principal local |
| Centenales / cultivo comparable | 93,13% | coherente | no es porcentaje del territorio físico |
| Centenales / subtotal total explícito | 72,16% | coherente | incluye usos no cultivados en el denominador |
| Índice anualizado activo | 1.578,25 | aritméticamente coherente | supuesto analítico bienal |
| Peso centenal en ese índice | 87,14% | aritméticamente coherente | no observado directamente |
| Abejas | 18 = 7+6+3+1+1 | coherente | activo declarado, no riqueza total |
| Utilidad apícola | 36 reales | coherente | 18 × 2 |
| Concentración apícola | 72,2% | coherente | 13/18 en dos titulares |
| Ruedas en cuatro casas | 8 = 3+2+2+1 | coherente | ruedas del venturero no declaradas |
| Utilidad de esas ruedas | 26 cargas | coherente | 3×2 + 5×4 |
| Gastos comunes explícitos | 233 reales | coherente | 200+8+15+10; faltan otras cantidades |
| Mínimo monetario institucional | 1.006 reales | coherente | 633+233+140; no es presión fiscal total |
| Destino exterior explícito del gasto común | 25 reales; 10,73% | coherente | 15+10 sobre 233 |
| Suelo exterior sobre 1.006 | 2,49% | coherente | no clasifica Conde ni boto |
| Jornaleros | 18 = 14+3+1 | coherente | no sumar a vecinos/labradores |
| Diezmo de lino | 160 libras | coherente | 40 haces × 4 libras |

### 6.2. Discordancias que pertenecen a la fuente y están bien conservadas

Las seis capas mantienen correctamente, sin corregirlas por conjetura:

- prados cercados de secano: R5 declara primera y segunda calidad; R10 solo segunda, llamada única;
- montes: R5 declara primera y tercera calidad; R10 no cuantifica;
- sotos: R5 declara primera y tercera calidad; R10 solo tercera, llamada única;
- cabida total: total declarado y suma de partidas no se reconcilian sin equivalencia celemín–unidad principal;
- simiente de linaza de regadío: R9 no individualiza de forma inequívoca todas las calidades;
- boto: se conservan 24 quartales sin imponer el producto elidido;
- cargas de cereal: no se convierten a quartales o fanegas;
- reales y maravedís: no se homogeneizan mediante una equivalencia externa.

## 7. Matriz de compatibilidad entre capas

| Tema | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | Diagnóstico |
|---|---|---|---|---|---|---|---|
| Autoridad v3.5 | explícita | explícita | explícita | explícita | explícita | explícita | compatible |
| Cabida y calidades | prudente, con M-01 | completa | reutiliza | satélite | reutiliza | consolida | cifras compatibles |
| Demografía | cautela | matriz completa | integrada | hogares modelizados | exposición | consolidada | compatible; evitar hogar=vecino |
| Común y Concejo | separados de forma más prudente | datos separados | fusionados | fusionados | mezcla funcional | fusionados en pasajes | corregir A-02 |
| Aprovechamientos comunes | funciones | funciones | propiedad/gestión sugerida | cuenta comunal | nodo comunal | bien comunal consolidado | corregir A-01 |
| Hidráulica | irregularidad | datos y utilidad | riesgo | grafo funcional | cadena causal fuerte | síntesis moderada | corregir M-02 |
| Monetización | lectura general | 1.006 | circuitos | matriz | vulnerabilidad | síntesis | compatible con cautelas |
| D/C/I | narrativo | reglas | explícito | mixto por flujo | categorías cualitativas | etiquetas visibles | mejorar M-04 |
| Trazabilidad directa | folios | respuesta+folio | parcial | IDs+folios | débil | desigual | corregir M-05 |

## 8. Duplicidades y propuesta de consolidación

### 8.1. Duplicidades principales

La mayor repetición se concentra en seis núcleos:

1. descripción del predominio centenal y del barbecho en v0.1, v0.3, v0.5 y v0.6;
2. común sin propios/arbitrios/renta y gasto de 233 reales en todas las capas desde v0.1;
3. red molinera y riesgo hidráulico en v0.1–v0.6;
4. estructura de jornaleros, labradores y hogar en v0.1–v0.6;
5. mínimo monetario de 1.006 reales en v0.2–v0.6;
6. límites sobre población, renta, producto, mercado y desigualdad en v0.1–v0.6.

La repetición ha servido como control, pero mantenerla en una obra canónica multiplicaría el riesgo de divergencia futura.

### 8.2. Función recomendada de cada capa

| Capa | Disposición futura | Contenido que debe conservarse |
|---|---|---|
| v0.1 | supersedida como narrativa, conservada como hito | primera organización temática y cautelas básicas |
| v0.2 | anexo cuantitativo canónico | matriz R1–R40, tablas, aritmética y discordancias |
| v0.3 | fuente de redacción, no anexo independiente necesario | modelo económico y separación dinero/especie |
| v0.4 | anexo formal canónico revisado | F01–F27, MCSH y grafos, corrigiendo A-01/A-02/M-04 |
| v0.5 | anexo temático canónico revisado | vulnerabilidades, con causalidad y nodos rebajados |
| v0.6 | base narrativa de la futura versión canónica | tesis integrada, estructura social, límites y conclusión |
| auditoría | anexo de control | hallazgos, decisiones y registro de resolución |

### 8.3. Arquitectura propuesta para `Estudio_Historico.md` canónico

1. **Metadatos, autoridad y método.** Edición v3.5, commit, blob, reglas `D/C/I` y límites.
2. **Tesis de conjunto.** Versión depurada de v0.6.
3. **Comunidad, jurisdicción y categorías sociales.** Separar lugar, común y Concejo de Ordás.
4. **Territorio y sistema productivo.** Síntesis narrativa; tablas extensas al anexo cuantitativo.
5. **Trabajo, activos y relaciones institucionales.** Evitar hogar=vecino como identidad automática.
6. **Dinero, especie y servicios.** Mantener 1.006 como mínimo de flujos, no fiscalidad total.
7. **Vulnerabilidad y resiliencia.** Solo dependencias apoyadas; escenarios claramente contrafactuales.
8. **Límites de conocimiento.** Población, renta, producto, desigualdad, consumo y comercio.
9. **Conclusión.** Una sola formulación canónica.
10. **Anexo A: registro de afirmaciones y fuentes.** IDs, R#, folio, unidad, `D/C/I`.
11. **Anexo B: cálculos.** Fórmulas, denominadores, supuestos y redondeo.
12. **Anexo C: MCSH, grafos y vulnerabilidades.** Versiones revisadas.

## 9. Terminología canónica recomendada

| Concepto actual | Forma recomendada | Motivo |
|---|---|---|
| `Común / concejo` | `común del lugar` / `Concejo de Ordás` | no fusionar escalas institucionales |
| `bienes comunales` | `espacios o recursos de aprovechamiento común documentado` | no atribuir propiedad sin título |
| `madera comunal` | `leña o madera de montes/soto destinada a puentes y puertas` | conservar función, no titularidad |
| `ruedas fijas` | `ocho ruedas descritas en cuatro casas` | evitar categoría no documental |
| `redundancia operativa` | `pluralidad de unidades; redundancia potencial` | capacidad sustitutiva no demostrada |
| `boto` / `voto` | `boto` documental; `voto de Santiago` solo con nota | coherencia terminológica |
| `Bega/Vega` | `Bega (var. Vega)` o forma del índice | identidad estable con variante |
| `medidas` | `medidas principales explicitadas en R10` | recordar que no son superficie moderna |
| `salida exterior` | `destino geográfico exterior inequívoco` | no inferir residencia final |
| `presión fiscal` | `mínimo de flujos institucionales monetarios` | evitar denominador de renta inexistente |

## 10. Plan de resolución para la futura versión canónica

### Prioridad 1 — antes de redactar

1. aprobar la separación `común del lugar` / `Concejo de Ordás`;
2. sustituir el vocabulario de propiedad comunal por aprovechamiento común documentado;
3. crear el registro de afirmaciones y cálculos;
4. fijar terminología de personas, cargas y unidades.

### Prioridad 2 — durante la redacción

1. usar v0.6 como esqueleto, no copiar simultáneamente v0.1 y v0.3;
2. insertar referencias a R#, folio y claim ID en cada párrafo factual;
3. mover tablas largas y cálculos condicionales a anexos;
4. revisar los grafos para distinguir dato, cálculo, interpretación e hipótesis;
5. conservar las incertidumbres documentales sin resolverlas por conjetura.

### Prioridad 3 — antes de publicar

1. ejecutar una tabla de concordancia automática de cifras repetidas;
2. comprobar que cada afirmación `[D]` tenga referencia directa a la edición;
3. comprobar que cada `[C]` tenga fórmula y denominador;
4. comprobar que cada `[I]` no se presente como hecho ocurrido;
5. publicar documento, anexos y registro en un único commit atómico;
6. verificar padre, archivos, blobs, controles, ausencia de PDF y CI.

## 11. Estado del proyecto en la base auditada

En `main@7d50e87645b0ae483d3557b1c68267eaab23daff` se comprobó:

- `schema_version: 2` en `proyecto.yaml`;
- rama canónica `main` y repositorio `miguel-conde/sorrios-ensenada`;
- fase `estudio_historico` con `historical_study_enabled: true`;
- Edición Crítica declarada como v3.5;
- 35 unidades en `unidades.yaml`;
- última unidad validada y cerrada: `hoja_enfrentada_posterior`;
- `current_unit`, `next_unit` y `current_location`: `null`;
- `open_issues: []` y `pending_tasks: []`;
- `operation.status: clean`;
- seis documentos 0.1–0.6 y sus registros de operación presentes;
- ningún PDF versionado en el árbol;
- workflow `Portable Python tests`, ejecución 156 sobre la base auditada: `completed/success`.

## 12. Dictamen

La serie 0.1–0.6 constituye una base suficiente para una versión canónica, pero no debe fusionarse de forma mecánica. La aritmética y la mayor parte de la lectura factual son estables. La intervención necesaria es principalmente epistemológica y editorial: separar uso de propiedad, distinguir común y Concejo, rebajar ciertas cadenas causales, normalizar el estatuto `D/C/I` y restaurar trazabilidad directa.

No se recomienda corregir ahora `Estudio_Historico.md` mediante cambios parciales. La resolución más segura es preparar una versión canónica integral, basada narrativamente en v0.6 y apoyada por anexos depurados de v0.2, v0.4 y v0.5, con esta auditoría como lista de control de aceptación.


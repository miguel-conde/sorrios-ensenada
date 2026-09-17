# Registro de afirmaciones y cálculos para la versión canónica

## Sorribas y Santibáñez de Ordás en 1752

**Versión:** 1.0  
**Fecha:** 17 de septiembre de 2026  
**Naturaleza:** instrumento de control previo; no sustituye al `Estudio_Historico.md` canónico  
**Base documental exclusiva:** `Edicion_Critica_v3_5.md`  
**Revisión de base:** `main@e3c103664ea58a20051024a428456dfc29de401a`  
**Control previo:** `Auditoria_Coherencia_0_1_0_6.md`  

## 1. Función del registro

Este documento fija un vocabulario controlado de afirmaciones admisibles para una futura versión canónica del estudio. Cada afirmación lleva un identificador estable, un nivel epistemológico y una localización en la Edición Crítica. Los análisis 0.1–0.6 sirven para localizar problemas y formular preguntas, pero no tienen autoridad documental propia.

Niveles:

- **D — dato:** declaración o cifra presente en el expediente.
- **C — cálculo:** operación reproducible cuyos operandos proceden de datos registrados.
- **I — interpretación:** lectura histórica compatible con los datos, formulada con cautela y sin convertirse en hecho documental.
- **L — límite:** ausencia, discrepancia o imposibilidad de cálculo que debe conservarse.

Estados:

- **Admitida:** puede incorporarse a la versión canónica con la formulación indicada.
- **Condicionada:** exige mantener la salvedad especificada.
- **Excluida:** no debe incorporarse como afirmación histórica en el corpus vigente.

## 2. Decisiones terminológicas vinculantes

1. Se distinguirán siempre el **común del lugar**, los **vecinos** y el **Concejo de Ordás**. No se tratarán como una sola entidad.
2. Se usará **espacios o aprovechamientos de uso común documentado**. Las expresiones «bienes comunales», «propiedad comunal» o «administración comunal» solo podrán emplearse si una fuente acredita el título o la gestión.
3. Se conservará **boto** al referirse al término documental. La identificación contextual con el Voto de Santiago irá en nota y no alterará el receptor declarado: la fábrica del Apóstol Santiago.
4. Para el cura se usará **Manuel Antonio de Bega (var. Vega)**, conforme a las variantes documentales registradas.
5. Se hablará de **ocho ruedas descritas en cuatro casas de molinos**. El número de ruedas del molino venturero no está declarado.
6. «Redundancia», «centralidad», «dependencia» y «vulnerabilidad» son categorías analíticas; nunca sustituyen la descripción documental.

## 3. Registro de afirmaciones documentales

### 3.1. Localidad, jurisdicción y producción del expediente

| ID | Afirmación canónica | Nivel | Evidencia | Estado y cautela |
|---|---|---:|---|---|
| JUR-001 | El expediente se refiere al lugar de Sorribas y Santibáñez de Ordás. | D | Portada; `portada` | Admitida. |
| JUR-002 | Los declarantes comparecen en el marco del Concejo de Ordás. | D | Preámbulo, ff. 306r–306v; `folio_306r`, `folio_306v` | Admitida; no equiparar sin más con el municipio contemporáneo. |
| JUR-003 | Juan Álvarez y Remirio Rodríguez son vecinos y únicos oficiales de justicia. | D | Preámbulo, ff. 306r–306v | Admitida. |
| JUR-004 | Domingo Díez y Francisco de Llorca fueron nombrados peritos por el Concejo; Domingo Suárez, de oficio. | D | Preámbulo, f. 306v | Admitida. |
| JUR-005 | El lugar es de señorío, pero no paga cosa alguna al señor en el concepto declarado en la respuesta 22. | D | R22, ff. 318r–318v | Condicionada: no generalizar a ausencia de derechos señoriales; R28 y R29 documentan derechos del conde de Luna. |
| JUR-006 | Las alcabalas están enajenadas a favor del conde de Luna y los vecinos pagan por ellas 633 reales anuales. | D | R28, ff. 319r–319v | Admitida. |

### 3.2. Territorio, medidas y usos agrarios

| ID | Afirmación canónica | Nivel | Evidencia | Estado y cautela |
|---|---|---:|---|---|
| TER-001 | El expediente distingue trece clases de tierras y aprovechamientos. | D | R4, ff. 307v–308v | Admitida; enumerar según la Edición Crítica. |
| TER-002 | Las calidades se distribuyen de manera distinta según la clase de tierra o prado. | D | R5, ff. 308v–309r | Admitida. |
| TER-003 | No se usa una medida superficial cierta reducible a varas castellanas. | D | R9, f. 309v | Admitida. |
| TER-004 | Las tierras de pan llevar y los prados de guadaña se estiman mediante quartales de sembradura; otras clases quedan al juicio de peritos. | D | R9, f. 309v | Admitida. |
| TER-005 | La relación interna expresamente documentada es cuatro quartales por fanega. | D | R9, ff. 309v–310r | Admitida; no existe equivalencia documental entre el celemín usado en R10 y el quartal/fanega de R9. |
| TER-006 | La suma declarada de cabida es 3.823 medidas y un celemín. | D | R10, ff. 310v–312r | Admitida como total escrito. |
| TER-007 | La suma aritmética de las partidas transcritas de R10 es 3.811,5 medidas, más siete celemines no convertibles con la información conservada. | C | R10, ff. 310v–312r; CAL-001 | Admitida; no reconciliar artificialmente con TER-006. |
| TER-008 | La primera calidad suma 666 medidas; la segunda, 1.398; y la tercera, 1.747,5, dentro de las partidas expresadas en la unidad principal. | C | R10; CAL-002 | Condicionada por los siete celemines separados. |
| TER-009 | R5 y R10 no coinciden plenamente en la presencia o calidad de algunos prados, montes y sotos. | L | R5, ff. 308v–309r; R10, ff. 310v–312r | Admitida como discrepancia de fuente; no corregir una respuesta con otra. |
| TER-010 | La duodécima respuesta proporciona rendimientos normativos por clase y calidad, no una cosecha anual observada. | D | R12, ff. 312r–314r | Admitida; usar «regula» o «declara rendimiento», no «produjo». |

### 3.3. Agricultura, lino y prados

| ID | Afirmación canónica | Nivel | Evidencia | Estado y cautela |
|---|---|---:|---|---|
| AGR-001 | El centeno, la cebada, el lino, la linaza y la yerba son las especies de frutos declaradas. | D | R11, f. 312r | Admitida. |
| AGR-002 | Las tierras centenales producen un año y descansan otro. | D | R4 y R12, ff. 307v–308r y 313r–313v | Admitida. |
| AGR-003 | Algunas tierras linares alternan lino con cebada o con centeno. | D | R4 y R12, ff. 307v–308r y 312v–313r | Admitida. |
| AGR-004 | La cabida cultivada comparable suma 2.953,5 medidas y las tierras centenales 2.750,5. | C | R10; CAL-003 y CAL-004 | Admitida, definiendo qué categorías entran en «cultivada comparable». |
| AGR-005 | Las tierras centenales representan el 93,13 % de esa cabida cultivada comparable y el 72,16 % del total explícito de 3.811,5 medidas. | C | R10; CAL-005 y CAL-006 | Admitida; nunca presentar ambos porcentajes como si tuvieran el mismo denominador. |
| AGR-006 | Un índice analítico de superficie activa anual da 1.578,25 medidas y un peso centenal del 87,14 %. | C | R4, R10; CAL-007 y CAL-008 | Condicionada: es un escenario mecánico que aplica los ciclos declarados; no es superficie efectivamente sembrada en un año concreto. |
| AGR-007 | Los rendimientos centenales regulados son 4, 3 y 2,5 quartales por quartal sembrado según primera, segunda y tercera calidad. | D | R12, f. 313v | Admitida. |
| AGR-008 | Los rendimientos del lino y de la linaza varían por regadío/secano y calidad. | D | R12, ff. 312v–313r | Admitida; no homogeneizar las series. |
| AGR-009 | Los cuarenta fejes de lino de cuatro libras equivalen a 160 libras en la regulación de los diezmos. | C | R16, f. 315r; CAL-009 | Admitida como conversión interna de esa partida. |
| AGR-010 | Cuatro montones de yerba componen un carro. | D | R12, f. 314r | Admitida; no convertir otros productos con esta relación. |

### 3.4. Ganadería, aprovechamientos comunes y apicultura

| ID | Afirmación canónica | Nivel | Evidencia | Estado y cautela |
|---|---|---:|---|---|
| GAN-001 | El expediente regula utilidades para distintas especies y usos ganaderos en la respuesta 20. | D | R20, ff. 316v–318r | Admitida; mantener especies y conceptos separados. |
| GAN-002 | Matorrales, eras, sitios, montes y soto no reciben utilidad en R12 porque sirven para pasto de los ganados del común. | D | R12, f. 314r | Admitida; acredita uso común, no título de propiedad. |
| GAN-003 | Se documentan dieciocho pies de abejas distribuidos entre cinco titulares. | D | R19, f. 316v | Admitida. |
| GAN-004 | La distribución declarada de colmenas es 7, 6, 3, 1 y 1. | D | R19, f. 316v | Admitida. |
| GAN-005 | A dos reales por pie, la utilidad anual total de las colmenas es 36 reales. | C | R19; CAL-010 | Admitida. |
| GAN-006 | Los dos mayores titulares concentran 13 de 18 colmenas, el 72,22 %. | C | R19; CAL-011 | Admitida como concentración de este activo, no como medida general de desigualdad. |
| GAN-007 | No hay casa destinada al esquileo; cada uno esquila su ganado en su habitación. | D | R18, f. 316r | Admitida. |

### 3.5. Río y molinos

| ID | Afirmación canónica | Nivel | Evidencia | Estado y cautela |
|---|---|---:|---|---|
| HID-001 | Se describen cuatro casas de molinos harineros movidas por el agua del río. | D | R17, ff. 315r–316r | Admitida. |
| HID-002 | Esas cuatro casas reúnen ocho ruedas descritas: 3 + 2 + 2 + 1. | C | R17; CAL-012 | Admitida. |
| HID-003 | La propiedad o participación en las ruedas se distribuye entre varios titulares y consortes. | D | R17, ff. 315r–316r | Admitida; no convertir automáticamente pluralidad de titulares en copropiedad de cada casa. |
| HID-004 | Las utilidades reguladas de las ocho ruedas suman 26 cargas de centeno. | C | R17; CAL-013 | Admitida; no convertir cargas a fanegas o quartales sin equivalencia documental. |
| HID-005 | Existe además un molino venturero que solo muele algunos meses de invierno y recibe una utilidad de cuatro quartales de centeno. | D | R17, ff. 315v–316r | Admitida; su número de ruedas no consta. |
| HID-006 | El expediente atribuye la regulación reducida de determinadas ruedas a que el río lleva los puentes y a que muelen solo la mitad del año. | D | R17, f. 316r | Admitida como coexistencia causal declarada en la respuesta. |
| HID-007 | El río constituye un factor físico compartido por los molinos descritos. | I | R17, ff. 315r–316r | Condicionada: interpretación directa; no afirmar que la pérdida de puentes paraliza necesariamente todos los molinos. |

### 3.6. Población, vivienda, trabajo y servicios

| ID | Afirmación canónica | Nivel | Evidencia | Estado y cautela |
|---|---|---:|---|---|
| DEM-001 | Se declaran 18 vecinos, 8 medios vecinos —incluidas dos viudas— y 8 residentes no considerados vecinos. | D | R21, f. 318r | Admitida. |
| DEM-002 | El expediente suma los vecinos y medios vecinos como 26 habitantes fiscales. | D | R21, f. 318r | Admitida; no equivale a población total. |
| DEM-003 | Se declaran 40 casas habitables, 2 arruinadas y 15 pajares separados. | D | R22, ff. 318r–318v | Admitida. |
| DEM-004 | No hay casa de campo ni alquería. | D | R21, f. 318r | Admitida. |
| TRA-001 | Se declaran 18 jornaleros: 14 hijos de familia, 3 criados sirvientes y 1 dedicado solo a ese ejercicio. | D | R35, ff. 320r–320v | Admitida. |
| TRA-002 | Se declaran 24 labradores. | D | R35, f. 320v | Admitida; no suponer exclusión mutua con otras categorías sin evidencia. |
| TRA-003 | A los jornaleros se les regulan 2,5 reales por día trabajado y a los labradores 3, incluida comida valorada en 1,5 reales. | D | R35, f. 320v | Admitida como regulación, no como ingreso anual. |
| TRA-004 | Hay un herrero que dedica la mayor parte del año a labrador y recibe una regulación adicional de medio real diario por el oficio. | D | R33, f. 320r | Admitida como evidencia explícita de pluriactividad individual. |
| TRA-005 | La taberna funciona por vecera entre los vecinos y no produce utilidad al común ni a particular. | D | R29, f. 319v | Admitida. |

### 3.7. Derechos, hacienda común y conexiones externas

| ID | Afirmación canónica | Nivel | Evidencia | Estado y cautela |
|---|---|---:|---|---|
| FIS-001 | Sobre las tierras se declaran diezmos, primicia y boto. | D | R15, f. 314v | Admitida. |
| FIS-002 | Los diezmos corresponden al cura Manuel Antonio de Bega (var. Vega), la primicia a la iglesia del lugar y el boto a la fábrica del Apóstol Santiago. | D | R15, f. 314v | Admitida con normalización onomástica explícita. |
| FIS-003 | R16 regula los diezmos en 30 cargas de centeno, 2 de cebada, 5 fanegas de trigo sembrado fuera del término, 40 fejes de lino de 4 libras y 140 reales de diezmos menudos. | D | R16, f. 315r | Admitida; unidades heterogéneas, no sumables sin precios o equivalencias adicionales. |
| FIS-004 | La primicia se expresa en 26 quartales de centeno y el boto en 24 quartales. | D | R16, f. 315r | Admitida. |
| FIS-005 | El común no tiene propios, arbitrios ni renta alguna. | D | R23–R24, f. 318v | Admitida. |
| FIS-006 | El común debe satisfacer 200 reales anuales y además 8 para fuentes, 15 al hospital de Inocentes de Valladolid y 10 por derecho de Mesta en León, junto con otras cantidades no cuantificadas. | D | R25, ff. 318v–319r | Admitida; no presentar 233 reales como total exhaustivo. |
| FIS-007 | Al carecer de propios para esas cantidades, se pagan por repartimiento entre los vecinos. | D | R25, f. 319r | Admitida. |
| FIS-008 | El común no tiene cargo de justicia ni está cargado de servicio ordinario o extraordinario. | D | R26–R27, f. 319r | Admitida. |
| FIS-009 | Las cargas monetarias institucionales explícitamente cuantificadas suman como mínimo 1.006 reales: 633 + 233 + 140. | C | R16, R25, R28; CAL-014 | Condicionada: mínimo parcial, no presión fiscal total ni balance del común. |
| FIS-010 | Los pagos explícitos fuera del entorno local suman al menos 25 reales: 15 a Valladolid y 10 a León. | C | R25; CAL-015 | Admitida como mínimo documentado. |
| FIS-011 | Esos 25 reales equivalen al 10,73 % de los 233 reales explícitos de R25 y al 2,49 % del mínimo monetario de 1.006 reales. | C | R16, R25, R28; CAL-016 y CAL-017 | Condicionada por sus respectivos denominadores. |
| FIS-012 | El pozo de pesca del conde de Luna está arrendado en nueve reales, declarados como utilidad. | D | R29, f. 319v | Admitida. |

## 4. Interpretaciones autorizables

| ID | Formulación admisible | Apoyo | Estado y condición |
|---|---|---|---|
| INT-001 | La comunidad presenta una base agraria marcadamente cerealista, especialmente centenaria. | AGR-004, AGR-005 | Admitida como interpretación cuantitativa; conservar denominador. |
| INT-002 | La economía local combina agricultura, prados, ganadería, molinos, apicultura, oficios y servicios. | AGR-001–010, GAN-001–007, HID-001–007, TRA-001–005 | Admitida; «economía mixta» es síntesis analítica. |
| INT-003 | La alternancia de cultivos y los descansos introducen diversidad y ritmos distintos dentro del sistema agrario. | AGR-002, AGR-003, AGR-008 | Admitida; no inferir rotaciones efectivamente ejecutadas parcela a parcela. |
| INT-004 | Los aprovechamientos de uso común documentado sostienen funciones ganaderas y materiales relevantes. | GAN-002, FIS-005–008 | Condicionada: no atribuir propiedad ni administración común no documentadas. |
| INT-005 | La pluralidad de molinos, ruedas y titulares ofrece una redundancia potencial de unidades, pero no independencia frente al agua del río. | HID-001–007 | Condicionada; no afirmar continuidad operativa garantizada. |
| INT-006 | La falta de propios, arbitrios y rentas hace visible la dependencia del repartimiento vecinal para los gastos declarados. | FIS-005–007 | Admitida. |
| INT-007 | La combinación de prestaciones en especie y pagos monetarios muestra monetización parcial, no una economía puramente monetaria ni cerrada. | FIS-001–012, TRA-003–004 | Admitida. |
| INT-008 | El herrero-labrador y la composición de los jornaleros muestran pluriactividad y dependencia familiar en casos documentados. | TRA-001, TRA-004 | Admitida; no universalizar a todos los hogares. |
| INT-009 | La estructura observada permite analizar vulnerabilidades, mecanismos de propagación y amortiguadores, pero no afirmar que ocurrieran crisis concretas. | Conjunto del registro | Admitida como regla metodológica. |
| INT-010 | El expediente permite describir estructura fiscal y productiva, pero no medir de forma completa renta familiar, producto total, consumo o nivel de vida. | LIM-001–LIM-008 | Admitida. |

## 5. Límites y discrepancias que deben permanecer visibles

| ID | Límite | Evidencia / consecuencia |
|---|---|---|
| LIM-001 | No consta población total por individuos. | R21 ofrece categorías fiscales y residentes, no un censo de almas. |
| LIM-002 | No puede reconstruirse la renta anual de los hogares. | Faltan jornadas efectivas, distribución de activos, autoconsumo, deudas y numerosos precios. |
| LIM-003 | No puede obtenerse un producto agrario total. | R10 y R12 no permiten asignar sin ambigüedad cada rendimiento a producción anual efectiva. |
| LIM-004 | No consta relación entre el celemín de R10 y el sistema quartal/fanega de R9. | Deben mantenerse siete celemines separados en la suma de partidas. |
| LIM-005 | No constan equivalencias entre carga, fanega y quartal para los productos de R16–R17. | Prohibida su agregación física. |
| LIM-006 | No consta equivalencia real–maravedí en el expediente. | Los precios mixtos pueden transcribirse, pero no decimalizarse con una equivalencia externa no declarada. |
| LIM-007 | R5 y R10 contienen diferencias internas. | TER-009; conservar la discrepancia, no armonizarla tácitamente. |
| LIM-008 | No puede medirse desigualdad general con la distribución parcial de colmenas o ruedas. | Esos activos no representan el patrimonio total de los hogares. |
| LIM-009 | No se documenta comercio neto ni destino predominante de la producción. | Evitar «autoconsumo» o «mercado» como explicación total. |
| LIM-010 | No consta el número de ruedas del molino venturero. | HID-005. |

## 6. Registro de cálculos reproducibles

| ID | Operación | Resultado | Entradas documentales | Condición de uso |
|---|---|---:|---|---|
| CAL-001 | Suma de partidas de R10 expresadas en unidad principal | 3.811,5 medidas + 7 celemines | R10 | No sumar los celemines sin equivalencia. |
| CAL-002 | Agrupación por calidad de las partidas principales | 666 / 1.398 / 1.747,5 | R10 | Total base: 3.811,5. |
| CAL-003 | Cabida cultivada comparable | 2.953,5 | R10 | Excluye prados, matorrales, eras/sitios, sotos y los siete celemines. |
| CAL-004 | Cabida centenal | 2.750,5 | R10 | Suma de categorías centenales identificadas. |
| CAL-005 | 2.750,5 ÷ 2.953,5 × 100 | 93,13 % | CAL-003, CAL-004 | Denominador: cultivada comparable. |
| CAL-006 | 2.750,5 ÷ 3.811,5 × 100 | 72,16 % | CAL-001, CAL-004 | Denominador: total explícito principal. |
| CAL-007 | Aplicación mecánica de coeficientes anuales según ciclo | 1.578,25 medidas | R4, R10 | Índice analítico, no observación anual. |
| CAL-008 | Componente centenal activo ÷ CAL-007 × 100 | 87,14 % | CAL-004, CAL-007 | Depende de los coeficientes del escenario. |
| CAL-009 | 40 fejes × 4 libras | 160 libras | R16 | Solo para la partida de lino decimal. |
| CAL-010 | 18 pies × 2 reales | 36 reales | R19 | Utilidad anual regulada. |
| CAL-011 | (7 + 6) ÷ 18 × 100 | 72,22 % | R19 | Concentración de colmenas, no riqueza total. |
| CAL-012 | 3 + 2 + 2 + 1 | 8 ruedas | R17 | Excluye el venturero de número desconocido. |
| CAL-013 | 3 ruedas × 2 cargas + 5 ruedas × 4 cargas | 26 cargas de centeno | R17 | No convertir a otras unidades. |
| CAL-014 | 633 + 233 + 140 | 1.006 reales | R16, R25, R28 | Mínimo monetario institucional explícito; no total fiscal. |
| CAL-015 | 15 + 10 | 25 reales | R25 | Mínimo con destino exterior explícito. |
| CAL-016 | 25 ÷ 233 × 100 | 10,73 % | R25 | Denominador: partidas monetarias explícitas de R25. |
| CAL-017 | 25 ÷ 1.006 × 100 | 2,49 % | CAL-014, CAL-015 | Denominador: mínimo monetario agregado. |
| CAL-018 | 14 + 3 + 1 | 18 jornaleros | R35 | Verificación interna de la composición. |
| CAL-019 | 18 + 8 | 26 habitantes fiscales declarados | R21 | Reproduce la suma textual; no población total. |
| CAL-020 | 7 + 6 + 3 + 1 + 1 | 18 pies de abejas | R19 | Verificación interna. |

## 7. Afirmaciones rechazadas o que requieren reformulación

| Formulación no admisible | Problema | Resolución canónica |
|---|---|---|
| «Los bienes comunales pertenecían al común.» | Confunde uso con propiedad. | Usar GAN-002 e INT-004. |
| «El común administraba montes, sotos y pastos.» | La administración no está documentada. | Limitarse al uso común declarado. |
| «El común del lugar era el Concejo de Ordás.» | Fusiona escalas y sujetos distintos. | Mantener JUR-002 y FIS-005–008 como nodos separados. |
| «No conocemos relación entre quartal y fanega.» | Contradice R9. | TER-005: cuatro quartales por fanega; la laguna afecta al celemín de R10. |
| «Las crecidas destruyeron puentes y paralizaron los molinos.» | Une dos hechos sin mecanismo completo documentado. | Usar HID-006 y, si procede, HID-007 como interpretación condicionada. |
| «El clima era un nodo causal documentado.» | El expediente no describe un régimen climático. | Puede formularse solo como hipótesis externa futura, no en el corpus cerrado. |
| «El cereal necesitaba molienda para convertirse en alimento.» | Generalización funcional no declarada por la fuente. | Describir molinos harineros y evitar necesidad exclusiva. |
| «La producción se destinaba al autoconsumo.» | El destino no está documentado. | Aplicar LIM-009. |
| «Había redundancia operativa del sistema molinero.» | La pluralidad no garantiza continuidad. | INT-005: redundancia potencial de unidades. |
| «La copropiedad era un amortiguador.» | Exceso causal y posible confusión de titulares. | Describir pluralidad de derechos; separar cualquier hipótesis. |
| «Ocho ruedas fijas y un molino venturero.» | «Fijas» no es término documental y el venturero puede inducir doble conteo. | HID-002 e HID-005. |
| «La presión fiscal total era de 1.006 reales.» | Agregado parcial y heterogéneo. | FIS-009: mínimo monetario institucional explícito. |
| «Era una pequeña economía de subsistencia.» | Comparación y tipología no demostradas. | INT-002 e INT-007, sin etiqueta totalizante. |

## 8. Reglas de incorporación a la versión canónica

1. Toda cifra derivada debe citar su `CAL-*` y las afirmaciones documentales que aportan sus operandos.
2. Una frase que combine D, C e I debe separarlos gramaticalmente o marcarlos de manera inequívoca.
3. Ningún cálculo se repetirá con redondeo o denominador diferente sin crear una nueva entrada.
4. Las discrepancias de la fuente se expondrán donde afecten al argumento, no solo en nota final.
5. Los escenarios de vulnerabilidad usarán la secuencia **dato → mecanismo inferido → posible efecto → amortiguador**, sin asignar probabilidad ni historicidad al escenario.
6. Las referencias mínimas serán respuesta, folio y, cuando sea útil para control interno, unidad lógica.
7. Las versiones 0.1–0.6 no se citarán como evidencia histórica; solo como antecedentes analíticos.

## 9. Criterio de cierre

El registro queda apto como puerta de entrada para la futura redacción canónica. Antes de publicar esa redacción deberá comprobarse que toda afirmación sustantiva corresponde a una entrada admitida o que cualquier nueva entrada se añade aquí con evidencia, nivel y cautela explícitos.


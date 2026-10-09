# Informe comparativo: composición 0.6 y candidata Quarto 1.0

**Fecha de revisión:** 9 de octubre de 2026<br>
**Fase:** 6A.1 — revisión editorial final de la candidata 1.0<br>
**Baseline de auditoría:** `088e4fcec91fa9723b5b0ffad4f65781a9c0af6c`<br>
**Commit de la candidata técnica:** `49ab2e1b1a58ca9201efab54b42a3125de7326f8`<br>
**Estado:** comparación editorial y funcional; las clasificaciones son propuestas pendientes de decisión humana.

## Conclusiones ejecutivas

1. La candidata Quarto ya es un libro completo: contiene las seis partes, los capítulos 1–16, las 18 páginas facsimilares, las 35 unidades transcritas, las 40 respuestas modernizadas, cuatro aparatos generados y nueve índices. Las afirmaciones del informe anterior sobre capítulos o aparatos todavía inexistentes han quedado obsoletas.
2. Quarto mejora de forma sustancial la fidelidad documental y la consulta: separa las 18 páginas completas de los 35 recortes, usa la Edición Crítica 3.6, conserva las seis secciones del aparato por unidad, genera una concordancia bidireccional y ofrece índices con enlaces HTML y páginas PDF reales.
3. La Parte II de Quarto tiene mayor desarrollo y cautela que 0.6. Conserva la cobertura temática, aumenta de unas 15.122 a 15.758 palabras extraídas y elimina o reformula afirmaciones demasiado fuertes sobre comunales, autoconsumo, clima, copropiedad, ruedas y resiliencia.
4. La principal pérdida material respecto a 0.6 es la cartografía. Las dos láminas de 0.6 cumplen una función de orientación regional, provincial y local que no tiene equivalente en la candidata.
5. La principal carencia bibliográfica es de sistema, no de número bruto de enlaces. Quarto conserva 41 URL únicas frente a 42 en 0.6 y la matriz identifica numerosas fuentes externas, pero `references.bib` sigue vacío y el capítulo del topónimo no ofrece al lector llamadas o referencias próximas que lo conduzcan a esas entradas.
6. La trazabilidad D/C/I/E/L es más robusta como dato estructurado: la matriz reproduce 112 entradas y la concordancia conecta respuestas, unidades, transcripción y facsímil. Sin embargo, las marcas del cuerpo no enlazan directamente con la matriz y solo son visibles de forma sistemática en los capítulos 9–13.
7. Faltan componentes que el Plan Maestro situó entre los preliminares y los aparatos narrativos: créditos y responsabilidades editoriales definitivas, cartografía, una presentación o guía preliminar consolidada, cronología, cuestiones abiertas, fuentes/bibliografía, historia de versiones y modelos de cita.
8. La candidata conserva todavía metadatos de desarrollo: subtítulo «Edición en desarrollo», versión `0.1.0-dev`, estado `development`, autor PDF vacío y ausencia de licencia, copyright, fecha editorial y URL canónica. Estos valores no deben llegar sin decisión a una publicación 1.0.
9. No debe restaurarse todo lo que aparecía en 0.6. Su facsímil solo por unidades, sus localizadores provisionales y varias formulaciones históricas superadas han sido sustituidos por soluciones equivalentes o mejores.
10. La matriz de decisiones se mantiene separada en [REVISION_EDITORIAL_CANDIDATA_1_0.md](./REVISION_EDITORIAL_CANDIDATA_1_0.md). Ninguna clasificación B/M/F/N equivale a una decisión del usuario.

## 1. Alcance, autoridad y baseline

La composición 0.6 se usa únicamente como referencia editorial. No prevalece sobre el manuscrito autoritativo, la Edición Crítica, el Manual Editorial, el Estudio Histórico, el Registro D/C/I/E/L ni los demás documentos canónicos de `project/`.

La auditoría partió de un árbol limpio en `feature/quarto-book`. Tras actualizar las referencias remotas se comprobó:

| Elemento | Valor |
|---|---|
| Baseline documental de auditoría | `088e4fcec91fa9723b5b0ffad4f65781a9c0af6c` |
| Candidata técnica | `49ab2e1b1a58ca9201efab54b42a3125de7326f8` |
| Upstream al inicio | `e74ce3cb8bd27921f50db5a046a0851528297ced` |
| Upstream final antes del commit | `088e4fcec91fa9723b5b0ffad4f65781a9c0af6c` |
| Relación upstream/baseline final | 0 detrás, 0 delante; coincidencia exacta |
| `main` y `origin/main` | `e81dc9239ac8dbabfe77168a50ef98c4d3b79170` |
| Árbol `project/` en candidata y `main` | `e32917763475ceebdfe7b54830e1fb43f6419dad`; igualdad exacta |
| Árbol `publication/` auditado | `cfcf349928fe3e1f2d3b33c005c31fa5621b1878` |

No se regeneró la candidata: el PDF disponible coincidía exactamente con el manifestado y bastaba para la auditoría. Los derivados se trataron como salidas de solo lectura.

## 2. PDFs comparados

| Dato | Composición 0.6 | Candidata Quarto |
|---|---|---|
| Ubicación | réplica externa `~/.local/share/sorrios-ensenada/Sorrios_1752_Volumen_Completo_0_6_Lectura.pdf` | `publication/_book/sorribos-santibanez-ordas-1752.pdf` |
| Páginas | 259 | 334 |
| Bytes | 6.806.113 | 73.994.496 |
| SHA-256 | `78551fc2bcc067634b97e6284b5a3b88b1916067851d51ee00b14e488e4187f4` | `f1eee2f465f554d3bf2b506d23a622967d1b4f1013ac657a774868e525688183` |
| Tamaño de página | A4 | Letter |
| Versión PDF | 1.4 | 1.7 |
| Texto | seleccionable | seleccionable |
| PDF etiquetado | no | no |

La diferencia de tamaño procede principalmente de las 53 imágenes del manuscrito a 180 dpi incorporadas por Quarto; no indica por sí sola mayor contenido intelectual.

## 3. Metodología y limitaciones

Se combinaron:

- extracción de texto con preservación de páginas y disposición;
- inventario de imágenes, fuentes y anotaciones URL con Poppler;
- revisión del índice general y de los límites de cada parte;
- inspección visual de portada, mapas, facsímil, transcripción, topónimo, aparatos e índices;
- contraste con `_quarto.yml`, los manifiestos de `publication/meta/`, los QMD editoriales y los derivados ya generados;
- recorridos funcionales por HTML y PDF para D/C/I/E/L, concordancia, respuestas, transcripción y facsímil;
- lectura del Plan Maestro, el roadmap y el informe de candidata.

No se hizo OCR porque ambos PDF ofrecen texto extraíble. No se realizó investigación histórica externa ni se verificó de nuevo la corrección científica de cada fuente citada. El recuento de «tablas» de 0.6 no es comparable de forma fiable porque ese PDF no expone estructura semántica; no se fuerza una cifra.

Los recuentos de marcas se refieren a grupos visibles con forma `[D:`, `[C:`, `[I:`, `[E:`, `[L:` o combinaciones. Una marca puede contener varios identificadores y no equivale a una entrada de la matriz.

## 4. Comparación cuantitativa

| Métrica | Composición 0.6 | Candidata Quarto | Método y lectura |
|---|---:|---:|---|
| Páginas PDF | 259 | 334 | `pdfinfo` |
| Bloques funcionales equivalentes a capítulos 1–16 | 16 | 16 | índice general; 0.6 no numera todos como capítulos |
| Páginas digitales completas del manuscrito | 0 como serie independiente | 18 | 0.6 muestra 35 unidades; Quarto separa páginas completas y recortes |
| Unidades materiales con imagen y transcripción | 35 | 35 | índice y concordancia |
| Preguntas/respuestas modernizadas | 40 | 40 | índice y contenido |
| Aparatos principales generados | 4 | 4 | glosario, cuadros, concordancia y matriz |
| Aparatos narrativos adicionales | 4 | 0 | cuestiones abiertas, fuentes, versiones y modelos de cita |
| Índices | 9 | 9 | índice general |
| Entradas de los índices | 129 | 164 | recuento de entradas; los índices 6, 7 y 9 son más amplios en Quarto |
| Imágenes incrustadas | 73 | 53 | `pdfimages -list`; 0.6 = 3 cartográficas + 35 facsimilares + 35 de transcripción; Quarto = 18 + 35 |
| Anotaciones URL | 154 | 91 | `pdfinfo -url`; incluye repeticiones |
| URL externas únicas | 42 | 41 | normalización exacta de destinos URL |
| Notas de la edición modernizada | 39 | 39 | 35 numéricas y 4 semánticas |
| Grupos D/C/I/E/L visibles en el cuerpo | 95 | 77 | extracción textual; Quarto los concentra en capítulos 9–13 |
| Entradas de la matriz D/C/I/E/L | 112 | 112 | Registro 1.2 reproducido |
| Entradas de glosario | 22 | 22 | títulos de entrada |
| Tablas accesibles auditadas | no comparable | 44 | cifra de la auditoría 5B; 0.6 carece de estructura semántica comparable |

La mayor paginación de Quarto no expresa redundancia de contenido: dedica 18 páginas al facsímil íntegro, unas 103 a transcripción y aparato y 38 a índices desarrollados. La Parte II ocupa 53 páginas frente a 42 en 0.6.

## 5. Arquitectura y cobertura intelectual

| Componente | 0.6 | Quarto | Evaluación |
|---|---|---|---|
| Portada | diseñada, con alcance y versión | tipográfica mínima, con subtítulo de desarrollo | pérdida de terminación editorial, no de contenido histórico |
| Preliminares | créditos, guía D/C/I/E/L, índice y nota de composición | portada e índice; funciones metodológicas desplazadas a capítulos 1–4 | equivalencia parcial |
| Parte I | cuatro capítulos funcionales | capítulos 1–4 | equivalente y algo más desarrollado |
| Parte II | nueve capítulos temáticos | capítulos 5–13 | cobertura equivalente; Quarto es más granular y cauteloso |
| Documento original | 35 recortes por unidad | 18 páginas completas | Quarto mejora materialidad; los recortes reaparecen en capítulo 15 |
| Transcripción | 35 unidades y aparato | 35 unidades y seis secciones por unidad | equivalente en cobertura; Quarto mejora navegación y legibilidad |
| Modernizada | 40 respuestas | 40 respuestas | equivalente; misma base 1.3 y 39 notas |
| Aparatos | ocho, cuatro de ellos narrativos | cuatro generados | pérdida real de aparatos narrativos |
| Índices | nueve, varios provisionales | nueve completos con localizadores reales | mejora clara de Quarto |
| Cierre | colofón provisional | termina con el índice de materias | ausencia no bloqueante por sí sola, pero requiere decisión editorial |

La cobertura intelectual de Catastro, interrogatorio, expediente local, materialidad, jurisdicción, vecindad, tierra, producción, ganadería, recursos comunes, molinos, fiscalidad, hacienda, dinero, oficios, conexiones, vulnerabilidades y límites está presente en ambas versiones. No hay pérdida de un tema histórico principal.

## 6. Profundidad del estudio histórico

La refundición Quarto preserva los nueve campos de la Parte II de 0.6 y los distribuye en capítulos más definidos. La extracción arroja unas 15.758 palabras en las páginas de la Parte II frente a 15.122 en 0.6; la diferencia es modesta en volumen, pero importante en método.

Quarto mejora expresamente:

- la separación entre vecino, medio vecino, residente, hogar, vivienda y población;
- los denominadores de cabida y porcentajes agrarios;
- la distinción entre valoración, utilidad, producción, renta e ingreso;
- el tratamiento de casa de molino, rueda, venturero, titular, operador y usuario;
- la separación entre común, concejo, vecinos, propiedad y uso documentado;
- la distinción entre dependencia, exposición, daño y resiliencia;
- la visibilidad de ausencias y magnitudes no calculables.

La candidata no debe recuperar las formulaciones de 0.6 que presentan «bienes comunales» sin título probado, una «fuerte base de autoconsumo», `CLIMA` como nodo documental, copropiedad o redundancia como amortiguador demostrado, «ocho ruedas fijas» o los 26 *avitadores* como habitantes fiscales. Su retirada o reformulación es una mejora, no una regresión.

## 7. Preliminares previstos y reales

| Elemento del Plan Maestro | Estado en la candidata | Evaluación |
|---|---|---|
| Portada | presente, mínima y aún marcada como desarrollo | requiere cierre editorial |
| Créditos | ausentes del libro | carencia real |
| Presentación | función repartida entre portada y capítulos 1–4 | cobertura parcial |
| Nota al lector | ausente como pieza propia | mejora conveniente |
| Guía de uso | función parcial en capítulos 4, 14–16 y aparatos | cobertura dispersa |
| Convenciones | explicadas parcialmente en capítulo 4 y en cada derivado | cobertura parcial |
| Guía D/C/I/E/L | capítulo 4 y matriz | presente con otro nombre y ubicación |
| Cronología | presente en el capítulo 3, no como preliminar autónomo | cobertura funcional; su ubicación requiere decisión |
| Cartografía | ausente | pérdida real respecto a 0.6 |
| Índice general | presente, 18 páginas | presente y detallado |
| Reproducciones y cuadros | presentes en capítulos 14–16 y aparatos | función cubierta fuera de preliminares |

No es necesario duplicar en preliminares lo que funciona mejor dentro del libro. Sí debe resolverse qué orientación mínima necesita un lector antes del capítulo 1.

## 8. Cartografía

0.6 contiene dos láminas:

1. «Situación regional», con una vista peninsular y otra provincial que señalan Ordás y declaran que la circunferencia no representa límites históricos.
2. «Sorribos (1752) y Sorrios actual», con Sorrios/Sorribos, Santibáñez de Ordás, Santa María de Ordás, Villapodambre, Tapia de la Ribera y Rioseco de Tapia; aclara que los círculos son localizadores puntuales.

Su valor es editorial: orientan al lector en escalas sucesivas y sitúan los núcleos necesarios para entender el expediente sin convertir el mapa contemporáneo en reconstrucción territorial de 1752. La candidata no ofrece imagen ni componente equivalente. La prosa que advierte contra una precisión cartográfica indebida es correcta, pero no sustituye esa orientación.

La ausencia cumple la definición de regresión real: estaba correctamente resuelta, sigue siendo deseable, el Plan Maestro la prometía y no existe una sustitución equivalente. Recuperarla exige revisar procedencia, licencia, fecha de consulta, base cartográfica, rotulación y texto alternativo; no autoriza a copiar las imágenes sin control.

## 9. Historia de Sorribos y Sorrios

Ambas versiones cubren 1215, 1267, 1715, 1752, 1768, 1831, 1836, 1848 y la identificación actual. Quarto formula con mayor claridad:

- la secuencia `Sorribios` → `Sorribos` → `Sorrios`;
- la diferencia entre continuidad de identificación y evolución fonética completa;
- el alcance patrimonial concreto de los testimonios medievales;
- que `Sorribas` es un error paleográfico descartado, no una variante histórica del núcleo de Ordás.

0.6, sin embargo, ofrece junto al pasaje una lista visible de siete referencias externas enlazadas y marcas E/I/L. En Quarto, el capítulo 3 presenta la cronología sin llamadas visibles; las referencias aparecen después en las entradas `TOP-004`–`TOP-011` de la matriz, pero el capítulo no conduce al lector hasta ellas. La información no se ha perdido, pero sí se ha debilitado su verificabilidad inmediata.

No se reabre la decisión paleográfica: la lectura `Sorribos` y la rectificación de `Sorribas` son mejoras canónicas de Quarto.

## 10. Fuentes, bibliografía y enlaces externos

La composición 0.6 presenta 154 anotaciones URL y 42 destinos únicos. Quarto presenta 91 anotaciones y 41 destinos únicos. La diferencia de anotaciones se debe sobre todo a repeticiones, no a una desaparición masiva de fuentes.

Quarto dispone de tres capas de procedencia:

1. `sources:` de cada capítulo, útil para el control editorial interno;
2. identificadores `evidence:` y una matriz de 112 entradas;
3. enlaces externos visibles en capítulos, transcripción, glosario, matriz e índices.

Estas capas no equivalen a una bibliografía para el lector. `references.bib` contiene cero entradas; no hay citas bibliográficas Pandoc en los capítulos; varias entradas E ofrecen solo una descripción breve y una URL; y el libro no incluye el aparato narrativo «Fuentes y bibliografía» previsto por el Plan Maestro.

La solución no tiene que copiar el apéndice F de 0.6 ni poner una nota en cada contexto E. Debe permitir identificar públicamente las fuentes, distinguir archivo/edición/estudio/recurso web y conectar las afirmaciones relevantes con referencias comprobables.

## 11. Trazabilidad D/C/I/E/L

### Cobertura y experiencia real

0.6 muestra 95 grupos de marcas en el cuerpo. Quarto muestra 77, concentrados en los capítulos 9–13; los capítulos 3 y 5–8 declaran evidencia en YAML, pero no muestran marcas junto a la prosa. Ambas versiones reproducen las 112 entradas de la matriz.

En HTML, cada entrada de la matriz tiene ancla y enlaza a los capítulos que la usan. Las marcas del cuerpo, sin embargo, son texto plano: `[D: HID-001]` no enlaza a `#evidencia-hid-001`. En PDF la búsqueda textual permite resolver el ID, pero tampoco hay salto directo desde la marca.

### Recorridos comprobados

Se siguió la misma cadena desde el capítulo 9 para los cinco niveles:

| Nivel | Afirmación / ID | Resolución en matriz | Evidencia y regreso al documento |
|---|---|---|---|
| D | cuatro casas de molinos, `HID-001` | entrada D, estado admitido | R17, ff. 315r–316r → concordancia → folios 315r, 315v y 316r → páginas digitales 11–12 |
| C | 26 cargas de utilidad, `HID-004` | entrada C con cautela de unidades | R17 y `CAL-013` → respuesta 17 → los mismos folios y facsímil |
| I | redundancia potencial, `INT-005` | entrada I condicionada | remite a `HID-001`–`HID-007`; la matriz separa interpretación de los datos de R17 |
| E | contexto molinero, `HID-008` | entrada E/I admitida como comparación | dos referencias externas visibles; la cautela impide transferir caudales o meses a Sorribos |
| L | ruedas desconocidas del venturero, `LIM-010` | entrada L | remite a `HID-005` → R17, ff. 315r–316r → transcripción y facsímil |

La cadena es completa, pero requiere búsqueda manual y conocer la función de la concordancia. Quarto mejora los eslabones posteriores a la matriz; 0.6 hace más continuas las marcas del cuerpo. La mejora pendiente es de navegación y visibilidad, no de ausencia de evidencia.

## 12. Facsímil

0.6 dedica 35 páginas a recortes de unidades materiales. Son grandes, legibles y rotulados con unidad, página digital y posición, pero no conserva en una serie separada las 18 imágenes completas.

Quarto dedica 18 páginas a las imágenes digitales completas, con márgenes, blancos, sellos y materialidad; el capítulo 15 vuelve a mostrar los 35 recortes correspondientes. La imagen completa impresa es algo menor que el recorte de 0.6, pero sigue siendo legible con ampliación y la salida HTML permite una consulta más flexible.

La candidata mejora cobertura, orden y contexto. No se observa pérdida que justifique volver al modelo exclusivo por unidades de 0.6.

## 13. Transcripción y aparato crítico

Las dos versiones cubren las 35 unidades. Quarto conserva en cada una:

- imagen;
- transcripción paleográfica;
- observaciones editoriales;
- notas paleográficas;
- notas históricas;
- referencias cruzadas.

La candidata aplica la Edición Crítica 3.6 vigente, mantiene lineación, abreviaturas y dudas, y enlaza unidades con respuestas y páginas facsimilares. Su composición ocupa más páginas y deja mayor aire tipográfico. 0.6 es más compacta y usa encabezados corridos más elaborados, pero no ofrece mayor fidelidad textual.

Las lecturas corregidas y las cautelas actuales son mejoras de Quarto. No debe recuperarse ninguna lectura antigua por el solo hecho de aparecer en 0.6.

## 14. Edición modernizada

Ambas versiones presentan portada, comparecencia, preguntas y respuestas 1–40, ratificación, edades, firmas, concordancia y nota de uso. Ambas conservan 39 notas.

0.6 asigna aproximadamente una página a cada respuesta y reúne las notas al final. Quarto compone el texto en 24 páginas, coloca las notas a pie en el punto de lectura y añade enlaces materiales en HTML. La candidata es más compacta sin perder respuestas ni cautelas. La diferencia es de diseño, no una regresión.

## 15. Aparatos

| Aparato previsto | 0.6 | Quarto | Evaluación |
|---|---|---|---|
| Glosario | 22 entradas | 22 entradas enlazadas | equivalente; Quarto mejora navegación |
| Cuadros cuantitativos | presentes | 13 entradas C y 17 cálculos asociados | Quarto más estructurado y reproducible |
| Concordancia | presente | dos vistas, 35 unidades, 40 respuestas y 65 relaciones | mejora clara |
| Matriz D/C/I/E/L | 112 entradas | 112 entradas con estado, cautela y uso en el libro | mejora de estructura y navegación |
| Cuestiones abiertas | apéndice propio | solo dispersas en matriz y capítulos | ausencia prevista por el plan, no equivalencia plena |
| Fuentes y bibliografía | apéndice propio y listas próximas | datos repartidos; `.bib` vacío | carencia de sistema público |
| Historia de versiones | apéndice propio | informe técnico fuera del libro | ausencia en la experiencia del lector |
| Modelos de cita | apéndice propio | ausentes | ausencia real |

Los cuatro últimos aparatos no fueron asignados a la fase generadora 4D, pero sí permanecieron prometidos por el Plan Maestro. Su ausencia no puede tratarse como olvido técnico accidental: requiere decidir ahora su alcance para 1.0.

## 16. Índices

Las dos versiones contienen nueve índices. En 0.6 los índices 6, 7, 8 y 9 se declaran provisionales y remiten a capítulos o respuestas; los localizadores de página se posponen a una versión 0.8. Quarto genera los nueve desde fuentes estructuradas y resuelve páginas reales en PDF y destinos enlazados en HTML.

Quarto amplía especialmente:

- productos, cultivos, ganados y recursos: 9 → 27 entradas;
- cargas, derechos, rentas y fiscalidad: 7 → 15;
- materias: 12 → 21.

El índice de preguntas conserva 40 entradas. Los cinco índices basados en fuentes vivas mantienen 21, 9, 7, 12 y 12 entradas. Los localizadores visibles, variantes, remisiones y cautelas hacen que la candidata sea funcionalmente superior. No hay regresión que recuperar.

## 17. Metadatos editoriales

| Elemento | 0.6 | Quarto | Evaluación |
|---|---|---|---|
| Título | título y subtítulo de alcance | título correcto | presente |
| Subtítulo | describe estudio y cuatro accesos | «Edición en desarrollo» | debe resolverse antes de 1.0 |
| Autor PDF | «Proyecto Sorríos - Catastro de Ensenada» | vacío | ninguna versión fija autoría personal; Quarto pierde incluso la atribución colectiva |
| Responsabilidad editorial | crédito de proyecto, no roles personales | ausente | pendiente |
| Versión/estado | 0.6, composición revisada | `0.1.0-dev`, `development` | bloqueante propuesto para 1.0 |
| Fecha | 2026 | fecha de creación técnica, no fecha editorial fijada | pendiente |
| Licencia/copyright | ausentes | ausentes | pendiente de decisión |
| URL canónica | ausente | ausente | depende de publicación, pero debe decidirse |
| ISBN | ausente | ausente | no bloqueante técnico; decisión separada |

La ausencia no autoriza a inventar datos. Sí obliga a obtener decisiones explícitas antes de declarar publicada una edición 1.0.

## 18. Diseño y experiencia de lectura

0.6 ofrece una identidad visual más terminada: portada compuesta, color, encabezados corridos, A4, mapas y aperturas de apéndice. Quarto usa una presentación LaTeX más sobria, Letter, mucho espacio blanco y una portada mínima. Las dos son legibles; no hay base para declarar A4 superior a Letter ni para reproducir la maqueta antigua.

Quarto es mejor en navegación digital, enlaces internos, búsqueda HTML, estructura accesible básica, anclas, localizadores e índices. 0.6 es mejor en orientación inicial, cartografía, proximidad de fuentes en el capítulo del topónimo y señalización editorial de preliminares/apéndices.

Ninguna versión es PDF etiquetado. La candidata no declara PDF/UA, PDF/A ni conformidad WCAG formal; esta limitación conocida no invalida por sí sola la edición 1.0.

## 19. Mejoras de Quarto respecto a 0.6

- 16 capítulos completos en una única fuente multiformato.
- Mayor cautela factual y eliminación de formulaciones superadas.
- 18 páginas facsimilares completas más 35 recortes de unidad.
- 35 unidades con seis secciones canónicas y navegación estable.
- 40 respuestas verificadas con notas en contexto.
- Glosario, cuadros, concordancia y matriz reproducibles.
- Matriz completa de 112 entradas y estados/cautelas visibles.
- Nueve índices enlazados con localizadores PDF automáticos.
- Índices 6, 7 y 9 notablemente ampliados.
- HTML con búsqueda, navegación, reflow y texto alternativo.
- Generación idempotente, validación automatizada y separación entre fuentes, edición y derivados.
- Distinciones más rigurosas entre dato, cálculo, interpretación, contexto y límite.

## 20. Elementos de 0.6 no equivalentes en la candidata

| Elemento de 0.6 | Aporte | Sustitución actual | ¿Genera REV-*? |
|---|---|---|---|
| Dos láminas cartográficas | orientación a tres escalas | ninguna | sí, `REV-002` |
| Fuentes visibles junto al topónimo y apéndice bibliográfico | verificabilidad pública | matriz distante y URL dispersas | sí, `REV-003` |
| Cuestiones abiertas | síntesis legible de límites | matriz L y cautelas dispersas | sí, `REV-004` |
| Historia de versiones | identifica base y evolución | informe externo al libro | sí, `REV-004` |
| Modelos de cita | facilita uso académico | ninguno | sí, `REV-004` |
| Créditos y versión visibles | identidad de la edición | metadatos de desarrollo incompletos | sí, `REV-001` |
| Colofón | cierre y fecha editorial | ninguno | sí, `REV-007` |
| Facsímil solo por unidades | gran tamaño de recorte | páginas completas + recortes | no recuperar; `REV-010` |
| Índices provisionales | consulta temática básica | índices completos y enlazados | no recuperar; `REV-011` |
| Formulaciones históricas fuertes | síntesis, pero con exceso inferencial | prosa más cauta | no recuperar; `REV-009` |
| Maqueta A4 y paginación | identidad visual | diseño Letter multiformato | diferencia neutral; `REV-012` |

## 21. Evolución de esta comparación

El informe del 4 de octubre describía un checkout de 68 páginas con capítulos 1–11, prototipos documentales, sin aparatos completos ni índices, y con idioma HTML incorrecto. Esa fotografía fue útil para detectar bibliografía, cartografía y trazabilidad, pero ya no representa la candidata.

Desde entonces se completaron los capítulos 12–16, los cuatro aparatos, los nueve índices, la auditoría integral 5B y la candidata 6A. El idioma público es español, la prueba técnica está fuera de navegación y el PDF tiene 334 páginas. Se conservan del análisis anterior únicamente los hallazgos que siguen verificados contra los dos PDF actuales.

## 22. Resultado

La candidata supera a 0.6 en integridad documental, rigor histórico, reproducibilidad, navegación e índices. No se detecta pérdida de capítulos, unidades, respuestas, matriz, glosario ni temas históricos principales.

Las pérdidas o carencias que requieren decisión se concentran en la terminación editorial: metadatos y créditos, cartografía, sistema bibliográfico visible, aparatos narrativos prometidos, orientación preliminar y cierre. La clasificación propuesta y las acciones posibles figuran en [REVISION_EDITORIAL_CANDIDATA_1_0.md](./REVISION_EDITORIAL_CANDIDATA_1_0.md).

## Referencias internas

- [Plan Maestro de publicación](./PLAN_MAESTRO_PUBLICACION_QUARTO.md)
- [Estado y roadmap](./ESTADO_PUBLICACION_QUARTO.md)
- [Informe de candidata 1.0](./CANDIDATA_PUBLICACION_1_0.md)
- [Matriz de revisión editorial](./REVISION_EDITORIAL_CANDIDATA_1_0.md)
- [Instrucciones de publicación](../.github/instructions/publication.instructions.md)
- [Configuración Quarto](../publication/_quarto.yml)
- [Capítulo 3: expediente y topónimo](../publication/content/01-catastro/03-expediente-sorribos-santibanez.qmd)
- [Capítulo 4: del manuscrito al volumen](../publication/content/01-catastro/04-manuscrito-volumen-actual.qmd)

**Nota de integridad:** los PDF comparados y las imágenes temporales de inspección permanecen fuera del repositorio. Esta auditoría no modifica la candidata ni las fuentes canónicas.

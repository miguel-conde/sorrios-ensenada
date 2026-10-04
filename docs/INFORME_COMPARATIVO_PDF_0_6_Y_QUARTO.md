# Informe comparativo: composición 0.6 y libro Quarto en desarrollo

**Fecha de revisión:** 4 de octubre de 2026 **Objeto:** comparación editorial entre el PDF «Sorribos y Santibáñez de Ordás en 1752», composición integral 0.6, y la edición Quarto presente en el checkout local. **Estado:** análisis comparativo; no es una auditoría de autoridad histórica ni una propuesta de cambiar fuentes canónicas.

## Conclusiones ejecutivas

1.  **La composición 0.6 es más completa como libro y ofrece más instrumentos de consulta visibles.** Integra estudio, facsímil, transcripción, edición modernizada, aparatos e índices en 259 páginas. Incluye dos mapas y un aparato bibliográfico visible que, en el ejemplo recibido de la página 15, coloca siete enlaces externos activos al final del tratamiento del topónimo.
2.  **Quarto sigue siendo una obra en curso, no una versión completa comparable página por página.** El render local consultado tiene 68 páginas; incluye los capítulos 1–11, una prueba técnica y prototipos de facsímil, transcripción, edición modernizada y aparato de molinos. No contiene todavía los capítulos 12–13 ni los aparatos e índices previstos para las fases posteriores.
3.  **En 0.6 los códigos tienen un uso editorial efectivo, no son solo una leyenda.** Se colocan al final de afirmaciones o párrafos para clasificar el tipo de afirmación y remitir por ID al Registro, cuyo apéndice D reproduce formulación, evidencia, estado y cautelas. Esto hace auditable el razonamiento, aunque el lector tenga que buscar manualmente el código.
4.  **Quarto explica explícitamente el mismo propósito, pero lo implementa de forma desigual.** El capítulo 4 define D/C/I/E/L y explica que preservan procedencia y grado de afirmación. En el cuerpo actual, las marcas aparecen en los capítulos 9–11; los capítulos 3 y 5–8 tienen inventarios en YAML, pero no marcas junto a sus afirmaciones. Un aparato prototipo de molinos permite una comprobación parcial desde el capítulo 9.
5.  **El recuento sigue mostrando una diferencia de cobertura visible.** En los capítulos que existen en ambas versiones (3 y 5–11), 0.6 presenta 68 grupos en el cuerpo y Quarto 41. Sin embargo, Quarto 9–11 tienen más marcas que sus equivalentes de 0.6; el vacío visible se concentra en el capítulo 3 y los capítulos 5–8.
6.  **Quarto conserva además 151 apariciones de identificadores D/C/I/E/L en YAML para los capítulos 3 y 5–11.** El validador coteja esos inventarios con lo esperado y comprueba que sus IDs existan en el Registro. Es un control real para el equipo, pero no relaciona cada ID con un párrafo, no valida semánticamente la asignación de cada marca y no hace visible el inventario en el HTML/PDF.
7.  **La composición 0.6 sí tiene enlaces bibliográficos externos activos, pero los códigos D/C/I/E/L no son hipervínculos al Registro.** Son dos mecanismos diferentes: las marcas epistemológicas se resuelven manualmente en el registro/apéndice; las URL bibliográficas sí son anotaciones de enlace. El capítulo 9 de Quarto enlaza a su aparato prototipo y a otras vistas, pero los códigos individuales tampoco son enlaces directos a filas.
8.  **Quarto no carece por completo de enlaces externos, pero aún no ofrece una bibliografía editorial propiamente dicha.** Los capítulos 1 y 2 incluyen nueve URL enlazadas a recursos externos. No se encontraron citas bibliográficas con claves `[@…]` en los capítulos editoriales, ni notas a pie en los capítulos 1–11; `references.bib` solo contiene un comentario y cero entradas. Los `sources:` y `evidence:` del front matter documentan procedencia técnica/editorial, no sustituyen citas legibles por el público.
9.  **El tratamiento del topónimo Sorrios se beneficia especialmente de las referencias más visibles de 0.6.** Quarto formula con prudencia la secuencia documental y los límites lingüísticos, pero su capítulo 3 no presenta junto al texto las fuentes externas que permiten comprobar los testimonios de 1215, 1267, 1715, 1768, 1831, 1836, 1848 y el uso actual. En 0.6, el ejemplo de página 15 combina las marcas E/I/L con una relación identificable de fuentes y enlaces.
10. **Ninguna versión acredita claramente a una persona autora.** El PDF lleva como metadato de autor «Proyecto Sorríos - Catastro de Ensenada», sin autoría personal visible en la portada revisada. El PDF Quarto no contiene metadato de autor y la configuración/metadata editorial consultada no declara campo `author`.
11. **Quarto tiene ventajas de método y control que no deben perderse al recuperar elementos del 0.6.** Su prosa reciente distingue con cuidado dato, cálculo, interpretación, contexto externo y límite; declara fuentes e identificadores por capítulo y somete contenido y procedencia a pruebas. El plan prevé generar la matriz D/C/I/E/L, los aparatos y los índices desde fuentes canónicas. La mejora consiste en hacer accesible al lector esa trazabilidad y las fuentes, no en reemplazar el modelo de trabajo ni copiar sin revisión el PDF antiguo.

## Alcance y cautelas de la comparación

-   El PDF 0.6 se consultó como referencia editorial externa, no como autoridad histórica. El estado canónico sigue siendo el de `project/` y el Registro vigente.
-   Se revisaron el PDF 0.6 localizado fuera del repositorio, el render local `publication/_book/`, los archivos QMD, el archivo de bibliografía, la configuración Quarto, el validador, el plan maestro y el roadmap. También se examinaron las capturas facilitadas por el usuario: la página 15 del capítulo 3 del PDF 0.6 y el apartado 4.4 del capítulo 4 Quarto.
-   Las cifras de marcas se obtuvieron buscando grupos con forma `[D:`, `[C:`, `[I:`, `[E:`, `[L:` o combinaciones como `[D/E/L:`. Un «grupo» es una aparición del conjunto de letras antes de los dos puntos; no equivale al número de identificadores que lo siguen.
-   La comparación principal de densidad usa solo capítulos disponibles en ambas versiones: 3 y 5–11. No se cuentan los capítulos 12–13 de 0.6 en ese total, pues todavía no están presentes en los QMD consultados. Tampoco se equiparan los 151 identificadores del YAML con marcas visibles del cuerpo.
-   El checkout examinado es la rama `feature/quarto-book`, diez commits por delante de `origin/feature/quarto-book`, con modificaciones locales preexistentes y un capítulo 11 sin seguimiento por Git. Por tanto, este informe describe ese estado local de trabajo, no una publicación final ni necesariamente el estado de `main`.
-   El informe no modifica `project/`, el roadmap, el PDF, los archivos generados ni el render. El PDF 0.6 y la captura no se incorporan al repositorio.

## Comparativa general

| Aspecto | Composición 0.6 | Quarto local en desarrollo | Evaluación |
|------------------|------------------|------------------|------------------|
| Extensión y cierre editorial | 259 páginas; incluye preliminares, estudio, facsímil, transcripción, edición modernizada, aparatos e índices. | 68 páginas; capítulos 1–11, capítulo técnico, prototipos de capítulos documentales y aparato de molinos. Faltan capítulos 12–13 y productos de fases posteriores. | 0.6 es más completo. La diferencia es esperable por el estado del roadmap Quarto, no prueba por sí sola una decisión editorial de suprimir material. |
| Guía y propósito de D/C/I/E/L | El capítulo 5 define los cinco niveles, declara que los corchetes remiten al Registro y formula restricciones metodológicas para el estudio. | El capítulo 4.4 define los cinco niveles y dice que conservan procedencia y grado de afirmación; el 4.5 describe la cadena de trazabilidad. | Ambos explican el propósito; el uso real debe juzgarse por cómo las etiquetas acompañan afirmaciones y llegan a su expediente de respaldo. |
| Uso de las marcas en el cuerpo | Las marcas aparecen junto a afirmaciones, a menudo al final del párrafo; las entradas pueden combinar niveles y varios IDs. | Hay 41 grupos en el cuerpo de los capítulos 9–11; capítulos 3 y 5–8 no muestran grupos pese a tener `evidence:` en YAML. | 0.6 es más continuo entre capítulos ya escritos; Quarto 9–11 es más denso y operativo en el propio texto, pero el uso no se ha extendido aún a todo el libro. |
| Resolución y control | El apéndice D reproduce el Registro completo; se busca manualmente el ID. El sistema aporta formulación, evidencia/respuesta/folio, estado y cautela o consecuencia. | El YAML se valida frente al inventario esperado y los IDs existentes. Un fragmento de matriz generado de molinos es accesible desde el capítulo 9, pero cubre solo una selección. | 0.6 ofrece una ruta de resolución más amplia y completa para el lector; Quarto combina validación del proyecto y un ejemplo de aparato navegable, pero aún no un resolutor general. |
| Referencias externas | En el ejemplo de la página 15, tras el pasaje sobre el topónimo hay una sección «Fuentes externas» con referencias identificadas y siete URL activas. El PDF declara 154 anotaciones URL en total. | Nueve URL externas en los capítulos 1–2; no se encontraron citas bibliográficas con claves ni bibliografía sustantiva. El capítulo 3 no muestra la lista de fuentes externas del topónimo. | 0.6 proporciona más información bibliográfica visible y más enlaces; Quarto ya enlaza algunos recursos, pero de modo parcial y sin un sistema bibliográfico común. |
| Notas | El ejemplo de página 15 no es una nota a pie: son marcas en el texto y una lista de fuentes al final del pasaje. | No se encontraron notas a pie en los capítulos editoriales 1–11. Hay una nota en el capítulo técnico de prueba, sin contenido histórico. | No debe describirse el ejemplo de 0.6 como prueba de que sus marcas D/C/I/E/L sean notas o enlaces. La comparación general de notas requiere revisar el PDF completo nota por nota. |
| Mapas | Se observaron dos mapas: uno de ubicación regional/provincial y otro de detalle local. | No hay archivos de mapas en `publication/assets/` ni mapas incluidos en los capítulos QMD inspeccionados. | 0.6 facilita orientación territorial; Quarto debería recuperar cartografía con procedencia, leyenda y límites interpretativos, conforme avance su plan. |
| Historia del nombre Sorrios | El capítulo 3 combina testimonios cronológicos, marcas de evidencia, referencias externas y URL activas en el ejemplo de página 15. | El capítulo 3 explica `Sorribios` → `Sorribos` → `Sorrios`, separa identificación histórica de reconstrucción fonética y declara fuentes internas en YAML; no presenta allí una lista visible equivalente de fuentes externas. | Quarto conserva cautelas interpretativas valiosas, pero 0.6 ofrece una ruta de comprobación bibliográfica más inmediata. |
| Autoría | Metadato PDF: «Proyecto Sorríos - Catastro de Ensenada»; no se observó nombre personal en la portada revisada. | Metadato `Author` vacío; no hay campo `author` en la configuración editorial consultada. | Ambas carecen de atribución personal clara. La mención del proyecto en metadatos de 0.6 no identifica autoría individual ni responsabilidades editoriales. |
| Formatos y composición | A4; 259 páginas. La paginación se declara provisional. | PDF local de 68 páginas en tamaño Letter; HTML generado declara `lang="en"` pese a que el contenido es español. | Hay cuestiones técnicas de localización/formato que revisar en Quarto antes de publicación; no invalidan su contenido ni implican por sí solas un defecto histórico. |
| Control metodológico | Integra el tratamiento alcanzado en 0.6 y presenta los aparatos, pero algunos usos pueden requerir revisión frente a fuentes canónicas y criterios actualizados. | Distingue capas epistemológicas, declara procedencia, tiene validación semántica y controles de identificadores; el plan define fuentes canónicas y generación reproducible. | Quarto tiene una arquitectura de control más explícita. El PDF 0.6 es referencia editorial, no autoridad que deba copiarse sin auditoría. |

## Marcas D/C/I/E/L: recuento y lectura correcta

### Recuento del cuerpo

| Capítulo | PDF 0.6: grupos en el cuerpo | Quarto QMD: grupos en el cuerpo |
|--------------------|-------------------------:|-------------------------:|
| 3\. Expediente / topónimo | 7 | 0 |
| 5\. Lugar, señorío y concejo | 10 | 0 |
| 6\. Vecinos, hogares, viviendas y trabajo | 11 | 0 |
| 7\. Tierra, sistema agrario y medidas | 10 | 0 |
| 8\. Ganadería, montes y aprovechamientos comunales | 12 | 0 |
| 9\. Río, molinos y recursos productivos | 5 | 17 |
| 10\. Iglesia, señorío y fiscalidad | 8 | 12 |
| 11\. Hacienda concejil y servicios colectivos | 5 | 12 |
| **Total comparable: capítulos 3 y 5–11** | **68** | **41** |

En el PDF 0.6 se contaron además 15 grupos en el capítulo 12, seis en el 13 y seis en el capítulo 16. El total hallado en el PDF completo fue 95. Ese total completo no es una comparación justa con los QMD, que no tienen aún los capítulos 12–13 y cuya composición incluye prototipos documentales diferentes.

La interpretación por tramo es más informativa que el total:

-   Los capítulos 3 y 5–8 de 0.6 suman 50 grupos visibles en el cuerpo (43 en 5–8 y siete en 3). Sus versiones QMD actuales no tienen marcas en el cuerpo.
-   Los capítulos 9–11 suman 18 grupos en 0.6 y 41 en Quarto. En ese tramo, Quarto no tiene menos marcas: los tres capítulos actuales están más anotados en el cuerpo.
-   En el render HTML observado, las marcas del cuerpo solo aparecen en las páginas/capítulos HTML 9, 10 y 11.

Por tanto, la formulación precisa es: **Quarto no aplica todavía las marcas visibles de forma uniforme a todo el contenido. Su déficit se concentra en capítulos anteriores, mientras que la anotación de los capítulos recientes es más densa que la de los capítulos equivalentes de 0.6.** No es correcto concluir que la práctica empezó en 9; empezó a estar visible allí, pero ya existían inventarios por capítulo en los metadatos de 3 y 5–8.

### Qué aporta el YAML y qué no

Los capítulos 3 y 5–11 declaran `evidence:` por categoría. En esos ocho archivos se contaron **151 apariciones de identificadores** en los inventarios. El validador de [publicación](../publication/scripts/validate_publication.py):

-   lee y normaliza el mapa `evidence`;
-   compara los inventarios de los capítulos con los esperados para cada fase;
-   comprueba que los identificadores declarados existan en el Registro vigente.

Esto no significa que el libro actual ofrezca al lector una referencia individual en cada afirmación. La lista YAML describe el conjunto de evidencia usado por el capítulo, no una relación explícita entre cada frase y su código. Tampoco es una nota al pie ni una bibliografía y no genera por sí sola anclas navegables para el lector. Los capítulos 1 y 2 tienen `sources:` pero no `evidence:`; el capítulo 4 tiene fuentes declaradas, y el validador especifica que no debe declarar evidencia. El plan maestro formula el objetivo de manera compatible: la trazabilidad puede conservarse mediante metadatos, notas, cuadros y una matriz final; no hace falta una letra en cada párrafo, pero el diseño de lectura debe permitir encontrar la fuente.

### Alcance de los códigos

`[L: LIM-001]` significa que la afirmación se clasifica como límite y se identifica con la entrada `LIM-001` del Registro. El código no explica por sí mismo el límite, no es una URL y no garantiza que el PDF lo lleve a un enlace. En 0.6 el código se puede resolver buscando la entrada reproducida en el apéndice D; en Quarto los inventarios YAML ayudan a controlar los identificadores, pero el prototipo actual no los convierte en enlaces individuales del cuerpo al Registro.

Es necesario distinguir, por tanto:

1.  **Marca epistemológica:** p. ej., `[L: LIM-001]`, que clasifica una afirmación e indica un identificador.
2.  **Registro de evidencia:** la entrada que desarrolla afirmación, fuente, respuesta/folio, cautela y, si procede, cálculo.
3.  **Referencia bibliográfica:** autor, título, publicación o archivo, fecha/localizador y URL de una fuente externa.
4.  **Enlace digital:** una anotación de URL o un vínculo interno que permite navegación. No se deduce automáticamente de los otros tres elementos.

### Uso efectivo en la composición 0.6

El capítulo 5 («Método, evidencia y alcance», página impresa 20) no se limita a enumerar las letras. Declara que las referencias entre corchetes remiten al `Registro_Afirmaciones_Calculos_v1.md`, explica qué debe preservar el análisis y añade diez restricciones metodológicas, entre ellas no sumar categorías vecinales como personas equivalentes, no estimar población total y no convertir escenarios causales en crisis ocurridas. Después, los capítulos emplean los códigos para marcar afirmaciones concretas y el apéndice D reproduce el Registro como una matriz extensa.

El ejemplo más directo es `LIM-001`. En el estudio demográfico, 0.6 escribe que los 26 *avitadores* no son una cifra de población individual, que los ocho residentes no deben sumarse a ellos y que no consta el total de habitantes; cierra ese pasaje con `[L: LIM-001]`. El apéndice D permite buscar `LIM-001` y encontrar la formulación «No consta población total por individuos» y su consecuencia: R21 ofrece categorías fiscales y residentes, no un censo de almas. En la prosa cercana, otras marcas separan el contexto externo de la inferencia (`[E/I: DEM-005; LIM-001]`) o combinan dato y límite (`[D/L: ...]`). Así, el código ayuda a distinguir clases de afirmación, conservar cautelas y localizar el fundamento.

La utilidad tiene límites prácticos: la etiqueta queda como texto, no como ancla clicable al apéndice; hay que ir al apéndice D y buscar el ID (en la copia digital puede usarse la búsqueda de texto del lector PDF). Una marca agrupada al final de un párrafo tampoco identifica necesariamente qué código respalda cada oración cuando allí se reúnen varias afirmaciones. Aun así, el Registro íntegro ofrece una ruta de auditoría concreta, más rica que una mera clave: entrada, formulación admitida, evidencia/localizador y estado o cautela.

### Uso efectivo en Quarto

La captura aportada corresponde al apartado 4.4 del capítulo 4, que explica correctamente los cinco tipos y afirma que las letras conservan «la procedencia y el grado de una afirmación». El mismo capítulo 4.5 presenta la cadena de trazabilidad imagen → unidad → transcripción/aparato → edición modernizada → Estudio → Registro, y dice que enlaces y anclas permiten recorrerla. También indica que las notas documentan decisiones y cautelas; sin embargo, no se encontraron notas a pie en los capítulos editoriales 1–11 (la única nota hallada está en el capítulo técnico de prueba). Estas frases describen el diseño pretendido, no prueban que cada mecanismo ya esté implementado.

En el cuerpo actual, las marcas sí están aplicadas de manera operativa en los capítulos 9–11: por ejemplo, en molinos `[D/C/L: HID-001, HID-002, HID-005, CAL-012, LIM-010]` acompaña una explicación que distingue el recuento de ruedas, la suma calculada y el número desconocido del venturero; las fórmulas hacen visibles los operandos del cálculo. En el capítulo 10, `[D/L: JUR-006, LIM-011]` acompaña el pasaje que separa el pago anual de alcabalas del título jurídico que no consta. Las combinaciones de letras son por párrafo y clasifican el contenido sin crear por sí solas una cita bibliográfica.

La práctica no está extendida a todos los capítulos. El caso de población muestra la diferencia con claridad: el capítulo 6 QMD formula en el cuerpo que 26 *avitadores* no son una población total, que no corresponde sumarles los ocho residentes y que faltan datos familiares; pero no coloca `[L: LIM-001]` junto al párrafo. El front matter sí incluye `LIM-001` en su lista `L`. Por tanto, allí el uso real del código es de control/procedencia del capítulo, no de señal visible para quien lee ese pasaje. Lo mismo ocurre en los capítulos 3 y 5, 7 y 8: hay IDs declarados, pero no marcas en el cuerpo.

Hay una excepción parcial relevante: el capítulo 9 enlaza al lector con un **aparato D/C/I/E/L prototipo**. La tabla del aparato-molinos presenta, para una selección de 13 IDs, nivel, formulación o regla, estado y cautela/límite, y permite volver al capítulo histórico. Esa salida realiza parte de la función del Registro y demuestra navegación en una sección concreta. Sin embargo, no es una matriz completa: no recoge todos los IDs del capítulo 9, no cubre los capítulos 3 y 5–8 o 10–11, y las marcas al final de los párrafos no enlazan directamente con las filas correspondientes. El lector llega al fragmento mediante un enlace expreso al final del capítulo 9, no siguiendo cada código.

El control automático también tiene un alcance específico. El validador compara el inventario YAML con la lista esperada para cada capítulo y verifica que los IDs existan en el Registro. No comprueba que cada afirmación del cuerpo tenga su marca, que el ID adjunto sea la categoría semánticamente correcta ni que cada marca visible resuelva a una fila enlazada. En consecuencia, el front matter es útil para el equipo y las pruebas, pero permanece oculto en la salida de lectura; no debe presentarse como equivalente funcional a una anotación visible junto al pasaje.

### Comparación práctica

| Pregunta del lector/editor | PDF 0.6 | Quarto actual |
|------------------------|------------------------|------------------------|
| ¿Qué tipo de afirmación se está haciendo? | La marca visible D/C/I/E/L indica una o varias clases al cierre del pasaje; la guía metodológica define las categorías. | Lo indican las marcas visibles de los capítulos 9–11. En capítulos 3 y 5–8, el inventario existe solo en YAML y no se ve en el pasaje. |
| ¿Cuál es el fundamento o límite concreto? | Buscar el ID en el apéndice D, que reproduce el Registro completo con formulación, evidencia/localizador, estado y cautela. | En general, el ID queda como texto visible en los capítulos 9–11, sin enlace individual al Registro. El aparato de molinos resuelve solo una selección de IDs del capítulo 9. |
| ¿Se conserva el cálculo? | El código puede llevar a un `CAL-*`; el texto o el Registro declara la operación. La etiqueta sola no sustituye operandos ni regla. | En los capítulos 9–11 se muestra la operación en prosa/fórmula y se adjuntan IDs `CAL-*`; el inventario YAML también registra esos IDs. |
| ¿Puede seguirse digitalmente la cadena? | Las marcas al Registro requieren búsqueda manual; enlaces bibliográficos externos son un mecanismo separado. | Hay enlaces internos entre capítulos y entre el capítulo 9 y sus vistas/aparato. La cadena no se implementa aún para cada marca o entrada de evidencia. |

La afirmación del capítulo 4.5 de que «los enlaces y las anclas permiten recorrer esa cadena» está respaldada para algunas relaciones editoriales y el prototipo de molinos, pero sería demasiado amplia si se interpreta como navegación completa desde todas las marcas D/C/I/E/L hasta sus entradas del Registro. El sistema Quarto que se ve hoy es híbrido: **guía conceptual completa, inventario de IDs controlado para varios capítulos, anotación visible concentrada en los capítulos 9–11 y un aparato parcial enlazado desde el capítulo 9**.

## Referencias: qué enseña el ejemplo de la página 15

La captura proporcionada muestra la página 15 del capítulo 3 de 0.6. Tras dos párrafos sobre testimonios de 1831, 1836 y 1848, el uso actual de `Sorrios` y la serie histórica `Sorribios` / `Sorribos` / `Sorrios`, aparecen marcas como `[E: TOP-009–TOP-011]` e `[I/L: TOP-002, TOP-003]`. A continuación se lee **«Fuentes externas»** y una relación de referencias que incluye, entre otros:

-   Cristina Jular Pérez-Alfaro, título de un estudio sobre tenentes, merinos y poder señorial/regio;
-   la edición de un documento de 1267 con referencia archivística `AHN, Clero, carp. 828, núm. 11`;
-   un nobiliario, un pleito de 1715 en PARES, una relación parroquial de 1768, la *Gaceta de Madrid* de 1864, un estudio de Fernando Álvarez-Balbuena García y la página del Ayuntamiento.

El PDF ofrece siete anotaciones URL en esa página; `pdfinfo -url` encontró 154 anotaciones URL en todo el documento (repeticiones incluidas). Los hipervínculos conducen a los recursos citados. En cambio, las marcas D/C/I/E/L del pasaje siguen siendo referencias textuales al Registro: no se detectó que cada una sea un hipervínculo a su entrada.

Este ejemplo **no demuestra que el pasaje use notas a pie**. Es una relación bibliográfica de sección colocada inmediatamente después de los párrafos a los que da soporte. Su fortaleza es la proximidad y visibilidad: el lector encuentra autor/título o descripción documental y puede abrir los enlaces sin depender exclusivamente de un apéndice distante. No siempre es una cita normalizada autor-fecha y la asociación entre cada fuente y cada frase puede seguir requiriendo interpretación; la lista y el Registro deben coordinarse.

En Quarto, [references.bib](../publication/references.bib) contiene solamente un comentario de que la bibliografía se incorporará en fases posteriores y tiene cero entradas. La configuración [\_quarto.yml](../publication/_quarto.yml) sí declara ese archivo como bibliografía. En los capítulos 1–11 no se encontraron claves de cita `[@…]` ni notas a pie; el único ejemplo de nota a pie localizado pertenece a [00-prueba-tecnica.qmd](../publication/content/00-preliminares/00-prueba-tecnica.qmd) y es explícitamente técnico. Sí hay **nueve URL externas enlazadas** en los capítulos 1 y 2 (recursos de PARES y del Catastro). Son enlaces útiles, pero no constituyen todavía una bibliografía coherente de la obra: no van acompañados de una clave/cita formal y se concentran en la introducción. En particular, los pasajes históricos del capítulo 3 y varios contextos externos de los capítulos 5–11 carecen de referencias externas visibles junto a las afirmaciones, aunque algunos identificadores E y las fuentes internas estén declarados en YAML.

### Balance de referencias

-   **0.6 es más sólido en referencias visibles al lector** en el ejemplo toponímico y en la distribución de enlaces externos por el PDF.
-   **Quarto tiene procedencia declarada y validable**: los campos `sources:` identifican archivos internos y localizadores; `evidence:` declara IDs del Registro y el validador comprueba las listas y la existencia de IDs. El aparato prototipo de molinos hace legible y navegable una selección de entradas.
-   **La debilidad actual de Quarto es la falta de cobertura y resolución general**, no la ausencia absoluta de uso. El lector no ve el YAML como aparato, no encuentra citas bibliográficas normalizadas ni una bibliografía completa en el `.bib`; los códigos visibles del cuerpo no tienen destino individual en el Registro.
-   **El PDF 0.6 tampoco resuelve todo automáticamente**: las marcas D/C/I/E/L requieren ir al Registro/apéndice y la relación entre un código y una fuente bibliográfica puede no ser evidente sin consultar la entrada completa. Sus URLs activas no convierten los códigos en enlaces.

## Otros hallazgos de la comparación inicial

### Cartografía

En 0.6 se observaron dos mapas: una lámina de localización regional/provincial y otra de detalle local que sitúa Sorribos/Sorrios respecto de Tapia de la Ribera, Villapodambre, Santibáñez de Ordás y Rioseco de Tapia. En el árbol `publication/assets/` no se encontraron archivos; en los capítulos QMD actuales no se encontraron figuras cartográficas. El texto de Quarto incluso advierte que no se debe deducir un mapa más preciso del que permite el documento, lo cual es una cautela adecuada, pero no sustituye una cartografía editorial de orientación.

La reincorporación debe pasar por la política de assets del proyecto: procedencia, fecha, escala, base cartográfica, transformación, leyenda y separación entre localización documentada e interpretación. La ausencia actual es coherente con que preliminares/cartografía y recursos gráficos estén previstos en el plan, no autoriza a reutilizar sin control una imagen antigua.

### Historia del topónimo

Quarto conserva una formulación históricamente prudente: distingue `Sorribios` medieval, `Sorribos` moderno y `Sorrios` actual; afirma la continuidad de identificación con cautela alta y niega que se disponga de una secuencia fonética completa. Esa disciplina debe conservarse.

La composición 0.6 resulta más verificable para el público en la página ilustrada porque acompaña ese relato con referencias externas identificables y enlaces. En Quarto, las fuentes del front matter del capítulo 3 son principalmente documentos internos del proyecto y Registro; no equivalen a la lista externa visible del PDF. Una mejora debería enlazar las entradas E del capítulo con referencias bibliográficas pertinentes, conservando la autoridad del Estudio y el Registro frente a cualquier discrepancia externa.

### Autoría y créditos

La observación inicial de que «ninguno menciona al autor» se mantiene en lo sustancial, con un matiz: los metadatos del PDF 0.6 sí declaran como autor al «Proyecto Sorríos - Catastro de Ensenada», pero no identifican a una persona. El PDF Quarto local tiene campo `Author` vacío. Ninguna versión consultada ofrece un crédito personal inequívoco ni un bloque de responsabilidades editoriales suficientemente explícito. Conviene decidir e incorporar autoría, edición, transcripción, institución y fecha de versión solo con metadatos comprobados y autorización editorial; no inferirlos.

### Estado de desarrollo y aspectos técnicos

-   El [roadmap](./ESTADO_PUBLICACION_QUARTO.md) deja la fase 3J (capítulo 11) como siguiente, pero el checkout local contiene ya un QMD 11 sin seguimiento y un render de 68 páginas que lo incluye. Debe evitarse presentar ese estado local como publicación o como roadmap actualizado.
-   El PDF Quarto observado tiene 68 páginas y tamaño Letter (`612 × 792 pt`); el 0.6 tiene 259 páginas y tamaño A4 (`595.276 × 841.89 pt`). La decisión final de formato corresponde al diseño editorial; el tamaño no debe cambiarse solo por imitación.
-   El HTML Quarto declara `lang="en"` a pesar de que el contenido es español. Es un aspecto de metadatos/accesibilidad que conviene corregir antes de publicación.
-   El capítulo técnico [00-prueba-tecnica.qmd](../publication/content/00-preliminares/00-prueba-tecnica.qmd) sigue apareciendo en la configuración/render local. Debe retirarse o mantenerse fuera de la edición pública conforme a la fase y al control de regresión establecido.
-   El render de 68 páginas se trata aquí solo como evidencia del checkout observado. `_book/` es derivado regenerable y no autoridad editorial.

## Valoración y prioridades editoriales

### Qué conservar o aprovechar de 0.6

1.  La cobertura integrada del libro y la navegación entre estudio, documento y aparatos.
2.  La cartografía orientativa, tras verificar procedencia, datos cartográficos, licencias y límites de representación.
3.  La práctica de colocar una relación visible de fuentes externas cerca del pasaje histórico al que sirve, con enlaces activos y datos bibliográficos suficientes.
4.  La presentación visible y relativamente consistente de marcas D/C/I/E/L en el estudio histórico, sin confundirlas con notas a pie ni con hipervínculos.

### Qué conservar o aprovechar de Quarto

1.  La arquitectura que separa el workspace canónico `project/`, el texto editorial `publication/content/` y los derivados regenerables.
2.  La distinción rigurosa entre dato, cálculo, interpretación, contexto externo y límite, especialmente en los capítulos 5–11, donde las etiquetas visibles acompañan los razonamientos.
3.  La declaración de fuentes y de identificadores en metadatos, y su comprobación automatizada.
4.  La cautela frente a equivalencias no documentadas, agregaciones y causalidades, así como la orientación a generar matriz, facsímil, transcripción, modernizada e índices desde fuentes canónicas.
5.  Los enlaces internos y externos que ya funcionan en los capítulos iniciales.

### Mejoras recomendadas para ambos

1.  Definir una política editorial clara de citas, bibliografía y notas: qué requiere llamada en el cuerpo, cuándo procede nota, cómo se representa archivo/folio y cómo se presenta bibliografía web; evitar que una lista de URLs sin contexto sustituya una referencia completa.
2.  Mantener alineados los identificadores D/C/I/E/L, las entradas del Registro y la bibliografía: toda marca debe conducir a una explicación localizable y toda fuente E debe poder identificarse sin búsquedas ambiguas. Distinguir además el control interno de front matter de la función de lectura de una marca impresa.
3.  Revisar la correspondencia de cada fuente externa con afirmaciones concretas; que una bibliografía aparezca cerca no prueba automáticamente qué frase respalda.
4.  Acreditar autoría y responsabilidades editoriales con información confirmada.
5.  Revisar mapas y figuras con metadatos de procedencia y una leyenda que no prometa más precisión de la permitida por la fuente.
6.  Preservar las cuatro formas de acceso definidas para el libro: facsímil, transcripción paleográfica y aparato, edición modernizada e interpretación histórica.

### Próximo paso editorial recomendado

Al completar el aparato previsto por el roadmap, tratar la salida visible de trazabilidad como requisito de lectura y no solo como control de build: desde una marca o una referencia externa debe poder alcanzarse el registro o la cita pertinente en HTML y encontrarse fácilmente en PDF. La implementación debe respetar el plan, la generación determinista y la autoridad del Registro; este informe no prescribe un filtro o una infraestructura particular.

## Referencias de comprobación dentro del repositorio

-   [Plan maestro de publicación Quarto](./PLAN_MAESTRO_PUBLICACION_QUARTO.md): arquitectura, criterios D/C/I/E/L, aparatos previstos y auditoría de la composición 0.6.
-   [Estado de publicación Quarto](./ESTADO_PUBLICACION_QUARTO.md): fase y siguiente tarea declarada.
-   [Instrucciones de publicación](../.github/instructions/publication.instructions.md): autoridades, metadatos, validación y política de assets.
-   [README de publicación](../publication/README.md): entradas, derivados y comandos.
-   [Registro de afirmaciones y cálculos v1.2](../project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md): autoridad del aparato D/C/I/E/L.
-   [Configuración Quarto](../publication/_quarto.yml): capítulos, bibliografía y render.
-   [Bibliografía BibTeX actual](../publication/references.bib): archivo actualmente vacío salvo comentario.
-   [Capítulo 3 QMD](../publication/content/01-catastro/03-expediente-sorribos-santibanez.qmd): tratamiento Quarto del expediente y topónimo.
-   [Capítulo 4 QMD](../publication/content/01-catastro/04-manuscrito-volumen-actual.qmd): explicación de D/C/I/E/L y de la cadena de trazabilidad.
-   [Capítulo 6 QMD](../publication/content/02-estudio/06-vecinos-hogares-viviendas-trabajo.qmd): ejemplo de cautela sobre vecinos, avitadores, residentes y población.
-   [Capítulo 9 QMD](../publication/content/02-estudio/09-rio-molinos-recursos.qmd): marcas visibles y enlace al aparato prototipo.
-   [Aparato de molinos QMD](../publication/generated/aparato-molinos.qmd): tabla parcial D/C/I/E/L del prototipo.
-   [Validador de publicación](../publication/scripts/validate_publication.py): comprobaciones de `sources`, `evidence` e identificadores.

**Nota de integridad:** las capturas de la página 15 del PDF 0.6 y del apartado 4.4 de Quarto fueron proporcionadas para esta comparación y no se copian a `docs/`. La composición 0.6 permanece fuera del checkout y no debe añadirse al repositorio.
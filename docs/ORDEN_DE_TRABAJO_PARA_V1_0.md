Con esta ronda ya podemos hacer una **consolidación bastante más completa**. Mi conclusión principal cambia respecto a la matriz 6A.1: ya no estamos ante cuatro bloqueantes y unas mejoras menores, sino ante una candidata técnicamente madura a la que todavía le falta una **última fase editorial sustantiva** antes de poder llamarla 1.0.

No tocaría todavía la candidata. Primero cerraría el mapa de decisiones y, en algunos puntos, haría auditorías específicas antes de decidir la solución.

## 1. Lo que muestran además las dos capturas

Las dos observaciones visuales son defectos reales, no preferencias.

En el índice general del PDF, numeraciones largas como `16.35`, `16.36`, etc. quedan pegadas al título —`16.35Respuesta 33...`—. Hay que corregir la composición del TOC PDF dando anchura/separación suficiente al número. Lo clasificaría como **bloqueante técnico de 1.0**, aunque sea fácil de solucionar.

En los índices, el problema también es real. El generador produce cada elemento como `.index-entry`, y el CSS HTML le da margen, padding y un filete. Pero el preámbulo LaTeX no tiene un tratamiento equivalente: por eso el PDF concatena visualmente una entrada con la siguiente. La captura del onomástico lo deja muy claro. Esto afecta previsiblemente a todos los índices con el mismo patrón. También lo consideraría **defecto de composición que hay que corregir antes de 1.0**.

Y he comprobado algo adicional sobre tu observación del orden alfabético: los **nueve índices sí tienen orden controlado por el generador** —los alfabéticos se ordenan mediante una clave Unicode determinista y el de preguntas/respuestas es deliberadamente numérico—. El **glosario, en cambio, no se ordena**: `build_apparatus.py` conserva el orden de `Glosario.md`. El Plan de composición especificaba expresamente «orden alfabético». Por tanto, aquí sí tenemos una desviación concreta que debe corregirse.

---

# 2. Consolidación de las REV-001–012 existentes

No eliminaría sus IDs, pero revisaría su interpretación.

| ID | Tema | Valoración consolidada |
|---|---|---|
| **REV-001** | Identidad, créditos, metadatos | **B**. Hay que descomponer internamente. `0.1.0-dev`, `development` y «Edición en desarrollo» no pueden llegar a 1.0. Autoría/responsabilidad, fecha, licencia, copyright, etc. requieren decisiones explícitas. |
| **REV-002** | Cartografía | **B**. Se refuerza. No solo estaba en 0.6: el Plan 0.5 y el índice rector la exigen explícitamente y con función editorial concreta. |
| **REV-003** | Fuentes y bibliografía | **B**. Se mantiene. El problema es de sistema de referencias para el lector, no de número bruto de URLs. |
| **REV-004** | Cuestiones abiertas, versiones, modelos de cita | **B**, pero debe descomponerse funcionalmente. No tienen necesariamente que ser tres grandes apéndices, pero sus funciones están prometidas y no están resueltas. |
| **REV-005** | Preliminares | Pasa de **M a B editorial**, a la luz de tus observaciones sobre prólogo, introducción y apertura. |
| **REV-006** | D/C/I/E/L navegable | **M**. Muy conveniente para 1.0, pero no invalida el sistema actual. |
| **REV-007** | Colofón | **M**, probablemente absorbible por REV-001/004. |
| **REV-008** | PDF/UA/PDF-A | **F**. 1.1+. |
| **REV-009** | Formulaciones antiguas superadas | **N**. Confirmado. |
| **REV-010** | Modelo de facsímil 0.6 | Ya no basta con **N**. No hay que volver al modelo 0.6, pero tu observación revela un problema diferente: la duplicación 18 páginas + 35 recortes debe revisarse. Lo separaría en una nueva REV. |
| **REV-011** | Índices antiguos | **N** respecto a recuperar 0.6. Pero aparecen nuevos defectos de composición de los índices actuales que requieren REV propias. |
| **REV-012** | A4/diseño 0.6 | **N** respecto a imitar 0.6. Mantendría abierta únicamente la cuestión futura de impresión si fuese relevante. |

---

# 3. Nuevas observaciones del usuario consolidadas

Manteniendo los IDs anteriores, propondría añadir las siguientes entradas a partir de `REV-013`.

### REV-013 — Prólogo personal

**Origen:** observación del usuario.  
**Clasificación propuesta:** **B editorial para 1.0**.

No porque todo libro necesite prólogo, sino porque tú has identificado una función importante que quieres incorporar: explicar el origen del proyecto, sus circunstancias y las personas vinculadas.

Debe ser claramente un texto personal, separado del aparato histórico. Mi recomendación sería que lo escribas tú; podemos ayudarte después a revisarlo editorialmente sin borrar tu voz.

---

### REV-014 — Introducción y guía de lectura del volumen

**Clasificación:** **B**.

Un volumen de más de 300 páginas, con estudio, facsímil, paleografía, modernizada, aparatos e índices necesita explicar al principio:

- qué contiene;
- por qué existe cada parte;
- cómo se relacionan;
- cómo puede leerse;
- qué diferencia hay entre fuente, transcripción, modernización e interpretación;
- posibles itinerarios de lectura.

Esto absorbe una parte importante del antiguo `REV-005`.

---

### REV-015 — Apertura/portada editorial actual

**Clasificación:** **B**.

El actual `index.qmd` sigue siendo prácticamente una página de prepublicación:

> «Esta edición digital se encuentra en desarrollo…»

y termina diciendo que sigue en estado de prepublicación.

Eso debe sustituirse por una auténtica apertura de libro coordinada con:

- título;
- subtítulo;
- prólogo;
- introducción;
- créditos;
- edición.

Se solapa con `REV-001`, pero conviene identificar expresamente la pieza editorial.

---

### REV-016 — Duplicación funcional del manuscrito

**Clasificación:** **B de decisión**, no necesariamente B de cambio.

La Parte III presenta 18 páginas completas y la IV vuelve a mostrar 35 recortes. La segunda reproducción tiene justificación para el cotejo paleográfico, pero en PDF produce sensación real de repetición y aumenta mucho el volumen.

Hay que decidir conscientemente entre al menos:

1. conservar ambas en HTML y PDF;
2. conservar imagen junto a transcripción en HTML, pero reducirla/eliminarla en PDF;
3. mantener en PDF solo miniatura o referencia al facsímil;
4. otra integración que preserve el cotejo sin duplicación excesiva.

**No decidiría todavía la solución.**

---

### REV-017 — Macroorden del libro: estudio antes o después del documento

**Clasificación:** **B de decisión arquitectónica**.

No porque el orden actual sea incorrecto. De hecho, está expresamente fijado por el índice rector:

> contexto → estudio histórico → facsímil → transcripción → edición modernizada → aparatos.

Y es un modelo perfectamente defendible para una edición con estudio introductorio.

Pero tu duda es sustantiva: el lector recibe la interpretación completa antes de encontrar sistemáticamente la fuente.

Hay que decidir antes de congelar 1.0 entre:

- mantener el modelo actual;
- trasladar documento/transcripción/modernizada antes del estudio;
- mantener el orden pero explicar claramente dos rutas de lectura en la introducción.

Mi inclinación provisional es **no reordenar todavía** y comprobar primero si una buena introducción con rutas de lectura resuelve el problema. Reordenar afectaría a capítulos, referencias, índices, páginas y narrativa.

---

### REV-018 — Navegación HTML inicialmente demasiado desplegada

**Clasificación:** **M alta / incluir en 1.0**.

Es una mejora pequeña y muy rentable. Con seis partes y treinta páginas HTML, parece más adecuado mostrar inicialmente las partes y permitir desplegarlas.

No tiene implicaciones históricas.

---

### REV-019 — Convención de cierre de capítulos

**Clasificación:** **M**.

La inspección muestra que los capítulos 5–13 sí poseen todos algún cierre, pero solo 9–12 lo llaman literalmente «Síntesis».

No creo que la solución sea necesariamente poner `Síntesis` en todos. De hecho, títulos como:

- «Una estructura visible y sus límites»;
- «Un sistema agrario desigual y mensurable con cautela»;
- «Una economía rural relacionada, no cerrada»

son mejores que un genérico «Síntesis».

Recomendaría **uniformidad funcional**, no uniformidad literal: todos deberían tener un cierre reconocible, preferentemente con un título significativo.

---

### REV-020 — Función del glosario y contexto histórico insuficiente

**Clasificación:** **B de auditoría previa**.

Esta es más importante de lo que parecía.

El glosario actual cumple exactamente su especificación canónica: define el término **en el expediente** y evita deliberadamente interpretación histórica extensa. Por eso *Señorío* no explica qué era históricamente un señorío.

Antes de modificarlo hay que hacer una auditoría aguas arriba:

1. ¿Qué contexto histórico existe ya en `Estudio_Historico.md`?
2. ¿Qué términos están suficientemente explicados allí?
3. ¿Qué términos no lo están?
4. ¿Qué carencias exigirían investigación histórica adicional con el plugin?
5. ¿Qué parte del nuevo conocimiento debe quedar en el Estudio y qué síntesis breve debe llegar al glosario?

Solo después podremos decidir entre:

- enriquecer el **Glosario histórico**;
- mantener el actual como **Glosario documental** y crear otra capa contextual;
- una solución híbrida.

Y cualquier nueva investigación histórica deberá propagarse, cuando corresponda, a estudio, registro, capítulos, bibliografía, glosario e índices. No se modifica solo el glosario.

---

### REV-021 — Gráficos, esquemas y recuadros explicativos

**Clasificación:** **B de auditoría y selección**.

La auditoría 6A.1 infravaloró este punto.

El Plan de composición 0.5 preveía explícitamente, entre otros:

- cronología visual;
- esquema Concejo histórico / municipio posterior;
- cuadro de categorías demográficas;
- recuadro metrológico;
- recuadros agrarios;
- ganado y molinos;
- instituciones y hacienda;
- tabla de mínimos monetarios;
- diagrama del modelo integrado de vulnerabilidad;
- ocho tipos de recuadros históricos.

Y establecía una regla sensata:

> gráficos limitados a relaciones que no resulten claras en una tabla.

Hay que hacer un inventario específico:

**0.6 + Plan 0.5 + candidata actual → conservar / reconstruir / descartar.**

No deberíamos reinstaurar gráficos que representen inferencias ya superadas.

---

### REV-022 — Estado «Edición en desarrollo»

**Clasificación:** **B**, aunque conceptualmente depende de `REV-001/015`.

Debe desaparecer de:

- subtítulo;
- metadata;
- portada;
- cualquier texto visible,

al constituir 1.0.

No hace falta mantener una REV independiente si luego consolidamos la implementación bajo `REV-001`.

---

### REV-023 — Numeración pegada a títulos en el índice general PDF

**Clasificación:** **B técnico**.

La captura demuestra un defecto visible:

`16.35Respuesta 32...`

Debe corregirse la anchura/espaciado del número de sección en el TOC PDF y probar expresamente los casos largos de capítulo 16.

---

### REV-024 — Orden alfabético del glosario

**Clasificación:** **B técnico/editorial**.

El Plan 0.5 especifica expresamente:

> glosario — orden alfabético.

El generador actual no ordena el glosario: respeta el orden de `Glosario.md`.

Debe corregirse, preferiblemente **en el generador**, sin alterar innecesariamente la fuente canónica.

Los índices especializados ya aplican ordenación determinista. El índice de preguntas/respuestas debe seguir siendo numérico.

---

### REV-025 — Separación visual de entradas de los índices PDF

**Clasificación:** **B técnico**.

La segunda captura demuestra que una entrada termina y la siguiente comienza sin suficiente separación.

El HTML ya dispone de estilo `.index-entry`; el PDF carece del equivalente LaTeX. Hay que diseñar una composición PDF consistente:

- separación vertical;
- jerarquía término/campos;
- evitar cortes malos;
- quizá sangrado/filete si resulta sobrio.

Debe comprobarse en los nueve índices.

---

### REV-026 — Peso del PDF y bundle web

**Origen:** revisión conjunta anterior.  
**Clasificación:** **M**.

PDF actual: ~74 MB frente a ~6,8 MB en 0.6.

Eso no indica un defecto documental: procede en buena parte de las imágenes de manuscrito. Pero antes del despliegue web conviene comprobar si puede reducirse significativamente **sin perder calidad útil**.

No optimizar a costa de la paleografía.

---

# 4. Una regla transversal nueva: investigación histórica → propagación

Tu comentario de que «probablemente nuevos estudios históricos tengan más implicaciones en el libro» es correcto y merece quedar como **regla del proceso**, no simplemente como otra REV.

Si al auditar el glosario descubrimos una carencia histórica y hacemos nueva investigación mediante el plugin, la secuencia correcta debería ser:

**investigación**
→ **fuente canónica correspondiente**
→ **Estudio Histórico**
→ **Registro D/C/I/E/L si procede**
→ **glosario**
→ **capítulos afectados**
→ **fuentes/bibliografía**
→ **índices**
→ **regeneración Quarto**.

Nunca:

**investigación nueva → parche directo en el glosario Quarto**.

---

# 5. Cómo queda ahora el mapa completo

Agruparía las 26 REV en ocho paquetes de decisión.

### A. Identidad y apertura del libro — resolver para 1.0

`REV-001`, `005`, `007`, `013`, `014`, `015`, `022`

Incluye:

- identidad de edición;
- título/subtítulo;
- créditos;
- prólogo;
- introducción;
- orientación;
- eventualmente colofón.

Este es un **paquete B**.

---

### B. Arquitectura del volumen — decisión antes de modificar

`REV-016`, `017`

Dos decisiones grandes:

- duplicación facsímil/transcripción;
- orden estudio/documento.

No deben implementarse hasta decidir el modelo editorial.

---

### C. Investigación y contexto histórico — auditoría antes de decidir

`REV-003`, `004`, `020` y parte de `021`

Incluye:

- fuentes/bibliografía;
- cuestiones abiertas;
- contexto del glosario;
- posible nueva investigación;
- propagación de resultados.

---

### D. Orientación visual — auditar y seleccionar para 1.0

`REV-002`, `021`

- mapas;
- cronología visual si procede;
- gráficos;
- esquemas;
- recuadros.

No recuperar mecánicamente 0.6.

---

### E. Trazabilidad y ayudas de consulta

`REV-006`, `024`

- navegación D/C/I/E/L;
- glosario correctamente ordenado.

---

### F. UX y composición

`REV-018`, `019`, `023`, `025`, `026`

- sidebar HTML;
- cierres de capítulos;
- TOC PDF;
- espaciado de índices;
- peso de salidas.

`REV-023` y `025` son defectos claros que yo corregiría sí o sí antes de 1.0.

---

### G. Trabajo futuro

`REV-008`

- PDF/UA;
- PDF/A;
- certificación formal de accesibilidad.

1.1+.

---

### H. Decisiones negativas ya muy sólidas

`REV-009`, `010`, `011`, `012`

Pero con una precisión:

- no recuperar formulaciones superadas;
- no volver al facsímil de 0.6;
- no recuperar índices provisionales;
- no copiar la maqueta de 0.6.

Esto **no impide** resolver `REV-016` sobre cómo mostrar las imágenes ni mejorar el diseño Quarto.

---

# 6. Qué considero ahora realmente bloqueante para 1.0

No interpretaría «B» como «hay que implementar exactamente lo propuesto», sino como «hay que resolver esta cuestión antes de publicar».

Veo cinco bloques reales:

1. **Apertura e identidad editorial.**
   Prólogo, introducción, portada/landing, créditos, metadata y cierre.

2. **Arquitectura de lectura.**
   Resolver orden estudio/documento y repetición facsímil/transcripción.

3. **Aparato histórico y documental.**
   Bibliografía/fuentes, cuestiones abiertas/modelos de cita y auditoría del glosario.

4. **Orientación visual.**
   Cartografía y auditoría de gráficos/recuadros previstos.

5. **Defectos finales de composición.**
   TOC PDF, glosario alfabético e índices PDF.

Todo lo demás puede resolverse después o dentro de esos bloques.

---

# 7. Orden de trabajo que recomiendo ahora

Ahora que has cerrado tu ronda de observaciones, **ya no seguiría modificando la matriz a ciegas ni empezaría a programar**.

Haría exactamente esto:

**Paso 1 — fijar esta consolidación en la documentación, sin tocar la candidata.**  
Actualizar `REVISION_EDITORIAL_CANDIDATA_1_0.md` para incorporar `REV-013`–`026`, las reclasificaciones y los cinco paquetes anteriores.

**Paso 2 — resolver primero las decisiones puramente editoriales**, sin investigación:
- prólogo;
- introducción;
- orden general;
- duplicación de imágenes;
- modelo de preliminares;
- cierre/síntesis;
- navegación HTML.

**Paso 3 — hacer tres auditorías específicas, todavía sin modificar el libro:**
- auditoría histórica del glosario/Estudio con el plugin;
- inventario de gráficos/recuadros/mapas 0.6 + Plan 0.5 + Quarto;
- auditoría de fuentes/bibliografía/aparatos narrativos.

**Paso 4 — tomar contigo las decisiones definitivas 1.0 / 1.1 / no incorporar.**

**Paso 5 — solo entonces preparar el plan de implementación de la nueva candidata.**

Creo que el **siguiente movimiento concreto** debería ser precisamente el Paso 1: preparar un prompt para que el agente **actualice únicamente la documentación de revisión** con esta consolidación, sin tocar `publication/` ni `project/`. Después podremos empezar por las decisiones editoriales y las tres auditorías especializadas.
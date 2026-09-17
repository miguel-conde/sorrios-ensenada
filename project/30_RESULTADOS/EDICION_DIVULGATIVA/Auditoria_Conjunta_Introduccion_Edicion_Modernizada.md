# Auditoría conjunta de la introducción y la edición modernizada

**Documentos auditados:**

- `project/30_RESULTADOS/EDICION_DIVULGATIVA/Introduccion_Catastro_Ensenada_Sorrios.md`, versión 1.0.
- `project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md`, versión 1.0.

**Fecha:** 17 de septiembre de 2026  
**Base Git:** `main@55cdb843e0c7c105d1109252b0ddc8ecd87ec971`  
**Autoridad textual local:** Edición Crítica v3.5  
**Autoridades auxiliares:** interrogatorio verificado, criterios de la edición modernizada, glosario e índices validados  
**Carácter:** auditoría; no introduce correcciones  
**Dictamen:** APTO CON CORRECCIONES PREVIAS PARA SU INTEGRACIÓN EN UN VOLUMEN

## 1. Objeto y alcance

La auditoría comprueba si la introducción y la edición modernizada pueden leerse conjuntamente sin contradicciones, pérdidas de trazabilidad, cambios semánticos inadvertidos o duplicaciones innecesarias. No vuelve a editar el manuscrito y no modifica ninguno de los documentos auditados.

Se revisan cinco dimensiones:

1. cobertura y estructura;
2. correspondencia entre las cuarenta preguntas y respuestas;
3. fidelidad de la modernización al texto local;
4. coherencia terminológica y onomástica;
5. preparación para un futuro volumen de lectura.

## 2. Jerarquía de control

| Materia | Autoridad empleada |
|---|---|
| Lectura del documento local | Edición Crítica v3.5 |
| Identidad, secuencia y materialidad | proyecto.yaml, estado.yaml y unidades.yaml |
| Criterio de modernización | Criterios_Edicion_Modernizada.md |
| Enunciados del formulario | Verificacion_Interrogatorio_40_Preguntas.md y sus fuentes institucionales |
| Términos históricos | Glosario.md |
| Personas y variantes de nombre | Indice_Personas.md |
| Medidas | Indice_Medidas.md |
| Estado técnico | Git y controles del proyecto |

## 3. Resultado estructural

| Comprobación | Resultado |
|---|---:|
| Estado del proyecto | clean |
| Unidades declaradas | 35 |
| Unidades presentes en la Edición Crítica | 35 |
| Unidades representadas en la edición modernizada | 35 |
| Respuestas modernizadas | 40 |
| Secuencia de respuestas | 1–40, sin saltos |
| Preguntas de la introducción | 40 |
| Secuencia de preguntas | 1–40, sin saltos |
| Notas llamadas en la edición modernizada | 35 |
| Notas definidas | 35 |
| Referencias de nota huérfanas | 0 |
| PDF incorporado al repositorio | No |
| Operación incompleta | No |

No se detectan pérdidas de respuestas, folios, cierre, firmas ni hojas en blanco. La correspondencia numérica entre pregunta y respuesta es completa.

## 4. Resumen de hallazgos

| Severidad | Número |
|---|---:|
| Alta | 2 |
| Media | 5 |
| Baja | 2 |
| Total | 9 |

Las incidencias altas no invalidan el uso separado de los documentos, pero deben resolverse antes de integrarlos en un volumen destinado al público general.

## 5. Hallazgos de severidad alta

### AC-01. La introducción presenta como modernización ortográfica lo que en varios casos es una paráfrasis

**Evidencia**

La introducción afirma que la lista «moderniza ortografía y puntuación». El informe de verificación añade que se conserva el formulario sin «paráfrasis económicas o explicaciones insertadas dentro del enunciado».

Sin embargo, varios enunciados han sido resumidos o reformulados:

- la pregunta 3 condensa la formulación sobre extensión, circunferencia por horas y leguas, linderos y figura;
- la 4 convierte una enumeración y sus condiciones productivas en una formulación sintética;
- la 9 reorganiza la relación entre medidas, varas y simiente;
- la 18 añade «o establecimiento de esquileo»;
- las 24 y 33 condensan cláusulas del formulario.

Las reformulaciones son comprensibles y generalmente fieles al sentido, pero no son únicamente una actualización ortográfica.

**Riesgo**

El lector puede creer que está ante el tenor íntegro modernizado del impreso de 1749. Esto reduce la trazabilidad precisamente en el documento que debía acreditar los enunciados.

**Resolución propuesta**

Opción preferente: sustituir las cuarenta preguntas por una versión cercana al tenor completo de PARES, modernizando únicamente grafía, puntuación y concordancias transparentes.

Opción alternativa: mantener la redacción actual, pero denominarla «síntesis explicativa de las cuarenta preguntas» y añadir aparte el enunciado completo modernizado.

**Prioridad para el volumen:** obligatoria.

### AC-02. «Avitadores» se moderniza como «habitantes» y genera una categoría demográfica no segura

**Evidencia**

La Edición Crítica transcribe en el folio 318r:

> «diez, y ocho vecinos, y ocho medios vecinos, inclusas dos biudas, que componen veinte y seis avitadores, y ocho residentes».

La edición modernizada escribe:

> «dieciocho vecinos y ocho medios vecinos […] que componen veintiséis habitantes».

La introducción afirma después que el expediente distingue «vecinos, medios vecinos, residentes y habitantes».

El glosario, en cambio, mantiene prudentemente la forma documental `avitadores` y no fija una equivalencia jurídica o demográfica general.

**Riesgo**

«Habitantes» puede interpretarse como población total. Además, la cautela introductoria convierte la modernización en una supuesta categoría expresa del expediente. Esto entra en tensión con el Estudio Histórico, que evita estimar población total.

**Resolución propuesta**

Conservar una forma marcada, por ejemplo «veintiséis habitadores [en el original, avitadores]», o mantener `avitadores` con nota. La introducción debe enumerar las categorías documentales sin convertirlas en población total.

**Prioridad para el volumen:** obligatoria.

## 6. Hallazgos de severidad media

### AC-03. «Esquilmo» recibe dos explicaciones incompatibles

**Evidencia**

La pregunta 18 de la introducción dice:

> «¿Hay algún esquilmo o establecimiento de esquileo?»

La nota 22 de la edición modernizada define `esquilmo` como «producto o rendimiento del ganado», en consonancia con el glosario y con el uso de la respuesta 20.

**Riesgo**

La conjunción «o» presenta «esquilmo» y «establecimiento de esquileo» como equivalentes. El formulario y la respuesta combinan vocabulario de esquileo y rendimiento ganadero, pero el proyecto no ha validado esa equivalencia general.

**Resolución propuesta**

Restituir la formulación verificada de la pregunta 18 sin glosa insertada. Añadir, fuera del enunciado, una nota que explique la relación contextual entre esquileo y esquilmo en las respuestas 18 y 20.

### AC-04. La relación entre «renta» y «venta» en la pregunta y respuesta 40 no se explica

**Evidencia**

La pregunta 40 de la introducción pregunta por «alguna finca o renta». La Edición Crítica transcribe en la respuesta local `venta, ni finca alguna`, y la edición modernizada conserva «venta ni finca» sin nota.

El informe de verificación reconoce expresamente que la forma local `venta` no debe utilizarse para alterar el formulario general.

**Riesgo**

En lectura conjunta parece una contradicción o un error tipográfico no controlado.

**Resolución propuesta**

Mantener «venta» por fidelidad al manuscrito y añadir una nota: el interrogatorio general dice «renta», mientras que la copia local ofrece `venta`; no se emienda sin evidencia material adicional.

### AC-05. La variante Bega/Vega puede parecer una inconsistencia de identidad

**Evidencia**

La introducción identifica al cura como «don Manuel Antonio de Bega», según la comparecencia. La respuesta 15 de la edición modernizada lo llama «don Manuel Antonio de Vega». El Índice de personas confirma que ambas formas están documentadas para el mismo cura.

**Riesgo**

El lector no especializado puede entender que se trata de dos personas.

**Resolución propuesta**

Añadir en la primera aparición una nota breve: «Bega en la comparecencia; Vega en la respuesta 15». Mantener cada variante en su lugar documental.

### AC-06. «Cubrirlas» interpreta una expresión oscura sin advertencia

**Evidencia**

En la respuesta 20, la Edición Crítica conserva para las yeguas:

> «administrarse vnos años al contrario, y otros al natural».

La edición modernizada escribe:

> «Como lo habitual es cubrirlas unos años al contrario y otros al natural».

La sustitución de `administrarse` por «cubrirlas» ofrece una interpretación reproductiva plausible, apoyada por el contexto de mulas y potros, pero no está señalada como tal.

**Riesgo**

El criterio publicado limita la modernización a cambios transparentes y correcciones que no alteren el contenido. Aquí se resuelve semánticamente una expresión histórica.

**Resolución propuesta**

Conservar una formulación más próxima —«administrarlas unos años al contrario y otros al natural»— con nota explicativa, o mantener «cubrirlas» acompañado de una nota que documente la inferencia.

### AC-07. La puntuación de los propietarios de ruedas en la respuesta 17 es ambigua

**Evidencia**

La edición modernizada dice:

> «Marcos y Andrés Suárez, Margarita y Manuel García y Bartolomé Fernández».

La secuencia previa distingue a Marcos Suárez, Andrés Suárez, Margarita García, Manuel García y Bartolomé Fernández, con copropiedades diferentes.

**Riesgo**

La frase puede leerse como «Marcos y Andrés Suárez» y «Margarita y Manuel García», desdibujando apellidos y relaciones de propiedad.

**Resolución propuesta**

Separar inequívocamente los nombres mediante punto y coma:

> «Marcos Suárez; Andrés Suárez; Margarita García; Manuel García; y Bartolomé Fernández».

La modificación debe conservar la advertencia ya existente sobre el número de casas y el «otro don Manuel».

## 7. Hallazgos de severidad baja

### AC-08. Las referencias entre documentos no son navegables

**Evidencia**

La introducción menciona la Edición Crítica, el Estudio Histórico, la edición modernizada y el informe de verificación, pero generalmente como nombres o rutas sin enlaces relativos. La edición modernizada no remite a la introducción recién publicada.

**Efecto**

No afecta a la fidelidad, pero dificulta la consulta conjunta.

**Resolución propuesta**

Añadir una breve sección «Documentos relacionados» con enlaces relativos estables. En el volumen, usar enlaces internos a preguntas, respuestas, notas y glosario.

### AC-09. Las validaciones individuales deben quedar superadas por una aceptación conjunta

**Evidencia**

Ambos documentos cuentan con informes individuales que los declaran aptos. Esas comprobaciones verificaron estructura y fidelidad por separado, pero no detectaron las tensiones que solo aparecen al leerlos conjuntamente.

**Efecto**

No invalida los informes anteriores; limita su alcance para el producto integrado.

**Resolución propuesta**

Tras corregir AC-01–AC-07, publicar una lista de aceptación conjunta que cite esta auditoría y declare qué incidencias se cerraron. Esa aceptación será la puerta de entrada al volumen de lectura.

## 8. Elementos correctamente resueltos

La auditoría confirma como adecuadas las siguientes decisiones:

- separación entre el interrogatorio externo y el manuscrito local;
- identificación y explicación de la truncación moderna de la pregunta 29;
- conservación de la laguna de la respuesta 9;
- mantenimiento de la discrepancia sobre las casas de molinos en la respuesta 17;
- falta de identificación del «otro don Manuel»;
- ausencia de unidad suplida tras los veinticuatro del voto;
- conservación marcada de «por no vacarse alguna»;
- documentación de la lectura «dado a renta» a partir de `dado arenta`;
- mantenimiento de medidas y monedas históricas sin conversiones;
- cobertura completa de portada, comparecencia, cuarenta respuestas, cierre y blancos;
- distinción explícita entre fuente local, contexto externo y análisis histórico.

## 9. Duplicidades y consolidación

La introducción y la edición modernizada repiten de manera útil algunas cautelas —medidas históricas, utilidad fiscal, vecino, límites del documento—, pero un volumen integrado no debería reproducirlas completas en varios lugares.

Se propone para el volumen:

1. una sola «Nota editorial» al comienzo;
2. las cautelas generales en la introducción;
3. notas al pie únicamente para problemas locales o primeras apariciones;
4. un glosario final consolidado a partir del Glosario validado;
5. enlaces desde cada término a su entrada, evitando repetir definiciones extensas;
6. una tabla única de concordancia pregunta–respuesta–folio.

## 10. Orden recomendado de resolución

1. AC-01: fijar el estatuto textual de las cuarenta preguntas.
2. AC-02: corregir el tratamiento de `avitadores`.
3. AC-03 y AC-04: aclarar esquilmo/esquileo y renta/venta.
4. AC-05: explicar Bega/Vega.
5. AC-06 y AC-07: revisar la interpretación de las yeguas y la puntuación de propietarios.
6. AC-08: añadir navegación.
7. AC-09: ejecutar aceptación conjunta.
8. Solo entonces preparar el volumen de lectura.

## 11. Dictamen final

Los dos documentos son estructuralmente completos, trazables y utilizables por separado. No se detectan pérdidas de contenido ni contradicciones numéricas generales.

La integración directa en un volumen debe esperar. Las dos incidencias altas afectan al estatuto del interrogatorio y a una categoría demográfica; las cinco medias afectan a términos o relaciones que un lector general podría interpretar erróneamente. Todas tienen resolución localizada y no requieren modificar la Edición Crítica.

La recomendación es preparar una corrección coordinada de la introducción y la edición modernizada, validarla conjuntamente y utilizar esas versiones corregidas como base del volumen de lectura.

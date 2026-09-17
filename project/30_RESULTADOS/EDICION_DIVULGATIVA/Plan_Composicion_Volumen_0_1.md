# Plan de composición del volumen

## Versión 0.1

**Fecha:** 17 de septiembre de 2026  
**Estado:** plan operativo inicial  
**Índice rector:** [Índice de referencia para el futuro volumen](./Indice_Referencia_Volumen_Final.md)  
**Título provisional:** *Sorribas y Santibáñez de Ordás en 1752. El Catastro de Ensenada: estudio histórico, facsímil, transcripción paleográfica y edición modernizada*

> Este plan define la arquitectura de composición, las dos salidas PDF, los controles y las fases de aceptación. No inicia todavía la composición del volumen ni modifica las fuentes editoriales.

# 1. Objetivo

Producir un volumen integral, legible y trazable que reúna:

- dieciséis capítulos;
- facsímil íntegro de las dieciocho páginas digitales del PDF autoritativo;
- transcripción paleográfica semidiplomática de las 35 unidades materiales;
- aparato crítico;
- edición modernizada con las cuarenta preguntas y respuestas;
- estudio histórico;
- glosario, cuadros y concordancias;
- nueve índices especializados;
- fuentes, tabla de versiones y criterios de citación.

El volumen se generará a partir de una sola composición maestra y se exportará en dos variantes con idéntico contenido, paginación, marcadores y enlaces.

# 2. Productos previstos

## 2.1. Salida de alta calidad

**Nombre propuesto:** `Sorrios_1752_Volumen_v1_0_Alta_Calidad.pdf`  
**Uso:** impresión, conservación y consulta detallada del facsímil.

Características:

- tamaño A4 vertical;
- color conservado;
- imágenes facsimilares sin reducción innecesaria;
- resolución efectiva objetivo de 300-400 ppp;
- compresión mínima o de alta calidad;
- texto y gráficos vectoriales;
- fuentes incrustadas;
- marcadores, enlaces internos y metadatos;
- sin cifrado ni restricciones de copia;
- tamaño esperado orientativo: 40-120 MB, sujeto a la resolución real del original.

No se declarará conformidad PDF/A sin una validación específica con una herramienta adecuada.

## 2.2. Salida comprimida

**Nombre propuesto:** `Sorrios_1752_Volumen_v1_0_Lectura.pdf`  
**Uso:** descarga, lectura en pantalla y circulación ordinaria.

Características:

- misma dimensión, contenido y paginación que la salida de alta calidad;
- color conservado;
- texto y gráficos vectoriales sin rasterizar;
- facsímiles y ampliaciones a una resolución efectiva objetivo de 160-200 ppp;
- compresión de imagen moderada, con calidad suficiente para leer la escritura;
- fuentes incrustadas;
- los mismos marcadores, enlaces internos y metadatos;
- tamaño esperado orientativo: 12-35 MB.

La salida comprimida se obtendrá después de cerrar la composición maestra. No se recompondrá por separado, para evitar diferencias de páginas, índices o referencias.

## 2.3. Ubicación y custodia

Durante la producción:

- los archivos temporales se mantendrán en `tmp/pdfs/`;
- las dos salidas finales se escribirán en `output/pdf/`;
- el PDF autoritativo y sus reproducciones temporales no se incorporarán al repositorio;
- GitHub conservará el plan, las fuentes textuales, los registros de operación y el informe de validación, pero no el PDF fuente ni los PDF finales;
- cada salida final tendrá tamaño, número de páginas y SHA-256 registrados.

# 3. Autoridades y congelación de fuentes

Antes de maquetar se fijará un único commit de GitHub como base de composición. La primera congelación deberá incluir:

- PDF autoritativo: `sorrios_ensenada_orden_lectura_calidad_original.pdf`;
- Edición Crítica v3.5;
- Introducción al Catastro, versión 1.1;
- edición modernizada, versión 1.1;
- Estudio Histórico, versión canónica 1.0;
- glosario histórico;
- índices vivos de personas, topónimos, instituciones, medidas y oficios;
- cuadros y documentos analíticos validados;
- índice de referencia del futuro volumen.

La identidad del PDF se comprobará mediante:

- identificador de Drive;
- nombre;
- MIME;
- tamaño esperado de 5.038.575 bytes;
- dieciocho páginas;
- SHA-256 esperado `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`, cuando el runtime permita calcularlo.

Las auditorías y validaciones se usarán como control, no como texto del cuerpo principal.

# 4. Formato físico

## 4.1. Página

- formato: A4 vertical, 210 × 297 mm;
- impresión a doble cara;
- sin sangrado, porque ningún elemento llegará al borde;
- márgenes enfrentados:
  - interior: 24 mm;
  - exterior: 18 mm;
  - superior: 18 mm;
  - inferior: 22 mm;
- apertura de cada parte y capítulo en página impar;
- páginas de cortesía sin cabecera ni folio visible cuando sean necesarias.

El A4 se adopta para preservar la legibilidad del facsímil. Un formato menor exigiría reducciones excesivas o una proliferación de ampliaciones.

## 4.2. Retícula

- una columna para narrativa, edición modernizada e índices;
- una columna de anchura controlada para la transcripción paleográfica;
- dos columnas solo en listados breves, glosario o índices cuando las pruebas de legibilidad lo permitan;
- tablas ajustadas a la caja; las tablas extensas podrán girarse a página horizontal sin alterar el resto del volumen;
- alineación vertical flexible: no se forzará la justificación vertical a costa de crear huecos o deformar notas.

# 5. Sistema tipográfico

## 5.1. Familias

Propuesta inicial:

- texto principal y transcripciones: Source Serif 4;
- títulos, cabeceras, tablas y navegación: Source Sans 3;
- símbolos auxiliares: Noto Sans Symbols, solo cuando sea necesario.

Alternativas de reserva:

- Liberation Serif;
- Liberation Sans.

Todas las fuentes deberán permitir incrustación. Antes de aprobar el diseño se comprobarán los caracteres españoles, numerales, corchetes editoriales, cruces, signos de interrogación y glifos históricos empleados.

## 5.2. Tamaños iniciales

- texto narrativo y modernizado: 10,5/14 pt;
- transcripción paleográfica: 9,5/12,5 pt;
- preguntas del interrogatorio: 10/13 pt, con diferenciación tipográfica;
- notas al pie: 8,5/11 pt;
- cuadros e índices: 8,5-9,5 pt según densidad;
- pies de facsímil: 8/10 pt;
- títulos de capítulo: 22-26 pt;
- títulos de parte: 28-34 pt.

Estos valores se confirmarán mediante una muestra impresa y una revisión en pantalla al 100 %.

## 5.3. Criterios de legibilidad

- contraste alto;
- no se comunicará información solo mediante color;
- evitar líneas de texto excesivamente largas;
- viudas y huérfanas controladas;
- al menos dos líneas de un párrafo antes o después de un salto de página;
- guionado moderado;
- preservación literal de los saltos de línea en la transcripción paleográfica.

# 6. Color y diseño

Paleta propuesta:

- negro y grises cálidos para el texto;
- azul grisáceo oscuro para navegación y títulos;
- granate oscuro como acento limitado;
- fondo blanco o marfil muy claro;
- recuadros de preguntas y avisos con tonos suficientemente claros para conservar contraste.

El diseño será sobrio y documental. No se aplicarán filtros decorativos al facsímil ni fondos que alteren la percepción del papel, la tinta o las anotaciones.

# 7. Arquitectura de página

## 7.1. Preliminares

- paginación romana en minúsculas;
- portada sin folio visible;
- créditos y nota editorial;
- índice general con enlaces;
- lista de reproducciones, cuadros y tablas.

## 7.2. Cuerpo

- paginación arábiga desde el capítulo 1;
- cabecera par: parte o sección;
- cabecera impar: capítulo;
- folio en el margen exterior inferior;
- sin cabecera en comienzos de parte o capítulo.

## 7.3. Capítulos históricos

- jerarquía máxima de tres niveles visibles;
- cuadros separados del discurso;
- llamadas de nota consistentes;
- distinción visible entre dato documental, cálculo e interpretación cuando el contenido lo requiera;
- referencias a respuestas y folios enlazadas internamente.

## 7.4. Preguntas y respuestas modernizadas

Cada bloque conservará:

1. título temático;
2. pregunta completa;
3. rótulo «Respuesta de Sorribas y Santibáñez»;
4. folio de procedencia;
5. texto modernizado;
6. notas.

La pregunta se distinguirá mediante un recuadro o filete discreto. No se usará una tipografía que pueda confundirse con la respuesta local.

# 8. Tratamiento del facsímil

## 8.1. Capítulo 14

- reproducción íntegra y en orden de las dieciocho páginas digitales;
- una imagen por página siempre que la legibilidad lo permita;
- centrado sin recorte;
- fondo neutro;
- pie con página digital, folios visibles y unidades relacionadas;
- rotación únicamente cuando sea necesaria para respetar la orientación de lectura;
- páginas y espacios en blanco conservados.

## 8.2. Capítulo 15

Para facilitar el cotejo de las 35 unidades:

- la imagen completa del capítulo 14 seguirá siendo la referencia facsimilar;
- podrán repetirse recortes de unidad en el capítulo 15;
- los recortes se identificarán siempre como ampliaciones;
- se indicarán la página digital y la posición `complete`, `left` o `right`;
- nunca se reconstruirán letras o zonas ilegibles mediante mejora generativa;
- los ajustes se limitarán a escala, rotación y correcciones globales no destructivas necesarias para la lectura.

## 8.3. Control de reproducción

Se verificará para cada una de las dieciocho páginas:

- presencia;
- orden;
- orientación;
- integridad de márgenes;
- correspondencia de folios;
- legibilidad en ambas salidas;
- ausencia de páginas duplicadas o sustituidas.

# 9. Transcripción paleográfica y aparato

La transcripción seguirá el Manual Editorial 1.6:

- ortografía, sintaxis, grafías, mayúsculas y puntuación conservadas;
- abreviaturas desarrolladas entre corchetes;
- numerales respetados;
- saltos de línea conservados;
- dudas, lagunas y blancos representados con los signos vigentes;
- 35 unidades en la secuencia de `unidades.yaml`;
- las seis secciones canónicas de cada unidad identificables en la composición.

Solución preferente:

- página par: facsímil o ampliación de unidad;
- página impar: transcripción correspondiente;
- observaciones y notas después de la transcripción o en páginas consecutivas cuando la extensión lo exija.

Si una unidad ocupa más de una página, las continuaciones llevarán unidad y folio en la cabecera. La composición no reducirá el cuerpo por debajo del mínimo fijado para forzar una correspondencia artificial.

# 10. Notas, citas y referencias cruzadas

- las notas de la edición modernizada irán al pie;
- las observaciones editoriales, notas paleográficas y notas históricas conservarán sus rótulos propios;
- las notas del estudio histórico podrán ir al pie o al final del capítulo según resulte más estable en la muestra;
- la numeración no se mezclará entre aparatos de distinta naturaleza;
- todas las referencias a capítulos, respuestas, folios, unidades, cuadros e índices se crearán como enlaces internos;
- no se mostrarán rutas técnicas, identificadores de herramientas ni marcadores provisionales.

# 11. Cuadros, gráficos y concordancias

- títulos y numeración propios;
- fuente o base documental bajo cada cuadro;
- repetición de encabezados en tablas partidas;
- prohibición de filas cortadas cuando pueda evitarse;
- sombreado compatible con escala de grises;
- cifras alineadas por unidad o separador decimal;
- uso de «dato», «cálculo» e «interpretación» conforme al estudio canónico;
- gráficos limitados a relaciones que no resulten claras en una tabla;
- concordancias con anclas hacia facsímil, unidad, folio, respuesta y capítulo.

# 12. Glosario e índices

## 12.1. Glosario

- orden alfabético;
- lema normalizado;
- forma documental;
- definición breve;
- primera aparición;
- referencias cruzadas;
- enlace de retorno desde la primera nota del texto cuando resulte útil.

## 12.2. Índices existentes

Se adaptarán y paginarán los índices de:

- personas;
- topónimos;
- instituciones;
- medidas;
- oficios.

## 12.3. Índices nuevos

Se construirán:

- productos, cultivos, ganados y recursos;
- cargas, derechos, rentas y fiscalidad;
- preguntas y respuestas;
- índice analítico general.

## 12.4. Regla de paginación

Los índices definitivos se generarán después de cerrar la paginación 0.8. Cada entrada podrá remitir a:

- página del facsímil;
- unidad o folio;
- transcripción paleográfica;
- respuesta modernizada;
- capítulo histórico.

Las variantes históricas se conservarán con remisiones de «véase» y «véase también». No se fusionarán formas documentales de manera silenciosa.

# 13. Accesibilidad y navegación

Ambas salidas incluirán:

- texto seleccionable y buscable;
- marcadores para partes, capítulos, apéndices e índices;
- índice general enlazado;
- enlaces de retorno cuando sean útiles;
- títulos y pies de figura legibles;
- orden lógico de lectura en el contenido textual;
- metadatos de título, materia, versión, fecha e idioma;
- contraste suficiente;
- significado independiente del color.

No se declarará conformidad PDF/UA sin una auditoría específica. La lectura del facsímil se apoyará siempre en la transcripción textual accesible.

# 14. Estimación inicial

Extensión provisional:

- preliminares: 12-18 páginas;
- partes I y II: 90-140 páginas;
- facsímil íntegro: 18-24 páginas;
- transcripción y aparato: 70-110 páginas;
- edición modernizada: 45-70 páginas;
- aparatos e índices: 55-90 páginas.

**Estimación total:** 290-450 páginas.

La amplitud del intervalo se reducirá después de la muestra de diseño y del inventario completo de notas, tablas e índices.

# 15. Flujo de producción

## Fase 0. Preflight y congelación

- fijar commit base;
- comprobar controles;
- verificar identidad del PDF;
- inventariar fuentes y versiones;
- confirmar 16 capítulos, 18 páginas, 35 unidades, 40 respuestas y nueve índices;
- crear una matriz fuente → sección → página prevista.

**Salida:** inventario de composición y registro de fuentes.

## Fase 1. Muestra de diseño 0.2

Preparar 12-20 páginas representativas:

- portada;
- comienzo de parte;
- capítulo narrativo;
- tabla;
- página facsimilar;
- pareja facsímil-transcripción;
- pregunta y respuesta modernizada;
- glosario;
- índice.

**Puerta de aceptación:** formato, tipografías, color, notas, cabeceras y tratamiento del facsímil.

## Fase 2. Maqueta completa 0.5

- incorporar todos los capítulos;
- integrar las dieciocho páginas facsimilares;
- incorporar las 35 unidades;
- integrar la edición modernizada;
- incorporar aparatos existentes;
- generar marcadores y enlaces provisionales.

**Puerta de aceptación:** integridad documental y estructura.

## Fase 3. Cierre de contenido 0.7

- resolver duplicaciones;
- normalizar notas y cuadros;
- cerrar fuentes y bibliografía;
- completar glosario e índices nuevos;
- impedir cambios textuales no registrados a partir de este punto.

**Puerta de aceptación:** contenido completo y estable.

## Fase 4. Paginación e índices 0.8

- cerrar saltos de página;
- asignar numeración definitiva;
- actualizar tabla de contenidos;
- generar los nueve índices;
- completar concordancias;
- validar referencias cruzadas.

**Puerta de aceptación:** paginación congelada.

## Fase 5. Prueba final 0.9

- exportar variante de alta calidad;
- derivar variante comprimida;
- ejecutar controles estructurales, textuales y visuales;
- corregir únicamente defectos registrados;
- regenerar ambas variantes desde la misma fuente maestra.

**Puerta de aceptación:** aceptación conjunta de las dos salidas.

## Fase 6. Publicación 1.0

- generar los dos PDF definitivos;
- registrar nombres, tamaños, páginas y SHA-256;
- archivar informe de validación;
- conservar la fuente de composición;
- entregar ambas variantes.

# 16. Control de calidad

## 16.1. Integridad editorial

- 16 capítulos presentes y en orden;
- 18 páginas facsimilares completas y en orden;
- 35 unidades paleográficas presentes y en orden;
- seis secciones canónicas por unidad;
- 40 preguntas y 40 respuestas consecutivas;
- glosario completo;
- nueve índices presentes;
- notas sin llamadas o definiciones huérfanas;
- tablas y figuras enumeradas;
- bibliografía y fuentes completas.

## 16.2. Control textual

- comparación de encabezados y secuencias con las fuentes canónicas;
- ausencia de sustituciones silenciosas;
- conservación de grafías paleográficas;
- coincidencia de preguntas entre introducción y edición modernizada;
- verificación de cifras, medidas, monedas y nombres;
- búsqueda de marcadores provisionales, rutas técnicas o mensajes de error;
- extracción de texto para comprobar orden, caracteres y buscabilidad.

## 16.3. Control visual

Se renderizarán todas las páginas a imágenes para comprobar:

- texto cortado o superpuesto;
- tablas rotas;
- notas fuera de caja;
- imágenes borrosas o deformadas;
- glifos ausentes;
- cabeceras y pies incoherentes;
- páginas en blanco no previstas;
- problemas de contraste;
- transiciones de parte y capítulo;
- legibilidad del facsímil en ambas salidas.

Las páginas críticas -portada, índices, facsímiles, transcripciones densas, tablas y cambios de orientación- se inspeccionarán además a resolución completa.

## 16.4. Control técnico

Para ambas salidas:

- apertura correcta;
- número de páginas idéntico;
- paginación y marcadores idénticos;
- enlaces internos funcionales;
- fuentes incrustadas;
- metadatos correctos;
- ausencia de cifrado;
- ausencia de formularios;
- texto seleccionable;
- tamaño registrado;
- SHA-256 registrado.

La versión comprimida deberá mantener el contenido y la legibilidad; solo podrán variar la compresión y la resolución de las imágenes.

# 17. Criterios de aceptación final

El volumen 1.0 solo se aceptará cuando:

1. se hayan cerrado todas las puertas de aceptación;
2. ambas salidas procedan de la misma composición;
3. no existan incidencias críticas o altas abiertas;
4. el facsímil sea legible y completo;
5. el texto paleográfico y modernizado sea íntegro;
6. los índices remitan a la paginación final;
7. la revisión visual no detecte defectos;
8. los controles técnicos sean satisfactorios;
9. las dos variantes tengan iguales páginas, navegación y contenido;
10. el informe final documente fuentes, versión y huellas digitales.

# 18. Riesgos y respuestas

| Riesgo | Respuesta prevista |
|---|---|
| Facsímil ilegible al reducirlo | A4, reproducción íntegra y ampliaciones de unidad |
| Volumen excesivamente pesado | Dos salidas y compresión solo de imágenes |
| Índices desfasados | Generarlos después de congelar paginación |
| Diferencias entre las dos salidas | Derivar ambas de una única composición maestra |
| Confusión entre fuente e interpretación | Diseño y rotulación diferenciados |
| Pérdida de saltos paleográficos | Estilos específicos y control línea a línea |
| Tablas demasiado anchas | Rediseño o páginas horizontales controladas |
| Cambios de contenido durante maquetación | Congelación 0.7 y registro de correcciones |
| Caracteres ausentes | Preflight de fuentes y revisión de glifos |
| Falsa declaración de estándares | No afirmar PDF/A o PDF/UA sin validación especializada |

# 19. Decisiones fijadas en 0.1

- un único volumen integral;
- formato A4 vertical;
- una composición maestra;
- dos salidas PDF;
- idéntica paginación y navegación;
- facsímil íntegro en color;
- alta calidad a 300-400 ppp;
- lectura comprimida a 160-200 ppp;
- dieciséis capítulos y nueve índices;
- PDF y reproducciones fuera de GitHub;
- aceptación por fases antes de la versión 1.0.

# 20. Decisiones que se confirmarán con la muestra 0.2

- familias tipográficas definitivas;
- color de acento;
- diseño de portada;
- ubicación final de las notas del estudio;
- uso de una o dos columnas en glosario e índices;
- frecuencia de ampliaciones facsimilares;
- solución exacta para tablas horizontales;
- extensión definitiva y tamaño de los archivos.

# 21. Próximo entregable

El siguiente producto será la **muestra de diseño 0.2**, no el volumen completo. Deberá representar todos los tipos de página y permitir aprobar la identidad visual y las reglas de composición antes de aplicar el diseño a varios centenares de páginas.

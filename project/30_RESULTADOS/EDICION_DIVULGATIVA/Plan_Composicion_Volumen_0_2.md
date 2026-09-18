# Plan de composición del volumen

## Versión 0.2

**Fecha:** 18 de septiembre de 2026  
**Estado:** plan operativo vigente  
**Índice rector:** [Índice de referencia para el futuro volumen](./Indice_Referencia_Volumen_Final.md)  
**Título provisional:** *Sorribos y Santibáñez de Ordás en 1752. El Catastro de Ensenada: estudio histórico, facsímil, transcripción paleográfica y edición modernizada*

> Este plan actualiza la versión 0.1 con la cartografía, la portada y la serie completa de índices definida por el índice rector 1.2. Establece la arquitectura de composición, las dos salidas PDF, los controles y las fases de aceptación. No inicia todavía la composición del volumen ni modifica las fuentes editoriales.

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
- Edición Crítica v3.6;
- Introducción al Catastro, versión 1.2;
- edición modernizada, versión 1.2;
- Estudio Histórico, versión canónica 1.1;
- glosario histórico;
- índices vivos de personas, topónimos, instituciones, medidas y oficios;
- cuadros y documentos analíticos validados;
- índice de referencia del futuro volumen, versión 1.2;
- fuentes cartográficas, licencias y memoria de elaboración del mapa.

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

# 7. Portada y cubierta

## 7.1. Momento de cierre

La muestra de diseño 0.2 incluirá una portada provisional para fijar jerarquía, tono y legibilidad. La portada y la cubierta definitivas se cerrarán en la prueba 0.9, una vez conocidas la paginación y la anchura del lomo.

## 7.2. Dirección visual

La propuesta combinará:

- tipografía sobria y contemporánea;
- un detalle auténtico del manuscrito, sin reconstrucciones imaginarias;
- líneas cartográficas discretas como recurso secundario;
- contraste suficiente en color y escala de grises;
- una composición que permita reconocer de inmediato el lugar, el año y la naturaleza documental del volumen.

No se usarán escenas históricas inventadas ni elementos que puedan confundirse con testimonios de 1752.

## 7.3. Elementos de cierre

La versión definitiva resolverá portada, lomo y contraportada; créditos de imagen y cartografía; zonas de seguridad; sangrados, si fueran necesarios; legibilidad en miniatura; y adaptación coherente a las dos salidas PDF.

# 8. Arquitectura de página

## 8.1. Preliminares

- paginación romana en minúsculas;
- portada sin folio visible;
- créditos y nota editorial;
- índice general con enlaces;
- mapa general de la zona;
- lista de mapas y reproducciones, cuadros y tablas.

## 8.2. Cuerpo

- paginación arábiga desde el capítulo 1;
- cabecera par: parte o sección;
- cabecera impar: capítulo;
- folio en el margen exterior inferior;
- sin cabecera en comienzos de parte o capítulo.

## 8.3. Capítulos históricos

- jerarquía máxima de tres niveles visibles;
- cuadros separados del discurso;
- llamadas de nota consistentes;
- distinción visible entre dato documental, cálculo e interpretación cuando el contenido lo requiera;
- referencias a respuestas y folios enlazadas internamente.

## 8.4. Preguntas y respuestas modernizadas

Cada bloque conservará:

1. título temático;
2. pregunta completa;
3. rótulo «Respuesta de Sorribos y Santibáñez»;
4. folio de procedencia;
5. texto modernizado;
6. notas.

La pregunta se distinguirá mediante un recuadro o filete discreto. No se usará una tipografía que pueda confundirse con la respuesta local.

# 9. Tratamiento del facsímil

## 9.1. Capítulo 14

- reproducción íntegra y en orden de las dieciocho páginas digitales;
- una imagen por página siempre que la legibilidad lo permita;
- centrado sin recorte;
- fondo neutro;
- pie con página digital, folios visibles y unidades relacionadas;
- rotación únicamente cuando sea necesaria para respetar la orientación de lectura;
- páginas y espacios en blanco conservados.

## 9.2. Capítulo 15

Para facilitar el cotejo de las 35 unidades:

- la imagen completa del capítulo 14 seguirá siendo la referencia facsimilar;
- podrán repetirse recortes de unidad en el capítulo 15;
- los recortes se identificarán siempre como ampliaciones;
- se indicarán la página digital y la posición `complete`, `left` o `right`;
- nunca se reconstruirán letras o zonas ilegibles mediante mejora generativa;
- los ajustes se limitarán a escala, rotación y correcciones globales no destructivas necesarias para la lectura.

## 9.3. Control de reproducción

Se verificará para cada una de las dieciocho páginas:

- presencia;
- orden;
- orientación;
- integridad de márgenes;
- correspondencia de folios;
- legibilidad en ambas salidas;
- ausencia de páginas duplicadas o sustituidas.

# 10. Transcripción paleográfica y aparato

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

# 11. Notas, citas y referencias cruzadas

- las notas de la edición modernizada irán al pie;
- las observaciones editoriales, notas paleográficas y notas históricas conservarán sus rótulos propios;
- las notas del estudio histórico podrán ir al pie o al final del capítulo según resulte más estable en la muestra;
- la numeración no se mezclará entre aparatos de distinta naturaleza;
- todas las referencias a capítulos, respuestas, folios, unidades, cuadros e índices se crearán como enlaces internos;
- no se mostrarán rutas técnicas, identificadores de herramientas ni marcadores provisionales.

# 12. Cuadros, gráficos y concordancias

- títulos y numeración propios;
- fuente o base documental bajo cada cuadro;
- repetición de encabezados en tablas partidas;
- prohibición de filas cortadas cuando pueda evitarse;
- sombreado compatible con escala de grises;
- cifras alineadas por unidad o separador decimal;
- uso de «dato», «cálculo» e «interpretación» conforme al estudio canónico;
- gráficos limitados a relaciones que no resulten claras en una tabla;
- concordancias con anclas hacia facsímil, unidad, folio, respuesta y capítulo.

# 13. Glosario e índices

## 13.1. Glosario

- orden alfabético;
- lema normalizado;
- forma documental;
- definición breve;
- primera aparición;
- referencias cruzadas;
- enlace de retorno desde la primera nota del texto cuando resulte útil.

## 13.2. Serie definitiva de índices

El volumen cerrará con nueve índices diferenciados y coordinados:

1. índice onomástico;
2. índice de lugares y topónimos;
3. índice de instituciones, jurisdicciones y entidades;
4. índice de oficios, cargos y condiciones;
5. índice de medidas, monedas y unidades;
6. índice de productos, cultivos, ganados y recursos;
7. índice de cargas, derechos, rentas y fiscalidad;
8. índice de preguntas y respuestas;
9. índice de materias.

Los cinco índices vivos ya existentes —personas, topónimos, instituciones, medidas y oficios— se adaptarán a esta nomenclatura y a la paginación del volumen. Los cuatro restantes se construirán durante la composición.

## 13.3. Índice onomástico

Reunirá todas las personas identificables, incluidas autoridades, declarantes, propietarios, clérigos, titulares de derechos y personas citadas en las fuentes o en el estudio. Conservará las variantes documentales mediante remisiones y distinguirá homónimos cuando la fuente lo permita.

## 13.4. Índice de materias

Funcionará como acceso analítico general al volumen. Incluirá conceptos históricos, económicos, sociales, editoriales y documentales; evitará duplicar mecánicamente los índices especializados y usará remisiones de «véase» y «véase también».

## 13.5. Regla de paginación y navegación

Los índices definitivos se generarán después de cerrar la paginación 0.8. Cada entrada podrá remitir a:

- página del facsímil;
- unidad o folio;
- transcripción paleográfica;
- respuesta modernizada;
- capítulo histórico;
- mapa o elemento cartográfico pertinente.

Las variantes históricas se conservarán con remisiones de «véase» y «véase también». No se fusionarán formas documentales de manera silenciosa. Todos los índices llevarán enlaces internos y retornos coherentes.

# 14. Cartografía

## 14.1. Lámina principal

Se incorporará una lámina cartográfica a doble página en los preliminares, después de la cronología y antes de la parte I. Deberá combinar:

- un mapa de situación regional;
- un mapa local de Sorribos y Santibáñez de Ordás y su entorno inmediato;
- si la evidencia lo permite, un esquema interpretativo claramente rotulado de elementos mencionados en 1752.

## 14.2. Fuentes y estatuto de la información

Se priorizarán bases oficiales del IGN/CNIG u otras fuentes públicas con licencia compatible. El diseño distinguirá de forma explícita:

- información geográfica actual;
- lugares o relaciones documentados en el expediente;
- localizaciones aproximadas o inferidas.

Toda capa tendrá fuente, fecha, licencia y criterio de elaboración registrados.

## 14.3. Diseño y exportación

La lámina incluirá escala, norte, leyenda y créditos. Se preparará para lectura en A4, funcionará en color y escala de grises y se exportará preferentemente como gráfico vectorial en ambas variantes PDF. Sus topónimos se coordinarán con el índice de lugares y topónimos.

## 14.4. Controles cartográficos

Antes de aprobarla se comprobarán:

- localización relativa de los núcleos;
- ortografía y jerarquía de topónimos;
- coordenadas y escala;
- fuentes y licencias;
- separación entre presente, dato documental e inferencia;
- legibilidad impresa y digital;
- enlaces desde la tabla de contenidos y los índices.

# 15. Accesibilidad y navegación

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

# 16. Estimación inicial

Extensión provisional:

- preliminares: 16-24 páginas;
- partes I y II: 90-140 páginas;
- facsímil íntegro: 18-24 páginas;
- transcripción y aparato: 70-110 páginas;
- edición modernizada: 45-70 páginas;
- aparatos e índices: 55-90 páginas.

**Estimación total:** 295-460 páginas.

La amplitud del intervalo se reducirá después de la muestra de diseño y del inventario completo de notas, tablas e índices.

# 17. Flujo de producción

## Fase 0. Preflight y congelación

- fijar commit base;
- comprobar controles;
- verificar identidad del PDF;
- inventariar fuentes y versiones;
- confirmar 16 capítulos, 18 páginas, 35 unidades, 40 respuestas, nueve índices y una lámina cartográfica;
- crear una matriz fuente → sección → página prevista.

**Salida:** inventario de composición y registro de fuentes.

## Fase 1. Muestra de diseño 0.2

Preparar 12-20 páginas representativas:

- portada provisional;
- lámina cartográfica;
- comienzo de parte;
- capítulo narrativo;
- tabla;
- página facsimilar;
- pareja facsímil-transcripción;
- pregunta y respuesta modernizada;
- glosario;
- índice.

**Puerta de aceptación:** portada provisional, mapa, formato, tipografías, color, notas, cabeceras y tratamiento del facsímil.

## Fase 2. Maqueta completa 0.5

- incorporar todos los capítulos;
- integrar la lámina cartográfica y sus créditos;
- integrar las dieciocho páginas facsimilares;
- incorporar las 35 unidades;
- integrar la edición modernizada;
- incorporar aparatos existentes;
- generar marcadores y enlaces provisionales.

**Puerta de aceptación:** integridad documental y estructura.

## Fase 3. Cierre de contenido 0.7

- resolver duplicaciones;
- normalizar notas y cuadros;
- cerrar fuentes, bibliografía y atribuciones cartográficas;
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

# 18. Control de calidad

## 18.1. Integridad editorial

- 16 capítulos presentes y en orden;
- 18 páginas facsimilares completas y en orden;
- 35 unidades paleográficas presentes y en orden;
- seis secciones canónicas por unidad;
- 40 preguntas y 40 respuestas consecutivas;
- glosario completo;
- nueve índices presentes, incluidos el onomástico y el de materias;
- lámina cartográfica completa, atribuida y enlazada;
- notas sin llamadas o definiciones huérfanas;
- tablas y figuras enumeradas;
- bibliografía y fuentes completas.

## 18.2. Control textual

- comparación de encabezados y secuencias con las fuentes canónicas;
- ausencia de sustituciones silenciosas;
- conservación de grafías paleográficas;
- coincidencia de preguntas entre introducción y edición modernizada;
- verificación de cifras, medidas, monedas y nombres;
- búsqueda de marcadores provisionales, rutas técnicas o mensajes de error;
- extracción de texto para comprobar orden, caracteres y buscabilidad.

## 18.3. Control visual

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
- legibilidad del facsímil en ambas salidas;
- escala, orientación, leyenda, topónimos y créditos del mapa.

Las páginas críticas —portada, mapa, índices, facsímiles, transcripciones densas, tablas y cambios de orientación— se inspeccionarán además a resolución completa.

## 18.4. Control técnico

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

# 19. Criterios de aceptación final

El volumen 1.0 solo se aceptará cuando:

1. se hayan cerrado todas las puertas de aceptación;
2. ambas salidas procedan de la misma composición;
3. no existan incidencias críticas o altas abiertas;
4. el facsímil sea legible y completo;
5. el texto paleográfico y modernizado sea íntegro;
6. los índices remitan a la paginación final;
7. el mapa sea legible, atribuible y distinga dato actual, dato documental e inferencia;
8. la portada y la cubierta estén cerradas y sean coherentes con el contenido;
9. la revisión visual no detecte defectos;
10. los controles técnicos sean satisfactorios;
11. las dos variantes tengan iguales páginas, navegación y contenido;
12. el informe final documente fuentes, versión y huellas digitales.

# 20. Riesgos y respuestas

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
| Confusión entre geografía actual y paisaje de 1752 | Rotular por separado presente, evidencia documental e inferencia |
| Fuentes cartográficas sin licencia clara | Registrar fuente, fecha y licencia antes de incorporar cada capa |
| Cierre prematuro de la cubierta | Usar portada provisional en 0.2 y cerrar lomo y contraportada en 0.9 |

# 21. Decisiones fijadas en 0.2

- un único volumen integral;
- formato A4 vertical;
- una composición maestra;
- dos salidas PDF;
- idéntica paginación y navegación;
- facsímil íntegro en color;
- alta calidad a 300-400 ppp;
- lectura comprimida a 160-200 ppp;
- dieciséis capítulos y nueve índices, con denominación expresa del onomástico y el de materias;
- una lámina cartográfica principal en los preliminares;
- portada provisional en 0.2 y cubierta definitiva en 0.9;
- PDF y reproducciones fuera de GitHub;
- aceptación por fases antes de la versión 1.0.

# 22. Decisiones que se confirmarán con la muestra 0.2

- familias tipográficas definitivas;
- color de acento;
- lenguaje visual de la portada provisional;
- ubicación final de las notas del estudio;
- uso de una o dos columnas en glosario e índices;
- frecuencia de ampliaciones facsimilares;
- solución exacta para tablas horizontales;
- extensión definitiva y tamaño de los archivos.

# 23. Próximo entregable

El siguiente producto será la **muestra de diseño 0.2**, no el volumen completo. Incluirá una portada provisional y una primera solución cartográfica, además de representar todos los tipos de página. Permitirá aprobar la identidad visual y las reglas de composición antes de aplicar el diseño a varios centenares de páginas.

# Historial de versiones

| Versión | Fecha | Cambio principal |
|---|---|---|
| 0.1 | 17 de septiembre de 2026 | Plan operativo inicial para un volumen y dos salidas PDF |
| 0.2 | 18 de septiembre de 2026 | Integración de portada, cartografía, índice onomástico, índice de materias y controles conjuntos; rectificación paleográfica del topónimo `Sorribos` y alineación con las fuentes 3.6/1.2/1.1 |

# Auditoría C — fuentes, bibliografía y aparatos narrativos

**Fecha:** 10 de octubre de 2026<br>
**Rama:** `feature/quarto-book`<br>
**Baseline:** `7bbfef34bed0dd237732d0a215989b8ea5245e12`<br>
**Candidata técnica auditada:** `49ab2e1b1a58ca9201efab54b42a3125de7326f8`<br>
**Estado:** diagnóstico cerrado; decisiones e implementación pendientes

## 1. Objeto y alcance

Esta auditoría separa cuatro problemas que la candidata no debe confundir:

1. la trazabilidad interna entre manuscrito, página, folio, unidad, respuesta, edición, registro, capítulo y aparatos;
2. las fuentes externas usadas como contexto `E` o como apoyo puntual;
3. la bibliografía pública que permitiría al lector identificar esas fuentes;
4. los aparatos narrativos prometidos: cuestiones abiertas, fuentes, bibliografía, historia de versiones y modelos de cita.

La pregunta central recibe una respuesta afirmativa con reservas: **la estructura de un sistema completo y coherente para 1.0 puede construirse fundamentalmente con información ya presente**, pero no puede cerrarse sin decisiones editoriales, datos de identidad y una verificación bibliográfica posterior de 16 referencias incompletas. Tampoco pueden cerrarse todavía las fuentes, licencias y atribuciones de los mapas futuros ni las ampliaciones históricas G3 de la Auditoría A.

No se abrió ninguna URL ni se hizo investigación externa. No se modificaron fuentes canónicas, `publication/`, `references.bib`, la candidata o los PDF. Las clasificaciones de este informe son diagnósticas y no autorizan implementación.

## 2. Baselines y materiales

| Elemento | Estado comprobado |
|---|---|
| Rama y `base_sha` | `feature/quarto-book` en `7bbfef34bed0dd237732d0a215989b8ea5245e12` |
| Upstream inicial | `origin/feature/quarto-book` en `7be36f60442e46bd5a4c74775e4ed5a5a8e7ba23`; 0 detrás / 1 delante |
| `main` / `origin/main` | ambos en `e81dc9239ac8dbabfe77168a50ef98c4d3b79170` |
| Estado canónico | `operation.status: clean`; Estudio Histórico habilitado |
| Árbol `project/` | `e32917763475ceebdfe7b54830e1fb43f6419dad` |
| Árbol `publication/` | `cfcf349928fe3e1f2d3b33c005c31fa5621b1878` |
| Composición 0.6 | 259 páginas; 6.806.113 bytes; SHA-256 `78551fc2bcc067634b97e6284b5a3b88b1916067851d51ee00b14e488e4187f4` |

Se auditaron el [Estudio Histórico 1.2](../project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md), el [Registro 1.2](../project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md), la [Edición Crítica 3.6](../project/20_TRABAJO_EDITORIAL/Edicion_Critica.md), el [Glosario](../project/20_TRABAJO_EDITORIAL/Glosario.md), la [Introducción 1.3](../project/30_RESULTADOS/EDICION_DIVULGATIVA/Introduccion_Catastro_Ensenada_Sorrios.md), la [edición modernizada 1.3](../project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md), el [índice rector 1.5](../project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md), el [Plan 0.5](../project/30_RESULTADOS/EDICION_DIVULGATIVA/Plan_Composicion_Volumen_0_5.md), la candidata Quarto y los apéndices E–H y colofón de 0.6.

El Manual 1.6 confirma la regla de propagación: una fuente externa puede aportar identificación o contexto citado, pero no se convierte en base documental autónoma del Estudio. Cualquier investigación sustantiva futura debe entrar primero por la autoridad canónica que corresponda y propagarse después al Estudio, Registro, glosario, capítulos, bibliografía e índices; nunca debe parchearse directamente en Quarto.

## 3. Sistema actual de trazabilidad

La trazabilidad interna es fuerte, mientras que la trazabilidad bibliográfica para el lector es incompleta.

| Capa | Situación actual | Visibilidad para el lector |
|---|---|---|
| Manuscrito → página → unidad/folio | 18 páginas, 35 unidades y metadatos materiales estables | alta en facsímil, transcripción y concordancia |
| Unidad/folio ↔ respuesta | concordancia bidireccional para 40 respuestas | alta |
| Respuesta/folio → D/C/I/E/L | Registro de 112 entradas con estado, cautela y evidencia | alta en la matriz; variable en capítulos |
| `sources:` de capítulos | rutas, versiones y localizadores internos detallados | control editorial; el front matter no constituye bibliografía pública |
| `evidence:` de capítulos | IDs estructurados por nivel | control editorial; no todos aparecen en el cuerpo renderizado |
| Marcas del cuerpo | texto del tipo `[E: HID-008]` | visible pero sin enlace directo a la matriz |
| Matriz | 112 entradas, anclas, evidencia y retornos | alta; las 25 E incluyen enlace externo |
| URLs próximas | ocho recursos institucionales únicos en capítulos 1–2; apoyos puntuales en transcripción y glosario | útil pero heterogénea |
| Bibliografía Pandoc | `bibliography: references.bib` configurado | nula: no hay entradas ni citas Pandoc |

Las 25 entradas `E` están en la matriz. Trece identificadores aparecen también en el cuerpo de al menos un capítulo; once se usan en prosa y constan en el front matter, pero no muestran el ID junto a la afirmación; `TOP-006` solo permanece en la matriz. Las entradas `TOP-004`–`TOP-011` muestran además `Uso en el libro: —` en la matriz, aunque siete de ellas sustentan el capítulo 3. La cadena existe, pero no siempre es recorrible desde la afirmación.

## 4. Inventario de referencias externas

El corpus auditado contiene **40 referencias externas únicas y 41 URL distintas**. La diferencia se debe a que el estudio de Álvarez-Balbuena aparece mediante dos rutas institucionales. El inventario consolida esa obra una sola vez. No incluye documentos internos del proyecto ni convierte las signaturas mencionadas dentro de una edición secundaria en nuevas obras consultadas.

| N.º | Referencia identificable con los datos existentes | Tipo | URL ya registrada | Lugar / E-ID / capítulo | Completitud |
|---:|---|---|---|---|---|
| 1 | Fernando Álvarez-Balbuena García, «Estudiu histórico-etimolóxicu de la toponimia mayor del términu municipal d’Ordás (Llión)» | publicación académica / repositorio | [BULERIA](https://buleria.unileon.es/handle/10612/12285); [revista](https://revistas.unileon.es/index.php/anada/article/view/6165) | Estudio, Registro, Edición Crítica; `TOP-010`, `JUR-007`; caps. 3 y 5 | suficiente |
| 2 | Ejemplo leonés de gastos de Corpus en respuestas catastrales, sitio Caboalles de Abajo | comparación contextual / web | [enlace](https://caboalles.wordpress.com/2008/09/29/catastro-de-ensenada-ano-1752/) | `FIS-017`; caps. 11 y 13 | mínima |
| 3 | AHN, serie «Expedición del título de Abogado de los Reales Consejos» | catálogo institucional | [Censo-Guía](https://censoarchivos.cultura.gob.es/CensoGuia/fondoDetail.htm?archivoId=9&eventDescendiente=descendienteDetail&id=1248343) | nota histórica de folio 306r; transcripción | suficiente |
| 4 | Ofelia Rey Castelao, estudio del Voto de Santiago en León | artículo / publicación académica | [Dialnet](https://dialnet.unirioja.es/descarga/articulo/246923.pdf) | `FIS-013`; caps. 10, 12 y 13 | parcial |
| 5 | Estudio sobre propios y arbitrios y la Contaduría General | artículo / publicación académica | [Dialnet](https://dialnet.unirioja.es/descarga/articulo/785131.pdf) | `FIS-016`; caps. 11 y 13 | mínima |
| 6 | *Nobiliario de la Montaña leonesa* | libro / fuente secundaria | [Dialnet](https://dialnet.unirioja.es/descarga/libro/770795.pdf) | `TOP-006`; matriz | parcial |
| 7 | RAE, DLE, voz «negrillo» | recurso léxico institucional | [DLE](https://dle.rae.es/negrillo) | Glosario; capítulo generado | suficiente |
| 8 | RAE, DLE, voz «pan» | recurso léxico institucional | [DLE](https://dle.rae.es/pan) | Glosario; capítulo generado | suficiente |
| 9 | Estudio sobre juzgados y señoríos leoneses del siglo XVIII | artículo / publicación académica | [Magallánica](https://fh.mdp.edu.ar/revistas/index.php/magallanica/article/view/6817) | `JUR-008`; cap. 5 | mínima |
| 10 | Edición moderna del documento de 1267, con remisión a `AHN, Clero, carp. 828, núm. 11` | edición documental / trabajo académico | [GREDOS](https://gredos.usal.es/bitstream/handle/10366/151409/SANTANO%20VALBUENA%2C%20FERNANDO%20-%20TFG.pdf?isAllowed=y&sequence=1) | `TOP-005`; cap. 3 | parcial |
| 11 | Juan Manuel Bartolomé, estudio sobre lino e hilaza en León | publicación académica | [GREDOS](https://gredos.usal.es/handle/10366/70337) | `AGR-011`; caps. 7 y 13 | parcial |
| 12 | Estudio léxico histórico de la Valduerna | publicación académica | [idUS](https://idus.us.es/server/api/core/bitstreams/f727d611-1345-4de8-84ed-a60f90ab56fe/content) | `AGR-013`; caps. 7, 8 y 13 | mínima |
| 13 | PARES, «Presentación de las Respuestas Generales» | recurso institucional | [PARES](https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=10) | Introducción; cap. 1 | suficiente |
| 14 | PARES, «Interrogatorio de 1749» | fuente documental / recurso institucional | [PARES](https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=30) | Introducción; cap. 2 | suficiente |
| 15 | PARES, «Interrogatorio en grafía actual» | edición documental institucional | [PARES](https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=31b) | Introducción; cap. 2 | suficiente |
| 16 | PARES, «Proceso catastral» | recurso institucional | [PARES](https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=32) | Introducción; caps. 1–2 | suficiente |
| 17 | PARES, «Conservación de las Respuestas Generales» | recurso institucional | [PARES](https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=33) | Introducción; cap. 1 | suficiente |
| 18 | PARES, estudio institucional del Catastro | recurso institucional | [PARES](https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=40) | Introducción; cap. 1 | suficiente |
| 19 | PARES, pleito de 1715, `PL CIVILES, ALONSO RODRÍGUEZ (OLV), CAJA 654,2` | catálogo / fuente primaria archivística | [PARES](https://pares.mcu.es/ParesBusquedas20/catalogo/description/12805146) | `TOP-007`; Edición Crítica; cap. 3 | completa |
| 20 | PARES, expediente de examen y título de abogado de los Reales Consejos | catálogo institucional | [PARES](https://pares.mcu.es/ParesBusquedas20/catalogo/description/1547060) | `JUR-009`; caps. 3 y 12 | suficiente |
| 21 | PARES, Honrado Concejo de la Mesta | catálogo institucional | [PARES](https://pares.mcu.es/ParesBusquedas20/catalogo/description/172318) | `FIS-015`; caps. 11–13 | suficiente |
| 22 | PARES, correspondencia de Francisco Alfonso Pimentel, XV conde de Luna, 1742–1753 | catálogo / fuente primaria archivística | [PARES](https://pares.mcu.es/ParesBusquedas20/catalogo/description/3925721) | `JUR-008`; Edición Crítica; caps. 5 y 12 | suficiente |
| 23 | PARES, referencia de 1751 a un vecino de Santibáñez, Concejo de Ordás | catálogo / fuente primaria archivística | [PARES](https://pares.mcu.es/ParesBusquedas20/catalogo/description/478437) | nota histórica de folio 306r; transcripción | suficiente |
| 24 | PARES, referencias de 1808 a la jurisdicción y padrones de Ordás | catálogo / fuente primaria archivística | [PARES](https://pares.mcu.es/ParesBusquedas20/catalogo/description/480016) | nota histórica de folio 306r; transcripción | suficiente |
| 25 | Estudio sobre ganado dado a renta o aparcería en León | publicación académica / comparación contextual | [Universidad de Oviedo](https://reunido.uniovi.es/index.php/RCG/article/download/894/824) | `GAN-008`; caps. 8 y 13 | mínima |
| 26 | Relación parroquial de 1768 enviada por el obispo de Oviedo al Consejo de Castilla; `B.R.A.H.M., leg. 9/6257` | edición documental / fuente primaria reproducida | [Memoria Ecclesiae 28](https://scrinia.org/wp-content/uploads/2021/12/Memoria-Ecclesiae-28.pdf) | `TOP-008`, `DEM-006`; caps. 3 y 6 | suficiente |
| 27 | Estudio sobre pobreza y hospitalidad pública en Valladolid / Hospital de Inocentes | publicación académica | [UVaDOC](https://uvadoc.uva.es/bitstream/handle/10324/21203/Investigaciones-1982-03-Pobreza-Hospitalidad-Publica-Ciudad-Valladolid.pdf) | `FIS-014`; caps. 11–13 | mínima |
| 28 | Pablo José Zapico, inventario de molinos leoneses en el Catastro de Ensenada | publicación académica | [UVaDOC](https://uvadoc.uva.es/handle/10324/22081) | `HID-008`; caps. 9 y 13 | parcial |
| 29 | Ayuntamiento de Santa María de Ordás, página de Santibáñez de Ordás | web institucional / recurso geográfico actual | [Ayuntamiento](https://www.aytosantamariadeordas.es/los-pueblos/santibanez-de-ordas/) | `TOP-011`; Edición Crítica; cap. 3 | suficiente |
| 30 | *Gaceta de Madrid*, 7 de septiembre de 1864, escritura de 1831 | fuente primaria publicada / publicación oficial | [BOE](https://www.boe.es/gazeta/dias/1864/09/07/pdfs/GMD-1864-251.pdf) | `TOP-009`; Edición Crítica; cap. 3 | completa |
| 31 | Dirección General del Catastro, *El Catastro de Ensenada. Vera 1752* | edición documental institucional | [Catastro](https://www.catastro.hacienda.gob.es/documentos/publicaciones/catalogoensenada_1752_vera.pdf) | Introducción; cap. 2 | suficiente |
| 32 | Dirección General del Catastro, fondo editorial sobre el Catastro de Ensenada | web institucional | [Catastro](https://www.catastro.hacienda.gob.es/es-ES/fondo_editorial.html) | Introducción; cap. 1 | suficiente |
| 33 | Ordenanzas concejiles leonesas y servicios por vecera | comparación contextual / web | [Cuadros de León](https://www.cuadrosleon.com/old/el%20concejo.htm) | `TRA-006`; caps. 11 y 13 | mínima |
| 34 | «Meros apuntes metrológicos provenientes de la medición de la tierra agraria…» | recurso metrológico / artículo | [e-medida](https://www.e-medida.es/numero-12/meros-apuntes-metrologicos-provenientes-de-la-medicion-de-la-tierra-agraria-repoblacion-y-repartimientos-desde-la-edad-media-al-siglo-xvi/) | `TER-011`; caps. 7 y 13 | parcial |
| 35 | Cristina Jular Pérez-Alfaro, «Conflictos ante tenentes y merinos en los siglos XII–XIII, ¿contestación al poder señorial o al poder regio?» | artículo / edición documental | [Historia Agraria](https://www.historiaagraria.com/FILE/articulos/HA13_jular.pdf) | `TOP-004`; cap. 3 | suficiente |
| 36 | Junta de Andalucía / Archivo Histórico Provincial de Granada, ficha sobre documento de 1727 relativo al Voto de Santiago | catálogo / web institucional | [Junta de Andalucía](https://www.juntadeandalucia.es/organismos/culturapatrimoniohistoricoydeporte/areas/cultura/archivos/archivos-consejeria/archivo-historico-provincial-granada/ahpg-recomienda/paginas/documento-ahpg-sep-2012.html) | Edición Crítica y Glosario; transcripción y glosario generado | suficiente |
| 37 | Ministerio de Agricultura, *Elementos constitutivos del patrimonio paisajístico* | publicación institucional / recurso léxico agrario | [Ministerio](https://www.mapa.gob.es/en/ministerio/servicios/informacion/Parte7_tcm38-102783.pdf) | Glosario: `Ferrañales`, `pelo`; cap. 8 indirecto | suficiente |
| 38 | Estudio regional de prados de uno y dos pelos en las riberas septentrionales de León | publicación académica / agregador | [Modernalia](https://www.modernalia.es/items/show/2587) | `AGR-012`; caps. 7, 8 y 13 | mínima |
| 39 | *El Catastro de Ensenada, 1749–1759: diez años de intenso trabajo y 80.000 volúmenes manuscritos* | publicación académica / copia en plataforma | [ResearchGate](https://www.researchgate.net/publication/28109852_El_Catastro_de_Ensenada_1749-1759_diez_anos_de_intenso_trabajo_y_80000_volumenes_manuscritos) | `DEM-005`; cap. 6 | parcial |
| 40 | *Recursos naturales y molienda a mediados del siglo XVIII: la Tierra de Campos* | publicación académica / copia en plataforma | [ResearchGate](https://www.researchgate.net/publication/330029888_Recursos_naturales_y_molienda_a_mediados_del_siglo_XVIII_la_Tierra_de_Campos) | `HID-008`; caps. 9 y 13 | parcial |

No se han inventado autores, fechas, títulos editoriales, revistas, volúmenes, páginas, DOI ni fechas de consulta. Las etiquetas descriptivas reproducen únicamente lo que ya consta en el proyecto o en la propia URL registrada.

## 5. Completitud bibliográfica

| Clase | Criterio aplicado | Referencias | Porcentaje |
|---|---|---:|---:|
| Completa | datos aplicables suficientes para una referencia pública sin consulta adicional | 2 | 5 % |
| Suficiente | identificación inequívoca y utilizable; puede faltar un campo de estilo no esencial | 22 | 55 % |
| Parcial | autor o título reconocible, pero faltan varios campos bibliográficos | 8 | 20 % |
| Mínima | descriptor temático o institucional y URL, sin metadatos bibliográficos básicos | 8 | 20 % |
| Solo URL | ningún descriptor recuperable en el proyecto | 0 | 0 % |
| **Total** | 40 referencias; 41 URL | **40** | **100 %** |

Ninguna referencia registra fecha de consulta. Tampoco consta una política sobre cuándo debe incluirse. Los identificadores persistentes solo están presentes cuando forman parte de las rutas de repositorios o catálogos ya anotadas; no consta ningún DOI como tal. Veinticuatro referencias —las dos completas y las veintidós suficientes— pueden incorporarse a una bibliografía inicial con los datos presentes. Las dieciséis parciales o mínimas requieren verificación externa antes de presentarse como registros normalizados definitivos.

## 6. Auditoría de entradas E

| E-ID | Contexto | Fuente declarada | Completitud | Visible en capítulo | Visible en matriz | Bibliografía | Problema | Acción futura |
|---|---|---|---|---|---|---|---|---|
| TOP-004 | mención de `Sorribios` en 1215 | Jular Pérez-Alfaro | suficiente | prosa en cap. 3; ID no visible | sí; destino `—` | no | la afirmación no conduce a su fuente | cita próxima + retorno matriz/capítulo |
| TOP-005 | venta de heredamiento en 1267 | edición moderna; `AHN, Clero, carp. 828, núm. 11` | parcial | prosa en cap. 3; ID no visible | sí; destino `—` | no | faltan metadatos de la edición | cita próxima; verificar referencia |
| TOP-006 | antecedente genealógico de 1601 | *Nobiliario de la Montaña leonesa* | parcial | no; tampoco front matter | sí; destino `—` | no | entrada no transferida al relato | decidir si se cita o se conserva solo en matriz |
| TOP-007 | pleito de 1715 | PARES, signatura declarada | completa | prosa en cap. 3; ID no visible | sí; destino `—` | no | trazabilidad indirecta | cita próxima + retorno |
| TOP-008 | relación parroquial de 1768 | relación del obispo de Oviedo; `B.R.A.H.M.` | suficiente | prosa en cap. 3; ID no visible | sí; destino `—` | no | trazabilidad indirecta | cita próxima + retorno |
| TOP-009 | escritura de 1831 publicada en 1864 | *Gaceta de Madrid* | completa | prosa en cap. 3; ID no visible | sí; destino `—` | no | trazabilidad indirecta | cita próxima + retorno |
| TOP-010 | municipio en 1836/1848 | Álvarez-Balbuena | suficiente | prosa en cap. 3; ID no visible | sí; destino `—` | no | dos URLs para una obra; sin relación de destino | autoridad bibliográfica única + cita próxima |
| TOP-011 | identificación actual Sorrios/Santibáñez | Ayuntamiento | suficiente | prosa en cap. 3; ID no visible | sí; destino `—` | no | fuente institucional alejada | cita próxima + retorno |
| JUR-007 | Concejo histórico / municipio posterior | relación de 1768 + Álvarez-Balbuena | suficiente | prosa en cap. 5; ID no visible | sí, cap. 5 | no | fuente compuesta, solo una URL en la entrada | normalizar ambos componentes y citar cerca |
| JUR-008 | jurisdicción y XV conde de Luna | estudio de señoríos + PARES | parcial | prosa en cap. 5; ID no visible | sí, cap. 5 | no | una de dos fuentes es mínima | completar metadatos y cita próxima |
| JUR-009 | abogado de los Reales Consejos | PARES, expedientes de examen y título | suficiente | sí en cap. 12; no junto al uso de cap. 3 | sí, cap. 12 | no | cobertura desigual entre capítulos | enlazar los usos sustantivos |
| DEM-005 | categorías personales y medio vecino | estudio general del Catastro | parcial | prosa en cap. 6; ID no visible | sí, cap. 6 | no | faltan autor/datos editoriales | verificar y citar cerca |
| DEM-006 | 137 habitantes parroquiales en 1768 | relación parroquial de 1768 | suficiente | prosa en cap. 6; ID no visible | sí, cap. 6 | no | cautela no conectada a fuente | cita próxima con cautela |
| TER-011 | medición agraria por sembradura | recurso e-medida | parcial | agrupada en cap. 13; no próxima en cap. 7 | sí, caps. 7 y 13 | no | falta proximidad y autor | verificar; cita próxima en cap. 7 |
| AGR-011 | lino e hilaza en León | Juan Manuel Bartolomé | parcial | agrupada en cap. 13; no próxima en cap. 7 | sí, caps. 7 y 13 | no | faltan título/datos editoriales | verificar; cita próxima en cap. 7 |
| AGR-012 | prados de uno y dos pelos | Modernalia | mínima | agrupada en cap. 13; no próxima en caps. 7–8 | sí, caps. 7, 8 y 13 | no | referencia mínima | verificar; cita donde se usa |
| AGR-013 | léxico `ferrañal` | estudio de la Valduerna | mínima | agrupada en cap. 13; no próxima en caps. 7–8 | sí, caps. 7, 8 y 13 | no | referencia mínima | verificar; coordinar con glosario |
| GAN-008 | ganado `arenta` | estudio leonés de renta/aparcería | mínima | agrupada en cap. 13; no próxima en cap. 8 | sí, caps. 8 y 13 | no | referencia mínima | verificar; cita próxima en cap. 8 |
| HID-008 | molino hidráulico y estacionalidad | Zapico + comparación Tierra de Campos | parcial | sí, caps. 9 y 13 | sí, caps. 9 y 13 | no | dos fuentes incompletas | completar y enlazar marca E |
| TRA-006 | servicios por vecera | ordenanzas concejiles leonesas | mínima | sí, caps. 11 y 13 | sí, caps. 11 y 13 | no | recurso web débilmente identificado | verificar; conservar alcance comparativo |
| FIS-013 | Voto de Santiago | Ofelia Rey Castelao | parcial | sí, caps. 10, 12 y 13 | sí, caps. 10, 12 y 13 | no | faltan datos del artículo | completar; coordinar con nota/glosario |
| FIS-014 | Hospital de Inocentes | estudio de pobreza/hospitalidad | mínima | sí, caps. 11–13 | sí, caps. 11–13 | no | referencia mínima; no resuelve obligación | verificar sin cerrar `LIM-012` |
| FIS-015 | Honrado Concejo de la Mesta | PARES | suficiente | sí, caps. 11–13 | sí, caps. 11–13 | no | identifica institución, no pago local | normalizar; mantener `LIM-013` |
| FIS-016 | propios y arbitrios | estudio sobre hacienda local | mínima | sí, caps. 11 y 13 | sí, caps. 11 y 13 | no | referencia mínima | verificar antes de bibliografía final |
| FIS-017 | Corpus en respuestas leonesas | ejemplo Caboalles | mínima | sí, caps. 11 y 13 | sí, caps. 11 y 13 | no | comparación web mínima | verificar o decidir no citar autónomamente |

**Balance:** 25/25 entradas E auditadas; 25/25 visibles en la matriz; 13/25 tienen una trazabilidad operativa desde el ID visible en el cuerpo hasta la matriz y su enlace, aunque el salto no es directo; 11/25 presentan trazabilidad parcial porque están en prosa y front matter sin ID visible; 1/25 (`TOP-006`) solo está en la matriz; 0/25 están resueltas por bibliografía. Hay 27 enlaces declarados para 25 fuentes únicas de E. Veintidós entradas dependen de una referencia principal; tres (`JUR-007`, `JUR-008`, `HID-008`) combinan dos fuentes. La relación varios-a-uno aparece al menos en la relación de 1768 (`TOP-008`, `DEM-006`) y en Álvarez-Balbuena (`TOP-010`, `JUR-007`).

El índice rector afirma que existen ocho entradas externas condicionadas; el Registro 1.2 marca explícitamente como `Condicionada` solo `TOP-006` y `DEM-006`. Las demás conservan cautelas, pero su estado literal es `Admitida`. La futura implementación debe obedecer al Registro vigente y no convertir la cifra antigua del índice rector en estado canónico.

## 7. Caso de control: serie histórica del topónimo

La serie visible en el capítulo 3 es sólida y cauta:

- `Sorribios`: 1215 y 1267;
- `Sorribos`: 1715, cuatro apariciones manuscritas en 1752, relación de 1768, escritura de 1831 publicada en 1864, arreglo de 1836 y Madoz en 1848;
- `Sorrios`: identificación municipal actual.

El proyecto ya conserva las fuentes de Jular, la edición moderna de 1267, el *Nobiliario*, PARES 1715, la relación de 1768, la *Gaceta*, Álvarez-Balbuena y el Ayuntamiento. También conserva la cautela decisiva: la continuidad de identificación no reconstruye por sí sola toda la evolución fonética. `Sorribas` queda fuera de la serie como lectura paleográfica descartada.

El lector del capítulo 3 ve fechas, testimonios y cautelas, pero no ve IDs, notas ni enlaces próximos. El front matter enumera `TOP-004`, `TOP-005` y `TOP-007`–`TOP-011`, pero esa información es de control. La matriz contiene `TOP-004`–`TOP-011` y sus fuentes, aunque asigna a todas `Uso en el libro: —`. `TOP-006`, referido a 1601, no fue incorporado al capítulo ni a su front matter.

Este caso prueba la conveniencia del sistema híbrido recomendado: una llamada breve o ID enlazado al lado de cada bloque cronológico relevante, matriz para formulación/cautela y bibliografía para la referencia completa. No hace falta convertir cada fecha en una nota extensa ni copiar la lista de siete enlaces de 0.6.

## 8. Matriz REF

Cada recurso o problema recibe una sola clase principal.

| REF-ID | Recurso o problema | Clase | Prioridad | Diagnóstico / acción futura |
|---|---|---|---|---|
| REF-001 | Concordancia manuscrito–página–unidad–folio–respuesta | REF0 | — | resuelta y navegable |
| REF-002 | Matriz D/C/I/E/L de 112 entradas | REF0 | — | resuelta como control y aparato; no sustituye bibliografía |
| REF-003 | Enlaces institucionales próximos en capítulos 1–2 | REF0 | — | función básica resuelta, pendiente solo normalización común |
| REF-004 | Inventario bibliográfico único de 40 referencias / 41 URL | REF1 | ALTA | la información ya está localizada; convertir después en fuente estructurada única |
| REF-005 | Incorporación inicial de 24 referencias completas o suficientes | REF1 | ALTA | puede prepararse con datos existentes, sin inventar campos |
| REF-006 | Enlaces de marcas E del cuerpo hacia la matriz | REF1 | ALTA | IDs y anclas existen; falta navegación |
| REF-007 | Tratamiento de las 12 E sin ID visible en el cuerpo | REF1 | ALTA | añadir después llamadas selectivas para las once usadas en prosa, en especial en los capítulos 3 y 5–8; decidir por separado `TOP-006` |
| REF-008 | Destinos de `TOP-004`–`TOP-011` en la matriz | REF1 | ALTA | corregir `Uso en el libro: —` según usos reales; decidir `TOP-006` |
| REF-009 | Estructura pública del aparato de fuentes | REF1 | ALTA | separar manuscrito, edición documental, E, recursos y cartografía |
| REF-010 | Aparato compacto de cuestiones abiertas QA1 | REF1 | ALTA | nueve cuestiones pueden resumirse con datos actuales |
| REF-011 | Historia intelectual/editorial mínima | REF1 | MEDIA | versiones y cambios relevantes ya están documentados |
| REF-012 | Esqueletos de modelos de cita | REF1 | ALTA | los objetos, IDs, versiones y localizadores internos ya existen |
| REF-013 | Selección y forma final del aparato QA | REF2 | ALTA | decidir extensión, agrupación y relación con capítulos/matriz |
| REF-014 | Modelo híbrido CIT-B/C y densidad de llamadas | REF2 | ALTA | decidir antes de implementar |
| REF-015 | Nota al pie, paréntesis, enlace sobre ID o combinación | REF2 | MEDIA | debe ser equivalente y legible en HTML/PDF |
| REF-016 | Estilo CSL y puntuación bibliográfica | REF2 | MEDIA | no hay necesidad de fijarlo durante el diagnóstico |
| REF-017 | Política de fechas de consulta para webs vivas | REF2 | BAJA | decidir según estilo y estabilidad de la fuente |
| REF-018 | Metadatos de ocho referencias parciales | REF3 | ALTA | verificar autoría, título, fecha y publicación aplicables |
| REF-019 | Metadatos de ocho referencias mínimas | REF3 | ALTA | comprobar la fuente/registro antes de bibliografía final |
| REF-020 | Bases, fecha, licencia y atribución de mapas futuros | REF3 | ALTA | Auditoría B las necesita; no hay fuente elegida |
| REF-021 | Ampliaciones G3 de la Auditoría A | REF4 | MEDIA | cuatro voces exigirían investigación y nuevas referencias/E si se autorizan |
| REF-022 | Cierre sustantivo de `LIM-011`–`LIM-013` | REF4 | MEDIA | requiere nuevas fuentes históricas; no es requisito para declarar el límite en 1.0 |
| REF-023 | Recuperar el resumen narrativo del apéndice F de 0.6 | REF5 | — | duplica el estudio y no es una bibliografía |
| REF-024 | Convertir el libro en changelog de commits, hashes y pruebas | REF5 | — | debe quedar en dossier técnico |
| REF-025 | Adoptar literalmente los modelos provisionales de cita 0.6 | REF5 | — | dependen de identidad y versión ya superadas |

| Clase | Total |
|---|---:|
| REF0 | 3 |
| REF1 | 9 |
| REF2 | 5 |
| REF3 | 3 |
| REF4 | 2 |
| REF5 | 3 |
| **Total** | **25** |

Entre REF1–REF4 hay 19 acciones aplicables: **13 de prioridad ALTA, 5 MEDIA y 1 BAJA**. REF0 y REF5 no reciben prioridad de ejecución.

## 9. Modelos CIT-A / CIT-B / CIT-C

| Criterio | CIT-A — bibliografía + enlaces | CIT-B — cita próxima + bibliografía | CIT-C — matriz como núcleo |
|---|---|---|---|
| Legibilidad | alta, pero puede ocultar qué fuente sostiene cada contexto | alta si las llamadas son breves y selectivas | alta en la prosa; exige conocer los IDs |
| Trazabilidad | baja-media para las E | alta | alta desde el ID, baja cuando el ID no aparece |
| Densidad | mínima | controlable | mínima en capítulos, alta en matriz |
| HTML | enlaces directos sencillos | notas/enlaces próximos y bibliografía navegable | excelente si cada ID enlaza a su ancla |
| PDF | bibliografía localizable, pero afirmación y fuente quedan lejos | notas o autor-fecha próximos | búsqueda de ID posible; navegación requiere hipervínculo |
| Mantenimiento | sencillo | medio; hay que coordinar cita y bibliografía | medio; matriz y destinos deben mantenerse |
| D/C/I/E/L | relación débil | distingue bien E cuando se formula con cautela | preserva al máximo la estructura del Registro |
| Topónimo | insuficiente por sí solo | óptimo para bloques cronológicos | útil como segundo salto |
| Contexto histórico | puede parecer prosa sin fuente | hace visible el cambio de autoridad | conserva formulación, estado y cautela |
| Glosario | adecuado para apoyos léxicos simples | útil para definiciones discutibles | excesivo si cada voz exige pasar por la matriz |

## 10. Recomendación de sistema de citas

Se recomienda un **híbrido CIT-B/C**:

1. cita o llamada breve próxima a las afirmaciones externas sustantivas;
2. ID `E` enlazado a la matriz cuando exista;
3. matriz como lugar de formulación canónica, estado, cautela y relación con el libro;
4. bibliografía final normalizada como autoridad descriptiva de cada referencia;
5. enlace externo concentrado preferentemente en la bibliografía y conservado en la matriz cuando tenga valor de verificación.

No hace falta mostrar una llamada en cada frase. Deben priorizarse el topónimo, identificaciones personales o institucionales, comparaciones regionales que sostienen una interpretación, equivalencias léxicas y cualquier afirmación cuya autoridad sea externa al manuscrito. Las referencias institucionales de los capítulos 1–2 pueden conservar enlaces próximos, coordinados con la bibliografía general.

## 11. Estado de `references.bib`

El archivo contiene únicamente el comentario «Bibliografía de la publicación. Se incorporará en fases posteriores.»: **cero entradas BibTeX**. `_quarto.yml` ya lo declara como bibliografía, pero no hay citas `[@clave]`, estilo CSL específico ni lista bibliográfica renderizada.

Pueden estructurarse ya 24 referencias completas/suficientes y reservar claves estables para las otras 16. No deben fabricarse sus campos ausentes. Antes de cerrar estas últimas habrá que comprobar, según el tipo de recurso: autor/editor, título exacto, año, revista o monografía, volumen/número/páginas, entidad editora, identificador persistente y, si se aprueba esa política, fecha de consulta. La obra de Álvarez-Balbuena debe tener una sola entrada con dos ubicaciones ya registradas, no dos referencias duplicadas.

## 12. Aparato de fuentes y bibliografía

Las cinco funciones previstas pueden resolverse en cuatro módulos editoriales si «Fuentes» y «Bibliografía» comparten un apéndice con secciones distintas.

| Aparato/función | Contenido disponible | Hueco principal | Clase | Necesidad 1.0 | Solapamiento a evitar |
|---|---|---|---|---|---|
| Cuestiones abiertas | 13 LIM, secciones de límites y matriz | selección/agrupación QA | REF1/REF2 | sí, compacto | no repetir todos los límites de cada capítulo |
| Fuentes | manuscrito, edición, interrogatorio, otras fuentes documentales, procedencia interna | arquitectura pública y cartografía futura | REF1/REF3 | sí | no tratar documentos internos como bibliografía externa |
| Bibliografía | 40 referencias inventariadas | normalización de 16 y estilo | REF1/REF2/REF3 | sí | no confundir URL con registro completo |
| Historia de versiones | versiones canónicas, 0.6, candidata y rectificaciones | selección intelectual frente a Git | REF1/REF2 | sí, breve | no copiar el roadmap ni hashes de pruebas |
| Modelos de cita | objetos, IDs, versiones y localizadores | identidad, URL, fecha y versión final | REF1/REF2 | sí | no duplicar créditos o colofón |

El aparato conjunto de fuentes/bibliografía debería distinguir:

- manuscrito autoritativo y procedencia de reproducciones;
- Edición Crítica y ediciones documentales empleadas;
- interrogatorio de 1749 y recursos institucionales del Catastro;
- fuentes primarias externas medievales, modernas y contemporáneas;
- bibliografía histórica, metrológica, agraria y económica asociada a E;
- recursos léxicos e institucionales;
- cartografía, licencias y atribuciones, cuando existan;
- documentos internos solo en una nota de arquitectura editorial, no mezclados alfabéticamente con bibliografía pública.

## 13. Cuestiones abiertas y entradas L

Se asigna un único estado QA a cada entrada `LIM-*` vigente. No se añaden preguntas nuevas.

| QA-ID | Entrada L | Cuestión | Visibilidad actual | Clase | Tratamiento diagnóstico |
|---|---|---|---|---|---|
| QA-001 | LIM-001 | población total por individuos | caps. 6, 10 y 13; matriz | QA1 | incluir en síntesis de límites de 1.0 |
| QA-002 | LIM-002 | renta anual de los hogares | caps. 6, 10, 12 y 13; matriz | QA1 | incluir agrupada bajo población/economía doméstica |
| QA-003 | LIM-003 | producto agrario total | caps. 7 y 13; matriz | QA1 | incluir agrupada bajo producción no reconstruible |
| QA-004 | LIM-004 | relación celemín–quartal/fanega | caps. 7 y 13; matriz | QA1 | incluir como límite metrológico principal |
| QA-005 | LIM-005 | equivalencias carga–fanega–quartal | caps. 7, 9, 10, 12 y 13; matriz | QA1 | incluir con QA-004 |
| QA-006 | LIM-006 | equivalencia interna real–maravedí | caps. 7, 12 y 13; matriz | QA2 | opcional o nota técnica; no autónoma para 1.0 |
| QA-007 | LIM-007 | discrepancias R5/R10 | caps. 7 y 13; matriz | QA0 | ya visible y explicada con precisión |
| QA-008 | LIM-008 | desigualdad general no medible con activos parciales | caps. 6, 8, 9, 12 y 13; matriz | QA3 | conservar como guardarraíl, no como pregunta autónoma |
| QA-009 | LIM-009 | comercio neto y destino predominante | caps. 7–9, 12–13; matriz | QA1 | incluir agrupada bajo producción/mercado |
| QA-010 | LIM-010 | ruedas del molino venturero | caps. 9 y 13; matriz | QA0 | ya visible y suficiente |
| QA-011 | LIM-011 | título jurídico de alcabalas y pozo | caps. 5, 9, 10, 12 y 13; matriz | QA1 | incluir como agenda histórica explícita |
| QA-012 | LIM-012 | origen de los 15 reales al Hospital | caps. 11–13; matriz | QA1 | incluir como agenda histórica explícita |
| QA-013 | LIM-013 | naturaleza de los 10 reales de Mesta | caps. 11–13; matriz | QA1 | incluir como agenda histórica explícita |

| Clase QA | Total |
|---|---:|
| QA0 | 2 |
| QA1 | 9 |
| QA2 | 1 |
| QA3 | 1 |
| **Total** | **13** |

El aparato de 1.0 debería reunir las nueve QA1 en cuatro grupos: población/hogares; producción y mercado; metrología; derechos y obligaciones pendientes. Las QA0 pueden remitirse a sus capítulos; QA2 puede quedar como nota técnica o 1.1+; QA3 debe seguir visible donde limita inferencias, sin presentarse como proyecto autónomo de investigación.

## 14. Historia de versiones

| Producto | Versión/estado existente | Información útil para el lector |
|---|---|---|
| Manual Editorial | 1.6 | método y principales ampliaciones normativas, no su historial completo |
| Edición Crítica | 3.6 | base paleográfica vigente y rectificaciones intelectualmente relevantes |
| Estudio Histórico | 1.2 | incorporación de contexto externo A–F y Registro como control |
| Registro D/C/I/E/L | 1.2 | sistema de 112 entradas y 25 E; no cada cambio técnico |
| Introducción | 1.3 | guía vigente y procedencia del interrogatorio |
| Edición modernizada | 1.3 | integración de 40 preguntas verificadas y actualización del Estudio |
| Índice rector | 1.5 | arquitectura de 16 capítulos y aparatos previstos |
| Plan de composición | 0.5 | precedente de composición, no autoridad del libro final |
| Composición 0.6 | referencia editorial de 259 páginas | antecedente intelectual y visual; no autoridad textual |
| Candidata Quarto | `0.1.0-dev`, técnica preeditorial | transición a una sola fuente multiformato; no presentarla como 1.0 |
| Edición 1.0 | futura | identidad, fecha, URL y alcance finalmente aceptados |

La historia pública debería explicar la relación entre manuscrito, Edición Crítica, modernizada, Estudio/Registro, composición 0.6 y edición Quarto 1.0, y mencionar rectificaciones que cambian la comprensión —en especial `Sorribas` → `Sorribos`— sin convertirlas en polémica narrativa. Commits, SHA de salidas, herramientas, recuentos de pruebas, incidencias de sandbox y validaciones completas pertenecen al dossier técnico. El colofón puede conservar una referencia condensada al snapshot, pero no sustituir la historia intelectual.

## 15. Modelos de cita

| Objeto citable | Datos disponibles | Falta | Puede resolverse ahora | Dependencias |
|---|---|---|---|---|
| Volumen completo | título de trabajo, alcance, futura edición 1.0 | autoría, fecha, URL, versión aceptada | estructura sí; fórmula final no | identidad editorial y publicación |
| Facsímil | título del volumen, 18 páginas, procedencia/hash del manuscrito, cap. 14 | autoría editorial, URL pública, fecha/versión final | sí como modelo interno | créditos, licencia/procedencia y URL |
| Página del manuscrito | páginas digitales 1–18 y anclas estables | URL pública y forma final de referencia | sí | edición final |
| Folio | folios 306r–321v, portada/reverso/hoja posterior | datos generales de edición final | sí | identidad del volumen |
| Unidad | 35 IDs, etiquetas, orden, página y posición | forma tipográfica final | sí | política de citación |
| Respuesta | números 1–40, anclas, folios y modernizada 1.3 | datos generales de edición final | sí | identidad/URL final |
| Transcripción paleográfica | Edición Crítica 3.6, unidad/folio y ancla | responsabilidad nominal, fecha y URL públicas | estructura sí | créditos y publicación |
| Edición modernizada | versión 1.3, respuesta y ancla | responsabilidad nominal, fecha y URL públicas | estructura sí | créditos y publicación |
| Capítulo histórico | títulos, números 5–13 y anclas | autoría, fecha, versión/URL final | estructura sí | identidad editorial |
| Entrada de matriz | ID estable y ancla `evidencia-*` | versión pública y URL final | sí | política CIT-B/C |
| Fuente externa | inventario de 40; 24 utilizables ya | metadatos de 16; estilo y fechas de consulta | parcialmente | REF-016–REF-019 |

Todos los modelos pueden diseñarse ahora como plantillas de campos. Ninguno debe redactarse como fórmula definitiva mientras falten autoría, responsabilidades, fecha editorial, URL canónica y versión final.

## 16. Relación con créditos y colofón

| Destino | Información propia | No debe duplicar |
|---|---|---|
| Créditos | nombres, roles, responsables de transcripción/modernización, colaboradores, copyright y licencia | bibliografía y explicación metodológica extensa |
| Bibliografía | descripción normalizada de fuentes externas y documentales | roles personales y changelog |
| Modelos de cita | orden y campos para citar cada objeto | lista completa de créditos |
| Historia de versiones | hitos intelectuales y relación entre productos | commits/pruebas exhaustivos |
| Colofón breve | título/edición, fecha, producción editorial, versión final, URL y quizá snapshot condensado | historia extensa, bibliografía y resultados de validación |
| Dossier técnico | hashes, commits, herramientas, pruebas, informes de aceptación | narrativa destinada al lector |

La Auditoría C confirma para `REV-007` dependencias con autoría/roles, fecha, versión 1.0, URL, licencia cuando proceda, denominación de los productos citables y política de snapshot. No redefine el colofón aprobado por `DEC-010`.

## 17. Dependencias con Auditoría A

Los siete G1 pueden enriquecerse con conocimiento ya presente. Si esa mejora reutiliza fuentes externas existentes —por ejemplo `boto`, `vecera`, `arenta` o apoyos léxicos— deberá enlazar con la misma bibliografía normalizada y, cuando formule contexto externo sustantivo, con su E correspondiente. No hace falta investigación nueva para decidir esa arquitectura.

Las cuatro voces G3 (`añino`, `alcavalas`, `servicio ordinario y extraordinario` y `pobre de solemnidad`) requieren investigación externa antes de ampliar su contexto. Si se autoriza, cada resultado deberá evaluar nueva referencia, posible nueva entrada E, cita próxima, bibliografía e índices. Los candidatos de glosario siguen siendo provisionales y no justifican por sí solos nuevas referencias.

## 18. Dependencias con Auditoría B

- La cronología VIS-002 puede construirse con las fuentes topónimas existentes, pero necesita citas próximas y bibliografía normalizada.
- Los mapas VIS-003 y VIS-004 requieren todavía base, autoría, fecha, licencia, atribución, método de localización y memoria de elaboración; son REF3 ALTA.
- El diagrama VIS-025 se basa en capítulos, Registro y matriz: necesita una declaración de base/cautela, no bibliografía externa nueva.
- VIS-019 puede resolverse mediante el aparato QA1 diagnosticado aquí; no tiene que convertirse en un recuadro visual.
- Cualquier lista de mapas, figuras o tablas debe derivarse del inventario final y compartir los mismos créditos/procedencia para HTML y PDF.

## 19. Elementos resolubles con información actual

Sin investigación externa pueden prepararse, después de la decisión del usuario:

- inventario estructurado único de 40 referencias y deduplicación de la obra con dos URLs;
- 24 registros bibliográficos completos/suficientes, dejando campos desconocidos explícitamente vacíos;
- enlaces desde IDs E del cuerpo a la matriz y retornos reales desde `TOP-*`;
- citas próximas para las E hoy indirectas, sin alterar su formulación canónica;
- arquitectura del aparato de fuentes y bibliografía;
- aparato compacto con las nueve QA1;
- historia intelectual/editorial mínima;
- plantillas de los once objetos citables;
- base bibliográfica de la cronología, el diagrama interno y los contextos G1;
- separación de créditos, versiones, cita, colofón y dossier técnico.

## 20. Elementos que requieren verificación externa

La verificación bibliográfica posterior debe completar las ocho referencias parciales y las ocho mínimas, comprobar títulos/autores/fechas/publicaciones sin depender de inferencias desde nombres de archivo y decidir identificadores persistentes. Esta es normalización y comprobación bibliográfica, no necesariamente investigación histórica.

Por separado, la cartografía requiere seleccionar y comprobar fuentes, licencias y atribuciones. También deben comprobarse, cuando exista URL pública, la forma final de citar el volumen y sus partes. Ninguna de estas verificaciones se ejecutó en esta auditoría.

## 21. Elementos que requieren investigación histórica

La investigación sustantiva queda limitada a necesidades no presentes hoy en el corpus:

- posibles ampliaciones G3 aprobadas por el usuario;
- título jurídico de alcabalas y pozo (`LIM-011`);
- origen de la obligación al Hospital de Inocentes (`LIM-012`);
- naturaleza del derecho de Mesta (`LIM-013`);
- cualquier reconstrucción cartográfica histórica que exceda la orientación actual;
- equivalencias, secuencias fonéticas o explicaciones locales que la documentación actual prohíbe completar por analogía.

Estas investigaciones no son requisito para que 1.0 declare honestamente las preguntas abiertas. Solo serían requisito si el usuario decidiera resolverlas o ampliar el relato antes de publicar.

## 22. Decisiones pendientes del usuario

1. Aprobar, modificar o rechazar el híbrido CIT-B/C.
2. Fijar densidad y forma de las llamadas próximas en HTML/PDF.
3. Decidir si las nueve QA1 forman un aparato compacto y cómo se agrupan.
4. Decidir el destino de `TOP-006`: capítulo/cronología, solo matriz o no incorporar al libro.
5. Aprobar la arquitectura del aparato conjunto de fuentes y bibliografía.
6. Elegir después un estilo CSL y una política de fechas de consulta.
7. Determinar qué mejoras G1 entran en 1.0 y si se autoriza investigación G3.
8. Determinar si se intenta resolver `LIM-011`–`LIM-013` o se publican como agenda abierta.
9. Fijar los datos de autoría, roles, copyright, licencia, fecha y URL necesarios para citas, créditos y colofón.
10. Decidir el alcance visual/cartográfico de 1.0 antes de completar su bibliografía y atribuciones.

## 23. Mapa de impacto sobre el libro

| Decisión futura | Preliminares | Caps. 1–4 | Caps. 5–13 | Aparatos | Índices | HTML/PDF |
|---|---|---|---|---|---|---|
| CIT-B/C | guía de convenciones | enlaces institucionales y topónimo | llamadas E selectivas | matriz + bibliografía | posibles remisiones | anclas/notas equivalentes |
| Fuentes/bibliografía | mención de procedencia | Catastro e interrogatorio | 25 E | nuevo aparato | autores no pasan automáticamente al onomástico | enlaces persistentes y composición bibliográfica |
| QA1 | ruta de consulta | — | remisiones desde límites | aparato compacto | materias | anclas y retornos |
| Historia de versiones | nota de edición | capítulo 4 resumido | — | tabla breve | materias | sin changelog técnico |
| Modelos de cita | guía de uso | — | — | modelos de once objetos | — | URL/localizadores finales |
| Cronología | orientación | cap. 3 | cap. 5 | fuentes | topónimos | alternativa textual |
| Mapas | orientación | caps. 3 y 5 | cap. 9 si procede | créditos/bibliografía | lugares | atribución y accesibilidad |
| Glosario G1/G3 | convenciones | — | capítulos afectados | glosario/bibliografía/matriz | materias | regeneración controlada |
| Colofón | créditos coordinados | — | — | cierre breve | — | versión, fecha y URL finales |

## 24. Conclusión

El proyecto no carece de fuentes: conserva 40 referencias externas únicas, 41 URL, 25 contextos E íntegros en la matriz y una trazabilidad interna muy superior a la de 0.6. La carencia es editorial y bibliográfica: no existe una lista pública normalizada, solo 13 E tienen su ID visible en el cuerpo, la serie topónima queda sin llamadas próximas y `references.bib` no contiene registros.

La solución mínima coherente para 1.0 es un híbrido CIT-B/C, una bibliografía única, un aparato de fuentes claramente tipificado, una síntesis QA1, una breve historia intelectual y modelos de cita. Nueve recursos REF1 pueden construirse con información actual; cinco decisiones REF2 corresponden al usuario; tres bloques REF3 requieren verificación externa; dos REF4 solo se activarían si se autoriza investigación; y tres soluciones heredadas de 0.6 no deben recuperarse.

La auditoría no decide ni implementa ese sistema. Deja preparado el diagnóstico para la consolidación conjunta de Auditorías A/B/C.

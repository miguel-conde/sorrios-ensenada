# Auditoría B — gráficos, cartografía y recuadros

**Fecha:** 10 de octubre de 2026<br>
**Fase:** 6A — auditoría especializada previa a implementación<br>
**Baseline:** `7be36f60442e46bd5a4c74775e4ed5a5a8e7ba23`<br>
**Rama:** `feature/quarto-book`<br>
**Estado:** diagnóstico completado; decisiones e implementación pendientes<br>
**Alcance autorizado:** composición 0.6 + Plan de composición 0.5 + índice rector 1.5 + candidata Quarto actual

## 1. Objeto y alcance

Esta auditoría determina qué recursos visuales y explicativos necesita realmente la edición 1.0. Compara su **función editorial**, no su parecido formal: cartografía, cronología, recuadros de contexto, gráficos cuantitativos, tablas explicativas y diagramas conceptuales se consideran equivalentes solo cuando ayudan al lector a resolver la misma pregunta con igual o mayor claridad y rigor.

La operación es exclusivamente diagnóstica y documental. No crea mapas, gráficos, cronologías, diagramas ni recuadros; no selecciona proveedor cartográfico; no investiga fuentes externas; no modifica `project/`, `publication/`, la candidata ni sus derivados; y no inicia la Auditoría C. La composición 0.6 se usa como referencia editorial, nunca como autoridad histórica o textual.

El universo de decisión contiene **27 recursos funcionales**. No se cuenta como recurso independiente cada tabla de datos, cada filete de diseño ni cada reproducción del manuscrito. Los facsímiles se contabilizan aparte porque su función es documental, no explicativa.

## 2. Baselines y materiales

| Material | Identidad comprobada | Estatuto en la auditoría |
|---|---|---|
| Repositorio | `feature/quarto-book`; `HEAD` `7be36f60442e46bd5a4c74775e4ed5a5a8e7ba23`; upstream coincidente al inicio | baseline documental |
| Árbol `project/` | `e32917763475ceebdfe7b54830e1fb43f6419dad` | fuente canónica; solo lectura |
| Árbol `publication/` | `cfcf349928fe3e1f2d3b33c005c31fa5621b1878` | candidata; solo lectura |
| Composición 0.6 | 259 páginas; 6.806.113 bytes; SHA-256 `78551fc2bcc067634b97e6284b5a3b88b1916067851d51ee00b14e488e4187f4` | referencia editorial externa |
| Candidata Quarto | 334 páginas; 73.994.496 bytes; SHA-256 `f1eee2f465f554d3bf2b506d23a622967d1b4f1013ac657a774868e525688183` | salida técnica vigente; no regenerada |
| Plan de composición | `Plan_Composicion_Volumen_0_5.md`, versión 0.5 | contrato editorial previsto |
| Índice rector | `Indice_Referencia_Volumen_Final.md`, versión 1.5 | arquitectura editorial vigente |
| Auditoría A | `AUDITORIA_GLOSARIO_ESTUDIO_HISTORICO_V1_0.md` | dependencias históricas y léxicas |

La réplica 0.6 permanece fuera del checkout. La candidata se inspeccionó tal como estaba disponible; no se ejecutó Quarto ni se reconstruyó ninguna salida.

## 3. Metodología

Se aplicaron cinco controles complementarios:

1. lectura completa del Plan 0.5 y del índice rector 1.5 para extraer recursos prometidos y límites obligatorios;
2. inventario técnico de imágenes incrustadas y extracción de texto de ambos PDF;
3. inspección visual de hojas de contacto que cubren las **259 páginas de 0.6** y las **334 de Quarto**, seguida de revisión ampliada de páginas críticas;
4. contraste con los QMD actuales y los aparatos generados para comprobar equivalencia funcional, no solo presencia gráfica;
5. clasificación de cada función mediante una única etiqueta VIS.

Las etiquetas significan:

- **VIS0:** resuelto en Quarto, o sustituido por una solución equivalente o mejor;
- **VIS1:** reconstruible para 1.0 con fuentes internas actuales;
- **VIS2:** exige una decisión editorial previa;
- **VIS3:** exige una fuente, base o recurso externo;
- **VIS4:** no debe recuperarse en la forma auditada.

Solo VIS1–VIS3 reciben prioridad `ALTA`, `MEDIA` o `BAJA`. La prioridad expresa necesidad editorial, no autorización de implementación.

El recuento de `pdfimages` se trató como pista, no como inventario definitivo. En 0.6 localiza 73 imágenes incrustadas —tres paneles cartográficos y setenta reproducciones documentales—, pero omite los dos diagramas de las páginas 45 y 49 porque están compuestos como vectores. Este hallazgo corrige la limitación declarada en el informe comparativo anterior.

## 4. Inventario visual de 0.6

### Recursos explicativos

| Categoría | Recuento funcional | Ubicación | Resultado |
|---|---:|---|---|
| Láminas cartográficas | 2 láminas, 3 paneles | pp. 16–17 | situación peninsular, provincial y local |
| Diagramas conceptuales vectoriales | 2 | pp. 45 y 49 | modelo socioeconómico; red de vulnerabilidades y amortiguadores |
| Familias de tablas y matrices explicativas | 8 | pp. 19, 23–32, 34–43, 49–52 y 57 | lectura, población, tierra, producción, ganado, molinos, instituciones, flujos y vulnerabilidad |
| Cronología visual autónoma | 0 | — | la serie histórica está en prosa, no en un eje temporal |
| Ocho recuadros históricos diferenciados del Plan 0.5 | 0 como sistema completo | — | sus funciones aparecen parcialmente en prosa, tablas y notas |

Las dos láminas cartográficas cumplen funciones distintas. La página 16 contiene dos escalas dentro de una sola lámina: localización peninsular y provincial. La página 17 ofrece el detalle local con Santibáñez de Ordás, Santa María de Ordás, Villapodambre, Tapia de la Ribera, Rioseco de Tapia y `Sorribos / Sorrios`.

El primer diagrama, «Modelo socioeconómico integrado» (p. 45), enlaza hogares, tierra y cultivos, ganadería y comunes, río y molinos, común del lugar, Iglesia y señorío y conexiones exteriores. Su función sigue siendo valiosa, pero sus contenidos no pueden copiarse sin revisar: incluye formulaciones como `consumo`, `comunes` y relaciones que la candidata actual ha acotado con mayor rigor.

El segundo, «Red de vulnerabilidades y amortiguadores» (p. 49), presenta como nodos favorables `diversificación productiva` y `copropiedad, vecera y red molinera`, y trata `recursos de uso común` como función ambivalente. La candidata actual ya no permite convertir esos mecanismos potenciales en amortiguación observada ni usar copropiedad como conclusión general. Su forma antigua no es recuperable.

### Reproducciones documentales

0.6 incorpora **70 colocaciones del manuscrito**: 35 unidades en el facsímil por unidades (pp. 64–98) y 35 imágenes repetidas junto a la transcripción y el aparato (pp. 99–166). No son gráficos explicativos. Su evaluación pertenece a `REV-010` y `REV-016`, fuera de esta auditoría.

### Lectura del inventario

0.6 no era un sistema visual completo conforme al Plan 0.5. Resolvía bien la orientación cartográfica y ensayaba dos diagramas; concentraba el resto de la explicación en tablas densas y texto. No contenía la cronología gráfica ni los ocho recuadros históricos como serie editorial diferenciada. Por tanto, «recuperar 0.6» no equivale a cumplir el Plan.

## 5. Recursos previstos por Plan 0.5 e índice rector

Los documentos rectores prevén estas funciones:

- una cronología esencial en un único eje, con intervalos y fechas puntuales inequívocos;
- una lámina cartográfica a doble página con mapa regional y mapa local no redundantes;
- un esquema opcional del término descrito en 1752, solo si la evidencia lo permite y rotulado como reconstrucción;
- guía breve D/C/I/E/L;
- ocho tipos de recuadro histórico: nombre; Concejo/municipio; categorías demográficas; sembradura; lino/prados/ferrañales; ganado/molinos; instituciones/hacienda concejil; límites/preguntas abiertas;
- recursos específicos de transferencia: esquema administrativo, notas contextuales, cuadros de lectura, recuadro metrológico, tabla provincial de molinos, fichas institucionales, cuadro concejil, tabla de mínimos y diagrama integrado;
- gráficos solo cuando una relación no resulte clara en una tabla;
- lista de mapas y reproducciones y lista de cuadros y tablas.

El Plan impone además límites sustantivos: no proyectar el municipio actual sobre 1752; no convertir medidas históricas; no usar contextos regionales para fabricar datos locales; no completar contratos, títulos jurídicos o magnitudes ausentes; y separar observación, mecanismo, escenario y desconocido.

## 6. Recursos actuales de Quarto

La candidata contiene **44 tablas semánticas auditadas**, incluidas tablas de lectura demográfica, tierra y medidas, ciclos, valores ganaderos, molinos, fiscalidad, hacienda, dinero, relaciones del sistema y aparatos cuantitativos. Ofrece además 53 reproducciones documentales: 18 páginas facsimilares completas y 35 recortes de unidad.

No contiene mapas, cronología visual, diagramas conceptuales ni un sistema de recuadros históricos diferenciado. Sin embargo, esa ausencia formal no equivale a 27 carencias: la mayoría de las funciones prometidas está resuelta mediante prosa, tablas y aparatos más cautos que los de 0.6.

Resumen de la clasificación:

| Clase VIS | Recursos | Lectura |
|---|---:|---|
| VIS0 | 18 | función ya resuelta o mejor sustituida |
| VIS1 | 3 | reconstruible con fuentes internas |
| VIS2 | 2 | decisión editorial previa |
| VIS3 | 2 | fuente o base externa necesaria |
| VIS4 | 2 | no recuperar |
| **Total** | **27** | una fila por función editorial |

Por prioridad, los siete recursos VIS1–VIS3 se distribuyen en **5 altas, 1 media y 1 baja**.

## 7. Matriz VIS completa

| ID | Recurso | Tipo | Ubicación 0.6 | Previsto en Plan | Función | Base/evidencia | Estado Quarto | Riesgo histórico | VIS | Prioridad | Acción futura | Dependencias |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VIS-001 | Guía D/C/I/E/L | orientación | pp. 2, 18–21 | sí | explicar niveles de evidencia | Manual, Estudio y Registro | cap. 4 + matriz completa | bajo si se conserva la separación | VIS0 | — | no duplicar; coordinar su forma final con preliminares | REV-005, REV-006 |
| VIS-002 | Cronología toponímica y administrativa | cronología | serie en prosa, pp. 14–15; sin eje visual | sí | ordenar 1215–actualidad y situar 1752 | TOP-004–TOP-011, JUR-007; cap. 3 | prosa completa, sin visualización | confundir hitos, intervalos o continuidad fonética | VIS1 | ALTA | diseñar después un eje único desde datos internos, con fuentes y texto alternativo | Auditoría C; REV-005 |
| VIS-003 | Situación regional | cartografía | p. 16, dos paneles | sí | España → León → Ordás | localización actual y convención histórica | ausente | presentar localizadores actuales como límites históricos | VIS3 | ALTA | obtener base verificable y licenciada; redibujar, no copiar | Auditoría C; REV-002 |
| VIS-004 | Mapa local | cartografía | p. 17 | sí | relacionar Sorribos/Sorrios, Santibáñez y entorno | topónimos del cap. 5, R3 e índice de lugares | ausente | confundir topónimo histórico, núcleo actual, caminos o límites | VIS3 | ALTA | obtener base externa; validar escala, relieve, hidrografía y topónimos | Auditoría C; REV-002 |
| VIS-005 | Esquema del término de 1752 | cartografía interpretativa | no existe | opcional | representar dimensiones, linderos y figura de R3 | R3; figura marginal; cap. 5 | la prosa conserva magnitudes y advierte que no forman un polígono | falsa precisión geográfica o catastral | VIS4 | — | no producir para 1.0; reconsiderar solo si una futura fuente cambia la base probatoria | posible investigación futura |
| VIS-006 | Listas de mapas/reproducciones y cuadros/tablas | navegación | índice general; no listas propias | sí | localizar recursos no narrativos | metadatos de figuras y tablas | TOC e índices cubren parte de la función | bajo; riesgo principal de duplicación | VIS2 | BAJA | decidir tras fijar el aparato final si la ganancia compensa dos listas nuevas | REV-005; paginación final |
| VIS-007 | Serie documental del nombre | recuadro histórico | pp. 14–15 | sí | explicar `Sorribios` → `Sorribos` → `Sorrios` y sus límites | TOP-004–TOP-011; cap. 3 | prosa actual más clara y cauta | inventar una secuencia fonética completa | VIS0 | — | conservar la prosa; la orientación temporal corresponde a VIS-002 | Auditoría C |
| VIS-008 | Concejo histórico y municipio posterior | esquema administrativo | prosa, pp. 21–22 | sí | distinguir escalas y cambios de 1768/1789 frente a 1836/1848 | JUR-007; cap. 5 | prosa correcta, sin esquema | proyectar geografía decimonónica sobre 1752 | VIS1 | MEDIA | valorar un esquema cronológico-relacional compacto con etiquetas de fecha | VIS-002; Auditoría C |
| VIS-009 | Señorío, conde y juez subdelegado | nota contextual | pp. 22–23 y 38–40 | sí | separar dato local, identificación externa y cargo | JUR-008–009; caps. 3, 5 y 10 | explicación más rigurosa en prosa y tablas | señorío entendido como propiedad universal | VIS0 | — | no crear un recuadro autónomo salvo necesidad posterior de composición | Auditoría A: `Señorío` G1 |
| VIS-010 | Categorías demográficas | cuadro de lectura | pp. 23–25 | sí | distinguir vecino, medio vecino, avitador, residente y hogar | DEM-001–006; cap. 6 | varias tablas y cautelas explícitas | convertir categorías fiscales en población | VIS0 | — | conservar solución tabular; no añadir gráfico de población | Auditoría A: `medio vecino`, `avitadores`, `hijo de familia`, `pobre de solemnidad` |
| VIS-011 | Medición por sembradura | recuadro metrológico | pp. 25–28 | sí | explicar medida local y equivalencias internas | TER-003–005, TER-011; cap. 7 e índice de medidas | tabla y prosa completas | conversión moderna falsa | VIS0 | — | mantener tabla/prosa; no añadir escala moderna | Auditoría A: `quartal`, `fejes` |
| VIS-012 | Lino, prados y ferrañales | recuadro agrario | pp. 29–32 | sí | contextualizar ciclos y especialización sin extrapolar | AGR-011–013; cap. 7 | tablas y prosa con límites | atribuir circuitos concretos a la producción local | VIS0 | — | no duplicar como recuadro; mejorar referencias, si procede, en Auditoría C | Auditoría A |
| VIS-013 | Ganado «arenta» | nota comparativa | pp. 34–35 | sí | aclarar la relación documental sin completar contrato | GAN-008; cap. 8 | tabla y cautela textual | inventar propietarios, contrato o equivalencia | VIS0 | — | conservar; un recuadro ganadero no añade valor suficiente | Auditoría A: `arenta`, `añino` |
| VIS-014 | Molinos hidráulicos en contexto | cuadro comparativo | pp. 35–37 | sí | situar casas, ruedas, estacionalidad y paralelo provincial | HID-001–008; cap. 9 | tablas actuales distinguen casa, rueda, utilidad y límites | ocho ruedas tratadas como fijas; puente convertido en causa de paralización | VIS0 | — | conservar tablas; no restaurar la formulación 0.6 | Auditoría A: `molino venturero` |
| VIS-015 | Voto de Santiago | nota institucional | pp. 38–40 | sí | explicar el `boto` sin alterar cuantía ni producto | FIS-013; cap. 10 | prosa y tabla suficientes | completar el producto elidido o generalizar obligación | VIS0 | — | coordinar futura capa histórica del glosario, sin nuevo gráfico | Auditoría A: `boto` G1 |
| VIS-016 | Hospital de Inocentes y Mesta | fichas institucionales | pp. 39–43 | sí | identificar perceptores y mantener abiertas causa/naturaleza | FIS-014–015; LIM-012–013; cap. 11 | prosa contextual y límites expresos | inventar origen, título o asistencia local | VIS0 | — | no exigir dos fichas; la forma narrativa actual es suficiente | Auditoría C |
| VIS-017 | Propios, arbitrios, Corpus y vecera | cuadro concejil | pp. 40–43 | sí | distinguir ausencia de rentas, gastos, repartimiento y turno | FIS-005–007, FIS-016–017, TRA-006; cap. 11 | tabla de partidas + explicación | convertir subtotal en presupuesto o generalizar vecera | VIS0 | — | conservar tablas; enlazar conceptos si lo decide la revisión final | Auditoría A: `propios`, `arbitrio`, `vecera`, `repartimiento` |
| VIS-018 | Monetización y conexiones | tabla de mínimos | pp. 41–44 | sí | separar dinero, especie, trabajo, utilidad y pagos exteriores | FIS-009–012; cap. 12 | varias tablas y denominadores explícitos | convertir mínimo parcial en renta, carga total o balanza | VIS0 | — | conservar solución actual | Auditoría C |
| VIS-019 | Límites y preguntas abiertas | recuadro/aparato | disperso, especialmente pp. 50–60 y apéndice E | sí | reunir desconocidos y evitar cierres falsos | LIM-001–013 y cautelas de capítulos | límites dispersos en capítulos y matriz | simplificar límites complejos o presentarlos como respuestas | VIS2 | ALTA | decidir en Auditoría C forma, selección y ubicación; no forzar un recuadro visual | REV-004; Auditoría C |
| VIS-020 | Cabida, calidades y discordancias | tablas cuantitativas | pp. 26–28 | sí | hacer visibles sumas, denominadores y discrepancias | TER-006–010; CAL-001–002 | tablas del cap. 7 + cuadros generados | mezclar medidas y celemines o completar montes por residuo | VIS0 | — | mantener tablas; no convertir a gráfico porcentual sin necesidad | — |
| VIS-021 | Cultivos, ciclos y rendimientos | tablas cuantitativas | pp. 29–32 | sí | distinguir estructura, descanso y regulación de rendimiento | AGR-001–010; CAL-003–009 | tablas del cap. 7 + cuadros generados | presentar índice como superficie o cosecha observada | VIS0 | — | mantener formato tabular | — |
| VIS-022 | Ganadería y valores regulados | tablas cuantitativas | pp. 34–35 | sí | separar especie, producto, cadencia y utilidad | GAN-001–007; CAL-010–011 | tablas del cap. 8 + cuadros generados | inferir efectivos o producción total | VIS0 | — | mantener formato tabular; no crear gráficos de existencias | Auditoría A: `añino` |
| VIS-023 | Molinos, activos y capacidad | tablas cuantitativas | pp. 35–37 | sí | distinguir casas, ruedas, titulares, usuarios y utilidad | HID-001–007; CAL-012 | tablas del cap. 9 + cuadros generados | confundir ruedas, capacidad, producción y actividad | VIS0 | — | mantener formato tabular | — |
| VIS-024 | Derechos, cargas y flujos institucionales | matrices/tablas | pp. 37–43 | sí | relacionar sujeto, perceptor, concepto, base y cuantía | JUR, FIS y caps. 10–12 | tablas actuales más precisas | sumar conceptos heterogéneos o cerrar títulos desconocidos | VIS0 | — | conservar; cualquier esquema fiscal nuevo depende de Auditorías A/C | Auditoría A: `alcavalas`, `servicio ordinario y extraordinario` |
| VIS-025 | Modelo económico integrado | diagrama conceptual | p. 45 | sí | mostrar relaciones que la prosa obliga a recorrer entre caps. 5–13 | INT y cap. 13 actual | prosa y tablas rigurosas; falta visión relacional | reintroducir consumo, autosuficiencia, causalidad o propiedad no probados | VIS1 | ALTA | rediseñar desde el cap. 13 actual con leyenda D/I/L y equivalencia textual | Auditorías A/C; REV-009 |
| VIS-026 | Red de vulnerabilidades y amortiguadores de 0.6 | diagrama conceptual | p. 49 | no como forma cerrada; el Plan pide separar categorías | sintetizar riesgos y buffers | versión antigua del Estudio | cap. 13 corrige el marco y no afirma resiliencia | presenta copropiedad/diversidad como amortiguadores y mezcla dependencia, exposición y daño | VIS4 | — | no recuperar; cualquier síntesis válida debe integrarse en VIS-025 con el marco actual | REV-009 |
| VIS-027 | Arquitectura de fragilidad y resiliencia | matriz conceptual | pp. 49–57 | sí, como matriz/agenda | distinguir exposición, centralidad, sustitución y materialización | INT, LIM y cap. 13 | tablas y secciones actuales separan dependencia, exposición, daño y mecanismos posibles | convertir escenarios en hechos observados | VIS0 | — | conservar la solución narrativa/tabular actual; no duplicar la matriz antigua | VIS-025 |

## 8. Cartografía

### 8.1. Situación regional

La función es necesaria para 1.0: el lector debe recorrer con rapidez España, León, Ordás y los dos núcleos del expediente. La lámina 0.6 demuestra el valor editorial, pero no es un asset reutilizable por defecto. La futura pieza necesita base, procedencia, licencia, fecha y memoria de elaboración verificables. Su estatuto es **VIS3 ALTA**.

El mapa regional no debe insinuar que un círculo de localización sea un límite histórico, ni convertir una división administrativa actual en jurisdicción de 1752. Conviene mantener dos escalas complementarias solo si cada una aporta orientación distinta y sigue siendo legible al tamaño final de impresión.

### 8.2. Mapa local

También es necesario para 1.0 y es **VIS3 ALTA**. Debe mostrar la relación entre `Sorribos (1752) / Sorrios (actual)`, Santibáñez de Ordás, Santa María de Ordás, Rioseco, Villapodambre y Tapia, junto con hidrografía, relieve y referencias viarias útiles en la medida en que la base escogida las sostenga.

La rotulación histórica y la actual deben distinguirse. `Sorribas` no puede aparecer como variante histórica. Caminos, términos o límites actuales no deben proyectarse retrospectivamente. El mapa local no debe ser un simple acercamiento redundante del regional: su función es explicar relaciones espaciales que la vista regional no puede hacer legibles.

### 8.3. Esquema histórico del término

No se recomienda para 1.0. R3 proporciona dimensiones en unidades históricas, linderos y una figura marginal, pero no permite construir un polígono geográfico exacto. La candidata conserva correctamente esa limitación y reproduce el documento dentro del facsímil y del aparato.

La etiqueta es **VIS4** para la propuesta auditada: no debe recuperarse como mapa ni como perímetro esquemático porque produciría una falsa precisión. Una futura fuente independiente podría justificar una nueva evaluación; en ese caso sería otro recurso, con otra base probatoria, no la simple ejecución de la promesa opcional del Plan.

### 8.4. Requisitos futuros

Antes de implementar cartografía deberán documentarse, sin elegir todavía proveedor:

- finalidad y escala de cada panel;
- fuente de cada capa, fecha de consulta, autoría, licencia y atribución;
- coordenadas o método de localización y memoria reproducible de elaboración;
- distinción gráfica entre dato actual, dato documental e inferencia;
- escala, norte, leyenda, créditos y topónimos comprobados;
- equivalencia en color y escala de grises;
- legibilidad real en el formato PDF que se decida y adaptación responsiva en HTML;
- texto alternativo y una descripción larga o tabla de lugares que transmita la misma información;
- exportación vectorial cuando sea viable, con fallback accesible y sin depender solo del color;
- coordinación con el índice de lugares y con la bibliografía/créditos que resuelva la Auditoría C.

## 9. Cronología

La cronología visual prometida no existe ni en 0.6 ni en Quarto. El capítulo 3 contiene ya los hitos y las cautelas necesarios, por lo que su estatuto es **VIS1 ALTA**: puede reconstruirse sin investigación nueva.

La futura pieza debe usar un único eje. Las fechas puntuales deben situarse dentro de los intervalos que les corresponden; en particular, `17-IX-1752` debe quedar dentro del tramo `1750–1754`. Debe distinguir testimonios del topónimo, cambios administrativos y fecha del expediente, sin dibujar una evolución fonética continua que las fuentes no prueban. En HTML necesita una alternativa textual ordenada; en PDF no debe depender de tamaño diminuto, color o rotación incómoda.

La lista de fuentes y su forma de cita se decidirán en la Auditoría C. El dato cronológico, sin embargo, ya está dentro del repositorio.

## 10. Recuadros históricos

No se recomienda construir mecánicamente los ocho recuadros previstos. La unidad de evaluación es la función:

| Familia prevista | Diagnóstico |
|---|---|
| Serie del nombre | cubierta por el capítulo 3; la mejora útil es la cronología VIS-002 |
| Concejo y municipio | prosa correcta; esquema opcional VIS-008 puede añadir claridad |
| Categorías demográficas | resuelta por tablas y cautelas del capítulo 6 |
| Medición por sembradura | resuelta por tabla, prosa e índice de medidas |
| Lino, prados y ferrañales | resuelta por tablas y contexto del capítulo 7 |
| Ganado y molinos | resuelta por capítulos 8–9; no debe convertirse en un bloque único artificial |
| Instituciones y hacienda concejil | resuelta por capítulos 10–12 y sus tablas |
| Límites y preguntas abiertas | función no consolidada; VIS-019 depende de decisión y Auditoría C |

El resultado no prohíbe los callouts como recurso de composición futuro. Sí evita que una cuota de «ocho recuadros» duplique texto, fragmente la lectura o mezcle dato local con contexto externo. Cada eventual recuadro deberá tener fuente, cautela y propósito propios.

## 11. Gráficos cuantitativos

No se recomienda añadir gráficos cuantitativos nuevos para 1.0. Las magnitudes centrales exigen denominadores, unidades y cautelas que las tablas expresan mejor:

- cabida y calidad conservan medidas principales y celemines separados;
- 93,13 % y 72,16 % responden a denominadores distintos;
- los rendimientos son regulaciones, no cosechas observadas;
- las utilidades no son producción, ingreso o beneficio;
- no existen efectivos ganaderos completos;
- ocho ruedas en cuatro casas no equivalen a ocho ruedas siempre activas;
- el mínimo monetario parcial no es presupuesto ni carga total.

Un gráfico de barras, sectores o flujos monetarios tendería a borrar precisamente esos límites. Los cuadros generados y las 44 tablas actuales son una sustitución funcional mejor que un repertorio gráfico más vistoso.

## 12. Diagramas conceptuales

Se recomienda para 1.0 **un solo diagrama integrado**, VIS-025, reconstruido desde el capítulo 13 vigente. Su valor consiste en reunir relaciones distribuidas por nueve capítulos: hogares y trabajo; tierra y cultivos; ganado y usos comunes documentados; agua y transformación; común, concejo e instituciones; pagos y conexiones exteriores.

El diagrama debe distinguir visualmente:

- relación documentada;
- interpretación cauta;
- límite o ausencia;
- mecanismo potencial, sin presentarlo como efecto observado.

No debe afirmar autoconsumo, autosuficiencia, mercado integrado, crisis, resiliencia, propiedad comunal uniforme, copropiedad como amortiguador ni causalidad entre daños de puentes y paralización molinera. Debe tener una descripción textual completa y orden de lectura comprensible fuera del color.

No se recomienda un segundo diagrama autónomo de vulnerabilidades. La antigua red de la página 49 es VIS4 y duplicaría el modelo integrado. El marco actual del capítulo 13 —dependencia documentada, exposición plausible, daño observado y mecanismo potencial— debe gobernar cualquier visualización futura.

## 13. Recursos superados o que no deben recuperarse

No deben recuperarse:

- el esquema del término como supuesto perímetro de 1752;
- la red de vulnerabilidades y amortiguadores de la página 49;
- el lenguaje visual que convierta diversidad o copropiedad en amortiguación efectiva;
- cualquier gráfico que trate los 26 `avitadores` como población;
- gráficos de producción, ingresos, presupuesto, presión fiscal o mercado no calculables;
- la representación de ocho ruedas como parque fijo y operativo;
- mapas copiados de 0.6 sin trazabilidad de base y licencia;
- los ocho recuadros como cuota formal independiente de su utilidad;
- diagramas que recuperen `CLIMA` como nodo local o que unan puente dañado y molino parado sin evidencia;
- conversión gráfica de medidas históricas a superficies modernas.

La negativa se refiere a esas soluciones y afirmaciones. No impide crear en el futuro recursos distintos, sustentados por el corpus vigente y sujetos a sus propias validaciones.

## 14. Recursos recomendados para 1.0

El paquete recomendado es deliberadamente breve:

1. **VIS-002 — cronología visual**, con datos internos y prioridad alta;
2. **VIS-003 — situación regional**, tras resolver fuente, derechos y procedencia;
3. **VIS-004 — mapa local**, con función no redundante y los mismos controles;
4. **VIS-025 — diagrama económico integrado**, rediseñado desde el capítulo 13 actual;
5. decisión previa sobre **VIS-019 — límites y preguntas abiertas**, cuya forma final corresponde a la Auditoría C y no tiene por qué ser visual.

Este conjunto cubre orientación temporal, orientación espacial y comprensión relacional. No se recomienda añadir gráficos cuantitativos nuevos ni reconstruir los ocho recuadros. VIS-008 puede entrar en 1.0 solo si el usuario considera que la distinción Concejo/municipio todavía resulta difícil después de ver la cronología y el mapa.

## 15. Recursos opcionales o 1.1+

- **VIS-008**, esquema administrativo Concejo/municipio, si no se incorpora a 1.0;
- **VIS-006**, listas separadas de mapas/reproducciones y cuadros/tablas, una vez estable el inventario definitivo;
- mejoras interactivas HTML de mapas o diagramas, siempre con equivalente estático;
- cualquier ampliación cartográfica histórica que dependa de fuentes todavía no investigadas;
- conformidad formal de accesibilidad gráfica asociada al trabajo futuro PDF/UA o PDF/A.

No se coloca VIS-005 en este backlog como tarea ordinaria: permanece descartado mientras la base probatoria no cambie.

## 16. Dependencias con Auditorías A y C

### Auditoría A

La Auditoría A impone límites a cualquier recurso futuro:

- el cuadro demográfico no puede definir `pobre de solemnidad` ni fijar un coeficiente para `medio vecino` sin la decisión correspondiente;
- un recurso ganadero no puede resolver visualmente `añino` ni completar `arenta` más allá del contexto validado;
- un esquema fiscal no puede completar el título de las `alcavalas` ni el alcance de `servicio ordinario y extraordinario`;
- los G1 —`Señorío`, `medio vecino`, `propios`, `arbitrio`, `boto`, `vecera`, `hijo de familia` y candidatos internos— pueden informar recursos editoriales solo después de decidir su tratamiento;
- `entreparedes`, `fejes` y `pies de abejas` deben conservar sus límites y no adquirir equivalentes gráficos modernos.

### Auditoría C

La Auditoría C debe resolver antes de implementación:

- fuentes y citas visibles de cronología y contextos E;
- créditos, procedencia, licencia y atribución cartográficas;
- destino público de la memoria de elaboración de mapas;
- forma final de cuestiones abiertas y límites;
- política de notas, bibliografía y listas de ilustraciones/tablas;
- coordinación del diagrama integrado con sus evidencias y cautelas.

Esta auditoría no anticipa esas decisiones ni propone proveedores.

## 17. Mapa de impacto sobre el libro

| Recurso futuro | Preliminares | Capítulos | Aparatos/índices | HTML | PDF |
|---|---|---|---|---|---|
| Cronología VIS-002 | pieza después de convenciones o según P3 | remisión desde cap. 3 | índice de lugares; fuentes | reflow o alternativa textual | eje legible sin rotación forzada |
| Mapa regional VIS-003 | lámina cartográfica | remisión desde caps. 3 y 5 | índice de lugares; créditos; bibliografía | imagen responsiva + descripción | escala y rótulos a tamaño real |
| Mapa local VIS-004 | mismo conjunto, función diferenciada | remisiones desde caps. 5 y 9 | índice de lugares; créditos | zoom no imprescindible; alternativa completa | detalle suficiente y escala de grises |
| Esquema VIS-008 | no necesario | cap. 5 | fuentes/contexto | SVG accesible o tabla equivalente | composición compacta |
| Límites VIS-019 | quizá guía o remisión | caps. 5–13 | aparato narrativo decidido en C | anclas y retornos | evitar recuadros partidos |
| Diagrama VIS-025 | no | cap. 13 | matriz D/C/I/E/L e índice de materias | SVG + descripción larga | vector o alta legibilidad, no solo color |
| Listas VIS-006 | preliminares | — | metadatos de figuras/tablas | enlaces | páginas finales estables |

La implementación futura deberá comprobar que el contenido accesible sea equivalente en HTML y PDF, aunque la interacción no sea idéntica.

## 18. Decisiones pendientes del usuario

| Decisión | Opciones que esta auditoría deja abiertas | Recomendación diagnóstica |
|---|---|---|
| Alcance visual mínimo de 1.0 | ninguno; parcial; paquete recomendado | cronología + dos mapas + un diagrama integrado |
| Esquema Concejo/municipio | 1.0; 1.1+; no incorporar | 1.1+ salvo que una prueba de lectura muestre necesidad |
| Límites y preguntas abiertas | recuadro, apéndice, síntesis distribuida u otra forma | decidir en Auditoría C antes de cerrar 1.0 |
| Listas de recursos | dos listas, una combinada o navegación actual | diferir hasta conocer el inventario final |
| Ocho recuadros del Plan | cuota completa, selección funcional o ninguno | selección funcional; no reproducir la cuota |
| Esquema del término | intentar con R3 o no producir | no producir con la evidencia actual |
| Diagrama antiguo de vulnerabilidades | recuperar, rediseñar aparte o absorber | no recuperar; absorber solo relaciones válidas en VIS-025 |

Ninguna recomendación equivale a decisión del usuario ni autoriza cambios en la candidata.

## 19. Conclusión

La candidata no carece de explicación visual en bloque. De los 27 recursos funcionales auditados, **18 están resueltos** por prosa, tablas o aparatos equivalentes o mejores. La brecha real para 1.0 es pequeña y nítida: cronología visual, situación regional, mapa local y un diagrama integrado rediseñado; además, debe decidirse la forma de presentar límites y preguntas abiertas.

La composición 0.6 aporta dos buenos precedentes cartográficos y revela dos diagramas vectoriales antes no inventariados. No es, sin embargo, una plantilla recuperable: el segundo diagrama y el esquema opcional del término tienen riesgos históricos incompatibles con la candidata actual, y la mayoría de sus tablas ya ha sido superada funcionalmente por Quarto.

El siguiente paso es la Auditoría C. Solo después podrán cerrarse citas, derechos, procedencia, aparatos narrativos y decisiones humanas, y entonces preparar un plan de implementación atómico para una nueva candidata.

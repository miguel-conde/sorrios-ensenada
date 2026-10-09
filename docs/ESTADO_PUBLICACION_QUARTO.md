# Estado y roadmap de la publicación Quarto

**Actualizado:** 9 de octubre de 2026<br>
**Estado global:** Fase 6 en curso; candidata local intacta y revisión editorial consolidada en 26 entradas REV-*<br>
**Fase actual:** Fase 6A — decisiones de arquitectura y apertura previas a auditorías especializadas, correcciones y preview<br>
**Base de concurrencia de 6A:** `c1d0499340da92a28feeb9d3e121c68322190b38`<br>
**Upstream inicial de 6A:** `e74ce3cb8bd27921f50db5a046a0851528297ced`<br>
**Upstream comprobado antes del commit de candidata:** `e74ce3cb8bd27921f50db5a046a0851528297ced`<br>
**Commit de candidata técnica:** `49ab2e1b1a58ca9201efab54b42a3125de7326f8`

## Lectura de entrada

Una sesión nueva de Copilot debe leer, en este orden:

1. `PROJECT.md`;
2. `project/00_CONTROL/proyecto.yaml` y `estado.yaml`;
3. `.github/copilot-instructions.md`;
4. `docs/PLAN_MAESTRO_PUBLICACION_QUARTO.md`;
5. este roadmap;
6. `docs/ORDEN_DE_TRABAJO_PARA_V1_0.md`;
7. `docs/REVISION_EDITORIAL_CANDIDATA_1_0.md`;
8. `.github/instructions/publication.instructions.md`;
9. `publication/README.md`;
10. `docs/ESPECIFICACION_BOOTSTRAP_PUBLICATION.md` como registro de aceptación de la Fase 2A.

## Estado comprobado

- `main` y `origin/main` comprobados en `e81dc9239ac8dbabfe77168a50ef98c4d3b79170`; permanecen intactos.
- Edición Crítica 3.6, Estudio Histórico 1.2, Registro 1.2 y edición modernizada 1.3 vigentes.
- Índice rector 1.5 y Plan de composición 0.5 vigentes.
- Manuscrito: PDF autoritativo de 18 páginas en Drive, solo lectura; no está en GitHub.
- PDF completo 0.6: referencia editorial externa, no autoridad ni archivo del repositorio.
- Bootstrap mínimo de `publication/` publicado en `e9c3991ed72d9abf0469c11d87958bf934720f92`.
- Prototipo vertical 2B implementado, corregido y validado en los commits registrados en este roadmap.
- Capítulo 1 implementado en `030ea7e51fc42d23bf32d914df0bf6b0d7ddfda7` y aceptado mediante auditoría independiente con veredicto `APTO`.
- Capítulo 2 implementado en `3b07bdf0a4c22bfe0e97015005f087125328c484`, corregido técnicamente y aceptado mediante auditoría independiente final con veredicto `APTO`.
- Capítulos 3 y 4 implementados en `5d9f600a68702f0c061b04c821e83e56ab3baf9f`, corregidos técnicamente y aceptados mediante auditoría independiente final con veredicto `APTO`; cierran la Parte I sin correcciones pendientes.
- Capítulo 5 implementado en `ad891d9a072c292302f813f0a5536e6c29a3a1d9`, corregido técnica y editorialmente en `1fd074e8e4b6dade5585cf20cefc2d4cbb27651c` y aceptado mediante auditoría independiente final con veredicto `APTO`; abre la Parte II sin correcciones pendientes.
- Capítulo 6 implementado en `1c5cb13c661f7bd27a3a6a9d6849655ece2d63d2` y aceptado mediante auditoría final focalizada con veredicto `APTO`; distingue vecindad, residencia, hogares, viviendas y categorías laborales sin producir cifras no sustentadas de población, hogares o ingresos.
- Capítulo 7 implementado en `dcaa6378168b442a16cc37f5c684e2f5edcab119` y aceptado mediante auditoría final con veredicto `APTO`; reconstruye clases, calidades, cabidas, ciclos, rendimientos y medidas sin conversiones modernas, agregaciones incompatibles ni falsa precisión productiva.
- Capítulo 8 implementado en `e5ddab34ef757aef9ddfbe0b62229f9cb40746df` y aceptado mediante auditoría final con veredicto `APTO`; distingue especies, regulaciones unitarias, usos y recursos sin inventar efectivos, producción total, reparto doméstico, suficiencia material ni títulos de propiedad.
- Capítulo 9 implementado en `da76dbb3d7714d4e282f936efb1e1bc657d0dcff` y aceptado mediante auditoría final con veredicto `APTO`; distingue casas, ruedas, venturero, titulares, explotación, usuarios, utilidades, producción y capacidad, e integra colmenas y pozo de pesca sin falsas equivalencias ni estimaciones de actividad.
- Capítulo 10 implementado en `02dcc31ea6db8250013c99fbc37ecbd0747bcaeb` y aceptado mediante validación final con veredicto `APTO`; separa jurisdicción, señorío, propiedad, rentas, derechos fiscales y obligaciones vecinales, y distingue perceptores, bases, cantidades reguladas y pagos sin agregaciones heterogéneas ni indicadores fiscales no sustentados.
- Capítulo 11 implementado en `9ac6d90141e0c609b1961367c3333fbf1d86a318` y aceptado mediante validación final con veredicto `APTO`; distingue común, concejo y vecinos, reconstruye el repartimiento y los servicios documentados, y limita los 233 reales a un subtotal anual explícito sin inventar patrimonio, presupuesto, balance ni cobertura estable.
- Capítulo 12 implementado en `413d1e6bd7c03e71ee7ce0a47a2531be6caf1f35` y aceptado mediante validación final con veredicto `APTO`; distingue precios, valoraciones, utilidades, jornales, pagos y gastos, conserva separadas moneda, especie y servicio, y documenta oficios y conexiones exteriores sin fabricar una economía de mercado, ingresos anuales ni flujos comerciales.
- Capítulo 13 implementado en `fdcb18dc8e714dabfcba5032439074d8460f67e1` y aceptado mediante validación final con veredicto `APTO`; integra los capítulos 5–12, distingue dependencia, exposición y daño, formula mecanismos potencialmente amortiguadores sin afirmar resiliencia y cierra la Parte II sin convertir la síntesis en balance total.
- Fase 4A implementada en `6c27050fe478386f6a887c1efa1c4f25f9fbc6df`; el capítulo 14 presenta las 18 páginas completas del manuscrito autoritativo mediante derivados reproducibles no versionados.
- Fase 4B implementada en `bd0d20c18ba25d079a5faa34d51b5f82f3d5b0c2`; el capítulo 15 presenta las 35 unidades de la Edición Crítica 3.6, con imagen, transcripción paleográfica y aparato crítico fieles y reproducibles.
- Fase 4C implementada en `84f31b4249b745fe50799b8cfce2682913100d8e`; el capítulo 16 presenta las 40 preguntas verificadas y sus respuestas locales en español actual, con notas, cautelas y navegación material hacia el capítulo 15.
- Fase 4D implementada en `f9a7bf9d9a7e8cb70516e41105a472d7d7f3eed2`; el glosario, los cuadros cuantitativos, la concordancia y la matriz D/C/I/E/L se generan como cuatro vistas reproducibles de sus fuentes estructuradas.
- Fase 5A implementada en `16084c95691d879675859030059c9bf25af1c7dc`; los nueve índices se generan desde sus fuentes estructuradas y comparten destinos para localizadores HTML y páginas PDF resueltas por LaTeX.
- Fase 5B implementada en `e74ce3cb8bd27921f50db5a046a0851528297ced`; el volumen completo queda auditado y corregido en estructura editorial, reproducibilidad, HTML, PDF y accesibilidad básica, sin modificar fuentes canónicas.
- Candidata técnica 1.0 preparada en `49ab2e1b1a58ca9201efab54b42a3125de7326f8`; snapshot, reconstrucción, HTML, PDF, seguridad y preview local están validados. El informe reproducible está en `docs/CANDIDATA_PUBLICACION_1_0.md`.
- Revisión editorial 6A.1 completada contra la composición 0.6 y posteriormente consolidada con la primera ronda de observaciones del usuario. `docs/REVISION_EDITORIAL_CANDIDATA_1_0.md` contiene 26 observaciones propuestas y ninguna decisión definitiva; `docs/ORDEN_DE_TRABAJO_PARA_V1_0.md` es la referencia de trabajo consolidada, no una fuente histórica.
- HTML y PDF técnicos renderizados correctamente; ninguna salida de render está versionada.
- No hay migración de capítulos en bloque ni configuración de despliegue.

## Fases

| Fase | Estado | Resultado / puerta |
|---|---|---|
| 0. Auditoría de viabilidad y volumen 0.6 | completada | inventario, procedencia y problemas de regresión identificados |
| 1. Diseño editorial y técnico v0.1 | completada | 16 capítulos, árbol objetivo, matriz manual/generado y estrategia de facsímil fijados |
| 1B. Contexto autosuficiente para Copilot | completada | instrucciones, plan, especificación y roadmap versionados |
| 2A. Bootstrap y smoke test | completada | implementación `e9c3991ed72d9abf0469c11d87958bf934720f92`; HTML, PDF y tests en PASS; `project/` intacto |
| 2B. Prototipo vertical | completada | muestra vertical multiformato validada; trazabilidad, facsímil, paleografía, modernización y aparato integrados |
| 3. Contenido editorial | completada | Fases 3A–3L completadas; capítulos 1–13 aceptados; Parte II cerrada |
| 4. Generación documental | completada | capítulos 14–16 y los cuatro aparatos reproducibles de 4D cerrados y validados |
| 5. Índices y calidad integral | completada | 5A y 5B cerradas: índices, calidad integral y accesibilidad básica validados |
| 6. Preview y publicación 1.0 | en curso | candidata local validada e intacta; decisiones editoriales, tres auditorías especializadas, correcciones, preview remoto y aceptación pendientes antes de 6B |

## Siguiente tarea exacta

Decisiones editoriales de arquitectura y apertura de la candidata 1.0, antes de las tres auditorías especializadas y antes de cualquier modificación del libro.

### Descomposición operativa de la Fase 4

| Tarea | Estado | Alcance |
|---|---|---|
| 4A | completada | infraestructura de generación y capítulo 14, «Facsímil íntegro del expediente» |
| 4B | completada | capítulo 15, transcripción y aparato crítico de las 35 unidades |
| 4C | completada | capítulo 16, edición modernizada |
| 4D | completada | glosario, cuadros cuantitativos, concordancia y matriz de evidencia |

### Descomposición operativa de la Fase 5

| Tarea | Estado | Alcance |
|---|---|---|
| 5A | completada | nueve índices reproducibles y localizadores HTML/PDF |
| 5B | completada | calidad integral y accesibilidad |

### Descomposición operativa de la Fase 6

| Tarea | Estado | Alcance |
|---|---|---|
| 6A | en curso; pendiente de proveedor | candidata reproducible y validada; faltan decisiones editoriales, auditorías especializadas, implementación posterior y, finalmente, proveedor y preview remoto para aceptación humana |
| 6A.1 | consolidada; decisiones pendientes | comparación 0.6, observaciones del usuario, 26 REV y orden de trabajo documentados; no modifica la candidata ni cierra 6A |
| 6B | pendiente | publicación 1.0, etiqueta y cierre; prohibida antes de la aceptación humana del preview |

### Cierre comprobado de 2A

- Implementación atómica publicada: `e9c3991ed72d9abf0469c11d87958bf934720f92`.
- `prepare.py`: dos ejecuciones directas en PASS; mismo estado y escrituras limitadas a `generated/`.
- Tests existentes: 34 en PASS.
- `quarto check`: PASS con Quarto 1.7.31 y TinyTeX 2026.
- HTML: PASS; portada, capítulo técnico, navegación y búsqueda generados.
- PDF: PASS con LuaHBTeX 1.24.0; 4 páginas, texto seleccionable e inspección visual correcta.
- Dependencias bloqueantes: ninguna; Quarto resolvió LuaLaTeX desde TinyTeX aunque no estaba en el `PATH` de la shell.
- `project/`, `plugins/`, `tests/` y las instrucciones permanecieron intactos en el commit de implementación.
- Ningún PDF, `_book/` ni contenido de `generated/` quedó versionado.

## Cierre comprobado de 2B

- Implementación 2B: `a5dd318203fad847b6429e47ccd10b6b5b6c165b`.
- Corrección de lineación: `ad70d0bbfc08e9c59abe57ede8c5f8440fef7c01`.
- Formalización del flujo local-first: `88286ef68642811daada1841bd5757dfc7adc117`.
- Paleografía: 18 líneas y siete guiones documentales conservados.
- Generación: seis derivados idempotentes.
- Tests existentes: 47 en PASS.
- `quarto check`: PASS.
- Render multiformato HTML/PDF: PASS.
- Validador estricto: PASS.
- PDF: 15 páginas; inspección visual aceptada.
- `project/`, `plugins/` y `main` permanecieron intactos.
- Ningún PDF ni derivado quedó versionado.

## Cierre comprobado de 3A

- Implementación: `030ea7e51fc42d23bf32d914df0bf6b0d7ddfda7` (`feat(publication): add chapter 1`).
- Auditoría independiente: `APTO`; ninguna corrección pendiente antes del cierre.
- Capítulo 1 creado como primer capítulo editorial real de la Parte I; fuentes, límites con los capítulos 2–4 y separación entre dato local y contexto externo aceptados.
- Composición: preliminares no numerados y capítulo nuevo numerado correctamente como capítulo 1; prototipo 2B conservado sin regresiones.
- Generación: dos preparaciones idempotentes y seis derivados con SHA-256 idénticos.
- Validación: validador estático y renderizado en PASS; 48 tests en PASS; `quarto check` y render multiformato HTML/PDF en PASS.
- HTML: ocho páginas, con el capítulo navegable y numerado como 1. PDF: 19 páginas, con el capítulo 1 en las páginas 6–8; inspección visual de esas páginas en PASS.
- Regresión 2B: 18 líneas paleográficas y siete guiones documentales conservados.
- Integridad: `project/`, `plugins/`, fuentes canónicas y `main` intactos; ningún PDF, `_book/` ni derivado versionado; ninguna dependencia bloqueante.

## Cierre comprobado de 3B

- Implementación: `3b07bdf0a4c22bfe0e97015005f087125328c484` (`feat(publication): add chapter 2`).
- Primera corrección técnica: `096c24830eb1ec207e20cdf6e5538f01cffeb60c` (`fix(publication): align validation with render workflow`).
- Segunda corrección técnica: `2322ea31d285fd25534d61890da5532a15da03aa` (`fix(publication): detect bare questionnaire markers`).
- Auditorías independientes: editorial inicial `APTO CON AJUSTES`, sin defectos de contenido; primera corrección `APTO CON AJUSTES`, por el marcador sin sufijo; auditoría final `APTO`, sin correcciones pendientes.
- Resultado editorial: capítulo 2, «Las Respuestas Generales y el interrogatorio de cuarenta preguntas», incorporado como segundo capítulo editorial real de la Parte I. No duplica las cuarenta preguntas: las organiza mediante un cuadro de diez bloques temáticos; la pregunta 29 conserva su incidencia de transmisión documentada; formulario externo y respuesta local mantienen autoridades separadas.
- Fronteras: preservadas con los capítulos 1, 3, 4 y 16. El capítulo 2 no fue modificado durante las correcciones técnicas.
- Generación: preparación ejecutada dos veces; seis derivados con SHA-256 idénticos. Se conservaron 18 líneas paleográficas y siete guiones documentales.
- Validación: validador estático y renderizado en PASS; `quarto check`, render multiformato HTML/PDF y regresiones 3A/2B en PASS; suite final de 61 tests en PASS, también con el PDF ignorado todavía presente.
- Composición: nueve páginas HTML; PDF de 22 páginas, con el capítulo 2 en las páginas 9–11; ninguna dependencia bloqueante.
- Política de PDFs: los PDFs seguidos o no ignorados se rechazan; el PDF reproducible de `_book/` se permite y permanece ignorado. Ningún PDF, `_book/` ni derivado quedó versionado.
- Integridad: `project/`, `plugins/`, fuentes canónicas y `main` permanecieron intactos.

## Cierre comprobado de 3C

- Implementación: `5d9f600a68702f0c061b04c821e83e56ab3baf9f` (`feat(publication): add chapters 3 and 4`). Correcciones técnicas: `efd403cc414e38fc0e1d1aa164e9012c5439d7eb` (`fix(publication): strengthen phase 3C semantic validation`), `1bff0c633c6fb1c63b1404a743a087f31a3f57a7` (`fix(publication): make phase 3C relation checks polarity-aware`), `899a927acf9718aada83e29987441008ceb48d88` (`fix(publication): scope phase 3C relations by clause`) y `399c9b3a5abf59da84984c9b45ed688025de50c4` (`fix(publication): distinguish phonetic attribute polarity`).
- Resultado editorial: el capítulo 3, «El expediente de Sorribos y Santibáñez de Ordás», describe el expediente histórico local, sus participantes, materialidad, cierre y evolución positiva del topónimo; el capítulo 4, «Del manuscrito al volumen actual», explica las capas documentales y editoriales, la trazabilidad y la separación entre `content/` y `generated/`. Ambos capítulos cierran la Parte I.
- Fronteras: se preservaron la separación con la Parte II y con los capítulos generados; las fuentes canónicas no fueron modificadas.
- Auditorías: la auditoría editorial inicial fue `APTO CON AJUSTES`, sin defectos históricos o editoriales en los capítulos. Las auditorías técnicas intermedias detectaron y permitieron corregir cobertura semántica, polaridad, orden sintáctico, asociación por subcláusulas y uso atributivo de `documentada`. La auditoría independiente final de `399c9b3a5abf59da84984c9b45ed688025de50c4` fue `APTO`; no quedan defectos bloqueantes dentro del contrato validado.
- Validación semántica: parser único con separación de front matter y cuerpo y validación por secciones, proposiciones y subcláusulas; matriz adversarial anterior `34/34`, matriz ampliada `21/21` y total independiente `55/55`; pruebas fonéticas focalizadas `18 passed`, regresiones semánticas focalizadas `65 passed`, suite completa final `126 passed` y validador estático en PASS.
- Generación y composición: preparación idempotente de seis derivados con hashes conservados; `quarto check` y render conjunto HTML/PDF en PASS; 11 documentos HTML y PDF de 29 páginas, con el capítulo 3 en las páginas 12–14 y el capítulo 4 en las páginas 15–18; inspección visual aceptada.
- Regresiones e integridad: 18 líneas paleográficas, siete guiones documentales y seis secciones canónicas conservados; ningún PDF, `_book/` ni derivado versionado; ninguna dependencia bloqueante; `project/`, `plugins/`, fuentes canónicas y `main` intactos.
- La auditoría final focalizada no repitió el render porque el último diff solo afectaba al validador y sus pruebas; el render completo ya había pasado en el commit de corrección.

## Cierre comprobado de 3D

- Implementación: `ad891d9a072c292302f813f0a5536e6c29a3a1d9` (`feat(publication): add chapter 5`). Corrección técnica y editorial: `1fd074e8e4b6dade5585cf20cefc2d4cbb27651c` (`fix(publication): tighten chapter 5 validation`).
- Resultado editorial: el capítulo 5, «Un lugar de señorío en el Concejo de Ordás», abre la Parte II y distingue lugar, común, vecinos, Concejo de Ordás y municipio posterior. Separa el Concejo histórico de la configuración municipal decimonónica y el `Conde de Luna` documental de la identificación externa del XV conde. Interpreta conjuntamente las respuestas 2, 22, 28 y 29 sin convertir la exención por establecimiento del suelo en ausencia general de derechos; conserva `LIM-011`; presenta las dimensiones y la figura del término sin conversiones modernas; mantiene las fronteras con los capítulos 6, 7, 9, 10 y 11; y no modifica fuentes canónicas.
- Procedencia aceptada: D — `JUR-001`, `JUR-002`, `JUR-005`, `JUR-006`, `FIS-012`; E — `JUR-007`, `JUR-008`; L — `LIM-011`. No se declararon C ni I. `JUR-007` permaneció bajo E y la formulación interpretativa inicial se sustituyó por una descripción externa de una configuración administrativa posterior; el Registro no fue modificado.
- Auditorías: la primera auditoría fue `APTO CON AJUSTES`; consideró sólidos el contenido editorial y el render y pidió ampliar las variantes sobre la respuesta 22 y el conocimiento del título jurídico, conservar las fronteras de párrafo y reformular `JUR-007`. La auditoría final focalizada de `1fd074e8e4b6dade5585cf20cefc2d4cbb27651c` fue `APTO`; no queda ningún defecto bloqueante ni corrección pendiente de 3D.
- Validación semántica: pruebas focalizadas `27 passed`; arnés focal independiente `12/12`; arnés independiente de fronteras `8/8`; suite completa `152 passed` antes y después del render; colección estable de 152 identificadores, sin `skip` ni colección condicional, con hash `cb37d5e676e9297719bf8fe3b714eae238efdf47090942f9bb20518ddf17e14f`.
- Generación y composición: `prepare.py` se ejecutó dos veces y conservó seis derivados idempotentes con sus hashes aceptados; validador estático y `--rendered`, `quarto check` y render HTML/PDF en PASS; 12 documentos HTML y PDF de 32 páginas y 3.610.801 bytes, con el capítulo 5 en las páginas 19–21; inspección visual aceptada.
- Regresiones e integridad: 18 líneas paleográficas, siete guiones documentales y seis secciones canónicas conservados; ningún PDF, `_book/` ni derivado versionado; ninguna dependencia bloqueante; `project/`, `plugins/`, fuentes canónicas y `main` intactos.

## Cierre comprobado de 3E

- Implementación atómica: `1c5cb13c661f7bd27a3a6a9d6849655ece2d63d2` (`feat(publication): add chapter 6`). No fue necesario un commit posterior de corrección: los ajustes de validación y paginación se resolvieron antes del commit.
- Resultado editorial: el capítulo 6, «Vecinos, hogares, viviendas y trabajo», distingue persona, vecino, medio vecino, residente, hogar, casa, recuento vecinal-fiscal, oficio, ocupación, condición laboral y fuente potencial de ingreso. Conserva `avitadores` como forma documental y explica que 18 vecinos + 8 medios vecinos = 26 reproduce la suma de la respuesta 21, no una población de individuos; tampoco agrega los ocho residentes ni aplica coeficientes genéricos. Separa las 40 casas habitables, dos arruinadas y quince pajares de hogares y viviendas ocupadas; mantiene no aditivas las categorías de 18 jornaleros, 24 labradores y un herrero-labrador; y no transforma utilidades diarias en ingresos anuales.
- Procedencia aceptada: D — `DEM-001`–`DEM-004`, `GAN-007`, `TRA-001`–`TRA-005`, `FIS-007`; C — `CAL-018`, `CAL-019`; I — `INT-002`, `INT-008`, `INT-010`; E — `DEM-005`, `DEM-006`; L — `LIM-001`, `LIM-002`, `LIM-008`. Las afirmaciones directas adicionales sobre pobres de solemnidad y eclesiásticos conservan localizador de respuesta y folio; no se modificó el Registro.
- Validación semántica: matriz D/C/I/E/L completa; 16 pruebas focalizadas del capítulo 6 en PASS, incluidas diez mutaciones adversariales y cinco formulaciones cautelares; suite completa final `168 passed`, sin `skip`, con hash de colección `914a4fabdea5ca941bf13a6646a5df9cb39a3972ae9fa59420756a0274aafe7d`; validador estático y `--rendered` en PASS.
- Generación y composición: `prepare.py` se ejecutó dos veces y conservó idénticos los SHA-256 de los seis derivados; `quarto check` en PASS con Quarto 1.7.31 y TinyTeX 2026; render multiformato HTML/PDF en PASS; 13 documentos HTML y PDF de 38 páginas y 3.627.444 bytes, con el capítulo 6 en las páginas 22–27.
- Inspección visual: título, numeración, navegación anterior/siguiente, anclas, tablas y saltos revisados. Las colisiones iniciales con el pie en las páginas 23–25 se corrigieron antes del commit; la tabla laboral conserva encabezado al continuar y el resultado final es legible y no presenta desbordes.
- Auditoría final: `APTO`. No se detectaron confusiones vecino/habitante, hogar/vivienda, dobles conteos, ponderación falsa de medios vecinos, normalización injustificada de `avitadores`, estimaciones falsas de población o ingresos, cifras sin procedencia, contradicciones con los capítulos 1–5 ni anticipación de los capítulos 7–13.
- Regresiones e integridad: 18 líneas paleográficas, siete guiones documentales y seis secciones canónicas conservados; `git diff --check` en PASS; ningún PDF, `_book/` ni derivado versionado; `project/`, `plugins/`, fuentes canónicas y `main` intactos; ninguna dependencia bloqueante.

## Cierre comprobado de 3F

- Implementación atómica: `dcaa6378168b442a16cc37f5c684e2f5edcab119` (`feat(publication): add chapter 7`).
- Resultado editorial: el capítulo 7, «Tierra, sistema agrario y medidas», integra las trece clases de tierras y aprovechamientos, la distribución no uniforme de calidades, las discordancias entre las respuestas 5 y 10, la cabida por sembradura, cultivos, alternancias, descansos y rendimientos regulados. Distingue cabida, simiente, producto, rendimiento y valor; conserva por separado el total escrito de 3.823 medidas y un celemín y la suma de 3.811,5 medidas principales más siete celemines; y no reconstruye montes por residuo.
- Resultados cuantitativos: 666 / 1.398 / 1.747,5 medidas principales por calidad sobre el denominador 3.811,5; cabida cultivada comparable de 2.953,5 y centenal de 2.750,5; pesos centenales de 93,13 % y 72,16 % con denominadores distintos; índice mecánico anualizado de 1.578,25 unidades activas medias y 87,14 % centenal, expresamente identificado como escenario analítico y no como superficie sembrada observada.
- Procedencia aceptada: D — `TER-001`–`TER-006`, `TER-010`, `AGR-001`–`AGR-003`, `AGR-007`–`AGR-008`, `AGR-010`; C — `TER-007`–`TER-008`, `AGR-004`–`AGR-006`, `AGR-009`, `CAL-001`–`CAL-009`; I — `INT-001`, `INT-003`; E — `TER-011`, `AGR-011`–`AGR-013`; L — `TER-009`, `LIM-003`–`LIM-007`, `LIM-009`.
- Límites preservados: ninguna equivalencia métrica de legua, vara, `quartal`, fanega, celemín, carga, libra, montón o carro; solo se usan las relaciones internas cuatro `quartales` por fanega y cuatro montones por carro. No se mezclan unidades, no se calcula producto agrario total, no se convierte alternancia en rotación completa y no se deducen autoconsumo, suficiencia, productividad por hogar o trabajador ni nivel de vida.
- Validación semántica: 22 pruebas específicas del capítulo 7 en PASS —estructura y procedencia, dieciséis mutaciones adversariales y cinco formulaciones cautelares—; suite completa final `190 passed`, sin `skip`, con hash de colección `8d083bb553fb21ec973269ad69e75a1a4569deea698f7b3c83d4a31f5a10e483`.
- Generación y composición: `prepare.py` se ejecutó dos veces con SHA-256 idénticos para los seis derivados; validador estático y `--rendered`, `quarto check` y render HTML/PDF multiformato en PASS. El PDF final tiene 47 páginas y 3.656.317 bytes; el capítulo 7 ocupa las páginas 29–36.
- Inspección visual: título, numeración, navegación, anclas, nueve secciones, tablas, continuaciones con encabezado repetido, saltos y pies revisados en las ocho páginas; no se detectaron desbordes ni colisiones. La navegación HTML enlaza los capítulos 6, 7 y el prototipo siguiente.
- Incidencias resueltas: el primer render no activó `.venv` y un intento posterior encontró las cachés de Sass y LuaTeX fuera del perfil de escritura restringido; se regeneraron los derivados, se usó el entorno correcto y el render multiformato final se ejecutó con acceso a la caché normal de TinyTeX. Ninguna incidencia afectó al contenido o a las fuentes.
- Auditoría final: `APTO`. Todas las cifras tienen fuente o cálculo declarado; las operaciones muestran operandos, denominador y regla; las interpretaciones siguen a la evidencia; las fronteras con los capítulos 6 y 8–13 permanecen explícitas; no se requirió cambiar criterios editoriales ni corregir fuentes canónicas.
- Regresiones e integridad: 18 líneas paleográficas, siete guiones documentales y seis secciones canónicas conservados; `git diff --check` en PASS; ningún PDF, `_book/` ni derivado versionado; `project/`, `plugins/`, fuentes canónicas y `main` intactos; ninguna dependencia bloqueante.

## Cierre comprobado de 3G

- Implementación atómica: `e5ddab34ef757aef9ddfbe0b62229f9cb40746df` (`feat(publication): add chapter 8`).
- Resultado editorial: el capítulo 8, «Ganadería, montes y aprovechamientos comunales», documenta vacuno, lanar, cerda, yeguas y crías mulares; separa valores de crías, productos anuales regulados, animales de labor y prestaciones *arenta*; y declara indeterminados los efectivos ganaderos porque la respuesta 20 no ofrece un censo de cabezas. Integra esquileo doméstico, ferrañales, prados, matorrales, eras o sitios, montes de robles y soto de negrillos, alisos y fresnos sin convertir funciones unitarias en producción total.
- Montes, pastos y uso común: distingue el otoño pastado en común de los prados abiertos de secano y el pasto de los ganados del común en matorrales, eras o sitios, montes y soto. Conserva los usos declarados de leña, reparación y resguardo del cereal, pero separa titularidad, uso, derecho de aprovechamiento, administración y beneficio económico; no atribuye propiedad ni gestión común no documentadas.
- Procedencia aceptada: D — `TER-001`, `GAN-001`, `GAN-002`, `GAN-007`; C — sin entradas, porque no existe base para un cálculo editorial de totales; I — `INT-002`, `INT-004`; E — `AGR-012`, `AGR-013`, `GAN-008`; L — `TER-009`, `LIM-008`, `LIM-009`.
- Límites preservados: no se reconstruyen stock por especie, reparto por hogares o titulares, producción total o neta, destino predominante, ingresos, costes, carga ganadera, suficiencia de pastos o combustible, presión sobre los recursos, equilibrio ecológico, sostenibilidad, superficie de montes por residuo ni título jurídico de los espacios de uso común. Se mantienen explícitas las fronteras con el capítulo 7 y con los capítulos 9–13.
- Validación semántica: 32 pruebas específicas del capítulo 8 en PASS —estructura y procedencia, 24 mutaciones adversariales y siete formulaciones cautelares—; suite completa final `222 passed`, sin `skip`, con hash de colección `606dad318389f1aa87519a1cad05ebebbd05fa702d482f5d0506347e42c3f862`.
- Generación y composición: `prepare.py` se ejecutó dos veces con SHA-256 idénticos para los seis derivados; validador estático y `--rendered`, `quarto check` y render HTML/PDF multiformato en PASS. El libro genera 15 documentos HTML; el PDF final tiene 54 páginas y 3.679.088 bytes; el capítulo 8 ocupa las páginas 37–43.
- Inspección visual: título, numeración, navegación, anclas, nueve secciones, tablas, continuaciones con encabezado repetido, saltos y pies revisados en las siete páginas; no se detectaron desbordes ni colisiones. La tabla principal continúa correctamente entre las páginas 38–39.
- Auditoría final: `APTO`. Cada cifra conserva su naturaleza; no se confunden cabeza, stock, flujo, valor, prestación, renta o propiedad; las interpretaciones y el contexto externo permanecen graduados; no se requirió investigación nueva, cambio de criterio editorial ni corrección de fuentes canónicas.
- Regresiones e integridad: 18 líneas paleográficas, siete guiones documentales y seis secciones canónicas conservados; `git diff --check` en PASS; ningún PDF, `_book/` ni derivado versionado; `project/`, `plugins/`, fuentes canónicas y `main` intactos; ninguna dependencia bloqueante.

## Cierre comprobado de 3H

- Implementación atómica: `da76dbb3d7714d4e282f936efb1e1bc657d0dcff` (`feat(publication): add chapter 9`).
- Resultado editorial: el capítulo 9, «Río, molinos y otros recursos productivos», reconstruye el río como soporte productivo, cuatro casas con ocho ruedas descritas y otro molino venturero cuyo número de ruedas no consta. Separa casa, rueda y molino; titular o partícipe, molinero, operador y usuario; utilidad, renta, producción y capacidad. Integra como recursos pertinentes los 18 pies de abejas y el pozo de pesca arrendado, y reserva el marco institucional del conde para el capítulo 10.
- Funcionamiento y vínculo agrario: conserva la molienda de determinadas ruedas durante la mitad del año, la referencia a algunos meses invernales del venturero y la mención conjunta de puentes y funcionamiento sin convertirlas en calendario completo, causalidad universal, caudal permanente o suficiencia de agua. Vincula descriptivamente molinos harineros, centeno y sistema cerealista del capítulo 7 sin deducir volumen molido, usuarios, abastecimiento, autosuficiencia o excedente.
- Resultados cuantitativos: `3 + 2 + 2 + 1 = 8` ruedas descritas; `(3 × 2) + (5 × 4) = 26` cargas de utilidad regulada, sin agregar los cuatro quartales del venturero; `7 + 6 + 3 + 1 + 1 = 18` pies de abejas; `18 × 2 = 36` reales de utilidad anual regulada; `13 / 18 × 100 = 72,22 %` para los dos mayores titulares, limitado a este activo; nueve reales de utilidad para el pozo, sin formar una renta sectorial agregada.
- Procedencia aceptada: D — `HID-001`, `HID-003`, `HID-005`, `HID-006`, `GAN-003`, `GAN-004`, `FIS-012`; C — `HID-002`, `HID-004`, `GAN-005`, `GAN-006`, `CAL-010`, `CAL-011`, `CAL-012`, `CAL-013`, `CAL-020`; I — `HID-007`, `INT-002`, `INT-005`; E — `HID-008`; L — `LIM-005`, `LIM-008`, `LIM-009`, `LIM-010`, `LIM-011`.
- Límites preservados: no se estiman producción, capacidad, días de uso, grado de utilización, número de usuarios, población abastecida, capturas, miel o cera, renta neta, autosuficiencia o excedente. No se identifica al venturero con otro molino o titular, no se convierte pluralidad en copropiedad general ni redundancia garantizada y no se agregan cargas, quartales y reales.
- Validación semántica: 26 pruebas específicas del capítulo 9 en PASS —metadatos, estructura y procedencia, dieciséis mutaciones adversariales y ocho formulaciones cautelares—; suite completa final `247 passed`, sin `skip`, con colección estable de 247 identificadores y hash `fc50ee0dc8533448265f09492037800bf126740cd7b81eb0b457df59d8f0b0ec` calculado solo sobre los identificadores coleccionados.
- Generación y composición: `prepare.py` se ejecutó dos veces de forma directa con SHA-256 idénticos para los seis derivados; validador estático y `--rendered`, `quarto check` y render HTML/PDF multiformato en PASS. El libro genera 15 documentos HTML; el PDF final tiene 58 páginas y 3.692.865 bytes; el capítulo 9 ocupa las páginas 44–48.
- Inspección visual: título, numeración, navegación anterior/siguiente, diez anclas, dos tablas, encabezados, pies y saltos revisados en las cinco páginas. Un primer render dejó tres líneas aisladas en una sexta página; se compactaron dos pasajes redundantes, se repitieron pruebas y render, y el resultado final no presenta desbordes, colisiones ni páginas huérfanas.
- Auditoría final: `APTO`. Cada molino y cifra conserva respaldo y significado; propiedad y explotación, utilidad y producción, agua y funcionamiento permanecen separados; la conexión cerealista está graduada; no se repiten los capítulos 7–8 ni se desarrollan de forma sustantiva los capítulos 10–13. No se requirió investigación externa, cambio de criterio editorial ni corrección de fuentes canónicas.
- Regresiones e integridad: prototipo vertical, 18 líneas paleográficas, siete guiones documentales y seis secciones canónicas conservados; `git diff --check` en PASS; ningún PDF, `_book/` ni derivado versionado; `project/`, `plugins/`, fuentes canónicas y `main` intactos; ninguna dependencia bloqueante.

## Cierre comprobado de 3I

- Implementación atómica: `02dcc31ea6db8250013c99fbc37ecbd0747bcaeb` (`feat(publication): add chapter 10`).
- Resultado editorial: el capítulo 10, «Iglesia, señorío y fiscalidad», distingue señorío y jurisdicción de propiedad; separa los diezmos recibidos por don Manuel Antonio de Vega, la primicia de la iglesia local y el voto destinado a la fábrica del Apóstol Santiago; y diferencia las alcabalas pagadas por los vecinos de la utilidad del pozo atribuido al conde de Luna. La percepción del diezmo no se convierte en propiedad, la utilidad del pozo no se trata como impuesto y ninguna institución absorbe derechos ajenos.
- Magnitudes y sujetos: conserva como regulación anual 30 cargas de centeno, dos de cebada, cinco fanegas de trigo para el caso territorial indicado, 40 fejes de lino de cuatro libras y 140 reales de diezmos menudos; calcula únicamente las 160 libras de lino. Mantiene separados los 26 quartales de centeno de primicia, los 24 quartales de voto con producto omitido, los 633 reales anuales de alcabalas y los nueve reales de utilidad del pozo. No suma especies, unidades o importes de naturaleza distinta ni transforma cantidades reguladas en pagos efectivos.
- Procedencia aceptada: D — `JUR-005`, `JUR-006`, `FIS-001`–`FIS-004`, `FIS-008`, `FIS-012`; C — `CAL-009`; I — `INT-010`; E — `FIS-013`; L — `LIM-001`, `LIM-002`, `LIM-005`, `LIM-011`.
- Límites preservados: las exenciones por establecimiento del suelo y por servicio ordinario y extraordinario conservan sujetos y conceptos específicos; no se generalizan. No se calculan carga por vecino, hogar o habitante, presión fiscal, renta disponible, desigualdad o vulnerabilidad; tampoco se completa el título jurídico de las alcabalas o del pozo. Hacienda común, circulación entre especie y dinero y vulnerabilidad quedan reservadas a los capítulos 11–13.
- Validación semántica: 31 pruebas específicas del capítulo 10 en PASS —estructura y procedencia, diecinueve mutaciones adversariales y once formulaciones cautelares—; suite completa final `278 passed`, sin `skip`, con colección estable de 278 identificadores y hash `d1043ce9acc7d0744c73a4d343e11aa8c54f5cfec5d6b1141216e4dc549f6247` calculado solo sobre los identificadores coleccionados.
- Generación y composición: `prepare.py` se ejecutó dos veces de forma directa con SHA-256 idénticos para los seis derivados; validador estático y `--rendered`, `quarto check` y render HTML, PDF y multiformato en PASS. El libro genera 16 documentos HTML; el PDF final tiene 62 páginas y 3.708.291 bytes; el capítulo 10 ocupa las páginas 49–53.
- Inspección visual: título, numeración, navegación, diez anclas, dos matrices, encabezados, pies y saltos revisados en las cinco páginas. Las tablas son legibles, no hay desbordes ni colisiones y la síntesis termina antes del capítulo siguiente.
- Validación final: `APTO`. Las 19 confusiones semánticas definidas para la fase están cubiertas por regresiones y las cautelas equivalentes se aceptan. No se requirió investigación externa, cambio de criterio editorial ni corrección de fuentes canónicas.
- Regresiones e integridad: prototipo vertical, 18 líneas paleográficas, siete guiones documentales y seis secciones canónicas conservados; `git diff --check` en PASS; ningún PDF, `_book/` ni derivado versionado; `project/`, `plugins/`, fuentes canónicas y `main` intactos; ninguna dependencia bloqueante.

## Cierre comprobado de 3J

- Implementación atómica: `9ac6d90141e0c609b1961367c3333fbf1d86a318` (`feat(publication): add chapter 11`).
- Resultado editorial: el capítulo 11, «Hacienda concejil y servicios colectivos», distingue común, concejo, vecinos y municipio moderno; documenta la ausencia declarada de propios, arbitrios y renta; reconstruye el repartimiento vecinal, la taberna por vecera y la limpieza de fuentes; y mantiene separados uso colectivo, propiedad, administración, renta, prestación y cobertura. Los puentes no se convierten en gasto o patrimonio concejil sin un pagador o administrador documentado.
- Magnitudes y sujetos: conserva los 200 reales del Corpus, ocho de limpieza de fuentes, quince al Hospital de Inocentes de Valladolid y diez por derecho de Mesta en León. La operación `200 + 8 + 15 + 10 = 233` se presenta exclusivamente como subtotal anual de las partidas expresamente cuantificadas en la respuesta 25; las otras cantidades sin importe impiden tratarlo como ingreso total, gasto total, presupuesto o balance.
- Procedencia aceptada: D — `FIS-005`–`FIS-008`, `GAN-002`, `TRA-005`; C — sin entradas, porque no existe en el registro un cálculo canónico específico para este subtotal; I — `INT-004`, `INT-006`; E — `FIS-014`–`FIS-017`, `TRA-006`; L — `LIM-012`, `LIM-013`.
- Límites preservados: no se conoce el origen jurídico del pago al Hospital de Inocentes ni la naturaleza precisa del derecho de Mesta; la ausencia de hospital local no elimina otras formas posibles de asistencia; no se reconstruyen cuotas individuales, ejecución efectiva, cuentas de caja, cobertura universal, servicios permanentes, patrimonio concejil, capacidad financiera, eficiencia, fragilidad o resiliencia. La circulación monetaria queda reservada al capítulo 12 y la evaluación sistémica al capítulo 13.
- Validación semántica: 35 pruebas específicas del capítulo 11 en PASS —estructura y procedencia, diecinueve mutaciones adversariales y quince formulaciones cautelares—; suite completa final `313 passed`, sin `skip`, con colección estable de 313 identificadores y hash `364e4b22876e3a3e0c3e9b7b5437a18496a3af97f786c6cae96982ba2c17941a` calculado solo sobre los identificadores coleccionados.
- Generación y composición: `prepare.py` se ejecutó dos veces de forma directa con SHA-256 idénticos para los seis derivados; validador estático y `--rendered`, `quarto check` y render HTML, PDF y multiformato en PASS. El libro genera 17 documentos HTML; el PDF final tiene 68 páginas y 3.723.590 bytes; el capítulo 11 ocupa las páginas 55–59.
- Inspección visual: título, numeración, navegación, diez anclas, tabla, fórmula, encabezados, pies y saltos revisados en las cinco páginas. La tabla es legible, no hay desbordes ni colisiones y la síntesis termina antes del capítulo siguiente sin página huérfana.
- Validación final: `APTO`. Las 19 confusiones semánticas definidas para la fase están cubiertas por regresiones y las cautelas equivalentes se aceptan. No se requirió investigación externa, cambio de criterio editorial ni corrección de fuentes canónicas.
- Regresiones e integridad: prototipo vertical, 18 líneas paleográficas, siete guiones documentales y seis secciones canónicas conservados; `git diff --check` en PASS; ningún PDF, `_book/` ni derivado versionado; `project/`, `plugins/`, fuentes canónicas y `main` intactos; ninguna dependencia bloqueante.

## Cierre comprobado de 3K

- Implementación atómica: `413d1e6bd7c03e71ee7ce0a47a2531be6caf1f35` (`feat(publication): add chapter 12`).
- Resultado editorial: el capítulo 12, «Dinero, oficios y conexiones exteriores», distingue precio o valor ordinario, valor o producto regulado, utilidad regulada, pago declarado y gasto u obligación. Conserva la coexistencia de dinero, especie y servicio y no convierte valoraciones catastrales en compraventas, utilidades en ingresos efectivos ni presencia monetaria en monetización plena.
- Magnitudes y naturaleza: mantiene los valores ordinarios de centeno, cebada, linaza, lino, trigo y heno en sus unidades documentales; calcula `18 × 2 = 36` reales como utilidad regulada de los pies de abejas; y reúne `633 + 233 + 140 = 1.006` reales únicamente como mínimo institucional explícito de tres magnitudes anuales heterogéneas, no como circulación total, presupuesto, presión fiscal, ingreso local, salida neta o balance.
- Trabajo y oficios: conserva 18 jornaleros —14 hijos de familia, tres criados sirvientes y uno dedicado solo a ese ejercicio—, 24 labradores y un herrero que trabaja principalmente como labrador como categorías cruzadas, no aditivas ni equivalentes a población activa moderna. Los 2,5 reales diarios del jornalero, tres del labrador y medio real adicional del herrero mantienen su carácter de utilidad por día trabajado; no se suponen días, continuidad, salario anual, renta familiar ni riqueza.
- Conexiones exteriores: documenta quince reales al Hospital de Inocentes de Valladolid y diez por derecho de Mesta en León. `15 + 10 = 25`, `25 / 233 = 10,73 %` y `25 / 1.006 = 2,49 %` usan denominadores parciales distintos y no son cuotas de comercio exterior ni de una balanza de pagos. Las siembras fuera del término, el voto a la fábrica del Apóstol Santiago y los derechos del conde conservan su naturaleza territorial, eclesiástica o señorial; no prueban importaciones, exportaciones, movilidad habitual o una red mercantil estable.
- Procedencia aceptada: D — `GAN-001`, `GAN-003`, `HID-005`, `TRA-001`–`TRA-005`, `JUR-006`, `FIS-002`–`FIS-004`, `FIS-006`, `FIS-007`, `FIS-012`; C — `GAN-005`, `HID-004`, `FIS-009`–`FIS-011`, `CAL-010`, `CAL-014`–`CAL-017`; I — `INT-007`, `INT-008`, `INT-010`; E — `JUR-009`, `FIS-013`–`FIS-015`; L — `LIM-002`, `LIM-005`, `LIM-006`, `LIM-008`, `LIM-009`, `LIM-011`–`LIM-013`.
- Límites preservados: las negativas de las respuestas 31, 32 y 34 acotan las categorías preguntadas, pero no prueban ausencia de todo intercambio o transporte. Joaquín Aguado acredita una conexión administrativa y documental, no comercial. No se calculan mercado, comercio, importaciones, exportaciones, ingresos domésticos, autosuficiencia, dependencia, vulnerabilidad o resiliencia; la síntesis sistémica queda reservada al capítulo 13.
- Validación semántica: 42 pruebas específicas del capítulo 12 en PASS —estructura y procedencia, 21 mutaciones adversariales y 20 formulaciones cautelares—; selección focal final `44 passed` al incluir dos pruebas de frontera preexistentes. Suite completa final `355 passed`, sin `skip`, con colección estable de 355 identificadores y hash `6c93ecd9bb6adb59c9f613e5d8cae21dabda3113d2e18c245e2057a81f178254` calculado solo sobre los identificadores coleccionados.
- Generación y composición: `prepare.py` se ejecutó dos veces de forma directa con SHA-256 idénticos para los seis derivados; validador estático y `--rendered`, `quarto check` y render HTML, PDF y multiformato en PASS. El libro genera 18 documentos HTML; el PDF final tiene 74 páginas y 3.740.568 bytes; el capítulo 12 ocupa las páginas 60–65.
- Inspección visual: título, numeración, navegación, diez anclas, tablas, fórmulas, encabezados, pies y saltos revisados en las seis páginas. Una primera composición acercó la última línea al pie de la página 61; se compactaron dos pasajes, se repitieron pruebas y render, y el resultado final no presenta desbordes, colisiones ni páginas huérfanas.
- Validación final: `APTO`. Las 21 confusiones semánticas definidas para la fase están cubiertas por regresiones y las cautelas equivalentes se aceptan. No se requirió investigación externa, cambio de criterio editorial ni corrección de fuentes canónicas.
- Regresiones e integridad: prototipo vertical, 18 líneas paleográficas, siete guiones documentales y seis secciones canónicas conservados; `git diff --check` en PASS; ningún PDF, `_book/` ni derivado versionado; `project/`, `plugins/`, fuentes canónicas, informe comparativo y `main` intactos; ninguna dependencia bloqueante.

## Cierre comprobado de 3L

- Implementación atómica: `fdcb18dc8e714dabfcba5032439074d8460f67e1` (`feat(publication): add chapter 13`).
- Resultado editorial: el capítulo 13, «Una economía rural integrada: vulnerabilidades, resiliencia y límites», sintetiza territorio, población documental, trabajo, tierras, ganado, agua, transformación, derechos, hacienda y dinero como relaciones locales funcionales e institucionales. La integración interna no se presenta como integración en mercados regionales, autosuficiencia, equilibrio, sostenibilidad o resiliencia.
- Dependencias y amortiguación: distingue dependencia documentada, exposición plausible y crisis o daño observado; acota el predominio centenal, los ritmos agrarios, la dependencia hidráulica, los usos comunes y el repartimiento sin atribuir impactos sufridos. Describe diversidad de actividades, pluralidad de unidades y mecanismos colectivos como posibilidades de amortiguación cuya eficacia no puede medirse; para afirmar resiliencia fuerte exige choque, respuesta, recuperación o adaptación observables.
- Magnitudes y límites: reutiliza únicamente cálculos canónicos con sus denominadores y naturalezas —93,13 %, 72,16 %, 1.578,25 unidades, ocho ruedas en cuatro casas, 26 cargas de utilidad regulada, 36 y nueve reales de utilidad y el mínimo institucional parcial de 1.006 reales—. No calcula producción total, renta por habitante u hogar, nivel de vida, desigualdad, suficiencia, presión fiscal, presupuesto, comercio regular o causalidad económica.
- Procedencia aceptada: D — `JUR-001`, `JUR-002`, `JUR-005`, `JUR-006`, `TER-001`, `TER-010`, `AGR-001`–`AGR-003`, `AGR-010`, `GAN-001`–`GAN-003`, `GAN-007`, `HID-001`, `HID-005`, `HID-006`, `DEM-001`, `DEM-003`, `TRA-001`–`TRA-005`, `FIS-001`–`FIS-008`, `FIS-012`; C — `AGR-004`–`AGR-006`, `GAN-005`, `HID-002`, `HID-004`, `FIS-009`–`FIS-011`, `CAL-003`–`CAL-006`, `CAL-012`–`CAL-017`; I — `INT-001`–`INT-010`; E — `TER-011`, `AGR-011`–`AGR-013`, `GAN-008`, `HID-008`, `TRA-006`, `FIS-013`–`FIS-017`; L — `LIM-001`–`LIM-013`.
- Validación semántica: 25 inversiones semánticas y 25 formulaciones cautelares cubiertas, además de nueve guardas transversales para los capítulos 5–13; selección focal final `64 passed`. Suite completa final `416 passed`, sin `skip`, con colección estable de 416 identificadores y hash `f99eae9678d9a7cf49897d5fcefbb0fa5eff82d900fe33081216e067b4829f76` calculado solo sobre los identificadores coleccionados.
- Generación y composición: `prepare.py` se ejecutó dos veces de forma directa con SHA-256 idénticos para los seis derivados; validador estático y `--rendered`, `quarto check` y render HTML, PDF y multiformato en PASS. El libro genera 19 documentos HTML; el PDF final tiene 81 páginas y 3.762.360 bytes; el capítulo 13 ocupa las páginas 66–72.
- Inspección visual: se revisaron las páginas 65–73, incluidas la salida del capítulo 12, las siete páginas del capítulo 13 y la entrada al facsímil. Título, numeración, once anclas, dos tablas, encabezados, pies y saltos son legibles; no hay desbordes, colisiones ni encabezados huérfanos y la Parte III comienza limpiamente en la página 73.
- Cierre de parte: los capítulos 5–13 mantienen las cautelas aceptadas y la transición final devuelve al soporte material sin confundir facsímil, transcripción e interpretación. La Parte II queda cerrada con veredicto `APTO`; no se requirió investigación externa, cambio de criterio editorial ni corrección de fuentes canónicas.
- Regresiones e integridad: prototipo vertical, 18 líneas paleográficas, siete guiones documentales y seis secciones canónicas conservados; `git diff --check` en PASS; ningún PDF, `_book/` ni derivado versionado; `project/`, `plugins/`, fuentes canónicas, informe comparativo y `main` intactos; ninguna dependencia bloqueante.

## Cierre comprobado de 4A

- Implementación atómica: `6c27050fe478386f6a887c1efa1c4f25f9fbc6df` (`feat(publication): generate chapter 14 facsimile`).
- Contrato de entrada: `check_sources.py` valida las cuatro fuentes versionadas, los metadatos concordantes del manuscrito, su réplica local fuera del checkout, tamaño, SHA-256, 18 páginas, las 35 unidades en orden, capítulos, evidencia y activos. La réplica usada fue `/home/miguel/.local/share/sorrios-ensenada/manuscript.pdf`, con SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`; no hubo descarga desde Drive ni uso del PDF 0.6.
- Generación: `prepare.py` verifica primero las entradas y coordina por separado el prototipo vertical y el nuevo `build_facsimile.py`. El capítulo 14 y 18 PNG completos a 180 dpi se reconstruyen solo bajo `publication/generated/`, sin recortes, OCR o realce y sin borrar salidas ajenas. Las seis salidas previas del prototipo conservan su contrato.
- Reproducibilidad: dos preparaciones consecutivas mantuvieron idénticos los SHA-256 de las 25 salidas generadas; el manifiesto conjunto tiene SHA-256 `424466caf39943e013c63dc18ee96e4d91b29a21869fd29113e7b71b535497f0`. Las 18 imágenes suman 35.063.833 bytes.
- Política de activos: el QMD y los PNG son derivados reproducibles ignorados mediante la política vigente `generated_ignored`; no se versionan binarios, no se introduce Git LFS y no queda decisión pendiente sobre activos.
- Validación: 10 pruebas focalizadas y 426 pruebas totales en PASS, sin `skip`; hash de la colección de identificadores `729cf4621fa720f98e08b71d2e76617103e30078b6c6a6a32802174730b236ee`. `check_sources.py`, validadores estático y renderizado, `quarto check`, render HTML, PDF y multiformato, y `git diff --check` en PASS.
- Composición: 19 documentos HTML y PDF de 100 páginas y 36.540.687 bytes. El capítulo 14 ocupa las páginas 74–92: apertura de Parte III en la 74 y una hoja por cada página digital en las 75–92. La primera imagen vertical se ajustó al 62 % para evitar una hoja en blanco y mantener su nota de procedencia; las otras 17 conservan el 82 %.
- Inspección visual: se revisaron las 18 imágenes generadas y las páginas PDF 73–94. Orden, orientación, márgenes, blancos, sellos, reclamos, nitidez, pies, paginación y transiciones son correctos; no hay cortes, colisiones ni páginas huérfanas propias de 4A. La página 93 es la hoja de cortesía previa a la apertura del capítulo 15 en la 94.
- Regresiones e integridad: capítulos 1–13, D/C/I/E/L, 18 líneas paleográficas, siete guiones documentales y seis secciones canónicas continúan en PASS. `project/`, `plugins/`, fuentes canónicas, `main` y `origin/main` permanecen intactos; ningún PDF, `_book/`, QMD generado ni PNG quedó versionado.
- Estado: 4A cerrada; la Fase 4 continúa en curso y 4B es la única tarea siguiente.

## Cierre comprobado de 4B

- Implementación atómica: `bd0d20c18ba25d079a5faa34d51b5f82f3d5b0c2` (`feat(publication): generate chapter 15 transcription`).
- Contrato: el parser compartido exige correspondencia exacta, unívoca y ordenada entre las 35 unidades de `unidades.yaml` y la sección 3 de la Edición Crítica 3.6. Cada unidad conserva una imagen y cinco secciones textuales —transcripción paleográfica, observaciones editoriales, notas paleográficas, notas históricas y referencias cruzadas— sin modernización, OCR ni contenido editorial nuevo.
- Generación: `prepare.py` ejecuta comprobación de fuentes, 4A, 4B y el prototipo en ese orden. `build_transcription.py` recorta las 35 unidades desde las 18 páginas PNG verificadas de 4A con la semántica `complete/left/right`; solo escribe `generated/15-transcripcion.qmd` y `generated/assets/transcription/`. Los recortes PNG suman 38.226.819 bytes.
- Fidelidad: comparación exacta de las cinco secciones textuales de las 35 unidades y de su lineación en QMD, HTML y PDF en PASS. El salto interno del croquis de folio 307r y el signo editorial `[...]` se conservan. `folio_315v` coincide con el prototipo en texto y en imagen, con SHA-256 `5e3779962ef5180bab36ff7dc132c641484e55e8b772a4accc31db157220e0cc`.
- Reproducibilidad: dos preparaciones finales conservaron los hashes de colección `b3e99b6c4d307e0d84842a906f85bb695eea00597b5e8ab576c58ebdfa884e2a` para 4A, `e612ad8be0baee5af644c91b7bd70bcea8550447a47bec465c2cb8cb31eaecb6` para 4B, `31bd1932af1aeeba8bc6521fe06cd1df7839710b9d8ec2eb4173d4725cad9421` para el prototipo y `d0f3175eca6aea157efe0f72f0302e722c29c30bb7148fd09fcf781a9d4a852d` para las 61 salidas conjuntas, que suman 76.928.942 bytes.
- Validación: 24 pruebas focalizadas y 450 pruebas totales en PASS, sin `skip`; colección estable de 450 identificadores con SHA-256 `87d193492d236545f1327f34bd06a097e9b76dd19976c789260ec3bca2637017`. `check_sources.py`, validadores estático y `--rendered`, `quarto check`, render HTML, PDF y multiformato, y `git diff --check` en PASS.
- Composición: 19 documentos HTML; las 35 anclas, imágenes, textos alternativos, ampliación y enlaces internos están validados y no existe un segundo capítulo 15 visible. El PDF final tiene 205 páginas y 73.735.955 bytes; el capítulo 15 ocupa las páginas 98–201.
- Inspección visual: se revisaron individualmente los 35 recortes y las 104 páginas completas del capítulo. La asociación imagen/unidad, encabezados, saltos, pies, bloques de líneas, caracteres paleográficos, corchetes, cursivas, notas, continuaciones y referencias son correctos; no hay imágenes separadas, páginas en blanco inesperadas, encabezados huérfanos ni colisiones.
- Política e integridad: QMD y PNG siguen siendo derivados reproducibles ignorados; no se versionan binarios ni se introduce Git LFS. El PDF autoritativo permanece fuera del checkout y el PDF 0.6 fuera del flujo. `project/`, `plugins/`, fuentes canónicas, `main` y `origin/main` permanecen intactos.
- Estado: 4B cerrada; la Fase 4 continúa en curso y 4C —capítulo 16, edición modernizada— es la única tarea siguiente.

## Cierre comprobado de 4C

- Implementación atómica: `84f31b4249b745fe50799b8cfce2682913100d8e` (`feat(publication): generate chapter 16 modernized edition`).
- Contrato y fidelidad: el parser exige la versión 1.3, el orden documental completo, 40 respuestas consecutivas y únicas, 35 filas de concordancia y todas las llamadas y definiciones de nota. Las 40 preguntas coinciden una a una con la lista verificada de la Introducción 1.3; el generador compara cada bloque con la fuente y emite errores localizados por respuesta.
- Generación: `prepare.py` ejecuta comprobación de fuentes, 4A, 4B, 4C y el prototipo en ese orden. `build_modernized.py` es propietario solo de `generated/16-edicion-modernizada.qmd`; separa visualmente pregunta externa y respuesta local, conserva 46 anclas estables y deriva la navegación hacia las unidades del capítulo 15 desde la concordancia canónica. La sección fuente «Documentos relacionados» se sustituye explícitamente por la navegación del libro porque sus enlaces son internos al repositorio.
- Cautelas: se conservan la laguna `en este pueblo […] medida de tierra`, las medidas y categorías documentales, `avitadores`, la pregunta 40 sobre `renta` y la respuesta local `venta`, además de las 39 notas —35 numéricas y cuatro semánticas—. Los identificadores técnicos de nota se aíslan con el prefijo `modernizada-` para evitar colisiones entre capítulos, sin alterar llamadas, texto ni correspondencia.
- Reproducibilidad: dos preparaciones finales conservaron los hashes de 4A `b3e99b6c4d307e0d84842a906f85bb695eea00597b5e8ab576c58ebdfa884e2a`, 4B `e612ad8be0baee5af644c91b7bd70bcea8550447a47bec465c2cb8cb31eaecb6`, 4C `626e39103178a96b6798ae081cd0c26e9e2ea67d2ddbebad5da8b199d490c0ed` y prototipo `31bd1932af1aeeba8bc6521fe06cd1df7839710b9d8ec2eb4173d4725cad9421`; las 62 salidas conjuntas tienen SHA-256 `46dc55dba60a68b3c7b0165dcb138ac0577b70a7c94f3972939babe75886c8ae`. El QMD del capítulo 16 tiene SHA-256 `873a4f4f3a6662d65afac01d94d0777e0e3e14a880299279ab953f32c6d2ba05`.
- Validación: 30 pruebas focalizadas y 480 pruebas totales en PASS, sin `skip`; colección estable con SHA-256 `0110803960024ba8c3831118edf4cebdbc74068ae19ff6e0f36ae7502093fb64`. `check_sources.py`, validadores estático y `--rendered`, `quarto check`, render HTML, PDF y multiformato, y `git diff --check` en PASS.
- Composición: 18 documentos HTML y PDF de 226 páginas y 73.801.346 bytes; el capítulo 16 ocupa las páginas 203–226. Se inspeccionaron visualmente esas 24 páginas y la transición desde la 202: preguntas, respuestas, notas, tabla de concordancia, encabezados, pies y saltos son legibles y no presentan desbordes ni colisiones. Pandoc conserva un aviso no bloqueante por el identificador `portada`, exigido también por el capítulo 15; cada HTML mantiene su ancla propia y la navegación está validada.
- Integridad: el capítulo real es el único 16 visible; los prototipos permanecen como regresión fuera de la navegación. QMD y artefactos renderizados siguen ignorados; ningún PDF ni derivado quedó versionado. `project/`, `plugins/`, fuentes canónicas, `main` y `origin/main` permanecen intactos.
- Estado: 4C cerrada; la Fase 4 continúa en curso y 4D —glosario, cuadros cuantitativos, concordancia y matriz de evidencia— es la única tarea siguiente.

## Cierre comprobado de 4D

- Implementación atómica: `f9a7bf9d9a7e8cb70516e41105a472d7d7f3eed2` (`feat(publication): generate reproducible apparatus`).
- Arquitectura: `apparatus_sources.py` modela y valida el Glosario y el Registro; `build_apparatus.py` deriva exclusivamente `glosario.qmd`, `cuadros-cuantitativos.qmd`, `concordancia.qmd` y `matriz-evidencia.qmd`. `check_sources.py`, `prepare.py`, la navegación, el posprocesado y el validador integran 4D sin listas de publicación paralelas ni escritura en `project/` o `plugins/`.
- Glosario: 22 entradas fieles a `Glosario.md`. Como la fuente no declara versión, `publication.yml` conserva ruta y snapshot Git `0df18f89e2f39f8d75279d06e6f1b0bfa77362fe`; no se inventa una versión. Folios, respuestas, referencias internas y fuentes externas seguras quedan enlazados; las referencias a índices futuros permanecen como texto.
- Cuadros: 13 entradas canónicas de nivel C y 17 cálculos `CAL-*` asociados, derivados del Registro 1.2. Operaciones, resultados, unidades, denominadores, estados y cautelas se conservan literalmente. `CAL-018`–`CAL-020` no se presentan como resultados C porque el Registro los asocia a controles documentales.
- Concordancia: dos vistas derivadas de una misma relación estructurada cubren 35 unidades, 18 páginas facsimilares, 40 respuestas y 65 relaciones unidad↔respuesta, incluidas las correspondencias muchos-a-muchos y los bloques no equivalentes. Los enlaces a los capítulos 14–16 están validados.
- Matriz: 112 entradas fieles al Registro, con conteo por componentes D/C/I/E/L de 47/13/27/25/16; los niveles compuestos se conservan. Registra 88 estados `Admitida`, 10 `Condicionada`, ninguno `Excluida`, una cautela explícita adicional y 13 límites cuya tabla fuente no declara columna separada de estado. `Uso en el libro` se deriva únicamente de metadatos estructurados de los capítulos 5–13.
- Identificadores: la colisión global `portada` quedó resuelta mediante `transcripcion-portada` y `modernizada-portada`; enlaces y regresiones se actualizaron y el render combinado ya no emite el aviso de identificador duplicado.
- Reproducibilidad: dos preparaciones finales conservaron los hashes de grupo 4A `b3e99b6c4d307e0d84842a906f85bb695eea00597b5e8ab576c58ebdfa884e2a`, 4B `ccbc1db0e9549dc53af0bf9bb0b3f6539714a24b4d9300bc098c39da03a4ac3f`, 4C `ddd22812826f5aa2b04bd26884c2515bf596d6de28616d47fbdd65269311d8a3`, 4D `db2f5768f87fc5ad38b56a2af2ba0a6bf44573354d1c20a4f0b4f1c3fe7b2584` y prototipo `31bd1932af1aeeba8bc6521fe06cd1df7839710b9d8ec2eb4173d4725cad9421`. El flujo produce 66 salidas reproducibles.
- Validación: 42 pruebas focalizadas y 522 pruebas totales en PASS, sin `skip`; colección estable de 522 identificadores con SHA-256 `a99c86a08832f5d3203b3160b67b60ca4816b57c5b9f65b0cf0b5699ac965867`. `check_sources.py`, validadores estático y `--rendered`, `quarto check`, render HTML, PDF y multiformato, y `git diff --check` en PASS.
- Composición: 22 documentos HTML y PDF de 289 páginas y 73.955.867 bytes. El glosario ocupa 231–239; los cuadros, 240–246; la concordancia, 247–251; y la matriz, 252–289. Se inspeccionaron visualmente las 59 páginas: tablas, denominadores, cautelas, enlaces, fórmulas, URLs y saltos son legibles y no pierden información.
- Auditoría global: capítulos 14–16 y los cuatro aparatos de 4D existen, son reproducibles y mantienen intactas sus autoridades. Las cuestiones abiertas, fuentes, versiones y modelos de cita no estaban asignados a 4D y no bloquean este cierre. No se inició ningún índice ni se creó `build_indexes.py`.
- Integridad: `project/`, `plugins/`, fuentes canónicas, `main` y `origin/main` permanecen intactos; QMD generados, PNG, PDF y `_book/` continúan ignorados y no se versionó ningún binario.
- Estado: 4D y la Fase 4 quedan cerradas. La única tarea siguiente es Fase 5 — índices, calidad integral y accesibilidad.

## Cierre comprobado de 5A

- Implementación atómica: `16084c95691d879675859030059c9bf25af1c7dc` (`feat(publication): generate nine indexes`).
- Arquitectura: `index_sources.py` aplica un parser común a los cinco índices vivos y valida los destinos estructurados `section`, `unit` y `response`; `build_indexes.py` es propietario de nueve QMD bajo `generated/indices/`. Los índices 1–5 proceden de las cinco fuentes vivas, los índices 6, 7 y 9 de `meta/indexes.yml`, y el índice 8 se deriva de las 40 respuestas de la edición modernizada. `check_sources.py`, `prepare.py`, la navegación y el validador integran 5A sin modificar `project/`.
- Cobertura: los nueve índices contienen respectivamente 21, 9, 7, 12, 12, 27, 15, 40 y 21 entradas. La ordenación alfabética usa una clave Unicode determinista separada de la forma visible; las variantes, remisiones y grados de seguridad se conservan sin duplicar localizadores. `indexes.yml` contiene únicamente metadata editorial conservadora con destinos a secciones existentes y ninguna página escrita manualmente.
- Localizadores: una única relación estructurada produce enlaces HTML y referencias PDF. HTML enlaza a las anclas estables de los capítulos 1–16; PDF usa `hyperref`, `pageref` y las etiquetas del propio render, suprimiendo páginas repetidas. La composición normal realizó tres pasadas de LuaLaTeX, sin manifiesto post-render, OCR ni tabla paralela de páginas.
- Reproducibilidad: tres preparaciones de control —incluidas dos consecutivas— conservaron los hashes de grupo 4A `324f74a22d26eed7f24865366a2f2645b0c8d5ae1d4c98f8066211a9324f5bfd`, 4B `b7d12494f0fa8ddcc951700f0bc64917c9085afb1714a3505d480ecd7a5423e7`, 4C `5c9af85c196402c38376b644041e485a4364e8a1448564235aac44f3599e0a12`, 4D `af424eabbc32a15a7af4aa3ea853c69a2e496838560ae1fa60522e3d51f84c5f`, 5A `f7c673e966d8d94f7d053cbc1933d8cd8b80233fe0eafd2fe7a85874b049c5cd` y prototipo `a2cc3d473329bc44cedcc296c4263c83d8bd22a4961184630a250798c8062c75`. El flujo produce 75 salidas reproducibles.
- Validación: 66 pruebas focalizadas y 546 pruebas totales en PASS, sin `skip` ni `xfail`; colección estable con SHA-256 `ab824cba2aed01260fc25fd395a1ba69d30833e8f130bae7332a1edb74f4f059`. `check_sources.py`, validadores estático y `--rendered`, `quarto check`, render HTML, PDF y multiformato, auditoría global de enlaces/anclas y `git diff --check` están en PASS.
- Composición: 31 documentos HTML sin enlaces fragmentarios rotos ni rutas locales. El PDF final tiene 329 páginas y 74.026.158 bytes; los índices ocupan, en orden, 292–298, 299–301, 302–304, 305–308, 309–312, 313–317, 318–321, 322–325 y 326–329. Una muestra distribuida por los nueve índices confirmó automáticamente la correspondencia entre página impresa y destino real.
- Inspección editorial y visual: se revisaron las 38 páginas de índices. Orden, grafías, cautelas metrológicas, remisiones, números, encabezados, pies, saltos y caracteres paleográficos son legibles; no hay desbordes, colisiones, páginas vacías, URLs accidentales ni identificadores duplicados. Se mantienen Sorribos/Sorrios, el contexto explícito del error `Sorribas`, Bega/Vega y las distinciones entre común, propiedad, vecindad, población, ruedas y medidas aceptadas en fases anteriores.
- Integridad: `project/`, `plugins/`, fuentes canónicas, `main` y `origin/main` permanecen intactos; los QMD generados, PNG, PDF y `_book/` continúan ignorados y no se versionó ningún binario ni archivo temporal.
- Estado: 5A queda cerrada; la Fase 5 continúa en curso. La única tarea siguiente es 5B — calidad integral y accesibilidad.

## Cierre comprobado de 5B

- Implementación atómica: `e74ce3cb8bd27921f50db5a046a0851528297ced` (`feat(publication): complete quality and accessibility review`). No se modificaron `project/`, `plugins/`, fuentes canónicas, paleografía, modernización, cifras, cálculos ni estados D/C/I/E/L.
- Estructura editorial: 30 documentos HTML en seis partes; portada, capítulos numerados 1–16, cuatro aparatos y nueve índices en el orden del Plan Maestro. La prueba técnica permanece como regresión no publicada; portada, navegación y manifestación editorial ya no conservan afirmaciones obsoletas de bootstrap. Aparatos e índices son capítulos no numerados y no muestran marcadores Markdown.
- Auditoría textual: `check_sources.py` verificó cinco fuentes, 35 unidades, 40 preguntas/respuestas, 22 entradas de glosario, 112 entradas D/C/I/E/L y 20 cálculos. Las guardas transversales confirmaron Sorribos/Sorrios/Sorribas, Concejo/municipio, uso común/propiedad, `avitadores`, ruedas y venturero, utilidad/producción, jornal/ingreso, dinero/monetización, diversidad/resiliencia, dependencia/daño y ausencia documental/histórica. No aparecieron contradicciones de cifras, unidades, denominadores, porcentajes o etiquetas.
- HTML y accesibilidad básica: los 30 documentos declaran español, un H1 lógico y títulos únicos; se auditaron 3.405 enlaces, 2.282 identificadores, landmarks, jerarquía de encabezados, búsqueda, TOC, navegación, botones y fragmentos. Las 53 imágenes tienen alternativa; las 44 tablas tienen cabeceras, alcance, nombre accesible y región desplazable por teclado. Se añadieron foco visible, reflow y ajuste de textos; contraste, viewport estrecho y escala 200 % fueron comprobados con cálculo y Chrome Headless. No quedan rutas locales, enlaces QMD ni residuos de desarrollo en el contenido público.
- PDF: 334 páginas, 73.994.496 bytes, título correcto, idioma de catálogo configurado como `es-ES`, texto editorial seleccionable, glifos críticos extraíbles, 14 variantes Latin Modern embebidas/subconjuntadas con Unicode, 53 imágenes, 90 URI y 1.100 destinos inspeccionables. Las seis partes, los capítulos 1–16 y los aparatos/índices aparecen con nombres editoriales; no hay URI `.qmd`, rutas locales ni destinos de scaffolding. Los localizadores de los nueve índices se revalidaron contra la paginación final.
- Inspección visual: las 334 páginas se revisaron a nivel de geometría/composición y se ampliaron aperturas, cierres, tablas, facsímil, transcripción, modernizada, aparatos e índices. Se corrigieron un bloque final huérfano de referencias, la numeración impropia 17–29 y los marcadores `{.unnumbered}`/`#` visibles. No quedan cortes, colisiones, desbordes ni páginas corruptas conocidos.
- Reproducibilidad: dos preparaciones finales consecutivas produjeron las mismas 75 salidas. SHA-256 de los manifiestos `sha256sum` ordenados: 4A `b3e99b6c4d307e0d84842a906f85bb695eea00597b5e8ab576c58ebdfa884e2a`; 4B `ccbc1db0e9549dc53af0bf9bb0b3f6539714a24b4d9300bc098c39da03a4ac3f`; 4C `824b1a794da01ab8d50616d92f5733846b05eb03e21de22ac10da4fd29052260`; 4D `bdeee6ff70d36a766da82ea838be2512872e0fcc407c55410fe527a52b5efae6`; 5A `b9f32dfa454e5c812c8733cc1da46e49af8e7fab8e71e40f82b6fc784dddffcf`; prototipo `31bd1932af1aeeba8bc6521fe06cd1df7839710b9d8ec2eb4173d4725cad9421`; conjunto `0f2a27a3294060552ee5dde8a9b4d61258e85fef049679f650e3d71465234da0`.
- Validación: 11 pruebas específicas 5B y 557 pruebas totales en PASS, sin `skip` ni `xfail`; colección estable de 557 identificadores con SHA-256 `43daf422db8b3cbfb1c31f43c418052b9654dbbb8cddf5ba7c481a284f228552`. `check_sources.py`, validadores estático y profundo `--rendered`, `quarto check`, render HTML, PDF y multiformato, auditoría de enlaces/anclas, Poppler y `git diff --check` están en PASS. El render final no emite avisos propios del libro.
- Herramientas y limitaciones: se usaron Quarto 1.7.31, LuaHBTeX/TinyTeX 2026, Chrome Headless y Poppler (`pdfinfo`, `pdffonts`, `pdftotext`, `pdfimages`, `pdftoppm`). No estaban disponibles axe, pa11y, Lighthouse, v.Nu, PAC, veraPDF, qpdf ni mutool y no se instaló nada. El PDF informa `Tagged: no`; por tanto se registra como limitación no bloqueante y no se declara PDF/UA. Tampoco se declaran WCAG 2.1/2.2 AA ni PDF/A. Autoría, editor, licencia, copyright e ISBN no se inventaron y podrán resolverse en la operación editorial correspondiente.
- Incidencias de entorno resueltas: se activó `.venv` para Pillow y se aislaron en `/tmp` las cachés de Sass y LuaTeX exigidas por el sandbox. La ausencia de `babel-spanish` en TinyTeX se resolvió sin instalar paquetes mediante rótulos visibles y metadatos españoles locales. Los únicos mensajes residuales fueron informativos de disponibilidad de herramientas y D-Bus de Chrome, ajenos al libro.
- Integridad: `project/`, `plugins/`, fuentes canónicas, manuscrito externo, PDF 0.6, `main` y `origin/main` permanecen intactos. Ningún PDF, PNG, `_book/`, derivado ni temporal está versionado. No se ejecutó preview, despliegue, publicación, etiqueta, release ni push.
- Veredicto: `PASS`; no quedan bloqueantes conocidos. 5B y la Fase 5 quedan cerradas. La única tarea siguiente es Fase 6 — preview y publicación 1.0.

## Estado comprobado de 6A

- Candidata técnica: `49ab2e1b1a58ca9201efab54b42a3125de7326f8` (`chore(publication): prepare 1.0 release candidate`). `base.git_commit` identifica `main@e81dc9239ac8dbabfe77168a50ef98c4d3b79170`; los árboles `project/` de `main` y de la candidata coinciden en `e32917763475ceebdfe7b54830e1fb43f6419dad`.
- Metadata: se conservan `0.1.0-dev` y `development`; no se inventó versión RC ni autoría, responsabilidad editorial, licencia, copyright, fecha, URL o ISBN. Las decisiones editoriales necesarias para 1.0 permanecen explícitamente pendientes de 6B.
- Reproducibilidad: dos preparaciones completas consecutivas produjeron las mismas 75 salidas, 77.225.629 bytes y SHA-256 conjunto `0f2a27a3294060552ee5dde8a9b4d61258e85fef049679f650e3d71465234da0`; el informe `docs/CANDIDATA_PUBLICACION_1_0.md` registra los hashes de 4A, 4B, 4C, 4D, 5A y prototipo.
- Salidas: 30 documentos HTML; bundle sin PDF de 77.085.904 bytes. PDF `sorribos-santibanez-ordas-1752.pdf`, 334 páginas, 73.994.496 bytes, SHA-256 `f1eee2f465f554d3bf2b506d23a622967d1b4f1013ac657a774868e525688183`. La descarga HTML sirve exactamente ese PDF.
- Validación: diez pruebas 6A y 567 pruebas totales en PASS, sin `skip` ni `xfail`; colección SHA-256 `2707830a38956a186b7b4c5a377fadf59cfcd98894dafb48ed28df86d58f7fe7`. `check_sources.py`, dos preparaciones, validadores estático/profundo, `quarto check`, renders HTML/PDF/multiformato, enlaces/anclas, localizadores, Poppler, seguridad pública y `git diff --check` pasan.
- Inspección: las 334 páginas superaron la comprobación geométrica y las muestras de release de portada, partes, capítulos 1/5/13, facsímil, transcripción, modernizada, aparatos, nueve índices y última página no muestran defectos. HTML se comprobó en escritorio y viewport estrecho.
- Preview local: smoke test temporal en `http://127.0.0.1:4319/` con páginas, búsqueda, assets y PDF en `200`; el servidor quedó cerrado. No existe preview remoto ni URL persistente.
- Proveedor: no hay `netlify.toml`, Pages, workflow de despliegue ni decisión inequívoca. Netlify sigue siendo la preferencia del Plan Maestro y GitHub Pages la alternativa; esta puerta permanece pendiente después de la decisión editorial sobre `REV-*`.
- Seguridad e integridad: la salida pública no contiene `project/`, manuscrito fuente, PDF 0.6, QMD, scripts, configuración sensible, secretos ni rutas locales. `project/`, `plugins/`, `main` y `origin/main` permanecen intactos. No se hizo push, despliegue, merge, tag, release ni publicación definitiva.
- Estado: candidata técnicamente válida; 6A y Fase 6 permanecen abiertas. La consolidación editorial ampliada pasa a ser la puerta inmediata antes de cualquier auditoría especializada, corrección o preview remoto.

## Estado comprobado de 6A.1

- Baseline: auditoría iniciada en `088e4fcec91fa9723b5b0ffad4f65781a9c0af6c`, con candidata técnica `49ab2e1b1a58ca9201efab54b42a3125de7326f8`, upstream inicial `e74ce3cb8bd27921f50db5a046a0851528297ced`, upstream final pre-commit coincidente con la baseline y `main == origin/main == e81dc9239ac8dbabfe77168a50ef98c4d3b79170`.
- Referencia 0.6: réplica externa de 259 páginas, 6.806.113 bytes y SHA-256 `78551fc2bcc067634b97e6284b5a3b88b1916067851d51ee00b14e488e4187f4`; se usó solo como referencia editorial.
- Candidata: PDF de 334 páginas, 73.994.496 bytes y SHA-256 `f1eee2f465f554d3bf2b506d23a622967d1b4f1013ac657a774868e525688183`; no fue regenerado ni modificado.
- Comparación: Quarto conserva o mejora los 16 capítulos funcionales, 18 páginas completas, 35 unidades, 40 respuestas, cuatro aparatos generados, matriz de 112 entradas y nueve índices. Las pérdidas o carencias se concentran en metadatos/créditos, cartografía, referencias públicas y aparatos narrativos prometidos.
- Consolidación: la primera ronda de observaciones del usuario quedó fijada en `docs/ORDEN_DE_TRABAJO_PARA_V1_0.md` y propagada a la matriz sin modificar ese documento rector. La matriz contiene 26 entradas: 16 B, 5 M, 1 F y 4 N; ocho proceden de comparación con 0.6, cinco de auditoría actual y trece de observaciones del usuario. Todas las decisiones permanecen `PENDIENTE`.
- Paquetes y bloques: las REV se agrupan en ocho paquetes conceptuales y cinco bloques que deben resolverse antes de decidir 1.0: apertura e identidad, arquitectura de lectura, aparato histórico/documental, orientación visual y defectos finales de composición.
- Orden de trabajo: primero decisiones editoriales puras de arquitectura y apertura; después, por separado, auditorías de glosario/Estudio, gráficos/cartografía/recuadros y fuentes/bibliografía/aparatos; luego decisión definitiva, implementación, nueva candidata, validación, preview y aceptación.
- Investigación: cualquier conocimiento histórico nuevo deberá incorporarse primero a sus fuentes canónicas y propagarse por Estudio, Registro, glosario, capítulos, bibliografía e índices según corresponda; queda prohibido parchearlo directamente en Quarto o en `generated/`.
- Integridad: `project/`, `publication/`, la candidata y los derivados permanecen intactos; solo cambió documentación de auditoría. No se inició 6B ni se hizo preview remoto, despliegue, push, tag o release.
- Puerta inmediata: decisiones editoriales de arquitectura y apertura de la candidata 1.0. Las tres auditorías especializadas y cualquier modificación del libro quedan para pasos posteriores.

## Reglas para actualizar este roadmap

- Solo marcar una fase como completada cuando cumpla todos sus criterios.
- Registrar el commit de cierre y los resultados de validación.
- Mantener una sola `siguiente tarea exacta`.
- No convertir este archivo en diario detallado; los razonamientos estables van al plan maestro y los informes de validación tendrán documentos propios cuando sean necesarios.
- Si cambian fuentes canónicas, reauditar versiones y actualizar `meta/publication.yml` en una operación específica.

## Prompt recomendado para la siguiente sesión

> Lee `PROJECT.md`, `.github/copilot-instructions.md`, `docs/PLAN_MAESTRO_PUBLICACION_QUARTO.md`, `docs/ESTADO_PUBLICACION_QUARTO.md`, `docs/CANDIDATA_PUBLICACION_1_0.md`, `docs/INFORME_COMPARATIVO_PDF_0_6_Y_QUARTO.md`, `docs/ORDEN_DE_TRABAJO_PARA_V1_0.md`, `docs/REVISION_EDITORIAL_CANDIDATA_1_0.md`, `.github/instructions/publication.instructions.md` y `publication/README.md`. Continúa únicamente con las decisiones editoriales de arquitectura y apertura: prólogo, introducción, apertura, macroorden, duplicación funcional de imágenes, preliminares, cierres y navegación HTML. No ejecutes todavía las auditorías especializadas, no modifiques la candidata, no configures el preview remoto, no ejecutes 6B, no publiques 1.0, no crees tag/release y no alteres fuentes canónicas.

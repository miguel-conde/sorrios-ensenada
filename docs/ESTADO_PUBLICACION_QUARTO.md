# Estado y roadmap de la publicación Quarto

**Actualizado:** 4 de octubre de 2026<br>
**Estado global:** Fase 3 en curso; Fases 3A, 3B, 3C, 3D, 3E, 3F y 3G completadas<br>
**Fase actual:** 3H — capítulo 9 (siguiente; no iniciada)<br>
**Base documental auditada:** `6b49be848c92c4772b37c46495135352821d50f8`  
**Operación canónica al auditar:** `clean`

## Lectura de entrada

Una sesión nueva de Copilot debe leer, en este orden:

1. `PROJECT.md`;
2. `project/00_CONTROL/proyecto.yaml` y `estado.yaml`;
3. `.github/copilot-instructions.md`;
4. `docs/PLAN_MAESTRO_PUBLICACION_QUARTO.md`;
5. este roadmap;
6. `.github/instructions/publication.instructions.md`;
7. `publication/README.md`;
8. `docs/ESPECIFICACION_BOOTSTRAP_PUBLICATION.md` como registro de aceptación de la Fase 2A.

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
| 3. Contenido editorial | en curso | Fases 3A–3G completadas; capítulos 1–8 aceptados; Fase 3H como única tarea siguiente |
| 4. Generación documental | pendiente | capítulos 14–16, glosario, cuadros, concordancia y matriz reproducibles |
| 5. Índices y calidad integral | pendiente | nueve índices; HTML/PDF completos; accesibilidad y revisión visual |
| 6. Preview y publicación 1.0 | pendiente | snapshot, validación, preview aceptada, etiqueta y publicación con puerta editorial |

## Siguiente tarea exacta

Fase 3H: crear y validar exclusivamente el capítulo 9, «Río, molinos y otros recursos productivos», manteniendo la trazabilidad D/C/I/E/L y las cautelas ya fijadas sobre ruedas, titularidad, utilidades, dependencia hidráulica y relaciones causales, sin iniciar los capítulos 10–13 ni modificar fuentes canónicas.

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

## Reglas para actualizar este roadmap

- Solo marcar una fase como completada cuando cumpla todos sus criterios.
- Registrar el commit de cierre y los resultados de validación.
- Mantener una sola `siguiente tarea exacta`.
- No convertir este archivo en diario detallado; los razonamientos estables van al plan maestro y los informes de validación tendrán documentos propios cuando sean necesarios.
- Si cambian fuentes canónicas, reauditar versiones y actualizar `meta/publication.yml` en una operación específica.

## Prompt recomendado para la siguiente sesión

> Lee `PROJECT.md`, `.github/copilot-instructions.md`, `docs/PLAN_MAESTRO_PUBLICACION_QUARTO.md`, `docs/ESTADO_PUBLICACION_QUARTO.md`, `.github/instructions/publication.instructions.md` y `publication/README.md`. Ejecuta únicamente la Fase 3H: crea y valida exclusivamente el capítulo 9, «Río, molinos y otros recursos productivos», manteniendo la trazabilidad D/C/I/E/L y las cautelas sobre ruedas, titularidad, utilidades, dependencia hidráulica y relaciones causales, sin iniciar los capítulos 10–13 ni modificar fuentes canónicas. Revisa el diff y publica un único commit atómico solo si la rama sigue en el mismo `base_sha`.

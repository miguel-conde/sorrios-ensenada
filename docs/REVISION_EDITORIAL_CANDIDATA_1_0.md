# Revisión editorial consolidada de la candidata 1.0

**Fecha:** 9 de octubre de 2026<br>
**Fase:** 6A.2 — decisiones editoriales de arquitectura y apertura registradas<br>
**Estado:** decisiones 6A.2 cerradas documentalmente y Auditoría A completada; decisiones, datos, auditorías B/C e implementación pendientes<br>
**Informe de evidencia:** [INFORME_COMPARATIVO_PDF_0_6_Y_QUARTO.md](./INFORME_COMPARATIVO_PDF_0_6_Y_QUARTO.md)<br>
**Referencia de trabajo consolidada:** [ORDEN_DE_TRABAJO_PARA_V1_0.md](./ORDEN_DE_TRABAJO_PARA_V1_0.md)
**Registro de decisiones:** [DECISIONES_EDITORIALES_6A_2.md](./DECISIONES_EDITORIALES_6A_2.md)

## 1. Objeto

Este documento consolida la comparación integral entre la composición 0.6 y la candidata Quarto, la primera ronda de observaciones personales del usuario y el orden de trabajo acordado. La referencia principal para esta consolidación es `ORDEN_DE_TRABAJO_PARA_V1_0.md`; ese documento organiza el trabajo editorial, pero no es una fuente histórica ni sustituye las autoridades canónicas de `project/`.

La consolidación 6A.1 no modificó la candidata ni inició las auditorías especializadas. La operación 6A.2 registra ahora las decisiones humanas de arquitectura y apertura sin implementar ninguna de ellas. La composición 0.6 continúa siendo referencia editorial, no autoridad histórica o textual.

## 2. Baseline

| Elemento | Valor |
|---|---|
| Rama | `feature/quarto-book` |
| Baseline de esta consolidación | `dbeb50c8f266e5f2eba9cfa2a39c8010cfc78f1b` |
| Baseline de la auditoría 6A.1 | `088e4fcec91fa9723b5b0ffad4f65781a9c0af6c` |
| Commit de candidata técnica | `49ab2e1b1a58ca9201efab54b42a3125de7326f8` |
| `main` / `origin/main` | `e81dc9239ac8dbabfe77168a50ef98c4d3b79170` |
| Árbol `project/` | `e32917763475ceebdfe7b54830e1fb43f6419dad` |
| Árbol `publication/` | `cfcf349928fe3e1f2d3b33c005c31fa5621b1878` |
| PDF 0.6 | 259 páginas; 6.806.113 bytes; SHA-256 `78551fc2bcc067634b97e6284b5a3b88b1916067851d51ee00b14e488e4187f4` |
| PDF Quarto | 334 páginas; 73.994.496 bytes; SHA-256 `f1eee2f465f554d3bf2b506d23a622967d1b4f1013ac657a774868e525688183` |

La candidata técnica y las fuentes canónicas se mantienen en solo lectura durante esta operación.

## 3. Criterios B/M/F/N

### B — Bloqueante para 1.0

Cuestión que debe quedar resuelta antes de decidir la publicación 1.0. `B` no significa que la acción propuesta esté aprobada ni que siempre exista ya una solución elegida: puede ser un bloqueo de decisión editorial, de auditoría previa o de corrección técnica.

### M — Mejora conveniente

Mejora real que puede incorporarse a 1.0 si su coste y riesgo son razonables, pero cuya ausencia no invalida por sí sola la edición.

### F — Futura

Mejora o ampliación apropiada para 1.1 o posterior.

### N — No incorporar

Diferencia respecto a 0.6 superada, errónea, más débil, sustituida por una solución mejor o incompatible con la arquitectura vigente. Esta clasificación solo rechaza la recuperación de la solución antigua descrita; no cierra problemas nuevos con ID propio.

Todas son **clasificaciones propuestas**. Ninguna equivale a una decisión editorial del usuario ni autoriza implementación.

## 4. Matriz REV-*

| ID | Origen | Área | Observación | Evidencia 0.6 | Estado Quarto | Evaluación | Clasificación propuesta | Acción propuesta | Decisión del usuario |
|---|---|---|---|---|---|---|---|---|---|
| REV-001 | Auditoría actual | Identidad, créditos y metadatos | La candidata mantiene `0.1.0-dev`, `development`, «Edición en desarrollo», autor PDF vacío y carece de varias decisiones editoriales de publicación. | 0.6 identifica proyecto, versión y año, aunque tampoco resuelve todos los créditos. | 6A.2 aprueba T1 como identidad de trabajo, el modelo de créditos por roles, la resolución legal previa a la nueva candidata y que 1.0 no dependa de ISBN. Faltan nombres, roles concretos, titular, licencia, fecha, URL e identidad de proyecto. | Decisión editorial cerrada en principio, con datos humanos y legales pendientes. | B | Recabar los datos pendientes e implementar después de las auditorías; coordinar con REV-007, REV-015 y REV-022. No inventar valores. | APROBADA EN PRINCIPIO 6A.2 (`DEC-007`, `DEC-008`, `DEC-009`, `DEC-015`); datos e implementación pendientes |
| REV-002 | Comparación 0.6 | Cartografía | No existe equivalente de las láminas de orientación regional, provincial y local. | Págs. 16–17: tres escalas, topónimos útiles y cautelas sobre límites/localizadores. | No hay mapas ni assets cartográficos. | Carencia reforzada por 0.6, Plan Maestro, Plan de composición 0.5 e índice rector. | B | Auditar y seleccionar cartografía con procedencia, licencia, leyenda, cautelas y alternativas accesibles antes de diseñarla. | PENDIENTE |
| REV-003 | Comparación 0.6 | Fuentes externas y bibliografía | El sistema público de referencias es incompleto y la fuente queda a menudo alejada de la afirmación. | Pág. 15 y apéndice F: referencias identificables y enlaces visibles. | Existen URL y fuentes estructuradas, pero `references.bib` está vacío y no hay aparato bibliográfico público completo. | El problema es de sistema para el lector, no de número bruto de URL; requiere auditoría especializada. | B | Auditar fuentes, bibliografía y contextos E; definir después el sistema público de referencias. | PENDIENTE |
| REV-004 | Comparación 0.6 | Aparatos narrativos | Faltan cuestiones abiertas, historia de versiones y modelos de cita como funciones visibles del libro. | Apéndices E, G y H; el apéndice F cubre fuentes. | Límites e historia están dispersos o fuera del libro; no hay modelos de cita. | Las funciones prometidas deben resolverse, aunque no necesariamente mediante tres apéndices extensos; deben descomponerse funcionalmente. | B | Incluir estas funciones en la auditoría especializada de fuentes y aparatos; decidir forma y ubicación después. | PENDIENTE |
| REV-005 | Auditoría actual | Preliminares y orientación | Presentación, nota al lector, guía de uso, convenciones y cronología no forman unos preliminares consolidados. | 0.6 ofrece orientación inicial parcial. | 6A.2 aprueba P3: preliminares modulares multiformato, prólogo tras créditos, introducción con rutas y pieza compacta separada de convenciones. | Arquitectura editorial decidida; cronología, cartografía y otros recursos siguen sujetos a auditorías especializadas. | B | Implementar P3 solo después de las auditorías y de fijar los datos editoriales necesarios. | APROBADA 6A.2 (`DEC-001`, `DEC-003`, `DEC-004`); implementación pendiente |
| REV-006 | Auditoría actual | D/C/I/E/L y navegación | Las marcas del cuerpo son texto plano y su presencia visible se concentra en capítulos 9–13. | 95 grupos visibles; resolución manual en el apéndice D. | 77 grupos; matriz completa con anclas y retornos, sin enlace directo desde cada marca. | La cadena funciona, pero su experiencia de consulta puede mejorar. | M | Decidir una política coherente de marcas y enlaces sin saturar la prosa. | PENDIENTE |
| REV-007 | Comparación 0.6 | Cierre editorial | El volumen termina en el índice de materias sin colofón o declaración final de edición. | Pág. 259: colofón provisional. | 6A.2 aprueba un colofón breve técnico-editorial. Su contenido final depende de identidad, versión, URL y de la Auditoría C. | Decisión editorial cerrada; alcance concreto e implementación pendientes. | M | Definir el contenido final tras la Auditoría C e implementarlo coordinadamente con REV-001 y REV-004. | APROBADA 6A.2 (`DEC-010`); dependencias e implementación pendientes |
| REV-008 | Auditoría actual | Accesibilidad formal | El PDF no está etiquetado y no existe validación PDF/UA o PDF/A. | 0.6 tampoco está etiquetado. | Accesibilidad básica validada; no se declara conformidad formal. | No es regresión ni bloqueante conocido para 1.0; requiere alcance y herramientas específicos. | F | Mantener la limitación declarada y estudiar conformidad formal en 1.1 o posterior. | PENDIENTE |
| REV-009 | Comparación 0.6 | Contenido histórico superado | 0.6 contiene formulaciones demasiado fuertes sobre comunales, autoconsumo, clima, copropiedad, ruedas, habitantes fiscales y amortiguación. | Expresiones localizadas en la Parte II. | Quarto las elimina o reformula con límites y distinciones de autoridad. | Recuperarlas sería una regresión metodológica e histórica. | N | Conservar las formulaciones actuales; usar 0.6 solo como prueba negativa de regresión. | PENDIENTE |
| REV-010 | Comparación 0.6 | Modelo antiguo de facsímil | 0.6 presenta el facsímil solo como 35 unidades con recortes grandes. | Págs. 64–98: 35 imágenes de unidad. | Quarto ofrece 18 páginas completas y 35 recortes de cotejo en la transcripción. | No debe recuperarse el modelo exclusivo de 0.6. Esta negativa no resuelve la duplicación funcional actual, tratada en REV-016. | N | No volver al facsímil exclusivo por unidades; decidir REV-016 de manera independiente. | PENDIENTE |
| REV-011 | Comparación 0.6 | Modelo antiguo de índices | Los índices 6–9 de 0.6 son provisionales y carecen de páginas finales. | 129 entradas contadas y localizadores provisionales. | Quarto genera nueve índices más amplios con localizadores reales. | No deben recuperarse las listas antiguas. Los defectos actuales de composición están separados en REV-023 y REV-025. | N | Mantener la arquitectura generada; resolver por separado los defectos actuales. | PENDIENTE |
| REV-012 | Comparación 0.6 | Formato y diseño antiguos | 0.6 usa A4, color y una maqueta más ornamental. | Portada, encabezados y aperturas más elaborados. | Quarto usa Letter y diseño sobrio multiformato. | No hay fundamento para copiar paginación o maqueta 0.6; esto tampoco declara Letter como solución definitiva para una eventual impresión. | N | No imitar 0.6; cualquier decisión futura de impresión deberá justificarse por su propio alcance. | PENDIENTE |
| REV-013 | Observación del usuario | Preliminares y autoría personal | El usuario echa de menos un prólogo y probablemente lo escribirá personalmente para explicar origen, circunstancias y personas vinculadas al libro. | No es una recuperación automática de 0.6. | 6A.2 aprueba un prólogo personal y firmado, de unas 900–1.500 palabras, situado después de los créditos. | Función, extensión y posición decididas; el texto corresponde al usuario. | B | Reservar la pieza; redactarla el usuario y revisarla después preservando su voz. | APROBADA 6A.2 (`DEC-002`, `DEC-003`); texto e implementación pendientes |
| REV-014 | Observación del usuario | Introducción y guía de lectura | El volumen necesita explicar contenido, estructura, relación entre sus capas y posibles itinerarios de lectura. | 0.6 ofrecía orientación parcial. | 6A.2 aprueba una introducción con rutas histórica y documental, una pieza compacta separada de convenciones y un resumen enlazado del capítulo 4. | Alcance, relación y ubicación decididos; redacción pendiente. | B | Redactar e implementar después de las auditorías, conservando el capítulo 4 como explicación metodológica detallada. | APROBADA 6A.2 (`DEC-004`, `DEC-005`, `DEC-011`); implementación pendiente |
| REV-015 | Observación del usuario | Apertura editorial | `index.qmd` continúa siendo una apertura de prepublicación y presenta como provisional la identidad visible del libro. | 0.6 tenía una apertura compuesta, sin ser modelo obligatorio. | 6A.2 aprueba landing HTML breve, portada PDF propia y preliminares separados; T1 queda como título/subtítulo de trabajo. | Modelo de apertura decidido; metadata y candidata continúan intactas. | B | Implementar después junto con REV-001, REV-005, REV-013, REV-014 y REV-022. | APROBADA 6A.2 (`DEC-006`, `DEC-007`); implementación pendiente |
| REV-016 | Observación del usuario | Duplicación funcional del manuscrito | Parte III presenta 18 páginas completas y Parte IV vuelve a mostrar el manuscrito mediante 35 recortes. | 0.6 utilizaba solo recortes, modelo descartado por REV-010. | 6A.2 selecciona F3 como hipótesis de prototipo: facsímil íntegro, recortes completos en HTML y miniaturas/localizadores enlazados en PDF. | Decisión de prototipo, no solución final irreversible. | B | Construir y validar un prototipo posterior; adoptar o revisar F3 solo tras comprobar cotejo, legibilidad, accesibilidad, paginación y peso. | PROTOTIPO APROBADO 6A.2 (`DEC-012`); validación, decisión final e implementación pendientes |
| REV-017 | Observación del usuario | Macroorden del volumen | El estudio histórico precede al facsímil, transcripción y modernizada. | 0.6 y el índice rector sostienen el orden contexto → estudio → documento. | 6A.2 mantiene el macroorden actual y añade dos rutas explícitas, histórica y documental. | Decisión arquitectónica cerrada sin reordenar el volumen. | B | Implementar las rutas en introducción, landing y navegación después de las auditorías. | APROBADA 6A.2 (`DEC-011`); implementación pendiente |
| REV-018 | Observación del usuario | Navegación HTML | La barra lateral aparece inicialmente demasiado desplegada para seis partes y unos treinta documentos. | No aplica. | 6A.2 aprueba parte activa desplegada y partes inactivas plegadas. | Decisión UX cerrada; requiere implementación y validación HTML. | M | Implementar y comprobar teclado, escritorio y viewport estrecho en una operación posterior. | APROBADA 6A.2 (`DEC-014`); implementación pendiente |
| REV-019 | Observación del usuario | Cierre de capítulos | Capítulos 5–13 tienen cierre funcional, pero solo 9–12 usan literalmente «Síntesis». | No aplica. | 6A.2 aprueba títulos conclusivos específicos con función común y la sustitución de `Síntesis` cuando exista un título informativo adecuado. | Convención retórica decidida; los textos no se modifican todavía. | M | Revisar conjuntamente los títulos de cierre e implementarlos en una operación posterior. | APROBADA 6A.2 (`DEC-013`); implementación pendiente |
| REV-020 | Observación del usuario | Glosario y contexto histórico | El ejemplo «Señorío» muestra que el glosario explica principalmente el sentido documental/local y no siempre el concepto históricamente. | 0.6 no decide la arquitectura correcta para la fuente vigente. | La [Auditoría A](./AUDITORIA_GLOSARIO_ESTUDIO_HISTORICO_V1_0.md) revisa las 22 voces: G0 8, G1 7, G2 0, G3 4 y G4 3; propone GH-B selectivo y registra 6 candidatos provisionales. No se modificaron fuentes ni candidata. | La carencia es selectiva: `Señorío` y otros seis casos pueden mejorar con conocimiento existente; cuatro ampliaciones exigirían investigación externa y no hay G2. | B | Decidir el modelo GH, el alcance para 1.0, los candidatos y si se autoriza investigar algún G3. No implementar ni investigar hasta esa decisión. | AUDITORÍA REALIZADA; DECISIÓN PENDIENTE |
| REV-021 | Observación del usuario | Gráficos, esquemas y recuadros | El usuario echa de menos recursos explicativos presentes o previstos en composiciones anteriores. | El recuento de imágenes incrustadas puede omitir gráficos vectoriales; 0.6 y el Plan 0.5 requieren inventario específico. | Existen tablas, pero no se ha comparado de forma exhaustiva cronología visual, esquemas, recuadros y diagramas previstos. | Bloqueante de auditoría y selección; no toda pieza antigua debe recuperarse. | B | Inventariar `0.6 + Plan 0.5 + candidata` y clasificar cada recurso como conservar, reconstruir, sustituir o descartar. | PENDIENTE |
| REV-022 | Observación del usuario | Estado visible de edición | «Edición en desarrollo» aparece en subtítulo, metadatos y apertura. | 0.6 mostraba una versión de composición, no una solución definitiva. | 6A.2 aprueba que esa fórmula no forme parte de la identidad final y adopta T1 como título/subtítulo de trabajo. La metadata actual no se modifica en esta operación. | Decisión editorial cerrada; retirada e identidad final pendientes de implementación. | B | Sustituir el estado visible únicamente al construir la nueva candidata, coordinado con REV-001 y REV-015. | APROBADA 6A.2 (`DEC-006`, `DEC-007`); implementación pendiente |
| REV-023 | Observación del usuario | TOC PDF | Numeraciones largas aparecen pegadas a los títulos, por ejemplo `16.35Respuesta 32...`. | No aplica. | Defecto visual comprobado en la candidata. | Bloqueante técnico de composición; debe cubrir especialmente numeraciones largas del capítulo 16. | B | Corregir anchura o separación del número de sección en una operación posterior y probar los casos extremos. | PENDIENTE |
| REV-024 | Observación del usuario | Orden del glosario | El Plan de composición 0.5 exige orden alfabético. | No aplica. | Los índices alfabéticos se ordenan de forma determinista; el glosario generado conserva el orden de `Glosario.md`. | Desviación técnica/editorial real. | B | Corregir preferentemente en generación/publicación, sin alterar innecesariamente la fuente canónica. | PENDIENTE |
| REV-025 | Observación del usuario | Índices PDF | Las entradas del índice onomástico aparecen pegadas; el problema también se observa en lugares/topónimos. | No aplica a la recuperación de los índices antiguos. | HTML tiene estilo `.index-entry`; PDF carece de separación visual equivalente suficiente. | Bloqueante técnico; la arquitectura compartida exige comprobar los nueve índices. | B | Diseñar posteriormente el tratamiento PDF y validar separación, jerarquía y cortes en los nueve índices. | PENDIENTE |
| REV-026 | Auditoría actual | Peso del PDF y bundle web | La candidata PDF ronda 74 MB frente a unos 6,8 MB en 0.6. | 0.6: 6.806.113 bytes. | Quarto: 73.994.496 bytes; la diferencia procede principalmente de imágenes del manuscrito. | No es por sí sola una regresión, pero conviene evaluar optimización antes del despliegue sin perder calidad documental o paleográfica. | M | Medir y ensayar optimización en una operación posterior; no optimizar ahora. | PENDIENTE |

## 5. Observaciones del usuario incorporadas

La primera ronda de observaciones personales está incorporada como `REV-013`–`REV-025`, con `Origen: Observación del usuario`. Incluye los defectos visuales documentados mediante capturas y las dudas editoriales sobre apertura, arquitectura, glosario y recursos gráficos.

Que una observación proceda del usuario no la convierte automáticamente en una decisión de implementación. 6A.2 cierra las decisiones de `REV-013`–`REV-019` y `REV-022` con los matices registrados en [DECISIONES_EDITORIALES_6A_2.md](./DECISIONES_EDITORIALES_6A_2.md); ninguna está implementada. Las demás conservan su estado pendiente. Las observaciones futuras comenzarán en `REV-027`, sin renumerar ni reutilizar IDs.

La Auditoría A de `REV-020` está realizada: clasificó 22 entradas en G0 8, G1 7, G2 0, G3 4 y G4 3; recomienda conceptualmente GH-B selectivo e identifica 6 candidatos provisionales a nueva entrada. Es un resultado diagnóstico: no cierra `REV-020`, no autoriza investigación o implementación y remite a `REV-003`, `REV-004` y `REV-021` solo por sus posibles efectos sobre bibliografía, aparatos y recursos explicativos.

## 6. Decisiones del usuario

| ID | Decisión del usuario | Notas de decisión |
|---|---|---|
| REV-001 | APROBADA EN PRINCIPIO 6A.2 | `DEC-007`, `DEC-008`, `DEC-009`, `DEC-015`; faltan datos concretos e implementación. |
| REV-002 | PENDIENTE | — |
| REV-003 | PENDIENTE | — |
| REV-004 | PENDIENTE | — |
| REV-005 | APROBADA 6A.2 | P3, prólogo, introducción y convenciones; implementación pendiente. |
| REV-006 | PENDIENTE | — |
| REV-007 | APROBADA 6A.2 | Colofón breve; depende de datos finales y parcialmente de la Auditoría C. |
| REV-008 | PENDIENTE | — |
| REV-009 | PENDIENTE | — |
| REV-010 | PENDIENTE | — |
| REV-011 | PENDIENTE | — |
| REV-012 | PENDIENTE | — |
| REV-013 | APROBADA 6A.2 | Prólogo personal y firmado, 900–1.500 palabras, después de créditos; texto pendiente. |
| REV-014 | APROBADA 6A.2 | Introducción con dos rutas y convenciones separadas; redacción e implementación pendientes. |
| REV-015 | APROBADA 6A.2 | Landing HTML, portada PDF y preliminares separados; implementación pendiente. |
| REV-016 | PROTOTIPO APROBADO 6A.2 | F3 debe validarse antes de una decisión final; no implementada. |
| REV-017 | APROBADA 6A.2 | Macroorden actual con rutas histórica y documental; implementación pendiente. |
| REV-018 | APROBADA 6A.2 | Parte activa desplegada y partes inactivas plegadas; implementación pendiente. |
| REV-019 | APROBADA 6A.2 | Cierres específicos con función común; implementación pendiente. |
| REV-020 | AUDITORÍA REALIZADA; DECISIÓN PENDIENTE | G0 8, G1 7, G2 0, G3 4, G4 3; GH-B selectivo recomendado; 6 candidatos provisionales; sin investigación ni implementación. |
| REV-021 | PENDIENTE | — |
| REV-022 | APROBADA 6A.2 | T1 sustituirá la identidad visible de desarrollo al implementar la nueva candidata; metadata intacta por ahora. |
| REV-023 | PENDIENTE | — |
| REV-024 | PENDIENTE | — |
| REV-025 | PENDIENTE | — |
| REV-026 | PENDIENTE | — |

Las decisiones aprobadas en 6A.2 no equivalen a implementación. Las restantes `REV-*` mantienen sus clasificaciones propuestas y su decisión `PENDIENTE` hasta una decisión humana posterior.

## 7. Paquetes de decisión consolidados

### A. Identidad y apertura del libro

`REV-001`, `REV-005`, `REV-007`, `REV-013`, `REV-014`, `REV-015`, `REV-022`.

6A.2 cierra la arquitectura del paquete: T1, P3, prólogo, introducción, apertura y colofón. Permanecen pendientes los datos concretos de créditos, copyright/licencia, fecha, URL e identidad de proyecto, además de la implementación y de dependencias de la Auditoría C.

### B. Arquitectura del volumen

`REV-016`, `REV-017`.

El macroorden queda cerrado: se conserva el actual con dos rutas explícitas. F3 queda seleccionada únicamente para prototipo y validación antes de una decisión final sobre la duplicación funcional.

### C. Investigación y contexto histórico

`REV-003`, `REV-004`, `REV-020` y la parte histórica de `REV-021`.

Fuentes, bibliografía, cuestiones abiertas, modelos de cita, glosario y posible investigación histórica.

### D. Orientación visual

`REV-002`, `REV-021`.

Cartografía, cronología visual, gráficos, esquemas y recuadros.

### E. Trazabilidad y ayudas de consulta

`REV-006`, `REV-024`.

Navegación D/C/I/E/L y glosario ordenado.

### F. UX y composición

`REV-018`, `REV-019`, `REV-023`, `REV-025`, `REV-026`.

Sidebar y convención de cierres quedan decididos en 6A.2, sin implementar. TOC PDF, índices PDF y tamaño de salidas continúan pendientes.

### G. Trabajo futuro

`REV-008`.

Etiquetado PDF y validación formal PDF/UA o PDF/A.

### H. Decisiones negativas sólidas

`REV-009`, `REV-010`, `REV-011`, `REV-012`.

`H` significa no recuperar soluciones antiguas de 0.6. No significa cerrar otras cuestiones nuevas: en particular, REV-010 no resuelve REV-016 y REV-011 no resuelve REV-023 o REV-025.

## 8. Cinco bloques que deben resolverse antes de 1.0

1. **Apertura e identidad editorial:** arquitectura decidida en 6A.2; quedan datos, dependencias e implementación.
2. **Arquitectura de lectura:** macroorden decidido; F3 pendiente de prototipo y validación.
3. **Aparato histórico y documental:** bibliografía/fuentes, cuestiones abiertas/modelos de cita y auditoría del glosario.
4. **Orientación visual:** cartografía y auditoría de gráficos, esquemas y recuadros.
5. **Defectos finales de composición:** TOC PDF, glosario alfabético e índices PDF.

Son grupos de cuestiones que deben resolverse antes de decidir la publicación 1.0, no cinco tareas de implementación ya aprobadas.

## 9. Regla transversal para nueva investigación histórica

Si una auditoría demuestra que hace falta investigación histórica nueva, queda prohibido parchear directamente el libro Quarto, `generated/` o el glosario publicado. La secuencia será, ajustando solo las etapas no aplicables:

```text
investigación
→ fuente canónica correspondiente
→ Estudio Histórico
→ Registro D/C/I/E/L, si procede
→ glosario
→ capítulos afectados
→ fuentes/bibliografía
→ índices
→ regeneración Quarto
```

## 10. Orden de trabajo acordado

1. **Consolidación documental:** completada en 6A.1; fijó REV-001–REV-026 sin modificar la candidata ni investigar.
2. **Decisiones editoriales puras:** completadas documentalmente en 6A.2; quedan pendientes los datos señalados, el prototipo F3 y toda implementación.
3. **Tres auditorías especializadas:**
   - glosario / Estudio Histórico / necesidad real de investigación: Auditoría A completada; decisiones pendientes;
   - gráficos, recuadros y cartografía: 0.6 + Plan 0.5 + candidata;
   - fuentes, bibliografía y aparatos narrativos.
4. **Decisión definitiva:** clasificar cada cuestión como 1.0, 1.1+, no incorporar o investigación previa.
5. **Implementación:** plan de cambios, operaciones canónicas cuando procedan, cambios Quarto, nueva candidata, validación, preview, aceptación humana y, solo después, 6B.

La Auditoría A completa el primer componente del paso 3 sin ejecutar investigación ni implementación. El siguiente trabajo es la Auditoría B; no se inicia aquí.

## 11. Lista propuesta para 1.0

La propuesta actual es resolver los cinco bloques del apartado 8 antes de decidir la publicación. 6A.2 resuelve las decisiones puramente editoriales enumeradas en su registro, pero no aprueba todavía una implementación, no cierra las auditorías ni convierte F3 en solución definitiva. `Resolver` puede significar elegir una opción, completar una auditoría previa, aprobar una corrección o decidir justificadamente no implementar una solución concreta.

Las mejoras M pueden incorporarse si el usuario lo decide y su coste/riesgo resulta razonable. Las entradas N son propuestas de no recuperar soluciones antiguas, no trabajo de implementación.

## 12. Backlog propuesto 1.1+

- `REV-008`: estudiar etiquetado PDF y validación formal PDF/UA o PDF/A.
- Cualquier ampliación histórica que no resulte necesaria para cerrar 1.0 deberá clasificarse después de la auditoría correspondiente.

## 13. Recuento consolidado

| Clasificación propuesta | Número |
|---|---:|
| B | 16 |
| M | 5 |
| F | 1 |
| N | 4 |
| **Total** | **26** |

| Origen | Número |
|---|---:|
| Comparación 0.6 | 8 |
| Auditoría actual | 5 |
| Observación del usuario | 13 |

## 14. Puerta editorial

La candidata no debe modificarse todavía. Las decisiones editoriales 6A.2 y el diagnóstico de la Auditoría A quedan registrados, pero la decisión sobre `REV-020`, las auditorías B y C, los datos humanos y legales, el prototipo F3, el alcance definitivo y toda implementación siguen pendientes.

## 15. Datos editoriales pendientes del usuario

Sin inventar valores, siguen pendientes:

- nombre que debe figurar como autor;
- roles editoriales concretos;
- responsables de transcripción y modernización, si deben acreditarse de forma diferenciada;
- colaboradores;
- titular del copyright;
- licencia concreta;
- fecha editorial final;
- URL canónica cuando exista;
- identidad de proyecto que deba mostrarse.

Estos datos no bloquean el cierre documental de 6A.2. Los que afecten a créditos o metadata deberán resolverse antes de construir la nueva candidata.

## 16. Tag, versión e implementación

No se crea tag ahora. La candidata técnica `49ab2e1b1a58ca9201efab54b42a3125de7326f8` no es 1.0 y la consolidación documental tampoco lo es. No habrá tag intermedio: el tag final solo podrá plantearse después de auditorías, implementación, nueva candidata, preview, aceptación humana y Fase 6B.

Ninguna `REV-*` se marca como implementada en esta operación.

**SIGUIENTE PASO: Auditoría B — gráficos / cartografía / recuadros: 0.6 + Plan 0.5 + candidata.**

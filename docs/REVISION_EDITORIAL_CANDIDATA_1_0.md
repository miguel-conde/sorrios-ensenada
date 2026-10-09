# Revisión editorial consolidada de la candidata 1.0

**Fecha:** 9 de octubre de 2026<br>
**Fase:** 6A.1 — consolidación posterior a la primera ronda de observaciones del usuario<br>
**Estado:** cuestiones y clasificaciones propuestas; todas las decisiones permanecen pendientes<br>
**Informe de evidencia:** [INFORME_COMPARATIVO_PDF_0_6_Y_QUARTO.md](./INFORME_COMPARATIVO_PDF_0_6_Y_QUARTO.md)<br>
**Referencia de trabajo consolidada:** [ORDEN_DE_TRABAJO_PARA_V1_0.md](./ORDEN_DE_TRABAJO_PARA_V1_0.md)

## 1. Objeto

Este documento consolida la comparación integral entre la composición 0.6 y la candidata Quarto, la primera ronda de observaciones personales del usuario y el orden de trabajo acordado. La referencia principal para esta consolidación es `ORDEN_DE_TRABAJO_PARA_V1_0.md`; ese documento organiza el trabajo editorial, pero no es una fuente histórica ni sustituye las autoridades canónicas de `project/`.

La consolidación no modifica la candidata, no implementa correcciones, no inicia las auditorías especializadas y no decide qué solución debe entrar definitivamente en 1.0. La composición 0.6 continúa siendo referencia editorial, no autoridad histórica o textual.

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
| REV-001 | Auditoría actual | Identidad, créditos y metadatos | La candidata mantiene `0.1.0-dev`, `development`, «Edición en desarrollo», autor PDF vacío y carece de varias decisiones editoriales de publicación. | 0.6 identifica proyecto, versión y año, aunque tampoco resuelve todos los créditos. | Las decisiones sobre autoría o responsabilidad, fecha, licencia, copyright, URL y demás metadatos siguen abiertas. | Bloqueante editorial que agrupa decisiones distintas y deberá descomponerse antes de implementar. | B | Resolver separadamente identidad, responsabilidades y metadatos; coordinar con REV-007, REV-015 y REV-022. No inventar valores. | PENDIENTE |
| REV-002 | Comparación 0.6 | Cartografía | No existe equivalente de las láminas de orientación regional, provincial y local. | Págs. 16–17: tres escalas, topónimos útiles y cautelas sobre límites/localizadores. | No hay mapas ni assets cartográficos. | Carencia reforzada por 0.6, Plan Maestro, Plan de composición 0.5 e índice rector. | B | Auditar y seleccionar cartografía con procedencia, licencia, leyenda, cautelas y alternativas accesibles antes de diseñarla. | PENDIENTE |
| REV-003 | Comparación 0.6 | Fuentes externas y bibliografía | El sistema público de referencias es incompleto y la fuente queda a menudo alejada de la afirmación. | Pág. 15 y apéndice F: referencias identificables y enlaces visibles. | Existen URL y fuentes estructuradas, pero `references.bib` está vacío y no hay aparato bibliográfico público completo. | El problema es de sistema para el lector, no de número bruto de URL; requiere auditoría especializada. | B | Auditar fuentes, bibliografía y contextos E; definir después el sistema público de referencias. | PENDIENTE |
| REV-004 | Comparación 0.6 | Aparatos narrativos | Faltan cuestiones abiertas, historia de versiones y modelos de cita como funciones visibles del libro. | Apéndices E, G y H; el apéndice F cubre fuentes. | Límites e historia están dispersos o fuera del libro; no hay modelos de cita. | Las funciones prometidas deben resolverse, aunque no necesariamente mediante tres apéndices extensos; deben descomponerse funcionalmente. | B | Incluir estas funciones en la auditoría especializada de fuentes y aparatos; decidir forma y ubicación después. | PENDIENTE |
| REV-005 | Auditoría actual | Preliminares y orientación | Presentación, nota al lector, guía de uso, convenciones y cronología no forman unos preliminares consolidados. | 0.6 ofrece orientación inicial parcial. | Sus funciones están ausentes o repartidas entre capítulos y aparatos. | La ronda del usuario confirma que la apertura y orientación son cuestiones sustantivas para 1.0. | B | Definir la arquitectura de preliminares junto con REV-013–REV-015 y decidir qué funciones se reúnen antes del capítulo 1. | PENDIENTE |
| REV-006 | Auditoría actual | D/C/I/E/L y navegación | Las marcas del cuerpo son texto plano y su presencia visible se concentra en capítulos 9–13. | 95 grupos visibles; resolución manual en el apéndice D. | 77 grupos; matriz completa con anclas y retornos, sin enlace directo desde cada marca. | La cadena funciona, pero su experiencia de consulta puede mejorar. | M | Decidir una política coherente de marcas y enlaces sin saturar la prosa. | PENDIENTE |
| REV-007 | Comparación 0.6 | Cierre editorial | El volumen termina en el índice de materias sin colofón o declaración final de edición. | Pág. 259: colofón provisional. | El informe técnico de candidata queda fuera del libro. | Mejora conveniente, posiblemente absorbible por identidad, versiones o modelos de cita. | M | Valorar un cierre mínimo coordinado con REV-001 y REV-004. | PENDIENTE |
| REV-008 | Auditoría actual | Accesibilidad formal | El PDF no está etiquetado y no existe validación PDF/UA o PDF/A. | 0.6 tampoco está etiquetado. | Accesibilidad básica validada; no se declara conformidad formal. | No es regresión ni bloqueante conocido para 1.0; requiere alcance y herramientas específicos. | F | Mantener la limitación declarada y estudiar conformidad formal en 1.1 o posterior. | PENDIENTE |
| REV-009 | Comparación 0.6 | Contenido histórico superado | 0.6 contiene formulaciones demasiado fuertes sobre comunales, autoconsumo, clima, copropiedad, ruedas, habitantes fiscales y amortiguación. | Expresiones localizadas en la Parte II. | Quarto las elimina o reformula con límites y distinciones de autoridad. | Recuperarlas sería una regresión metodológica e histórica. | N | Conservar las formulaciones actuales; usar 0.6 solo como prueba negativa de regresión. | PENDIENTE |
| REV-010 | Comparación 0.6 | Modelo antiguo de facsímil | 0.6 presenta el facsímil solo como 35 unidades con recortes grandes. | Págs. 64–98: 35 imágenes de unidad. | Quarto ofrece 18 páginas completas y 35 recortes de cotejo en la transcripción. | No debe recuperarse el modelo exclusivo de 0.6. Esta negativa no resuelve la duplicación funcional actual, tratada en REV-016. | N | No volver al facsímil exclusivo por unidades; decidir REV-016 de manera independiente. | PENDIENTE |
| REV-011 | Comparación 0.6 | Modelo antiguo de índices | Los índices 6–9 de 0.6 son provisionales y carecen de páginas finales. | 129 entradas contadas y localizadores provisionales. | Quarto genera nueve índices más amplios con localizadores reales. | No deben recuperarse las listas antiguas. Los defectos actuales de composición están separados en REV-023 y REV-025. | N | Mantener la arquitectura generada; resolver por separado los defectos actuales. | PENDIENTE |
| REV-012 | Comparación 0.6 | Formato y diseño antiguos | 0.6 usa A4, color y una maqueta más ornamental. | Portada, encabezados y aperturas más elaborados. | Quarto usa Letter y diseño sobrio multiformato. | No hay fundamento para copiar paginación o maqueta 0.6; esto tampoco declara Letter como solución definitiva para una eventual impresión. | N | No imitar 0.6; cualquier decisión futura de impresión deberá justificarse por su propio alcance. | PENDIENTE |
| REV-013 | Observación del usuario | Preliminares y autoría personal | El usuario echa de menos un prólogo y probablemente lo escribirá personalmente para explicar origen, circunstancias y personas vinculadas al libro. | No es una recuperación automática de 0.6. | No existe esa pieza personal. | Es una función de apertura importante y no debe generarse como contenido histórico canónico. | B | Reservar una pieza preliminar personal; redacción del usuario y eventual revisión editorial posterior que preserve su voz. | PENDIENTE |
| REV-014 | Observación del usuario | Introducción y guía de lectura | El volumen necesita explicar contenido, estructura, relación entre sus capas y posibles itinerarios de lectura. | 0.6 ofrecía orientación parcial. | La información está repartida y no existe una guía inicial consolidada. | Bloqueante editorial para orientar un volumen de seis partes y más de 300 páginas. | B | Decidir alcance y ubicación de una introducción/guía antes de redactarla. | PENDIENTE |
| REV-015 | Observación del usuario | Apertura editorial | `index.qmd` continúa siendo una apertura de prepublicación y presenta como provisional la identidad visible del libro. | 0.6 tenía una apertura compuesta, sin ser modelo obligatorio. | El libro abre con «Edición en desarrollo» y declara estado de prepublicación. | Debe resolverse coordinadamente con título, subtítulo, prólogo, introducción, créditos y metadatos. | B | Definir primero el modelo de apertura; implementar después junto con REV-001, REV-005, REV-013, REV-014 y REV-022. | PENDIENTE |
| REV-016 | Observación del usuario | Duplicación funcional del manuscrito | Parte III presenta 18 páginas completas y Parte IV vuelve a mostrar el manuscrito mediante 35 recortes. | 0.6 utilizaba solo recortes, modelo descartado por REV-010. | No hay duplicación técnica exacta, pero sí posible repetición perceptiva, especialmente en PDF; la imagen junto a la transcripción permite cotejo. | Bloqueante de decisión, no presupone eliminar ninguna vista. | B | Estudiar: mantener ambas vistas; diferenciarlas por formato; usar miniatura/enlace/referencia en PDF; u otra integración equivalente. No elegir todavía. | PENDIENTE |
| REV-017 | Observación del usuario | Macroorden del volumen | El estudio histórico precede al facsímil, transcripción y modernizada. | 0.6 y el índice rector sostienen el orden contexto → estudio → documento. | El orden actual es deliberado y defendible, pero antepone interpretación a la lectura sistemática de la fuente. | Bloqueante de decisión arquitectónica. | B | Decidir después entre mantener el orden, adelantar el documento o mantenerlo con itinerarios de lectura explícitos. No reordenar ahora. | PENDIENTE |
| REV-018 | Observación del usuario | Navegación HTML | La barra lateral aparece inicialmente demasiado desplegada para seis partes y unos treinta documentos. | No aplica. | La navegación funciona, pero su densidad inicial puede reducir usabilidad. | Mejora de alto valor y bajo alcance, candidata a 1.0. | M | Valorar partes inicialmente plegadas con expansión voluntaria; no modificar `_quarto.yml` en esta operación. | PENDIENTE |
| REV-019 | Observación del usuario | Cierre de capítulos | Capítulos 5–13 tienen cierre funcional, pero solo 9–12 usan literalmente «Síntesis». | No aplica. | Los demás emplean títulos conclusivos específicos. | Es una cuestión de consistencia retórica, no ausencia de cierre; uniformidad funcional no implica título idéntico. | M | Revisar en conjunto los cierres y acordar una convención antes de editar capítulos. | PENDIENTE |
| REV-020 | Observación del usuario | Glosario y contexto histórico | El ejemplo «Señorío» muestra que el glosario explica principalmente el sentido documental/local y no siempre el concepto históricamente. | 0.6 no decide la arquitectura correcta para la fuente vigente. | El generador reproduce correctamente `Glosario.md`, cuya autoridad evita interpretación histórica extensa. | Bloqueante de auditoría previa: la posible carencia puede estar aguas arriba, no ser solo de presentación. | B | Auditar Estudio, términos y huecos; distinguir contexto ya disponible, investigación nueva, contenido del Estudio y síntesis de glosario. No elegir solución todavía. | PENDIENTE |
| REV-021 | Observación del usuario | Gráficos, esquemas y recuadros | El usuario echa de menos recursos explicativos presentes o previstos en composiciones anteriores. | El recuento de imágenes incrustadas puede omitir gráficos vectoriales; 0.6 y el Plan 0.5 requieren inventario específico. | Existen tablas, pero no se ha comparado de forma exhaustiva cronología visual, esquemas, recuadros y diagramas previstos. | Bloqueante de auditoría y selección; no toda pieza antigua debe recuperarse. | B | Inventariar `0.6 + Plan 0.5 + candidata` y clasificar cada recurso como conservar, reconstruir, sustituir o descartar. | PENDIENTE |
| REV-022 | Observación del usuario | Estado visible de edición | «Edición en desarrollo» aparece en subtítulo, metadatos y apertura. | 0.6 mostraba una versión de composición, no una solución definitiva. | Es la identidad visible actual. | No puede permanecer como identidad final de una edición 1.0; depende funcionalmente de REV-001 y REV-015. | B | Resolver e implementar dentro del paquete de identidad y apertura, sin inventar una fórmula ahora. | PENDIENTE |
| REV-023 | Observación del usuario | TOC PDF | Numeraciones largas aparecen pegadas a los títulos, por ejemplo `16.35Respuesta 32...`. | No aplica. | Defecto visual comprobado en la candidata. | Bloqueante técnico de composición; debe cubrir especialmente numeraciones largas del capítulo 16. | B | Corregir anchura o separación del número de sección en una operación posterior y probar los casos extremos. | PENDIENTE |
| REV-024 | Observación del usuario | Orden del glosario | El Plan de composición 0.5 exige orden alfabético. | No aplica. | Los índices alfabéticos se ordenan de forma determinista; el glosario generado conserva el orden de `Glosario.md`. | Desviación técnica/editorial real. | B | Corregir preferentemente en generación/publicación, sin alterar innecesariamente la fuente canónica. | PENDIENTE |
| REV-025 | Observación del usuario | Índices PDF | Las entradas del índice onomástico aparecen pegadas; el problema también se observa en lugares/topónimos. | No aplica a la recuperación de los índices antiguos. | HTML tiene estilo `.index-entry`; PDF carece de separación visual equivalente suficiente. | Bloqueante técnico; la arquitectura compartida exige comprobar los nueve índices. | B | Diseñar posteriormente el tratamiento PDF y validar separación, jerarquía y cortes en los nueve índices. | PENDIENTE |
| REV-026 | Auditoría actual | Peso del PDF y bundle web | La candidata PDF ronda 74 MB frente a unos 6,8 MB en 0.6. | 0.6: 6.806.113 bytes. | Quarto: 73.994.496 bytes; la diferencia procede principalmente de imágenes del manuscrito. | No es por sí sola una regresión, pero conviene evaluar optimización antes del despliegue sin perder calidad documental o paleográfica. | M | Medir y ensayar optimización en una operación posterior; no optimizar ahora. | PENDIENTE |

## 5. Observaciones del usuario incorporadas

La primera ronda de observaciones personales está incorporada como `REV-013`–`REV-025`, con `Origen: Observación del usuario`. Incluye los defectos visuales documentados mediante capturas y las dudas editoriales sobre apertura, arquitectura, glosario y recursos gráficos.

Que una observación proceda del usuario no la convierte automáticamente en una decisión de implementación. Todas conservan `PENDIENTE`. Las observaciones futuras comenzarán en `REV-027`, sin renumerar ni reutilizar IDs.

## 6. Decisiones del usuario

| ID | Decisión del usuario | Notas de decisión |
|---|---|---|
| REV-001 | PENDIENTE | — |
| REV-002 | PENDIENTE | — |
| REV-003 | PENDIENTE | — |
| REV-004 | PENDIENTE | — |
| REV-005 | PENDIENTE | — |
| REV-006 | PENDIENTE | — |
| REV-007 | PENDIENTE | — |
| REV-008 | PENDIENTE | — |
| REV-009 | PENDIENTE | — |
| REV-010 | PENDIENTE | — |
| REV-011 | PENDIENTE | — |
| REV-012 | PENDIENTE | — |
| REV-013 | PENDIENTE | — |
| REV-014 | PENDIENTE | — |
| REV-015 | PENDIENTE | — |
| REV-016 | PENDIENTE | — |
| REV-017 | PENDIENTE | — |
| REV-018 | PENDIENTE | — |
| REV-019 | PENDIENTE | — |
| REV-020 | PENDIENTE | — |
| REV-021 | PENDIENTE | — |
| REV-022 | PENDIENTE | — |
| REV-023 | PENDIENTE | — |
| REV-024 | PENDIENTE | — |
| REV-025 | PENDIENTE | — |
| REV-026 | PENDIENTE | — |

No se asignarán `APROBADA`, `RECHAZADA`, `DIFERIDA`, `INCLUIR` o `NO INCORPORAR` sin una decisión explícita posterior.

## 7. Paquetes de decisión consolidados

### A. Identidad y apertura del libro

`REV-001`, `REV-005`, `REV-007`, `REV-013`, `REV-014`, `REV-015`, `REV-022`.

Identidad, título y subtítulo, créditos, prólogo, introducción, orientación y posible colofón.

### B. Arquitectura del volumen

`REV-016`, `REV-017`.

Duplicación funcional facsímil/transcripción y orden estudio/documento.

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

Sidebar, cierres, TOC PDF, índices PDF y tamaño de salidas.

### G. Trabajo futuro

`REV-008`.

Etiquetado PDF y validación formal PDF/UA o PDF/A.

### H. Decisiones negativas sólidas

`REV-009`, `REV-010`, `REV-011`, `REV-012`.

`H` significa no recuperar soluciones antiguas de 0.6. No significa cerrar otras cuestiones nuevas: en particular, REV-010 no resuelve REV-016 y REV-011 no resuelve REV-023 o REV-025.

## 8. Cinco bloques que deben resolverse antes de 1.0

1. **Apertura e identidad editorial:** prólogo, introducción, portada/apertura, créditos, metadatos y cierre.
2. **Arquitectura de lectura:** orden estudio/documento y repetición facsímil/transcripción.
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

1. **Consolidación documental:** esta operación; fija REV-001–REV-026 sin modificar la candidata ni investigar.
2. **Decisiones editoriales puras:** prólogo, introducción, apertura, orden general, duplicación de imágenes, estructura de preliminares, cierres y navegación HTML.
3. **Tres auditorías especializadas:**
   - glosario / Estudio Histórico / necesidad real de investigación;
   - gráficos, recuadros y cartografía: 0.6 + Plan 0.5 + candidata;
   - fuentes, bibliografía y aparatos narrativos.
4. **Decisión definitiva:** clasificar cada cuestión como 1.0, 1.1+, no incorporar o investigación previa.
5. **Implementación:** plan de cambios, operaciones canónicas cuando procedan, cambios Quarto, nueva candidata, validación, preview, aceptación humana y, solo después, 6B.

Esta operación ejecuta únicamente el paso 1.

## 11. Lista propuesta para 1.0

La propuesta actual es resolver los cinco bloques del apartado 8 antes de decidir la publicación. `Resolver` puede significar elegir una opción, completar una auditoría previa, aprobar una corrección o decidir justificadamente no implementar una solución concreta. No significa que las dieciséis entradas B estén ya aprobadas como cambios.

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

La candidata no debe modificarse todavía. El siguiente trabajo consiste en resolver con el usuario las decisiones editoriales de arquitectura y apertura; solo después se ejecutarán las tres auditorías especializadas y se adoptarán decisiones definitivas de alcance 1.0.

**SIGUIENTE PASO: decisiones editoriales de arquitectura y apertura de la candidata 1.0.**

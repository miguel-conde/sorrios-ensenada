# Revisión editorial de la candidata 1.0

**Fecha:** 9 de octubre de 2026<br>
**Fase:** 6A.1<br>
**Estado:** propuestas pendientes de decisión humana<br>
**Informe de evidencia:** [INFORME_COMPARATIVO_PDF_0_6_Y_QUARTO.md](./INFORME_COMPARATIVO_PDF_0_6_Y_QUARTO.md)

## 1. Objeto

Este documento convierte la comparación integral entre la composición 0.6 y la candidata Quarto en una matriz estable de observaciones `REV-*`. No modifica la candidata, no decide qué entra definitivamente en 1.0 y no autoriza publicación, despliegue ni Fase 6B.

La composición 0.6 es referencia editorial, no autoridad histórica o textual. Que un elemento aparezca en 0.6 no basta para recuperarlo.

## 2. Baseline auditada

| Elemento | Valor |
|---|---|
| Rama | `feature/quarto-book` |
| Baseline de auditoría | `088e4fcec91fa9723b5b0ffad4f65781a9c0af6c` |
| Commit de candidata | `49ab2e1b1a58ca9201efab54b42a3125de7326f8` |
| Upstream al inicio | `e74ce3cb8bd27921f50db5a046a0851528297ced` |
| Upstream final antes del commit | `088e4fcec91fa9723b5b0ffad4f65781a9c0af6c` (coincide con la baseline) |
| `main` / `origin/main` | `e81dc9239ac8dbabfe77168a50ef98c4d3b79170` |
| Árbol `project/` | `e32917763475ceebdfe7b54830e1fb43f6419dad` |
| Árbol `publication/` | `cfcf349928fe3e1f2d3b33c005c31fa5621b1878` |
| PDF 0.6 | 259 páginas; 6.806.113 bytes; SHA-256 `78551fc2bcc067634b97e6284b5a3b88b1916067851d51ee00b14e488e4187f4` |
| PDF Quarto | 334 páginas; 73.994.496 bytes; SHA-256 `f1eee2f465f554d3bf2b506d23a622967d1b4f1013ac657a774868e525688183` |

La candidata técnica y las fuentes canónicas se mantuvieron en solo lectura durante la auditoría.

## 3. Criterios B/M/F/N

### B — Bloqueante para 1.0

Problema que debería resolverse antes de publicar la primera edición: error, omisión significativa, pérdida accidental, contradicción, cobertura prometida y ausente, trazabilidad relevante insuficiente o defecto editorial serio.

### M — Mejora conveniente

Mejora real que podría incorporarse a 1.0 si su coste y riesgo son razonables, pero cuya ausencia no invalida la edición.

### F — Futura

Mejora o ampliación apropiada para 1.1 o posterior.

### N — No incorporar

Diferencia respecto a 0.6 superada, errónea, más débil, sustituida por una solución mejor o incompatible con la arquitectura vigente.

Estas letras son una **clasificación propuesta**, no una decisión editorial. Todas las filas conservan `Decisión del usuario: PENDIENTE`.

## 4. Matriz REV-*

| ID | Origen | Área | Observación | Evidencia 0.6 | Estado Quarto | Evaluación | Clasificación propuesta | Acción propuesta | Decisión del usuario |
|---|---|---|---|---|---|---|---|---|---|
| REV-001 | Auditoría actual | Metadatos, créditos y portada | La candidata mantiene `0.1.0-dev`, `development`, «Edición en desarrollo», autor PDF vacío y carece de responsabilidad editorial, licencia, copyright, fecha editorial y URL canónica. | 0.6 identifica proyecto, versión y año, aunque tampoco fija autoría personal, licencia o copyright. | El informe de candidata reconoce expresamente las decisiones pendientes. | No debe publicarse como 1.0 con identidad de desarrollo ni con responsabilidades esenciales sin decidir. | B | Obtener decisiones humanas; después actualizar portada, créditos y metadatos mediante una operación separada. No inventar valores. | PENDIENTE |
| REV-002 | Comparación 0.6 | Cartografía | No existe equivalente de las dos láminas de orientación regional/provincial y local. | Págs. 16–17: tres escalas, topónimos útiles y cautelas sobre límites históricos/localizadores. | No hay mapas ni assets cartográficos; la prosa solo advierte contra una precisión indebida. | Regresión real y componente prometido por el Plan Maestro. | B | Diseñar o readaptar cartografía con procedencia, licencia, fecha, leyenda, cautelas y texto alternativo verificados. | PENDIENTE |
| REV-003 | Comparación 0.6 | Fuentes externas y bibliografía | El sistema público de referencias es incompleto; el caso del topónimo pierde proximidad entre afirmación y fuente. | Pág. 15 y apéndice F: referencias identificables y enlaces visibles; 42 URL únicas. | 41 URL únicas y fuentes en matriz, transcripción, glosario e índices; `references.bib` vacío, sin citas en capítulos y sin aparato bibliográfico. | La evidencia existe, pero su verificabilidad para el lector depende de búsquedas y conocimiento de la matriz. | B | Definir un sistema de referencias visible; cubrir al menos topónimo, contextos E y fuentes generales sin confundir front matter con bibliografía. | PENDIENTE |
| REV-004 | Comparación 0.6 | Aparatos narrativos | Faltan cuestiones abiertas, historia de versiones y modelos de cita como piezas del libro. | Apéndices E, G y H presentes; 0.6 también ofrece un apéndice F de fuentes. | Los límites aparecen dispersos en capítulos y matriz; la historia está en documentos técnicos externos; no hay modelos de cita. | Cobertura prometida por el Plan Maestro y no plenamente sustituida. El alcance exacto requiere juicio editorial. | B | Decidir y redactar las piezas mínimas para 1.0 desde fuentes vigentes; no copiar mecánicamente 0.6. | PENDIENTE |
| REV-005 | Auditoría actual | Preliminares | Presentación, nota al lector, guía de uso, convenciones y cronología no existen como preliminares consolidados. | 0.6 ofrece créditos, guía D/C/I/E/L, índice y nota de composición, pero tampoco resuelve toda la lista del Plan. | Capítulos 1–4 y las introducciones de capítulos/aparatos cubren parte de esas funciones de forma dispersa. | No todo requiere una pieza separada; una orientación inicial breve mejoraría la entrada al volumen. | M | Decidir qué funciones deben reunirse antes del capítulo 1 y cuáles quedan mejor cubiertas en su ubicación actual. | PENDIENTE |
| REV-006 | Auditoría actual | D/C/I/E/L y navegación | Las marcas del cuerpo son texto plano y su presencia visible se concentra en capítulos 9–13. | 95 grupos visibles; resolución manual en el apéndice D. | 77 grupos; matriz de 112 entradas con anclas y enlaces de retorno, pero sin enlace directo desde cada marca; capítulos 3 y 5–8 solo declaran evidencia en YAML. | La cadena funciona mediante búsqueda y concordancia, pero no con la fluidez que permite la arquitectura actual. | M | Enlazar marcas a entradas cuando sea viable y decidir una política visible coherente para capítulos 3 y 5–8, sin saturar la prosa. | PENDIENTE |
| REV-007 | Comparación 0.6 | Cierre editorial | El volumen termina en el índice de materias sin colofón o declaración final de edición. | Pág. 259: colofón provisional con base, finalidad y fecha. | El informe técnico de candidata queda fuera del libro. | No es una pérdida histórica ni un bloqueo técnico, pero un cierre breve puede fijar edición, snapshot y forma de cita. | M | Valorar un colofón mínimo coordinado con REV-001 y REV-004. | PENDIENTE |
| REV-008 | Auditoría actual | Accesibilidad formal | El PDF no está etiquetado y no existe validación PDF/UA o PDF/A. | 0.6 tampoco está etiquetado. | Accesibilidad básica HTML/PDF validada; 53 imágenes con alternativa en HTML; no se declara conformidad formal. | No es regresión ni bloqueante conocido; requiere herramientas y alcance específicos. | F | Mantener la limitación declarada y estudiar PDF etiquetado/UA en 1.1 o posterior. | PENDIENTE |
| REV-009 | Comparación 0.6 | Contenido histórico superado | 0.6 contiene formulaciones demasiado fuertes sobre bienes comunales, autoconsumo, clima, copropiedad, ruedas fijas, habitantes fiscales y amortiguadores. | Expresiones localizadas en la Parte II y en análisis incorporados. | Quarto las elimina o reformula con límites, denominadores y distinciones de autoridad. | Recuperarlas sería una regresión metodológica e histórica. | N | Conservar las formulaciones actuales; usar 0.6 solo como prueba negativa de regresión. | PENDIENTE |
| REV-010 | Comparación 0.6 | Facsímil | 0.6 presenta el facsímil solo como 35 unidades, con recortes grandes. | Págs. 64–98: 35 imágenes de unidad. | Quarto presenta 18 páginas completas y vuelve a mostrar los 35 recortes junto a la transcripción. | La candidata resuelve mejor materialidad y lectura; no existe pérdida funcional. | N | No restaurar un segundo facsímil exclusivo por unidades ni duplicar imágenes adicionales. | PENDIENTE |
| REV-011 | Comparación 0.6 | Índices | Los índices 6–9 de 0.6 son provisionales y carecen de páginas finales. | 129 entradas contadas; localizadores por capítulo/respuesta y promesa de páginas en 0.8. | 164 entradas; nueve índices enlazados y páginas PDF calculadas automáticamente. | Quarto sustituye el sistema por uno más amplio, preciso y reproducible. | N | Mantener los índices generados; no recuperar listas o páginas manuales de 0.6. | PENDIENTE |
| REV-012 | Comparación 0.6 | Formato y diseño | 0.6 usa A4, color y una maqueta más ornamental; Quarto usa Letter y diseño sobrio. | Portada, encabezados, color y aperturas de apéndice más elaborados. | Composición legible y validada, con mejor equivalencia HTML/PDF; portada aún provisional por REV-001. | La preferencia estética o el tamaño de página no prueban una regresión. | N | No imitar paginación ni maqueta 0.6; resolver solo la terminación necesaria dentro del sistema Quarto. | PENDIENTE |

## 5. Observaciones del usuario pendientes de incorporar

No se encontró un documento versionado ni contexto explícito que contenga observaciones editoriales personales del usuario para esta candidata.

Esta sección queda abierta. Las observaciones futuras se incorporarán con `Origen: observación del usuario` y con nuevos IDs a partir de `REV-013`, sin renumerar ni alterar de forma destructiva las entradas existentes.

## 6. Decisiones del usuario

Todas las decisiones están pendientes. La clasificación propuesta no autoriza correcciones.

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

Valores futuros permitidos en esta tabla tras decisión explícita: `APROBADA`, `RECHAZADA` o `DIFERIDA`, acompañados de una nota. En 6A.1 no se asigna ninguno.

## 7. Lista propuesta para 1.0

Propuesta, no decisión aprobada:

1. `REV-001`: cerrar identidad editorial, créditos y metadatos de edición.
2. `REV-002`: incorporar cartografía de orientación debidamente documentada.
3. `REV-003`: implantar un sistema público de fuentes y bibliografía.
4. `REV-004`: resolver cuestiones abiertas, historia de versiones y modelos de cita.

Las mejoras `REV-005`–`REV-007` podrían entrar en 1.0 si el usuario las aprueba y el coste/riesgo resulta razonable. `REV-009`–`REV-012` son propuestas de no recuperación, no tareas de implementación.

## 8. Backlog propuesto 1.1+

Propuesta, no decisión aprobada:

- `REV-008`: estudiar etiquetado PDF y validación formal PDF/UA o PDF/A.
- Cualquier ampliación histórica o nueva investigación que surja al resolver fuentes debe abrirse fuera de 6A.1 y respetar las autoridades canónicas.

## 9. Resumen de clasificación

| Clasificación propuesta | Número |
|---|---:|
| B | 4 |
| M | 3 |
| F | 1 |
| N | 4 |
| **Total** | **12** |

| Origen | Número |
|---|---:|
| Comparación 0.6 | 8 |
| Auditoría actual | 4 |
| Observación del usuario | 0 |

## 10. Puerta editorial

No debe modificarse la candidata hasta que el usuario revise la matriz y decida cada entrada necesaria para 1.0. Cualquier implementación posterior será una operación separada, con alcance, autoridad y validación propios.

**SIGUIENTE PASO: revisión y decisión humana de las entradas REV-* antes de modificar la candidata 1.0.**

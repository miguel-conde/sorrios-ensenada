# Plan maestro de publicación Quarto

**Proyecto:** Sorribos y Santibáñez de Ordás en 1752  
**Estado:** decisiones de las fases 0 y 1 consolidadas  
**Fecha de consolidación:** 28 de septiembre de 2026  
**Snapshot canónico auditado:** `main@6b49be848c92c4772b37c46495135352821d50f8`  
**Documento de estado:** `docs/ESTADO_PUBLICACION_QUARTO.md`

## 1. Objetivo y alcance

Quarto será el sistema de composición y publicación de un único libro con salida HTML y PDF descargable. `project/` seguirá siendo el sistema canónico de investigación y edición. La capa `publication/` seleccionará, explicará, enlazará y transformará esas fuentes sin reemplazarlas.

El libro conservará la cobertura intelectual del volumen completo 0.6 y del índice rector 1.5, pero no su paginación ni su maqueta. La Parte II se refundirá de nuevo bajo control D/C/I/E/L; el facsímil, la transcripción, la edición modernizada y los aparatos derivados se generarán desde las fuentes vigentes.

No son objetivos de la primera fase técnica:

- copiar o reproducir página a página el PDF 0.6;
- añadir nueva investigación histórica;
- cambiar la Edición Crítica, el Manual, el Estudio Histórico o el Registro;
- publicar automáticamente cada cambio de `main`;
- subir el PDF manuscrito o el PDF 0.6 al repositorio.

## 2. Línea base auditada

La Fase 0 comprobó que el PDF completo 0.6 y `main` usaban el mismo commit, `6b49be848c92c4772b37c46495135352821d50f8`. En la fecha de esta consolidación `main` seguía en ese SHA, `operation.status` era `clean` y no había divergencia textual que reconciliar antes de diseñar Quarto.

Versiones vigentes comprobadas:

| Fuente | Versión | Ruta o ubicación |
|---|---:|---|
| Manual Editorial | 1.6 | `project/00_CONTROL/Manual_Editorial.md` |
| Edición Crítica | 3.6 | `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md` |
| Estudio Histórico | 1.2 | `project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md` |
| Registro de afirmaciones y cálculos | 1.2 | `project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md` |
| Introducción | 1.3 | `project/30_RESULTADOS/EDICION_DIVULGATIVA/Introduccion_Catastro_Ensenada_Sorrios.md` |
| Edición modernizada | 1.3 | `project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md` |
| Índice rector | 1.5 | `project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md` |
| Plan de composición | 0.5 | `project/30_RESULTADOS/EDICION_DIVULGATIVA/Plan_Composicion_Volumen_0_5.md` |
| Plugin y skill | 2.0.2 | `project/00_CONTROL/proyecto.yaml` |

El manuscrito autoritativo sigue en Google Drive, en modo de solo lectura: 18 páginas, 5.038.575 bytes, SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`. Estos datos se leen siempre de `proyecto.yaml`; no autorizan una copia del PDF en GitHub.

La documentación de arquitectura previa queda vigente: GitHub es el workspace canónico, Drive conserva únicamente el manuscrito y las operaciones multiarchivo son atómicas y condicionadas por `base_sha`.

## 3. Arquitectura y jerarquía de autoridad

```text
Google Drive
PDF manuscrito autoritativo
          │
          ▼
GitHub / project/
Edición Crítica + Manual + controles
Estudio Histórico + Registro D/C/I/E/L
edición modernizada + glosario + índices
análisis auxiliares
          │
          ├───────────────┐
          ▼               ▼
publication/content/   publication/generated/
texto editorial        derivados reproducibles
          │               │
          └───────┬───────┘
                  ▼
                Quarto
             ┌────┴────┐
             ▼         ▼
           HTML       PDF
```

Jerarquía operativa:

| Nivel | Autoridad | Ejemplos | Edición desde `publication/` |
|---|---|---|---:|
| A | fuente primaria | PDF manuscrito de Drive | no |
| B | autoridad editorial | Manual y Edición Crítica 3.6 | no |
| C | resultados canónicos | Estudio 1.2, Registro 1.2, modernizada 1.3, glosario, índices | no |
| D | análisis auxiliares | análisis cuantitativo, reconstrucción, matriz, vulnerabilidades, síntesis | no |
| E | texto editorial del libro | capítulos de `publication/content/` | sí |
| F | derivados de publicación | `generated/`, HTML, PDF, recortes | nunca manualmente |

El PDF 0.6 es testimonio de la edición compuesta alcanzada: ayuda a decidir qué conservar, actualizar, ampliar, adaptar o retirar. No gana autoridad sobre A–D.

## 4. Frontera `project/` / `publication/`

`project/` conserva hechos, lecturas, método, estados, resultados y trazabilidad canónica. `publication/` conserva decisiones propias del libro: estructura narrativa, selección, orden, enlaces, metadatos de capítulo, presentación y generación.

Si durante la redacción se descubre un posible error factual:

1. no se corrige silenciosamente en el capítulo;
2. se identifica la autoridad afectada;
3. se abre una operación canónica separada conforme a `PROJECT.md`;
4. se valida y publica la corrección en la fuente;
5. se actualiza o regenera la publicación.

Un cambio de estilo o navegación sí se resuelve directamente en `publication/`.

## 5. Frontera `content/` / `generated/`

`content/` contiene obra editorial que exige juicio humano. Se revisa y versiona. Incluye preliminares, capítulos 1–13 y los aparatos narrativos de fuentes, cuestiones abiertas, historia de versiones y modelos de cita.

`generated/` contiene material reconstruible desde fuentes y metadatos declarados. Puede eliminarse por completo antes de cada preparación. Incluye los capítulos 14–16, glosario, cuadros, concordancia, matriz de evidencia y nueve índices.

Regla decisoria:

- selección, argumentación o explicación para el lector → `content/`;
- transformación determinista de una fuente → `generated/`;
- corrección factual o paleográfica → primero la fuente en `project/`;
- salida de Quarto → `_book/`, nunca fuente.

## 6. Estructura prevista de `publication/`

```text
publication/
├── _quarto.yml
├── index.qmd
├── README.md
├── references.bib
├── meta/
│   ├── publication.yml
│   ├── chapters.yml
│   ├── indexes.yml
│   └── assets.yml
├── content/
│   ├── 00-preliminares/
│   ├── 01-catastro/
│   ├── 02-estudio/
│   └── 06-aparatos/
├── generated/
│   ├── 14-facsimil.qmd
│   ├── 15-transcripcion.qmd
│   ├── 16-edicion-modernizada.qmd
│   ├── glosario.qmd
│   ├── cuadros-cuantitativos.qmd
│   ├── concordancia.qmd
│   ├── matriz-evidencia.qmd
│   └── indices/
├── assets/
│   ├── facsimile/pages/
│   ├── maps/
│   ├── figures/
│   └── cover/
├── scripts/
│   ├── prepare.py
│   ├── check_sources.py
│   ├── build_facsimile.py
│   ├── build_transcription.py
│   ├── build_modernized.py
│   ├── build_apparatus.py
│   ├── build_indexes.py
│   └── validate_publication.py
└── styles/
    ├── book.scss
    ├── book.css
    └── latex/preamble.tex
```

Esta es la estructura objetivo, no una orden de crear todos los archivos vacíos en el primer commit. Los componentes se incorporan cuando una fase los necesita. No se crearán filtros Lua sin un caso concreto.

## 7. Índice Quarto v0.1

La decisión vigente conserva 16 capítulos y separa de nuevo facsímil y transcripción; esta decisión de Fase 1 sustituye la fusión explorada durante la Fase 0.

### Preliminares

Portada, créditos, presentación, nota al lector, guía de uso, convenciones, guía D/C/I/E/L, cronología, cartografía, índice general, reproducciones y cuadros.

### Parte I. El Catastro y su documento

1. El Catastro de Ensenada.
2. Las Respuestas Generales y el interrogatorio de cuarenta preguntas.
3. El expediente de Sorribos y Santibáñez de Ordás.
4. Del manuscrito al volumen actual.

### Parte II. Sorribos y Santibáñez en 1752

5. Un lugar de señorío en el Concejo de Ordás.
6. Vecinos, hogares, viviendas y trabajo.
7. La tierra y el sistema agrario.
8. Ganadería, montes y aprovechamientos comunales.
9. Río, molinos y otros recursos productivos.
10. Iglesia, señorío y fiscalidad.
11. Hacienda concejil y servicios colectivos.
12. Dinero, oficios y conexiones exteriores.
13. Una economía rural integrada: vulnerabilidades, resiliencia y límites.

### Parte III. El manuscrito original

14. Facsímil íntegro del expediente: las 18 páginas completas.

### Parte IV. Transcripción y aparato crítico

15. Las 35 unidades, cada una con ancla propia, recorte y las seis secciones canónicas.

### Parte V. El Catastro en español actual

16. Portada, comparecencia, preguntas y respuestas 1–40, ratificación, edades, firmas, concordancia y notas.

### Parte VI. Aparatos e índices

Glosario, cuadros cuantitativos, concordancia, matriz D/C/I/E/L, cuestiones abiertas, fuentes, versiones, modelos de cita y nueve índices.

## 8. Matriz de procedencia

| Destino | Tipo | Autoridad o base principal | Regla |
|---|---|---|---|
| Presentación y guía | editorial | plan maestro e índice 1.5 | escribir en `content/` |
| Capítulos 1–2 | editorial adaptado | Introducción 1.3, Manual, Estudio 1.2 | no duplicar las 40 preguntas fuera de su función explicativa |
| Capítulo 3 | editorial adaptado | Introducción, Estudio, Registro | conservar serie `Sorribios` → `Sorribos` → `Sorrios` |
| Capítulo 4 | editorial adaptado | Manual, Edición Crítica, controles | explicar método sin sustituir el Manual |
| Capítulos 5–13 | refundición editorial | Estudio 1.2 + Registro 1.2 + análisis 0.2–0.6 + referencia 0.6 | revisión humana; metadatos `sources` y `evidence` |
| Capítulo 14 | generado | PDF autoritativo + `unidades.yaml` | 18 páginas completas; no usar el PDF 0.6 |
| Capítulo 15 | generado | Edición Crítica 3.6 + `unidades.yaml` | 35 unidades, seis secciones cada una |
| Capítulo 16 | generado/adaptado | edición modernizada 1.3 + preguntas verificadas | 40 respuestas y anclas estables |
| Glosario | generado | `Glosario.md` | enlaces y retornos sin cambiar definiciones canónicas |
| Cuadros | generado | Registro + Estudio | mostrar denominador y regla de cálculo |
| Concordancia | generado | unidades + edición + modernizada | una fuente estructurada, varias vistas |
| Matriz de evidencia | generado | Registro 1.2 | conservar estado y cautela |
| Cuestiones abiertas | mixto | entradas LIM + decisiones editoriales | no cerrar lagunas por analogía |
| Índices 1–5 | generado | índices canónicos vivos | adaptar nomenclatura y localizadores |
| Índices 6–7 | generado | `meta/indexes.yml` + contenido | entradas editoriales revisables |
| Índice 8 | generado | preguntas y respuestas 1–40 | automático |
| Índice 9 | generado | `meta/indexes.yml` + contenido | índice real con subentradas y remisiones |

## 9. D/C/I/E/L

- **D — dato:** contenido explícito de la Edición Crítica 3.6.
- **C — cálculo:** operación reproducible con datos registrados; debe declarar operandos, denominador y regla.
- **I — interpretación:** lectura histórica compatible con los datos, nunca presentada como literal del manuscrito.
- **E — contexto externo:** fuente identificada para situar institución, término, antecedente o continuidad; no crea cifras ni rasgos locales.
- **L — límite:** ausencia, discrepancia, cautela o imposibilidad de cálculo que debe permanecer visible.

La prosa no tiene que mostrar una letra en cada párrafo. La trazabilidad se conserva mediante metadatos, notas, cuadros y la matriz final. Los scripts comprobarán que los identificadores citados existen; no decidirán si una interpretación es históricamente correcta.

## 10. Auditoría de la composición 0.6

El PDF 0.6 tiene 259 páginas: preliminares 1–8, Parte I 9–19, Parte II 20–61, facsímil 62–98, transcripción 99–166, modernizada 167–213, aparatos 214–236, índices 237–258 y colofón 259. Contiene una refundición valiosa de los análisis, pero no se trasladará sin revisión.

Problemas que deben convertirse en pruebas editoriales de regresión:

| Problema detectado | Riesgo | Regla para Quarto |
|---|---|---|
| «bienes comunales» | atribuir un título no acreditado | usar espacios o aprovechamientos de uso común documentado, salvo prueba expresa |
| «fuerte base de autoconsumo» | inferir destino predominante de la producción | declarar que la fuente no permite repartir consumo, semilla, cargas, venta y otros destinos |
| `CLIMA` como nodo causal | presentar un régimen no documentado | retirarlo del modelo documental; solo reaparece en estudio ambiental externo separado |
| copropiedad como amortiguador | convertir titularidad en efecto causal | describir pluralidad de titulares o derechos compartidos |
| «ocho ruedas fijas» | añadir un término no documental y confundir el molino venturero | usar la fórmula canónica de ocho ruedas en cuatro casas y número desconocido en el venturero |
| puentes dañados → paralización molinera | fundir hechos e hipótesis causal | separar hechos, inferencia y escenario |
| «26 habitantes fiscales» en `CAL-019` | sugerir población individual | usar `avitadores`; auditar el Registro antes de reutilizar la etiqueta |

`validate_publication.py` señalará estas expresiones o combinaciones para revisión contextual. No hará sustituciones automáticas. Cualquier cambio a `CAL-019` se hará primero en el Registro mediante otra operación.

## 11. Facsímil

El capítulo 14 conservará las 18 páginas completas, incluidos márgenes, blancos, sellos, reclamos y materialidad. En HTML se prevé ampliación; en PDF, reproducción legible.

El PDF fuente permanece en Drive. La estrategia preferida para builds reproducibles es versionar, tras medir tamaño y decidir Git o LFS, solo 18 imágenes completas optimizadas con procedencia en `meta/assets.yml`. Son derivados de publicación, no autoridad. Los 35 recortes se producen en cada preparación desde esas imágenes y `unidades.yaml`; no se versionan por duplicado.

Antes de adoptar esta estrategia se comprobarán tamaño, calidad, licencia/atribución y equivalencia con el hash del PDF fuente. Hasta entonces no se incorpora ningún derivado.

## 12. Transcripción y edición modernizada

`generated/15-transcripcion.qmd` será una sola página Quarto con 35 secciones y anclas estables. Cada sección conserva Imagen, Transcripción paleográfica, Observaciones editoriales, Notas paleográficas, Notas históricas y Referencias cruzadas. La lógica `left/right/complete` procede de `unidades.yaml` y reutiliza `render_unit.py`.

`generated/16-edicion-modernizada.qmd` será una sola página con anclas para comparecencia y respuestas 1–40. La modernización facilita lectura, pero no sustituye facsímil ni paleografía. Las preguntas completas viven con cada respuesta; el capítulo 2 explica el formulario sin duplicarlo como segunda fuente.

## 13. Índices y aparatos

El libro tendrá nueve índices: onomástico; lugares y topónimos; instituciones, jurisdicciones y entidades; oficios, cargos y condiciones; medidas, monedas y unidades; productos, cultivos, ganados y recursos; cargas, derechos, rentas y fiscalidad; preguntas y respuestas; materias.

Los cinco primeros parten de índices vivos. Los índices 6, 7 y 9 usan entradas editoriales de `meta/indexes.yml`; el 8 se deriva de las 40 respuestas. En HTML los localizadores son enlaces y anclas; en PDF deben resolverse como localizadores de página después de estabilizar la composición. Nunca se mantienen dos listas manuales divergentes.

Los aparatos comparten la misma regla: una fuente estructurada, distintas vistas. Glosario, cálculos, concordancia y matriz se generan; fuentes, cuestiones abiertas, versiones y cita admiten redacción editorial donde sea necesaria.

## 14. Generación prevista

```text
check_sources.py
  ├── comprueba rutas, versiones, hash declarado, 35 unidades y 40 respuestas
  └── valida identificadores y metadatos
          ↓
prepare.py
  ├── build_facsimile.py
  ├── build_transcription.py
  ├── build_modernized.py
  ├── build_apparatus.py
  └── build_indexes.py
          ↓
generated/
          ↓
quarto render
          ↓
validate_publication.py
```

Los scripts serán deterministas, idempotentes, con mensajes de error accionables y sin escrituras en `project/`. `meta/publication.yml` congela la edición: versión, estado, commit base, rutas y versiones de fuentes y metadatos del manuscrito. `chapters.yml` fija orden y tratamiento; `indexes.yml`, entradas editoriales; `assets.yml`, procedencia y transformaciones.

### Perfil local de composición

La arquitectura editorial universal y la composición local son perfiles
complementarios. ChatGPT Web/Desktop puede reconstruir el estado desde GitHub y
leer el PDF de Drive sin requerir herramientas locales. El libro Quarto, en
cambio, se prepara en el checkout con `.venv` y una réplica persistente del
manuscrito situada fuera del worktree.

La réplica local no es estado canónico ni autoridad: debe coincidir con los
metadatos de `proyecto.yaml` y se rechaza si está dentro del checkout. El orden
de resolución es una ruta explícita en `SORRIOS_MANUSCRIPT_PDF`, la ubicación
XDG y `~/.local/share/sorrios-ensenada/manuscript.pdf`. No hay descarga
automática. Cuando la réplica falta o no coincide, el build se detiene y el
usuario decide cómo renovarla desde Drive.

Durante este perfil, Copilot lee las fuentes versionadas en el checkout y solo
usa el remoto Git para sincronización, comprobación de concurrencia y publicación.
El PDF 0.6 puede mantenerse fuera del worktree como referencia visual, pero no
participa en la generación ni adquiere autoridad textual.

## 15. Validación y criterios de aceptación

### Integridad editorial

- 16 capítulos en orden;
- 18 páginas facsimilares completas;
- 35 unidades y seis secciones por unidad;
- 40 preguntas y respuestas consecutivas;
- glosario, concordancia, matriz y nueve índices;
- identificadores de evidencia existentes y cautelas conservadas;
- ningún cambio silencioso en fuentes canónicas.

### Control textual y de regresión

- fórmulas problemáticas de 0.6 revisadas;
- `Sorribos`/`Sorrios` coherentes y `Sorribas` restringido al historial;
- cifras, medidas, nombres y localizadores contrastados;
- D/C/I/E/L distinguibles y entradas condicionadas con salvedad;
- ausencia de marcadores, rutas locales y mensajes de error.

### HTML

- navegación, búsqueda, anclas y enlaces internos;
- diseño adaptable, lightbox cuando se implemente y texto alternativo;
- equivalencia de contenido con PDF;
- PDF descargable únicamente cuando exista una salida validada.

### PDF

- render completo con LuaLaTeX o motor aprobado;
- texto seleccionable, fuentes y glifos correctos;
- tablas, notas, figuras y páginas críticas inspeccionadas visualmente;
- marcadores, enlaces, metadatos y paginación coherentes;
- no declarar PDF/A o PDF/UA sin validación específica.

### Repositorio

- tests existentes aplicables en PASS;
- `project/` intacto en tareas de publicación;
- ningún PDF incorporado al repositorio;
- `generated/` reproducible y `_book/` ignorado;
- un único commit atómico por operación multiarchivo.

En el bootstrap técnico, HTML debe renderizar. Para PDF se exige ejecutar `quarto check` y probar el render; si falta LaTeX, se registra con precisión la dependencia ausente y la fase no presume un PDF válido.

## 16. Publicación

La publicación tendrá puerta editorial. Un cambio de `main` no debe alterar
automáticamente la edición pública. La primera puesta en escena usará una
preview de rama con acceso controlado; Netlify y GitHub Pages siguen siendo
alternativas sujetas a decisión explícita. La automatización se implementará
solo después del prototipo vertical y de validar HTML/PDF.

Flujo objetivo:

```text
snapshot aprobado → generación → render HTML/PDF → validación
→ preview controlada → aceptación editorial → publicación 1.0
```

La edición 1.0 registrará commit de fuentes, versiones, hash del manuscrito, nombres, tamaños y hashes de salidas, informe de validación y etiqueta Git. Los derivados públicos no convierten el PDF manuscrito en archivo del repositorio.

## 17. Forma de trabajar con Copilot

Copilot debe recibir tareas pequeñas, con alcance de rutas, fuentes, criterios de aceptación y prohibiciones explícitas. Antes de editar lee instrucciones y roadmap; después informa de diff, comandos y resultados. No migra capítulos masivamente mientras el prototipo no esté aceptado.
En tareas Quarto trabaja localmente con `.venv`, la réplica verificada y los
archivos del checkout; no repite accesos a Drive o GitHub cuando las entradas
locales válidas ya están disponibles.

Secuencia normal:

1. confirmar rama, `base_sha`, estado limpio y siguiente tarea;
2. leer solo fuentes necesarias;
3. proponer o ejecutar un cambio acotado;
4. validar en el formato afectado;
5. comprobar que no cambió `project/`;
6. revisar diff y publicar un commit atómico;
7. actualizar el roadmap solo cuando una fase cumpla sus criterios.

## 18. Fases y documento operativo

- Fase 0 — auditoría del volumen 0.6: completada.
- Fase 1 — arquitectura editorial y técnica v0.1: completada.
- Fase 1B — documentación autosuficiente para Copilot: este conjunto documental.
- Fase 2A — bootstrap mínimo y primer render: siguiente tarea.
- Fase 2B — prototipo vertical real.
- Fase 3 — redacción controlada de capítulos 1–13.
- Fase 4 — generadores documentales y aparatos.
- Fase 5 — índices, calidad integral y accesibilidad.
- Fase 6 — preview y publicación 1.0.

El estado, las puertas y la siguiente tarea exacta se mantienen únicamente en `docs/ESTADO_PUBLICACION_QUARTO.md`. La creación inicial se especifica en `docs/ESPECIFICACION_BOOTSTRAP_PUBLICATION.md`.


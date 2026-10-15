# Plan de ejecución de la edición 1.0

**Fase de origen:** 6A.4<br>
**Fecha:** 10 de octubre de 2026<br>
**Contrato de alcance:** [ALCANCE_APROBADO_V1_0.md](./ALCANCE_APROBADO_V1_0.md)<br>
**Estado:** plan operativo; PKG-00–05 y PKG-08 completados e integrados;
CR-V1-001 e INC-BIB-001/002 cerradas; GATE-01 en PASS y GATE-02 pendiente

## 1. Reglas generales

- Este plan ejecuta el alcance aprobado; no lo amplía.
- Cada paquete parte de un `base_sha`, comprueba rama/upstream y termina con
  árbol limpio.
- No se autorizan escrituras simultáneas conflictivas en un mismo worktree.
- En ejecución secuencial, cada paquete lógico produce su propio commit.
- En ejecución paralela futura, cada paquete usa rama/worktree separado y una
  integración explícita.
- Los cambios canónicos y los cambios de publicación nunca se mezclan.
- No se hace push salvo orden del usuario.
- No se crea tag antes de PKG-13.
- Una necesidad fuera de alcance requiere una CR aprobada conforme a
  `CR-V1-*`.

## 2. Paquetes de ejecución

### PKG-00 — Inputs editoriales del usuario

**Objetivo:** obtener los datos humanos y textos que bloquean la edición.

**Estado:** **CERRADO CON DIFERIMIENTOS CONTROLADOS**. Las decisiones humanas
están normalizadas en
[CIERRE_PKG_00_INPUTS_EDITORIALES.md](./CIERRE_PKG_00_INPUTS_EDITORIALES.md).

Incluye:

- DAT-001 nombre de autor;
- DAT-002 roles editoriales;
- DAT-003 responsabilidad de transcripción;
- DAT-004 responsabilidad de modernización;
- DAT-005 colaboradores;
- DAT-006 identidad visible del proyecto;
- DAT-007 titular de copyright;
- DAT-008 licencia;
- prólogo personal firmado de 900–1.500 palabras.

DAT-001–DAT-008 y DAT-AI-01 están resueltos. DAT-009 tiene resuelto el modelo
de fecha, con su valor final diferido hasta la publicación; DAT-010 está
diferido hasta PKG-12/PKG-13. El prólogo es obligatorio y su texto definitivo
permanece diferido. También permanecen controlados los agradecimientos
eventuales, la nota final de derechos por componentes y los asuntos
`LEGAL-PENDIENTE` relativos a materiales externos.

**Autoridad:** usuario.<br>
**Escritura:** no modifica `project/`; no inventa datos.<br>
**Salida:** dossier de inputs aprobado; autoría, roles, identidad, copyright y
licencia del contenido original cerrados; prólogo definitivo diferido.

### PKG-01 — Glosario canónico GH-B

**Objetivo:** ejecutar una operación canónica separada.

**Estado:** **COMPLETADO E INTEGRADO** en el commit canónico
`9ae4d1fd46d9f2d7bca685de861bff2a554a7a39`. El cierre se documenta en
[CIERRE_PKG_01_GLOSARIO_CANONICO.md](./CIERRE_PKG_01_GLOSARIO_CANONICO.md).

Debe:

- mejorar `Señorío`, `medio vecino`, `propios`, `arbitrio`, `boto`, `vecera` e
  `hijo de familia` con conocimiento existente;
- incorporar `avitadores`, `utilidad`, `repartimiento` y `quartal`;
- auditar `establecimiento del suelo` y `arenta` durante la operación e
  incorporarlas solo si cumplen los cuatro criterios aprobados;
- no investigar G3;
- mantener cautelas y la separación entre dato local, contexto e inferencia;
- seguir el flujo canónico de la skill del Catastro.

**Autoridad afectada:** `project/`.<br>
**Salida:** fuentes canónicas validadas; siete G1 mejoradas y seis voces nuevas
incorporadas —`avitadores`, `utilidad`, `repartimiento`, `quartal`,
`establecimiento del suelo` y `arenta`—. No se investigó G3. CR-V1-001 completó
la sincronización técnica con la publicación; la presentación editorial final y
la regeneración de la candidata permanecen pendientes.<br>
**Prohibición:** no editar directamente `publication/generated/`; la
regeneración corresponde a PKG-10.

### PKG-02 — EXT-A verificación bibliográfica

**Objetivo:** verificar las 16 referencias parciales o mínimas.

**Estado:** **COMPLETADO E INTEGRADO; INCIDENCIAS CANÓNICAS CERRADAS;
PROPAGACIÓN PKG-08 COMPLETADA**. Las 16/16
referencias fueron tratadas en
[VERIFICACION_BIBLIOGRAFICA_PKG_02_V1_0.md](./VERIFICACION_BIBLIOGRAFICA_PKG_02_V1_0.md)
y el cierre/triage consta en
[CIERRE_PKG_02_VERIFICACION_BIBLIOGRAFICA.md](./CIERRE_PKG_02_VERIFICACION_BIBLIOGRAFICA.md).
`INC-BIB-001` y `INC-BIB-002` fueron cerradas mediante el commit canónico
`a162fad1792aa9b3804a5499d348ab355e5ce574`; la revisión e integración constan
en [CIERRE_RESOLUCION_CANONICA_INC_BIB_001_002.md](./CIERRE_RESOLUCION_CANONICA_INC_BIB_001_002.md).

Es **verificación bibliográfica**, no investigación histórica. Debe comprobar:

- autor o responsable;
- título;
- entidad o editor;
- fecha y edición;
- identificadores;
- URL estable;
- correspondencia entre fuente y uso.

Si aparece una contradicción sustantiva con una afirmación E, se detiene esa
incidencia. No se modifica silenciosamente `project/`.

**Salida:** dossier de verificación, procedencia de cada dato, incidencias y
registros preparados para `references.bib`. Resultado: catorce verificadas con
ajustes, una verificación parcial y una incompatibilidad de uso; S1 = 13,
S2 = 1, S3 = 1 y S4 = 1. La correspondencia canónica fuente/uso de las dos
incidencias está cerrada y su propagación editorial y bibliográfica quedó
integrada mediante PKG-08.

### PKG-03 — EXT-B cartografía

**Objetivo:** producir un mapa regional y un mapa local de orientación
contemporánea/editorial.

Debe resolver base, procedencia, licencia, atribución, escala, norte, leyenda,
fecha, accesibilidad, texto alternativo, redistribución y reproducibilidad.

**Prohibido:** reconstruir límites, caminos, términos o propiedades históricas
no demostrados.

**Salida:** assets, fuentes, metadatos, atribuciones y memoria de elaboración
completados e integrados en `feature/quarto-book` mediante PKG-03. Los mapas no
se insertan en capítulos ni en las salidas antes de PKG-07, después de GATE-01.

### PKG-04 — F3

**Objetivo:** comparar la política actual con F3 mediante una prueba
multiformato.

**Estado:** **COMPLETADO E INTEGRADO**. La revisión humana registró H1–H5 y
P1–P8 en **Sí**, con decisión `F3-APROBAR`. El commit
`61a50987a4ce3d05721834043d4e1c5c6c611a39` desplegó e integró el modelo
sobre 18/18 páginas y 35/35 unidades.

HTML debe probar recortes completos junto a la transcripción. PDF debe probar
miniatura/localizador, enlace al facsímil completo y retorno adecuado.

Debe medir:

- capacidad de cotejo;
- legibilidad;
- navegación;
- accesibilidad;
- páginas;
- tamaño;
- complejidad;
- reproducibilidad.

**Salida:** F3 aprobada e integrada globalmente: HTML con recorte al 74 %,
lightbox y navegación bidireccional; PDF con localizador al 28 %,
página/posición textual y navegación bidireccional. Suite completa:
**616 passed**.<br>
**Puerta:** decisión humana satisfecha para F3; GATE-01 permanece abierto por
las demás dependencias del plan.

### PKG-05 — Correcciones técnicas y rendimiento

**Estado:** **COMPLETADO E INTEGRADO**. El commit
`0be55e60cd25d1965eac9b4e421f5b8dda948650` fue revisado e integrado por
avance rápido. El cierre detallado consta en
[CIERRE_PKG_05_CORRECCIONES_TECNICAS_RENDIMIENTO.md](./CIERRE_PKG_05_CORRECCIONES_TECNICAS_RENDIMIENTO.md).

Correcciones obligatorias:

- REV-023, TOC PDF;
- REV-024, orden alfabético del glosario;
- REV-025, separación de entradas de los nueve índices PDF;
- DEC-014, comportamiento de la sidebar.

Optimización oportunista:

- auditoría REV-026 del PDF y bundle web;
- ensayos de optimización segura y reproducible.

No se impone un objetivo de megabytes, no se degrada la paleografía y no se
elimina contenido. Si no existe una mejora material y segura, el peso no bloquea
1.0.

**Salida:** REV-023–026 y DEC-014 resueltas; PDF de validación de 333 páginas y
70.802.128 bytes; web sin PDF de 73.910.522 bytes; 630 pruebas y validadores en
PASS. El render no constituye candidata formal.

### Preparación tras el cierre de PKG-00

| Paquete | Estado | Dependencia conservada |
|---|---|---|
| PKG-01 | **COMPLETADO E INTEGRADO** | Commit canónico `9ae4d1fd46d9f2d7bca685de861bff2a554a7a39`; sincronización técnica completada por CR-V1-001; presentación editorial y candidata pendientes. |
| PKG-02 | **COMPLETADO E INTEGRADO; INCIDENCIAS CANÓNICAS CERRADAS; PROPAGACIÓN PKG-08 COMPLETADA** | 16/16 tratadas; `INC-BIB-001` y `INC-BIB-002` cerradas en `a162fad`; 24 referencias activas integradas mediante PKG-08. |
| PKG-03 | **COMPLETADO E INTEGRADO** | Mapas regional y local APTO; procedencia, licencia, atribución, redistribución, accesibilidad y reproducibilidad verificadas. Inserción editorial pendiente de PKG-07. |
| PKG-04 | **COMPLETADO E INTEGRADO** | Prototipo `7c6d687`; `F3-APROBAR`; despliegue global `61a5098`; 18/18 páginas, 35/35 unidades y suite completa en PASS. |
| PKG-05 | **COMPLETADO E INTEGRADO** | REV-023–026 y DEC-014 resueltas en `0be55e6`; auditoría A/B sin pérdida, 630 pruebas y validadores en PASS. |

### Revisión de pretrabajos antes de GATE-01

No se integra el libro final hasta revisar conjuntamente:

- PKG-01;
- PKG-02;
- PKG-03;
- PKG-04;
- PKG-05;
- inputs disponibles de PKG-00.

Decisiones de salida:

- F3 aprobada humanamente, desplegada sobre 18/18 páginas y 35/35 unidades e
  integrada en la rama de publicación;
- aceptación registrada de `establecimiento del suelo` y `arenta` en PKG-01;
- resolución de `INC-BIB-001` e `INC-BIB-002` conforme al plan aprobado;
- aceptación de los dos mapas;
- aceptación del resultado de optimización.

### PKG-06 — Preliminares y arquitectura editorial

**Estado:** **HABILITADO — NO INICIADO** tras `GATE-01 = PASS`.

Implementa, sin reabrirlas:

- P3;
- landing HTML;
- portada PDF;
- créditos disponibles;
- prólogo;
- introducción;
- rutas histórica y documental;
- convenciones compactas;
- conservación del capítulo 4;
- macroorden actual;
- título y subtítulo;
- cierres conclusivos;
- retirada de la identidad de desarrollo.

**Salida:** apertura y arquitectura completas en `publication/`.

### PKG-07 — Aparato visual interno

**Estado:** **HABILITADO — NO INICIADO** tras `GATE-01 = PASS`.

Integra:

- cronología visual basada solo en hitos sustentados;
- diagrama económico integrado basado exclusivamente en el capítulo 13;
- mapas aprobados procedentes de PKG-03.

No incluye esquema Concejo/municipio, esquema histórico del término ni antigua
red de vulnerabilidades/amortiguadores.

**Salida:** recursos visuales multiformato, accesibles y con procedencia.

### PKG-08 — Fuentes, citas, trazabilidad y aparatos

**Estado:** **COMPLETADO E INTEGRADO** en
`c38bb87073362a8a100e7e91106b08f2a1592acb`. La revisión y el cierre constan en
[CIERRE_PKG_08_FUENTES_CITAS_TRAZABILIDAD_APARATOS.md](./CIERRE_PKG_08_FUENTES_CITAS_TRAZABILIDAD_APARATOS.md).

Implementa:

- CIT-B/C;
- `references.bib`;
- bibliografía pública;
- citas próximas selectivas;
- enlaces E ↔ matriz;
- política D/C/I/E/L;
- aparato compacto con nueve QA1;
- historia intelectual/editorial breve;
- modelos de cita principales por familias, cubriendo los once objetos;
- TOP-006 solo en la matriz.

No convierte el libro en un sistema de notas excesivo ni modifica afirmaciones
canónicas desde la bibliografía.

### PKG-09 — Identidad final, metadatos y cierre

**Estado:** **HABILITADO — NO INICIADO**, sujeto a sus DAT aplicables, tras
`GATE-01 = PASS`.

Cierra:

- valores finales diferidos de DAT-009 y, cuando ya exista, DAT-010;
- copyright;
- licencia;
- fecha editorial;
- URL canónica;
- versión final;
- créditos definitivos;
- colofón.

No inventa ningún valor. El ISBN continúa sin ser requisito de 1.0.

### PKG-10 — Regeneración reproducible y candidata

Debe:

- regenerar derivados;
- construir HTML;
- construir PDF;
- registrar tamaños y hashes;
- registrar versiones de fuentes;
- comprobar reproducibilidad.

**Salida:** nueva candidata 1.0. Todavía no es release.

### PKG-11 — Validación integral

Debe validar al menos:

- suite completa;
- integridad canónica;
- reproducibilidad;
- enlaces, citas, bibliografía y anclas;
- D/C/I/E/L;
- glosario, índices y TOC;
- HTML y PDF;
- navegación por teclado y vista estrecha;
- imágenes y equivalentes accesibles;
- mapas, cronología y diagrama;
- facsímil, transcripción y F3 final;
- peso;
- no regresión histórica;
- ausencia de identidad de desarrollo.

**Salida:** informe PASS o incidencias. Una incidencia fuera de alcance sigue el
mecanismo `CR-V1-*`.

### PKG-12 — Preview y aceptación humana

Despliega una preview según la decisión posterior de proveedor y realiza una
revisión humana real. No crea tag.

**Salida:** aceptación humana explícita o lista acotada de correcciones.

### PKG-13 — Fase 6B / release 1.0

Solo se inicia después de GATE-04 y GATE-05. Debe fijar versión, snapshot,
hashes, manifiesto, documentación final, commit de release, tag `v1.0` —o la
convención que se apruebe— y publicación según la política autorizada.

El tag solo aparece en este paquete.

## 3. DAG textual

```text
GATE-00
   ├── PKG-00 ───────────────────────────────┐
   ├── PKG-01 ───────────────────────────────┤
   ├── PKG-02 ───────────────────────────────┤
   ├── PKG-03 ───────────────────────────────┤
   ├── PKG-04 ───────────────────────────────┤
   └── PKG-05 ───────────────────────────────┘
                                               ↓
                                           GATE-01
                                               ↓
                         ┌───────── PKG-06 ─────────┐
                         ├───────── PKG-07 ─────────┤
                         ├───────── PKG-08 ─────────┤
                         └───────── PKG-09 ─────────┘
                                               ↓
                                           GATE-02
                                               ↓
                                            PKG-10
                                               ↓
                                            PKG-11
                                               ↓
                                           GATE-03
                                               ↓
                                            PKG-12
                                               ↓
                                           GATE-04
                                               ↓
                                           GATE-05
                                               ↓
                                            PKG-13
```

PKG-00–PKG-05 son conceptualmente paralelizables, pero no autorizan escrituras
simultáneas en un mismo worktree. `GATE-01 = PASS` habilita PKG-06–PKG-09;
pueden prepararse como ramas separadas solo cuando exista un plan explícito de
integración.

## 4. Tabla de dependencias

| Paquete | Requiere | Puede avanzar en paralelo con | Bloquea |
|---|---|---|---|
| PKG-00 | GATE-00 — cerrado con diferimientos controlados | PKG-01–05 | PKG-06, PKG-09 y citas finales |
| PKG-01 | GATE-00 — completado e integrado | PKG-00, PKG-02–05 | Regeneración de glosario; GATE-01 |
| PKG-02 | GATE-00 — completado e integrado; dos incidencias cerradas canónicamente | PKG-03–05 | Propagación editorial y bibliográfica en PKG-08 |
| PKG-03 | GATE-00 — completado e integrado | PKG-00–02, PKG-04–05 | PKG-07; GATE-01 |
| PKG-04 | GATE-00; `CR-V1-001` cerrada; prototipo, aprobación y despliegue global completados | PKG-00–03, PKG-05 | Política final del manuscrito integrada; GATE-01 |
| PKG-05 | GATE-00 — completado e integrado | PKG-00–04 | GATE-01 y PKG-10 |
| PKG-06 | GATE-01 — PASS; inputs aplicables de PKG-00 | PKG-07–09 con ramas/worktrees separados | GATE-02 |
| PKG-07 | GATE-01 — PASS; PKG-03 aceptado | PKG-06, PKG-08–09 | GATE-02 |
| PKG-08 | GATE-01 — PASS; PKG-02 aceptado | PKG-06–07, PKG-09 | GATE-02 |
| PKG-09 | GATE-01 — PASS; DAT resueltos o con diferimiento autorizado | PKG-06–08 | GATE-02 |
| PKG-10 | GATE-02 | — | PKG-11 |
| PKG-11 | PKG-10 | — | GATE-03 |
| PKG-12 | GATE-03 | — | GATE-04 |
| PKG-13 | GATE-04 y GATE-05 | — | Release 1.0 |

## 5. Autoridad y ámbito de escritura

| Paquete | Puede leer | Puede modificar | No puede modificar | Autoridad |
|---|---|---|---|---|
| PKG-00 | Documentos de alcance y formularios humanos | Dossier/input autorizado | `project/`, datos no proporcionados | Usuario |
| PKG-01 | Controles, fuentes canónicas y documentación necesaria | `project/` dentro de una operación canónica | `publication/generated/` como fuente; historia no autorizada | Manual y fuentes canónicas |
| PKG-02 | Inventario interno y, tras autorización, fuentes bibliográficas | Dossier de verificación; después datos bibliográficos de publicación | Afirmaciones históricas de `project/` | Fuentes bibliográficas para metadatos; Registro para el uso |
| PKG-03 | Alcance, índice de lugares y bases autorizadas | Assets/metadatos cartográficos de trabajo | `project/`; reconstrucción histórica | Licencia/base cartográfica y datos canónicos de nombres |
| PKG-04 | Facsímil, transcripción y configuración | Prototipo y despliegue global en `publication/` | `project/`; cambios históricos | DEC-012 y autoridades documentales |
| PKG-05 | Configuración, estilos, generadores y salidas | `publication/` técnico | `project/`, contenidos históricos | Contrato de publicación |
| PKG-06 | Decisiones y contenido editorial vigente | `publication/content/`, configuración y metadatos aplicables | `project/` y derivados manuales | DEC-001–015 |
| PKG-07 | Capítulos, Registro y assets aprobados | `publication/` visual y metadatos | `project/`; inferencias nuevas | DEC-020–024 |
| PKG-08 | Registro, auditoría bibliográfica y decisiones | `publication/` editorial/bibliográfico | Hechos o lecturas canónicas | DEC-025–033 |
| PKG-09 | DAT aprobados y resultados integrados | Metadatos, créditos y colofón de `publication/` | Datos humanos no declarados; `project/` | Usuario |
| PKG-10 | Fuentes y configuración aceptadas | Solo derivados regenerables y salidas | Fuentes canónicas o editoriales manuales | Pipeline reproducible |
| PKG-11 | Repositorio y candidata | Informes o correcciones autorizadas por incidencia | Ampliaciones silenciosas | Criterios de aceptación |
| PKG-12 | Candidata validada | Configuración de preview autorizada | Contenido sin CR/paquete; tag | Usuario/proveedor aprobado |
| PKG-13 | Snapshot aceptado e informes | Documentación y metadatos de release autorizados | Historia previa; fuentes fuera de alcance | Aceptación humana y política de release |

PKG-06–PKG-09 nunca parchean un cambio canónico. Si detectan uno, detienen la
incidencia y abren la operación correspondiente.

## 6. Estrategia de commits

- Un commit por paquete lógico aceptado.
- PKG-01 produce un commit canónico propio.
- Verificación/investigación e implementación no se mezclan salvo autorización
  expresa del contrato de un paquete.
- El árbol debe quedar limpio entre paquetes.
- Los commits de integración PKG-06–09 pueden separarse si sus ámbitos son
  independientes; no se fusionan artificialmente con PKG-01–05.
- No se hace push sin orden del usuario.
- No se crea tag antes de PKG-13.

Mensajes sugeridos, sin ejecutarlos:

```text
docs(publication): record editorial inputs for 1.0
feat(glossary): apply approved GH-B scope
docs(publication): verify bibliography for 1.0
feat(publication): add licensed orientation maps
test(publication): prototype F3 document access
fix(publication): resolve final composition defects
feat(publication): integrate 1.0 preliminaries
feat(publication): add approved visual apparatus
feat(publication): integrate citations and narrative apparatus
feat(publication): finalize 1.0 metadata and colophon
chore(publication): build 1.0 release candidate
docs(publication): validate 1.0 release candidate
docs(publication): record preview acceptance
chore(release): publish version 1.0
```

## 7. Puertas de control

### GATE-00 — Alcance 1.0 aprobado

- DEC-001–034 registradas.
- REV-001–026 clasificadas.
- Backlog, NO INCORPORAR y mecanismo `CR-V1-*` vigentes.
- Plan PKG-00–13 aprobado documentalmente.

### GATE-01 — Pretrabajos aceptados

**Decisión:** `GATE-01 = PASS` el 14 de octubre de 2026, sobre el HEAD evaluado
`9678856cff35d7cd2398a74590429180ef969bcc`. Evidencia completa en
[GATE_01_PRETRABAJOS_ACEPTADOS.md](./GATE_01_PRETRABAJOS_ACEPTADOS.md).

- PKG-01 canónico validado.
- PKG-02 integrado; `INC-BIB-001` e `INC-BIB-002` cerradas antes de aceptar
  GATE-01 y de implementar la correspondencia final fuente/uso en PKG-08.
- Mapas de PKG-03 aceptados y licenciados.
- `CR-V1-001` cerrada e integrada; suite general en PASS y PKG-04 desbloqueado.
- F3 decidido humanamente, desplegado globalmente e integrado.
- REV-023–025 tienen solución comprobada.
- Resultado de peso documentado.
- Inputs disponibles de PKG-00 revisados.

### GATE-02 — Integración editorial completa

**Estado:** `PENDIENTE`; permanece cerrado hasta integrar PKG-06–PKG-09.

- PKG-06–09 integrados.
- No quedan datos obligatorios sin resolver.
- No quedan cambios canónicos parcheados en `publication/`.
- El alcance coincide con `ALCANCE_APROBADO_V1_0.md`.

### GATE-03 — Nueva candidata validada técnicamente

- PKG-10 reproducible.
- PKG-11 en PASS.
- Sin defectos críticos o altos abiertos.
- Integridad de fuentes y ausencia de identidad de desarrollo comprobadas.

### GATE-04 — Preview aceptado por el usuario

- Preview real accesible por la vía autorizada.
- Revisión humana completada.
- Correcciones solicitadas resueltas y revalidadas.
- Aceptación explícita registrada.

### GATE-05 — Autorización explícita de 6B/release

- Snapshot, versión y política de publicación confirmados.
- Autorización humana expresa para PKG-13.
- Ninguna CR o incidencia bloqueante abierta.

## 8. Definición de DONE de 1.0

- [x] 1. Alcance aprobado.
- [ ] 2. Inputs editoriales resueltos.
- [x] 3. Glosario canónico actualizado.
- [x] 4. Bibliografía verificada; dos incidencias de correspondencia cerradas
  canónicamente y propagación editorial asignada a PKG-08.
- [x] 5. Mapas documentados y licenciados; assets preparados, integración
  editorial pendiente de PKG-07.
- [x] 6. F3 decidido, aprobado, desplegado globalmente e integrado.
- [x] 7. Defectos REV-023–025 corregidos; REV-026 optimizada sin pérdida y
  DEC-014 implementada.
- [ ] 8. Apertura y preliminares integrados.
- [ ] 9. Aparato visual integrado.
- [x] 10. CIT, bibliografía, QA, historia y modelos de cita integrados.
- [x] 11. D/C/I/E/L navegable.
- [ ] 12. Metadatos, licencia y copyright cerrados.
- [ ] 13. Salidas reproducibles.
- [ ] 14. Validación integral en PASS.
- [ ] 15. Preview revisado.
- [ ] 16. Aceptación humana registrada.
- [ ] 17. Fase 6B completada.
- [ ] 18. Tag 1.0 creado únicamente al final.

## 9. Control de alcance durante la ejecución

Un paquete no puede añadir trabajo por conveniencia. Cualquier necesidad nueva
se registra como `CR-V1-NNN` con origen, motivo, impacto, tipo —defecto o
ampliación—, recomendación y decisión humana. Una CR no aprobada no se ejecuta.

Los defectos de validación pueden producir CR correctivas, pero no autorizan
nuevos capítulos, investigaciones, visualizaciones o aparatos. La autoridad y el
procedimiento de cada cambio siguen siendo los de su paquete.

### CR-V1-001 — compatibilidad del analizador del Glosario GH-B

- Tipo: corrección técnica, sin ampliación de alcance.
- Estado: `CERRADA E INTEGRADA`.
- Origen: validación completa de PKG-03.
- Implementación: `c07bc011a42952f64622e3f78e8d759ad361cf29` adapta el
  consumidor técnico al GH-B aprobado sin modificar `project/`.
- Validación: suite completa en PASS; cuatro aparatos reproducibles bajo
  `publication/generated/`, ignorados y con cero archivos versionados.
- Resultado: bloqueo técnico eliminado; PKG-04 pudo ejecutarse y quedó
  aprobado e integrado posteriormente.

**GATE-01 — PASS. PKG-08 INTEGRADO; PKG-06, PKG-07 Y PKG-09 HABILITADOS; GATE-02 PENDIENTE.**

**SIGUIENTE PASO RECOMENDADO: racionalizar y formalizar el protocolo permanente de ejecución antes de iniciar PKG-06, PKG-07 o PKG-09.**

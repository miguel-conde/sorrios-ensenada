# PKG-02 — Cierre de verificación bibliográfica

## 1. Estado

`COMPLETADO E INTEGRADO CON INCIDENCIAS ABIERTAS`

`PKG-02: APTO PARA INTEGRACIÓN CON INCIDENCIAS ABIERTAS`

Las incidencias identificadas afectan a la correspondencia entre fuente externa
y uso, no a la lectura material de las respuestas 21 y 29. No impiden iniciar
PKG-03, pero deben cerrarse antes de GATE-01 y antes de implementar PKG-08.

## 2. Base e integración

- Base: `6e16d7aa12832ebd8fccc17f0988c90f00ad8357`.
- Rama de trabajo: `pkg-02/verificacion-bibliografica-v1`.
- Commit PKG-02: `9dbc0f8e7147c5ffa637f819ba17cfad5d19309d`
  (`docs(publication): verify bibliography for 1.0`).
- Rama objetivo: `feature/quarto-book`.
- Integración: fast-forward estricto desde la base al commit PKG-02; no se creó
  commit de merge, no se hizo rebase ni cherry-pick.
- Remoto: `origin/feature/quarto-book` permanecía en
  `da2c596b20abd5447c11c83955d18a99ad9af9a6`; no se hizo push.

## 3. Cobertura

- Referencias tratadas: 16/16, `BIB-001`–`BIB-016`.
- Correspondencia con Auditoría C: referencias 2, 4, 5, 6, 9, 10, 11, 12,
  25, 27, 28, 33, 34, 38, 39 y 40.
- `VERIFICADA CON AJUSTES BIBLIOGRÁFICOS`: 14.
- `VERIFICACIÓN PARCIAL`: 1.
- `INCOMPATIBILIDAD DE USO`: 1.
- Soporte: S1 = 13; S2 = 1; S3 = 1; S4 = 1.

## 4. Resultados bibliográficos

La revisión independiente confirma que el dossier completa los metadatos
aplicables sin inventar campos y conserva explícitas las discrepancias o
ausencias. El contraste focalizado con catálogos, repositorios institucionales,
DOI e ISBN no reveló errores manifiestos. BIB-012 permanece parcial porque la
URL registrada no permite verificar la formulación exacta. BIB-015 identifica
correctamente la obra institucional de Concepción Camarero Bullón, pero esa
obra no contiene la equivalencia entre viuda y medio vecino que se le atribuyó.

No se incorporaron fuentes sustitutivas, afirmaciones históricas nuevas, citas
ni registros BibTeX. El placeholder `publication/references.bib`, versionado
desde el bootstrap, permanece sin entradas y no fue modificado por PKG-02.

## 5. INC-BIB-001

### Problema

BIB-012 no permite demostrar que unas ordenanzas concejiles leonesas formulen
el uso completo atribuido a `TRA-006`. La URL original no estaba disponible y
las reproducciones localizadas solo permiten confirmar el sentido general de
`vecera` como turno.

### Trazabilidad interna

- La Edición Crítica 3.6, R29, folio 319v, dice que la taberna, «por no haver
  quien la arriende», «anda por vecera entre los vecinos» y no rinde utilidad.
- `TRA-005` registra ese extremo como D y lo vincula a R29.
- La edición modernizada, el Estudio Histórico y la voz canónica `vecera`
  conservan ese funcionamiento local.
- `TRA-006` es E/I: añade el paralelo general de ordenanzas leonesas y depende
  de la fuente externa no comprobada.

### Clasificación e impacto

- Clasificación: **BIB-A**.
- Autoridad afectada: correspondencia fuente/uso de `TRA-006` y su propagación
  contextual; no la lectura de R29 ni `TRA-005`.
- Severidad: **MEDIA**.
- Bloquea 1.0: **CONDICIONAL**; debe cerrarse antes de GATE-01.
- Bloquea PKG-03: **NO**.

### Operación recomendada

Abrir una operación canónica independiente que separe el dato local D del
paralelo E/I. Si la fuente actualmente registrada sigue sin demostrar el
paralelo, `TRA-006` y sus propagaciones deberán restringirse o retirarse sin
sustituir silenciosamente la fuente. La futura cita bibliográfica solo podrá
atribuir a BIB-012 aquello que esté efectivamente comprobado.

## 6. INC-BIB-002

### Problema

BIB-015 sustenta la organización de los libros de cabezas de casa o familias y
la inclusión de cónyuge, hijos, criados y otros convivientes. También declara
que viudas con casa abierta eran cabezas de casa. No sustenta que en diversos
lugares las viudas se computasen como medio vecino.

### Trazabilidad interna

- La Edición Crítica 3.6, R21, folio 318r, documenta ocho medios vecinos,
  «inclusas dos biudas».
- `DEM-001` registra ese extremo local como D.
- La edición modernizada y el Glosario mantienen el dato local y advierten que
  no constituye una regla jurídica general.
- `DEM-005` es E/I y reúne el contexto general de los libros personales con una
  generalización comparativa sobre viudas que BIB-015 no contiene.
- El capítulo 6 reproduce ambos niveles en un mismo párrafo contextual.

### Clasificación e impacto

- Clasificación: **MIX-B**.
- Autoridad afectada: separación D/E-I de `DEM-001` y `DEM-005`, más sus
  propagaciones; no la lectura de R21.
- Severidad: **MEDIA**.
- Bloquea 1.0: **CONDICIONAL**; debe cerrarse antes de GATE-01.
- Bloquea PKG-03: **NO**.

### Operación recomendada

Abrir una operación canónica independiente que conserve en D el dato local de
las dos viudas incluidas entre los medios vecinos y limite BIB-015 al contexto
que sí sustenta. `DEM-005` debe separar o modular los dos niveles antes de su
implementación bibliográfica en PKG-08. La operación no requiere buscar una
fuente sustitutiva ni reinterpretar R21.

## 7. Principio de autoridad

Las fuentes externas no deben utilizarse para respaldar artificialmente datos
primarios que ya pertenecen a D. R21 y R29 sostienen los datos locales; una
fuente E solo puede aportar el contexto externo que efectivamente documenta.

## 8. Propagación pendiente

Aún no se han implementado:

- registros bibliográficos en el placeholder `references.bib`;
- bibliografía final;
- citas próximas definitivas;
- correcciones de las entradas E/I afectadas;
- propagación de esas correcciones a capítulos o aparatos;
- regeneración Quarto.

## 9. Gate

PKG-02 queda integrado y permite continuar los pretrabajos con PKG-03. GATE-01
permanece abierto: `INC-BIB-001` e `INC-BIB-002` deberán estar resueltas porque
afectan a la correspondencia final fuente/uso y a formulaciones canónicas que
PKG-08 deberá propagar.

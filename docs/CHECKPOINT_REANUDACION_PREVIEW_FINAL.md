# Checkpoint de reanudación hasta PKG-12

**Base de la operación vigente:** `feature/quarto-book@bce6b38747ec6bc0bc5a58577f6e269c307b04a5`
**Función:** congelar el orden de reanudación sin iniciar ninguna operación.

## Estado actual

- PKG-01–PKG-11 están completados según su estado vigente.
- `GATE-01 = PASS` y `GATE-02 = PASS`.
- La candidata 1.0 fue validada integralmente por PKG-11.
- HUM-01B está completado: prólogo definitivo y declaración sobre
  IA/herramientas cerrados.
- E1 — REV-LECTOR-01 está **COMPLETADA**.
- E2 — LINK-01 está **COMPLETADA**.
- E3 — REV-LECTOR-02 está **COMPLETADA E INTEGRADA**.
- R4 — AUD-REPO-02 resultó **PASS** sobre `f41ad6a536fbda24696406723345e695fa531e3f`.
- R5A — preparación final del remoto está **COMPLETADA**.
- R5B — cambio controlado de visibilidad está **COMPLETADA**; el repositorio
  público fue verificado desde una perspectiva anónima.
- PUB-POLICY-01 está **COMPLETADA**.
- NETLIFY-RUNBOOK-01 está **COMPLETADA**.
- NETLIFY-CAPABILITY-02 está **COMPLETADA**: el flujo
  `draft → Publish Deploy` del mismo deploy quedó validado empíricamente,
  Netlify fue ratificado y el site canónico fue reservado.
- El proveedor, los parámetros operativos y la política de URL y fecha están
  registrados en
  [POLITICA_PUBLICACION_V1_0.md](./POLITICA_PUBLICACION_V1_0.md).
- Site canónico: `sorribos-santibanez-1752`;
  <https://sorribos-santibanez-1752.netlify.app/>.
- La URL canónica está **FIJADA**; su incorporación al libro está pendiente de
  `META-FINAL-01`.
- La fecha exacta continúa **PENDIENTE** hasta `DATE-FINAL-01`.
- La validación integral y los renders posteriores a HUM-01B están
  deliberadamente diferidos.
- PKG-12 **NO** se ha iniciado.

## Línea principal editorial congelada

### E1 — REV-LECTOR-01

**COMPLETADA.** Sus 23 hallazgos se aplicaron conjuntamente en E3.

Auditoría editorial orientada al lector, previa a cualquier corrección. Debe
cubrir:

- repetición excesiva del nombre del autor en Créditos;
- «dos operaciones» y su sustitución por una formulación más natural;
- versiones internas visibles de Edición Crítica, modernizada, Estudio y
  Registro;
- uso innecesario de «Quarto» en el discurso dirigido al lector;
- referencias públicas a `publication/content/`, `publication/generated/` y
  rastros técnicos similares;
- presentación adecuada de herramientas/IA;
- ubicación de «Correcciones y contacto»;
- referencia pública al repositorio.

### E2 — LINK-01

**COMPLETADA.** Sus correcciones localizadas se aplicaron conjuntamente en E3.

Auditoría de **todos** los enlaces externos e internos, bibliografía, anchors,
facsímil ↔ transcripción y matriz/retornos. Debe comprobar expresamente
`https://hdl.handle.net/10366/151409` y clasificar cada resultado como
`válido`, `redirigido`, `roto` o `no verificable automáticamente`.

### E3 — REV-LECTOR-02

**COMPLETADA E INTEGRADA.** Resultado incorporado a `feature/quarto-book` en
`73ed35830ca2cc3c36b531da4d8bde47efa73686`.

Aplicación conjunta de las correcciones resultantes de E1 y E2. Debe incluir:

- sección pública «Correcciones y contacto»;
- `miguelco2000@gmail.com` como correo público aprobado;
- GitHub Issues como canal complementario;
- referencia al repositorio público si ya está preparado.

Puede usarse provisionalmente un placeholder para email o repositorio. No se
ejecutará todavía la validación integral mientras sigan abiertas observaciones.

### E4 — REV-FINAL-PREVIEW

Solo cuando estén cerradas **todas** las observaciones editoriales:

- ejecutar una vez la suite completa y los validadores integrales;
- realizar un render HTML completo y un render PDF completo;
- registrar los nuevos hashes;
- completar una revisión final representativa.

El resultado será el objeto que pase a PKG-12.

### E5 — PKG-12

Preview y aceptación humana. No se ejecutará antes de E4.

## Línea paralela — repositorio público

### R1 — AUD-REPO-01

**COMPLETADA.** Resultado:

`REPO NO APTO TODAVÍA PARA APERTURA PÚBLICA`

Bloqueantes actuales:

1. tratamiento de privacidad de terceros vivos en el prólogo;
2. estructura de licencias.

Otros asuntos: README raíz, NOTICE/atribuciones, correo de contacto, rutas
locales, metadatos de correo Git, ramas temporales, Actions, referencias a la
visibilidad del repositorio y dependencia externa del manuscrito.

### R2A — Decisiones humanas de privacidad

**COMPLETADA.** Se conservan las menciones familiares del prólogo y el correo
histórico del autor en Git; no se reescribe el historial. Las personas
nombradas han revisado el prólogo y aceptan que se mantenga tal como está.

`REVISIÓN FAMILIAR DEL PRÓLOGO = COMPLETADA`

### R2B — Decisión humana de licencias

**COMPLETADA.** Contenido y documentación originales: CC BY 4.0; software y
herramientas: MIT; materiales de terceros y exclusiones: NOTICE.

### R3 — PUB-REPO-01

**COMPLETADA E INTEGRADA.** Preparación controlada del repositorio para su
revisión. **No** cambia todavía su visibilidad.

### R4 — AUD-REPO-02

**PASS.** Auditoría final de HEAD e historial completada sobre
`f41ad6a536fbda24696406723345e695fa531e3f`.

### R5A — Preparación final del remoto

**COMPLETADA.** Revisión familiar cerrada, correo público resuelto como
`miguelco2000@gmail.com` y remoto privado normalizado para la apertura.

### R5B — Cambio de visibilidad

**COMPLETADA.** El repositorio
<https://github.com/miguel-conde/sorrios-ensenada> es público. La URL canónica
del libro continúa pendiente y se rige por
[POLITICA_PUBLICACION_V1_0.md](./POLITICA_PUBLICACION_V1_0.md).

## Relación entre líneas

- La preparación del repositorio no sustituye ni reordena la línea editorial.
- E1 y E2 pueden ejecutarse aunque R2 o R3 sigan pendientes.
- E3 puede usar provisionalmente placeholders de email o repositorio.
- La URL canónica del libro está fijada y debe incorporarse mediante
  `META-FINAL-01` antes de E4.
- La apertura debe completarse antes del release si la edición final enlaza al
  repositorio.
- PKG-12 no debe convertirse en una auditoría del repositorio.

## Observaciones editoriales conocidas

1. Simplificar Créditos.
2. Cambiar «operaciones».
3. Revisar el enlace GREDOS/handle.
4. Revisar todos los enlaces.
5. Retirar versiones internas visibles innecesarias.
6. Retirar «Quarto» cuando sea jerga innecesaria.
7. Eliminar rutas internas del discurso dirigido al lector.
8. La declaración IA/herramientas ya fue revisada en HUM-01B.
9. Añadir un canal para reportar errores.
10. Añadir una referencia al repositorio público.
11. Correo público resuelto como `miguelco2000@gmail.com` por decisión humana.

Nuevas observaciones humanas pueden incorporarse antes de REV-FINAL-PREVIEW.

## Reanudación

- **Siguiente operación de la línea principal:** `E4 — REV-FINAL-PREVIEW`
  (**PENDIENTE** y bloqueada únicamente hasta incorporar la URL canónica y la
  referencia pública mediante `META-FINAL-01`).
- **Siguiente paso previo a E4:**
  `META-FINAL-01 — INCORPORACIÓN DE URL CANÓNICA Y REFERENCIA PÚBLICA PREVIA A E4`.
- `GATE-03` y `GATE-04` permanecen **PENDIENTES**.
- PKG-12 y PKG-13 permanecen **NO INICIADOS**.

Ninguna de esas operaciones se inicia en este checkpoint.

# Checkpoint de reanudación hasta PKG-12

**Candidata validada por E4:** `d073fd8711f9fa50705308c65fabea0a2fae0d29`
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
- META-FINAL-01 está **COMPLETADA**: la URL canónica y la referencia pública
  del repositorio están incorporadas a la edición.
- La URL canónica está **RESUELTA** y en estado
  **RESERVADA / PREPUBLICACIÓN**. Production permanece sin el libro; un HTTP
  404 es esperado hasta PKG-13. PKG-12 revisará una URL de draft distinta y
  PKG-13 hará live el draft final autorizado en la URL canónica.
- Repositorio, email y año editorial están **RESUELTOS**.
- La fecha exacta continúa **PENDIENTE** hasta `DATE-FINAL-01`.
- E4-FIX-01 está **PASS**. Los abortos operativos E4-R2 y E4-R3 quedaron
  superados mediante el bootstrap previo y el `PATH` verificado de
  `rsvg-convert`.
- E4-R4 está **PASS** y E4 está **COMPLETADA** sobre
  `CANDIDATE_SOURCE_SHA = d073fd8711f9fa50705308c65fabea0a2fae0d29`.
- Las huellas finales HTML/PDF constan en
  [E4_REV_FINAL_PREVIEW.md](./E4_REV_FINAL_PREVIEW.md).
- GATE-03 está **PASS** y la candidata técnica construida desde
  `d073fd8711f9fa50705308c65fabea0a2fae0d29` está **ACEPTADA PARA PKG-12**.
  La decisión formal consta en
  [GATE_03_CANDIDATA_TECNICA_ACEPTADA.md](./GATE_03_CANDIDATA_TECNICA_ACEPTADA.md).
- Siguen vigentes el manifiesto web
  `3748a882e2e5f43581cb01071895c6219d5008c3275f306818a47f1658166ef1`
  y el PDF
  `a00db79d7cbcec39c63f4b4d16a9c369a0eae4ab9c6c3d2d408c4d52171981f7`.
- PKG-12 tiene la **PREVIEW DESPLEGADA / REVISIÓN HUMANA PENDIENTE**. El
  dossier es [PKG_12_PREVIEW_ACEPTACION_HUMANA.md](./PKG_12_PREVIEW_ACEPTACION_HUMANA.md).
- Deploy ID: `6ad6498e223ba4f4bb20e6bd`.
- Draft:
  <https://6ad6498e223ba4f4bb20e6bd--sorribos-santibanez-1752.netlify.app>.
- Production continúa vacío y sin servir el libro; el deploy es manual, no
  productivo, sin build remoto y sin integración Git.

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

**COMPLETADA.** E4-R4 terminó con el veredicto
`E4 PASS — CANDIDATA VIGENTE APTA PARA GATE-03`. La evidencia integral y las
huellas finales están registradas en
[E4_REV_FINAL_PREVIEW.md](./E4_REV_FINAL_PREVIEW.md).

La validación ejecutada, una vez cerradas todas las observaciones editoriales,
incluyó:

- ejecutar una vez la suite completa y los validadores integrales;
- realizar un render HTML completo y un render PDF completo;
- registrar los nuevos hashes;
- completar una revisión final representativa.

El resultado es el objeto que debe evaluar GATE-03 antes de PKG-12.

### E5 — PKG-12

**PREVIEW DESPLEGADA / REVISIÓN HUMANA PENDIENTE.** La candidata técnica
aceptada por GATE-03 está disponible en el draft registrado en
[PKG_12_PREVIEW_ACEPTACION_HUMANA.md](./PKG_12_PREVIEW_ACEPTACION_HUMANA.md).
No puede declararse aceptada hasta recibir la decisión humana expresa.

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
del libro está resuelta y se rige por
[POLITICA_PUBLICACION_V1_0.md](./POLITICA_PUBLICACION_V1_0.md).

## Relación entre líneas

- La preparación del repositorio no sustituye ni reordena la línea editorial.
- E1 y E2 pueden ejecutarse aunque R2 o R3 sigan pendientes.
- E3 puede usar provisionalmente placeholders de email o repositorio.
- La URL canónica y la referencia pública quedaron incorporadas mediante
  `META-FINAL-01` antes de E4.
- La apertura debe completarse antes del release si la edición final enlaza al
  repositorio.
- PKG-12 no debe convertirse en una auditoría del repositorio.

## Cierre de observaciones previas a E4

E1–E3, HUM-01B y META-FINAL-01 han resuelto las observaciones editoriales
conocidas: texto orientado al lector, enlaces, declaración IA/herramientas,
canales de corrección, repositorio público y URL canónica. No quedan
observaciones editoriales conocidas que bloqueen E4. La fecha exacta no es una
observación abierta: está **DIFERIDA POR POLÍTICA** hasta `DATE-FINAL-01`.

## Reanudación

- `GATE-03 = PASS`; candidata técnica **ACEPTADA**.
- `PKG-12 = PREVIEW DESPLEGADA / REVISIÓN HUMANA PENDIENTE`.
- **Siguiente acción exclusiva:** revisión humana del draft de PKG-12.
- `GATE-04` y `GATE-05` permanecen **PENDIENTES**.
- PKG-13 permanece **NO INICIADO**.
- `DATE-FINAL-01` permanece **PENDIENTE**.

Ninguna de esas operaciones se inicia en este checkpoint.

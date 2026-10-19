# GATE-03 — Candidata técnica aceptada

**Decisión:** `GATE-03 PASS — CANDIDATA TÉCNICA ACEPTADA PARA PKG-12`
**Fecha:** 19 de octubre de 2026

## Identidad

- `CANDIDATE_SOURCE_SHA`:
  `d073fd8711f9fa50705308c65fabea0a2fae0d29`.
- `E4_R4_EVIDENCE_SHA`:
  `8bc13788d43b74832323087b5bdd422fdd3e1089`.
- El commit de evidencia es hijo directo del commit fuente y modifica solo
  [E4_REV_FINAL_PREVIEW.md](./E4_REV_FINAL_PREVIEW.md) y
  [CHECKPOINT_REANUDACION_PREVIEW_FINAL.md](./CHECKPOINT_REANUDACION_PREVIEW_FINAL.md).
- La candidata aceptada sigue siendo el commit fuente; el commit E4 no la
  redefine ni altera `project/`, `publication/`, tests, configuración,
  generadores o metadata.

## Evidencia E4 reutilizada

El dossier [E4_REV_FINAL_PREVIEW.md](./E4_REV_FINAL_PREVIEW.md) registra:

- E4 inicial: FAIL real de validación, corregido mediante E4-FIX-01;
- E4-R2 y E4-R3: abortos operativos superados, sin defecto de contenido;
- E4-FIX-01: PASS;
- E4-R4: PASS;
- suite integral: `696 passed`, 0 failed y 0 errors;
- validadores integrales, revisión visual HTML/PDF y accesibilidad: PASS;
- Netlify: 0 deploys.

No se repitieron render, suite, preparación ni revisión visual integral porque
el SHA, los inputs, la configuración y el toolchain relevantes no cambiaron.

## Artefactos aceptados

Los artefactos locales de `publication/_book/` siguen disponibles y fueron
verificados de nuevo sin regeneración.

### Web

- 40 documentos HTML;
- 120 archivos públicos, excluido el PDF;
- 74.657.296 bytes;
- SHA-256 del manifiesto ordenado:
  `3748a882e2e5f43581cb01071895c6219d5008c3275f306818a47f1658166ef1`.

### PDF

- 360 páginas;
- 71.028.386 bytes;
- SHA-256:
  `a00db79d7cbcec39c63f4b4d16a9c369a0eae4ab9c6c3d2d408c4d52171981f7`.

PKG-12 debe desplegar exactamente estos bytes.

## Integridad

- Árbol `project/`:
  `a8ccb6d783e51aafb6493fed9791097d0a678086`.
- Manuscrito: 18 páginas, 5.038.575 bytes, SHA-256
  `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`.
- `publication/_book/` y `publication/generated/` permanecen ignorados.
- No hay derivados versionados ni incidencias técnicas abiertas.

## Metadata y Netlify

- versión 1.0, año 2026, URL canónica, repositorio público y correo:
  resueltos;
- fecha exacta: pendiente por política hasta `DATE-FINAL-01`;
- ISBN: ausente y no bloqueante;
- site: `sorribos-santibanez-1752`;
- site ID: `1539a52a-d500-426f-9995-7db9c01e6d45`;
- integración Git: ninguna;
- deploys: 0; drafts: 0; production: vacío.

La fecha exacta pendiente no impide GATE-03 ni PKG-12.

## Decisión formal

La evidencia E4 es íntegra, el commit documental no altera la candidata, los
artefactos locales coinciden exactamente con sus huellas validadas y la
integridad canónica está preservada. PKG-12 puede recibir la candidata
construida desde `d073fd8711f9fa50705308c65fabea0a2fae0d29`.

`GATE-03 PASS — CANDIDATA TÉCNICA ACEPTADA PARA PKG-12`

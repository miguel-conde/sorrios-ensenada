# PKG-12 — Preview y aceptación humana

**Veredicto técnico:** `PKG-12 PREVIEW DEPLOYED — HUMAN REVIEW REQUIRED`
**Revisión humana:** `PENDIENTE`
**Fecha técnica del deploy:** `2026-10-19T16:47:10.561Z`

## Identidad de la candidata

- `GATE03_TARGET`:
  `4a366e5c49cb4553f5fedc56bd696ff4c2136a8d`.
- `CANDIDATE_SOURCE_SHA`:
  `d073fd8711f9fa50705308c65fabea0a2fae0d29`.
- `E4_R4_EVIDENCE_SHA`:
  `8bc13788d43b74832323087b5bdd422fdd3e1089`.
- Árbol `project/`:
  `a8ccb6d783e51aafb6493fed9791097d0a678086`.

No se regeneró la candidata. Antes del despliegue, el `_book/` existente
coincidió exactamente con las huellas aceptadas por E4 y GATE-03:

### Web

- 40 documentos HTML;
- 120 archivos, excluido el PDF;
- 74.657.296 bytes;
- SHA-256 del manifiesto ordenado:
  `3748a882e2e5f43581cb01071895c6219d5008c3275f306818a47f1658166ef1`.

### PDF

- 360 páginas;
- 71.028.386 bytes;
- SHA-256:
  `a00db79d7cbcec39c63f4b4d16a9c369a0eae4ab9c6c3d2d408c4d52171981f7`.

## Deploy draft no productivo

- Site: `sorribos-santibanez-1752`.
- Site ID: `1539a52a-d500-426f-9995-7db9c01e6d45`.
- Deploy ID: `6ad6498e223ba4f4bb20e6bd`.
- URL del draft:
  <https://6ad6498e223ba4f4bb20e6bd--sorribos-santibanez-1752.netlify.app>.
- Permalink adicional: Netlify no expone otro; la URL anterior está ligada al
  deploy ID.
- Contexto Netlify: `deploy-preview`.
- Estado: `ready`, manual y no publicado (`published_at = null`).
- Build remoto: 0; `build_id = null`.
- Integración Git: ninguna; `repo_url = null` y configuración de build vacía.

El deploy se creó manualmente mediante el inventario de archivos de Netlify,
sin build y sin promoverlo a producción. La URL canónica de producción sigue
devolviendo HTTP 404 y el site continúa sin `published_deploy`.

## Verificación de identidad

- Inventario almacenado en Netlify: 121/121 archivos; rutas, tamaños y SHA-1
  coinciden con todos los blobs locales.
- Manifiesto web local vuelto a comprobar contra E4/GATE-03: PASS.
- PDF descargado desde el draft: 360 páginas, 71.028.386 bytes y SHA-256
  exacto: PASS.
- Muestra representativa de CSS, JavaScript, SVG y PNG servidos: bytes y
  SHA-256 exactos.
- Doce HTML representativos: contenido textual visible idéntico al local.
- Netlify aplica `Pretty URLs` al servir HTML y reescribe únicamente enlaces
  internos; el inventario de blobs almacenados conserva identidad íntegra por
  ruta, tamaño y SHA-1.

## Smoke remoto

Respondieron HTTP 200:

- landing;
- créditos;
- prólogo;
- capítulos 3 y 13;
- facsímil;
- transcripción;
- edición modernizada;
- matriz de evidencia;
- «Cómo citar»;
- «Correcciones y contacto»;
- colofón;
- PDF descargable.

Los 40 HTML están presentes y responden. La navegación interna está poblada
en las páginas representativas. Los 40 canonical apuntan al dominio de
producción. El draft conserva la versión 1.0, el año 2026, la URL canónica, el
repositorio público, GitHub Issues y `miguelco2000@gmail.com`; mantiene la
fecha exacta como pendiente y no añade ISBN.

## Integridad operativa

- Fuentes del libro: sin cambios.
- `project/`: intacto.
- `publication/_book/`: no versionado.
- 0 renders.
- 0 ejecuciones de `prepare.py`.
- 0 suites completas.
- Production: intacta y sin servir el libro.
- Builds remotos: 0.
- Integración Git en Netlify: ninguna.
- Tag/release: no creados.

## Estado

- PKG-12: `PREVIEW DESPLEGADA / REVISIÓN HUMANA PENDIENTE`.
- GATE-04: `PENDIENTE`.
- DATE-FINAL-01: `PENDIENTE`.
- GATE-05: `PENDIENTE`.
- PKG-13: `NO INICIADO`.

La decisión humana posterior debe ser exactamente una de estas:

- `PKG-12 ACEPTADA — PREVIEW APROBADA`;
- `PKG-12 REQUIERE CORRECCIONES`.

# PKG-12 — Preview y aceptación humana

**Veredicto técnico vigente:**
`PKG-12-R3 PREVIEW DEPLOYED — FINAL HUMAN APPROVAL REQUIRED`

**Revisión humana final:** `PENDIENTE`

**Fecha técnica del deploy vigente:** `2026-10-31T13:40:04.432Z`

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

## R2 — Preview corregida tras HUM-REVIEW-FIX-01

La primera preview fue revisada por el autor y dio lugar a tres correcciones:
ajuste mínimo de una frase del prólogo, sustitución de la etiqueta «Autor/a»
por «Autor» y actualización integral del README público. También se cerró como
decisión editorial que no se solicitará ISBN para la versión 1.0 no comercial.
El cierre de esas correcciones consta en
[HUM_REVIEW_01_CIERRE.md](./HUM_REVIEW_01_CIERRE.md).

### Identidad de la candidata corregida

- `HUM_REVIEW_FIX_TARGET`:
  `cf34af15ea3f8b6b538ba4464fabe2dda3ee2e20`.
- Árbol `project/`:
  `a8ccb6d783e51aafb6493fed9791097d0a678086`.
- Web: 40 documentos HTML; 120 archivos excluido el PDF; 74.657.270 bytes;
  manifest SHA-256
  `2e2eb284c7539647349c072f0262f04a8da334e37720181009924c99600bf4cd`.
- PDF: 360 páginas; 71.028.364 bytes; SHA-256
  `7d0a63e85329951ec4cf1f5e747f23cfa41e062d0b929d2a128dc52354c876d2`.

La identidad local se recalculó antes del despliegue sin regenerar ningún
artefacto y coincidió exactamente con HUM-REVIEW-FIX-01.

### Nuevo deploy draft no productivo

- Site: `sorribos-santibanez-1752`.
- Site ID: `1539a52a-d500-426f-9995-7db9c01e6d45`.
- Deploy ID: `6ae5b63c48bf70292280a8fb`.
- Fecha técnica: `2026-10-31T09:34:52.920Z`.
- URL del draft:
  <https://6ae5b63c48bf70292280a8fb--sorribos-santibanez-1752.netlify.app>.
- Contexto: `deploy-preview`; estado: `ready`.
- `published_at = null`; `build_id = null`.

El deploy se creó manualmente con los artefactos locales ya construidos. No se
usó producción, conexión Git ni build remoto.

### Verificación remota R2

- Inventario Netlify: 121/121 rutas, tamaños y SHA-1 idénticos al inventario
  local.
- Los 40 HTML responden HTTP 200 y declaran la URL canónica correcta.
- El PDF remoto coincide byte a byte con el local y conserva el SHA-256
  registrado.
- Muestras de CSS, JavaScript, SVG y PNG coinciden byte a byte.
- El prólogo muestra «Cuando conocí Sorríos» y no la redacción anterior.
- La portada HTML muestra «Autor»; «Autor/a» no aparece en la superficie HTML.
- El ISBN no figura como pendiente y la fecha exacta continúa diferida.
- Repositorio, GitHub Issues y correo público son correctos.
- El README de `main` en GitHub coincide con el local y cubre proyecto, obra,
  autoría, URL, estructura, reproducibilidad, licencias, ISBN y contacto.
- Production continúa sin `published_deploy` y responde HTTP 404.
- Los dos deploys existentes tienen `build_id = null` y `published_at = null`;
  la integración Git sigue ausente.

### Estado R2

`REVISIÓN HUMANA FINAL PENDIENTE`

- GATE-04: `PENDIENTE`.
- DATE-FINAL-01: `PENDIENTE`.
- GATE-05: `PENDIENTE`.
- PKG-13: `NO INICIADO`.

## R3 — Preview final tras HUM-REVIEW-FIX-02

La revisión humana de R2 solicitó un último retoque localizado del comienzo
del prólogo. HUM-REVIEW-FIX-02 incorporó y validó ese cambio sin alterar el
resto del contenido ni la arquitectura de la publicación.

### Identidad de la candidata final corregida

- `HUM_REVIEW_FIX_02_TARGET`:
  `e0bba5379cf3277a47556e9627772ef03f7bb3a8`.
- Árbol `project/`:
  `a8ccb6d783e51aafb6493fed9791097d0a678086`.
- Web: 40 documentos HTML; 120 archivos excluido el PDF; 74.658.040 bytes;
  manifest SHA-256
  `84cfc5214a4da777fd407f2b93da4b1fe3b037a0e22426d96509bb50ccfbee61`.
- PDF: 360 páginas; 71.028.850 bytes; SHA-256
  `00d25e78504597f0a9472f0df91e9f41f0b473c8d56dffb08529cf943e8a16e2`.

La identidad local se recalculó antes del despliegue sin regenerar artefactos
y coincidió exactamente con HUM-REVIEW-FIX-02.

### Deploy draft final no productivo

- Site: `sorribos-santibanez-1752`.
- Site ID: `1539a52a-d500-426f-9995-7db9c01e6d45`.
- Deploy ID: `6ae5efb49656d03ff46118df`.
- Fecha técnica: `2026-10-31T13:40:04.432Z`.
- URL del draft:
  <https://6ae5efb49656d03ff46118df--sorribos-santibanez-1752.netlify.app>.
- Contexto: `deploy-preview`; estado: `ready`.
- `published_at = null`; `build_id = null`.

El deploy se creó manualmente con los artefactos locales ya construidos. No se
usó producción, conexión Git ni build remoto.

### Verificación remota R3

- Inventario Netlify: 121/121 rutas, tamaños y SHA-1 idénticos al inventario
  local.
- Los 40 HTML responden HTTP 200 y declaran la URL canónica correcta.
- El PDF remoto coincide byte a byte con el local, conserva el SHA-256
  registrado y tiene 360 páginas.
- Muestras de CSS, JavaScript, SVG y PNG coinciden byte a byte.
- El prólogo contiene el inicio final aprobado y conserva las menciones
  editoriales requeridas; la redacción sustituida no aparece.
- La composición focal del prólogo en HTML y en las páginas 23–24 del PDF no
  presenta defectos visibles.
- La portada HTML muestra «Autor»; «Autor/a» no aparece.
- El ISBN no figura como pendiente y la fecha exacta continúa diferida.
- Repositorio, GitHub Issues y correo público son correctos.
- El README público de `main` coincide con el local y conserva el contrato
  aprobado.
- Production continúa sin `published_deploy` y responde HTTP 404.
- Los tres deploys existentes tienen `build_id = null` y
  `published_at = null`; la integración Git sigue ausente.

### Estado R3

`REVISIÓN HUMANA FINAL PENDIENTE`

- GATE-04: `PENDIENTE`.
- DATE-FINAL-01: `PENDIENTE`.
- GATE-05: `PENDIENTE`.
- PKG-13: `NO INICIADO`.

# GATE-05 — Aprobación del snapshot final exacto

## Veredicto

`GATE-05 PASS — SNAPSHOT FINAL EXACTO AUTORIZADO PARA PUBLICACIÓN v1.0`

## Base reconciliada

- `DATE_FINAL_FIX_01_TARGET`:
  `58f669d5c9aac9d2e8d960484f828506beb6ae71`.
- `GATE05_BASE_TARGET`:
  `a1de56fb6d074c78a02883ffbb331403f92f83b5` — reconciliación documental y
  descripción factual corregida de DATE-FINAL-01-FIX-01.
- Desde DATE-FINAL-01-FIX-01 solo cambiaron documentación de control y una
  prueba de roadmap. `publication/`, `project/`, el artefacto aprobado y el
  deploy permanecen intactos.

La evidencia técnica se reutiliza de
[DATE-FINAL-01](./DATE_FINAL_01.md) y
[DATE-FINAL-01-FIX-01](./DATE_FINAL_01_FIX_01.md); no se reconstruyó ni se
regeneró ningún artefacto.

## Snapshot aprobado

- Deploy ID: `6ae6435a5695ab37b483c758`.
- Draft:
  <https://6ae6435a5695ab37b483c758--sorribos-santibanez-1752.netlify.app>.
- Estado: `ready`, manual, no productivo, sin build remoto ni integración Git.
- Web: 40 HTML, 120 archivos sin PDF y 74.657.837 bytes.
- Manifest web SHA-256:
  `67b1d03ae63d33886121daefda72f1479382227f25643eb52341aad6be59a29f`.
- PDF: 360 páginas y 71.029.142 bytes.
- PDF SHA-256:
  `e6b00d65876a5c5a20f2327bde39d624ba1f6da82b1b40d18a57b055fd8de470`.
- Conjunto completo: 121 archivos y 145.686.979 bytes.
- Manifest completo SHA-256:
  `e49e1e50f0f5a43dbe0c78bfd15b131afd37e1e40cd51af7ad39ddd0c5c9333a`.
- Identidad remota validada: 121/121 archivos; PDF remoto idéntico byte a
  byte.

## Decisión humana vinculante

`GATE-05 AUTORIZADO — APRUEBO EL SNAPSHOT FINAL EXACTO PARA PUBLICACIÓN v1.0`

La aprobación se refiere exclusivamente al deploy y a las huellas indicadas
arriba. No se transfiere a un rebuild, rerender, nueva subida o deploy
distinto.

## Decisiones editoriales finales

- Autor: Miguel Conde de Simón.
- Título: *Sorribos y Santibáñez de Ordás en 1752*.
- Subtítulo: *Estudio histórico y edición integral del Catastro de Ensenada*.
- Versión: `1.0`.
- Fecha oficial: `1 de noviembre de 2026`.
- Colofón: `1 de noviembre de 2026, solemnidad de Todos los Santos`.
- Firma del prólogo: `Madrid, octubre de 2026`.
- ISBN: `NO SE SOLICITA`.
- URL canónica:
  <https://sorribos-santibanez-1752.netlify.app/>.

## Regla de inmutabilidad para PKG-13

PKG-13 debe publicar **EXACTAMENTE** el deploy
`6ae6435a5695ab37b483c758`. No puede rerenderizar, reconstruir, ejecutar
`prepare.py`, modificar fuentes, volver a subir `_book/`, crear un deploy
equivalente ni cambiar ningún byte. Debe usar **Publish Deploy** o el mecanismo
de Netlify que haga live ese mismo deploy.

Si Netlify no permite promover exactamente ese deploy, la operación debe
detenerse. No puede sustituirse la identidad de bytes aprobada por una
equivalencia supuesta.

## Estado al cierre

- Production: no publicada; la URL canónica continúa respondiendo HTTP 404.
- Draft aprobado: accesible con HTTP 200.
- GATE-05: `PASS`.
- PKG-13: habilitada como siguiente y única operación de publicación.
- Tag `v1.0`: no creado.
- GitHub Release: no creada.

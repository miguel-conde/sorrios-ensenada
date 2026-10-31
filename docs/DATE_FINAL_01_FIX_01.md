# DATE-FINAL-01-FIX-01 — Corrección focal del colofón

## Veredicto

`DATE-FINAL-01-FIX-01 PASS — COLOFÓN CORREGIDO Y NUEVO SNAPSHOT FINAL PREPARADO PARA REVISIÓN HUMANA`

## Incidencia y corrección

La revisión humana de la candidata fechada detectó que, en PDF, la URL
canónica continuaba en la misma línea que la fecha de publicación. El defecto
era exclusivamente de composición: el bloque usaba etiquetas HTML `<br>`, que
no imponían el mismo salto en LaTeX/PDF.

En `publication/content/06-aparatos/colofon.qmd` se sustituyó únicamente ese
mecanismo por saltos de línea Markdown/Pandoc:

```markdown
**Año editorial:** 2026.\
**Fecha de publicación:** 1 de noviembre de 2026, solemnidad de Todos los Santos.\
**URL canónica:** <https://sorribos-santibanez-1752.netlify.app/>.
```

No cambió ningún carácter del contenido aprobado. La comparación contra
`aed21c5e619fc66465046d86243f4b8c33597c93` confirma que este es el único
cambio editorial; `project/` permanece intacto.

## Validación

- Validación focal de fuente: PASS; bloque único, texto idéntico y ausencia de
  `<br>` en las tres líneas.
- Tests focales: `46 passed`.
- Suite completa, ejecutada una sola vez: `701 passed`, `0 failed`,
  `0 errors`.
- Preparación reproducible: `PREPARE_TOTAL = 2`.
- SHA-256 de `publication/generated/` tras ambas preparaciones:
  `e777ba39fc5781fd667265900760d2c58e02ef922e7f7022725a1c6c32904375`.
- Render completo HTML/PDF: PASS.
- Validadores canónico, de fuentes, publicación estática y renderizada,
  cartografía, enlaces, anchors, bibliografía, D/C/I/E/L, candidata, PDF,
  contraste y compilación Python: PASS.
- `git diff --check`: PASS.

## Revisión visual focal

- HTML: Año editorial, fecha de publicación y URL canónica aparecen en tres
  líneas separadas; enlace correcto y sin desbordamiento.
- PDF, página 360: las tres líneas aparecen separadas y la URL comienza en una
  línea propia; no hay salto de página extraño, desbordamiento ni alteración
  textual.

## Nueva candidata para GATE-05

### Web

- Documentos HTML: 40.
- Archivos, excluido el PDF: 120.
- Tamaño, excluido el PDF: 74.657.837 bytes.
- Manifest SHA-256:
  `67b1d03ae63d33886121daefda72f1479382227f25643eb52341aad6be59a29f`.

### PDF

- Páginas: 360.
- Tamaño: 71.029.142 bytes.
- SHA-256:
  `e6b00d65876a5c5a20f2327bde39d624ba1f6da82b1b40d18a57b055fd8de470`.

### Conjunto completo

- Archivos: 121.
- Tamaño: 145.686.979 bytes.
- Manifest SHA-256:
  `e49e1e50f0f5a43dbe0c78bfd15b131afd37e1e40cd51af7ad39ddd0c5c9333a`.

Estos valores sustituyen a los registrados en DATE-FINAL-01 como identidad de
la candidata para GATE-05.

## Nuevo draft no productivo

- Site ID: `1539a52a-d500-426f-9995-7db9c01e6d45`.
- Deploy ID: `6ae6435a5695ab37b483c758`.
- URL:
  <https://6ae6435a5695ab37b483c758--sorribos-santibanez-1752.netlify.app>.
- Creación técnica: `2026-10-31T19:36:58.738Z`.
- Estado: `ready`, manual, no productivo, sin build remoto y sin integración
  Git.

La identidad remota quedó comprobada: inventario `121/121`, tamaños y SHA-1
idénticos; 40 HTML accesibles con canonical correcto; bloque del colofón en
tres líneas; PDF remoto idéntico byte a byte. Production continúa en HTTP 404,
sin deploy publicado, con cero builds remotos e integración Git ausente.

El deploy anterior `6ae5ffeaa97b544ed057b110` queda **SUPERADO** y no debe
usarse en GATE-05.

## Continuación

- `GATE-05`: pendiente de revisión humana del nuevo snapshot.
- `PKG-13`: no iniciado.
- Production: no publicada.
- Tag/release: no creados.

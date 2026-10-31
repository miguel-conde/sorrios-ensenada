# DATE-FINAL-01 — Fecha oficial y candidata final fechada

## Veredicto

`DATE-FINAL-01 PASS — CANDIDATA FINAL FECHADA PREPARADA PARA GATE-05`

## Decisión editorial aplicada

- Fecha oficial ISO: `2026-11-01`.
- Fecha pública: `1 de noviembre de 2026`.
- Colofón: `1 de noviembre de 2026, solemnidad de Todos los Santos`.
- Firma final del prólogo:

  `**Miguel Conde de Simón**<br>` y, en la línea siguiente,
  `Madrid, octubre de 2026`.

La firma constituye una enmienda humana posterior a GATE-04, limitada al
bloque de firma del prólogo. La fecha oficial y esta enmienda quedan sometidas
a la comprobación final de GATE-05.

## Alcance del cambio

Se actualizaron exclusivamente la metadata de fecha, sus manifestaciones
públicas en el colofón y «Cómo citar», la firma del prólogo, el README, los
validadores y las expectativas de prueba directamente dependientes. No se
modificaron `project/`, la transcripción, la modernizada, la bibliografía, los
aparatos D/C/I/E/L, la cartografía ni la lógica F3.

Ficheros modificados:

- `README.md`;
- `publication/_quarto.yml`;
- `publication/meta/publication.yml`;
- `publication/content/00-preliminares/02-prologo.qmd`;
- `publication/content/06-aparatos/como-citar.qmd`;
- `publication/content/06-aparatos/colofon.qmd`;
- `publication/scripts/fix_rendered_links.py`;
- `publication/scripts/quality_audit.py`;
- `tests/test_hum_review_fix_01.py`;
- `tests/test_public_repo_readiness.py`;
- `tests/test_publication_hum01b.py`;
- `tests/test_publication_phase6a.py`;
- `tests/test_publication_pkg06.py`;
- `tests/test_publication_pkg09.py`;
- `docs/DATE_FINAL_01.md`;
- `docs/CHECKPOINT_REANUDACION_PREVIEW_FINAL.md`.

La comprobación de delta confirma:

- fecha exacta y firma anterior ausentes de las fuentes y artefactos públicos;
- ISBN ausente y no pendiente;
- 24 referencias bibliográficas y 111 anchors D/C/I/E/L preservados;
- `publication/generated/` y `publication/_book/` no versionados;
- árbol `project/` idéntico al aprobado.

## Validación

- Tests focales: `57 passed`.
- Suite completa, ejecutada una sola vez: `701 passed`, `0 failed`,
  `0 errors`.
- Preparación reproducible: `PREPARE_TOTAL = 2`.
- SHA-256 de `publication/generated/` tras ambas preparaciones:
  `e777ba39fc5781fd667265900760d2c58e02ef922e7f7022725a1c6c32904375`.
- Render completo HTML/PDF: PASS; la fecha española quedó comprobada en ambos
  formatos.
- Validadores canónico, de fuentes, publicación estática y renderizada,
  cartografía, enlaces, anchors, bibliografía y compilación Python: PASS.
- `git diff --check`: PASS.
- Revisión visual focal de portada, prólogo, «Cómo citar» y colofón en HTML y
  PDF: PASS.

## Candidata final fechada

### Web

- Documentos HTML: 40.
- Archivos, excluido el PDF: 120.
- Tamaño, excluido el PDF: 74.657.839 bytes.
- Manifest SHA-256:
  `ab3bfbd19dc14f183c754b7b0d1408bfa05f7498a3b1d132f9c725f5d723c874`.

### PDF

- Páginas: 360.
- Tamaño: 71.029.176 bytes.
- SHA-256:
  `a59a0029fb15f4e6bfae8bd2edd791a3889e4a6121a34072da755b2854f10bde`.

### Conjunto completo

- Archivos: 121.
- Tamaño: 145.687.015 bytes.
- Manifest SHA-256:
  `8038c72e1465da9dd72c9539f5a9939754a4c0e3dee51d20ae488ba9ba190d26`.

## Draft final no productivo

- Site ID: `1539a52a-d500-426f-9995-7db9c01e6d45`.
- Deploy ID: `6ae5ffeaa97b544ed057b110`.
- URL:
  <https://6ae5ffeaa97b544ed057b110--sorribos-santibanez-1752.netlify.app>.
- Creación técnica: `2026-10-31T14:49:14.361Z`.
- Estado: `ready`, manual, no productivo, sin build remoto y sin integración
  Git.

La verificación remota confirmó 121 archivos con las mismas rutas, tamaños y
huellas SHA-1; 40 HTML accesibles y con canonical correcto; PDF remoto idéntico
byte a byte; assets representativos idénticos; fecha, firma, colofón, repositorio,
Issues y correo correctos. Production continúa intacta y sin servir el libro.

## Continuación

- `GATE-05`: siguiente operación.
- `PKG-13`: no iniciado.
- Production: no publicada.
- Tag/release: no creados.

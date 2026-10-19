# E4 — Revisión final de la candidata previa al preview

**Estado:** `E4 PASS — CANDIDATA VIGENTE APTA PARA GATE-03`
**Fecha de validación:** 19 de octubre de 2026
**CANDIDATE_SOURCE_SHA:** `d073fd8711f9fa50705308c65fabea0a2fae0d29`
**Rama de evidencia:** `e4/rev-final-preview-r4-v1`

## Antecedentes

- El primer intento de E4 detectó fallos reales de validación, corregidos de
  forma focal mediante E4-FIX-01.
- E4-R2 fue un aborto operativo: Quarto validaba los capítulos generados antes
  de ejecutar el `pre-render`.
- E4-R3 fue un aborto operativo durante SVG→PDF: `rsvg-convert` existía, pero
  no estaba expuesto en el `PATH` efectivo.
- E4-R2 y E4-R3 no demostraron defectos de contenido de la candidata.
- E4-R4 es la ejecución integral definitiva documentada en este dossier.

## Procedimiento reproducible vigente

`preflight toolchain + rsvg smoke` → `clean generated` →
`prepare bootstrap` → `quarto render` → `pre-render prepare` → `suite` →
`validadores` → `revisión visual`.

`rsvg-convert` 2.58.0 es una dependencia efectiva del render PDF en el entorno
actual. En esta ejecución se extrajo temporalmente, fuera del checkout, el
paquete oficial Ubuntu `librsvg2-bin` 2.58.0 y se añadió su directorio `bin` al
inicio del `PATH` de la sesión, sin instalación en el sistema ni binarios en el
repositorio. Es el mismo mecanismo temporal empleado en PKG-10.

## Fuente, preflight y toolchain

- Base, `origin/main` y `origin/feature/quarto-book`:
  `d073fd8711f9fa50705308c65fabea0a2fae0d29`.
- Árbol `project/`: `a8ccb6d783e51aafb6493fed9791097d0a678086`.
- Manuscrito local verificado: 18 páginas, 5.038.575 bytes,
  SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`.
- Python 3.12.10; pytest 9.1.1; Quarto 1.7.31; LuaHBTeX 1.24.0 con
  TinyTeX 2026; Poppler 24.02.0; Chrome 142.0.7444.134;
  `rsvg-convert` 2.58.0.
- `PATH` relevante: binario temporal de `librsvg2-bin`, entorno `.venv` y
  TinyTeX, en ese orden; no se registran valores ajenos al toolchain.
- Smoke SVG→PDF: PASS; conversión con código 0, PDF temporal no vacío de una
  página y lectura correcta mediante `pdfinfo`. Los temporales se eliminaron.

## Preparación, render y suite

- Limpieza limitada a `publication/_book/` y `publication/generated/`; Git
  permaneció limpio.
- Bootstrap manual: PASS; 83 archivos generados; 78.446.231 bytes; 230,52 s.
- `GENERATED_BOOTSTRAP_HASH`:
  `e777ba39fc5781fd667265900760d2c58e02ef922e7f7022725a1c6c32904375`.
- Render único `quarto render publication`: HTML PASS, PDF PASS y post-render
  PASS; 560,88 s.
- El `pre-render` ejecutó la segunda y última preparación:
  `PREPARE_TOTAL = 2`.
- `GENERATED_PRERENDER_HASH`:
  `e777ba39fc5781fd667265900760d2c58e02ef922e7f7022725a1c6c32904375`.
- Las dos huellas son idénticas y coinciden con la referencia de E4-R3.
- Suite integral ejecutada una vez: `696 passed` en 40,84 s; 0 failed,
  0 errors, 0 skipped, 0 xfailed y 0 xpassed.
- Único aviso de composición: creación inicial de la base temporal de fuentes
  de LuaTeX. No afectó al resultado ni se repitió el render.

## Validadores y regresiones

PASS en todos los casos:

- coherencia del proyecto canónico;
- fuentes: 5 fuentes, 35 unidades, 40 respuestas modernizadas, 28 entradas de
  glosario, 111 entradas D/C/I/E/L y 20 cálculos;
- publicación estática y publicación renderizada, incluida la auditoría
  profunda de las 360 páginas PDF;
- cartografía `--check`;
- metadata, referencias, bibliografía y TOC;
- facsímil, transcripción, modernizada, glosario e índices;
- enlaces, anchors y retornos;
- compilación Python de plugins, scripts y tests;
- `quarto check` y `git diff --check`.

Las regresiones que motivaron E4-FIX-01 quedaron verificadas:

- colofón sin salto de jerarquía `h1`→`h3`;
- seis aparatos narrativos presentes;
- F3 conserva paleografía exacta y `reader_facing_source_text` en el aparato
  público;
- prólogo definitivo de HUM-01B preservado;
- capítulo 4 idéntico byte a byte a E3
  (`73ed35830ca2cc3c36b531da4d8bde47efa73686`), con SHA-256
  `7e2b1f203b5423d5ce0ce773ffb3cc112e37e07f2e5be337e52a80e7b2970e46`.

## Cobertura y producto

- facsímil: 18/18 páginas;
- unidades y relaciones: 35/35, con navegación bidireccional y sin anchors
  duplicados ni huérfanos;
- modernizada: 40/40 respuestas;
- modelos de cita: 7 familias y 11/11 objetos;
- D/C/I/E/L: 111 entradas únicas;
- bibliografía: 24 referencias activas y 24 registros BibTeX;
- índices: 9; glosario: 28 entradas; QA1: 9/9;
- TOC, concordancia, matrices y aparatos completos.

## Revisión visual y accesibilidad

La revisión HTML real se efectuó en escritorio (1440 × 1000) y viewport
estrecho de 390 px sobre portada, créditos, prólogo, introducción, capítulos 3,
5 y 13, facsímil, transcripción, modernizada, matriz, glosario, dos índices,
«Cómo citar», «Correcciones y contacto», bibliografía y colofón. Navegación,
sidebar, TOC, encabezados, tablas, imágenes, foco, reflow y responsive: PASS;
no hubo desbordamiento de página y las tablas anchas conservaron scroll local.

La revisión PDF cubrió portada, preliminares, índice general, comienzos de las
seis partes (pp. 29, 46, 101, 121, 224 y 249), cronología (p. 39), mapas local
y regional (pp. 40 y 47), diagrama económico (p. 95), capítulo 13 y tabla
ancha, facsímil (p. 103), transcripción (p. 122), modernizada (p. 225),
glosario (p. 250), concordancia/matriz e índices, «Cómo citar» (p. 318) y
colofón (pp. 359–360). Resultado: PASS, sin defectos bloqueantes.

Accesibilidad HTML:

- 40/40 documentos con un único `h1`, `lang="es"`, landmarks y jerarquía sin
  saltos;
- 57/57 imágenes con texto alternativo;
- 45/45 tablas semánticas o nombradas;
- 0 enlaces o controles sin nombre;
- navegación por teclado, foco visible de 3 px y reflow estrecho: PASS.

No se declara conformidad PDF/UA ni PDF/A.

## Metadata y residuos

Fuente y render confirman versión 1.0, año editorial 2026, idioma español,
URL canónica <https://sorribos-santibanez-1752.netlify.app/>, enlaces
`canonical`, repositorio público de GitHub, GitHub Issues y correo aprobado.
La fecha exacta sigue diferida a DATE-FINAL-01 y no existe ISBN.

No se hallaron residuos públicos impropios: `PLACEHOLDER`, URL o correo
pendientes, repositorio privado, «edición en desarrollo», rutas de usuario o
Windows, rutas `publication/content` o `publication/generated`, ni referencias
PKG/GATE dirigidas al lector. Los marcadores legítimos de los modelos de cita
se conservaron como tales.

## Huellas finales de la candidata

### Web

- HTML: 40 documentos.
- Archivos: 120, excluido el PDF.
- Tamaño: 74.657.296 bytes, excluido el PDF.
- SHA-256 del manifiesto agregado:
  `3748a882e2e5f43581cb01071895c6219d5008c3275f306818a47f1658166ef1`.

### PDF

- Archivo: `sorribos-santibanez-ordas-1752.pdf`.
- Páginas: 360.
- Tamaño: 71.028.386 bytes.
- SHA-256:
  `a00db79d7cbcec39c63f4b4d16a9c369a0eae4ab9c6c3d2d408c4d52171981f7`.

### Conjunto completo

- Archivos: 121.
- Tamaño: 145.685.682 bytes.
- SHA-256 del manifiesto agregado:
  `78e87218868d9e0a7ed36a6472385aae9b47411806d48830039aa25b9b52ebb3`.

Estas son las huellas que PKG-12 deberá comprobar antes del upload.
`publication/_book/` queda conservado localmente e ignorado.

## Integridad y Netlify

- `project/` y todas las fuentes versionadas del libro permanecen intactos.
- `publication/generated/` y `publication/_book/` siguen ignorados y ningún
  derivado está versionado.
- Site Netlify `sorribos-santibanez-1752`: 0 deploys, 0 drafts y production
  vacío. El HTTP 404 de prepublicación continúa siendo el estado esperado.
- No se ejecutaron deploy, integración, push, tag, release, GATE-03 ni PKG-12.

## Veredicto

`E4 PASS — CANDIDATA VIGENTE APTA PARA GATE-03`

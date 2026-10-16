# Candidata de publicación 1.0

> **Referencia histórica sustituida.** Esta candidata técnica de
> `49ab2e1b1a58ca9201efab54b42a3125de7326f8` queda conservada como baseline
> preeditorial. La candidata formal vigente se documenta en
> [PKG_10_CANDIDATA_1_0.md](./PKG_10_CANDIDATA_1_0.md).

**Fase:** 6A — candidata a publicación 1.0 y preview para aceptación editorial<br>
**Fecha de construcción:** 9 de octubre de 2026<br>
**Commit de candidata:** `49ab2e1b1a58ca9201efab54b42a3125de7326f8`<br>
**Estado:** técnicamente válida; preview remoto pendiente de decisión y configuración de proveedor

Este documento manifiesta la candidata técnica. No declara una edición 1.0
publicada, no sustituye la aceptación editorial humana y no autoriza la Fase 6B.

## Snapshot

| Elemento | Identificación |
|---|---|
| Rama de publicación | `feature/quarto-book` |
| Base de concurrencia de 6A | `c1d0499340da92a28feeb9d3e121c68322190b38` |
| Commit de candidata | `49ab2e1b1a58ca9201efab54b42a3125de7326f8` |
| Fuentes Git canónicas (`main`, `origin/main`) | `e81dc9239ac8dbabfe77168a50ef98c4d3b79170` |
| Árbol `project/` en `main` | `e32917763475ceebdfe7b54830e1fb43f6419dad` |
| Árbol `project/` en la candidata | `e32917763475ceebdfe7b54830e1fb43f6419dad` |
| Resultado | igualdad exacta; la publicación no modificó fuentes canónicas |

`publication/meta/publication.yml` usaba antes el snapshot de la auditoría de
Fase 0, `6b49be848c92c4772b37c46495135352821d50f8`. En 6A,
`base.git_commit` se actualizó a `e81dc9239ac8dbabfe77168a50ef98c4d3b79170`,
porque el contrato del campo es congelar el commit de fuentes canónicas vigente,
no el HEAD técnico de publicación. Este commit de `main` normalizó finales de
línea; las versiones y el contenido histórico permanecen sin cambios.

## Metadatos de edición

- `publication.version`: antes y después, `0.1.0-dev`.
- `publication.status`: antes y después, `development`.
- Título fijado: «Sorribos y Santibáñez de Ordás en 1752».
- Subtítulo fijado para la preview: «Edición en desarrollo»; debe confirmarse o
  sustituirse expresamente antes de 6B.
- Autoría, responsabilidad editorial, copyright, licencia, fecha/edición y URL
  canónica no están fijados. No son necesarios para esta preview local, pero
  requieren decisión humana antes de la publicación 1.0.
- ISBN no está fijado y no es requisito del pipeline web/PDF actual; cualquier
  decisión al respecto queda fuera de 6A.
- No se inventó ningún valor editorial ni se declaró estado `published`.

## Fuentes congeladas

| Fuente | Versión o snapshot |
|---|---|
| Edición Crítica | 3.6 |
| Estudio Histórico | 1.2 |
| Registro D/C/I/E/L | 1.2 |
| Edición modernizada | 1.3 |
| Glosario | blob Git `0df18f89e2f39f8d75279d06e6f1b0bfa77362fe` |

Manuscrito autoritativo externo:

- nombre: `sorrios_ensenada_orden_lectura_calidad_original.pdf`;
- tamaño: 5.038.575 bytes;
- páginas: 18;
- SHA-256: `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`;
- autoridad: Google Drive, solo lectura; la réplica verificada permanece fuera
  del checkout y no forma parte de la candidata pública.

## Reproducibilidad

Dos preparaciones completas consecutivas produjeron 75 archivos y 77.225.629
bytes con resultados idénticos. Los hashes corresponden a manifiestos
`sha256sum` ordenados:

| Grupo | Salidas | SHA-256 del manifiesto |
|---|---:|---|
| 4A | 19 | `b3e99b6c4d307e0d84842a906f85bb695eea00597b5e8ab576c58ebdfa884e2a` |
| 4B | 36 | `ccbc1db0e9549dc53af0bf9bb0b3f6539714a24b4d9300bc098c39da03a4ac3f` |
| 4C | 1 | `824b1a794da01ab8d50616d92f5733846b05eb03e21de22ac10da4fd29052260` |
| 4D | 4 | `bdeee6ff70d36a766da82ea838be2512872e0fcc407c55410fe527a52b5efae6` |
| 5A | 9 | `b9f32dfa454e5c812c8733cc1da46e49af8e7fab8e71e40f82b6fc784dddffcf` |
| Prototipo/regresiones | 6 | `31bd1932af1aeeba8bc6521fe06cd1df7839710b9d8ec2eb4173d4725cad9421` |
| Conjunto | 75 | `0f2a27a3294060552ee5dde8a9b4d61258e85fef049679f650e3d71465234da0` |

## Salidas de la candidata

### HTML

- directorio regenerable: `publication/_book/`;
- entrada: `publication/_book/index.html`;
- 30 documentos HTML en seis partes;
- 105 archivos públicos, 151.080.400 bytes incluido el PDF;
- bundle HTML y assets sin el PDF: 77.085.904 bytes;
- documentos HTML: 2.048.214 bytes;
- navegación, búsqueda, TOC, enlaces, anclas, imágenes, tablas, teclado, foco y
  reflow validados;
- no contiene QMD, Python, YAML, TOML, `.env`, rutas locales, credenciales,
  `project/`, manuscrito fuente ni PDF 0.6.

### PDF

- archivo: `publication/_book/sorribos-santibanez-ordas-1752.pdf`;
- páginas: 334;
- tamaño: 73.994.496 bytes;
- SHA-256: `f1eee2f465f554d3bf2b506d23a622967d1b4f1013ac657a774868e525688183`;
- versión PDF 1.7, tamaño letter, texto seleccionable, 14 variantes de fuente
  embebidas y 53 imágenes;
- `Tagged: no`; no se declara PDF/UA;
- el enlace de descarga HTML sirve exactamente estos bytes y conserva el mismo
  SHA-256.

## Validación

- diez pruebas focalizadas 6A: PASS;
- suite completa: 567 pruebas en PASS, sin `skip` ni `xfail`;
- colección: 567 identificadores; SHA-256
  `2707830a38956a186b7b4c5a377fadf59cfcd98894dafb48ed28df86d58f7fe7`;
- `check_sources.py`: PASS;
- dos reconstrucciones limpias y reproducibilidad: PASS;
- validador estático y `--rendered`: PASS;
- `quarto check`: PASS con Quarto 1.7.31 y TinyTeX 2026;
- render HTML, PDF y multiformato: PASS;
- enlaces, anclas, localizadores PDF, descarga y controles Poppler: PASS;
- controles heredados de accesibilidad básica de 5B: PASS;
- auditoría de seguridad del árbol público: PASS;
- `git diff --check`: PASS.

La geometría de las 334 páginas fue comprobada automáticamente. Además se
inspeccionaron portada, preliminares, comienzos de las seis partes, capítulos
1, 5 y 13, principio y final del facsímil, muestras facsimilares, principio,
medio y final de la transcripción, respuestas 17 y 40, los cuatro aparatos,
principio y final de los nueve índices y última página. No se observaron cortes,
colisiones, desbordes ni páginas corruptas. La salida HTML se inspeccionó en
escritorio y viewport estrecho.

Limitaciones conservadas: no se declara conformidad formal WCAG 2.1/2.2 AA,
PDF/UA ni PDF/A. Los mensajes de Jupyter ausente, D-Bus/GPU de Chrome y la
petición opcional de `favicon.ico` no afectan al libro ni a sus assets.

## Preview

Se verificó temporalmente una preview local en `http://127.0.0.1:4319/` mediante
un servidor de `publication/_book/`; portada, muestra de capítulos, facsímil,
transcripción, modernizada, aparatos, índices, búsqueda y PDF respondieron `200`.
El servidor se cerró al terminar. Para repetirla tras reconstruir la candidata:

```sh
python -m http.server 4319 --bind 127.0.0.1 --directory publication/_book
```

No existe una decisión o configuración inequívoca de preview remoto:

- Netlify es la preferencia del Plan Maestro, pero requiere aprobación del
  proveedor, conexión autorizada al repositorio privado y una estrategia segura
  para publicar el `_book/` validado sin exponer el manuscrito fuente;
- GitHub Pages es la alternativa y requiere decisión explícita, configuración de
  Pages/workflow y la misma estrategia segura de artefacto;
- no existe `netlify.toml`, Pages, workflow de despliegue ni CLI de Netlify;
- no se hizo push, despliegue, tag, release, merge ni publicación definitiva.

La siguiente decisión humana es elegir y autorizar el proveedor y su
configuración de preview. Después deberá verificarse la URL real y solicitarse
la aceptación editorial explícita. Solo entonces podrá plantearse 6B.

`CANDIDATA 1.0 LISTA — PENDIENTE DECISIÓN/CONFIGURACIÓN DE PROVEEDOR DE PREVIEW`

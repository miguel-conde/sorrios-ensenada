# Cierre de PKG-11 — Validación integral de la candidata 1.0

**Estado:** `COMPLETADO E INTEGRADO`<br>
**Commit integrado:** `526304867e2bba16b745f3477fb63d44be49bd19`<br>
**Commit fuente de la candidata:** `a666e878eb6672bee337ac4a2b6f0410ae8e0872`<br>
**Commit PKG-10:** `d02b9fbf0e17625f87d19ebe12bf36c1ce633c80`

PKG-11 queda revisado e integrado por avance rápido en
`feature/quarto-book`. La candidata 1.0 está validada integralmente, con suite
completa de `678 passed`, validadores en PASS y cero defectos bloqueantes.

## Reproducibilidad

- HTML: 39 documentos, 117 archivos y 74.567.798 bytes. El hash reconstruido
  `86f32e8b48e6ee46ebd30feb0d96bc85439f034485cbbd6a00db3ebd7b55b9d9`
  difiere del de PKG-10 únicamente por el orden no semántico de atributos.
- PDF: 355 páginas y 71.020.397 bytes. El hash reconstruido
  `8862d2e3020f23b57e79b7331a7d6f5ba69d829455e5076f8058d2701020c1fb`
  difiere únicamente por timestamps e IDs internos.

Texto, imágenes, fuentes, paginación, rasterización, estructura y contenido
visible son equivalentes. Las dos diferencias quedan registradas como
observaciones técnicas inocuas, no como defectos.

## Integridad y siguiente operación

`project/` y las fuentes de `publication/` permanecen intactos. Los derivados
siguen ignorados y no se versionaron. El prólogo, la fecha exacta, la URL
canónica y el ISBN conservan sus diferimientos autorizados.

PKG-12 queda técnicamente habilitado, pero antes de iniciarlo se recomienda
cerrar los inputs editoriales humanos finales: prólogo y revisión de la
declaración sobre IA. No hubo push, tag, release ni inicio de PKG-12 o Fase 6B.

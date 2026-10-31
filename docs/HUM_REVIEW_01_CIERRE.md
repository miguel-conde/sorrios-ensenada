# Cierre de HUM-REVIEW-01

## Estado

`HUM-REVIEW-FIX-01 PASS — CORRECCIONES DE LA REVISIÓN HUMANA INCORPORADAS`

La primera preview de PKG-12 fue revisada íntegramente por el autor. Las
incidencias comunicadas se corrigieron y la nueva candidata quedó validada
técnicamente. No se realizó ningún despliegue en esta operación.

## Correcciones aplicadas

- El comienzo de la frase señalada en el prólogo se cambió de «La primera vez
  que conocí Sorríos» a «Cuando conocí Sorríos», sin alterar ningún otro pasaje.
- La etiqueta pública de autoría se fijó como «Autor» mediante el override
  localizado de idioma de Quarto; no se editaron derivados.
- El README público se reorganizó para explicar la obra, el alcance y la
  estructura del repositorio, la reproducción de la publicación, las
  licencias, la cita, el contacto y las exclusiones de distribución.
- La metadata dejó de considerar el ISBN como pendiente.

## Decisiones editoriales

- El consentimiento de las personas identificables mencionadas en el prólogo
  está confirmado; sus nombres se conservan.
- No se solicitará ISBN para la edición v1.0 no comercial. Solo se reconsiderará
  si existe una futura edición destinada a un circuito comercial.
- La fecha exacta de publicación permanece pendiente y se fijará exclusivamente
  en `DATE-FINAL-01`, después de GATE-04.

## Validación

- Tests focales: `406 passed`; comprobación focal posterior del contrato
  público: `11 passed`.
- Suite integral final: `701 passed`, `0 failed`, `0 errors`.
- Preparación desde cero: `PREPARE_TOTAL = 2`; las huellas de
  `publication/generated/` tras el bootstrap y tras el pre-render coincidieron
  en `e777ba39fc5781fd667265900760d2c58e02ef922e7f7022725a1c6c32904375`.
- Render completo Quarto: PASS.
- Validadores canónico, de fuentes, publicación estática y renderizada,
  cartografía y compilación Python: PASS.
- Bibliografía: 24 registros; D/C/I/E/L: 111 anchors únicos.
- Revisión visual focal HTML de escritorio y viewport estrecho, y PDF de
  portada, créditos y prólogo: PASS. La etiqueta «Autor/a» no aparece y la
  corrección del prólogo se compone correctamente.

## Artefactos de la nueva candidata

### Web

- Documentos HTML: 40.
- Archivos, excluido el PDF: 120.
- Tamaño, excluido el PDF: 74.657.270 bytes.
- Manifest SHA-256:
  `2e2eb284c7539647349c072f0262f04a8da334e37720181009924c99600bf4cd`.

### PDF

- Páginas: 360.
- Tamaño: 71.028.364 bytes.
- SHA-256:
  `7d0a63e85329951ec4cf1f5e747f23cfa41e062d0b929d2a128dc52354c876d2`.

## Integridad y continuación

- `project/` permanece idéntico a la base autorizada.
- `publication/generated/` y `publication/_book/` siguen sin versionarse.
- No se modificaron el manuscrito, la transcripción, la modernizada, los
  registros D/C/I/E/L, la bibliografía, la cartografía ni la lógica F3.
- `PKG-12-R2` es la siguiente operación y deberá desplegar exactamente esta
  candidata corregida.
- GATE-04, `DATE-FINAL-01`, GATE-05 y PKG-13 permanecen pendientes.

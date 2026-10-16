# GATE-02 — Implementación 1.0 aceptada

## 1. Decisión

`GATE-02 = PASS`

La evaluación se realizó el 16 de octubre de 2026 sobre
`feature/quarto-book`, con HEAD
`3eda91015802928eca0ec919391986c08d52dbbc`, árbol limpio y PKG-06–PKG-09
integrados. No se inició PKG-10 ni se modificaron `project/` o `publication/`.

## 2. Contrato literal de la puerta

| Criterio GATE-02 | Evidencia | Estado | Bloqueante | Observaciones |
|---|---|---|---|---|
| PKG-06–09 integrados | Los commits `6040015`, `93e745b`, `c38bb87` y `25fb7dc` son ancestros de HEAD; cierres y dossiers de los cuatro paquetes | PASS | No | Preliminares, aparato visual, fuentes/aparatos e identidad final están incorporados. |
| No quedan datos obligatorios sin resolver | DAT-001–008 y DAT-AI-01 resueltos; año 2026 fijado; fecha exacta y URL con momento posterior; ISBN no obligatorio; decisión humana vigente sobre el prólogo | PASS — diferimiento previsto | No | Los diferimientos no autorizan inventar valores y no impiden PKG-10. |
| No quedan cambios canónicos parcheados en `publication/` | PKG-08 resincronizó el estado canónico de `a162fad`; `project/` es idéntico entre la base de PKG-06–09 y el HEAD evaluado | PASS | No | La propagación está documentada y separada de la autoridad canónica. |
| El alcance coincide con `ALCANCE_APROBADO_V1_0.md` | Dossiers PKG-06–09, decisiones DEC-020–024, exclusiones preservadas y ausencia de PKG-10 | PASS | No | No se añadieron investigación, recursos excluidos ni cambios de alcance. |

## 3. Evidencia por paquete

| Paquete | Evidencia aceptada | Resultado |
|---|---|---|
| PKG-06 | Preliminares P3, landing HTML, portada PDF, créditos, introducción, rutas, convenciones y cierres; focal `14 passed`, suite `661 passed`; HTML 38 documentos; PDF 349 páginas | PASS |
| PKG-07 | Cronología, diagrama económico y dos mapas aprobados; DEC-020–022 implementadas y DEC-023–024 preservadas; focal `28 passed`, suite `669 passed`; revisión visual APTO | PASS |
| PKG-08 | Resincronización canónica; 24 fuentes activas y 24 registros BibTeX; CIT-B/C; 111 anchors D/C/I/E/L; QA1 9/9; cita 11/11; TOP-006 solo matriz; suite `650 passed` | PASS |
| PKG-09 | Identidad, metadatos, créditos, derechos, licencia, colofón y declaración de herramientas/IA; focal `40 passed`, suite `678 passed`; HTML 39 documentos; PDF 355 páginas | PASS |

Los renders y suites anteriores corresponden a los SHA exactos ya aceptados y
se reutilizan como evidencia. Esta evaluación documental no los repite.

## 4. Diferimientos evaluados

| Elemento | Estado | Tratamiento |
|---|---|---|
| Prólogo personal | PASS — diferimiento previsto | La decisión humana vigente permite conservar en esta fase el **PLACEHOLDER CONTROLADO PENDIENTE DE REDACCIÓN PERSONAL**. Miguel Conde de Simón lo sustituirá en una operación posterior; el texto definitivo sigue siendo obligatorio antes del cierre/release de 1.0. La indicación histórica de sustituirlo antes de GATE-02 queda aclarada por esta decisión expresa y no bloquea la puerta. |
| Fecha exacta | PASS — diferimiento previsto | El año visible es 2026; el día y mes se fijarán en el release y no se inventan. |
| URL canónica | PASS — diferimiento previsto | Se fijará cuando exista el destino de publicación autorizado, dentro de PKG-12/PKG-13. |
| ISBN | PASS — diferimiento previsto | No es requisito de 1.0 y permanece ausente mientras no exista. |

## 5. Integridad y bloqueos

- `project/` permanece intacto a través de PKG-06–PKG-09.
- `publication/generated/`, `_book/`, PDF, HTML y capturas permanecen sin
  versionar.
- Los controles no registran incidencias ni tareas bloqueantes abiertas y
  `operation.status` es `clean`.
- PKG-10 no está iniciado; tampoco se adelantan PKG-11, PKG-12, PKG-13 ni la
  Fase 6B.
- No se ejecutaron renders, suite completa ni revisión visual durante esta
  evaluación.

## 6. Consecuencia

Los cuatro criterios contractuales están satisfechos sin fórmula condicional.
`GATE-02 = PASS`; PKG-06–PKG-09 quedan aceptados y PKG-10 queda habilitado,
pero no iniciado, para regenerar de forma reproducible la candidata 1.0.

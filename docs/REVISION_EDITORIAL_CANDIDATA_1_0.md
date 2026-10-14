# Revisión editorial consolidada de la candidata 1.0

**Fecha:** 12 de octubre de 2026<br>
**Fase:** 6A — ejecución del alcance 1.0<br>
**Estado:** DEC-001–DEC-034 cerradas; PKG-01–05, CR-V1-001 e INC-BIB-001/002 integrados; `GATE-01 = PASS`; PKG-06–PKG-09 habilitados y no iniciados; candidata formal, presentación editorial, citas y bibliografía pendientes<br>
**Cierre humano:** [CIERRE_ALCANCE_V1_0.md](./CIERRE_ALCANCE_V1_0.md)<br>
**Contrato de alcance:** [ALCANCE_APROBADO_V1_0.md](./ALCANCE_APROBADO_V1_0.md)<br>
**Plan operativo:** [PLAN_EJECUCION_V1_0.md](./PLAN_EJECUCION_V1_0.md)

## 1. Objeto

Este documento conserva las 26 observaciones REV de la candidata y registra su
decisión humana final. Las Auditorías A/B/C aportan el diagnóstico; las
decisiones `DEC-001`–`DEC-034` fijan el alcance. Un estado resuelto en fuente
canónica no significa que el cambio esté ya propagado a PDF o HTML.

La composición 0.6 continúa siendo referencia editorial, no autoridad textual o
histórica. `project/` mantiene la autoridad canónica. CR-V1-001 sincronizó
técnicamente el Glosario GH-B de 28 entradas con la publicación y
`publication/` contiene ya los assets cartográficos de PKG-03, pero la candidata
no se ha regenerado: el contexto histórico y los mapas no están integrados en la
presentación final HTML/PDF.

## 2. Estados de alcance

- **INCLUIR EN 1.0:** implementación obligatoria.
- **INCLUIR EN 1.0 CON PRETRABAJO:** forma parte de 1.0, pero depende de inputs,
  verificación, operación canónica o assets aprobados.
- **RESUELTA E IMPLEMENTADA:** decisión humana e implementación en la rama de
  publicación completadas; candidata formal pendiente de regeneración.
- **DIFERIR A 1.1+:** no bloquea 1.0.
- **NO INCORPORAR:** exclusión deliberada.

## 3. Matriz REV-001–REV-026 cerrada

| ID | Área | Diagnóstico consolidado | Decisión humana final | Trabajo pendiente / condición |
|---|---|---|---|---|
| REV-001 | Identidad, créditos y metadatos | La candidata conserva identidad de desarrollo y carece de datos humanos y legales finales. | **INCLUIR EN 1.0 CON PRETRABAJO** — DEC-007–009 y DEC-015. | DAT-001–010 según PKG-00/09; no inventar valores. |
| REV-002 | Cartografía | PKG-03 ha preparado y validado los mapas regional y local contemporáneos; no se reconstruye el término histórico. | **INCLUIR EN 1.0 CON PRETRABAJO** — DEC-021; PKG-03 completado e integrado. | **ASSET PREPARADO / INTEGRACIÓN EN PUBLICACIÓN PENDIENTE**: insertar y validar ambos mapas en PKG-07; todavía no aparecen en PDF/HTML. |
| REV-003 | Fuentes y bibliografía | Las 16 referencias incompletas fueron tratadas en PKG-02: 14 verificadas con ajustes, una parcial y una incompatibilidad de uso; `INC-BIB-001` e `INC-BIB-002` están cerradas canónicamente y `references.bib` continúa vacío. | **INCLUIR EN 1.0 CON PRETRABAJO** — DEC-025–028 y DEC-032; verificación y resolución canónica completadas, propagación editorial pendiente. | PKG-08 debe propagar la resolución a CIT-B/C, bibliografía visible, citas próximas, aparatos y TOP-006 solo en matriz. |
| REV-004 | Aparatos narrativos | Nueve QA1, historia intelectual y once objetos citables están diagnosticados. | **INCLUIR EN 1.0 CON PRETRABAJO** — DEC-029–031. | QA1 compacto; historia breve; modelos por familias; datos finales de identidad/cita. |
| REV-005 | Preliminares y orientación | P3, introducción y convenciones están decididos; la cronología es viable con datos internos. | **INCLUIR EN 1.0** — DEC-001, DEC-003–005 y DEC-020. | Implementación en PKG-06/07. |
| REV-006 | D/C/I/E/L | La cadena existe, pero las marcas no enlazan de forma homogénea con la matriz. | **INCLUIR EN 1.0** — DEC-033. | Enlaces, retornos y política coherente sin saturación. |
| REV-007 | Colofón | Está aprobado y depende de identidad, roles, fecha, URL, versión y licencia. | **INCLUIR EN 1.0 CON PRETRABAJO** — DEC-010. | DAT y PKG-09. |
| REV-008 | Accesibilidad formal | El PDF no está etiquetado ni validado como PDF/UA o PDF/A; no es regresión frente a 0.6. | **DIFERIR A 1.1+**. | Mantener accesibilidad básica y no declarar conformidad formal. |
| REV-009 | Formulaciones superadas | 0.6 contiene afirmaciones demasiado fuertes ya corregidas por Quarto. | **NO INCORPORAR**. | Conservar pruebas de no regresión. |
| REV-010 | Facsímil antiguo | El modelo exclusivo de 35 recortes pierde la serie de 18 páginas completas. | **NO INCORPORAR**. | REV-016 decide la presentación futura mediante prototipo. |
| REV-011 | Índices antiguos | Eran provisionales y carecían de localizadores finales. | **NO INCORPORAR**. | Mantener arquitectura actual y corregir REV-025. |
| REV-012 | Formato/diseño 0.6 | No hay base para copiar A4, paginación u ornamentación. | **NO INCORPORAR**. | Una futura edición impresa tendría alcance propio. |
| REV-013 | Prólogo personal | Prólogo firmado de 900–1.500 palabras después de créditos. | **INCLUIR EN 1.0 CON PRETRABAJO** — DEC-002–003. | Texto del usuario y revisión que preserve su voz. |
| REV-014 | Introducción y guía | Dos rutas y convenciones compactas sin sustituir el capítulo 4. | **INCLUIR EN 1.0** — DEC-004–005 y DEC-011. | Redacción e implementación en PKG-06. |
| REV-015 | Apertura editorial | Landing HTML, portada PDF y preliminares separados. | **INCLUIR EN 1.0** — DEC-006–007. | Implementación coordinada con REV-001/005/013/014/022. |
| REV-016 | Duplicación funcional | El prototipo confirmó que F3 reduce satisfactoriamente la duplicación PDF sin perder orientación o comprobación. | **RESUELTA E IMPLEMENTADA** — DEC-012; H1–H5 y P1–P8 en Sí. | Prototipo `7c6d687`, aprobación y despliegue global `61a5098` integrados. La implementación está en la rama de publicación; la candidata formal se regenerará posteriormente. |
| REV-017 | Macroorden | Se conserva contexto → estudio → documento con rutas histórica y documental. | **INCLUIR EN 1.0** — DEC-011. | Implementar rutas; no reordenar. |
| REV-018 | Sidebar HTML | La navegación inicial estaba demasiado desplegada. | **RESUELTA E IMPLEMENTADA** — DEC-014. | PKG-05 deja abierta solo la parte activa y valida teclado, foco, escritorio y móvil. |
| REV-019 | Cierres de capítulos | Se exige función conclusiva común con títulos específicos. | **INCLUIR EN 1.0** — DEC-013. | Revisión de capítulos 5–13. |
| REV-020 | Glosario y contexto | A: G0 8, G1 7, G2 0, G3 4, G4 3; GH-B selectivo. | **RESUELTO EN FUENTE CANÓNICA Y SINCRONIZADO TÉCNICAMENTE** — DEC-016–019; commits `9ae4d1fd46d9f2d7bca685de861bff2a554a7a39` y `c07bc011a42952f64622e3f78e8d759ad361cf29`. | **PRESENTACIÓN EDITORIAL PENDIENTE**: el derivado contiene 28 entradas y PKG-05 resolvió su orden alfabético, pero `Contexto histórico` aún no se presenta y la candidata formal no se ha regenerado. |
| REV-021 | Aparato visual | B: cronología, dos mapas y diagrama aportan valor; los dos mapas están ya preparados y validados como assets. | **INCLUIR EN 1.0 CON PRETRABAJO** — DEC-020–024 y DEC-029. | Mapas: asset preparado en PKG-03 e integración pendiente en PKG-07; cronología/diagrama pendientes; diferir Concejo/municipio y no producir término histórico. |
| REV-022 | Identidad de desarrollo | `0.1.0-dev`, `development` y «Edición en desarrollo» no pueden llegar a 1.0. | **INCLUIR EN 1.0** — DEC-006–007. | Retirar al integrar la nueva candidata. |
| REV-023 | TOC PDF | Numeraciones largas se pegaban a los títulos. | **RESUELTA E IMPLEMENTADA**. | PKG-05 fija la caja numérica y valida las páginas 2–19. |
| REV-024 | Orden del glosario | La salida no respetaba el orden alfabético previsto. | **RESUELTA E IMPLEMENTADA**. | PKG-05 ordena 28/28 lemas mediante clave española determinista sin alterar `project/`. |
| REV-025 | Índices PDF | Las entradas carecían de separación visual suficiente. | **RESUELTA E IMPLEMENTADA**. | PKG-05 valida separación, cortes y localizadores en los nueve índices. |
| REV-026 | Peso PDF/web | El tamaño procede principalmente del manuscrito y no es por sí solo una regresión. | **RESUELTA CON OPTIMIZACIÓN E IMPLEMENTADA** — DEC-034. | Compresión PNG sin pérdida de 35 recortes: PDF −4,3679 % y web −4,1925 % en A/B comparable. |

## 4. Recuento de alcance

| Estado | REV |
|---|---:|
| INCLUIR EN 1.0 | 7 |
| INCLUIR EN 1.0 CON PRETRABAJO | 8 |
| RESUELTA E IMPLEMENTADA | 6 |
| DIFERIR A 1.1+ | 1 |
| NO INCORPORAR | 4 |
| **Total** | **26** |

## 5. Condiciones que continúan abiertas sin reabrir decisiones

- DAT-001–DAT-010: valores humanos y editoriales concretos.
- Regeneración posterior de la candidata formal para incorporar las
  implementaciones F3 y PKG-05 ya integradas en la rama de publicación.
- Propagación en PKG-08 de `INC-BIB-001` e `INC-BIB-002`, ya cerradas
  canónicamente, sin sustituir fuentes ni parchear la autoridad desde
  `publication/`.
- Integración narrativa y multiformato de los assets cartográficos en PKG-07;
  no marcarlos como presentes en la candidata antes de ese paquete.
- PKG-04 está completado e integrado: prototipo, decisión `F3-APROBAR` y
  despliegue 18/18 páginas y 35/35 unidades. La candidata formal todavía no se
  ha regenerado.

Estas condiciones determinan cómo ejecutar decisiones ya cerradas; no vuelven a
convertirlas en `PENDIENTE`.

## 6. Backlog y exclusiones

El backlog 1.1+ y la lista `NO INCORPORAR` se mantienen únicamente en
[ALCANCE_APROBADO_V1_0.md](./ALCANCE_APROBADO_V1_0.md) como contrato de alcance.
REV-023, REV-024 y REV-025 no pueden trasladarse al backlog.

## 7. Regla de autoridad

Una modificación histórica o del glosario canónico entra primero por `project/`
mediante una operación separada. PKG-06–PKG-09 no pueden parchear fuentes
canónicas desde `publication/`. La verificación bibliográfica no equivale a
investigación histórica y la cartografía de orientación no equivale a
reconstrucción geográfica histórica.

## 8. Tag e implementación

No se crea tag en 6A. La candidata técnica
`49ab2e1b1a58ca9201efab54b42a3125de7326f8` se conserva como baseline
pre-PKG-01 y no está sincronizada con la fuente canónica actual. REV-020 está
resuelta en la fuente y sincronizada en el flujo técnico, pero su presentación
editorial y la regeneración de la candidata permanecen pendientes. REV-024 y
las restantes correcciones de PKG-05 están implementadas en la rama, igual que
F3, pero no forman aún una nueva candidata formal. El tag solo puede aparecer en PKG-13, después de
candidata nueva, validación, preview, aceptación humana y autorización explícita
de Fase 6B.

**GATE-01 = PASS. PKG-06–PKG-09 HABILITADOS Y NO INICIADOS. GATE-02 = PENDIENTE.**

**SIGUIENTE PASO RECOMENDADO: PKG-08, para propagar el nuevo estado canónico y restaurar la sincronización de `publication/`.**

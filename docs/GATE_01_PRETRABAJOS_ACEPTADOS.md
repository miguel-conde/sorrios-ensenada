# GATE-01 — Pretrabajos aceptados

## 1. Fecha

14 de octubre de 2026.

## 2. Base

- Rama evaluada: `feature/quarto-book`.
- HEAD evaluado: `9678856cff35d7cd2398a74590429180ef969bcc`.
- Upstream comprobado tras `fetch`: `origin/feature/quarto-book` en
  `d4153c60489f4df24cdadf75d7740ec85b9406dd`.
- Divergencia inicial: dos commits por delante y cero por detrás.
- Árbol de trabajo inicial: limpio.

## 3. Contrato de la puerta

La evaluación aplica exclusivamente los ocho criterios de
`GATE-01 — Pretrabajos aceptados` del Plan de ejecución:

1. PKG-01 canónico validado.
2. PKG-02 integrado e `INC-BIB-001`/`INC-BIB-002` cerradas antes de aceptar
   GATE-01 y de implementar la correspondencia final en PKG-08.
3. Mapas de PKG-03 aceptados y licenciados.
4. CR-V1-001 cerrada e integrada, con su validación en PASS y PKG-04
   desbloqueado.
5. F3 decidido humanamente, desplegado globalmente e integrado.
6. REV-023–025 con solución comprobada.
7. Resultado de peso documentado.
8. Inputs disponibles de PKG-00 revisados.

| Criterio GATE-01 | Evidencia | Estado | Bloqueante | Observaciones |
|---|---|---|---|---|
| PKG-01 canónico validado | Commit `9ae4d1f`; 28 entradas; siete G1 mejoradas; seis altas; validador y 32 pruebas en PASS | PASS | No | `establecimiento del suelo` y `arenta` fueron aceptadas en DEC-018 e incorporadas tras superar los cuatro criterios canónicos. |
| PKG-02 e incidencias | Commit bibliográfico `9dbc0f8`; resolución canónica `a162fad`; dossier de cierre | PASS | No | Las 16/16 referencias conservan su resultado histórico; ambas incidencias están cerradas canónicamente. |
| Mapas PKG-03 | Commit `4d0210f`; dos SVG APTO; licencias, atribuciones, accesibilidad y hashes verificados | PASS — diferimiento previsto por contrato | No | La inserción narrativa y multiformato corresponde a PKG-07. |
| CR-V1-001 | Commit `c07bc01`; parser GH-B compatible; suite en PASS al cierre; PKG-04 ejecutado después | PASS | No | Los no-PASS actuales nacen de la operación canónica posterior y pertenecen a PKG-08, no reabren la CR. |
| F3 | `F3-APROBAR`; H1–H5 y P1–P8 en Sí; commits `7c6d687` y `61a5098` | PASS | No | Despliegue 18/18 páginas, 35/35 unidades e integración comprobados. |
| REV-023–025 | Cierre PKG-05, commit `0be55e6`; TOC, glosario e índices verificados | PASS | No | REV-018/DEC-014 y REV-026 quedaron también resueltas. |
| Resultado de peso | A/B de 333 páginas; PDF −4,3679 %; web −4,1925 %; compresión lossless reproducible | PASS | No | El contrato no establece un umbral de megabytes. |
| Inputs disponibles PKG-00 | DAT-001–008 y DAT-AI-01 resueltos; diferimientos inventariados | PASS — diferimiento previsto por contrato | No | DAT-009, DAT-010, prólogo y cierres legales tienen paquete o momento posterior explícito. |

GATE-01 no exige candidata formal, publicación totalmente sincronizada,
bibliografía final, mapas insertados, preliminares terminados ni suite de
release en PASS. Esas condiciones pertenecen a PKG-06–PKG-11 y a GATE-02/03.

## 4. PKG-00

Autoría, roles, responsabilidades de transcripción y modernización, identidad
del proyecto, copyright del contenido original, licencia CC BY 4.0 y política
de IA están resueltos. El único participante humano es Miguel Conde de Simón.

Los siguientes diferimientos están expresamente autorizados y tienen momento
posterior: valor final de DAT-009; DAT-010; texto definitivo del prólogo;
agradecimientos eventuales; nota de derechos por componentes; y asuntos
`LEGAL-PENDIENTE`. Ninguno es obligatorio antes de GATE-01.

Resultado: `PKG-00: PASS PARA GATE-01`.

## 5. PKG-01

El commit canónico `9ae4d1fd46d9f2d7bca685de861bff2a554a7a39`
está integrado. El Glosario contiene 28 entradas, las siete G1 fueron mejoradas
y se incorporaron seis altas. `CIERRE_ALCANCE_V1_0.md` registra DEC-018 y los
cuatro criterios de aceptación de `establecimiento del suelo` y `arenta`;
`CIERRE_PKG_01_GLOSARIO_CANONICO.md` documenta que ambas fueron evaluadas e
incorporadas. No se investigó G3. CR-V1-001 está cerrada e integrada.

Resultado: `PKG-01: PASS`.

## 6. PKG-02

Las 16 referencias fueron tratadas: catorce verificadas con ajustes, una en
verificación parcial y una con incompatibilidad de uso. El cierre original con
incidencias abiertas se conserva como hecho histórico; BIB-012 y BIB-015
mantienen sus diagnósticos.

### INC-BIB-001

R29 y `TRA-005` permanecen intactas; `TRA-006` fue retirada y el Estudio y el
Glosario dejaron de atribuir el paralelo E/I no demostrado.

Estado: `CERRADA CANÓNICAMENTE`.

### INC-BIB-002

R21 y `DEM-001` permanecen intactas; `DEM-005` se restringió al contexto
realmente respaldado por BIB-015 y quedó separado del dato local D.

Estado: `CERRADA CANÓNICAMENTE`.

### Propagación PKG-08

La resolución canónica y la propagación editorial son operaciones distintas.
El plan asigna a PKG-08 los capítulos 6, 11 y 13, `references.bib`, citas,
bibliografía, provenance, matriz, Glosario generado y validadores asociados.
También declara que esa propagación condiciona PKG-08, no la evaluación de
GATE-01.

`PROPAGACIÓN EDITORIAL: DIFERIMIENTO PREVISTO POR CONTRATO — PKG-08`.

Resultado: `PKG-02: PASS PARA GATE-01`.

## 7. PKG-03

Los mapas regional y local tienen veredicto APTO. Sus bases BDLJE, NGBE e
IGR_HIDROGRAFIA, licencias, atribuciones, redistribución, accesibilidad,
carácter contemporáneo, generador offline y hashes están documentados. La
inserción en capítulos y salidas pertenece expresamente a PKG-07.

Resultado: `PKG-03: PASS PARA GATE-01`.

## 8. PKG-04

El prototipo fue aprobado humanamente mediante `F3-APROBAR`: H1–H5 y P1–P8
obtuvieron Sí. El modelo se desplegó e integró sobre 18/18 páginas, 35/35
unidades y 35/35 relaciones, con fidelidad, navegación y reproducibilidad
verificadas.

Resultado: `PKG-04: PASS`.

## 9. PKG-05

REV-023, REV-024, REV-025 y REV-018/DEC-014 están resueltas. REV-026/DEC-034
acepta compresión PNG sin pérdida. El A/B conserva 333 páginas en ambos lados:
PDF de 74.035.908 a 70.802.128 bytes y web de 77.144.851 a 73.910.522 bytes.
La diferencia histórica 341→333 se explica por `samepage` frente a `minipage`,
no por pérdida de contenido. Píxeles, paleografía, texto, destinos y
localizadores se preservan, y dos preparaciones fueron reproducibles.

Resultado: `PKG-05: PASS` y `PESO/DEC-034: PASS`.

## 10. Inputs humanos

Todos los inputs actualmente disponibles han sido revisados. No hay un input
faltante que el contrato exija antes de GATE-01. Los valores de publicación,
prólogo, agradecimientos y cierres legales que faltan tienen diferimiento
explícito y se resolverán en PKG-06, PKG-09, PKG-12 o PKG-13 según su función.

## 11. Suite general y desincronización

Resultado real sobre el HEAD evaluado:

- 585 pruebas superadas;
- nueve fallos;
- 36 errores.

Clasificación exhaustiva:

1. tres fallos de Fase 4D por el blob anterior del Glosario;
2. un fallo de Fase 6A porque la candidata congela el snapshot canónico
   anterior;
3. tres fallos de PKG-05 que dependen del mismo blob y no alcanzan la
   generación del Glosario;
4. dos fallos del prototipo por `TRA-006` todavía presente en los capítulos 11
   y 13;
5. 36 errores de Fase 4D por fixtures que encuentran el provenance anterior o
   el parser todavía fijado al Registro 1.2.

No aparece ningún fallo canónico, histórico nuevo, de cálculo, F3,
cartografía, estructura o pérdida de datos. Los fallos nominalmente situados en
PKG-05 no constituyen una regresión de sus correcciones: se detienen antes por
el blob canónico deliberadamente no propagado.

Respuesta a la pregunta decisiva:
`DESINCRONIZACIÓN CONTROLADA PREVISTA`.

La suite actual es compatible con GATE-01 porque las causas están identificadas
una a una, el inventario de propagación existe, todas pertenecen al alcance
explícito de PKG-08 y el plan no exige resolverlas antes de esta puerta.

## 12. Integridad canónica

- Validador canónico: PASS (`VALID: GitHub workspace v2 coherent`).
- Pruebas canónicas: 32 superadas.
- Registro/Estudio: 131 IDs definidos, 126 IDs canónicos citados y cero
  referencias canónicas ausentes.
- Tablas Markdown, referencias internas y `git diff --check`: PASS.
- Edición Crítica, R21, R29 y controles YAML: blobs idénticos a la base previa
  a la resolución de incidencias.
- `CAL-001`–`CAL-020`: 20 filas, idénticas a la base.
- Manuscrito operativo: SHA-256
  `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`,
  5.038.575 bytes y 18 páginas, coincidente con `proyecto.yaml`.
- `operation.status`: `clean`.

## 13. Riesgos/deudas controladas

- Propagación canonical → publication: PKG-08.
- `references.bib` vacío, citas y bibliografía: PKG-08.
- `Contexto histórico` todavía no presentado: PKG-08.
- Mapas todavía no insertados: PKG-07.
- Preliminares, prólogo y arquitectura: PKG-06.
- Identidad y metadatos finales: PKG-09, sujetos a sus DAT.
- Nueva candidata formal: PKG-10.
- Diferimientos de PKG-00: paquetes y puertas posteriores ya asignados.

Son trabajos posteriores del DAG y no criterios incumplidos de GATE-01.

## 14. Decisión

`GATE-01 = PASS`

Todos los criterios contractuales están satisfechos. No se aplica una fórmula
condicional y no se declara completado ningún paquete posterior.

## 15. Consecuencias

- PKG-06: habilitado, no iniciado.
- PKG-07: habilitado, no iniciado.
- PKG-08: habilitado, no iniciado; primera operación recomendada.
- PKG-09: habilitado sujeto a sus DAT, no iniciado.
- GATE-02: pendiente y cerrado hasta integrar PKG-06–PKG-09.
- Fase 6B: continúa prohibida antes de GATE-04 y GATE-05.

Recomendación operativa: `Ejecutar PKG-08 primero`, para restaurar cuanto antes
la sincronización canonical → publication sin convertir esa recomendación en
un requisito retroactivo de la puerta.

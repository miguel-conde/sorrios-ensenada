# Alcance aprobado de la edición 1.0

**Fase:** 6A.4 — cierre documental del alcance 1.0<br>
**Fecha:** 10 de octubre de 2026<br>
**Estado:** contrato de alcance aprobado; implementación no iniciada

## 1. Autoridad y función

Este documento deriva de las decisiones humanas `DEC-001`–`DEC-034`. Las
Auditorías A/B/C aportan la evidencia diagnóstica; no sustituyen esas decisiones.
[CIERRE_ALCANCE_V1_0.md](./CIERRE_ALCANCE_V1_0.md) conserva la decisión humana
de `DEC-016`–`DEC-034`, y
[DECISIONES_EDITORIALES_6A_2.md](./DECISIONES_EDITORIALES_6A_2.md) conserva
`DEC-001`–`DEC-015`.

Este documento normaliza ese cierre para su ejecución. No constituye
implementación, investigación, verificación bibliográfica, creación de
cartografía, aceptación de prototipo, candidata ni publicación.

Categorías:

- **V1 — incluido en 1.0:** debe implementarse.
- **VP — incluido en 1.0 con trabajo previo:** pertenece a 1.0, pero necesita un
  input o paquete anterior.
- **P — prototipo obligatorio antes de la decisión final de implementación:** no
  se adopta hasta validar el prototipo.
- **D — diferido a 1.1+:** no bloquea 1.0.
- **N — no incorporar:** queda deliberadamente fuera.
- **DAT — dato humano/editorial:** su estado se registra en PKG-00; no es
  investigación ni implementación.

## 2. Matriz maestra REV-001–REV-026

| ID | Elemento | Estado | Decisión que lo sustenta | Trabajo previo | Autoridad afectada | Validación | Notas |
|---|---|---|---|---|---|---|---|
| REV-001 | Identidad, créditos y metadatos | VP | DEC-007–009, DEC-015 | PKG-00 y PKG-09 | Usuario; `publication/` al ejecutar | Coherencia HTML/PDF, créditos, licencia y metadatos | No inventar datos; ISBN no bloquea 1.0. |
| REV-002 | Mapa regional y mapa local | VP | DEC-021 | PKG-03 y GATE-01 | Fuente cartográfica externa; después `publication/` | Procedencia, licencia, atribución, escala, leyenda, accesibilidad y reproducibilidad | Solo orientación actual/editorial; no reconstrucción histórica. |
| REV-003 | CIT-B/C, referencias y bibliografía pública | VP | DEC-025–028 | PKG-02 y GATE-01 | Verificación bibliográfica; después `publication/` | Correspondencia fuente-uso, registros normalizados, citas y enlaces | Verificación no equivale a investigación histórica. |
| REV-004 | QA1, historia editorial y modelos de cita | VP | DEC-029–031 | PKG-00, PKG-02 y PKG-08 | `publication/`; datos del usuario | Nueve QA1; síntesis no técnica; once objetos cubiertos por familias | No usar un changelog Git. |
| REV-005 | Preliminares modulares P3 y orientación | V1 | DEC-001, DEC-003–005, DEC-020 | PKG-06 y PKG-07 | `publication/` | Correspondencia multiformato, rutas y cronología | El capítulo 4 se conserva. |
| REV-006 | Navegación D/C/I/E/L | V1 | DEC-033 | PKG-08 | `publication/`; Registro solo como autoridad de lectura | Enlaces a matriz, retornos, cobertura y ausencia de saturación | Mejor conexión, no más marcas por sistema. |
| REV-007 | Colofón técnico-editorial breve | VP | DEC-010 | PKG-00 y PKG-09 | Usuario; `publication/` | Identidad, roles, fecha, versión, URL y licencia | No duplica historia, créditos ni bibliografía. |
| REV-008 | PDF/UA, PDF/A y certificación formal | D | Cierre 6A.4; limitación conocida | Ninguno para 1.0 | Futuro paquete específico | Herramientas formales cuando se autorice | La accesibilidad básica sí permanece obligatoria. |
| REV-009 | Formulaciones históricas superadas de 0.6 | N | Revisión 6A.1 y decisiones negativas ratificadas | Ninguno | — | Pruebas de no regresión | No recuperar comunales uniformes, autoconsumo, clima causal, amortiguación ni falsas cifras. |
| REV-010 | Facsímil antiguo de 35 recortes como sustituto del íntegro | N | DEC-012 y cierre 6A.4 | Ninguno | — | Prueba de no regresión | La política futura se decide mediante F3, no volviendo a 0.6. |
| REV-011 | Índices provisionales de 0.6 | N | Cierre 6A.4 | Ninguno | — | Mantener nueve índices con localizadores reales | REV-025 corrige la composición actual. |
| REV-012 | Imitación de formato y maqueta 0.6 | N | Cierre 6A.4 | Ninguno | — | Prueba visual de no regresión | Una futura edición impresa tendría alcance propio. |
| REV-013 | Prólogo personal firmado, 900–1.500 palabras | VP | DEC-002–003 | Texto del usuario en PKG-00 | Usuario; después `publication/` | Posición tras créditos y preservación de voz | No redactarlo por inferencia. |
| REV-014 | Introducción, rutas y convenciones compactas | V1 | DEC-004–005, DEC-011 | PKG-06 | `publication/` | Rutas histórica/documental y enlace al capítulo 4 | No duplicar el método detallado. |
| REV-015 | Landing HTML y portada PDF propias | V1 | DEC-006–007 | PKG-06 | `publication/` | Diferenciación por formato e identidad coherente | Título/subtítulo de trabajo aprobados. |
| REV-016 | F3 para facsímil/transcripción | P | DEC-012 | PKG-04 y decisión en GATE-01 | `publication/` solo en prototipo | Cotejo, legibilidad, navegación, accesibilidad, páginas, peso y reproducibilidad | No integrar definitivamente antes de aceptación humana. |
| REV-017 | Macroorden y dos rutas de lectura | V1 | DEC-011 | PKG-06 | `publication/` | Orden conservado y rutas accesibles | No reordenar el volumen. |
| REV-018 | Sidebar HTML | V1 | DEC-014 | PKG-05 | `publication/` | Parte activa abierta; teclado, escritorio y viewport estrecho | Corrección UX obligatoria. |
| REV-019 | Cierres conclusivos específicos | V1 | DEC-013 | PKG-06 | `publication/` | Revisión de capítulos 5–13 | Uniformidad funcional, no literal. |
| REV-020 | Glosario GH-B selectivo | VP | DEC-016–019 | PKG-01 canónico y GATE-01 | `project/`; después regeneración en `publication/` | Siete G1, cuatro altas nuevas, dos candidatas auditadas y cautelas G3 | G3 no bloquea 1.0. |
| REV-021 | Cronología, dos mapas, diagrama y límites | VP | DEC-020–024, DEC-029 | PKG-03, PKG-07 y PKG-08 | `publication/`; fuentes externas solo para mapas | Fidelidad, atribución, equivalencia textual y accesibilidad | Concejo/municipio se difiere; esquema del término no se produce. |
| REV-022 | Retirada de la identidad de desarrollo | V1 | DEC-006–007 | PKG-06 y PKG-09 | `publication/` | Ausencia de `0.1.0-dev`, `development` y «Edición en desarrollo» en la candidata | No cambiar antes de la integración. |
| REV-023 | Separación de numeración y títulos en TOC PDF | V1 | Defecto confirmado en 6A.1 | PKG-05 | `publication/` | Casos extremos del capítulo 16 y TOC completo | Corrección obligatoria. |
| REV-024 | Orden alfabético del glosario | V1 | Defecto confirmado en 6A.1 | PKG-05, después de PKG-01 | Generación de `publication/`; no reordenación manual innecesaria de `project/` | Orden determinista, tildes y paridad HTML/PDF | Corrección obligatoria. |
| REV-025 | Separación de entradas de índices PDF | V1 | Defecto confirmado en 6A.1 | PKG-05 | `publication/` | Los nueve índices, jerarquía y cortes de página | Corrección obligatoria. |
| REV-026 | Auditoría y optimización segura de peso | V1 | DEC-034 | PKG-04 y PKG-05 | `publication/` | Medición antes/después, calidad paleográfica y reproducibilidad | Sin objetivo arbitrario; si no hay mejora segura, el tamaño no bloquea 1.0. |

Recuento de las 26 REV: **V1 12; VP 8; P 1; D 1; N 4**. Ninguna está
marcada como implementada.

## 3. Decisiones adicionales normalizadas

### Glosario

- `DEC-016`: GH-B selectivo.
- `DEC-017`: mejorar las siete G1 —`Señorío`, `medio vecino`, `propios`,
  `arbitrio`, `boto`, `vecera` e `hijo de familia`— con conocimiento ya
  existente.
- `DEC-018`: incorporar `avitadores`, `utilidad`, `repartimiento` y `quartal`;
  auditar canónicamente `establecimiento del suelo` y `arenta` e incorporarlas
  solo si cumplen presencia significativa, utilidad, autonomía y seguridad.
- `DEC-019`: `añino`, `alcavalas`, `servicio ordinario y extraordinario` y
  `pobre de solemnidad` no condicionan 1.0; se conservan las cautelas.

### Visual

- `DEC-020`: cronología visual en 1.0, limitada a hitos sustentados.
- `DEC-021`: mapa regional y mapa local en 1.0, sujetos a PKG-03.
- `DEC-022`: diagrama económico integrado desde el capítulo 13 vigente.
- `DEC-023`: esquema Concejo histórico/municipio diferido a 1.1+.
- `DEC-024`: no producir un esquema exacto del término histórico con la
  evidencia actual.

### Fuentes, aparatos y trazabilidad

- `DEC-025`: sistema híbrido CIT-B/C.
- `DEC-026`: verificar las 16 referencias pendientes antes de 1.0.
- `DEC-027`: bibliografía pública, normalizada y visible.
- `DEC-028`: citas o notas próximas selectivas.
- `DEC-029`: aparato compacto con las nueve QA1.
- `DEC-030`: historia intelectual/editorial breve.
- `DEC-031`: modelos principales agrupados por familias, con cobertura de los
  once objetos citables.
- `DEC-032`: TOP-006 permanece solo en la matriz y no se usa como prueba
  narrativa de continuidad.
- `DEC-033`: mejorar enlaces y política de visibilidad D/C/I/E/L en 1.0.
- `DEC-034`: auditar e intentar optimización segura; el peso no es un bloqueo si
  no existe reducción material, reproducible y sin pérdida apreciable.

## 4. Datos humanos y editoriales — DAT

PKG-00 quedó cerrado con diferimientos controlados. La autoridad humana y la
formulación ejecutiva completa se conservan en
[CIERRE_PKG_00_INPUTS_EDITORIALES.md](./CIERRE_PKG_00_INPUTS_EDITORIALES.md).

| ID | Valor aprobado | Estado | Momento de uso/cierre |
|---|---|---|---|
| DAT-001 | Miguel Conde de Simón; forma bibliográfica `Conde de Simón, Miguel`; sin ORCID ni afiliación | **RESUELTO** | Portada, créditos, metadatos, colofón y citas |
| DAT-002 | Autor, investigación y dirección editorial; edición crítica: Miguel Conde de Simón | **RESUELTO** | Créditos y responsabilidad intelectual |
| DAT-003 | Transcripción paleográfica y revisión: Miguel Conde de Simón | **RESUELTO** | Créditos y modelos de cita |
| DAT-004 | Edición modernizada y revisión: Miguel Conde de Simón | **RESUELTO** | Créditos y modelos de cita |
| DAT-005 | Ningún colaborador humano | **RESUELTO** | Agradecimientos eventuales, sin alterar autoría, al redactar el prólogo |
| DAT-006 | Línea secundaria `Proyecto Sorríos — Catastro de Ensenada`; título y subtítulo aprobados; autor Miguel Conde de Simón | **RESUELTO** | Landing, portada, créditos y metadatos |
| DAT-007 | Miguel Conde de Simón, limitado al contenido original | **RESUELTO PARA CONTENIDO ORIGINAL** | Aviso de copyright y colofón; materiales externos bajo régimen propio |
| DAT-008 | CC BY 4.0, limitada al contenido original que el autor pueda licenciar | **RESUELTO PARA CONTENIDO ORIGINAL** | Distribución y reutilización; sin relicenciar materiales externos |
| DAT-009 | Modelo F1: año efectivo de publicación visible y fecha completa en metadatos/colofón/release | **MODELO RESUELTO — VALOR FINAL DIFERIDO HASTA PUBLICACIÓN** | Publicación efectiva |
| DAT-010 | No existe URL pública canónica aprobada | **DIFERIDO HASTA PKG-12/PKG-13** | Mecanismo real de publicación |

Recuento DAT: **10**. DAT-001–DAT-008 están resueltos; DAT-009 conserva solo el
valor final diferido y DAT-010 se cierra con la publicación. Ningún valor se
infiere.

Diferimientos adicionales controlados de PKG-00: texto definitivo del prólogo,
agradecimientos eventuales, nota final de derechos por componentes y asuntos
`LEGAL-PENDIENTE` sobre facsímil, reproducciones, cartografía e imágenes
externas. No impiden iniciar PKG-01–PKG-05.

## 5. Backlog 1.1+

- Conformidad formal PDF/UA o PDF/A y herramientas de certificación.
- Esquema Concejo histórico/municipio, si una prueba de lectura demuestra su
  valor.
- Investigación G3 sobre `añino`, `alcavalas`, `servicio ordinario y
  extraordinario` y `pobre de solemnidad`.
- Investigación posterior de límites que no sea necesaria para 1.0, incluidas
  `LIM-011`–`LIM-013` si se decide resolverlas.
- Cartografía histórica únicamente cuando exista nueva evidencia suficiente y
  una operación canónica autorizada.
- Mejoras interactivas no esenciales con equivalente estático y accesible.
- Listas autónomas de mapas/tablas solo si el inventario final demuestra valor
  real de navegación.

REV-023, REV-024 y REV-025 no pertenecen al backlog: son defectos obligatorios
de 1.0.

## 6. NO INCORPORAR

- Antigua red de vulnerabilidades/amortiguadores.
- Esquema exacto del término histórico con la evidencia actual.
- Reconstrucciones cartográficas históricas no sustentadas.
- Conversiones metrológicas no sustentadas.
- Gráficos cuantitativos por cuota.
- Recuperación mecánica de la composición 0.6.
- Facsímil antiguo de 35 recortes como sustituto del facsímil íntegro.
- Índices provisionales de 0.6.
- Imitación de la antigua maqueta o paginación.
- Formulaciones históricas superadas.
- TOP-006 como prueba narrativa de continuidad toponímica.
- Changelog Git como historia editorial.
- Investigación histórica parcheada directamente en `publication/`.
- Objetivos arbitrarios de tamaño que degraden el documento.

## 7. Cobertura DEC-001–DEC-034

| Decisiones | Sede ejecutiva en este contrato |
|---|---|
| DEC-001, DEC-003, DEC-004, DEC-005 | REV-005 y REV-014 |
| DEC-002 | REV-013 |
| DEC-006, DEC-007 | REV-001, REV-015 y REV-022 |
| DEC-008, DEC-009 | REV-001 y DAT-001–DAT-008 |
| DEC-010 | REV-007 |
| DEC-011 | REV-014 y REV-017 |
| DEC-012 | REV-016 |
| DEC-013 | REV-019 |
| DEC-014 | REV-018 |
| DEC-015 | REV-001 |
| DEC-016, DEC-017, DEC-018, DEC-019 | REV-020 y apartado 3 |
| DEC-020 | REV-005, REV-021 |
| DEC-021 | REV-002, REV-021 |
| DEC-022, DEC-023, DEC-024 | REV-021 |
| DEC-025, DEC-026, DEC-027, DEC-028 | REV-003 |
| DEC-029, DEC-030, DEC-031 | REV-004 |
| DEC-032 | REV-003 y apartado 3 |
| DEC-033 | REV-006 |
| DEC-034 | REV-026 |

Las 34 decisiones están representadas y ninguna se reabre.

Índice nominal de control: `DEC-001`, `DEC-002`, `DEC-003`, `DEC-004`,
`DEC-005`, `DEC-006`, `DEC-007`, `DEC-008`, `DEC-009`, `DEC-010`, `DEC-011`,
`DEC-012`, `DEC-013`, `DEC-014`, `DEC-015`, `DEC-016`, `DEC-017`, `DEC-018`,
`DEC-019`, `DEC-020`, `DEC-021`, `DEC-022`, `DEC-023`, `DEC-024`, `DEC-025`,
`DEC-026`, `DEC-027`, `DEC-028`, `DEC-029`, `DEC-030`, `DEC-031`, `DEC-032`,
`DEC-033`, `DEC-034`.

## 8. Control de cambios después de 6A.4

Después de aprobar este documento, ningún paquete de ejecución puede añadir una
función, investigación, recurso visual, capítulo, aparato o cambio canónico que
no esté incluido en este alcance.

Toda nueva necesidad se registrará como `CR-V1-001`, `CR-V1-002`, etc. Cada CR
debe indicar:

- origen;
- motivo;
- impacto;
- si corrige un defecto o amplía alcance;
- recomendación;
- decisión humana.

Una CR no aprobada **no se implementa**. Un defecto descubierto durante la
validación puede producir una CR correctiva, pero no autoriza ampliaciones
editoriales silenciosas. Los cambios canónicos conservan su operación separada
y su propia autoridad.

## 9. Estado de cierre

El alcance 1.0 queda documentalmente aprobado. Su ejecución se rige por
[PLAN_EJECUCION_V1_0.md](./PLAN_EJECUCION_V1_0.md). La candidata técnica actual
permanece intacta y ninguna fila de este contrato equivale a trabajo ya
implementado.

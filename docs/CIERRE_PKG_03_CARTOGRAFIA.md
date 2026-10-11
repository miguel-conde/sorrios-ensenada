# PKG-03 — Cierre de cartografía

## 1. Estado

`COMPLETADO E INTEGRADO`

`PKG-03: APTO PARA INTEGRACIÓN`

Los dos mapas contemporáneos de orientación han superado la revisión
cartográfica, jurídica, geográfica, visual, accesible y reproducible. Los assets
están integrados en la rama de publicación, pero todavía no se han insertado en
capítulos ni en las salidas HTML/PDF.

## 2. Git

- Base: `ddfa2adb9f06f7b50585dbc80f156e62c968f570`.
- Rama de trabajo: `pkg-03/cartografia-v1`.
- Commit PKG-03: `4d0210f5f127933ac7a059bb029cde04ecd6d28b`
  (`feat(publication): prepare reproducible cartography for 1.0`).
- Rama objetivo: `feature/quarto-book`.
- Integración: fast-forward estricto mediante
  `git merge --ff-only pkg-03/cartografia-v1`; no se creó commit de merge, no
  se hizo rebase ni cherry-pick.
- Remoto: `origin/feature/quarto-book` permaneció en
  `da2c596b20abd5447c11c83955d18a99ad9af9a6`; no se hizo push.

## 3. Mapas

### Regional

- Asset: `publication/assets/cartography/mapa-regional.svg`.
- Función: situar el ámbito del volumen en la secuencia España → provincia
  actual de León → municipio actual de Santa María de Ordás → entorno
  Sorrios–Santibáñez.
- Fuentes: BDLJE para límites actuales y NGBE para el punto local.
- Resultado: **APTO**; 1.200 × 800 px lógicos, sin solapamientos o clipping,
  con escala, norte, leyenda, aviso de contemporaneidad y atribuciones visibles.

### Local

- Asset: `publication/assets/cartography/mapa-local.svg`.
- Función: mostrar la relación espacial entre Sorrios, Santibáñez de Ordás,
  Santa María de Ordás, Villapodambre, Rioseco de Tapia y Tapia de la Ribera,
  junto con el curso actual del río Luna y límites municipales actuales.
- Fuentes: NGBE, BDLJE e IGR_HIDROGRAFIA v1 2023.
- Resultado: **APTO**; 1.200 × 940 px lógicos, legible a ancho aproximado de
  página, en pantalla y en escala de grises.
- La fórmula `Sorrios (Sorribos en el expediente de 1752)` funciona como
  aclaración editorial subordinada: no atribuye geometría histórica ni se
  presenta como prueba de continuidad toponímica.

## 4. Fuentes y derechos

- BDLJE — Límites y Unidades Administrativas Actuales, IGN/CNIG: licencia de
  uso IGN compatible con CC BY 4.0; atribución `Obra derivada de BDLJE CC-BY
  4.0 ign.es`.
- NGBE — Nomenclátor Geográfico Básico de España, IGN/CNIG: licencia de uso
  IGN compatible con CC BY 4.0; atribución `Obra derivada de NGBE CC-BY 4.0
  ign.es`.
- IGR_HIDROGRAFIA v1 2023, Sistema Cartográfico Nacional/IGN: CC BY 4.0;
  atribución `Obra derivada de IGR_HIDROGRAFIA v1 2023 CC-BY 4.0 scne.es`.

La revisión independiente confirmó que las tres fuentes permiten reutilizar,
transformar y redistribuir los mapas derivados con reconocimiento. Las fórmulas
exigidas están incorporadas de forma visible en los SVG y deben conservarse.
Los datos externos mantienen su procedencia: la licencia CC BY 4.0 del contenido
original del volumen no los convierte en creación del autor del libro.

## 5. Carácter contemporáneo

Los mapas son instrumentos contemporáneos de orientación editorial. No son
reconstrucciones de 1752 y no muestran:

- el término histórico exacto;
- jurisdicciones, señoríos o límites parroquiales históricos;
- propiedades o parcelas históricas;
- caminos históricos.

Los límites administrativos, puntos y curso fluvial representados son actuales.
Ambos assets contienen el aviso de que no constituyen una reconstrucción de los
límites ni de la organización territorial de 1752.

## 6. Accesibilidad

- Cada SVG contiene `role="img"`, título, descripción y `aria-labelledby`.
- El título, pie, leyenda y aviso son visibles dentro del asset.
- Tramas, formas, contornos y estilos de línea evitan depender solo del color.
- Los textos alternativos editoriales están documentados en
  `docs/CARTOGRAFIA_PKG_03_V1_0.md` para su uso en PKG-07.
- La revisión material comprobó color, escala de grises y ancho aproximado de
  inserción.

## 7. Reproducibilidad

- Generador: `publication/scripts/build_cartography.py`.
- Snapshot mínimo: `publication/assets/cartography/cartography.json`.
- Tests: `tests/test_publication_pkg03.py`.
- Reconstrucción ordinaria offline y `--check`: **PASS**.
- Refresco desde los WFS oficiales: **PASS**, sin cambios en el snapshot o los
  SVG.
- Tests focales antes y después de integrar: **9 passed**.

Hashes SHA-256 verificados antes y después de regenerar y tras la integración:

| Archivo | SHA-256 |
|---|---|
| `cartography.json` | `b4ac5ad2744f531c1ec0c7c212a3e25aca77a2172b676863ca143a47a02b68d8` |
| `mapa-regional.svg` | `2c6f3c76293a3c67aa698b9abd8b6ad184ad35c4fae3d80de6ec2f176ce99a1d` |
| `mapa-local.svg` | `ebc54b6593eab73778860a41db66221e78b6b83028b51602769d02a523fd15df` |

## 8. Integración editorial pendiente

Los assets están preparados y versionados, pero **todavía no están integrados
en la publicación**: no se han insertado en capítulos, preliminares, HTML o PDF.
La integración narrativa, multiformato y accesible pertenece a
`PKG-07 — Aparato visual interno`, después de la puerta correspondiente.

## 9. Incidencia técnica descubierta

La validación completa descubrió la incompatibilidad registrada como
`CR-V1-001`. El parser de `publication/scripts/apparatus_sources.py` conserva
el contrato anterior de cinco campos y rechaza el campo canónico selectivo
`Contexto histórico` aprobado e integrado en PKG-01.

La comparación del mismo test en la base previa y en PKG-03 demuestra que el
fallo es preexistente y no tiene relación causal con la cartografía. Se clasifica
como **TECH-A / DEFECTO TÉCNICO**. Debe corregirse adaptando el consumidor antes
de PKG-04; no se debe revertir ni modificar el Glosario GH-B.

## 10. Estado de INC-BIB

- `INC-BIB-001`: abierta.
- `INC-BIB-002`: abierta.
- Ambas deben cerrarse antes de GATE-01 conforme a su plan específico.

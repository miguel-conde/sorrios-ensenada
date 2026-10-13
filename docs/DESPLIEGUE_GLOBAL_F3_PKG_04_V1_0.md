# PKG-04 — Despliegue global F3

## 1. Decisión de origen

El despliegue aplica sin reabrirla la decisión humana `F3-APROBAR`, registrada
el 12 de octubre de 2026 sobre el prototipo del commit
`7c6d6870214cac19b799d57b392bb1b9d347edd1`:

- H1–H5: **Sí**;
- P1–P8: **Sí**;
- HTML: facsímil completo, crop al 74 %, lightbox nativo, fallback directo y
  navegación bidireccional;
- PDF: facsímil completo principal, localizador al 28 %, página y posición en
  texto y navegación interna bidireccional.

La implementación parte exactamente de
`18e596bac4047b3cc162236e73fec1917a76eb63` en la rama aislada
`pkg-04/f3-global-v1`.

## 2. Alcance

- 18/18 páginas digitales del manuscrito;
- 35/35 unidades documentales;
- 35 relaciones página → unidad;
- 35 relaciones unidad → página;
- ninguna modificación de las fuentes canónicas de `project/`.

La página 1 contiene una unidad completa. Las páginas 2–18 contienen dos
unidades cada una, en posiciones izquierda y derecha. Esta cardinalidad procede
de `project/00_CONTROL/unidades.yaml`; no se deduce de nombres de archivo.

## 3. Matriz página ↔ unidad

| Página | Unidad | Orden | Posición | Anchor de página | Anchor de unidad |
|---:|---|---:|---|---|---|
| 1 | `portada` | 1 | página completa | `pagina-digital-01` | `transcripcion-portada` |
| 2 | `reverso_portada` | 2 | izquierda | `pagina-digital-02` | `reverso-portada` |
| 2 | `folio_306r` | 3 | derecha | `pagina-digital-02` | `folio-306r` |
| 3 | `folio_306v` | 4 | izquierda | `pagina-digital-03` | `folio-306v` |
| 3 | `folio_307r` | 5 | derecha | `pagina-digital-03` | `folio-307r` |
| 4 | `folio_307v` | 6 | izquierda | `pagina-digital-04` | `folio-307v` |
| 4 | `folio_308r` | 7 | derecha | `pagina-digital-04` | `folio-308r` |
| 5 | `folio_308v` | 8 | izquierda | `pagina-digital-05` | `folio-308v` |
| 5 | `folio_309r` | 9 | derecha | `pagina-digital-05` | `folio-309r` |
| 6 | `folio_309v` | 10 | izquierda | `pagina-digital-06` | `folio-309v` |
| 6 | `folio_310r` | 11 | derecha | `pagina-digital-06` | `folio-310r` |
| 7 | `folio_310v` | 12 | izquierda | `pagina-digital-07` | `folio-310v` |
| 7 | `folio_311r` | 13 | derecha | `pagina-digital-07` | `folio-311r` |
| 8 | `folio_311v` | 14 | izquierda | `pagina-digital-08` | `folio-311v` |
| 8 | `folio_312r` | 15 | derecha | `pagina-digital-08` | `folio-312r` |
| 9 | `folio_312v` | 16 | izquierda | `pagina-digital-09` | `folio-312v` |
| 9 | `folio_313r` | 17 | derecha | `pagina-digital-09` | `folio-313r` |
| 10 | `folio_313v` | 18 | izquierda | `pagina-digital-10` | `folio-313v` |
| 10 | `folio_314r` | 19 | derecha | `pagina-digital-10` | `folio-314r` |
| 11 | `folio_314v` | 20 | izquierda | `pagina-digital-11` | `folio-314v` |
| 11 | `folio_315r` | 21 | derecha | `pagina-digital-11` | `folio-315r` |
| 12 | `folio_315v` | 22 | izquierda | `pagina-digital-12` | `folio-315v` |
| 12 | `folio_316r` | 23 | derecha | `pagina-digital-12` | `folio-316r` |
| 13 | `folio_316v` | 24 | izquierda | `pagina-digital-13` | `folio-316v` |
| 13 | `folio_317r` | 25 | derecha | `pagina-digital-13` | `folio-317r` |
| 14 | `folio_317v` | 26 | izquierda | `pagina-digital-14` | `folio-317v` |
| 14 | `folio_318r` | 27 | derecha | `pagina-digital-14` | `folio-318r` |
| 15 | `folio_318v` | 28 | izquierda | `pagina-digital-15` | `folio-318v` |
| 15 | `folio_319r` | 29 | derecha | `pagina-digital-15` | `folio-319r` |
| 16 | `folio_319v` | 30 | izquierda | `pagina-digital-16` | `folio-319v` |
| 16 | `folio_320r` | 31 | derecha | `pagina-digital-16` | `folio-320r` |
| 17 | `folio_320v` | 32 | izquierda | `pagina-digital-17` | `folio-320v` |
| 17 | `folio_321r` | 33 | derecha | `pagina-digital-17` | `folio-321r` |
| 18 | `folio_321v` | 34 | izquierda | `pagina-digital-18` | `folio-321v` |
| 18 | `hoja_enfrentada_posterior` | 35 | derecha | `pagina-digital-18` | `hoja-enfrentada-posterior` |

La validación de la matriz exige páginas 1–18, identificadores y anchors únicos,
posiciones válidas, ausencia de páginas vacías y exactamente una asociación por
unidad. Resultado: **18 páginas, 35 unidades, 35 relaciones, 0 huérfanas y 0
duplicadas**.

## 4. Arquitectura

- `publication/scripts/f3_model.py` concentra los parámetros cerrados, la regla
  de anchors, la validación del mapping, los enlaces página/unidad y el marcado
  diferenciado por formato.
- `build_facsimile.py` consume la matriz completa y añade a cada página todos
  sus enlaces reales hacia la transcripción.
- `build_transcription.py` genera para cada unidad la tarjeta de procedencia, el
  crop HTML y el localizador PDF mediante la misma regla compartida.
- `build_f3_prototype.py` conserva la muestra 12/22/23 como regresión y reutiliza
  la implementación compartida; sus hardcodes no gobiernan producción.
- `prepare.py` carga el manifest canónico y produce F3 global dentro del flujo
  ordinario, sin comando especial.
- `pdf_internal_links.lua` convierte los enlaces `QMD#fragmento` en enlaces PDF
  internos al fragmento y sigue eliminando los enlaces QMD sin destino.

No se introdujeron excepciones por unidad ni cambios en estilos generales.

## 5. HTML

- 18 páginas facsimilares completas y ordenadas;
- 35 unidades con crop al **74 %**;
- 35 lightboxes nativos de Quarto, sin CDN ni nueva dependencia;
- 35 enlaces directos alternativos a la imagen;
- 35 enlaces facsímil → unidad y 35 retornos unidad → facsímil materializados;
- 18 anchors de página y 35 anchors de unidad válidos, sin enlaces `.qmd`
  residuales en el HTML renderizado.

## 6. PDF

- 18 páginas completas, sin convertir el facsímil principal en thumbnail;
- 35 localizadores al **28 %**;
- página digital y posición expresadas en texto para las 35 unidades;
- 35 enlaces facsímil → unidad;
- 35 enlaces principales unidad → facsímil y 35 enlaces equivalentes desde la
  explicación del localizador.

La inspección reproducible con `pdftohtml -xml` sobre las páginas físicas
89–108 y 109–211 contabilizó respectivamente **35**, **35** y **35** enlaces
internos para las tres clases anteriores. Todos se resolvieron a páginas
existentes del PDF.

## 7. Anchors

- página: `pagina-digital-{NN}`, con relleno a dos dígitos;
- unidad: se preserva `published_unit_anchor()` sin renombrados;
- anchors de página: 18/18 únicos;
- anchors de unidad: 35/35 únicos;
- destinos HTML rotos o duplicados: 0;
- relaciones sin destino: 0.

## 8. Reproducibilidad

`publication/scripts/prepare.py` se ejecutó dos veces. Las dos ejecuciones
produjeron **141 archivos** bajo `publication/generated/` y el conjunto de
SHA-256 fue idéntico. El directorio continúa ignorado y
`git ls-files publication/generated` devuelve vacío.

Los crops y localizadores proceden de las mismas imágenes derivadas y de la
posición declarada en `unidades.yaml`; no existen recortes manuales.

## 9. Fidelidad documental

- Las cinco secciones textuales de cada una de las 35 unidades se compararon
  con la edición crítica canónica: **idénticas**.
- La lineación paleográfica se comprobó unidad por unidad en los artefactos
  generados, el HTML y el PDF: **35/35 PASS**.
- El orden material y el mapping se conservaron: **35/35 PASS**.
- Manuscrito: 18 páginas y SHA-256
  `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`.
- `project/` permanece intacto.

## 10. Accesibilidad

- 18/18 páginas y 35/35 crops tienen texto alternativo contextual;
- cada fallback nombra la unidad y declara que abre la imagen completa;
- página y posición están disponibles como texto, no solo por disposición
  visual;
- el lightbox conserva cierre visible y alternativa independiente sin
  JavaScript;
- no se declara conformidad WCAG formal.

## 11. Tests globales

Se añadieron `GF3-01`–`GF3-18` para cubrir cardinalidades, mapping, unicidad de
anchors, navegación en ambos sentidos, 74/28 %, lightbox, fallback, localización
textual, fidelidad, política de generados y ausencia de hardcodes productivos.

Resultados finales:

- GF3-01–GF3-18 + prototipo PKG-04 + Phase 4A/4B/4D/6A: **126 passed**;
- suite completa: **616 passed**, 0 failed, 0 errors y ningún skip/xfail nuevo;
- compilación Python: **PASS**.

## 12. Render HTML completo

El libro completo se renderizó correctamente en **30 documentos**. La
validación material confirmó:

- 18 páginas y 35 unidades en orden;
- 35 crops F3, 35 lightboxes y 35 fallbacks;
- 35 enlaces en cada sentido;
- assets locales y ausencia de enlaces QMD rotos o rutas absolutas.

Este HTML es un **artefacto de validación**, no una candidata formal.

## 13. Render PDF completo

El pipeline completó las tres pasadas de LuaLaTeX necesarias. Resultado:

- páginas: **335**;
- bytes: **74.041.686**;
- SHA-256:
  `cf19ec66912e9b805b42ef1d2b08f5c3a4f3e65f5281d32c4cbe217d2001c3c9`;
- enlaces internos F3 inspeccionados: **105** anotaciones relevantes (35 de
  ida y dos retornos equivalentes por cada una de las 35 unidades).

Este PDF es un **artefacto de validación**, no una candidata formal.

## 14. Revisión visual

La muestra estratificada examinó:

| Formato | Casos | Resultado |
|---|---|---|
| HTML escritorio | páginas 1, 12 y 18; portada, folio 315v y hoja enfrentada posterior | jerarquía, imágenes, enlaces, pies y texto estables |
| HTML 390 px | portada completa y lightbox abierto | crop, tarjeta, fallback, texto y cierre contenidos y legibles |
| PDF facsímil | páginas físicas 90, 101 y 107 | página completa principal y enlaces de unidades correctos |
| PDF transcripción | páginas físicas 109, 171 y 209 | localizador 28 %, localización textual y flujo correctos |

La muestra incluye la cardinalidad singular de la página 1, la muestra humana
ya aprobada 12/22/23, la última página, una unidad extensa y la unidad final en
blanco. No se detectaron casos extremos que exigieran alterar los parámetros.

## 15. Métricas antes/después

| Métrica | Candidata anterior | Validación F3 global | Diferencia |
|---|---:|---:|---:|
| Páginas PDF | 334 | 335 | +1 |
| Bytes PDF | 73.994.496 | 74.041.686 | +47.190 |
| SHA-256 | `f1eee2f465f554d3bf2b506d23a622967d1b4f1013ac657a774868e525688183` | `cf19ec66912e9b805b42ef1d2b08f5c3a4f3e65f5281d32c4cbe217d2001c3c9` | cambio esperado |

La diferencia procede de la maquetación F3 de las partes III–IV y no se usa
como criterio de calidad.

## 16. Limitaciones

- No se crea candidata 1.0 ni se actualizan versión, estado, fecha, URL o hash
  oficial de publicación.
- No se inicia PKG-05, PKG-07, PKG-08, PKG-10 ni Fase 6B.
- `INC-BIB-001`, `INC-BIB-002` y `REV-024` permanecen intactas.
- No se insertan mapas en capítulos ni se modifica la bibliografía.
- No se integra, publica, etiqueta ni crea release desde esta operación.

## 17. Resultado

Validadores finales:

- `validate_project.py`: **PASS**;
- `check_sources.py`: **PASS**;
- `validate_publication.py`: **PASS**;
- `validate_publication.py --rendered`: **PASS**;
- cartografía `--check`: **PASS**;
- `git diff --check`: **PASS**.

**`DESPLIEGUE F3 GLOBAL: APTO PARA INTEGRACIÓN`**

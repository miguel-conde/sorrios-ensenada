# PKG-10 — Candidata formal 1.0

**Estado:** `PKG-10: CANDIDATA 1.0 GENERADA Y TÉCNICAMENTE APTA`<br>
**Rama:** `pkg-10/candidate-1.0-v1`<br>
**Commit fuente:** `a666e878eb6672bee337ac4a2b6f0410ae8e0872`<br>
**Fecha de construcción técnica:** 16 de octubre de 2026<br>
**Naturaleza:** candidata de prepublicación; no es la release 1.0

La fecha de construcción técnica identifica esta ejecución y no constituye la
fecha editorial de publicación.

## 1. Procedencia

| Elemento | Valor |
|---|---|
| Snapshot canónico | `a162fad1792aa9b3804a5499d348ab355e5ce574` |
| Árbol `project/` | `a8ccb6d783e51aafb6493fed9791097d0a678086` |
| Edición Crítica | 3.6 |
| Estudio Histórico | 1.3 |
| Registro D/C/I/E/L | 1.3 |
| Edición modernizada | 1.3 |
| Glosario | 28 entradas; blob `29089c7bbc2a60e4459b9ffc0e86de1f3363edeb` |
| Manuscrito | 18 páginas; 5.038.575 bytes; SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24` |

El árbol canónico coincide exactamente con el del commit fuente. El manuscrito
se leyó desde la réplica local verificada exterior al checkout; Drive conserva
la autoridad.

## 2. Preparación y reproducibilidad

La construcción comenzó sin `publication/_book/`, `publication/generated/`
ni caché local del proyecto. La preparación manual se ejecutó una vez; los
renders posteriores invocaron el `pre-render` contractual.

- 5 fuentes, 35 unidades y manuscrito verificados;
- 83 derivados reproducibles;
- 78.448.397 bytes;
- SHA-256 del manifiesto ordenado de derivados:
  `f4e50559edd884bcbd106f32ffa494c9ca373c68f490aec06474f62ff5623e9e`;
- huella idéntica antes y después de los renders: PASS.

## 3. Tests y validadores

- focal PKG-06–PKG-09/candidata: `58 passed`;
- suite completa, ejecutada una vez: `678 passed`, 0 fallos y 0 errores;
- proyecto canónico: PASS;
- fuentes y snapshot: PASS;
- publicación estática: PASS;
- cartografía: PASS;
- compilación Python: PASS;
- `quarto check`: PASS;
- publicación renderizada HTML/PDF: PASS;
- `git diff --check`: PASS.

## 4. Salida HTML

- directorio: `publication/_book/`;
- entrada: `publication/_book/index.html`;
- 39 documentos HTML;
- 117 archivos públicos sin contar el PDF;
- 74.567.798 bytes sin contar el PDF;
- 2.638.399 bytes de documentos HTML;
- SHA-256 del manifiesto ordenado del bundle HTML/assets:
  `74b49ecd3f9261bf8153a499ef0bbe59ffd78d24935b7647c3e65be0d37f047e`;
- navegación, sidebar, búsqueda, enlaces, anclas, citas, F3 y descarga PDF:
  PASS;
- viewport emulado de 390 px: `scrollWidth = clientWidth = 390`; PASS.

## 5. Salida PDF

- archivo: `publication/_book/sorribos-santibanez-ordas-1752.pdf`;
- 355 páginas;
- 71.020.397 bytes;
- SHA-256:
  `7361b491c8095f55a6bb6add3445924b52db6518f49610342cfbbf5a946f4771`;
- PDF 1.7, tamaño letter, texto seleccionable, 23 variantes de fuente
  embebidas y 53 imágenes;
- TOC, paginación, enlaces, imágenes, F3, bibliografía, índices y colofón:
  PASS.

## 6. Revisión técnica representativa

Se comprobaron en HTML la landing, créditos, placeholder del prólogo,
introducción y convenciones; los capítulos 3, 6, 11 y 13; cronología,
diagrama y mapas; facsímil, transcripción, modernización, glosario, matriz,
QA1, «Cómo citar», bibliografía, índices y colofón. La revisión incluyó
navegación, enlaces internos, sidebar, F3 y vista estrecha.

En PDF se inspeccionaron la portada, el índice general, los preliminares, la
cronología, ambos mapas, el diagrama económico, facsímil, localizador F3,
transcripción, modernización, glosario, matriz, QA1, modelos de cita,
bibliografía, índice de materias y colofón. No se observaron cortes,
colisiones, imágenes ausentes ni regresiones de composición.

Resultado: `REVISIÓN TÉCNICA = PASS`.

## 7. Controles de regresión

- `TRA-006` no reaparece;
- `DEM-005` conserva la corrección canónica;
- BIB-012 no se usa como autoridad;
- BIB-015 mantiene el contexto doméstico restringido;
- `TOP-006` permanece solo en la matriz;
- QA1: 9/9;
- objetos de cita: 11/11;
- F3 y REV-023–026: intactas;
- los SVG de PKG-03 son idénticos a los aprobados;
- no aparece la identidad visible «edición en desarrollo»;
- `project/` permanece intacto.

## 8. Toolchain

- Python 3.12.10 y pytest 9.1.1;
- Quarto 1.7.31 y Pandoc 3.6.3;
- LuaHBTeX 1.24.0 / TinyTeX 2026;
- Poppler 24.02.0;
- Chrome 142.0.7444.134;
- `rsvg-convert` 2.58.0.

El sistema no exponía inicialmente `rsvg-convert` en `PATH`. Para el render se
extrajo temporalmente, fuera del checkout, el paquete oficial
`librsvg2-bin` 2.58.0 usado también en la validación de PKG-07. No se instaló
software en el sistema ni se versionó ningún binario.

## 9. Diferimientos preservados

- Prólogo: **PLACEHOLDER CONTROLADO PENDIENTE DE REDACCIÓN PERSONAL**; Miguel
  Conde de Simón lo sustituirá antes del cierre/release de 1.0.
- Fecha exacta: no inventada; el año visible sigue siendo 2026.
- URL canónica: no inventada; diferida a publicación/release.
- ISBN: ausente y no bloqueante.

## 10. Manifest e integridad

Este dossier es el manifest documental de la candidata PKG-10 y sustituye como
referencia editorial vigente a la candidata técnica histórica `49ab2e1`. Los
artefactos HTML/PDF y los derivados permanecen locales e ignorados; no se
versionan `publication/_book/`, `publication/generated/`, PDF, HTML ni
capturas.

No se modificaron fuentes canónicas, contenido editorial, generadores,
cartografía ni configuración del libro. No hubo push, tag, release, despliegue
ni inicio de PKG-11 o Fase 6B.

## 11. Resultado y siguiente operación

`PKG-10: CANDIDATA 1.0 GENERADA Y TÉCNICAMENTE APTA`

La rama queda preparada para revisión independiente e integración. Tras esa
integración podrá iniciarse PKG-11 — Validación integral; GATE-03 continúa
pendiente hasta que PKG-10 sea reproducible e integrado y PKG-11 termine en
PASS.

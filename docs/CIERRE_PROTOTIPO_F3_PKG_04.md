# PKG-04 — Cierre del prototipo F3

## Estado

`PROTOTIPO APROBADO E INTEGRADO`

## Base

`5d90b280af8a2fe7185737f3342245cde8e6fac8`

## Commit

`7c6d6870214cac19b799d57b392bb1b9d347edd1`

## Muestra

PKG-04 construyó y evaluó un mini-libro F3 reproducible para la página digital
12 y las unidades `folio_315v` y `folio_316r`. El prototipo comparó el modelo
vigente con una presentación diferenciada por formato sin modificar las fuentes
canónicas de `project/`.

## Resultado técnico

- HTML: facsímil completo, recorte completo al 74 %, lightbox local, alternativa
  accesible sin JavaScript y navegación bidireccional.
- PDF: facsímil completo, localizador al 28 %, página y posición textual y
  enlaces internos de ida y vuelta comprobados en el PDF compilado.
- Generación: ocho derivados reproducibles e ignorados producidos por
  `publication/scripts/build_f3_prototype.py` y `prepare.py`.
- Integridad: ninguna salida generada, PDF ni fuente externa quedó versionada.

## Resultado humano

La revisión registrada en
[APROBACION_HUMANA_F3_PKG_04.md](./APROBACION_HUMANA_F3_PKG_04.md) obtuvo:

- H1–H5: **Sí**;
- P1–P8: **Sí**;
- decisión: **`F3-APROBAR`**.

No se requieren cambios en los porcentajes ni otro ensayo previo al despliegue.

## Decisión

`F3-APROBAR`

## Modelo aprobado

### HTML

- facsímil completo;
- crop 74 %;
- lightbox;
- navegación bidireccional.

### PDF

- facsímil completo como reproducción principal;
- localizador 28 %;
- página/posición textual;
- navegación bidireccional.

La solución preserva el cotejo y la orientación y reduce satisfactoriamente la
duplicación visual en PDF.

## Integración Git

El commit `7c6d6870214cac19b799d57b392bb1b9d347edd1`, hijo directo de la base
`5d90b280af8a2fe7185737f3342245cde8e6fac8`, fue revisado e integrado en
`feature/quarto-book` mediante fast-forward estricto. No se creó commit de
merge y no se hizo `push` durante el cierre.

## Validación

- generación completa con `publication/scripts/prepare.py`: **PASS**;
- tests focales PKG-04 + Phase 4A/4B: **46 passed**;
- suite completa tras la integración: **597 passed**;
- `validate_project.py`: **PASS**;
- `check_sources.py`: **PASS** — 35 unidades, 18 páginas y hash del manuscrito
  exacto;
- `validate_publication.py`: **PASS**;
- generador cartográfico con `--check`: **PASS**;
- compilación Python y `git diff --check`: **PASS**.

## Integridad canónica

- `project/` permanece intacto.
- `publication/generated/` no contiene archivos versionados.
- `INC-BIB-001` e `INC-BIB-002` permanecen abiertas hasta GATE-01.
- `REV-024` permanece pendiente de PKG-05.

## Qué NO se ha hecho

- No se desplegó F3 sobre las 35 unidades.
- No se regeneró la candidata completa HTML/PDF.
- No se inició PKG-05, PKG-10, PKG-12, PKG-13 ni Fase 6B.
- No se creó etiqueta ni release.

## Siguiente operación

`Despliegue global F3 sobre las 35 unidades.`

## Continuidad histórica

El modelo posteriormente se desplegó globalmente en PKG-04; véase
[CIERRE_PKG_04_F3_GLOBAL.md](./CIERRE_PKG_04_F3_GLOBAL.md). Este enlace no
altera el hecho histórico de que el despliegue estaba pendiente al cerrar el
prototipo.

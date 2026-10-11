# PKG-01 — Cierre del Glosario canónico GH-B

## 1. Estado

`COMPLETADO E INTEGRADO`

## 2. Base

- Rama de origen: `feature/quarto-book`.
- SHA base: `da2c596b20abd5447c11c83955d18a99ad9af9a6`.
- Rama aislada: `pkg-01/glosario-gh-b-v1`.
- Commit canónico: `9ae4d1fd46d9f2d7bca685de861bff2a554a7a39`
  (`feat(project): enrich canonical glossary for 1.0`).
- Integración: fast-forward estricto mediante `git merge --ff-only`; no se creó
  commit de merge, no se hizo rebase ni cherry-pick.

## 3. Plugin/skill

- Plugin local `sorrios-ensenada`: versión 2.0.2.
- Skill local `editar-catastro-sorrios`: versión 2.0.2.
- Se usó la copia versionada del workspace bajo `plugins/sorrios-ensenada/`, sin
  reinstalación ni actualización.

## 4. Alcance ejecutado

- Mejoradas las siete voces G1: `Señorío`, `medio vecino`, `propios`,
  `arbitrio`, `boto`, `vecera` e `hijo de familia`.
- Incorporadas las cuatro voces nuevas obligatorias: `avitadores`, `utilidad`,
  `repartimiento` y `quartal`.
- Evaluadas e incorporadas las dos voces condicionales: `establecimiento del
  suelo` y `arenta`.
- Las cuatro G3 no fueron investigadas ni ampliadas.
- Las tres G4 no fueron ampliadas.
- Las restantes voces G0 permanecieron intactas.

## 5. Resultado de las condicionales

- `establecimiento del suelo` = **INCORPORADA**. La locución documentada de la
  respuesta 22 tiene utilidad autónoma para limitar esa ausencia concreta de
  pago sin convertirla en ausencia general de derechos señoriales.
- `arenta` = **INCORPORADA**. La forma documental de la respuesta 20 resulta
  opaca y admite una interpretación canónica cauta en relación con renta o
  aparcería, sin normalizar la lectura ni reconstruir el contrato.

## 6. Archivos canónicos modificados

1. `project/20_TRABAJO_EDITORIAL/Glosario.md`.
2. `project/00_CONTROL/CAMBIOS.md`.
3. `project/00_CONTROL/OPERACIONES/PKG-01-GLOSARIO-GH-B-2026-10-11.md`.

## 7. Validación

- Revisión independiente del diff completo y del registro semántico: `APTO`.
- Relación de Git comprobada: el commit canónico tiene como padre directo la
  base declarada y era el único commit por integrar.
- Validador local 2.0.2: `VALID: GitHub workspace v2 coherent`, antes y después
  de la integración.
- Pruebas focalizadas: 32 en PASS antes y después de la integración.
- Glosario: 28 entradas finales, 13 voces objetivo presentes y ningún encabezado
  duplicado.
- G3, G4 y las restantes G0: sin cambios en el diff.
- `git diff --check`: PASS.
- Ningún PDF quedó versionado; `publication/`, plugin, tests y `.github/`
  permanecieron intactos durante la operación canónica.
- La candidata local preexistente conserva 73.994.496 bytes y el SHA-256
  `f1eee2f465f554d3bf2b506d23a622967d1b4f1013ac657a774868e525688183`.

## 8. Propagación pendiente

El Glosario canónico ya está actualizado. La salida publicada no se regenera en
PKG-01. La propagación al aparato publicado, al orden alfabético, a los enlaces,
al PDF y al HTML se realizará en paquetes posteriores conforme al plan.

REV-024 continúa pendiente de PKG-05: el orden alfabético debe resolverse en la
generación publicada sin alterar innecesariamente el orden de la fuente.

## 9. Estado de candidata previa

La candidata de 334 páginas y SHA-256
`f1eee2f465f554d3bf2b506d23a622967d1b4f1013ac657a774868e525688183` se conserva
como baseline pre-PKG-01. No representa ya el estado canónico actual del libro y
queda pendiente de regeneración futura; no se invalida su anterior validación
técnica.

## 10. Próximo paso

`PKG-02 — Verificación bibliográfica`

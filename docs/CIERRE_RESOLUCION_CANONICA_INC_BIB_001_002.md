# Cierre — Resolución canónica INC-BIB-001 / INC-BIB-002

**Fecha:** 14 de octubre de 2026

## 1. Estado

`INTEGRADA`

Veredicto independiente:
`RESOLUCIÓN CANÓNICA INC-BIB-001/002: APTA PARA INTEGRACIÓN`.

## 2. Base

La operación partió de
`d4153c60489f4df24cdadf75d7740ec85b9406dd`, que era también el HEAD limpio y
sin divergencia de `feature/quarto-book` antes de la integración.

## 3. Commit canónico

`a162fad1792aa9b3804a5499d348ab355e5ce574`

El commit es hijo directo de la base, contiene exclusivamente las seis rutas
previstas y mantiene separada esta operación de los cambios editoriales de
publicación.

## 4. INC-BIB-001

- Autoridad primaria: R29, folio 319v.
- `TRA-005`: preservada sin cambios como dato local D.
- `TRA-006`: retirada del Registro por no estar demostrado el paralelo E/I
  atribuido a BIB-012.
- Estudio Histórico: retirados el paralelo general y su fuente; conservada la
  descripción local de la taberna que «anda por vecera entre los vecinos».
- Glosario: conservada la definición local de `vecera` y eliminada la
  generalización externa no demostrada.
- Resultado: `CERRADA CANÓNICAMENTE`.

## 5. INC-BIB-002

- Autoridad primaria: R21, folio 318r.
- `DEM-001`: preservada sin cambios; mantiene los ocho medios vecinos,
  incluidas dos viudas, como dato local D.
- `DEM-005`: restringida al contexto que BIB-015 sí respalda sobre libros
  personales, convivientes y viudas con casa abierta como cabezas de casa; no
  sostiene una equivalencia general entre viuda y medio vecino.
- Estudio Histórico: separa expresamente el dato local D del contexto E/I y de
  las cautelas L.
- Glosario: conserva el uso local de `medio vecino` y elimina la
  generalización comparativa no sustentada.
- Resultado: `CERRADA CANÓNICAMENTE`.

## 6. Integridad documental

- Edición Crítica y sus R21/R29: idénticas a la base.
- `DEM-001`, `DEM-002`, `TRA-005` y `CAL-001`–`CAL-020`: idénticos a la base.
- Controles `proyecto.yaml`, `estado.yaml` y `unidades.yaml`: idénticos.
- Manuscrito y cartografía: intactos.
- `publication/` y `references.bib`: sin cambios en el commit canónico ni en
  este cierre.
- Registro: 131 IDs definidos; Estudio: 126 IDs citados; cero citas ausentes.

## 7. Validación canónica

- Validador canónico: PASS (`VALID: GitHub workspace v2 coherent`).
- Pruebas focalizadas: 32 superadas.
- Estructura de tablas Markdown, referencias internas e IDs: PASS.
- `git diff --check`: PASS.
- Auditoría de residuos: cero residuos incorrectos en documentación canónica
  activa; las demás apariciones son historia de control o propagación
  editorial pendiente.

## 8. Integración Git

La rama `canonical/inc-bib-001-002-v1` se integró en
`feature/quarto-book` mediante `git merge --ff-only`. El resultado fue el
commit exacto `a162fad1792aa9b3804a5499d348ab355e5ce574`; no hubo commit de
merge, rebase, cherry-pick ni push.

## 9. Desincronización controlada de publicación

La suite general registra 585 pruebas superadas, nueve fallos y 36 errores.
Todos los no-PASS se explican por la actualización intencionada de `project/`
sin propagar todavía el nuevo contrato a `publication/`:

1. tres fallos de Fase 4D y los errores de sus fixtures parten del blob antiguo
   del Glosario o del parser fijado al Registro 1.2;
2. tres fallos de PKG-05 dependen del mismo blob anterior y bloquean la
   generación del Glosario;
3. dos fallos del prototipo detectan `TRA-006` todavía declarado en los
   capítulos 11 y 13;
4. un fallo de Fase 6A detecta que la candidata congela el árbol canónico
   anterior.

No hay fallos canónicos, de F3, cartografía, cálculos, pérdida de datos o
estructura. Esta desincronización es el resultado esperado de respetar la
separación de autoridades y no se corrige aquí porque esta operación prohíbe
modificar `publication/`; su resolución pertenece a PKG-08. La cifra anterior
586/8/36 del dossier canónico se corrigió a partir de la reproducción real
sobre el commit exacto.

## 10. Propagación obligatoria en PKG-08

Inventario comprobado, sin ejecutar en esta operación:

- INC-BIB-001: retirar `TRA-006` del front matter, localizadores y prosa de los
  capítulos 11 y 13; no se localizaron otros capítulos con ese ID.
- INC-BIB-002: revisar en el capítulo 6 el uso de `DEM-005` y conservar la
  separación entre dato local, contexto externo y cautela; no se localizaron
  otros capítulos con ese ID.
- Actualizar `publication/meta/publication.yml`: commit/árbol canónico,
  versiones y blobs de Registro, Estudio y Glosario.
- Adaptar `publication/scripts/apparatus_sources.py` y los textos/contratos de
  `build_apparatus.py`, `build_vertical_prototype.py` y
  `validate_publication.py` al Registro vigente, sin relajar provenance.
- Regenerar, no editar manualmente, el Glosario y la matriz de evidencia, junto
  con los aparatos dependientes bajo `publication/generated/`.
- Actualizar las expectativas equivalentes de
  `tests/test_publication_phase4d.py`, `tests/test_publication_pkg05.py`,
  `tests/test_publication_prototype.py` y el snapshot canónico de
  `tests/test_publication_phase6a.py`.
- Tratar BIB-012 solo para lo efectivamente verificado y BIB-015 solo para el
  contexto contenido en la obra; implementar las citas próximas y la
  bibliografía en `references.bib` sin presentar ninguna de ellas como soporte
  del dato primario local que no demuestra.
- Regenerar y validar HTML/PDF y los derivados después de completar la
  propagación; la candidata formal resultante corresponde a PKG-10.

## 11. Estado de GATE-01

`GATE-01: LISTO PARA EVALUACIÓN`

No se declara `PASS` ni `FAIL` en esta operación. PKG-06 no se ha iniciado y
Fase 6B permanece prohibida antes de la aceptación humana del preview.

## 12. Siguiente paso

`Evaluación formal de GATE-01.`

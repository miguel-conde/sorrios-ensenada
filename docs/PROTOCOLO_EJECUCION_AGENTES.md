# Protocolo permanente de ejecución de agentes

## 1. Finalidad y alcance

Este documento concentra el contrato común de ejecución del proyecto Sorríos.
Los encargos posteriores deben ser diferenciales: declaran paquete, base, rama,
tipo, alcance, aceptación y condiciones de parada específicas, sin repetir las
reglas permanentes de entorno, Git, validación, renders e informe.

El protocolo no sustituye las autoridades del proyecto, `PROJECT.md`, la skill
`editar-catastro-sorrios`, las instrucciones de publicación ni el contrato de
cada paquete. Una instrucción específica aprobada para una operación prevalece
sobre este patrón general dentro de su alcance.

## 2. Ejecución silenciosa

Por defecto, el agente:

- no narra el progreso ni anuncia cada comando;
- no envía actualizaciones del tipo «ahora voy a…»;
- no informa de intentos intermedios ni de errores operativos recuperables;
- corrige silenciosamente un entorno invocado de forma incorrecta cuando la
  corrección no cambia el resultado ni el alcance.

Solo interrumpe la ejecución cuando se activa una condición de parada, necesita
una decisión humana o termina la operación. El informe final resume resultados,
no reproduce un diario cronológico.

## 3. Preflight único y entorno estándar

Cada operación comienza con un único preflight rápido, antes de editar o de
ejecutar una comprobación costosa. Debe confirmar:

- repositorio, rama, HEAD/base, refs y árbol de trabajo;
- ausencia de cambios ajenos no explicados;
- herramientas requeridas y versiones relevantes;
- entorno correcto para Python, pytest y Quarto;
- validadores y comandos aplicables al tipo de operación.

El entorno estándar del repositorio es:

```sh
source .venv/bin/activate
python ...
pytest ...
quarto ...
```

`python` y `pytest` deben resolver dentro de `.venv/bin/`. Quarto puede ser un
binario del sistema, pero se invoca desde la shell con `.venv` activada para que
sus hooks usen el Python y las dependencias del proyecto. El preflight no
ejecuta la suite completa, `prepare.py` ni renders.

## 4. Tres niveles de validación

### Nivel 1 — Preflight

Siempre y una sola vez. Es rápido y comprueba Git, entorno y tooling. No incluye
suite completa ni render.

### Nivel 2 — Focal

Se usa durante la implementación:

- tests de los archivos, contratos o regresiones afectados;
- validadores del ámbito modificado;
- render parcial únicamente si el cambio es visual o necesita comprobar una
  salida concreta.

No se ejecuta la suite completa después de cada cambio.

### Nivel 3 — Integral

Se ejecuta una sola vez al final del paquete, cuando su tipo lo requiere:

- suite completa;
- validadores integrales;
- render completo solo si el cambio afecta realmente a la composición o si el
  contrato específico lo exige.

Una corrección posterior invalida únicamente las evidencias que pueda afectar.
Se repite la comprobación mínima necesaria y se evita reiniciar todo el ciclo
sin una causa técnica.

## 5. Política de trabajo costoso

### Renders

Cuando el paquete cambia la composición, el máximo ordinario es un render HTML
completo final y un render PDF completo final. Durante el desarrollo se
prefieren previews o renders focales.

Se admiten ejecuciones adicionales justificadas para:

- experimentos A/B;
- diagnóstico y corrección de un defecto visual;
- recuperación de un fallo de render;
- PKG-10–PKG-13, según su contrato específico.

Después de un `merge --ff-only` no se repite un render si el SHA integrado es
exactamente el ya renderizado, no hay cambios posteriores y no cambió el
entorno relevante.

### `prepare.py`

`publication/scripts/prepare.py` no se ejecuta por rutina varias veces. Se hace
una ejecución cuando sea necesaria. Dos ejecuciones para demostrar determinismo
solo corresponden cuando cambian generadores, parsers, provenance,
transformaciones reproducibles u outputs generados.

Debe contarse el `pre-render` de Quarto, que invoca la preparación: no se añade
una llamada manual idéntica sin motivo.

### Tests

El patrón normal es:

1. tests focales durante el desarrollo;
2. suite completa una sola vez al final cuando el tipo de cambio la requiere;
3. tras el avance rápido de un SHA ya validado, smoke mínimo y ninguna segunda
   suite completa.

No se repite una suite si no han cambiado código, inputs, configuración ni
toolchain relevantes.

### Reutilización de evidencia

Puede reutilizarse una validación previa cuando coinciden:

- SHA;
- inputs;
- configuración;
- toolchain relevante.

El cierre debe identificar la evidencia reutilizada y confirmar esas
coincidencias. Registrar la reutilización es preferible a repetir trabajo
costoso sin cambio material.

## 6. Tipos de operación

| Tipo | Focal | Suite completa | prepare x2 | HTML completo | PDF completo | Visual |
|---|---|---|---|---|---|---|
| T1 — Documentación / roadmap | Obligatorio | No | No | No | No | No |
| T2 — Código no visual | Obligatorio | Obligatorio | No | Condicional | Condicional | No |
| T3 — Contenido / publicación | Obligatorio | Obligatorio | Condicional | Condicional | Condicional | Condicional |
| T4 — Layout / visual | Obligatorio | Obligatorio | Condicional | Obligatorio | Obligatorio | Obligatorio |
| T5 — Generadores / parser / provenance | Obligatorio | Obligatorio | Condicional | Condicional | Condicional | Condicional |
| T6 — Candidata / validación / release | Condicional | Condicional | Condicional | Condicional | Condicional | Condicional |

Aplicación:

- **T1:** preflight, validación documental/focal y `git diff --check`; sin
  suite completa ni render.
- **T2:** focales y suite final; render solo ante una necesidad funcional
  demostrable.
- **T3:** focales, suite final y un render completo final cuando cambie el
  libro.
- **T4:** previews focales, suite final, un HTML/PDF final y revisión visual
  representativa.
- **T5:** preparación cuando corresponda, determinismo si lo exige la clase de
  cambio, focales y suite final; render solo si cambia la salida publicada.
- **T6:** aplica la política integral específica de PKG-10–PKG-13. «Integral»
  no obliga a repetir evidencia válida sobre el mismo SHA.

## 7. Condiciones permanentes de parada

La operación se detiene ante:

- HEAD, base o ref inesperados;
- árbol sucio no explicado;
- conflicto de autoridad;
- necesidad de modificar una capa prohibida;
- fallo ajeno al alcance que impide validar o continuar;
- decisión humana nueva necesaria;
- ampliación de alcance;
- pérdida de reproducibilidad.

Los prompts futuros solo deben añadir las condiciones específicas del paquete.
Un fallo operativo recuperable de entorno no es por sí solo una condición de
parada si puede corregirse sin alterar el resultado.

## 8. Contrato Git permanente

Salvo instrucción expresa en contrario:

- la implementación se hace en una rama aislada;
- no se hace push, tag ni release;
- no se usa reset destructivo ni rebase que reescriba historia;
- se revisa y valida antes de integrar;
- la integración se hace preferentemente con `merge --ff-only`;
- `publication/generated/`, `_book/`, PDF, HTML, screenshots y demás derivados
  no se versionan;
- el árbol queda limpio al cerrar.

## 9. Tooling existente y reutilización

El repositorio ya ofrece piezas suficientes para ejecutar el protocolo sin
crear un framework nuevo:

- preflight Git con `git status`, `git rev-parse`, `git show-ref` y
  `git merge-base`;
- entorno con `source .venv/bin/activate` y comprobación de `python`, `pytest`
  y `quarto`;
- tests focales mediante rutas o node IDs de pytest y suite integral con
  `pytest -q`;
- validación canónica con
  `python plugins/sorrios-ensenada/tools/validate_project.py .`;
- fuentes sin generación con
  `python publication/scripts/check_sources.py`;
- publicación estática con
  `python publication/scripts/validate_publication.py` y validación de
  artefactos, cuando proceda, mediante `--rendered`;
- cartografía sin reescritura con
  `python publication/scripts/build_cartography.py --check`;
- entorno Quarto con `quarto check` y composición con `quarto render` solo en
  los tipos que la autorizan;
- higiene del diff con `git diff --check`.

No existe un validador Markdown dedicado ni un wrapper único de niveles. Como
mejora futura puede crearse un wrapper pequeño con subcomandos `preflight`,
`check focal` y `check full`, siempre que solo orqueste herramientas existentes,
no oculte su salida relevante y no ejecute preparación o renders implícitos.
No se construye ese framework en esta operación.

## 10. Prompt diferencial estándar

```text
Ejecuta `<PKG/operación>` conforme a
`docs/PROTOCOLO_EJECUCION_AGENTES.md`.

Base: `<sha>`
Rama: `<rama>`
Tipo: `<T1–T6>`

Alcance específico:
- ...
- ...

Criterios de aceptación:
- ...
- ...

Condiciones de parada adicionales:
- ...

Resultado:
`rama aislada` / `integrar tras validación`, según se indique.
```

Un prompt normal debe caber aproximadamente en 20–40 líneas. Solo se amplía
cuando la semántica particular del paquete lo exige.

## 11. Aplicación retrospectiva

### PKG-08

Con este protocolo habría bastado con:

1. preflight único;
2. SYNC-08, tests focales y una suite completa para recuperar el baseline
   verde;
3. implementación restante;
4. tests y validadores focales;
5. una suite integral final;
6. un único render HTML/PDF completo final;
7. tras el fast-forward, smoke mínimo, sin rerender ni segunda suite completa.

Habrían sido redundantes las suites completas entre iteraciones focales, las
preparaciones adicionales fuera de la comprobación necesaria de determinismo,
los renders completos intermedios que no aislaran un defecto y cualquier suite
o render repetido después de integrar exactamente el SHA ya validado.

### PKG-05

Los renders A/B adicionales de PKG-05 sí estaban justificados: la variación de
paginación de 341 a 333 páginas exigía aislar experimentalmente la causa y
comparar el resultado sin pérdida. El protocolo reduce redundancia; no prohíbe
experimentos necesarios, explícitos y medibles.

## 12. Informe final compacto

Por defecto, el cierre informa únicamente de:

- resultado;
- cambios relevantes;
- tests;
- renders, si los hubo;
- validadores;
- estado Git;
- integridad;
- pendientes o siguiente paso.

## 13. Puntos de incorporación futura

`PROJECT.md` tiene un punto natural en «Inicio obligatorio», tras la selección
del modo de tarea. La skill versionada tiene otro en `SKILL.md`, dentro de
«Inicio» o antes de «Escritura en GitHub». Ambos pueden remitir a este protocolo
en una operación posterior expresamente autorizada; no se modifican ahora.

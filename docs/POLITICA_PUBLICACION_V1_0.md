# Política de publicación de la versión 1.0

**Estado:** política ratificada de publicación de la versión 1.0<br>
**Base de ratificación:** `bce6b38747ec6bc0bc5a58577f6e269c307b04a5`<br>
**Ámbito:** hosting, URL canónica, fecha de publicación y relación entre
PKG-12 y PKG-13

Este documento concreta la política posterior al
[plan de ejecución](./PLAN_EJECUCION_V1_0.md) y al
[checkpoint de reanudación](./CHECKPOINT_REANUDACION_PREVIEW_FINAL.md). No
inicia E4, PKG-12 ni PKG-13.

## Decisiones cerradas

- El repositorio público es
  <https://github.com/miguel-conde/sorrios-ensenada>.
- R5B está completada: el repositorio es público y su superficie fue
  verificada desde una perspectiva anónima.
- El año editorial es **2026**.
- El correo público es `miguelco2000@gmail.com`.
- El ISBN está ausente y no es bloqueante para la versión 1.0.
- GitHub es el repositorio de fuentes, código, documentación y trazabilidad.
- Los derivados HTML y PDF no se incorporan a `main`.

La URL pública del repositorio no equivale por sí sola a la URL canónica del
libro.

## NETLIFY — PROVEEDOR RATIFICADO

**PROVEEDOR DE PUBLICACIÓN V1.0 = NETLIFY.** La decisión quedó ratificada tras
la prueba empírica `NETLIFY-CAPABILITY-02`, realizada en la cuenta actual el
18 de octubre de 2026.

Parámetros actuales:

| Parámetro | Valor |
|---|---|
| Team | `New generation blog` / `miguelco2000` |
| Plan | Free (`nf_team_dev`) |
| Site name | `sorribos-santibanez-1752` |
| Site ID | `1539a52a-d500-426f-9995-7db9c01e6d45` |
| URL canónica | <https://sorribos-santibanez-1752.netlify.app/> |
| Integración Git | ninguna |
| Build remoto | ninguno |
| Año editorial | 2026 |
| Fecha exacta | pendiente hasta la publicación real |

El contrato de alojamiento es:

- sin conexión Git;
- sin continuous deployment;
- sin builds remotos;
- render local;
- despliegue manual de artefactos ya construidos;
- PKG-12 sobre un **draft deploy** no productivo;
- production no se modifica durante la revisión;
- `DATE-FINAL-01` genera y valida el artefacto final fechado;
- ese artefacto se sube como un nuevo draft final;
- PKG-13 publica, mediante **Publish Deploy**, el mismo draft final aceptado.

> **DRAFT ≠ PRIVADO.** La URL del draft no se publicita, pero puede ser
> accesible por quien la conozca.

La separación de responsabilidades queda fijada así: GitHub conserva fuentes,
código, documentación y trazabilidad; el entorno local construye, renderiza,
valida y calcula hashes; Netlify aloja artefactos preconstruidos. Netlify no
ejecuta Quarto.

Si PKG-12 exige correcciones, se corrigen las fuentes, se reconstruye y se crea
otro draft. Nunca se publica un deploy rechazado o sustituido.

El procedimiento operativo definitivo se documenta en el
[runbook de despliegue y actualización](./RUNBOOK_DESPLIEGUE_NETLIFY.md). El
site canónico permanece vacío hasta que la secuencia autorice el primer draft.
La URL está en estado **RESERVADA / PREPUBLICACIÓN**: mientras production no
contenga el libro, un HTTP 404 es el resultado esperado y no constituye una
excepción general a la validación de enlaces. PKG-12 revisará una URL de draft
distinta; tras PKG-13, la URL canónica deberá responder HTTP 200 y servir el
contenido correcto.

## Política de URL

> **La URL canónica debe estar fijada antes de E4.**

La regla responde a cuatro motivos:

- la URL forma parte del contenido citable;
- debe aparecer en «Cómo citar» y en la metadata o el colofón aplicables;
- debe poder verificarse durante PKG-12;
- cambiarla después invalidaría innecesariamente la candidata.

Proveedor, nombre del site y URL canónica están cerrados. `META-FINAL-01`
incorporó la URL canónica y la referencia al repositorio público en la edición;
la fecha exacta sigue diferida.

## Política de fecha

- El año editorial queda fijado en **2026**.
- No se anticipará una fecha exacta futura.
- La fecha exacta recomendada será la fecha **real** de publicación de la
  versión 1.0.
- La fecha exacta se fijará después de GATE-04 y antes de GATE-05/PKG-13.

La candidata revisada en PKG-12 podrá diferir del snapshot final únicamente por
un delta de fecha o metadata de release expresamente autorizado. Ese delta
exige:

- un cambio focal;
- un nuevo render HTML y PDF;
- validación proporcional;
- comprobación de que no existe ningún otro cambio semántico;
- hashes y manifiesto finales nuevos.

No se repetirá E4 completa salvo que aparezca cualquier otro cambio. Si el
delta supera fecha o metadata de release, deja de aplicarse esta excepción y
debe evaluarse el alcance real antes de continuar.

## Secuencia normativa vigente

```text
R5B — completada
→ NETLIFY-CAPABILITY-02 — completada
→ META-FINAL-01 — completada
→ E4
→ GATE-03
→ PKG-12
→ GATE-04
→ DATE-FINAL-01, cambio focal + rerender + delta validation
→ draft final y revisión focal
→ GATE-05
→ PKG-13 — Publish Deploy del mismo draft final aceptado
→ v1.0
```

E4, GATE-03, PKG-12, GATE-04, DATE-FINAL-01, GATE-05 y PKG-13 permanecen
pendientes. La fecha exacta sigue pendiente. Este documento no autoriza el
despliegue del libro, tags, releases ni cambios de proveedor.

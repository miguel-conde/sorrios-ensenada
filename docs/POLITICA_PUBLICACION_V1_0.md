# Política de publicación de la versión 1.0

**Estado:** registro normativo de decisiones cerradas, reglas vigentes y
recomendaciones pendientes de ratificación humana<br>
**Base:** `cadab208b5aec0a9620afc604c8383e1afc829f9`<br>
**Ámbito:** hosting, URL canónica, fecha de publicación y relación entre
PKG-12 y PKG-13

Este documento concreta la política posterior al
[plan de ejecución](./PLAN_EJECUCION_V1_0.md) y al
[checkpoint de reanudación](./CHECKPOINT_REANUDACION_PREVIEW_FINAL.md). No
inicia E4, PKG-12 ni PKG-13 y no convierte una recomendación de proveedor en
decisión humana definitiva.

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
libro, que continúa pendiente.

## Política recomendada pendiente de ratificación

Se recomienda **Netlify** como host de publicación con este contrato:

- sin conexión Git;
- sin continuous deployment;
- sin builds remotos;
- render local;
- despliegue manual de artefactos ya construidos;
- PKG-12 sobre un production deploy privado;
- PKG-13 haciendo público el mismo deploy aceptado, siempre que no haya habido
  correcciones.

Esta configuración es una recomendación operativa, no una decisión humana
definitiva. Permanecen pendientes la ratificación del proveedor, la elección
del nombre del site y la aprobación de la URL resultante. Si PKG-12 exige
correcciones, el objeto que se publique deberá ser el nuevo artefacto corregido
y aceptado, no el deploy anterior.

El procedimiento condicionado a una eventual ratificación de Netlify se
documenta en el
[runbook de despliegue y actualización](./RUNBOOK_DESPLIEGUE_NETLIFY.md). El
runbook no altera el estado pendiente de la recomendación.

## Política de URL

> **La URL canónica debe estar fijada antes de E4.**

La regla responde a cuatro motivos:

- la URL forma parte del contenido citable;
- debe aparecer en «Cómo citar» y en la metadata o el colofón aplicables;
- debe poder verificarse durante PKG-12;
- cambiarla después invalidaría innecesariamente la candidata.

Continúan pendientes:

- el proveedor definitivo;
- el nombre del site;
- la URL canónica concreta.

La incorporación de esa URL al libro será una operación focal posterior; no se
realiza en este registro.

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

## Secuencia normativa propuesta

```text
R5B — completada
→ decisión proveedor/site/URL
→ incorporar URL canónica
→ E4
→ GATE-03
→ PKG-12
→ GATE-04
→ fijar fecha real
→ DATE-FINAL-01, cambio focal + rerender + delta validation
→ GATE-05
→ PKG-13
→ v1.0
```

E4, GATE-03, PKG-12, GATE-04, DATE-FINAL-01, GATE-05 y PKG-13 permanecen
pendientes. Este documento no autoriza tags, releases, cambios de proveedor ni
configuración externa.

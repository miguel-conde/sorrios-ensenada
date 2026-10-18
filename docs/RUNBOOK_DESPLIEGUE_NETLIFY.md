# Runbook de despliegue y actualización en Netlify

**Estado del proveedor:** `NETLIFY — PROVEEDOR RATIFICADO`

**Ámbito:** primera publicación de la versión 1.0, mantenimiento, nuevas
versiones y rollback

**Política rectora:**
[POLITICA_PUBLICACION_V1_0.md](./POLITICA_PUBLICACION_V1_0.md)

Este es el procedimiento operativo definitivo para alojar en Netlify los
artefactos construidos localmente. La ratificación del proveedor y la reserva
del site canónico se realizaron mediante `NETLIFY-CAPABILITY-02`. El runbook no
autoriza por sí solo un despliegue del libro.

## 1. Contrato operativo

La separación de responsabilidades es obligatoria:

- **GitHub** conserva fuentes, código, documentación y trazabilidad.
- **El entorno local** prepara, valida y renderiza el libro con Quarto.
- **Netlify** aloja artefactos HTML ya construidos; no compila el proyecto.
- `publication/_book/` es un derivado local y no se incorpora a Git.
- Los secretos y credenciales quedan fuera del repositorio y de los artefactos.
- La URL canónica debe ser estable y estar fijada antes de E4.

El site no se conecta al repositorio Git, no usa continuous deployment ni
ejecuta builds remotos de Quarto. Cada publicación debe poder relacionarse de
forma verificable con una versión, un commit Git, los hashes o el manifiesto de
los artefactos y el identificador del deploy de Netlify.

### 1.1. Parámetros actuales del proyecto

| Parámetro | Valor |
|---|---|
| Team | `New generation blog` / `miguelco2000` |
| Plan | Free (`nf_team_dev`) |
| Site name | `sorribos-santibanez-1752` |
| Site ID | `1539a52a-d500-426f-9995-7db9c01e6d45` |
| URL canónica | <https://sorribos-santibanez-1752.netlify.app/> |
| Integración Git | ninguna |
| Build command remoto | ninguno |
| Deploys al ratificar | 0 |

El site quedó reservado vacío: sin production deploy, draft deploy, dominio
personalizado ni contenido del libro.

### 1.2. Evidencia de capacidad

`NETLIFY-CAPABILITY-02` validó empíricamente el 18 de octubre de 2026, en esta
misma cuenta, el recorrido manual `draft → Publish Deploy`. El draft no alteró
production; se publicó exactamente el mismo deploy ID; el número de deploys se
mantuvo en uno; no hubo builds, Git integration ni CI; y el site temporal fue
eliminado junto con sus URLs. La prueba no utilizó contenido del libro.

**Resultado:** `DRAFT→PUBLISH SAME DEPLOY: PASS`.

## 2. Requisitos previos

Antes de cualquier despliegue:

1. confirmar la operación autorizada y el estado de sus gates;
2. confirmar el commit exacto de fuentes y que el árbol Git está limpio;
3. construir y validar localmente el artefacto conforme al paquete aplicable;
4. verificar que `publication/_book/` corresponde a ese commit y no contiene
   credenciales, rutas locales ni material excluido;
5. disponer del manifiesto y de los hashes exigidos;
6. comprobar la identidad del site y el destino del despliegue;
7. autenticar Netlify CLI solo en el entorno local autorizado.

La autenticación y los tokens de Netlify no se guardan en Git, en
`_publish.yml`, en documentación versionada ni dentro de `publication/_book/`.

## 3. Primera publicación de la versión 1.0

La primera publicación usa el site canónico ya reservado, cuya production
permanece vacía hasta PKG-13.

### 3.1. Site canónico reservado

Antes de E4:

1. conservar el site canónico sin conexión Git, CI ni build remoto;
2. mantener estable el nombre, el site ID y la URL registrados;
3. incorporar la URL canónica al libro mediante `META-FINAL-01` antes de E4;
4. mantener production vacío o sin publicar hasta PKG-13;
5. no guardar credenciales en el repositorio.

No se exige privacidad al draft. Su URL no se publicita, pero puede ser
accesible por quien la conozca.

### 3.2. Candidata, aceptación y salida pública

La secuencia de la versión 1.0 es:

1. ejecutar E4 localmente sobre las fuentes con la URL canónica ya fijada;
2. subir el artefacto construido como **draft deploy**, sin `--prod` ni build
   remoto;
3. ejecutar PKG-12 sobre la URL independiente del draft, sin modificar
   production;
4. si hay correcciones, volver a las fuentes y aplicar el ciclo de corrección
   descrito en este runbook;
5. tras `GATE-04`, fijar la fecha real mediante `DATE-FINAL-01`;
6. volver a renderizar, hacer la validación delta y subir el artefacto final
   fechado como un **nuevo draft final**;
7. revisar focalmente ese draft final y registrar su deploy ID;
8. superar `GATE-05` y ejecutar PKG-13;
9. usar **Publish Deploy** sobre ese deploy ID aceptado, sin nuevo render ni
   segundo upload de producción;
10. verificar la URL canónica desde una sesión anónima.

El draft aceptado en PKG-12 no puede publicarse si fue sustituido por una
corrección o por el artefacto fechado de `DATE-FINAL-01`. El registro final debe
identificar inequívocamente el draft final que alcanzó production.

## 4. Despliegue de revisión

El comando de referencia, ejecutado desde la raíz del repositorio y sobre un
artefacto ya construido, es:

```sh
netlify deploy --dir=publication/_book --no-build
```

Cuando ayude a identificar la candidata, puede añadirse un alias controlado:

```sh
netlify deploy --dir=publication/_book --no-build --alias=<identificador-candidato>
```

Sin `--prod`, Netlify crea un **draft deploy** con URL separada: permite revisar
el artefacto sin reemplazar el site público. `--no-build` impide que Netlify
reconstruya el proyecto y mantiene a Quarto como única capa de construcción.

> **DRAFT ≠ PRIVADO.** La URL del draft no se publicita ni se comparte fuera
> de la revisión autorizada, pero puede ser accesible por quien la conozca.

Durante PKG-12 y la revisión del draft final nunca se usa `--prod`. Production
no se toca hasta PKG-13.

## 5. Promoción a producción

En PKG-13 se selecciona en Netlify el deploy final ya revisado y se usa
**Publish Deploy**. Antes de confirmar, el deploy ID debe coincidir exactamente
con el registrado en la aceptación. Así, el objeto validado y el publicado es
el mismo deploy atómico; no se produce un nuevo render, upload ni build.

Si Netlify cambia su API o producto y deja de ofrecer esta promoción, se
detiene la publicación y se decide un fallback explícito. No se sustituye
silenciosamente por un segundo deploy de producción, porque ya no demostraría
identidad de deploy.

## 6. Alternativa soportada de Quarto

`quarto publish netlify --no-render` es una alternativa soportada para publicar
un render existente. No es la opción preferida en este proyecto: el contrato
mantiene a **Quarto como herramienta de construcción** y a **Netlify como capa
de alojamiento**, con el despliegue manual explícito y auditable entre ambas.

## 7. Actualizaciones después de v1.0

Una vez que el site sea público, toda actualización o nueva versión sigue este
ciclo:

```text
fuentes
→ validación proporcional
→ render local
→ draft deploy
→ revisión
→ correcciones, si existen
→ aceptación
→ DATE-FINAL-01, cuando corresponda
→ draft final
→ validación final
→ Publish Deploy
→ verificación pública
→ tag/release, cuando la operación lo autorice
```

Nunca se reemplaza production para obtener una preview. La revisión sucede en
una URL de draft separada y solo el draft final aceptado se promueve.

La semántica de versionado se rige por la política editorial vigente y, si aún no existe, requiere una decisión separada.

## 8. Correcciones durante el preview

Si una candidata es rechazada o necesita cambios:

1. modificar las fuentes versionadas, no el artefacto;
2. crear el commit correspondiente;
3. ejecutar la validación proporcional al cambio;
4. generar un nuevo render local;
5. crear un nuevo draft deploy;
6. revisar y aceptar ese nuevo deploy.

`publication/_book/` nunca se edita manualmente. Un deploy rechazado se conserva
solo como evidencia operativa mientras lo exija el registro; no se promociona.

## 9. Fecha bibliográfica

La fecha se rige por la
[política de publicación](./POLITICA_PUBLICACION_V1_0.md#política-de-fecha):

- no se anticipan fechas futuras;
- la fecha exacta es la fecha real de publicación de la edición;
- para una edición nueva, la aceptación precede a la fijación de fecha;
- el cambio de fecha requiere rerender, validación delta, nuevo draft final y
  comprobación focal antes de publicar;
- los hashes y el manifiesto finales se calculan sobre el artefacto fechado.

Un redeploy puramente técnico o un rollback no cambia por sí solo la fecha
bibliográfica. Cualquier cambio de fecha requiere una decisión editorial
expresa.

## 10. Registro de publicación

Cada publicación debe conservar, como mínimo, estos campos:

| Campo | Valor |
|---|---|
| Versión editorial | `<versión>` |
| Commit Git de fuentes | `<sha>` |
| Tag, si está autorizado | `<tag o no aplica>` |
| URL canónica | `<url>` |
| Manifiesto y hashes | `<ruta/identificadores>` |
| Netlify site ID | `<site-id>` |
| Netlify deploy ID | `<deploy-id>` |
| URL del draft revisado | `<draft-url>` |
| Permalink del deploy | `<permalink>` |
| Fecha y hora de aceptación | `<ISO 8601>` |
| Fecha de publicación | `<fecha real>` |
| Identidad del deploy final | `<deploy-id + hash/manifiesto>` |
| Comprobación pública | `<fecha, alcance y resultado>` |

El registro debe permitir demostrar que el deploy promovido procede del
artefacto aceptado y del commit declarado.

## 11. Rollback

Ante un defecto en producción:

1. identificar el último deploy público conocido como correcto;
2. promoverlo mediante **Publish Deploy**;
3. confirmar que la URL canónica vuelve a servir ese deploy;
4. registrar el incidente, el deploy retirado y el restaurado;
5. corregir las fuentes versionadas;
6. reanudar el ciclo ordinario desde validación y render local.

No se corrige directamente el contenido de producción ni se edita el artefacto
desplegado. El rollback restaura servicio; la corrección permanente vuelve
siempre a las fuentes.

## 12. Lista previa a Publish Deploy

- [ ] Existe autorización para publicar y los gates exigidos están en PASS.
- [ ] El árbol Git está limpio y el SHA fuente está registrado.
- [ ] El draft corresponde al manifiesto y a los hashes aceptados.
- [ ] El deploy ID coincide exactamente con el draft final autorizado.
- [ ] La URL canónica, la versión y la fecha aplicables son correctas.
- [ ] La revisión humana identifica expresamente este deploy.
- [ ] No hay secretos, rutas locales ni artefactos excluidos.
- [ ] El site y el deploy ID de destino se han comprobado.
- [ ] Está identificado el último deploy correcto para un posible rollback.
- [ ] No se va a ejecutar ningún build remoto ni nuevo render implícito.

## 13. Lista posterior a la publicación

- [ ] La URL canónica responde desde una sesión anónima.
- [ ] Navegación, recursos, enlaces críticos y descarga del PDF funcionan.
- [ ] El deploy público coincide con el deploy aceptado.
- [ ] Se han registrado permalink, deploy ID, fecha/hora y resultado.
- [ ] Los hashes y el manifiesto finales quedan asociados al SHA y versión.
- [ ] No se ha modificado Git ni se han incorporado derivados a `main`.
- [ ] El tag o release se crea solo si la operación vigente lo autoriza.

## 14. Cosas que NO hacer

- No conectar Netlify a GitHub ni habilitar continuous deployment.
- No configurar builds remotos de Quarto.
- No usar `--prod` para una preview o durante su revisión.
- No reemplazar producción para enseñar una candidata.
- No reconstruir deliberadamente un artefacto ya aceptado al publicarlo.
- No editar manualmente `publication/_book/` ni un deploy.
- No versionar `_book/`, HTML, PDF u otros derivados en `main`.
- No guardar tokens o credenciales en Git, `_publish.yml`, documentación o
  artefactos.
- No desplegar sin comprobar el site y el destino efectivos.
- No corregir producción al margen de las fuentes y del ciclo normal.
- No cambiar la fecha bibliográfica por un redeploy técnico.
- No crear tags o releases fuera del paquete que los autorice.
- No desplegar sobre otro site ni cambiar el nombre o la URL canónica sin una
  decisión humana nueva.

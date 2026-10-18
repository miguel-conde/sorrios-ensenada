# Runbook de despliegue y actualización en Netlify

**Estado del proveedor:** `PROPUESTA RECOMENDADA — PENDIENTE DE RATIFICACIÓN`

**Ámbito:** primera publicación de la versión 1.0, mantenimiento, nuevas
versiones y rollback

**Política rectora:**
[POLITICA_PUBLICACION_V1_0.md](./POLITICA_PUBLICACION_V1_0.md)

Este runbook describe el procedimiento que se aplicará si Netlify es ratificado
como proveedor. No constituye esa ratificación, no crea ni configura un site y
no autoriza un despliegue. Las decisiones sobre proveedor, nombre del site y
URL canónica siguen pendientes.

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

La primera publicación tiene un recorrido especial porque todavía no existe
un site público estable.

### 3.1. Alta y preparación privada

Después de ratificar Netlify:

1. crear un proyecto de Netlify sin conexión Git, CI ni build remoto;
2. fijar el nombre del site y obtener la URL estable propuesta;
3. aprobar e incorporar la URL canónica al libro antes de E4;
4. mantener el proyecto y sus deploys bajo acceso privado durante la revisión;
5. registrar el identificador del site sin guardar credenciales.

La capacidad real de mantener privado el proyecto o deploy debe comprobarse
en la cuenta elegida antes de avanzar. Si el acceso anónimo no queda impedido,
la operación se detiene y la configuración debe decidirse de nuevo.

### 3.2. Candidata, aceptación y salida pública

La secuencia de la versión 1.0 es:

1. ejecutar E4 localmente sobre las fuentes con la URL canónica ya fijada;
2. subir el artefacto construido, sin build remoto, y promoverlo dentro del
   site protegido como **production deploy privado**;
3. ejecutar PKG-12 sobre ese production deploy privado;
4. si hay correcciones, volver a las fuentes y aplicar el ciclo de corrección
   descrito en este runbook;
5. tras `GATE-04`, fijar la fecha real mediante `DATE-FINAL-01`;
6. volver a renderizar, hacer la validación delta y subir el artefacto final
   fechado como nuevo deploy privado;
7. superar `GATE-05` y ejecutar PKG-13;
8. publicar exactamente el deploy final aceptado y hacer público el site;
9. verificar la URL canónica desde una sesión anónima.

El deploy aceptado en PKG-12 no puede publicarse si fue sustituido por una
corrección o por el artefacto fechado de `DATE-FINAL-01`. El registro final debe
identificar inequívocamente cuál de ellos alcanzó producción.

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

Durante la revisión nunca se usa `--prod`.

## 5. Promoción a producción

El procedimiento preferido es seleccionar en Netlify el deploy ya revisado y
usar **Publish Deploy**. Así, el objeto validado y el publicado es el mismo
deploy atómico; no se genera deliberadamente un artefacto nuevo para
producción.

Si Netlify deja de ofrecer esa promoción, el procedimiento alternativo es:

1. conservar el artefacto local ya validado sin reconstruirlo;
2. verificar su equivalencia con los hashes o el manifiesto aceptados;
3. realizar un deploy de producción de ese mismo artefacto con `--no-build`;
4. comprobar de nuevo en producción su identidad y comportamiento;
5. registrar que se utilizó la vía alternativa y los identificadores de ambos
   deploys.

No se vuelve a renderizar deliberadamente para crear el deploy de producción.

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

Nunca se reemplaza producción para obtener una preview. La revisión sucede en
una URL de draft separada y solo el deploy aceptado se promueve.

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
- No presentar Netlify como proveedor ratificado mientras siga pendiente la
  decisión humana.

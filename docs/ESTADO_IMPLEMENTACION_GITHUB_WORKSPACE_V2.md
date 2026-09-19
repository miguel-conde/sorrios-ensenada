# Estado de implementación — GitHub workspace v2

**Fecha:** 18 de septiembre de 2026  
**Rama canónica:** `main`  
**Versión activa:** 2.0.2  
**Estado:** H1, H2, H3, H4, H5 y H6 completados; mantenimiento 2.0.2 tras rectificación paleográfica del topónimo

La arquitectura definida en `ARQUITECTURA_CHATGPT_GITHUB_DRIVE.md` está activa en `main`. GitHub es el workspace canónico del proyecto vivo. Google Drive queda reservado al PDF autoritativo en solo lectura.

## H3 validado

- CI en Windows y Ubuntu, Python 3.10 y 3.13: PASS.
- Bootstrap Web/Desktop y skill real: PASS.
- PDF de Drive como archivo real sin Base64: PASS.
- Escritura Git reversible, atomicidad multiarchivo y concurrencia por `base_sha`: PASS.

## H4 completado

- Cutover fast-forward de `main` mediante `update_ref(..., force=false)`: PASS.
- Verificación post-cutover y CI: PASS.

## H5 completado

- Primer ciclo editorial real sobre `main`: Portada validada y cerrada.
- D-001 resuelta como cruz invocativa reconocible (`†`).
- Estado resultante entonces: `reverso_portada`, página 2 `left`, sin dudas abiertas, `operation.status: clean`.
- Continuidad desde otro ordenador mediante Chat normal + `PROJECT.md` + GitHub `main`: PASS.

## H6 completado

- Inventario final de Drive contrastado con GitHub: 32 archivos de texto preservados en GitHub y dos copias binarias idénticas del PDF en el legado previo.
- PDF canónico conservado con file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`, nombre original, 5.038.575 bytes y SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`.
- PDF movido a la raíz de la carpeta canónica de Drive conservando su file ID.
- La eliminación permanente del legado fue bloqueada por los controles de seguridad de la plataforma; no se produjo ningún borrado parcial.
- Como alternativa segura y reversible, las siete carpetas antiguas fueron retiradas de la carpeta canónica y agrupadas en la carpeta hermana `Sorrios - legado Drive retirado 2026-09-06` (ID `1cdycMdPbmP_-AXJgn2UnxiCrc_TZeUSh`).
- La carpeta canónica `Sorrios - Catastro Ensenada` (ID `1gS8ZUgCxdYuJmb3TCWAN-nYo_Rjds6tJ`) contiene exactamente un elemento: el PDF autoritativo.
- Acceso posterior al PDF: archivo real, sin Base64, mismo tamaño y hash.
- En el cierre de H6 se conservó intacto el estado editorial existente en ese momento.

## Mantenimiento posterior — versión 2.0.1

- Cerrada la reparación retrospectiva de Notas históricas hasta `folio_309r` contra el plan aprobado.
- Confirmadas cuatro Notas históricas puntuales en tres unidades: `Sorribas`/Sorrios en Portada; `Concejo de Ordas` y `abogado De los R[eale]s Consejos` en folio 306r; identificación del `Conde De Luna` en folio 307r.
- Confirmados los derivados B en Glosario e índices; `legua` y `baras` permanecen sin equivalencia métrica fijada por falta de seguridad suficiente.
- `editorial-procedure.md` incorpora el checkpoint obligatorio A/B/C/D y la decisión positiva sobre si una unidad necesita Nota histórica o puede quedar justificadamente sin ella.
- Plugin y skill promovidos a 2.0.1; validador, manifiesto, paquete de herramientas y plantilla de proyecto quedan alineados con esa versión.
- La plantilla de `proyecto.yaml` queda además alineada con Manual Editorial 1.6 y Edición crítica 3.5.
- Estado editorial preservado: `last_closed_unit: folio_309r`, `current_unit: folio_309v`, `operation.status: clean`.
- El Estudio Histórico continúa desactivado y el PDF permanece fuera de GitHub y en solo lectura en Drive.


## Mantenimiento posterior — versión 2.0.2

- Releídas visualmente las cuatro apariciones del topónimo en Portada, folio 306r y folio 306v; se fija `Sorribos` como lectura manuscrita.
- La lectura anterior `Sorribas` queda rectificada como error paleográfico del proyecto; los documentos de archivo se preservan con errata explícita.
- Edición Crítica promovida a v3.6; Estudio Histórico a v1.1; introducción, criterios y edición modernizada a v1.2.
- Índice de topónimos ampliado con PARES 1715, estudio toponímico de Álvarez-Balbuena, Gaceta de Madrid y forma moderna Sorrios.
- Plugin y skill promovidos a 2.0.2; manifiesto, `proyecto.yaml`, `pyproject.toml`, validador y plantilla alineados.
- El estado editorial terminal y `operation.status: clean` no cambian; el PDF autoritativo permanece fuera de GitHub y sin modificación en Drive.

## Mantenimiento posterior — validación histórica de 19 de septiembre de 2026

- Estudio Histórico 1.2 auditado fuente por fuente y validado; 17 entradas PASS, ocho PASS condicionadas y ninguna retirada.
- Corregida la atribución bibliográfica del testimonio de 1215; normalizados enlaces institucionales sin cambiar el contenido histórico.
- Introducción y edición modernizada promovidas a 1.3; índice rector a 1.4; creado Plan de composición 0.4.
- Edición Crítica v3.6, Manual Editorial 1.6, estado terminal, unidades y PDF autoritativo permanecen sin cambios.

## Resultado final de la migración

H1-H6: **PASS**.

El uso normal del proyecto queda sustentado por:

- GitHub `main` como workspace canónico vivo;
- `PROJECT.md` para Chat normal Web/Desktop;
- `editar-catastro-sorrios` para entornos con skills;
- Google Drive exclusivamente como ubicación activa del PDF autoritativo.

La carpeta de legado retirada se conserva fuera del workspace activo como respaldo reversible; no forma parte de las fuentes canónicas.

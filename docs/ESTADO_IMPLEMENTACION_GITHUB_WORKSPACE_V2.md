# Estado de implementación — GitHub workspace v2

**Fecha:** 6 de septiembre de 2026  
**Rama canónica:** `main`  
**Versión activa:** 2.0.0  
**Estado:** H1, H2, H3, H4, H5 y H6 completados

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
- Estado resultante: `reverso_portada`, página 2 `left`, sin dudas abiertas, `operation.status: clean`.
- Continuidad desde otro ordenador mediante Chat normal + `PROJECT.md` + GitHub `main`: PASS.

## H6 completado

- Inventario final de Drive contrastado con GitHub: 32 archivos de texto preservados en GitHub y dos copias binarias idénticas del PDF en el legado previo.
- PDF canónico conservado con file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`, nombre original, 5.038.575 bytes y SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`.
- PDF movido a la raíz de la carpeta canónica de Drive conservando su file ID.
- La eliminación permanente del legado fue bloqueada por los controles de seguridad de la plataforma; no se produjo ningún borrado parcial.
- Como alternativa segura y reversible, las siete carpetas antiguas fueron retiradas de la carpeta canónica y agrupadas en la carpeta hermana `Sorrios - legado Drive retirado 2026-09-06` (ID `1cdycMdPbmP_-AXJgn2UnxiCrc_TZeUSh`).
- La carpeta canónica `Sorrios - Catastro Ensenada` (ID `1gS8ZUgCxdYuJmb3TCWAN-nYo_Rjds6tJ`) contiene exactamente un elemento: el PDF autoritativo.
- Acceso posterior al PDF: archivo real, sin Base64, mismo tamaño y hash.
- GitHub conserva intacto el estado editorial posterior a H5.

## Resultado final de la migración

H1-H6: **PASS**.

El uso normal del proyecto queda sustentado por:

- GitHub `main` como workspace canónico vivo;
- `PROJECT.md` para Chat normal Web/Desktop;
- `editar-catastro-sorrios` para entornos con skills;
- Google Drive exclusivamente como ubicación activa del PDF autoritativo.

La carpeta de legado retirada se conserva fuera del workspace activo como respaldo reversible; no forma parte de las fuentes canónicas.

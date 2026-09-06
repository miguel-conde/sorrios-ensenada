# Validación H6 — limpieza de Drive y retirada de legado

**Fecha:** 6 de septiembre de 2026  
**Resultado:** PASS  
**Rama canónica:** `main`

## Precondiciones

- H1-H5: PASS.
- GitHub `main`: workspace canónico vivo.
- Inventario de Drive completado antes de modificar la estructura.

## Inventario previo

La carpeta canónica de Drive contenía siete carpetas de la arquitectura anterior, 32 archivos de texto y dos copias del PDF.

Los textos vivos e históricos necesarios estaban ya preservados en GitHub bajo `project/` y `project/90_ARCHIVO/`.

La copia histórica del PDF tenía el mismo tamaño y el mismo SHA-256 que el PDF canónico.

## PDF canónico

- Nombre: `sorrios_ensenada_orden_lectura_calidad_original.pdf`
- File ID: `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`
- Tamaño: 5.038.575 bytes
- SHA-256: `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- MIME: `application/pdf`

Se movió desde `10_FUENTE_PRIMARIA/` a la raíz de la carpeta canónica `Sorrios - Catastro Ensenada` conservando el mismo file ID y los mismos bytes.

Tras el movimiento se descargó nuevamente como archivo real, con `b64_string: null`, y se verificaron de nuevo tamaño y hash.

## Retirada del legado

Las siete carpetas antiguas se retiraron de la carpeta canónica y se agruparon en una carpeta hermana de archivo reversible:

- `Sorrios - legado Drive retirado 2026-09-06`
- ID `1cdycMdPbmP_-AXJgn2UnxiCrc_TZeUSh`

Contenido retirado:

- `00_CONTROL`
- `10_FUENTE_PRIMARIA`
- `20_TRABAJO_EDITORIAL`
- `30_RESULTADOS`
- `90_ARCHIVO`
- `FUENTES ACTIVAS`
- `FUERA DEL CONTEXTO ACTIVO`

La retirada reversible sustituye a la eliminación física prevista inicialmente, que no estaba disponible a través de la superficie utilizada.

## Estado final de Drive

La carpeta canónica `Sorrios - Catastro Ensenada` (ID `1gS8ZUgCxdYuJmb3TCWAN-nYo_Rjds6tJ`) contiene exactamente un elemento:

```text
sorrios_ensenada_orden_lectura_calidad_original.pdf
```

No queda ningún texto ni carpeta de control dentro del workspace canónico de Drive.

## Comprobación de independencia de GitHub

Después de limpiar Drive se releyó `project/00_CONTROL/estado.yaml` directamente desde GitHub `main` y se confirmó:

- `last_validated_unit: portada`
- `last_closed_unit: portada`
- `current_unit: reverso_portada`
- `next_unit: folio_306r`
- `current_location.pdf_page: 2`
- `current_location.position: left`
- `open_issues: []`
- `operation.status: clean`

## Veredicto

**H6: PASS.**

GitHub conserva todo el workspace vivo y la carpeta canónica de Google Drive queda dedicada exclusivamente al PDF autoritativo. El legado permanece fuera del workspace activo como archivo reversible.

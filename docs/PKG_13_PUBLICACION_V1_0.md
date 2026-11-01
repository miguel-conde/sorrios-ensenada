# PKG-13 — Publicación definitiva de v1.0

**Estado:** `COMPLETADA`<br>
**Veredicto:** `PKG-13 PASS — v1.0 PUBLICADA`

## Identidad de la publicación

| Campo | Valor |
|---|---|
| Fecha oficial | 1 de noviembre de 2026 |
| Hora técnica de publicación | `2026-11-01T08:19:29.483+01:00` (`Europe/Madrid`) |
| `GATE05_TARGET` | `3421a0cda2432bec3e52fb6a5e56c0a4deb36c63` |
| Source SHA del artefacto | `58f669d5c9aac9d2e8d960484f828506beb6ae71` |
| Deploy publicado | `6ae6435a5695ab37b483c758` |
| Site ID | `1539a52a-d500-426f-9995-7db9c01e6d45` |
| URL canónica | <https://sorribos-santibanez-1752.netlify.app/> |

Netlify promovió mediante **Publish Deploy** el mismo deploy atómico aprobado
en GATE-05. No hubo render, reconstrucción, nueva subida, nuevo deploy, build
remoto ni integración Git. Antes de la promoción, production no tenía un
deploy publicado y la URL canónica respondía HTTP 404; ese es el estado de
rollback documental de esta primera publicación.

## Inventario e integridad

| Objeto | Identidad verificada |
|---|---|
| Web | 40 HTML; 120 archivos sin PDF; 74.657.837 bytes |
| Manifest web SHA-256 | `67b1d03ae63d33886121daefda72f1479382227f25643eb52341aad6be59a29f` |
| Manifest completo SHA-256 | `e49e1e50f0f5a43dbe0c78bfd15b131afd37e1e40cd51af7ad39ddd0c5c9333a` |
| PDF | 360 páginas; 71.029.142 bytes |
| PDF SHA-256 | `e6b00d65876a5c5a20f2327bde39d624ba1f6da82b1b40d18a57b055fd8de470` |
| Inventario Netlify | 121/121 archivos |

La URL canónica y los 40 documentos HTML responden HTTP 200. Portada,
prólogo, «Cómo citar», colofón, facsímil, transcripción, edición modernizada,
estudio histórico, índices, CSS, JavaScript y recursos principales fueron
comprobados. El PDF público responde HTTP 200 y es idéntico byte a byte al
aprobado. Canonical, versión 1.0, fecha, idioma, autor, repositorio, Issues y
correo público son correctos. El colofón y la firma del prólogo conservan los
textos aprobados.

El `published_deploy.id` es `6ae6435a5695ab37b483c758`, los builds remotos
permanecen en cero y el site sigue sin integración Git.

## Release

- Tag anotado `v1.0`: creado sobre el commit final de PKG-13 y verificado en
  <https://github.com/miguel-conde/sorrios-ensenada/tree/v1.0>.
- GitHub Release pública `v1.0 — Sorribos y Santibáñez de Ordás en 1752`:
  creada, no draft, no prerelease y verificada en
  <https://github.com/miguel-conde/sorrios-ensenada/releases/tag/v1.0>.
- La Release no adjunta binarios nuevos; remite al PDF canónico identificado
  por su SHA-256.

No quedan operaciones pendientes para v1.0. Cualquier corrección posterior
debe ser una nueva modificación versionada y no puede alterar silenciosamente
este tag, esta Release ni el deploy publicado.

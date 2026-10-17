# LINK-01 — Auditoría integral de enlaces

**Fecha de comprobación:** 17 de octubre de 2026

**Base auditada:** `feature/quarto-book@9056b94783373c77460755915df2703472c45059`

**Tipo:** T1, auditoría técnica/editorial; no se ha corregido ningún enlace.

## Veredicto

**ENLACES LISTOS PARA CORRECCIÓN LOCALIZADA EN E3**

La navegación publicada no presenta destinos internos rotos: las 1.284
ocurrencias internas de las fuentes tienen destino material y las 4.190
referencias `href` del HTML existente resuelven archivo y, cuando procede,
ancla. Sí hay cuatro enlaces fuente obsoletos al antiguo prototipo vertical,
un DOI bibliográfico que devuelve 404, URLs institucionales antiguas que
redirigen y varios destinos no verificables automáticamente. Son correcciones
técnicas localizadas; ninguna exige una decisión histórica o editorial humana
nueva.

## Alcance y método

- Se recorrieron los 39 documentos declarados por `_quarto.yml`, sus 1.345
  enlaces Markdown, `references.bib`, los aparatos e índices generados
  existentes y la procedencia cartográfica versionada.
- Se comprobaron 60 destinos externos activos únicos: 24 bibliográficos y 36
  documentales, institucionales o de procedencia. La ficha alternativa de
  GREDOS `10366/151409`, todavía no enlazada, se comprobó además para resolver
  el caso obligatorio.
- Las peticiones usaron cuatro conexiones como máximo, una descarga parcial de
  128 KiB y un solo reintento focal cuando hubo timeout o reinicio de conexión.
  No se eludieron bloqueos ni se descargaron PDF completos.
- La verificación semántica contrastó títulos o cabeceras cuando la landing los
  ofrecía y, para PDF o fichas opacas, los identificadores ya documentados en
  el registro, la bibliografía y los dossiers de PKG-02/08.
- Se excluyeron los namespaces XML/SVG y las constantes de servicios que no son
  enlaces navegables. Se incluyeron los endpoints y consultas reales guardados
  en `assets/cartography/cartography.json` por su función de trazabilidad.

## Caso GREDOS / 10366/151409

| Comprobación | Resultado |
|---|---|
| `https://hdl.handle.net/10366/151409` | El GET agotó el timeout y una comprobación focal HEAD devolvió HTTP 500 desde Cloudflare; no se obtuvo una cadena de redirección completa. Estado: `TIMEOUT`, no `BROKEN`. |
| `https://gredos.usal.es/handle/10366/151409` | HTTP 200, pero entrega el desafío anti-bot «Making sure you're not a bot!». Estado: `BLOCKED_AUTOMATION`. |
| Bitstream directo hoy usado por `TOP-005` | HTTP 200 con el mismo desafío anti-bot; además es una URL de descarga más frágil que la ficha. Estado: `BLOCKED_AUTOMATION`. |
| Correspondencia semántica | El identificador `10366/151409`, el título y la autoría de Santano Valbuena coinciden con la referencia y con `TOP-005`; no se detectó un recurso distinto. |

**Recomendación: conservar ambos.** Mantener el handle como identificador
persistente de la referencia bibliográfica y ofrecer la ficha institucional de
GREDOS como alternativa legible; sustituir en la matriz el bitstream directo
por la ficha. No usar URLs de sesión ni convertir el bloqueo de automatización
en diagnóstico de enlace roto.

## Resumen agregado

Las clases «internos» y «navegación documental» se solapan deliberadamente: la
segunda es el subconjunto de navegación facsímil, transcripción, modernización,
aparatos e índices.

| Clase | Total | OK | Redirigidos | Rotos | Bloqueados | Pendientes |
|---|---:|---:|---:|---:|---:|---:|
| Externos no bibliográficos, incluida procedencia cartográfica | 36 | 29 | 2 | 0 | 3 | 2 |
| Internos en fuentes | 1.284 | 1.280 | 0 | 0 | 0 | 4 |
| Bibliográficos | 24 | 13 | 5 | 1 | 1 | 4 |
| Navegación documental | 1.205 | 1.205 | 0 | 0 | 0 | 0 |

En «Pendientes» se agrupan `TIMEOUT`, `TLS/DNS_ERROR` y los cuatro enlaces
internos `OBSOLETO`. Los HTTP 400 de los tres endpoints WFS desnudos no se
cuentan como rotos: sin parámetros esa respuesta es la esperable y las seis
consultas WFS registradas respondieron 200 con el recurso solicitado.

## Matriz de resultados externos y bibliográficos

| ID | Ubicación | URL/destino | Tipo | Estado | Acción recomendada | Prioridad |
|---|---|---|---|---|---|---|
| B-001 | `references.bib` / `jularconflictos` | `https://www.historiaagraria.com/FILE/articulos/HA13_jular.pdf` | BIBLIOGRÁFICO | OK | CONSERVAR | BAJA |
| B-002 | `references.bib` / `santanovalbuena2022documentos` | `https://hdl.handle.net/10366/151409` | BIBLIOGRÁFICO | TIMEOUT | INVESTIGAR EN E3 | ALTA |
| B-003 | `references.bib` / `sanchezbadiola2019nobiliario` | `https://dialnet.unirioja.es/servlet/libro?codigo=770795` | BIBLIOGRÁFICO | OK | CONSERVAR | BAJA |
| B-004 | `references.bib` / `pares1715santibanez` | `https://pares.mcu.es/ParesBusquedas20/catalogo/description/12805146` | BIBLIOGRÁFICO | REDIRECT_OK / SUPERSEDED | ACTUALIZAR | MEDIA |
| B-005 | `references.bib` / `relacionparroquial1768` | `https://scrinia.org/wp-content/uploads/2021/12/Memoria-Ecclesiae-28.pdf` | BIBLIOGRÁFICO | OK | CONSERVAR | BAJA |
| B-006 | `references.bib` / `gaceta1864sorribos` | `https://www.boe.es/gazeta/dias/1864/09/07/pdfs/GMD-1864-251.pdf` | BIBLIOGRÁFICO | OK | CONSERVAR | BAJA |
| B-007 | `references.bib` / `alvarezbalbuenatoponimia` | `https://buleria.unileon.es/handle/10612/12285` | BIBLIOGRÁFICO | BLOCKED_AUTOMATION | ACTUALIZAR | MEDIA |
| B-008 | `references.bib` / `ayuntamientosantamariaordassantibanez` | `https://www.aytosantamariadeordas.es/los-pueblos/santibanez-de-ordas/` | BIBLIOGRÁFICO | OK | CONSERVAR | BAJA |
| B-009 | `references.bib` / `pousadieguez2022juzgados` | `https://fh.mdp.edu.ar/revistas/index.php/magallanica/article/view/6817` | BIBLIOGRÁFICO | OK | CONSERVAR | BAJA |
| B-010 | `references.bib` / `paresconde1742` | `https://pares.mcu.es/ParesBusquedas20/catalogo/description/3925721` | BIBLIOGRÁFICO | REDIRECT_OK / SUPERSEDED | ACTUALIZAR | MEDIA |
| B-011 | `references.bib` / `parestituloabogado` | `https://pares.mcu.es/ParesBusquedas20/catalogo/description/1547060` | BIBLIOGRÁFICO | REDIRECT_OK / SUPERSEDED | ACTUALIZAR | MEDIA |
| B-012 | `references.bib` / `camarerobullon2002catastro` | `https://www.catastro.hacienda.gob.es/documentos/publicaciones/ct/ct46/06.%20Concepcion%20Camarero.pdf` | BIBLIOGRÁFICO | OK | CONSERVAR | BAJA |
| B-013 | `references.bib` / `castanoalvarez2017apuntes` | `https://www.e-medida.es/numero-12/meros-apuntes-metrologicos-provenientes-de-la-medicion-de-la-tierra-agraria-repoblacion-y-repartimientos-desde-la-edad-media-al-siglo-xvi/` | BIBLIOGRÁFICO | OK | CONSERVAR | BAJA |
| B-014 | `references.bib` / `bartolomebartolome2001comercio` | `https://hdl.handle.net/10366/70337` | BIBLIOGRÁFICO | TIMEOUT | INVESTIGAR EN E3 | MEDIA |
| B-015 | `references.bib` / `sanchezlopezdevinuesa2001cultivos` | `https://www.modernalia.es/items/show/2587` | BIBLIOGRÁFICO | OK | CONSERVAR | BAJA |
| B-016 | `references.bib` / `riescochueca2013lexico` | `https://idus.us.es/server/api/core/bitstreams/f727d611-1345-4de8-84ed-a60f90ab56fe/content` | BIBLIOGRÁFICO | OK | CONSERVAR | BAJA |
| B-017 | `references.bib` / `cortizoalvarez1984ganado` | `https://doi.org/10.17811/er.0.1984.71-94` | BIBLIOGRÁFICO | BROKEN | SUSTITUIR | ALTA |
| B-018 | `references.bib` / `zapicogutierrez2016molinos` | `https://doi.org/10.35376/10324/22081` | BIBLIOGRÁFICO | TIMEOUT | INVESTIGAR EN E3 | MEDIA |
| B-019 | `references.bib` / `hernandezcubero2018recursos` | `https://doi.org/10.14201/shhmo2018402233269` | BIBLIOGRÁFICO | REDIRECT_OK | CONSERVAR | BAJA |
| B-020 | `references.bib` / `reycastelao1985voto` | `https://dialnet.unirioja.es/descarga/articulo/246923.pdf` | BIBLIOGRÁFICO | OK | CONSERVAR | BAJA |
| B-021 | `references.bib` / `mazazorrilla1982pobreza` | `https://uvadoc.uva.es/bitstream/handle/10324/21203/Investigaciones-1982-03-Pobreza-Hospitalidad-Publica-Ciudad-Valladolid.pdf` | BIBLIOGRÁFICO | TIMEOUT | INVESTIGAR EN E3 | MEDIA |
| B-022 | `references.bib` / `paresmesta` | `https://pares.mcu.es/ParesBusquedas20/catalogo/description/172318` | BIBLIOGRÁFICO | REDIRECT_OK / SUPERSEDED | ACTUALIZAR | MEDIA |
| B-023 | `references.bib` / `garciagarcia1986haciendas` | `https://dialnet.unirioja.es/descarga/articulo/785131.pdf` | BIBLIOGRÁFICO | OK | CONSERVAR | BAJA |
| B-024 | `references.bib` / `caputvallis2008catastro` | `https://caboalles.wordpress.com/2008/09/29/catastro-de-ensenada-ano-1752/` | BIBLIOGRÁFICO | OK | CONSERVAR | BAJA |
| E-001 | Edición crítica / índice de instituciones | `https://censoarchivos.cultura.gob.es/CensoGuia/fondoDetail.htm?archivoId=9&eventDescendiente=descendienteDetail&id=1248343` | EXTERNO | OK | CONSERVAR | BAJA |
| E-002 | Créditos y colofón | `https://creativecommons.org/licenses/by/4.0/deed.es` | EXTERNO | OK | CONSERVAR | BAJA |
| E-003 | Matriz / `TOP-006` | `https://dialnet.unirioja.es/descarga/libro/770795.pdf` | EXTERNO | OK / DUPLICATE | CONSERVAR | BAJA |
| E-004 | Glosario / `negrillos` | `https://dle.rae.es/negrillo` | EXTERNO | OK | CONSERVAR | BAJA |
| E-005 | Glosario / `pan` | `https://dle.rae.es/pan` | EXTERNO | OK | CONSERVAR | BAJA |
| E-006 | Matriz / `TOP-005` | `https://gredos.usal.es/bitstream/handle/10366/151409/SANTANO%20VALBUENA%2C%20FERNANDO%20-%20TFG.pdf?isAllowed=y&sequence=1` | EXTERNO | BLOCKED_AUTOMATION / DUPLICATE | SUSTITUIR | MEDIA |
| E-007 | Matriz / `AGR-011` | `https://gredos.usal.es/handle/10366/70337` | EXTERNO | BLOCKED_AUTOMATION / DUPLICATE | CONSERVAR | BAJA |
| E-008 | Capítulo 1 | `https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=10` | EXTERNO | OK | CONSERVAR | BAJA |
| E-009 | Capítulo 2 | `https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=30` | EXTERNO | OK | CONSERVAR | BAJA |
| E-010 | Capítulo 2 | `https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=31b` | EXTERNO | OK | CONSERVAR | BAJA |
| E-011 | Capítulos 1–2 | `https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=32` | EXTERNO | OK | CONSERVAR | BAJA |
| E-012 | Capítulo 1 | `https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=33` | EXTERNO | OK | CONSERVAR | BAJA |
| E-013 | Capítulo 1 | `https://pares.cultura.gob.es/catastro/servlets/ServletController?accion=2&opcion=40` | EXTERNO | OK | CONSERVAR | BAJA |
| E-014 | Edición crítica / índice de instituciones | `https://pares.mcu.es/ParesBusquedas20/catalogo/description/478437` | EXTERNO | REDIRECT_OK / SUPERSEDED | ACTUALIZAR | MEDIA |
| E-015 | Edición crítica / índice de instituciones | `https://pares.mcu.es/ParesBusquedas20/catalogo/description/480016` | EXTERNO | REDIRECT_OK / SUPERSEDED | ACTUALIZAR | MEDIA |
| E-016 | Matriz / `GAN-008` | `https://reunido.uniovi.es/index.php/RCG/article/download/894/824` | EXTERNO | OK | CONSERVAR | BAJA |
| E-017 | Edición crítica | `https://revistas.unileon.es/index.php/anada/article/view/6165` | EXTERNO | OK | CONSERVAR | BAJA |
| E-018 | Matriz / `HID-008` | `https://uvadoc.uva.es/handle/10324/22081` | EXTERNO | TIMEOUT / DUPLICATE | INVESTIGAR EN E3 | MEDIA |
| E-019 | Capítulo 2 | `https://www.catastro.hacienda.gob.es/documentos/publicaciones/catalogoensenada_1752_vera.pdf` | EXTERNO | OK | CONSERVAR | BAJA |
| E-020 | Capítulo 1 | `https://www.catastro.hacienda.gob.es/es-ES/fondo_editorial.html` | EXTERNO | OK | CONSERVAR | BAJA |
| E-021 | Glosario / `boto` | `https://www.juntadeandalucia.es/organismos/culturapatrimoniohistoricoydeporte/areas/cultura/archivos/archivos-consejeria/archivo-historico-provincial-granada/ahpg-recomienda/paginas/documento-ahpg-sep-2012.html` | EXTERNO | OK | CONSERVAR | BAJA |
| E-022 | Glosario / `Ferrañales` y `pelo` | `https://www.mapa.gob.es/en/ministerio/servicios/informacion/Parte7_tcm38-102783.pdf` | EXTERNO | TLS/DNS_ERROR | SUSTITUIR | ALTA |
| E-023 | Matriz / `HID-008` | `https://www.researchgate.net/publication/330029888_Recursos_naturales_y_molienda_a_mediados_del_siglo_XVIII_la_Tierra_de_Campos` | EXTERNO | BLOCKED_AUTOMATION / DUPLICATE | ELIMINAR | MEDIA |
| C-001 | Procedencia cartográfica | `https://centrodedescargas.cnig.es/CentroDescargas/detalleArchivo?sec=12633136` | EXTERNO | OK | CONSERVAR | BAJA |
| C-002 | Procedencia cartográfica | `https://centrodedescargas.cnig.es/CentroDescargas/detalleArchivo?sec=9000001` | EXTERNO | OK | CONSERVAR | BAJA |
| C-003 | Procedencia cartográfica | `https://centrodedescargas.cnig.es/CentroDescargas/detalleArchivo?sec=9000029` | EXTERNO | OK | CONSERVAR | BAJA |
| C-004 | Procedencia cartográfica | `https://servicios.idee.es/wfs-inspire/hidrografia` | EXTERNO | OK | CONSERVAR | BAJA |
| C-005 | Procedencia cartográfica | `https://servicios.idee.es/wfs-inspire/hidrografia?service=WFS&version=2.0.0&request=GetFeature&typeNames=hy-p%3AWatercourse&srsName=EPSG%3A4326&bbox=-5.9%2C42.68%2C-5.74%2C42.78%2CEPSG%3A4326` | EXTERNO | OK | CONSERVAR | BAJA |
| C-006 | Procedencia cartográfica | `https://www.ign.es/resources/licencia/Condiciones_licenciaUso_IGN.pdf` | EXTERNO | OK | CONSERVAR | BAJA |
| C-007 | Procedencia cartográfica | `https://www.ign.es/wfs-inspire/ngbe` | EXTERNO | OK | CONSERVAR | BAJA |
| C-008 | Procedencia cartográfica | `https://www.ign.es/wfs-inspire/ngbe?service=WFS&version=2.0.0&request=GetFeature&typeNames=gn%3ANamedPlace&outputFormat=application%2Fgeo%2Bjson&srsName=EPSG%3A4326&bbox=-5.9%2C42.68%2C-5.74%2C42.78%2CEPSG%3A4326` | EXTERNO | OK | CONSERVAR | BAJA |
| C-009 | Procedencia cartográfica | `https://www.ign.es/wfs-inspire/unidades-administrativas` | EXTERNO | OK | CONSERVAR | BAJA |
| C-010 | Procedencia cartográfica | consulta WFS `resourceId=AU_ADMINISTRATIVEUNIT_34000000000` | EXTERNO | OK | CONSERVAR | BAJA |
| C-011 | Procedencia cartográfica | consulta WFS `resourceId=AU_ADMINISTRATIVEUNIT_34072400000` | EXTERNO | OK | CONSERVAR | BAJA |
| C-012 | Procedencia cartográfica | consulta WFS `resourceId=AU_ADMINISTRATIVEUNIT_34072424133` | EXTERNO | OK | CONSERVAR | BAJA |
| C-013 | Procedencia cartográfica | consulta WFS `resourceId=AU_ADMINISTRATIVEUNIT_34072424158` | EXTERNO | OK | CONSERVAR | BAJA |

## Enlaces externos problemáticos

1. El DOI `10.17811/er.0.1984.71-94` devuelve 404 «DOI Not Found». La propia
   matriz ya usa el PDF institucional de Uniovi que respondió 200 y corresponde
   a la obra; `references.bib` debe dejar de publicar el DOI inválido.
2. Las seis URLs `pares.mcu.es` redirigen correctamente a la misma ruta bajo
   `pares.cultura.gob.es`. Conviene actualizar la fuente estable y evitar
   depender del dominio heredado.
3. La URL de MAPA falla la validación TLS por una cadena con certificado
   autofirmado. Al ser visible en dos entradas del glosario, E3 debe localizar
   una landing institucional vigente o una copia institucional estable.
4. Bulería y GREDOS entregan un desafío anti-bot; ResearchGate devuelve 403.
   No se clasifican como rotos. Bulería tiene una landing editorial accesible
   ya registrada en la edición crítica; ResearchGate duplica el DOI válido de
   la misma obra y no aporta robustez.
5. DOI/UvaDoc `10324/22081`, los dos handles de Salamanca y el bitstream de
   UvaDoc no alcanzaron un destino final estable durante la ventana de prueba.
   Se conservan como `TIMEOUT` pendientes de una comprobación humana normal en
   navegador durante E3, sin ampliar la investigación histórica.

## Enlaces internos problemáticos

| ID | Ubicación | URL/destino | Tipo | Estado | Acción recomendada | Prioridad |
|---|---|---|---|---|---|---|
| I-001 | `content/02-estudio/09-rio-molinos-recursos.qmd` | `14-facsimil-prototipo.qmd#pagina-digital-12` | INTERNO | OBSOLETO | ACTUALIZAR | MEDIA |
| I-002 | mismo archivo | `15-transcripcion-prototipo.qmd#folio-315v` | INTERNO | OBSOLETO | ACTUALIZAR | MEDIA |
| I-003 | mismo archivo | `16-modernizada-prototipo.qmd#respuesta-17` | INTERNO | OBSOLETO | ACTUALIZAR | MEDIA |
| I-004 | mismo archivo | `aparato-molinos.qmd#matriz-molinera` | INTERNO | OBSOLETO | ACTUALIZAR | MEDIA |
| I-005 | 39 documentos del libro | otros 1.280 enlaces fuente | INTERNO | OK | CONSERVAR | BAJA |
| I-006 | HTML existente | 4.190 referencias internas con archivo/ancla | INTERNO | OK | CONSERVAR | BAJA |

Los cuatro destinos obsoletos existen todavía como artefactos de regresión,
pero no forman parte del libro. `fix_rendered_links.py` los sustituye hoy por
los capítulos 14–16 y `#evidencia-hid-001`; por eso el HTML resultante no está
roto. E3 debe enlazar las fuentes reales directamente y retirar esta deuda de
compatibilidad, ajustando sus pruebas, sin editar `generated/`.

No se detectaron rutas absolutas locales, enlaces al source tree visibles en el
HTML, anclas inexistentes, retornos de matriz sin destino ni referencias a
headings renombrados. TOC, preliminares, bibliografía, «Cómo citar», glosario,
cuestiones abiertas y los nueve índices resuelven estructuralmente.

## Bibliografía

- Hay 24 fuentes activas, 24 registros BibTeX y 24 claves citadas; no faltan
  claves y no quedan registros activos sin cita.
- Las 24 entradas tienen URL; tres registran además DOI. Uno de esos DOI es el
  roto descrito en B-017 y contradice el destino institucional funcional usado
  para la misma obra en `GAN-008`.
- `BIB-012` y `TRA-006` no reaparecen en la publicación vigente.
- `BIB-015` (`camarerobullon2002catastro`) solo respalda el contexto doméstico
  acotado de `DEM-005`.
- `TOP-006` aparece solo en la matriz. Su landing de Dialnet y su PDF directo
  son duplicados funcionales, pero la primera sirve a la bibliografía y el
  segundo a la evidencia de matriz; no se propone ampliar su uso narrativo.
- Los modelos de cita mantienen 11/11 objetos. Los marcadores de URL canónica
  son diferimientos, no claves ni enlaces rotos.

## Navegación facsímil/transcripción

| ID | Ubicación | URL/destino | Tipo | Estado | Acción recomendada | Prioridad |
|---|---|---|---|---|---|---|
| F-001 | Capítulo 14 | 18 páginas `#pagina-digital-01`–`18` | FACSÍMIL | OK | CONSERVAR | BAJA |
| F-002 | Capítulo 14 → 15 | 35/35 unidades | FACSÍMIL | OK | CONSERVAR | BAJA |
| F-003 | Capítulo 15 → 14 | 35/35 unidades, 70 ocurrencias de enlace | FACSÍMIL | OK | CONSERVAR | BAJA |
| F-004 | Capítulo 16 → 15 | 65 remisiones materiales | FACSÍMIL | OK | CONSERVAR | BAJA |
| M-001 | Matriz D/C/I/E/L | 111 anclas `#evidencia-*` únicas y 244 retornos | MATRIZ | OK | CONSERVAR | BAJA |
| M-002 | Cuestiones abiertas | 9 QA1 y 18 enlaces a capítulo/matriz | MATRIZ | OK | CONSERVAR | BAJA |
| M-003 | Glosario | 28 anclas únicas y 169 remisiones internas | MATRIZ | OK | CONSERVAR | BAJA |
| M-004 | Concordancia | 87 enlaces a facsímil, 100 a transcripción y 110 a modernización | MATRIZ | OK | CONSERVAR | BAJA |
| M-005 | Nueve índices | 272 localizadores internos | MATRIZ | OK | CONSERVAR | BAJA |

La navegación documental auditada suma 1.205 enlaces internos. Todos sus
destinos y fragmentos existen. Los localizadores de página y posición coinciden
con `unidades.yaml`; quedan cubiertas 18/18 páginas y 35/35 unidades en ambas
direcciones previstas.

## Placeholders autorizados

| ID | Ubicación | URL/destino | Tipo | Estado | Acción recomendada | Prioridad |
|---|---|---|---|---|---|---|
| P-001 | `content/06-aparatos/como-citar.qmd` | diez modelos con `[URL canónica pendiente]` | PLACEHOLDER | DIFERIMIENTO AUTORIZADO | RESOLVER ANTES DE RELEASE | ALTA |
| P-002 | `content/06-aparatos/colofon.qmd` | fecha exacta y URL canónica diferidas | PLACEHOLDER | DIFERIMIENTO AUTORIZADO | RESOLVER ANTES DE RELEASE | ALTA |
| P-003 | futura sección «Correcciones y contacto» | email todavía ausente | PLACEHOLDER | DIFERIMIENTO AUTORIZADO | RESOLVER ANTES DE RELEASE | ALTA |
| P-004 | futura referencia al repositorio público | URL todavía ausente | PLACEHOLDER | DIFERIMIENTO AUTORIZADO | RESOLVER ANTES DE RELEASE | ALTA |

P-001 y P-002 son visibles al lector. P-003 y P-004 todavía no aparecen: E3
debe incorporar los placeholders acordados, sin inventar valores. La URL
canónica, el correo y la URL pública real deben quedar resueltos antes del
release; la preparación del repositorio sigue su línea separada. El ISBN
continúa ausente y no bloqueante.

## Duplicados y URLs obsoletas

- GREDOS `10366/151409`: handle bibliográfico y bitstream de matriz; conservar
  el identificador persistente, añadir la ficha y retirar el bitstream directo.
- GREDOS `10366/70337`: handle bibliográfico y ficha directa; duplicación
  aceptable si se conserva el handle como forma principal.
- Dialnet `770795`: landing bibliográfica y PDF directo de `TOP-006`; funciones
  distintas, sin convertir la fuente condicionada en apoyo narrativo.
- Cortizo Álvarez: DOI inválido frente a PDF institucional funcional de Uniovi;
  el DOI queda `SUPERSEDED` y debe sustituirse.
- Hernández/Cubero: DOI institucional y ResearchGate; eliminar el duplicado de
  ResearchGate y conservar el DOI.
- PARES: seis rutas bajo el dominio histórico `mcu.es`; actualizar al dominio
  final `cultura.gob.es` sin alterar los identificadores de descripción.

## Archivos que conviene corregir conjuntamente con E1

| Archivo | Hallazgo E1 | Hallazgo E2 | Conviene corregir conjuntamente |
|---|---|---|---|
| `publication/content/01-catastro/04-manuscrito-volumen-actual.qmd` | Jerga Quarto/front matter y rutas `publication/content/` / `generated/` visibles | Sus enlaces internos son correctos; al reescribir el pasaje no deben perderse las remisiones a capítulos 3 y 14 | Sí |
| `publication/content/02-estudio/09-rio-molinos-recursos.qmd` | Revisión lectora general del discurso técnico | Cuatro enlaces obsoletos al prototipo vertical | Sí |
| `publication/content/06-aparatos/como-citar.qmd` | Versiones y formulaciones internas visibles | Diez placeholders de URL canónica autorizados y anclas de cita que deben preservarse | Sí |
| `publication/content/06-aparatos/bibliografia.qmd` | Mención pública al archivo técnico `references.bib` | La bibliografía depende de 24 URLs; una está rota y cinco redirigen | Sí, coordinado con `references.bib` |
| `publication/content/06-aparatos/colofon.qmd` | «release», «candidata» y formulación técnica para lector | URL canónica diferida y enlace CC válido | Sí |
| `publication/generated/matriz-evidencia.qmd` | Versiones/rutas internas visibles en aparatos generados | Bitstream GREDOS, duplicados y URLs PARES heredadas | Sí, pero solo desde sus fuentes/generador; nunca editar el derivado |
| `publication/generated/15-transcripcion.qmd` | Nombres de archivos y detalles de implementación visibles | URLs PARES heredadas en notas generadas | Sí, pero solo desde la edición canónica/generador |
| `publication/generated/indices/*.qmd` | Explicaciones de implementación de índices | Destinos internos correctos; dos URLs PARES heredadas proceden de fuente canónica | Sí, desde las fuentes/generador |

`01-creditos.qmd` y `03-introduccion.qmd` conservan hallazgos E1, pero LINK-01 no
añade en ellos un defecto de enlace. Las correcciones de URLs que proceden del
Registro, Glosario o Edición Crítica exigen una operación canónica atómica
dentro de E3; no deben parchearse en `publication/generated/`.

## Validación

- `publication/scripts/validate_publication.py`: PASS.
- Focales estructurales de capítulos 14–16, aparatos, índices, bibliografía y
  trazabilidad: **14 passed**.
- Auditoría propia efímera, no versionada: 1.284 enlaces fuente internos sin
  destino ausente; 4.190 `href` internos del HTML existente sin archivo ni
  ancla ausente.
- HTTP: 60 destinos activos únicos y una ficha alternativa GREDOS; sin
  autenticación, sin evasión de bloqueos y sin descarga integral de PDF.
- 0 renders; 0 suites completas; `prepare.py` no ejecutado.

## Próximo paso

`E3 — REV-LECTOR-02 — APLICACIÓN CONJUNTA DE CORRECCIONES E1 + E2`

E3 debe corregir el DOI inválido, normalizar PARES, eliminar los cuatro enlaces
de prototipo y resolver las sustituciones GREDOS/MAPA y los duplicados señalados,
coordinándolos con los hallazgos lectores de E1. No quedan decisiones humanas
bloqueantes para iniciar esa operación.

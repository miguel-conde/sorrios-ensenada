# PKG-03 — Cartografía de orientación

**Fecha de consulta y snapshot:** 11 de octubre de 2026

**Rama de trabajo:** `pkg-03/cartografia-v1`

**Base:** `ddfa2adb9f06f7b50585dbc80f156e62c968f570`

**Estado del paquete:** `APTO PARA REVISIÓN HUMANA; NO INTEGRADO`

## 1. Alcance

PKG-03 prepara dos activos vectoriales para la edición 1.0: un mapa regional y
un mapa local. Ambos son instrumentos contemporáneos de orientación editorial.
La operación selecciona y conserva únicamente datos oficiales necesarios,
documenta derechos y procedencia, genera los SVG sin edición manual opaca y
prepara título, pie y alternativa textual. No modifica capítulos, configuración
Quarto, estilos generales, aparatos publicados, índices ni fuentes canónicas.

Los SVG quedan listos para evaluación humana. Su futura colocación en el libro
corresponde a PKG-07 y no forma parte de este paquete.

## 2. Principio de no reconstrucción histórica

Los mapas no representan el término, los caminos, las jurisdicciones, las
parroquias, los señoríos, las parcelas ni las propiedades de 1752. Los polígonos
son límites administrativos **actuales** obtenidos de BDLJE; los puntos y el
curso del río son referencias contemporáneas. La forma histórica `Sorribos`
aparece solo como aclaración editorial subordinada a `Sorrios`, sin geometría y
sin convertir el mapa en prueba de continuidad toponímica.

Ambos SVG incorporan de forma visible:

> Mapa contemporáneo de orientación. No constituye una reconstrucción de los
> límites ni de la organización territorial de 1752.

## 3. Fuentes evaluadas

| Fuente | Contenido | Autoridad | Licencia | Redistribución | Seleccionada |
|---|---|---|---|---|---|
| IGN/CNIG, BDLJE — Límites y Unidades Administrativas Actuales | España, León y municipios actuales | cartografía oficial estatal | licencia de uso IGN compatible con CC BY 4.0 | sí, incluida obra derivada con atribución | sí |
| IGN/CNIG, NGBE | topónimos y coordenadas geográficas | nomenclátor oficial del IGN; integra NGMEP y BTN25 según la entidad | licencia de uso IGN compatible con CC BY 4.0 | sí, incluida obra derivada con atribución | sí |
| SCN/IGN, IGR_HIDROGRAFIA v1 2023 | curso contemporáneo del río Luna | información geográfica de referencia | CC BY 4.0 | sí, incluida obra derivada con atribución | sí |
| IGN, IGR Redes de Transporte | red viaria contemporánea | información geográfica de referencia | licencia IGN compatible con CC BY 4.0 | jurídicamente posible con atribución | no: densidad excesiva y función editorial insuficiente |
| IGN, modelos digitales del terreno | relieve contemporáneo | información geográfica oficial | licencia IGN compatible con CC BY 4.0 | jurídicamente posible con atribución | no: no mejora la identificación de los lugares y reduce legibilidad |
| OpenStreetMap y derivados | posible base alternativa | comunidad OSM | no evaluada para incorporación porque las fuentes oficiales bastan | no necesaria para este paquete | no |
| Google Maps, Bing, Apple Maps y teselas comerciales | mapas de terceros | proveedores comerciales | condiciones ajenas al paquete | no se verificó una vía necesaria de redistribución | no |

No existe incidencia `LEGAL-CART-*`: las tres fuentes incorporadas identifican
proveedor, licencia, atribución y permiso de reutilización/redistribución.

## 4. Fuente/s elegidas

### BDLJE

- Institución: Instituto Geográfico Nacional / Centro Nacional de Información
  Geográfica.
- Recurso: Límites y Unidades Administrativas Actuales, fecha de catálogo
  28-07-2026.
- Servicio: `https://www.ign.es/wfs-inspire/unidades-administrativas`.
- Catálogo:
  `https://centrodedescargas.cnig.es/CentroDescargas/detalleArchivo?sec=9000029`.
- Licencia: licencia de uso del IGN compatible con CC BY 4.0.
- Atribución: `Obra derivada de BDLJE CC-BY 4.0 ign.es`.

### NGBE

- Institución: Instituto Geográfico Nacional / CNIG.
- Recurso: Nomenclátor Geográfico Básico de España, edición 2026.
- Servicio: `https://www.ign.es/wfs-inspire/ngbe`.
- Catálogo:
  `https://centrodedescargas.cnig.es/CentroDescargas/detalleArchivo?sec=9000001`.
- Licencia: licencia de uso del IGN compatible con CC BY 4.0.
- Atribución: `Obra derivada de NGBE CC-BY 4.0 ign.es`.

### IGR_HIDROGRAFIA

- Institución: Sistema Cartográfico Nacional / IGN.
- Recurso: IGR_HIDROGRAFIA v1 2023, consultado mediante el WFS oficial.
- Servicio: `https://servicios.idee.es/wfs-inspire/hidrografia`.
- Catálogo de licencia y producto:
  `https://centrodedescargas.cnig.es/CentroDescargas/detalleArchivo?sec=12633136`.
- Licencia: CC BY 4.0.
- Atribución:
  `Obra derivada de IGR_HIDROGRAFIA v1 2023 CC-BY 4.0 scne.es`.

La licencia común de uso se conserva en
`https://www.ign.es/resources/licencia/Condiciones_licenciaUso_IGN.pdf`.

### Selección funcional previa al dibujo

| Elemento | Mapa | Función | Fuente geográfica | Riesgo de anacronismo y control |
|---|---|---|---|---|
| España actual | regional | ofrecer referencia nacional | BDLJE | bajo; se presenta como marco contemporáneo |
| provincia actual de León | regional | pasar de España al ámbito provincial | BDLJE | medio; leyenda y pie dicen `actual` |
| municipio actual de Santa María de Ordás | regional/local | localizar el área de Ordás | BDLJE | alto si se proyectara a 1752; patrón, leyenda y aviso lo impiden |
| municipio actual de Rioseco de Tapia | local | situar Rioseco y Tapia respecto del ámbito principal | BDLJE | alto si se leyera como término histórico; se rotula como límite municipal actual |
| seis puntos de lugar actuales | local | mostrar relaciones espaciales esenciales | NGBE | bajo; se registran nombre fuente, tipo y coordenadas |
| río Luna actual | local | referencia física y orientación del corredor | IGR_HIDROGRAFIA | medio; se identifica expresamente como curso actual |
| `Sorribos` | local, solo texto | enlazar el núcleo actual con la forma de 1752 ya sustentada por el proyecto | fuentes canónicas en solo lectura | controlado: no tiene geometría y figura entre paréntesis bajo `Sorrios` |
| norte y escala gráfica | ambos | lectura espacial independiente | cálculo del generador en EPSG:4326 | sin proyección histórica |

Villapodambre, Rioseco de Tapia y Tapia de la Ribera se incluyen porque la
Auditoría B y el índice canónico de topónimos los identifican como relaciones
espaciales necesarias para comprender los linderos descritos por el expediente.
No se añaden otros núcleos por mera proximidad.

## 5. Mapa regional

- **Finalidad:** permitir que una persona sin conocimiento previo pase de
  España a León y de León al área de Ordás y al ámbito local del volumen.
- **Composición:** dos paneles complementarios, no un acercamiento redundante.
  El primero destaca León dentro de España; el segundo destaca el municipio
  actual de Santa María de Ordás dentro de la provincia y marca el entorno de
  Sorrios y Santibáñez.
- **Datos:** contornos de BDLJE y punto contemporáneo del NGBE.
- **Decisiones:** se eliminan del contorno nacional polígonos inferiores a
  0,001 grados cuadrados, invisibles a escala regional; no se alteran las
  unidades destacadas. Tramas y contornos sostienen la lectura en escala de
  grises.
- **Título editorial:** `Situación regional`.
- **Pie propuesto:** `Situación contemporánea del ámbito del volumen: provincia
  de León y área de Ordás. Los límites representados son actuales.`
- **Texto alternativo:** `Mapa contemporáneo en dos escalas: España con la
  provincia de León destacada, y la provincia de León con el municipio actual
  de Santa María de Ordás y el ámbito de Sorrios y Santibáñez señalado. No
  representa límites históricos de 1752.`
- **Atribución visible:** BDLJE y NGBE, mediante las dos fórmulas oficiales de
  obra derivada.
- **Licencia:** fuentes compatibles con CC BY 4.0; activo redistribuible con la
  atribución incorporada.
- **Asset:** `publication/assets/cartography/mapa-regional.svg`, 1.200 × 800 px
  lógicos, SVG vectorial.

## 6. Mapa local

- **Finalidad:** explicar la posición relativa de los asentamientos que el
  volumen necesita para orientarse en el entorno inmediato.
- **Lugares:** Sorrios, Santibáñez de Ordás, Santa María de Ordás,
  Villapodambre, Rioseco de Tapia y Tapia de la Ribera.
- **Datos:** puntos del NGBE, límites municipales actuales BDLJE y segmentos del
  río Luna de IGR_HIDROGRAFIA.
- **Decisiones:** Sorrios usa un símbolo anular propio; los otros lugares usan
  círculos. Los dos municipios se distinguen por trama, contorno y estilo de
  línea, no solo por color. No se incorporan carreteras ni relieve: no añaden
  orientación suficiente a esta escala y restarían claridad.
- **Título editorial:** `Entorno local`.
- **Pie propuesto:** `Entorno contemporáneo de Sorrios —Sorribos en el
  expediente de 1752— y Santibáñez de Ordás. El río y los límites municipales
  representados son actuales.`
- **Texto alternativo:** `Mapa contemporáneo del entorno de Ordás con Sorrios,
  identificado como Sorribos en el expediente de 1752, Santibáñez de Ordás,
  Santa María de Ordás, Villapodambre, Rioseco de Tapia y Tapia de la Ribera.
  Incluye el río Luna y límites municipales actuales; no representa límites
  históricos.`
- **Atribución visible:** BDLJE, NGBE e IGR_HIDROGRAFIA, con las fórmulas de
  obra derivada requeridas.
- **Licencia:** las tres capas permiten redistribución bajo CC BY 4.0 con
  atribución.
- **Asset:** `publication/assets/cartography/mapa-local.svg`, 1.200 × 940 px
  lógicos, SVG vectorial.

## 7. Coordenadas/topónimos verificados

Las coordenadas son contemporáneas, se expresan como latitud/longitud en
EPSG:4326 y no pretenden localizar entidades históricas de 1752.

| Nombre mostrado | Denominación NGBE | Tipo NGBE seleccionado | Latitud | Longitud | Municipio actual comprobado | Fuente | Consulta |
|---|---|---|---:|---:|---|---|---|
| Sorrios | Sorrios de Ordás | Entidad menor de población | 42.735473758 | -5.804687737 | Santa María de Ordás | NGBE/BTN25; denominación `Sorrios` contrastada con el Ayuntamiento | 11-10-2026 |
| Santibáñez de Ordás | Santibáñez de Ordás | Capital de EATIM | 42.727747510 | -5.812751392 | Santa María de Ordás | NGBE/NGMEP | 11-10-2026 |
| Santa María de Ordás | Santa María de Ordás | Capital de municipio | 42.726235550 | -5.823981043 | Santa María de Ordás | NGBE/NGMEP | 11-10-2026 |
| Rioseco de Tapia | Rioseco de Tapia | Capital de municipio | 42.729572000 | -5.792285806 | Rioseco de Tapia | NGBE/NGMEP | 11-10-2026 |
| Villapodambre | Villapodambre | Capital de EATIM | 42.754841800 | -5.835745129 | Santa María de Ordás | NGBE/NGMEP | 11-10-2026 |
| Tapia de la Ribera | Tapia de la Ribera | Capital de EATIM | 42.747027330 | -5.780599131 | Rioseco de Tapia | NGBE/NGMEP | 11-10-2026 |

La validación geométrica comprueba que los seis puntos caen dentro de la
provincia actual de León y del municipio actual declarado. También comprueba
orientaciones relativas respecto de Sorrios. Distancias geodésicas de control:
Santibáñez 1,083 km; Rioseco 1,207 km; Santa María 1,881 km; Tapia 2,350 km;
Villapodambre 3,327 km.

El NGBE registra el punto como `Sorrios de Ordás` y lo clasifica como entidad
menor de población procedente de BTN25. El Ayuntamiento de Santa María de Ordás
identifica `Sorrios` como barrio de Santibáñez. El rótulo del mapa adopta la
forma contemporánea breve del Ayuntamiento y conserva la denominación NGBE en
los metadatos; no se corrige ni modifica ninguna fuente canónica.

## 8. Reproducibilidad

### Archivos

- script: `publication/scripts/build_cartography.py`;
- snapshot: `publication/assets/cartography/cartography.json`;
- salidas fuente: `mapa-regional.svg` y `mapa-local.svg`;
- instrucciones y procedencia resumida:
  `publication/assets/cartography/README.md`.

### Comandos

```bash
.venv/bin/python publication/scripts/build_cartography.py
.venv/bin/python publication/scripts/build_cartography.py --check
.venv/bin/python publication/scripts/build_cartography.py --refresh
```

La reconstrucción ordinaria es offline, usa solo la biblioteca estándar de
Python y no modifica `project/`. La actualización de red consulta los WFS
oficiales, selecciona identificadores/nombres explícitos, redondea coordenadas a
seis decimales en geometrías, aplica Ramer–Douglas–Peucker con tolerancias
declaradas, filtra polígonos nacionales invisibles a escala y ordena las
entidades antes de serializar.

Software de validación: Python 3.12.10 y Google Chrome 142.0.7444.134 para las
capturas temporales. Los PNG de inspección se generaron en `/tmp` y no forman
parte del paquete.

## 9. Derechos

| Asset | Fuentes | Licencia de fuente | Condición del mapa derivado | Atribución que debe conservarse | Compatibilidad con el volumen |
|---|---|---|---|---|---|
| `mapa-regional.svg` | BDLJE + NGBE | CC BY 4.0 compatible conforme a licencia IGN | puede copiarse, adaptarse y redistribuirse con reconocimiento | `Obra derivada de BDLJE CC-BY 4.0 ign.es` + `Obra derivada de NGBE CC-BY 4.0 ign.es` | sí; puede incorporarse a un volumen CC BY 4.0 manteniendo ambos créditos |
| `mapa-local.svg` | BDLJE + NGBE + IGR_HIDROGRAFIA | CC BY 4.0 | puede copiarse, adaptarse y redistribuirse con reconocimiento | los dos créditos anteriores + `Obra derivada de IGR_HIDROGRAFIA v1 2023 CC-BY 4.0 scne.es` | sí; puede incorporarse a un volumen CC BY 4.0 manteniendo los tres créditos |

No hay excepción incompatible con la licencia prevista del libro. La nota de
derechos del volumen deberá dejar claro que los datos externos mantienen su
procedencia y atribución; la CC BY 4.0 del contenido original no los convierte
en datos creados por el autor del libro.

## 10. Accesibilidad

- Cada SVG tiene `role="img"`, `<title>`, `<desc>` y `aria-labelledby`.
- El título editorial y el aviso de no reconstrucción se leen dentro del asset.
- Los polígonos se distinguen por trama, tono, contorno y estilo de línea; los
  lugares, por forma y jerarquía del símbolo. La información no depende solo del
  color.
- Escala, norte, leyenda y créditos conservan tamaños legibles al ancho de una
  página de libro y en pantalla.
- Los textos alternativos de los apartados 5 y 6 son los propuestos para
  PKG-07; las descripciones SVG ofrecen una alternativa larga compacta.
- Una tabla de seis lugares y coordenadas preserva la información esencial
  fuera del gráfico.

## 11. Limitaciones

- No se representan límites ni organización territorial de 1752.
- No se reconstruye el término histórico exacto.
- No se dibujan jurisdicciones, señoríos, parroquias, propiedades o parcelas
  históricas.
- No se infieren caminos históricos ni se proyecta la red viaria actual hacia
  el pasado.
- El curso del río, los puntos y los límites son contemporáneos y sirven solo
  para orientación.
- La simplificación responde a la escala editorial; el snapshot no sustituye a
  los datasets oficiales para medición, gestión administrativa o deslinde.
- `Sorrios (Sorribos en el expediente de 1752)` es una relación editorial ya
  sustentada por el proyecto, no una demostración cartográfica.
- Los mapas no se han integrado en Quarto ni se ha renderizado el libro.
- `INC-BIB-001` e `INC-BIB-002` permanecen abiertas e intactas.

## 12. Resultado

**APTO.** Los dos mapas cumplen la función aprobada, usan únicamente datos
oficiales redistribuibles, conservan las atribuciones obligatorias, pasan las
validaciones geográfica, jurídica, estructural y visual, y no transmiten una
reconstrucción histórica. Quedan preparados para revisión humana antes de una
eventual integración en PKG-07.

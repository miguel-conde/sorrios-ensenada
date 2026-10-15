# Cierre de PKG-08 — fuentes, citas, trazabilidad y aparatos

**Estado:** `COMPLETADO E INTEGRADO`<br>
**Commit integrado:** `c38bb87073362a8a100e7e91106b08f2a1592acb`<br>
**Rama objetivo:** `feature/quarto-book`

PKG-08 resincroniza `publication/` con el estado canónico representado por
`a162fad1792aa9b3804a5499d348ab355e5ce574`, sin modificar `project/`. La
publicación contiene 24 fuentes activas y 24 registros BibTeX, aplica CIT-B/C y
ofrece navegación D/C/I/E/L mediante 111 anchors únicos y retornos válidos.
`TOP-006` permanece solo en la matriz, el aparato QA1 cubre 9/9 cuestiones y
los modelos de cita cubren 11/11 objetos.

La revisión independiente declaró `PKG-08: APTO PARA INTEGRACIÓN`. Los tests
focales registraron 20 PASS y la suite completa, 650 PASS, con cero fallos y
cero errores. Pasaron los validadores canónico, de fuentes, publicación y
cartografía, la compilación estática, `quarto check` y `git diff --check`.

Se aceptó la evidencia de los renders completos ya ejecutados sobre el mismo
commit, sin repetirlos: HTML con 34 documentos y PDF de 345 páginas,
70.861.784 bytes y SHA-256
`734818090b7671b3fb395e02e29144178d4b1e5df9c6a91e77bc2421ba2fbd22`.

La integración fue un avance rápido desde
`8a532bc4f7f576d8855c66d946247122ebd3fa38`. `publication/generated/`,
`_book/` y los PDF continúan sin versionarse; los mapas de PKG-03 no se han
insertado; PKG-06, PKG-07 y PKG-09 no se han iniciado. `GATE-02` sigue
pendiente hasta integrar PKG-06–PKG-09.

Los próximos paquetes conservan su alcance: PKG-06 para preliminares y
arquitectura, PKG-07 para el aparato visual y mapas, y PKG-09 para identidad y
metadatos finales. Antes de iniciar cualquiera de ellos se racionalizará y
formalizará el protocolo permanente de ejecución.

# Desarrollo y pruebas

El uso normal del proyecto no requiere checkout local, Python, WSL, Poppler, Git local, VS Code, Codex CLI ni Work. Chat normal opera sobre GitHub y usa Google Drive solo para leer el PDF autoritativo.

Este documento cubre únicamente desarrollo y CI.

## Dependencias

La fuente de verdad para las ayudas Python de desarrollo es:

`plugins/sorrios-ensenada/pyproject.toml`

El extra `test` instala lo necesario para la suite. El extra `render` añade Pillow para `tools/render_unit.py`.

## Ejecutar la suite

Desde la raíz del repositorio:

### Windows

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".\plugins\sorrios-ensenada[test]"
.\.venv\Scripts\python.exe -m pytest
```

### Linux o WSL

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e './plugins/sorrios-ensenada[test]'
.venv/bin/python -m pytest
```

No reutilices entre Windows y Linux/WSL el mismo entorno virtual.

## Tools conservados

- `plugins/sorrios-ensenada/tools/validate_project.py`: valida el workspace GitHub v2 sin exigir una copia local del PDF.
- `plugins/sorrios-ensenada/tools/path_utils.py`: normaliza rutas lógicas y físicas para tests y tools.
- `plugins/sorrios-ensenada/tools/render_unit.py`: ayuda opcional para desarrollo y referencia de recorte `left`/`right`/`complete`.

Ejemplo de validación lógica:

```bash
python plugins/sorrios-ensenada/tools/validate_project.py .
```

## Render local opcional

`render_unit.py` no forma parte del contrato de uso de ChatGPT. Para usarlo localmente se necesita Pillow y un `pdftoppm` disponible en `PATH`:

```bash
python -m pip install -e './plugins/sorrios-ensenada[render]'
```

La CI general no instala ni exige Poppler. Las pruebas de recorte simulan `pdftoppm`; una integración real con Poppler puede ejecutarse aparte cuando interese.

## Drive

No existe ya un runtime local para materializar Drive. Los antiguos materializadores Base64 y de texto han sido retirados. En el flujo normal, ChatGPT obtiene el PDF directamente mediante la conexión de Google Drive, como archivo real y sin Base64.

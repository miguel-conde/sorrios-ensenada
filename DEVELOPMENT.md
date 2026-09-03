# Desarrollo y pruebas

Las dependencias Python tienen una única fuente de verdad:
`plugins/sorrios-ensenada/pyproject.toml`. El extra `test` es exclusivamente para
desarrollar y validar el repositorio; los tests no forman parte del artefacto del
plugin.

## Windows

Desde la raíz del repositorio, crea un entorno con el lanzador `py` si está
disponible:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".\plugins\sorrios-ensenada[test]"
.\.venv\Scripts\python.exe -m pytest
```

Si `py` no está disponible, ejecuta `-m venv .venv` con el `python.exe`
seleccionado en la instalación de Python o en el IDE. Después usa siempre el
intérprete del entorno virtual.

Poppler debe estar instalado y `pdftoppm.exe` debe estar disponible mediante
`PATH`. Compruébalo antes de la integración real:

```powershell
where.exe pdftoppm
```

## WSL/Linux

Desde la raíz del repositorio y dentro del filesystem de la distribución:

```bash
sudo apt-get update
sudo apt-get install python3-venv poppler-utils
python3 -m venv .venv
.venv/bin/python -m pip install -e './plugins/sorrios-ensenada[test]'
.venv/bin/python -m pytest
command -v pdftoppm
```

No reutilices en WSL el entorno virtual creado en Windows. La suite permite
omitir la integración real de Poppler cuando el ejecutable no existe en un
entorno local; CI establece `REQUIRE_PDFTOPPM=1`, por lo que allí su ausencia es
un error.

#!/usr/bin/env python3
import argparse, hashlib, sys
from pathlib import Path
import yaml

REQUIRED = {
 "00_CONTROL/proyecto.yaml","00_CONTROL/estado.yaml","00_CONTROL/unidades.yaml",
 "00_CONTROL/Manual_Editorial.md","00_CONTROL/INSTRUCCIONES_PROYECTO.md",
 "00_CONTROL/CAMBIOS.md","10_FUENTE_PRIMARIA/sorrios_ensenada_orden_lectura_calidad_original.pdf",
 "20_TRABAJO_EDITORIAL/Edicion_Critica.md","20_TRABAJO_EDITORIAL/Diario_Editorial.md",
 "20_TRABAJO_EDITORIAL/Glosario.md",
 "20_TRABAJO_EDITORIAL/INDICES/Indice_Personas.md",
 "20_TRABAJO_EDITORIAL/INDICES/Indice_Toponimos.md",
 "20_TRABAJO_EDITORIAL/INDICES/Indice_Instituciones.md",
 "20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md",
 "20_TRABAJO_EDITORIAL/INDICES/Indice_Oficios.md",
 "30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md",
}
SECTIONS=["### Imagen","### Transcripción paleográfica","### Observaciones editoriales",
          "### Notas paleográficas","### Notas históricas","### Referencias cruzadas"]

def read_yaml(path): return yaml.safe_load(path.read_text(encoding="utf-8"))

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("root",type=Path); ap.add_argument("--skip-pdf-hash",action="store_true")
 args=ap.parse_args(); root=args.root.resolve()
 errors=[f"Falta {x}" for x in sorted(REQUIRED) if not (root/x).is_file()]
 if errors: print("\n".join(errors)); return 1
 project=read_yaml(root/"00_CONTROL/proyecto.yaml"); state=read_yaml(root/"00_CONTROL/estado.yaml"); data=read_yaml(root/"00_CONTROL/unidades.yaml")
 rows=data.get("units",[])
 if data.get("unit_count")!=35 or len(rows)!=35: errors.append("unidades.yaml no contiene 35 unidades")
 if [u.get("order") for u in rows]!=list(range(1,36)): errors.append("Orden de unidades inválido")
 ids=[u.get("id") for u in rows]
 if len(ids)!=len(set(ids)): errors.append("Hay unidades duplicadas")
 current=state.get("current_unit")
 if current not in ids: errors.append("La unidad actual no existe")
 else:
  unit=rows[ids.index(current)]; loc=state.get("current_location",{})
  if loc.get("pdf_page")!=unit.get("pdf_page") or loc.get("position")!=unit.get("position"): errors.append("La ubicación actual no coincide con unidades.yaml")
 if state.get("last_closed_unit")!=state.get("last_validated_unit"): errors.append("La última unidad validada y cerrada no coincide")
 if state.get("operation",{}).get("status") not in {"clean","verified"}: errors.append("Existe una operación incompleta")
 pdf=root/"10_FUENTE_PRIMARIA/sorrios_ensenada_orden_lectura_calidad_original.pdf"; source=project.get("authorities",{}).get("manuscript",{})
 if pdf.stat().st_size!=source.get("size_bytes"): errors.append("Tamaño del PDF incorrecto")
 if not args.skip_pdf_hash and hashlib.sha256(pdf.read_bytes()).hexdigest()!=source.get("sha256"): errors.append("Hash del PDF incorrecto")
 edition=(root/"20_TRABAJO_EDITORIAL/Edicion_Critica.md").read_text(encoding="utf-8")
 for section in SECTIONS:
  if edition.count(section)!=35: errors.append(f"Sección {section}: se esperaban 35")
 if errors: print("\n".join(errors)); return 1
 print("VALID: workspace coherent"); return 0

if __name__=="__main__": sys.exit(main())

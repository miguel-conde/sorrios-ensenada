#!/usr/bin/env python3
import argparse, subprocess, tempfile
from pathlib import Path
import yaml
from PIL import Image

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("pdf",type=Path); ap.add_argument("units",type=Path); ap.add_argument("unit_id"); ap.add_argument("output",type=Path); ap.add_argument("--dpi",type=int,default=220)
 args=ap.parse_args(); data=yaml.safe_load(args.units.read_text(encoding="utf-8")); unit=next((u for u in data["units"] if u["id"]==args.unit_id),None)
 if not unit: raise SystemExit(f"Unidad desconocida: {args.unit_id}")
 with tempfile.TemporaryDirectory() as td:
  prefix=Path(td)/"page"
  subprocess.run(["pdftoppm","-f",str(unit["pdf_page"]),"-singlefile","-r",str(args.dpi),"-png",str(args.pdf),str(prefix)],check=True)
  image=Image.open(str(prefix)+".png")
  if unit["position"]=="left": image=image.crop((0,0,image.width//2,image.height))
  elif unit["position"]=="right": image=image.crop((image.width//2,0,image.width,image.height))
  elif unit["position"]!="complete": raise SystemExit("Posición inválida")
  args.output.parent.mkdir(parents=True,exist_ok=True); image.save(args.output)
 print(args.output.resolve())

if __name__=="__main__": main()

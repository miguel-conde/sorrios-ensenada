#!/usr/bin/env python3
import argparse, hashlib, json, sys
from pathlib import Path
import yaml

def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def tree(root): return {str(p.relative_to(root)):digest(p) for p in root.rglob("*") if p.is_file()}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("before",type=Path); ap.add_argument("after",type=Path); ap.add_argument("operation",type=Path); args=ap.parse_args()
 op=yaml.safe_load(args.operation.read_text(encoding="utf-8")); allowed=set(op.get("allowed_changes",[])); b,a=tree(args.before),tree(args.after)
 changed={p for p in b.keys()|a.keys() if b.get(p)!=a.get(p)}; errors=[]
 unexpected=sorted(changed-allowed)
 if unexpected: errors.append("Cambios no previstos: "+", ".join(unexpected))
 state=yaml.safe_load((args.after/"00_CONTROL/estado.yaml").read_text(encoding="utf-8"))
 if state.get("operation",{}).get("status") not in {"clean","verified"}: errors.append("El estado final conserva una operación abierta")
 if errors: print("\n".join(errors)); return 1
 print(json.dumps({"changed":sorted(changed),"status":"VALID"},ensure_ascii=False)); return 0
if __name__=="__main__": sys.exit(main())

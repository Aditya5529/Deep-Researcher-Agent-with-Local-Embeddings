# src/ingest.py
from pdfminer.high_level import extract_text
from pathlib import Path
import json

def extract_pdf_text(path: str) -> str:
    return extract_text(path)

def ingest_folder(folder="data", out_folder="raw_text"):
    folder = Path(folder)
    out_folder = Path(out_folder)
    out_folder.mkdir(exist_ok=True)  # ✅ auto-create raw_text if missing

    for p in folder.glob("**/*.pdf"):   # ✅ only PDFs
        text = extract_pdf_text(str(p))
        meta = {"source": str(p), "type": "pdf"}
        out = {"meta": meta, "text": text}

        out_file = out_folder / f"{p.stem}.json"
        with open(out_file, "w", encoding="utf8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)

        print(f"✅ Saved {out_file}")

if __name__ == "__main__":
    ingest_folder()

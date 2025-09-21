# src/chunker.py
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pathlib import Path
import json

splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=200)

def chunk_file(raw_json_path, out_dir="chunks"):
    out_dir = Path(out_dir)
    out_dir.mkdir(exist_ok=True)  # ✅ create chunks/ if missing

    with open(raw_json_path, 'r', encoding='utf8') as f:
        doc = json.load(f)

    chunks = splitter.split_text(doc['text'])
    out = []
    for i, c in enumerate(chunks):
        out.append({"text": c, "meta": {**doc['meta'], "chunk": i}})

    # Save chunks to file
    out_file = out_dir / (Path(raw_json_path).stem + ".json")
    with open(out_file, "w", encoding="utf8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved {out_file} with {len(out)} chunks.")

if __name__ == "__main__":
    for path in Path("raw_text").glob("*.json"):
        chunk_file(path)

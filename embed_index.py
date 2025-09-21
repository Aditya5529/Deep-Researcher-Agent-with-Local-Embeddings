# src/embed_index.py
import json
from pathlib import Path
from langchain_community.vectorstores import Chroma
from langchain.docstore.document import Document
from langchain_community.embeddings import SentenceTransformerEmbeddings

def build_chroma_index(chunks_folder="chunks", persist_dir="indices/chroma"):
    # Load chunks
    docs = []
    for path in Path(chunks_folder).glob("*.json"):
        with open(path, "r", encoding="utf8") as f:
            chunk_data = json.load(f)  # list of dicts: {"text":..., "meta":...}
            for c in chunk_data:
                docs.append(
                    Document(page_content=c["text"], metadata=c["meta"])
                )

    # Embedding model
    embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # Create Chroma index
    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embedding,
        persist_directory=persist_dir
    )
    vectordb.persist()
    return vectordb

if __name__ == "__main__":
    db = build_chroma_index()
    print("✅ Chroma index built and persisted.")

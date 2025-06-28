"""
embed.py - Embedding generation and FAISS vector store
"""
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json


def generate_embeddings(chunks, model_name="all-MiniLM-L6-v2"):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(chunks, show_progress_bar=True)
    return np.array(embeddings, dtype="float32")

def build_faiss_index(embeddings, out_path="faiss.index"):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    faiss.write_index(index, out_path)
    print(f"FAISS index saved to {out_path}")
    return index

def save_embeddings(embeddings, out_path="embeddings.npy"):
    np.save(out_path, embeddings)
    print(f"Embeddings saved to {out_path}")

if __name__ == "__main__":
    with open("data_chunks.json", "r", encoding="utf-8") as f:
        chunks = json.load(f)
    embeddings = generate_embeddings(chunks)
    save_embeddings(embeddings)
    build_faiss_index(embeddings) 
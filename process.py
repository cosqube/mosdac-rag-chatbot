"""
process.py - Text cleaning, chunking, and saving
"""
import re
import json
# import nltk
# import spacy


def clean_text(text):
    """Remove HTML tags, symbols, and unwanted characters."""
    text = re.sub(r"[\r\n\t]+", " ", text)
    text = re.sub(r"[^\w\s.,;:?!-]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def chunk_text(text, chunk_size=300):
    """Break text into chunks of ~300 chars."""
    chunks = []
    i = 0
    while i < len(text):
        chunks.append(text[i:i+chunk_size])
        i += chunk_size
    return chunks

def save_chunks(chunks, out_path):
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(chunks)} chunks to {out_path}")

if __name__ == "__main__":
    with open("data_raw.txt", "r", encoding="utf-8") as f:
        raw = f.read()
    cleaned = clean_text(raw)
    chunks = chunk_text(cleaned)
    save_chunks(chunks, "data_chunks.json") 
import os
import json
from app.schemas.rag import RAGChunk

DATA_DIR = "app/rag/data"
CHUNKS_FILE = os.path.join(DATA_DIR, "chunks.json")


def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)


def load_chunks() -> list[dict]:
    ensure_data_dir()

    if not os.path.exists(CHUNKS_FILE):
        return []

    with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_chunks(chunks: list[RAGChunk]):
    ensure_data_dir()

    existing = load_chunks()
    existing.extend([chunk.model_dump() for chunk in chunks])

    with open(CHUNKS_FILE, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
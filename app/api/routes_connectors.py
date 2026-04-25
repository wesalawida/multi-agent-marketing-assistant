from fastapi import APIRouter
from app.schemas.connectors import InstagramInspirationRequest, PinterestInspirationRequest
from app.connectors.instagram_adapter import build_instagram_document
from app.connectors.pinterest_adapter import build_pinterest_document
from app.rag.chunker import chunk_text
from app.rag.loader import save_chunks

router = APIRouter()


@router.post("/ingest-instagram-inspiration")
def ingest_instagram_inspiration(data: InstagramInspirationRequest):
    document = build_instagram_document(data)
    chunks = chunk_text(document)
    save_chunks(chunks)

    return {
        "status": "saved",
        "platform": "Instagram",
        "title": document.title,
        "chunks_created": len(chunks),
    }


@router.post("/ingest-pinterest-inspiration")
def ingest_pinterest_inspiration(data: PinterestInspirationRequest):
    document = build_pinterest_document(data)
    chunks = chunk_text(document)
    save_chunks(chunks)

    return {
        "status": "saved",
        "platform": "Pinterest",
        "title": document.title,
        "chunks_created": len(chunks),
    }
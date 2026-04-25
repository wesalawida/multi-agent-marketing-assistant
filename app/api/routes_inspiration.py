from fastapi import APIRouter
from app.schemas.inspiration import ManualInspirationRequest
from app.schemas.rag import RAGDocument
from app.rag.chunker import chunk_text
from app.rag.loader import save_chunks

router = APIRouter()


@router.post("/ingest-manual-inspiration")
def ingest_manual_inspiration(data: ManualInspirationRequest):
    document = RAGDocument(
        source="manual_inspiration",
        source_type="inspiration",
        title=data.title,
        text=data.content,
        platform=data.platform,
        account_name=data.account_name,
        content_type=data.content_type,
        tags=data.tags,
    )

    chunks = chunk_text(document)
    save_chunks(chunks)

    return {
        "status": "saved",
        "chunks_created": len(chunks),
        "title": data.title,
        "source_type": "inspiration"
    }
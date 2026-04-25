from fastapi import APIRouter
from app.schemas.rag import (
    UploadDocRequest,
    SearchDocsRequest,
    SearchDocsResponse,
    SearchResultItem,
    RAGDocument,
)
from app.rag.chunker import chunk_text
from app.rag.loader import save_chunks
from app.rag.retriever import search_chunks

router = APIRouter()


@router.post("/upload-doc")
def upload_doc(data: UploadDocRequest):
    document = RAGDocument(
        source=data.source,
        source_type=data.source_type,
        title=data.filename,
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
        "title": data.filename
    }


@router.post("/search-docs", response_model=SearchDocsResponse)
def search_docs(data: SearchDocsRequest):
    results = search_chunks(
        query=data.query,
        top_k=data.top_k,
        source_type=data.source_type,
        platform=data.platform,
    )

    return SearchDocsResponse(
        results=[
            SearchResultItem(
                chunk_id=item["chunk_id"],
                title=item["title"],
                text=item["text"],
                source=item["source"],
                source_type=item["source_type"],
                platform=item.get("platform"),
                account_name=item.get("account_name"),
                content_type=item.get("content_type"),
            )
            for item in results
        ]
    )
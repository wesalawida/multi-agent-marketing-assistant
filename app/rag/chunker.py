from app.schemas.rag import RAGDocument, RAGChunk


def chunk_text(document: RAGDocument, chunk_size: int = 300, overlap: int = 50) -> list[RAGChunk]:
    text = document.text.strip()
    chunks = []

    start = 0
    chunk_index = 0

    while start < len(text):
        end = start + chunk_size
        chunk_text_value = text[start:end]

        chunks.append(
            RAGChunk(
                chunk_id=f"{document.title}_{chunk_index}",
                source=document.source,
                source_type=document.source_type,
                title=document.title,
                text=chunk_text_value,
                platform=document.platform,
                account_name=document.account_name,
                content_type=document.content_type,
                tags=document.tags,
            )
        )

        start += chunk_size - overlap
        chunk_index += 1

    return chunks
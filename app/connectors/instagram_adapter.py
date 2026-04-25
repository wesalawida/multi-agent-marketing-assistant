from app.schemas.rag import RAGDocument
from app.schemas.connectors import InstagramInspirationRequest


def build_instagram_document(data: InstagramInspirationRequest) -> RAGDocument:
    parts = []

    if data.bio:
        parts.append(f"BIO:\n{data.bio}")

    if data.captions:
        parts.append("CAPTIONS:\n" + "\n\n".join(data.captions))

    if data.vibe_notes:
        parts.append(f"VIBE NOTES:\n{data.vibe_notes}")

    combined_text = "\n\n".join(parts)

    return RAGDocument(
        source="instagram_adapter",
        source_type="inspiration",
        title=f"instagram_{data.username}",
        text=combined_text,
        platform="Instagram",
        account_name=data.username,
        content_type="instagram_profile_inspiration",
        tags=["instagram", "inspiration", "social_style"],
    )
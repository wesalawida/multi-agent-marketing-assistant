from app.schemas.rag import RAGDocument
from app.schemas.connectors import PinterestInspirationRequest


def build_pinterest_document(data: PinterestInspirationRequest) -> RAGDocument:
    parts = []

    if data.pin_descriptions:
        parts.append("PIN DESCRIPTIONS:\n" + "\n\n".join(data.pin_descriptions))

    if data.vibe_notes:
        parts.append(f"VIBE NOTES:\n{data.vibe_notes}")

    combined_text = "\n\n".join(parts)

    return RAGDocument(
        source="pinterest_adapter",
        source_type="inspiration",
        title=f"pinterest_{data.board_name}",
        text=combined_text,
        platform="Pinterest",
        account_name=data.board_name,
        content_type="pinterest_board_inspiration",
        tags=["pinterest", "inspiration", "visual_style"],
    )
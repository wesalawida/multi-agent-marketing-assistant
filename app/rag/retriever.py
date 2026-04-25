from app.rag.loader import load_chunks


def search_chunks(query: str, top_k: int = 3, source_type: str | None = None, platform: str | None = None):
    chunks = load_chunks()
    scored_results = []

    for chunk in chunks:
        text = chunk["text"]

        if source_type and chunk.get("source_type") != source_type:
            continue

        if platform and chunk.get("platform") != platform:
            continue

        score = text.lower().count(query.lower())

        if score > 0:
            scored_results.append((score, chunk))

    scored_results.sort(key=lambda x: x[0], reverse=True)

    return [item[1] for item in scored_results[:top_k]]


def get_context_for_business(business_name: str, top_k: int = 3) -> str:
    results = search_chunks(query=business_name, top_k=top_k, source_type="brand_doc")

    if not results:
        chunks = [
            c for c in load_chunks()
            if c.get("source_type") == "brand_doc"
        ][:top_k]
        return "\n\n".join(chunk["text"] for chunk in chunks)

    return "\n\n".join(chunk["text"] for chunk in results)


def get_inspiration_context(query: str, top_k: int = 3, platform: str | None = None) -> str:
    results = search_chunks(
        query=query,
        top_k=top_k,
        source_type="inspiration",
        platform=platform,
    )

    return "\n\n".join(chunk["text"] for chunk in results)


def get_brand_chunks(business_name: str, top_k: int = 3):
    results = search_chunks(query=business_name, top_k=top_k, source_type="brand_doc")

    if not results:
        return [
            c for c in load_chunks()
            if c.get("source_type") == "brand_doc"
        ][:top_k]

    return results


def get_inspiration_chunks(query: str, top_k: int = 3, platform: str | None = None):
    return search_chunks(
        query=query,
        top_k=top_k,
        source_type="inspiration",
        platform=platform,
    )
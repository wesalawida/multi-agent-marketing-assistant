from pydantic import BaseModel
from typing import List, Optional


class RAGDocument(BaseModel):
    source: str
    source_type: str
    title: str
    text: str
    platform: Optional[str] = None
    account_name: Optional[str] = None
    content_type: Optional[str] = None
    tags: List[str] = []


class RAGChunk(BaseModel):
    chunk_id: str
    source: str
    source_type: str
    title: str
    text: str
    platform: Optional[str] = None
    account_name: Optional[str] = None
    content_type: Optional[str] = None
    tags: List[str] = []


class UploadDocRequest(BaseModel):
    filename: str
    content: str
    source: str = "local"
    source_type: str = "brand_doc"
    platform: Optional[str] = None
    account_name: Optional[str] = None
    content_type: Optional[str] = "document"
    tags: List[str] = []


class SearchDocsRequest(BaseModel):
    query: str
    top_k: int = 3
    source_type: Optional[str] = None
    platform: Optional[str] = None


class SearchResultItem(BaseModel):
    chunk_id: str
    title: str
    text: str
    source: str
    source_type: str
    platform: Optional[str] = None
    account_name: Optional[str] = None
    content_type: Optional[str] = None


class SearchDocsResponse(BaseModel):
    results: List[SearchResultItem]
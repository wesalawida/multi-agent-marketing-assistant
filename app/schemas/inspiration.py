from pydantic import BaseModel
from typing import List, Optional


class ManualInspirationRequest(BaseModel):
    title: str
    content: str
    platform: Optional[str] = None
    account_name: Optional[str] = None
    content_type: str = "inspiration_post"
    tags: List[str] = []
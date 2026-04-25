from pydantic import BaseModel
from typing import List, Optional


class InstagramInspirationRequest(BaseModel):
    username: str
    bio: Optional[str] = None
    captions: List[str] = []
    vibe_notes: Optional[str] = None
    platform: str = "Instagram"


class PinterestInspirationRequest(BaseModel):
    board_name: str
    pin_descriptions: List[str] = []
    vibe_notes: Optional[str] = None
    platform: str = "Pinterest"
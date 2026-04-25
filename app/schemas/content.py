from pydantic import BaseModel


class ContentRequest(BaseModel):
    business_name: str
    audience: str
    platform: str


class ContentResponse(BaseModel):
    platform: str
    content: str
    agent: str
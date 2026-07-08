from pydantic import BaseModel


class AskRequest(BaseModel):
    question: str


class Citation(BaseModel):
    file: str
    page: int
    snippet: str


class AskResponse(BaseModel):
    answer: str
    citations: list[Citation]
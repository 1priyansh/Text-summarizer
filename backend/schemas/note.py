from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NoteCreate(BaseModel):
    original_text: str
    tags: Optional[str] = ""

class NoteOut(BaseModel):
    id: int
    original_text: str
    summary_text: str
    tags: str
    created_at: datetime

    class Config:
        orm_mode = True

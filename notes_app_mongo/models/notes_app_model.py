from pydantic import BaseModel
from typing import Optional

class Note(BaseModel):
    id: Optional[int] 
    title: str
    body: str
    created_at: str
    task_done: bool = False


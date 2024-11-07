from pydantic import BaseModel
from datetime import datetime

class NoteCreate(BaseModel):
    title: str
    body: str
    task_done: bool = False

class NoteDisplay(BaseModel):
    id: int
    title: str
    body: str
    created_at: datetime
    task_done: bool = False
    
    model_config = {'from_attributes': True}

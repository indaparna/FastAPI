from pydantic import BaseModel

class NoteCreate(BaseModel):
    title: str
    body: str
    task_done: bool = False

class NoteDisplay(BaseModel):
    id: int
    title: str
    body: str
    created_at: str
    task_done: bool = False

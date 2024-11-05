from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional
from datetime import datetime

app = FastAPI()

# Dictionary to store notes
notes= {}

class Note(BaseModel):
    id: int = None  # auto-incremented
    title: str
    body: str
    created_at: str = None
    task_done: bool = False

# create
@app.post("/create/")
def create_note(note: Note):
    note.id = len(notes) + 1    
    note.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes[note.id] = note.model_dump()
    return {"message": "Note created successfully", "id": note.id - 1}

# read
@app.get("/read/")
def read_notes():
    return notes

# read with note id
@app.get("/read/{note_id}")
def read_note(note_id: int):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    return notes[note_id]

# update
@app.put("/update/{note_id}")
def update_note(note_id: int, updated_note: Note):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    updated_note.id = note_id
    updated_note.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes[note_id] = updated_note.model_dump()
    return {"message": "Note updated successfully"}

# delete
@app.delete("/delete/{note_id}")
def delete_note(note_id: int):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    del notes[note_id]
    return {"message": "Note deleted successfully!"}
    
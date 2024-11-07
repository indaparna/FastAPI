from datetime import datetime
from typing import List
from fastapi import HTTPException
from models.notes_app_model import Note
from schemas.notes_app_schema import NoteCreate, NoteDisplay
from configurations import collection 
from bson import ObjectId


def create_note_logic(note_data: NoteCreate) -> NoteDisplay:
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")   

    last_note = collection.find_one(sort=[("id", -1)])      
    global next_id    
    if last_note:
        next_id = last_note["id"] + 1 
    else:
        next_id = 1  

    note = Note(
        id=next_id,  
        title=note_data.title,
        body=note_data.body,
        created_at=created_at,
        task_done=note_data.task_done
    )   
    collection.insert_one(note.model_dump()) 
    return NoteDisplay(**note.model_dump())


def read_notes_logic() -> List[NoteDisplay]:
    return [NoteDisplay(**note) for note in collection.find()]


def read_note_logic(note_id: int) -> NoteDisplay:
    note_data = collection.find_one({"id": note_id})
    if not note_data:
        raise HTTPException(status_code=404, detail="Note not found")
    return NoteDisplay(**note_data)


def update_note_logic(note_id: int, updated_data: NoteCreate) -> NoteDisplay:
    note_data = collection.find_one({"id": note_id}) 
    
    if not note_data:
        raise HTTPException(status_code=404, detail="Note not found")
    
    updated_note = {
        "title": updated_data.title,
        "body": updated_data.body,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  
        "task_done": updated_data.task_done,
    }

    result = collection.find_one_and_update(
        {"id": note_id},
        {"$set": updated_note},
        return_document=True
    )
    if not result:
        raise HTTPException(status_code=404, detail="Note not found")
    
    result["id"] = result.pop("id")  
    return NoteDisplay(**result)

def delete_note_logic(note_id: str):
    result = collection.delete_one({"id": note_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted successfully!"}
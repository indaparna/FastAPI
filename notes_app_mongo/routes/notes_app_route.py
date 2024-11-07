from typing import List
from fastapi import APIRouter
from schemas.notes_app_schema import NoteCreate, NoteDisplay
import controllers.notes_app_controller as controller

router = APIRouter()

@router.post("/create/", response_model=NoteDisplay)
def create_note(note: NoteCreate):
    return controller.create_note_logic(note)

@router.get("/", response_model=List[NoteDisplay])
def read_notes():
    return controller.read_notes_logic()

@router.get("/read/{note_id}", response_model=NoteDisplay)
def read_note(note_id: int):
    return controller.read_note_logic(note_id)

@router.put("/update/{note_id}", response_model=NoteDisplay)
def update_note(note_id: int, updated_note: NoteCreate):
    return controller.update_note_logic(note_id, updated_note)

@router.delete("/delete/{note_id}")
def delete_note(note_id: int):
    return controller.delete_note_logic(note_id)

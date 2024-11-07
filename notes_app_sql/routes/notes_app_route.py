from typing import List
from fastapi import APIRouter, Depends
from schemas.notes_app_schema import NoteCreate, NoteDisplay
import controllers.notes_app_controller as controller
from sqlalchemy.orm import Session
from configurations import get_db

router = APIRouter()

@router.post("/create/", response_model=NoteDisplay)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    return controller.create_note_logic(note, db)

@router.get("/", response_model=List[NoteDisplay])
def read_notes(db: Session = Depends(get_db)):
    return controller.read_notes_logic(db)

@router.get("/read/{note_id}", response_model=NoteDisplay)
def read_note(note_id: int, db: Session = Depends(get_db)):
    return controller.read_note_logic(note_id, db)

@router.put("/update/{note_id}", response_model=NoteDisplay)
def update_note(note_id: int, updated_note: NoteCreate, db: Session = Depends(get_db)):
    return controller.update_note_logic(note_id, updated_note, db)

@router.delete("/delete/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    return controller.delete_note_logic(note_id, db)

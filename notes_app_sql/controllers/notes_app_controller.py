from datetime import datetime
from typing import List
from fastapi import HTTPException, Depends
from models.notes_app_model import Note
from schemas.notes_app_schema import NoteCreate, NoteDisplay
from configurations import get_db
from sqlalchemy.orm import Session


def create_note_logic(note_data: NoteCreate, db: Session = Depends(get_db)) -> NoteDisplay:
    note = Note(
        title=note_data.title,
        body=note_data.body,
        task_done=note_data.task_done,
        created_at=datetime.now()
    )
    db.add(note)
    db.commit()
    db.refresh(note)
    return NoteDisplay.model_validate(note)

def read_notes_logic(db: Session = Depends(get_db)) -> List[NoteDisplay]:
    notes = db.query(Note).all()
    return [NoteDisplay.model_validate(note) for note in notes]

def read_note_logic(note_id: int, db: Session =Depends(get_db)) -> NoteDisplay:
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return NoteDisplay.model_validate(note)


def update_note_logic(note_id: int, updated_data: NoteCreate, db: Session=Depends(get_db)) -> NoteDisplay:
    note =  db.query(Note).filter(Note.id == note_id).first()    
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    note.title = updated_data.title
    note.body = updated_data.body
    note.task_done = updated_data.task_done
    note.created_at = datetime.now()
    db.commit()
    db.refresh(note)
    # for key, value in updated_data.model_dump(exclude_unset=True).items():
    return NoteDisplay.model_validate(note)

def delete_note_logic(note_id: str, db: Session=Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return {"message": "Note deleted successfully!"}
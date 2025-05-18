from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend.schemas.note import NoteCreate, NoteOut
from backend.models.note import Note
from backend.database import get_db
from backend.utils.openai_client import generate_summary
from fastapi.security import OAuth2PasswordBearer
from backend.models.user import User
from backend.utils.security import decode_access_token

router = APIRouter(prefix="/notes", tags=["notes"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    user = db.query(User).filter(User.email == payload.get("sub")).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user

@router.post("/", response_model=NoteOut)
def create_note(note_create: NoteCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    summary = generate_summary(note_create.original_text)
    new_note = Note(
        user_id=user.id,
        original_text=note_create.original_text,
        summary_text=summary,
        tags=note_create.tags
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

@router.get("/", response_model=List[NoteOut])
def get_notes(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    notes = db.query(Note).filter(Note.user_id == user.id).order_by(Note.created_at.desc()).all()
    return notes

@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    note = db.query(Note).filter(Note.id == note_id, Note.user_id == user.id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()

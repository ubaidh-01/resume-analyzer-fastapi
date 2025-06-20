import os

from app.utils.analyzer import extract_text_from_pdf
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session

from app.crud import resume as crud_resume
from app.database import get_db
from app.models.user import User
from app.schemas.resume import ResumeOut
from app.utils.security import get_current_user

router = APIRouter(prefix="/resumes", tags=["Resumes"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/", response_model=ResumeOut)
def upload_resume(
        file: UploadFile = File(...),
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    contents = extract_text_from_pdf(file)
    path = os.path.join(UPLOAD_DIR, file.filename)
    with open(path, "wb") as f:
        f.write(file.file.read())

    return crud_resume.create_resume(db, current_user, filename=file.filename, content=contents)


@router.get("/", response_model=list[ResumeOut])
def list_user_resumes(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    return crud_resume.get_user_resumes(db, current_user)


@router.delete("/{resume_id}", response_model=ResumeOut)
def delete_resume(
        resume_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    deleted = crud_resume.delete_resume(db, resume_id, current_user)
    if not deleted:
        raise HTTPException(status_code=404, detail="Resume not found.")
    return deleted

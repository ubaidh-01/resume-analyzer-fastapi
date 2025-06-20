from sqlalchemy.orm import Session

from app.models.resume import Resume
from app.models.user import User


def create_resume(db: Session, user: User, filename: str, content: str | None = None):
    resume = Resume(filename=filename, content=content, owner=user)
    db.add(resume)
    db.commit()
    db.refresh(resume)
    return resume


def get_user_resumes(db: Session, user: User):
    return db.query(Resume).filter(Resume.user_id == user.id).all()


def get_resume(db: Session, resume_id: int, user: User):
    return db.query(Resume).filter(Resume.id == resume_id, Resume.user_id == user.id).first()


def delete_resume(db: Session, resume_id: int, user: User):
    resume = get_resume(db, resume_id, user)
    if resume:
        db.delete(resume)
        db.commit()
    return resume

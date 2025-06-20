from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    content = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", backref="resumes")

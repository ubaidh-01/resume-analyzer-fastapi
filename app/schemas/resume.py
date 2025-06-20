from typing import Optional

from pydantic import BaseModel


class ResumeBase(BaseModel):
    filename: str


class ResumeCreate(ResumeBase):
    pass


class ResumeOut(ResumeBase):
    id: int
    content: Optional[str]

    class Config:
        orm_mode = True

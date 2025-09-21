from pydantic import BaseModel
from typing import Optional

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: str

class StudentCreate(StudentBase):
    image: str # base64 encoded image

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True

class StudentRecognized(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str

class RecognizeRequest(BaseModel):
    image: str # base64 encoded image

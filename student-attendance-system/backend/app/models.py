from sqlalchemy import Column, Integer, String, LargeBinary
from .database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    face_encoding = Column(LargeBinary, nullable=True)

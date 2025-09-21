import base64
import io
import face_recognition
import numpy as np
from sqlalchemy.orm import Session
from . import models, schemas

def get_student_by_email(db: Session, email: str):
    return db.query(models.Student).filter(models.Student.email == email).first()

def create_student(db: Session, student: schemas.StudentCreate):
    image_data = base64.b64decode(student.image)
    image = face_recognition.load_image_file(io.BytesIO(image_data))
    face_encodings = face_recognition.face_encodings(image)

    if not face_encodings:
        return None

    db_student = models.Student(
        email=student.email,
        first_name=student.first_name,
        last_name=student.last_name,
        face_encoding=face_encodings[0].tobytes()
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_all_students_with_face_encodings(db: Session):
    return db.query(models.Student).filter(models.Student.face_encoding != None).all()

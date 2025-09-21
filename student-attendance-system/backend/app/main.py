import base64
import io
import face_recognition
import numpy as np
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.get_student_by_email(db, email=student.email)
    if db_student:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    created_student = crud.create_student(db=db, student=student)
    if created_student is None:
        raise HTTPException(status_code=400, detail="No face found in the image")
    return created_student


@app.post("/recognize/", response_model=schemas.StudentRecognized)
def recognize_face(request: schemas.RecognizeRequest, db: Session = Depends(get_db)):
    image_data = base64.b64decode(request.image)
    image = face_recognition.load_image_file(io.BytesIO(image_data))
    unknown_face_encodings = face_recognition.face_encodings(image)

    if not unknown_face_encodings:
        raise HTTPException(status_code=400, detail="No face found in the image")

    known_students = crud.get_all_students_with_face_encodings(db)
    if not known_students:
        raise HTTPException(status_code=404, detail="No students with face encodings found in the database")

    known_face_encodings = [np.frombuffer(student.face_encoding) for student in known_students]

    for unknown_face_encoding in unknown_face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)
        
        if True in matches:
            first_match_index = matches.index(True)
            matched_student = known_students[first_match_index]
            return matched_student

    raise HTTPException(status_code=404, detail="No matching student found")

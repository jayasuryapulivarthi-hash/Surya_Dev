from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from database import SessionLocal
from student_service import get_students, create_student, update_student
from student_api_model import Student_api_model
from student_db_model import Student_db_model

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/students")
def read_students(db: Session = Depends(get_db)):
    return get_students(db)

@app.post("/students")
def add_student(student: Student_api_model, db: Session = Depends(get_db)):
    return create_student(db, student)
    
@app.put("/students/{student_id}")
def modify_student(student_id: str, student: Student_api_model, db: Session = Depends(get_db)):
    updated_student = update_student(db, student_id, student)
    if updated_student is None:
        return {"message": "Student not found"}
    return updated_student
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.student_api_schema import Student_api_schema
from app.services.student_service import get_students, create_student, update_student, get_active_students
from fastapi import HTTPException


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.get("")
def read_students(db: Session = Depends(get_db)):
    return get_students(db)

@router.get("/Active_students")
def read_active_students(db: Session = Depends(get_db)):
    return get_active_students(db)


@router.post("")
def add_student(student: Student_api_schema, db: Session = Depends(get_db)):
    return create_student(db, student)


@router.put("/{student_id}")
def modify_student(student_id: str, student: Student_api_schema, db: Session = Depends(get_db)):
    updated_student = update_student(db, student_id, student)

    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return updated_student
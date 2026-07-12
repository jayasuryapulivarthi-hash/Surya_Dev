from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.course_api_schema import Course_api_schema
from app.services.course_service import get_courses, create_course, update_course


router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


@router.get("")
def read_courses(db: Session = Depends(get_db)):
    return get_courses(db)


@router.post("")
def add_course(course: Course_api_schema, db: Session = Depends(get_db)):
    return create_course(db, course)


@router.put("/{course_id}")
def modify_course(course_id: str, course: Course_api_schema, db: Session = Depends(get_db)):
    updated_course = update_course(db, course_id, course)

    if updated_course is None:
        return {"message": "Course not found"}

    return updated_course
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.course_instructor_api_schema import Course_instructor_api_schema
from app.services.course_instructor_service import (
    get_course_instructors,
    create_course_instructor,
    remove_course_instructor
)


router = APIRouter(
    prefix="/course-instructors",
    tags=["Course Instructors"]
)


@router.get("")
def read_course_instructors(db: Session = Depends(get_db)):
    return get_course_instructors(db)


@router.post("")
def add_course_instructor(
    course_instructor: Course_instructor_api_schema,
    db: Session = Depends(get_db)
):
    return create_course_instructor(db, course_instructor)


@router.delete("/{course_id}/{instructor_id}")
def delete_course_instructor(
    course_id: str,
    instructor_id: str,
    db: Session = Depends(get_db)
):
    deleted_record = remove_course_instructor(db, course_id, instructor_id)

    if deleted_record is None:
        return {"message": "Course instructor record not found"}

    return deleted_record
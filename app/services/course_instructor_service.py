from sqlalchemy.orm import Session

from app.models.course_instructor_db_model import Course_instructor_db_model
from app.schemas.course_instructor_api_schema import Course_instructor_api_schema
from app.repositories.course_instructor_repository import (
    get_all_course_instructors,
    get_course_instructor_by_ids,
    add_course_instructor,
    delete_course_instructor as repository_delete_course_instructor
)


def get_course_instructors(db: Session):
    return get_all_course_instructors(db)


def create_course_instructor(db: Session, course_instructor: Course_instructor_api_schema):
    existing_record = get_course_instructor_by_ids(
        db,
        course_instructor.course_id,
        course_instructor.instructor_id
    )

    if existing_record is not None:
        return {"message": "Course instructor record already exists"}

    course_instructor_db = Course_instructor_db_model(
        course_id=course_instructor.course_id,
        instructor_id=course_instructor.instructor_id
    )

    return add_course_instructor(db, course_instructor_db)


def remove_course_instructor(db: Session, course_id: str, instructor_id: str):
    course_instructor_db = get_course_instructor_by_ids(
        db,
        course_id,
        instructor_id
    )

    if course_instructor_db is None:
        return None

    return repository_delete_course_instructor(db, course_instructor_db)
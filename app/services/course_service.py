from sqlalchemy.orm import Session

from app.models.course_db_model import Course_db_model
from app.schemas.course_api_schema import Course_api_schema
from app.repositories.course_repository import (
    get_all_courses,
    get_course_by_id,
    add_course,
    update_course as repository_update_course
)


def get_courses(db: Session):
    return get_all_courses(db)


def create_course(db: Session, course: Course_api_schema):
    course_db = Course_db_model(
        course_id=course.course_id,
        course_name=course.course_name,
        credits=course.credits
    )

    return add_course(db, course_db)


def update_course(db: Session, course_id: str, course: Course_api_schema):
    course_db = get_course_by_id(db, course_id)

    if course_db is None:
        return None

    course_db.course_name = course.course_name
    course_db.credits = course.credits

    return repository_update_course(db, course_db)
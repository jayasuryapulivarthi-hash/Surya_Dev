from sqlalchemy.orm import Session

from app.models.instructor_db_model import Instructor_db_model
from app.schemas.instructor_api_schema import Instructor_api_schema
from app.repositories.instructor_repository import (
    get_all_instructors,
    get_instructor_by_id,
    add_instructor,
    update_instructor as repository_update_instructor
)


def get_instructors(db: Session):
    return get_all_instructors(db)


def create_instructor(db: Session, instructor: Instructor_api_schema):
    instructor_db = Instructor_db_model(
        instructor_id=instructor.instructor_id,
        instructor_name=instructor.instructor_name,
        department=instructor.department
    )

    return add_instructor(db, instructor_db)


def update_instructor(db: Session, instructor_id: str, instructor: Instructor_api_schema):
    instructor_db = get_instructor_by_id(db, instructor_id)

    if instructor_db is None:
        return None

    instructor_db.instructor_name = instructor.instructor_name
    instructor_db.department = instructor.department

    return repository_update_instructor(db, instructor_db)
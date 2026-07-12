from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.instructor_api_schema import Instructor_api_schema
from app.services.instructor_service import (
    get_instructors,
    create_instructor,
    update_instructor
)


router = APIRouter(
    prefix="/instructors",
    tags=["Instructors"]
)


@router.get("")
def read_instructors(db: Session = Depends(get_db)):
    return get_instructors(db)


@router.post("")
def add_instructor(instructor: Instructor_api_schema, db: Session = Depends(get_db)):
    return create_instructor(db, instructor)


@router.put("/{instructor_id}")
def modify_instructor(
    instructor_id: str,
    instructor: Instructor_api_schema,
    db: Session = Depends(get_db)
):
    updated_instructor = update_instructor(db, instructor_id, instructor)

    if updated_instructor is None:
        return {"message": "Instructor not found"}

    return updated_instructor
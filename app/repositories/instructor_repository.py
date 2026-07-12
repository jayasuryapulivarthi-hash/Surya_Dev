from sqlalchemy.orm import Session

from app.models.instructor_db_model import Instructor_db_model


def get_all_instructors(db: Session):
    return db.query(Instructor_db_model).all()


def get_instructor_by_id(db: Session, instructor_id: str):
    return db.query(Instructor_db_model).filter(
        Instructor_db_model.instructor_id == instructor_id
    ).first()


def add_instructor(db: Session, instructor_db: Instructor_db_model):
    db.add(instructor_db)
    db.commit()
    db.refresh(instructor_db)
    return instructor_db


def update_instructor(db: Session, instructor_db: Instructor_db_model):
    db.commit()
    db.refresh(instructor_db)
    return instructor_db
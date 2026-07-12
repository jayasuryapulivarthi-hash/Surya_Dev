from sqlalchemy.orm import Session

from app.models.course_db_model import Course_db_model


def get_all_courses(db: Session):
    return db.query(Course_db_model).all()


def get_course_by_id(db: Session, course_id: str):
    return db.query(Course_db_model).filter(
        Course_db_model.course_id == course_id
    ).first()


def add_course(db: Session, course_db: Course_db_model):
    db.add(course_db)
    db.commit()
    db.refresh(course_db)
    return course_db


def update_course(db: Session, course_db: Course_db_model):
    db.commit()
    db.refresh(course_db)
    return course_db
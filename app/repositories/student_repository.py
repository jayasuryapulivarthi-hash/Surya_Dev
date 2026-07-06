from app.models.student_db_model import Student_db_model
from sqlalchemy.orm import Session


def get_all_students(db: Session):
    return db.query(Student_db_model).all()


def get_student_by_id(db: Session, student_id: str):
    return db.query(Student_db_model).filter(
        Student_db_model.student_id == student_id
    ).first()


def add_student(db: Session, student_db: Student_db_model):
    db.add(student_db)
    db.commit()
    db.refresh(student_db)
    return student_db


def update_student(db: Session, student_db: Student_db_model):
    db.commit()
    db.refresh(student_db)
    return student_db

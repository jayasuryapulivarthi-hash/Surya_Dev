from sqlalchemy.orm import Session

from app.models.course_instructor_db_model import Course_instructor_db_model


def get_all_course_instructors(db: Session):
    return db.query(Course_instructor_db_model).all()


def get_course_instructor_by_ids(db: Session, course_id: str, instructor_id: str):
    return db.query(Course_instructor_db_model).filter(
        Course_instructor_db_model.course_id == course_id,
        Course_instructor_db_model.instructor_id == instructor_id
    ).first()


def add_course_instructor(db: Session, course_instructor_db: Course_instructor_db_model):
    db.add(course_instructor_db)
    db.commit()
    db.refresh(course_instructor_db)
    return course_instructor_db


def delete_course_instructor(db: Session, course_instructor_db: Course_instructor_db_model):
    db.delete(course_instructor_db)
    db.commit()
    return {"message": "Course instructor record deleted successfully"}
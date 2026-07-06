from app.models.student_db_model import Student_db_model
from app.schemas.student_api_schema import Student_api_schema
from app.repositories.student_repository import (
    get_all_students,
    get_student_by_id,
    add_student,
    update_student as repository_update_student,
)
from datetime import date


def get_students(db):
    return get_all_students(db)

def get_active_students(db):
    all_students = get_all_students(db)
    active_students = [student for student in all_students if student.is_active]
    return active_students


def create_student(db, student: Student_api_schema):
    calculated_is_active = student.end_date >= date.today()

    student_db = Student_db_model(
        full_name=student.full_name,
        email=student.email,
        course=student.course,
        age=student.age,
        student_join_year=student.student_join_year,
        is_active=calculated_is_active,
        address=student.address,
        start_date=student.start_date,
        end_date=student.end_date
    )

    added_student = add_student(db, student_db)
    return {
        "message": "Student records inserted successfully",
        "student_id": added_student.student_id
    }


def update_student(db, student_id: str, student: Student_api_schema):
    student_db = get_student_by_id(db, student_id)

    if student_db is None:
        return None

    student_db.full_name = student.full_name
    student_db.email = student.email
    student_db.course = student.course
    student_db.age = student.age
    student_db.student_join_year = student.student_join_year
    student_db.is_active = student.is_active
    student_db.address = student.address
    student_db.start_date = student.start_date
    student_db.end_date = student.end_date

    return repository_update_student(db, student_db)

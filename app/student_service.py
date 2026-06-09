from student_db_model import Student_db_model
from student_api_model import Student_api_model


def get_students(db):
    return db.query(Student_db_model).all()

def create_student(db, student: Student_api_model):
    # student_db = Student_db_model(**student.dict())

    student_db = Student_db_model(
        
        full_name=student.full_name,
        email=student.email,
        course=student.course,
        age=student.age,
        student_join_year=student.student_join_year,
        is_active=student.is_active,
        address=student.address
        
    )

    db.add(student_db)
    db.commit()
    db.refresh(student_db)

    # return student_db
    return {
        "message": "Student records inserted successfully",
        "student_id": student_db.student_id
    }
def update_student(db, student_id: str, student: Student_api_model):
    student_db = db.query(Student_db_model).filter(
        Student_db_model.student_id == student_id
    ).first()

    if student_db is None:
        return None

    student_db.full_name = student.full_name
    student_db.email = student.email
    student_db.course = student.course
    student_db.age = student.age
    student_db.student_join_year = student.student_join_year
    student_db.is_active = student.is_active
    student_db.address = student.address

    db.commit()
    db.refresh(student_db)

    return student_db
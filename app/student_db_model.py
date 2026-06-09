from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, Integer, Boolean, text


class Base(DeclarativeBase):
    pass


class Student_db_model(Base):
    __tablename__ = "students_unt"
    __table_args__ = {"schema": "student"}

#     student_id = Column(
#     String,
#     primary_key=True,
#     server_default=text("'UNT_2025_' || LPAD(nextval('student.students_unt_student_id_seq')::TEXT, 4, '0')")
# )
    student_id = Column(String, primary_key=True)
    full_name = Column(String)
    email = Column(String, nullable=True)
    course = Column(String)
    age = Column(Integer)
    student_join_year = Column(Integer)
    is_active = Column(Boolean)
    address = Column(String)
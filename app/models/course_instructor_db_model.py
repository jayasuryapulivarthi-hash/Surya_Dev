from sqlalchemy import Column, String

from app.db.database import Base


class Course_instructor_db_model(Base):
    __tablename__ = "course_instructors"
    __table_args__ = {"schema": "academics"}

    course_id = Column(String, primary_key=True)
    instructor_id = Column(String, primary_key=True)
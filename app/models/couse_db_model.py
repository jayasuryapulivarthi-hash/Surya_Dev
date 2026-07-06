from sqlalchemy import Column, String, Integer

from app.db.database import Base


class Course_db_model(Base):
    __tablename__ = "courses"
    __table_args__ = {"schema": "academics"}

    course_id = Column(String, primary_key=True)
    course_name = Column(String, nullable=False)
    credits = Column(Integer, nullable=False)
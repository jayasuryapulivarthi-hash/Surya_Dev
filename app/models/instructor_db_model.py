from sqlalchemy import Column, String

from app.db.database import Base


class Instructor_db_model(Base):
    __tablename__ = "instructors"
    __table_args__ = {"schema": "academics"}

    instructor_id = Column(String, primary_key=True)
    instructor_name = Column(String, nullable=False)
    department = Column(String, nullable=False)
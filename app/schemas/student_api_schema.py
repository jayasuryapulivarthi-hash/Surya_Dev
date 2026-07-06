from pydantic import BaseModel
from datetime import date


class Student_api_schema(BaseModel):
    full_name: str
    email: str | None
    course: str
    age: int
    student_join_year: int
    address: str
    start_date: date
    end_date: date



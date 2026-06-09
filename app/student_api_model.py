from pydantic import BaseModel


class Student_api_model(BaseModel):
    full_name: str
    email: str | None
    course: str
    age: int
    student_join_year: int
    is_active: bool
    address: str

    class Config:
        from_attributes = True

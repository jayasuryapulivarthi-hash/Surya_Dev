from pydantic import BaseModel


class Course_instructor_api_schema(BaseModel):
    course_id: str
    instructor_id: str
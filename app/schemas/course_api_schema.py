from pydantic import BaseModel


class Course_api_schema(BaseModel):
    course_id: str
    course_name: str
    credits: int
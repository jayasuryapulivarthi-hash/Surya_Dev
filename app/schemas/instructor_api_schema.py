from pydantic import BaseModel


class Instructor_api_schema(BaseModel):
    instructor_id: str
    instructor_name: str
    department: str
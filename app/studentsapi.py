from read_students import router as  students_router
from fastapi import FastAPI

studentapi = FastAPI()
studentapi.include_router(students_router)
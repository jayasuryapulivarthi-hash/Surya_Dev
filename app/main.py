from fastapi import FastAPI

from app.controllers.student_controller import router as student_router


student_app = FastAPI()


student_app.include_router(student_router)
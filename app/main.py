from fastapi import FastAPI

from app.controllers.student_controller import router as student_router
from app.controllers.course_controller import router as course_router
from app.controllers.instructor_controller import router as instructor_router
from app.controllers.course_instructor_controller import router as course_instructor_router


student_app = FastAPI()


student_app.include_router(student_router)
student_app.include_router(course_router)
student_app.include_router(instructor_router)
student_app.include_router(course_instructor_router)
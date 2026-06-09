from fastapi import FastAPI
from read_students import router as students_router

app = FastAPI()

app.include_router(students_router)


@app.get("/")
def home():
    return {"message": "Surya DB Learning API is running"}



from pathlib import Path

import pandas as pd
from sqlalchemy import text, Date

from app.db.database import SessionLocal,engine


DATA_FOLDER = Path(__file__).resolve().parents[2] / "data"

COURSES_FILE = DATA_FOLDER / "courses.csv"
INSTRUCTORS_FILE = DATA_FOLDER / "instructors.csv"
COURSEINSTRUCTORS_FILE = DATA_FOLDER / "courseinstructors.csv"
ENROLLMENTS_FILE = DATA_FOLDER / "enrollments.csv"

def load_courses(db):
    df = pd.read_csv(COURSES_FILE)

    for _, row in df.iterrows():
        db.execute(
            text("""
                INSERT INTO academics.courses (course_id, course_name, credits)
                VALUES (:course_id, :course_name, :credits)
            """),
            {
                "course_id": row["course_id"],
                "course_name": row["course_name"],
                "credits": int(row["credits"])
            }
        )
    print("Courses loaded successfully.")
    
def load_instructors():
    df = pd.read_csv(INSTRUCTORS_FILE)

    df.to_sql(
        "instructors",
        engine,
        schema="academics",
        if_exists="append",
        index=False
    )

    print("Instructors loaded successfully.")

def load_courseinstructors():
    df = pd.read_csv(COURSEINSTRUCTORS_FILE)

    df.to_sql(
        "course_instructors",
        engine,
        schema="academics",
        if_exists="append",
        index=False

    )

    print("Course instructors loaded successfully.")

def load_enrollments():
    df = pd.read_csv(ENROLLMENTS_FILE)
    df["enrollment_date"] = pd.to_datetime(df["enrollment_date"])

    df.to_sql(
        "enrollments",
        engine,
        schema="academics",
        if_exists="append",
        index=False
    )

    print("Enrollments loaded successfully.")

def load_all_academic_data():
    db = SessionLocal()

    try:
        load_courses(db)
        db.commit()

        load_instructors()
        load_courseinstructors()
        load_enrollments()

        print("All academic CSV files loaded successfully.")

    except Exception as error:
        db.rollback()
        print(f"Error while loading academic CSV files: {error}")

    finally:
        db.close()


if __name__ == "__main__":
    load_all_academic_data()


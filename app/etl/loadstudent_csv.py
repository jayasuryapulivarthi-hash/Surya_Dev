from datetime import date
from pathlib import Path

import pandas as pd

from app.db.database import SessionLocal
from app.models.student_db_model import Student_db_model


CSV_FILE_PATH = Path(__file__).resolve().parents[2] / "data" / "students.csv"


def load_students():
    df = pd.read_csv(CSV_FILE_PATH)

    df["start_date"] = pd.to_datetime(df["start_date"]).dt.date
    df["end_date"] = pd.to_datetime(df["end_date"]).dt.date

    df["is_active"] = df["end_date"].apply(lambda end_date: end_date >= date.today())

    valid_df = df[df["end_date"] >= df["start_date"]]

    db = SessionLocal()

    try:
        for _, row in valid_df.iterrows():
            student = Student_db_model(
                full_name=row["full_name"],
                email=row["email"],
                course=row["course"],
                age=int(row["age"]),
                student_join_year=int(row["student_join_year"]),
                address=row["address"],
                start_date=row["start_date"],
                end_date=row["end_date"],
                is_active=bool(row["is_active"])
            )

            db.add(student)

        db.commit()

        print(f"Inserted students: {len(valid_df)}")
        print(f"Skipped invalid students: {len(df) - len(valid_df)}")

    except Exception as error:
        db.rollback()
        print(f"Error while loading CSV: {error}")

    finally:
        db.close()


if __name__ == "__main__":
    load_students()
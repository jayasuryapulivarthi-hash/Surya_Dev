from fastapi import APIRouter
from database import get_connection

router = APIRouter()

# ─────────────────────────────
# GET ALL STUDENTS
# ─────────────────────────────
@router.get("/students")
def get_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM student.students_unt")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    students = []
    for row in rows:
        students.append({
            "student_id":        row[0],
            "full_name":         row[1],
            "email":             row[2],
            "department":        row[3],
            "age":               row[4],
            "student_join_year": row[5],
            "is_active":         row[6],
            "address":           row[7]
        })

    return {"students": students}
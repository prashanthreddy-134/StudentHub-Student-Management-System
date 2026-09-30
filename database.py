import sqlite3

DB_NAME = "students.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            course TEXT NOT NULL,
            marks REAL DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


def add_student(name, email, phone, course, marks):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO students
            (name, email, phone, course, marks)
            VALUES (?, ?, ?, ?, ?)
        """, (name, email, phone, course, marks))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


def get_students():
    conn = get_connection()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students ORDER BY id DESC")

    students = cursor.fetchall()
    conn.close()

    return students


def update_student(student_id, name, email, phone, course, marks):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE students
            SET name=?, email=?, phone=?, course=?, marks=?
            WHERE id=?
        """, (name, email, phone, course, marks, student_id))

        conn.commit()
        return cursor.rowcount > 0

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()

    return deleted


create_table()
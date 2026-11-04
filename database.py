import sqlite3
from pathlib import Path

import os

DB_NAME = os.getenv("STUDENTHUB_DB_PATH", "students.db")


def get_connection():
    conn = sqlite3.connect(
        DB_NAME,
        timeout=10,
        check_same_thread=False
    )
    conn.execute("PRAGMA busy_timeout = 10000")
    return conn


def create_table():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                course TEXT NOT NULL,
                marks REAL DEFAULT 0
            )
        """)


def add_student(name, email, phone, course, marks):
    try:
        with get_connection() as conn:
            conn.execute("""
                INSERT INTO students
                (name, email, phone, course, marks)
                VALUES (?, ?, ?, ?, ?)
            """, (name, email, phone, course, marks))

        return True

    except sqlite3.IntegrityError:
        return False


def get_students():
    with get_connection() as conn:
        return conn.execute("""
            SELECT id, name, email, phone, course, marks
            FROM students
            ORDER BY id DESC
        """).fetchall()


def update_student(student_id, name, email, phone, course, marks):
    try:
        with get_connection() as conn:
            cursor = conn.execute("""
                UPDATE students
                SET name=?, email=?, phone=?, course=?, marks=?
                WHERE id=?
            """, (
                name, email, phone, course, marks, student_id
            ))

            return cursor.rowcount > 0

    except sqlite3.IntegrityError:
        return False


def delete_student(student_id):
    with get_connection() as conn:
        cursor = conn.execute(
            "DELETE FROM students WHERE id=?",
            (student_id,)
        )

        return cursor.rowcount > 0


create_table()
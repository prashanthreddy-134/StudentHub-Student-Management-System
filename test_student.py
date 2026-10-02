import pytest
import database


@pytest.fixture
def test_db(tmp_path, monkeypatch):
    """Create a separate temporary database for each test."""
    db_file = tmp_path / "test_students.db"

    monkeypatch.setattr(database, "DB_NAME", db_file)
    database.create_table()

    return database


def test_add_student(test_db):
    result = test_db.add_student(
        "Rahul", "rahul@gmail.com", "9876543210",
        "Computer Science", 85
    )

    assert result is True

    students = test_db.get_students()
    assert len(students) == 1
    assert students[0][1] == "Rahul"


def test_view_students(test_db):
    test_db.add_student(
        "Rahul", "rahul@gmail.com", "9876543210",
        "Computer Science", 85
    )
    test_db.add_student(
        "Priya", "priya@gmail.com", "9876543211",
        "Information Science", 90
    )

    students = test_db.get_students()

    assert len(students) == 2
    assert students[0][1] == "Priya"
    assert students[1][1] == "Rahul"


def test_update_student(test_db):
    test_db.add_student(
        "Rahul", "rahul@gmail.com", "9876543210",
        "Computer Science", 85
    )

    student_id = test_db.get_students()[0][0]

    result = test_db.update_student(
        student_id, "Rahul Kumar", "rahul@gmail.com",
        "9876543210", "Computer Science", 95
    )

    assert result is True

    student = test_db.get_students()[0]
    assert student[1] == "Rahul Kumar"
    assert student[5] == 95


def test_delete_student(test_db):
    test_db.add_student(
        "Rahul", "rahul@gmail.com", "9876543210",
        "Computer Science", 85
    )

    student_id = test_db.get_students()[0][0]

    result = test_db.delete_student(student_id)

    assert result is True
    assert len(test_db.get_students()) == 0


def test_duplicate_email(test_db):
    test_db.add_student(
        "Rahul", "rahul@gmail.com", "9876543210",
        "Computer Science", 85
    )

    result = test_db.add_student(
        "Priya", "rahul@gmail.com", "9876543211",
        "Information Science", 90
    )

    assert result is False
    assert len(test_db.get_students()) == 1


def test_update_nonexistent_student(test_db):
    result = test_db.update_student(
        9999, "Rahul", "rahul@gmail.com",
        "9876543210", "Computer Science", 85
    )

    assert result is False


def test_delete_nonexistent_student(test_db):
    result = test_db.delete_student(9999)

    assert result is False
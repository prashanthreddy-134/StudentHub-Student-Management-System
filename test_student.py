def test_add_student():
    students = []

    student = {
        "id": 101,
        "name": "Rahul",
        "age": 20
    }

    students.append(student)

    assert len(students) == 1
    assert students[0]["name"] == "Rahul"
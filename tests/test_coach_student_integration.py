from lib.coach import Coach
from lib.student import Student
import pytest

# TODO this will be implemented after the student class is created 
# def test_add_student_with_non_class_object():
#     coach = Coach("jay")

#     student = "test student"

#     with pytest.raises(TypeError) as error:
#         coach.add_student(student)

#     error_message = str(error.value)

#     assert error_message == "Not a student"


def test_add_student():
    coach = Coach("jay")

    student = Student("student")

    coach.add_student(student)

    assert coach.students == [student]
    assert len(coach.students) == 1

def test_count_submissions_with_one_student():
    coach = Coach("jay")

    student = Student("student")
    student.add_submission("maths")
    student.add_submission("english")
    student.add_submission("french")

    coach.add_student(student)

    assert coach.count_submissions() == 3

def test_count_submissions_with_multiple_students():
    coach = Coach("jay")

    student = Student("Student")
    student2 = Student("Student2")
    student3 = Student("Student3")

    for i in range(0, 5):
        student.add_submission(str(i))

    for i in range(0, 2):
        student2.add_submission(str(i))

    for i in range(0, 32):
        student3.add_submission(str(i))

    coach.add_student(student)
    coach.add_student(student2)
    coach.add_student(student3)

    assert coach.count_submissions() == 39

def test_print_student_names_with_one_student():
    coach = Coach("jay")

    student = Student("John")
    coach.add_student(student)

    assert coach.print_student_names() == "John"


def test_print_student_names_with_multiple_students():
    coach = Coach("jay")

    student = Student("John")
    student2 = Student("Gabe")
    student3 = Student("John Cena")

    coach.add_student(student)
    coach.add_student(student2)
    coach.add_student(student3)

    assert coach.print_student_names() == "John, Gabe, John Cena"

def test_upload_submission_for_students_with_one_student():
    coach = Coach("jay")

    student = Student("student")
    coach.add_student(student)

    assignment = "maths"
    coach.upload_submission_for_students(assignment)

    assert coach.count_submissions() == 1
    assert student.count_submissions() == 1


def test_upload_submission_for_students_with_multiple_students():
    # ASSIGN
    coach = Coach("jay")

    # create mocks
    student = Student("student")
    student2 = Student("student1")
    student3 = Student("student2")

    # add mocks
    coach.add_student(student)
    coach.add_student(student2)
    coach.add_student(student3)

    student.add_submission("english")

    student3.add_submission("english")
    student3.add_submission("french")
    student3.add_submission("ICT")

    # add the assignment
    assignment = "maths"
    coach.upload_submission_for_students(assignment)

    assert coach.count_submissions() == 7
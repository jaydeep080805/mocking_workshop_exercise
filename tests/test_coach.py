from lib.coach import Coach
from mock import Mock
import pytest

# AAA (Arrange, Act, Assert)


def test_coach_initialisation():
    coach = Coach("jay")

    assert coach.name == "jay"
    assert coach.students == []

def test_add_student():
    coach = Coach("jay")

    student = Mock()

    coach.add_student(student)

    assert coach.students == [student]
    assert len(coach.students) == 1

# TODO this will be implemented after the student class is created 
# def test_add_student_with_non_class_object():
#     coach = Coach("jay")

#     student = "test student"

#     with pytest.raises(TypeError) as error:
#         coach.add_student(student)

#     error_message = str(error.value)

#     assert error_message == "Not a student"


def test_count_submissions_with_one_student():
    coach = Coach("jay")

    student = Mock()
    student.count_submissions.return_value = 3
    print(f"MOCKED RETURN VALUE: {student.count_submissions()}")

    coach.add_student(student)

    assert coach.count_submissions() == 3

def test_count_submissions_with_multiple_students():
    coach = Coach("jay")

    student = Mock()
    student.count_submissions.return_value = 3

    student2 = Mock()
    student2.count_submissions.return_value = 5

    student3 = Mock()
    student3.count_submissions.return_value = 32

    coach.add_student(student)
    coach.add_student(student2)
    coach.add_student(student3)

    assert coach.count_submissions() == 40

def test_print_student_names_with_one_student():
    coach = Coach("jay")

    student = Mock()
    student.get_name.return_value = "John"

    coach.add_student(student)

    assert coach.print_student_names() == "John"

def test_print_student_names_with_multiple_students():
    coach = Coach("jay")

    student = Mock()
    student.get_name.return_value = "John"

    student2 = Mock()
    student2.get_name.return_value = "Gabe"

    student3 = Mock()
    student3.get_name.return_value = "John Cena"

    coach.add_student(student)
    coach.add_student(student2)
    coach.add_student(student3)

    assert coach.print_student_names() == "John, Gabe, John Cena"


def test_upload_submission_for_students_with_one_student():
    coach = Coach("jay")

    student = Mock()
    coach.add_student(student)

    assignment = "maths"
    coach.upload_submission_for_students(assignment)

    student.count_submissions.return_value = 1

    assert coach.count_submissions() == 1

def test_upload_submission_for_students_with_multiple_students():
    # ASSIGN
    coach = Coach("jay")

    # create mocks
    student = Mock()
    student2 = Mock()
    student3 = Mock()

    # add mocks
    coach.add_student(student)
    coach.add_student(student2)
    coach.add_student(student3)

    # add the assignment
    assignment = "maths"
    coach.upload_submission_for_students(assignment)

    # assuming before the function call:
        # student 1 - 3 submissions
        # student 2 - 0 submissions
        # student 1 - 5 submissions
    student.count_submissions.return_value = 4
    student2.count_submissions.return_value = 1
    student3.count_submissions.return_value = 6

    assert coach.count_submissions() == 11
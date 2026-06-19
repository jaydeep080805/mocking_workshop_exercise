from lib.student import Student
import pytest

def test_student_initialisation():
    student = Student("jay")

    assert student.name == "jay"
    assert student.submissions == []
    assert len(student.submissions) == 0

def test_add_submission():
    student = Student("jay")

    submission = "Computer Science"
    student.add_submission(submission)

    assert student.submissions == [submission]
    assert len(student.submissions) == 1

def test_count_submissions():
    student = Student("jay")

    student.add_submission("Computer Science")
    student.add_submission("maths")
    student.add_submission("english")

    assert student.count_submissions() == 3
    
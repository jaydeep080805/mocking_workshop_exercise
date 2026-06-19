class Student:
    def __init__(self, name):
        self.name = name
        self.submissions = []

    def add_submission(self, submission):
        self.submissions.append(submission)

    def count_submissions(self):
        return len(self.submissions)
class Student:
    def __init__(self, name):
        self.name = name
        self.submissions = []

    def get_name(self):
        return self.name

    def add_submission(self, submission):
        self.submissions.append(submission)

    def count_submissions(self):
        return len(self.submissions)
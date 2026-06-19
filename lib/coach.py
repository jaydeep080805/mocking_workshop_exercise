class Coach:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        # TODO this will be implemented after the student class is created 
        # if isinstance(student, Student):
        #     return TypeError("Not a student")
        
        self.students.append(student)
    
    def count_submissions(self):
        total_submissions = 0

        for student in self.students:
            total_submissions += student.count_submissions()

        print(f"TOTAL SUBMISSIONS: {total_submissions}")
        return total_submissions
    
    def print_student_names(self):
        list_of_names = []

        for student in self.students:
            list_of_names.append(student.get_name())

        return ", ".join(list_of_names)
    
    def upload_submission_for_students(self, submission):
        for student in self.students:
            student.add_submission(submission)
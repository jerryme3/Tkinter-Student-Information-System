class Student:

    def __init__(self, full_name: str, student_id: str, contact_number: str, email: str, password: str, teacher: str, grades, section: str):
        self.full_name = full_name
        self.student_id = student_id
        self.contact_number = contact_number
        self.email = email
        self.password = password
        self.teacher = teacher
        self.grades = grades
        self.section = section
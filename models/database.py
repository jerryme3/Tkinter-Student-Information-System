import csv
from models.student import Student

class Repository:

    def __init__(self):
        self.__file_path = 'combined.csv'

    def append(self, student: Student):
        with open(self.__file_path, mode='a', newline='') as repository:
            writer = csv.writer(repository)

            writer.writerow([student.full_name, student.student_id, student.contact_number, student.email, student.password, student.teacher, student.grades, student.section])

    def account_exists(self, email: str, password: str) -> bool:
        with open(self.__file_path, mode='r') as repository:
            reader = csv.reader(repository)

            for row in reader:
                if email in row and password in row:
                    return True

        return False

    def info_already_exists(self, information: str) -> bool:
        with open(self.__file_path, mode='r') as repository:
            reader = csv.reader(repository)

            for row in reader:
                if information in row:
                    return True

        return False

    def get_student(self, email: str, password: str) -> Student | None:
        with open(self.__file_path, mode='r') as repository:
            reader = csv.reader(repository)

            for row in reader:

                if email in row and password in row:

                    return Student(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])


        return None

    def edit_student(self, new_student: Student):
        with open(self.__file_path, mode='r') as repository:
            reader = csv.reader(repository)
            rows = list(reader)

            for i, row in enumerate(rows):
                if new_student.email in row:
                    rows[i] = [new_student.full_name,
                               new_student.student_id,
                               new_student.contact_number,
                               new_student.email,
                               new_student.password,
                               new_student.teacher,
                               new_student.grades,
                               new_student.section
                               ]

        with open(self.__file_path, mode='w', newline='') as repository:
            writer = csv.writer(repository)
            writer.writerows(rows)

    def get_table(self) -> list:

        table = []

        with open(self.__file_path, mode="r") as repository:
            reader = csv.reader(repository)

            for row in reader:
                table.append(row)

        return table

    def get_section_table(self, section: str) -> list:
        if section == "Gumamela Grove":
            section_file = 'gumamela_grove.csv'
        elif section == "Sunflower Field":
            section_file = 'sunflower_field.csv'
        elif section == "Rose Garden":
            section_file = 'rose_garden.csv'
        else:
            return []

        with open(file=section_file, mode='r') as repository:
            reader = csv.reader(repository)
            return list(reader)




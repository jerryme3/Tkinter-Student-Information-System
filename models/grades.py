import random as rnd

def generate_grades() -> list:
    grades = []

    for i in range(9):
        grades.append(rnd.randint(75, 100))

    return grades
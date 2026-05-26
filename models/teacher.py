import random as rnd

teachers = (
    "Tom Flestado",
    "Allen Balinbin",
    "Sid Serrano"
)

def get_teacher():
    return rnd.choice(teachers)
import random as rnd

sections = (
    "Rose",
    "Sunflower",
    "Gumamela"
)

def get_section():
    return sections[rnd.randint(0, len(sections))]
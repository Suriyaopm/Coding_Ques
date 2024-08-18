import random
from questions import questions

def generate_questions(num_easy, num_medium, num_difficult):
    selected_questions = {
        "easy": random.sample(questions["easy"], min(num_easy, len(questions["easy"]))),
        "medium": random.sample(questions["medium"], min(num_medium, len(questions["medium"]))),
        "difficult": random.sample(questions["difficult"], min(num_difficult, len(questions["difficult"]))),
    }
    return selected_questions

import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_round():
    number = random.randint(1, 100)
    question = print(f'Question: {number}')

    if number % 2 == 0:
        right_answer: str = 'yes'
    else:
        right_answer: str = 'no'
    return question, right_answer

import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_round():
    number = random.randint(1, 100)
    question = f'Question: {number}'

    if is_even(number):
        right_answer: str = 'yes'
    else:
        right_answer: str = 'no'
    return question, right_answer

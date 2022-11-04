import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def play_round():
    number = random.randint(1, 100)
    question: str = f'Question: {number}'

    if is_even(number):
        right_answer: str = 'yes'
    else:
        right_answer: str = 'no'
    return question, right_answer

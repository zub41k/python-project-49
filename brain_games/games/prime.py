import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_given(number):
    d = 2
    while number % d != 0:
        d += 1
    if d == number:
        return True
    return False


def play_round():

    number = random.randint(1, 1000)
    question = f'Question: {number}'

    if is_given(number):
        right_answer: str = 'yes'
    else:
        right_answer: str = 'no'

    return question, right_answer

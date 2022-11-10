import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_round():
    number = random.randint(1, 100)
    question = number
    right_answer: str = 'yes' if is_even(number) else 'no'
    return question, right_answer

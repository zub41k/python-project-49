import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return False

    if number % 2 == 0:
        return number == 2

    d = 3
    while d * d <= number and number % d != 0:
        d += 2
    return d * d > number


def generate_round():

    number = random.randint(1, 1000)
    question = f'Question: {number}'

    if is_prime(number):
        right_answer: str = 'yes'
    else:
        right_answer: str = 'no'

    return question, right_answer

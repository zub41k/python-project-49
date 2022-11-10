import random
import math

RULES = 'Find the greatest common divisor of given numbers.'


def generate_round():

    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)

    question = f'{first_number} {second_number}'

    right_answer = math.gcd(first_number, second_number)
    return question, str(right_answer)

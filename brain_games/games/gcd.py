import random
import math

RULES = 'Find the greatest common divisor of given numbers.'


def play_round():

    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)

    question = print(f'Question: {first_number} {second_number}')

    right_answer = math.gcd(first_number, second_number)
    return question, str(right_answer)

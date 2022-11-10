import random

RULES = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']
START = 1
FINISH = 10


def calculate(operator, first_number, second_number):

    if operator == '+':
        return first_number + second_number
    if operator == '-':
        return first_number - second_number
    if operator == '*':
        return first_number * second_number


def generate_round():
    operator = random.choice(OPERATORS)
    first_number = random.randint(START, FINISH)
    second_number = random.randint(START, FINISH)

    right_answer = calculate(operator, first_number, second_number)
    question = f'{first_number} {operator} {second_number}'

    return question, str(right_answer)

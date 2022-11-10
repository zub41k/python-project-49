import random

RULES = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']


def generate_equation(operator, first_number, second_number):

    if operator == '+':
        return first_number + second_number
    if operator == '-':
        return first_number - second_number
    if operator == '*':
        return first_number * second_number


def generate_round():
    operator = random.choice(OPERATORS)
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)

    right_answer = generate_equation(operator, first_number, second_number)
    question = f'{first_number} {operator} {second_number}'

    return question, str(right_answer)

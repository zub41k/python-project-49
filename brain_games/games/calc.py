import random

RULES = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']


def generate_round():

    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    operator = random.choice(OPERATORS)
    question = f'Question: {first_number} {operator} {second_number}'

    if operator == '+':
        right_answer = first_number + second_number
    if operator == '-':
        right_answer = first_number - second_number
    if operator == '*':
        right_answer = first_number * second_number
    return question, str(right_answer)

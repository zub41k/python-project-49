from random import randint

RULES = 'What number is missing in the progression?'


def generate_list():

    interval = randint(1, 10)
    start = randint(1, 100)
    stop = start + (interval * 10)

    list = [str(i) for i in range(start, stop, interval)]

    return list


def generate_round():
    progression = generate_list()

    skip = randint(0, 9)
    right_answer = progression[skip]

    progression[skip] = ".."
    question = 'Question: ' + ' '.join(progression)

    return question, right_answer

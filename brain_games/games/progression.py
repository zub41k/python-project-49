from random import randint

RULES = 'What number is missing in the progression?'


def generate_list(start, stop, interval):

    list = [str(i) for i in range(start, stop, interval)]

    return list


def generate_round():
    interval = randint(1, 10)
    start = randint(1, 100)
    stop = start + (interval * 10)
    progression = generate_list(start, stop, interval)

    skip = randint(0, len(progression) - 1)
    right_answer = progression[skip]

    progression[skip] = ".."
    question = ' '.join(progression)

    return question, right_answer

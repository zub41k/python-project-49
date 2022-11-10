import prompt

# Winning number of rounds
ROUND_COUNT = 3


def play(game):

    print("Welcome to the Brain Games!")

    name = prompt.string('May I have your name? ')

    print(f'Hello, {name}!')

    print(game.RULES)

    count_answer = 0
    while count_answer < ROUND_COUNT:
        question, right_answer = game.generate_round()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == right_answer:
            print('Correct!')
            count_answer += 1
        else:
            print(
                f"'{answer}' is wrong answer."
                f"\nCorrect answer was '{right_answer}'."
                f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')

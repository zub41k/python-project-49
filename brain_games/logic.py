import prompt


def greeting(game):

    print("Welcome to the Brain Games!")

    name = prompt.string('May I have your name? ')

    print('Hello, ' + name + '!')

    print(game.RULES)

    count_answer = 0
    while count_answer < 3:
        question: str
        question, right_answer = game.play_round()
        answer = prompt.string('Your answer: ')

        if answer == right_answer:
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer."
                f"\nCorrect answer was '{right_answer}'."
                f"Let's try again, {name}!")
            break
        count_answer += 1

        if count_answer == 3:
            print(f'Congratulations, {name}!')
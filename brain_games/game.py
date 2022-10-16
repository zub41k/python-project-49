import prompt
import random


def checking_num():
    print("Welcome to the Brain Games!")

    name = prompt.string('May I have your name? ')

    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    count_answer = 0
    while count_answer < 3:
        number = random.randint(1, 100)

        if number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        print(f'Question :{number}')
        answer = prompt.string('Your answer :')

        if answer == 'yes' and right_answer == 'yes':
            print('Correct!')
        elif answer == 'no' and right_answer == 'no':
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

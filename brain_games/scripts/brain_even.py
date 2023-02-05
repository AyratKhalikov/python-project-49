import prompt
from random import randint

def greeting(game_description):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello,", name + "!")
    print(game_description)
    return name


def main():
    game_description = 'Answer "yes" if the number is even, otherwise answer "no"'
    try_num = 0

    name = greeting(game_description)
    for i in range(3):
        question_value = randint(1, 100)
        print('Question: ', question_value)
        answer = prompt.string('Your answer: ')
        if (answer == 'yes') and (question_value % 2 == 0):
            try_num = try_num + 1
            print('Correct!')
        elif (answer == 'no') and (question_value % 2 != 0):
            try_num = try_num + 1
            print('Correct!')
        else:
            opposite_answer = 'yes'
            if answer == 'yes':
                opposite_answer = 'no'
            print("'" + answer + "'" + " is wrong answer ;(. Correct answer was '" + opposite_answer + "'.")
            print("Let's try again, " + name + "!")
            return

    if try_num == 3:
        print("Congratulations, " + name + "!")


if __name__ == '__main__':
    main()

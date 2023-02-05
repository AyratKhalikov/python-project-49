import prompt
from random import randint

def greeting(game_description):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello,", name + "!")
    print(game_description)
    return name


def main():
    game_description = 'What is the result of the expression?'
    try_num = 0

    name = greeting(game_description)
    for i in range(3):
        question_value1 = randint(1, 100)
        question_value2 = randint(1, 100)
        question_value3 = randint(1, 3)

        if question_value3 == 1:
            question_value3 = '+'
            question_check = question_value1 + question_value2
        elif question_value3 == 2:
            question_value3 = '-'
            question_check = question_value1 - question_value2
        else:
            question_value3 = '*'
            question_check = question_value1 * question_value2

        print('Question: ', question_value1, question_value3, question_value2)
        answer = prompt.string('Your answer: ')
        
        if answer.isdigit() == True:
            if int(answer) == question_check:
                try_num = try_num + 1
                print('Correct!')
            else:
                print("'" + str(answer) + "'" + " is wrong answer ;(. Correct answer was '" + str(question_check) + "'.")
                print("Let's try again, " + name + "!")
                return
        else:
            print("'" + str(answer) + "'" + " is wrong answer ;(. Correct answer was '" + str(question_check) + "'.")
            print("Let's try again, " + name + "!")
            return

    if try_num == 3:
        print("Congratulations, " + name + "!")


if __name__ == '__main__':
    main()

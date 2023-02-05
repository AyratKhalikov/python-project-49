import prompt
from random import randint

def greeting(game_description):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello,", name + "!")
    print(game_description)
    return name


def main():
    game_description = 'What number is missing in the progression?'
    try_num = 0

    name = greeting(game_description)
    for i in range(3):
        start = randint(1, 100)
        len = randint(5, 10)
        step = randint(1, 10)
        choice = randint(1, len)


        question_value1 = str(slice[start:chioce:step]) + '?' + str(slice(choice+1:start+len*step:step))
        question_check = question_value1[choice]

        print('Question: ', question_value1)
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

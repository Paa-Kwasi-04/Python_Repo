import random as r
from termcolor import cprint

QUESTION = 'question'
OPTIONS = 'options'
ANSWER = 'answer'

question_List = [
    {
        QUESTION: 'What is the capital of France?',
        OPTIONS: ['A. Berlin', 'B. Madrid', 'C. Paris', 'D. Rome'],
        ANSWER: 'C'
    },
    {
        QUESTION: 'Which planet is known as the red planet?',
        OPTIONS: ['A. Earth', 'B. Mars', 'C. Jupiter', 'D. Saturn'],
        ANSWER: 'B'
    },
    {
        QUESTION: 'What is the largest ocean on Earth?',
        OPTIONS: ['A. Atlantic', 'B. Indian', 'C. Arctic', 'D. Pacific'],
        ANSWER: 'D'
    },
]


def ask_question(index, question, options):
    print(f'Question {index}: {question}? ')

    for x in options:
        print(x)

    return input('Your answer: ').upper().strip()


def run_quiz(quiz):

    r.shuffle(quiz)
    score = 0

    for n, item in enumerate(quiz):
        ans = ask_question(n+1, item[QUESTION], item[OPTIONS])

        if ans == item[ANSWER]:  # check if your ans is correct
            cprint('Correct!', 'green')
            score += 1  # records your score
        else:
            cprint(f'Wrong! The correct answer is {item[ANSWER]}', 'red')

    print(f'Quiz over! Your final score is {score} out of {len(quiz)}')


if __name__ == '__main__':
    run_quiz(question_List)

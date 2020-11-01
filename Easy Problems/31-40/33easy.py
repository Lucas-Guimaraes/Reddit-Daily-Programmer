# https://www.reddit.com/r/dailyprogrammer/comments/rl24e/3302012_challenge_33_easy/

import random

list_of_questions = ['are you cool?', 'you\'re neat', 'what\'s your name?', 'what a wonderful world']
list_of_answers = ['yeah', 'thanks', 'name', 'indeed']
questions_and_answers = zip(list_of_questions, list_of_answers)
game_run = True

while game_run:
    index_number = random.randint(0, len(questions_and_answers)-1)
    print("The current question is: {question}\n".format(question=list_of_questions[index_number]))
    user_answer = raw_input("Put in the answer to the question - all answers will default to lowercase.\n\nIf you would like to quit, please press 'n':\n\n")
    user_answer = user_answer.lower()

    if user_answer == list_of_answers[index_number]:
        print('\n{answer} is correct\n'.format(answer=user_answer))

    elif user_answer == 'n':
        print("\nGoodbye")
        game_run = False

    else:
        print('\n{wrong_answer} is incorrect. The answer is {answer}\n'.format(wrong_answer=user_answer,answer=list_of_answers[index_number]))

raw_input("\nPress enter to exit.\n\n")
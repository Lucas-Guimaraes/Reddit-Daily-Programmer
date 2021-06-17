# https://www.reddit.com/r/dailyprogrammer/comments/15ul7q/122013_challenge_115_easy_guessthatnumber_game/
import random

#function that starts the game
def guess_that_number():
    print("C> Hello! Welcome to Guess That Number. Guess a number between 1-100")
    answer = random.randrange(1, 100)
    user_input = 101
    #gives the answer, and a starting user input
    while user_input != answer:
        user_input = int(raw_input("U> "))
        #if it is correct, the game ends
        if user_input == answer:
            print("C> That's right! {} is my number!".format(user_input))
            return
        #user guess is too high
        elif user_input > answer:
            print("C> Wrong. {} is above my number".format(user_input))
        #user guess is too low
        else:
            print("C> Wrong. {} is below my number".format(user_input))
            

guess_that_number()
raw_input()
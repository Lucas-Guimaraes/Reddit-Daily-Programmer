#https://www.reddit.com/r/dailyprogrammer/comments/2mlfxp/20141117_challenge_189_easy_hangman/

#'words_alpha.txt' is a supplementary file to this challenge.
import random

easy = []
medium = []
hard = []
f = open("words_alpha.txt", "r")
#prepares our list
for line in f.readlines():
    new = line.replace("\n", "")
    if len(new) < 6:
        easy.append(new)
    elif len(new) < 12:
        medium.append(new)
    else:
        hard.append(new)

def hangman(answer):
    print("\n")
    guesses = 6
    answer_lst = list(answer)
    user_lst = list('_' * len(answer))
    ascii_str = 'abcdefghijklmnopqrstuvwxyz'
    while user_lst != answer_lst:
        print("Options are: " + ascii_str + ". You have {} guesses".format(guesses))
        user_str = "".join(user_lst)
        print("\n")
        print(user_str)
        letter = raw_input()
        if len(letter) == 1 and letter.isalpha() and letter in ascii_str:
            letter = letter.lower()
            ascii_str = ascii_str.replace(letter, "")
            if letter in answer:
                for i in range(len(answer_lst)):
                    if answer_lst[i] == letter:
                        user_lst[i] = letter
                if user_lst == answer_lst:
                    print("Correct! The word is {}. You took {} guesses.".format(answer, guesses))
                    break
            else:
                guesses -= 1
                if guesses == 0:
                    print("Aw. You lose. The word was {}.".format(answer))
                    break

def selection(u_input):
    statement = "{} is not a valid difficulty!".format(u_input)
    if u_input.isalpha:
        u_input = u_input.lower()
        if u_input == 'easy':
            hangman(random.choice(easy))
        elif u_input == 'medium':
            hangman(random.choice(medium))
        elif u_input == 'hard':
            hangman(random.choice(hard))
        else:
            print(statement)
    else:
        print(statement)
    

print("Welcome to hangman!")
print("This program plays the classic game hangman!")
print("Select your difficulty before starting. The difficulty options are 'easy', 'medium' and 'hard'.")
print("\n~*~----------------~*~\n")
hang = True
while hang:
    difficulty = raw_input()
    if difficulty == 'q' or difficulty == 'Q':
        break
    selection(difficulty)
hangman(random.choice(easy))

raw_input("Press enter to exit.")
# https://www.reddit.com/r/dailyprogrammer/comments/3h9pde/20150817_challenge_228_easy_letters_in/

import string
letters = string.ascii_lowercase

def order_word(word):
    #Grabs the index from each letter so it can be sorted
    order = [letters.index(i) for i in word]
    print(order)
    #Checks if in order, if reverse, or none
    if order == sorted(order, key=int):
        return word + " IN ORDER"
    elif order == sorted(order, key=int, reverse=True):
        return word + " REVERSE ORDER"
    else:
        return word + " NOT IN ORDER"

#Explination
print("Welcome to Order Word")
print("Put in a word and print out whether the letters are in alphabetical order")
print("\n~*~----------------~*~\n")

#Checks input, quit case included
order = True
while order:
    w = raw_input().lower()
    if w == 'q':
        break
    if w.isalpha():
        print(order_word(w))

raw_input("Press enter to exit.")
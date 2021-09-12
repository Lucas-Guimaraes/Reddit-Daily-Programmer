# https://www.reddit.com/r/dailyprogrammer/comments/3q9vpn/20151026_challenge_238_easy_consonants_and_vowels/

import random

#Function to make our random word (or words)
def random_word(word):
    new_word = ''
    letters = {'c': 'bcdfghjklmnpqrstvwxyz', 'v': 'aeiou', ' ': ' '}
    #Checks each letter
    for i in word:
        ran_letter = random.choice(letters[i.lower()])
        #If the letter is uppercase, print upper
        if i.isupper():
            ran_letter = ran_letter.upper()
        new_word += ran_letter
    return new_word



print("Welcome to cvCV")
print("c for a constant, v for a vowel. Capitalize for their respective ones")
print("Spaces are allowed, too")
print("\n~*~----------------~*~\n")

cv_language = True
while cv_language:
    cv = raw_input()
    #quit code
    if cv.lower() == 'q':
        break

    # error handling
    cv_test = cv.lower().replace('v', 'c').replace(' ', '')
    cv_test_2 = 'c'
    if set(cv_test) == set(cv_test_2):
        print(random_word(cv))

raw_input("Press enter to exit.")

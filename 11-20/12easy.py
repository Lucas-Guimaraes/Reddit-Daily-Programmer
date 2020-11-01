#https://www.reddit.com/r/dailyprogrammer/comments/pxs2x/2202012_challenge_12_easy/
import random

string_input = raw_input("Give me a string!")
factorial_list = []

def permutation(x):
    count_factorial = len(x)
    count_check = len(x)
    factorial_store = 1
    factorial_list = []
    for i in range(count_check):
        factorial_store *= count_factorial
        count_factorial -= 1
        
    word_shuffle = factorial_store
    
    while factorial_store > 0:

        random_word = ''.join(random.sample(x, len(x)))

        if random_word not in factorial_list:
            print random_word
            factorial_list.append(random_word)
            factorial_store -= 1



permutation(string_input)
raw_input()
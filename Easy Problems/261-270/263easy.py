#https://www.reddit.com/r/dailyprogrammer/comments/4fc896/20160418_challenge_263_easy_calculating_shannon/

import math

def entropy(somestring):
    #Starts total; gets every unique letter
    total = 0.0
    letters = set(somestring)

    #For every unique letter, divide it by total letters
    #Multiply by it's binary
    #Add to total
    for letter in letters:
        cur = somestring.count(letter)/float(len(somestring))
        cur = cur*math.log(cur, 2)
        total += cur

    #Make total positive
    return -1*total

#Intro
print("Welcome to calculating Shannon Entropy of a String!")
print("You will give one input, a string.")
print("This program will return its Shannon")
print("\n~*~--------~*~\n")

#Input
shannon = True
while shannon:
    t = raw_input()
    t = t.lower()
    if t == 'q':
        break
    print(entropy(t))

raw_input("Press enter to exit.")
# https://www.reddit.com/r/dailyprogrammer/comments/11shra/10202012_challenge_105_easy_word_unscrambler/

#This is a supplementary file to 105easy.py
#This program will take the initial file
#and then shuffle every single letter

from random import shuffle

initial = open("105easy-test.txt", "r")
scramble = open("105easy-test-scrambled.txt", "r+")
def split(word):
    return [char for char in word]

for word in initial.readlines():

    temp_word = word
    temp_word = temp_word.replace("\n", "")
    temp_word = split(temp_word)
    
    shuffle(temp_word)
    
    temp_word = ''.join(temp_word)
    print(temp_word)
    temp_word = temp_word.lower()
    scramble.write(temp_word + "\n")



initial.close()
scramble.close()
raw_input()
# https://www.reddit.com/r/dailyprogrammer/comments/11shra/10202012_challenge_105_easy_word_unscrambler/

#This is a supplementary file to 105easy.py
#This will open the original text document, and then lowercase every word

from random import shuffle

initial = open("105easy-test.txt", "r")
lower = open("105easy-test-lower.txt", "r+")

#cleans up formatting
for word in initial.readlines():
    
    temp_word = word
    temp_word = temp_word.replace("\n", "")
    temp_word = temp_word.lower()
    lower.write(temp_word + "\n")



initial.close()
lower.close()
raw_input()
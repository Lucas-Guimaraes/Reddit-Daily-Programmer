# https://www.reddit.com/r/dailyprogrammer/comments/2w84hl/20150216_challenge_202_easy_i_am_bender_please/

import sys

#Converts binary sequence to words
def bin_to_words(lines):
    word = ''
    for i in range(0,len(lines),8):
        word += chr(int(lines[i:i+8], 2)) #Int base 2, chr is ascii
    return word

#Fancy print statements to introduce the user to the program
print("Welcome to binary to words!")
print("Input a binary sequence, and this will output the words!")
print("Remember to press enter, then CTRL+D after you're done, followed by another enter. If that does not work, try ctrl+z!")
print("\n~*~----------------~*~\n")

#gets multi-line input, converts list to string, then replaces all new lines
lines = sys.stdin.readlines()
lines = ''.join(lines)
lines = lines.replace('\n', '')

#Prints the word, followed by a prompt to exit
print("\n~*~----------------~*~\n")
print(bin_to_words(lines))
print("\n~*~----------------~*~\n")

raw_input("Press enter to exit.")
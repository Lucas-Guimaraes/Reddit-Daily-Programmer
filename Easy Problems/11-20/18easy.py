# https://www.reddit.com/r/dailyprogrammer/comments/qit0h/352012_challenge_18_easy/

#converts the letter into a number
def letter_to_number(word):
    number = ""
    for letter in word:
        if letter == "a" or letter == "b" or letter == "c":
            number += "2"
        if letter == "d" or letter == "e" or letter == "f":
            number += "3"
        if letter == "g" or letter == "h" or letter == "i":
            number += "4"
        if letter == "j" or letter == "k" or letter == "l":
            number += "5"
        if letter == "m" or letter == "n" or letter == "o":
            number += "6"
        if letter == "p" or letter == "q" or letter == "r" or letter == "s":
            number += "7"
        if letter == "t" or letter == "u" or letter == "v":
            number += "8"
        if letter == "w" or letter == "x" or letter == "y" or letter == "z":
            number += "9"
    return number

#checks if it's a word
def check_word(word):
    if len(word) == 7:
        print str(word) + " is a valid word!"
        return True
    else:
        print "Error. Please press enter to exit."
        return False

#this prints out the telephone number
def telephone_number(word):
    full_number = ""
    if check_word(word) is True:
        word = letter_to_number(word)
        full_number = "1-800-" + word[0:3] + "-" + word[3:7]
    return full_number


word_input = raw_input("Please input a word! ").lower()
print telephone_number(word_input)
raw_input()


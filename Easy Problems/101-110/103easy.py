#https://www.reddit.com/r/dailyprogrammer/comments/11erhd/10132012_challenge_103_easydifficult_text/
#https://cleanspeak.com/blog/2014/05/28/leet-speak-filtering-methods
#uses https://cleanspeak.com/images/blog/leet-wiki-table.png
#as reference for the table

#Random library is to pick randomly from the dictionary
#String is for importing the full string
import random
import string

def l33t_cre4tor(string_input):
    leet_dictionary_choices = {
    'A': ["4", "@", "/-\ ", "/\ ", "^"],
    'B': ["8", "|3", "6", "13", "|3"],
    'C': ["(", "<", "{"],
    'D': ["|)", "[)", "])", "I>", "|>", "0"],
    'E': ["3", "^", "[="],
    'F': ["|=", "]=", "}", "(="],
    'G': ["6", "9", "&", "(_+", "C-", "(Y,"],
    'H': ["|-|", "#", "]-[", "[-]", ")-(", "(-)", ":-:", "}{", "}-{"],
    'I': ["!", "1", "}"],
    'J': ["_|", "_/", "]", "</", "_)"],
    'K': ["X", "|<", "|X", "|{"],
    'L': ["1", "7", "|_", "|", "|_", "|_"],
    'M': ["44", "/\/\ ", "|\/|", "|v|", "IYI", "IVI", "[V]", "^^", "//\\//\\ ", "(V)",
        "(\/)", "/|\ ", "/|/|", ".\\", "/^^\ ", "/V\ ", "|^^"],
    'N': ["|\|", "/\/", "//\\// ", "[\]", "<\>", "//", "[]\[]", "]\[", "~"],
    'O': ["0", "()", "[]"],
    'P': ["|*", "|o", "|>", """|" """, "?", "9", "[]D", "|7", "q", "|D"],
    'Q': ["0_", "0,", "(,)", "<|", "9"],
    'R': ["|2", "2", "/2", "I2", "|^", "|~", "|2", "[z", "|`", ".-"],
    'S': ["5", "$", "z"],
    'T': ["7", "+", "-|-", "1", "']['"],
    'U': ["|_|", "(_)", "Y3W", "M", "[_]", "\_/", "\_\ ", "/_/ "],
    'V': ["\/", "\\//"],
    'W': ["\/\/", "vv", "'//", "\\'", "\^/", "(n)", "\X/", "\|/", "\_|_/", "\\//\\//", "\_:_/", "]I[", "UU", "JL"],
    'X': ["><", "}{", "*", ")(", "ecks"],
    'Y': ["j", "`/", "`(", "_/"],
    'Z': ["2", "3", "~/_", "7_", "%"]
    }
    letters = string.ascii_uppercase
    
    #takes one from every letter in the dictionary
    leet_dictionary = {letter:random.choice(leet_dictionary_choices[letter]) for letter in string.ascii_uppercase}
    l33t_str = ''
    for c in string_input:
        if c.isalpha():
          temp = c.upper()
          l33t_str += leet_dictionary[temp]
        else:
            l33t_str += c
    
    return string_input, l33t_str

#this program takes one input, a string, and returns it and the 'l33t' version

leet = raw_input("Put in your string to convert to l33t text:").lower()
print("\n~*~----------------~*~\n")
print(l33t_cre4tor(leet))
print("\n~*~----------------~*~\n")
raw_input("\nPress enter to exit.")

#test cases
#print(l33t_cre4tor('LEET SPEAK'))

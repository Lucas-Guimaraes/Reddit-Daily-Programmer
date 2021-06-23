# https://www.reddit.com/r/dailyprogrammer/comments/1pwl73/11413_challenge_139_easy_pangrams/
#string library used to import library, re used to make replacing easier
import string
import re

def pangram(put):
    #Prepares dictionary
    letter_dict = {k: 0 for k in string.ascii_lowercase}
    
    #Makes input all lowercased, followed by replacing non-lowercased letters
    put = put.lower()
    put = re.sub("[^a-z]+", "", put)
    
    #Returns our input
    if set(string.ascii_lowercase) == set(put):
        for key in letter_dict:
            letter_dict[key] = put.count(key)
        return True, letter_dict
    else:
        return False

#Loops until user quits
pan = True
while pan:
    pan_str = raw_input("Check your pangram here: ")
    if pan_str == "q" or pan_str == "Q":
        break
    print(pangram(pan_str))

raw_input("Press enter to exit.")
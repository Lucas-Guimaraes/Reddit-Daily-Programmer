# https://www.reddit.com/r/dailyprogrammer/comments/12k3xr/1132012_challenge_110_easy_keyboard_shift/

def keyboard_shift(text):
    shifted = ''
    goodkey = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    badkey = 'wertyuiop[sdfghjkl;xcvbnm,WERTYUIOP{SDFGHJKL:XCVBNM<'
    #If the letter exists in bad key
    #it will take the index from bad key and put that on good key
    #Otherwise, just add the same letter back
    for letter in text:
        if letter in badkey:
            shifted += goodkey[badkey.index(letter)]
        else:
            shifted += letter

    return shifted

print("This program will shift your string by a letter k. 'q' will quit the program.")
print("\n~*~----------------~*~\n")

#Checks input
shifty_string = True
while shifty_string:
    shift_text = raw_input("Give me a string: ")
    if shift_text == 'q' or shift_text == 'Q':
        shifty_string = False
        break
        
    print(keyboard_shift(shift_text))


raw_input("Press enter to exit.")


raw_input()
#test cases:
#print(keyboard_shift('Lmiyj od ,u jrtp'))

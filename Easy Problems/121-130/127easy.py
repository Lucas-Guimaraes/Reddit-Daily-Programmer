#https://www.reddit.com/r/dailyprogrammer/comments/1g0tw1/easy_longest_twocharacter_substring/

def two_char_substr(w):
    result = ''
    #This loops over the amount of letters in
    for c in range(len(w)):
        substring = ''
        #This checks every single letter from the beginning of the letter on to the point
        for letter in w[c:]:
            if letter not in substring and len(set(substring)) == 2:
                break
            else:
                substring += letter
        if len(substring) > len(result):
            result = substring
    return result


two_char = True
while two_char:
    str_input = raw_input("Give me a number. Press 'Q' or 'q' to quit: ")
    
    if str_input == 'q' or str_input == 'Q':
        two_char = False
        break
        
    print(two_char_substr(str_input))

raw_input("Press enter to exit.")

#Test cases:
#print(two_char_substr('tyytr'))
#print(two_char_substr('abbccc'))
#print(two_char_substr('abcabcabcabccc'))
#print(two_char_substr('qwertyytrewq'))
# https://www.reddit.com/r/dailyprogrammer/comments/101m7y/9172012_challenge_99_easy_words_with_letters_in/
#'99easytest.txt' is a supplementary file

import string

def alphabetical_words(file):
    count = 0
    alphabet = string.ascii_lowercase
    with open(file) as f:
        big_file = [line.rstrip() for line in f]
    
    #Will check if word is alphabetical
    for line in big_file:
        
        last_letter = ''
        line_str = str(line).lower()
        for i in range(len(line_str)):
            
            
            if last_letter == '':
                last_letter = line_str[i]
                continue
            
            ascii_idx = alphabet.index(line_str[i])
            ascii_idx = alphabet[ascii_idx+1:]

            #Breaks the loop
            if last_letter in ascii_idx:
                break
            else:
                last_letter = line[i]
            
            #adds the count
            if len(line)-1 == i:
                count += 1
    #Returns the count
    return count


op = '99easytest.txt'
print(alphabetical_words(op))
raw_input()
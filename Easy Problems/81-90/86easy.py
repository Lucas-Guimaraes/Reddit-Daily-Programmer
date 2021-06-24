#https://www.reddit.com/r/dailyprogrammer/comments/xxbbo/882012_challenge_86_easy_runlength_encoding/

#Length encoding function
def length_encoding(before):
    last_letter = ''
    encode = []
    
    
    for letter in before:
        #If in alphabet
        if letter.isalpha():
            #We unique
            if letter != last_letter:
                lst = [letter, 1]
                encode.append(lst)
            #If the same as last letter
            else:
                encode[-1][1] += 1
        #If not in alphabet
        else:
            continue
        #assigning last letter
        last_letter = letter
    return encode

#Input
print("Welcome to string encoder!")
print("This program will take a string you write and encode it")
print("\n~*~--------~*~\n")
stringing = True
while stringing:
    str_put = raw_input()
    if str_put == 'q' or str_put == 'Q':
        break
    print(length_encoding(str_put))
    
raw_input("Press enter to exit.")
    
       
#Test case
#print(length_encoding("Heeeeelllllooooo nurse!"))
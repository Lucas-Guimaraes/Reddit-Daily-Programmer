# https://www.reddit.com/r/dailyprogrammer/comments/299hvt/6272014_challenge_168_easy_string_index/

#this function handles the index
def str_index(word, index):
    new = word.replace(".", " ")
    str_split = new.split()

    str_split_final = []
    
    #This checks whether the word is, well, a word and not just a blank space
    for i in str_split:
        new_word = ''
        for x in i:
            if x.isalpha():
                new_word += x
        if new_word != ' ' and new_word != '':
            str_split_final.append(new_word)
    
    #tries to return it. If the index does not work, it will return as 1.
    if index > -1:
        try:
            return str_split_final[index-1]
        except:
            return None
    else:
        try:
            return str_split_final[index]
        except:
            return None

#Introduces the program
print("Welcome to word index!")
print("Put in a sentence, and then its Index")
print("The index count starts from 1, *not* 0.")
print("\n~*~----------------~*~\n")

working_index = True

#Loop that keeps the program go until the user quits
while working_index:
    s = raw_input("Give a sentence: ")
    i = raw_input("Give an idx: ")
    if i == 'q' or i == 'Q' or s == 'q' or s == 'Q':
        break
    if i.isdigit():
        print(str_index(s, int(i)))

raw_input("\nPress enter to exit.")
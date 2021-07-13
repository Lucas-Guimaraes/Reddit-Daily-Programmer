# https://www.reddit.com/r/dailyprogrammer/comments/98ufvz/20180820_challenge_366_easy_word_funnel_1/
#366easy.txt is a supplementary file to this program

word_lst = []
f = open("366easy.txt", "r")

# prepares our date list
for line in f.readlines():
    word = line.replace("\n", "")
    word_lst.append(word)


# Does the regular word funnel
def funnel(word, word2):
    for i in range(len(word)):
        # Checks where on the index
        if i == 0:
            temp_word = word[1:]
        elif i == len(word):
            temp_word = word[:len(word)]
        else:
            temp_word = word[:i] + word[i + 1:]

        # Checks if it is equal to Word 2
        if temp_word == word2:
            return True

    return False


def bonus(word):

    #Adds every letter removed
    w_lst = []
    for i in range(len(word)):
        if i == 0:
            temp_word = word[1:]
        elif i == len(word):
            temp_word = word[:len(word)]
        else:
            temp_word = word[:i] + word[i + 1:]
        
        w_lst.append(temp_word)
    
    #Checks if the word is in the word list
    new_lst = []
    for i in w_lst:
        if i in word_lst:
            new_lst.append(i)
    new_lst = list(set(new_lst))
    return new_lst

#test cases
print(funnel("leave", "eave"))
print(funnel("reset", "rest"))
print(funnel("dragoon", "dragon"))
print(funnel("eave", "leave"))
print(funnel("sleet", "lets"))
print(funnel("skiff", "ski"))
print(bonus('dragoon'))
print(bonus('boats'))
print(bonus('affidavit'))
raw_input("Press enter to exit")
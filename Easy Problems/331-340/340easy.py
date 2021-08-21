#https://www.reddit.com/r/dailyprogrammer/comments/7cnqtw/20171113_challenge_340_easy_first_recurring/

def first_recur(word):
    lst = []
    for w in range(len(word)):
        if word[w] in lst:
            return word[w], word.find(word[w])+1
        else:
            lst.append(word[w])
    return "There are no recursive characters in {}".format(word)
# Intro text
print("Welcome to first recur!")
print("Input a string. The output will be the first character that appears twice")
print("The second number will be the first index it appears")
print("This program uses 1-index system")
print("So the first B in 'ABBA' would return as 2, the second character.")
print("\n~*~----------------~*~\n")

#Run text
recurring = True
while recurring:
    w = raw_input()
    if w.lower() == 'q':
        break
    print(first_recur(w))


raw_input("Press enter to exit")

#test case
#print(first_recur('ABCDEBC'))
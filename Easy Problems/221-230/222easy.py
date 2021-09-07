#https://www.reddit.com/r/dailyprogrammer/comments/3c9a9h/20150706_challenge_222_easy_balancing_words/

#Balance the word
def balance_word(word):
    #String for index
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #loops every letter that is not first or last
    for i in range(1, len(word)-1):
        #Extracts the split points
        first_w = word[:i]
        second_w = word[i+1:]
        first_s = 0
        second_s = 0
        #Grabs score for the left side
        for f in range(len(first_w)):
            first_s += (alpha.find(first_w[f])+1) * (len(first_w) - f)
        #Grabs score for the right side
        for s in range(len(second_w)):
            second_s += (alpha.find(second_w[s])+1) * (s+1)
        #If equal, return
        if first_s == second_s:
            return first_w + " " + word[i] + " " + second_w + " - " + str(first_s)

    #If not equal
    return "{} does not balance".format(word)

#Intro
print("Welcome to Balance Word")
print("Give a word, check if it is balanced")
print("\n~*~----------------~*~\n")

#Run code
b = True
while b:
    w = raw_input().upper()
    if w == 'Q':
        break
    print(balance_word(w))

print("Press enter to exit")

#test case
#print(balance_word("STEAD"))
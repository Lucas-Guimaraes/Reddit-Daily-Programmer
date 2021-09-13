# https://www.reddit.com/r/dailyprogrammer/comments/2ptrmp/20141219_challenge_193_easy_acronym_expander/

#acronyms used
acronym_dic = {'lol': 'laugh out loud',
               'dw': "don't worry",
               'hf': "have fun",
               "gg": "good game",
               "brb": "be right back",
               "g2g": "got to go",
               "wtf": "what the fuck",
               "wp": "well played",
               "gl": "good luck",
               "imo": "in my opinion"}


#expand
def a_expand(sen):
    sen = sen.split()
    new_sen = []

    for word in sen:
        # Handles in the case the word has any additions. i.e. "wp."
        temp = ''
        cur = ''

        if word.isalnum() != True:
            temp = ''.join(ch for ch in word if ch.isalnum() == False)
            if temp == word[0]:
               cur = 'before'
            elif temp == word[-1]:
                cur = 'after'

            word = ''.join(ch for ch in word if ch.isalnum())

        #If cur is before, adds sign.
        #If word is in keys, add. If not, append. if cur is after, adds
        if cur == 'before':
            new_sen.append(temp)
        if word in acronym_dic.keys():
            new_sen.append(acronym_dic[word])
        else:
            new_sen.append(word)
        if cur == 'after':
            new_sen.append(temp)
    new_sen = " ".join(new_sen)

    return new_sen


print("Welcome to Acronym Expander!")
print("Give a sentence, expand the acronym's.")
print("\n~*~--------~*~\n")

expanding = True
while expanding:
    w = raw_input()
    if w.lower() == 'q':
        break
    print(a_expand(w))

raw_input("Press enter to exit.")

# test cases
# print(a_expand("wtf that was unfair"))
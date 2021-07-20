#https://www.reddit.com/r/dailyprogrammer/comments/6grwny/20170612_challenge_319_easy_condensing_sentences/

def condense(sentence):
    #Splits the string, makes list and previous word
    sentence = sentence.split()
    prev_w, lst = sentence[0], [sentence[0]]

    #Goes over the rest of the words
    for cur_w in sentence[1:]:
        lowest_len = min(len(prev_w), len(cur_w))
        check = True
        for i in range(lowest_len, 0, -1):
            if prev_w.endswith(cur_w[:i]):
                new_word = prev_w + cur_w[i:]

                check = False

        #Make current word the last one, append the cur to the list
        if check:
            prev_w = cur_w
            lst.append(cur_w)
        #the modified word becomes the previous, pop the last one, append the new one
        #Works this way so multiple condensings can be done (3 or more words)
        else:
            prev_w = new_word
            lst.pop()
            lst.append(new_word)

    condensed_sentence = " ".join(lst)
    return condensed_sentence

#Introduction text
print("Welcome to Sentence Condenser")
print("Input a sentence; output any extra letters")
print("Note: This program may not make coherent sense.")
print("\n~*~----------------~*~\n")

# Sentence input, quit case included

condensing = True
while condensing:
    words = raw_input("")
    if words.lower() == 'q':
        break

    print(condense(words))

raw_input("Press enter to exit.")

#Test cases:
#print(condense('I heard the pastor sing live verses easily.'))
#print(condense('Digital alarm clocks scare area children.'))
#print(condense('Deep episodes of Deep Space Nine came on the television only after the news.'))
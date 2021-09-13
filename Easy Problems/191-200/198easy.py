#https://www.reddit.com/r/dailyprogrammer/comments/2syz7y/20150119_challenge_198_easy_words_with_enemies/

def words_enemies(word_1, word_2):
    score_1, score_2, temp_2 = len(word_1), len(word_2), word_2
    for i in range(len(word_1)):
        if word_1[i] in temp_2:
            j = temp_2.find(word_1[i])
            temp_2 = letter_removal(word_2, j)
            score_1 -= 1
            score_2 -= 1
    if score_1 > score_2:
        return "{} defeats {}!".format(word_1, word_2)
    elif score_2 < score_1:
        return "{} defeats {}!".format(word_2, word_1)
    else:
        return "Both {} and {} have equal scores!".format(word_1, word_2)

def letter_removal(word, idx):
    if idx == 0:
        return word[1:]
    elif idx == len(word):
        return word[:idx]
    else:
        return word[:idx] + word[idx+1:]

print("Welcome to Words With Enemies!")
print("This will take your input, two words, and produce an output, the winner")
print("\n~*~--------~*~\n")

cannon = True
while cannon:
    w = raw_input("")
    if w == 'Q' or w == 'q':
        break
    w = w.split()
    print(words_enemies(w[0].lower(), w[1].lower()))

raw_input("Press enter to exit")

#Test Cases
#print(words_enemies("hello", "yeah"))
#print(words_enemies("hat", "cat"))
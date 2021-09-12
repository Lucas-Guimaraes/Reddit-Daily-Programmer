# https://www.reddit.com/r/dailyprogrammer/comments/5hy8sm/20161212_challenge_295_easy_letter_by_letter/

def trial_by_letter(sentence, goal):
    if len(sentence) != len(goal):
        print("Invalid input. Please try again.")
        return

    new_str = ""
    print(sentence)
    for i in range(len(sentence)):
        if sentence[i] == goal[i]:
            new_str += sentence[i]
            continue
        else:
            new_str = new_str + goal[i]
            print(new_str + sentence[i+1:])


print("Welcome to letter by letter")
print("This program will take two inputs: Two words")
print("Afterwards, it will change every letter. Letter. by. Letter")
print("\n~*~--------~*~\n")

sentence = True

while sentence:
    sen = raw_input()
    sen_2 = raw_input()
    if sen.lower() == 'q' or sen_2.lower() == 'q':
        break

    trial_by_letter(sen, sen_2)

raw_input("Press enter to exit.")
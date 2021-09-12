# https://www.reddit.com/r/dailyprogrammer/comments/5go843/20161205_challenge_294_easy_rack_management_1/

def scrabble(word, goal):
    total = 0
    total_goal = len(goal)
    for i in range(len(word)):
        if word[i] in goal:
            total += 1
            goal.replace(word[i], '', 1)
        if word[i] == '?':
           total += 1
    return total >= total_goal


print("Welcome to scrabble")
print("This program will take two inputs: Your bag, and the goal word")
print("It will then tell you if you can form that word")
print("\n~*~--------~*~\n")

sentence = True

while sentence:
    sen = raw_input()
    sen_2 = raw_input()
    if sen.lower() == 'q' or sen_2.lower() == 'q':
        break
    print(scrabble(sen, sen_2))

raw_input("Press enter to exit.")
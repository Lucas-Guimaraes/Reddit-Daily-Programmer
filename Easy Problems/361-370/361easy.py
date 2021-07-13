# https://www.reddit.com/r/dailyprogrammer/comments/8jcffg/20180514_challenge_361_easy_tally_program/

def tally(players, score):
    scorecard = {}
    for i in players:
        scorecard[i] = 0
    for i in score:
        if i.isupper():
            scorecard[i.lower()] -= 1
        else:
            scorecard[i] += 1

    sort_score = sorted(scorecard.items(), key=lambda x: x[1])
    sort_score = sort_score[::-1]
    return sort_score

print("Welcome to scorecard")
print("Example input (two inputs):")
print("abcde")
print("dbbaCEDbdAacCEAadcB")
print("Example output:")
print("[('d', 2), ('b', 2), ('a', 1), ('c', 0), ('e', -2)]")
print("\n~*~----------------~*~\n")

scoring = True

while scoring:
    players = raw_input("Players").lower()
    score = raw_input("Score")
    if players == 'q' or score == 'q'::
        break
    print(tally(players, score))
    
raw_input("Press enter to exit.")

#Test cases:
#print(tally('abcde', 'dbbaCEDbdAacCEAadcB'))
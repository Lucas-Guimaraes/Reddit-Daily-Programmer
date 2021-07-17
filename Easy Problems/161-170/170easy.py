# https://www.reddit.com/r/dailyprogrammer/comments/29zut0/772014_challenge_170_easy_blackjack_checker/

#Gives a score for each word
score_check = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
               'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}

#Returns the name, score, and trick (amt of cards)
def count_blackjack(lst):
    name, cards = lst.split(':')
    cards = ''.join(cards).lower()
    cards = cards.split(', ')
    trick = len(cards)
    score = 0
    for x in cards:
        temp = x.split()

        score += score_check[temp[0]]
    return name, score, trick


print("Welcome to Blackjack Checker!")
print("For the first line of input, insert how many players you will have")
print("Next you will insert a name, and the count")
print("\n~*~----------------~*~\n")

#Runs program
checking = True
while checking:
    n = raw_input()
    
    #quit code
    if n == 'q' or n == 'Q':
        break
    
    #checks if digit
    if n.isdigit():
        scorecard = []
        
        #for every line, gets the name, score, and trick
        for i in range((int(n))):
            name, score, trick = count_blackjack(raw_input())
            scorecard.append((name, score))
            
        #sort
        scorecard.sort(key=lambda x: x[1])
        scorecard = reversed(scorecard)

        #prints the winner; accounts for trick
        for x in scorecard:
            if 21 >= x[1] and trick == 5:
                print("{} has won with a 5-card trick!".format(x[0]))
                break
            elif 21 >= x[1]:
                print("{} has won!".format(x[0]))
                break

raw_input("Press enter to exit.")
#https://www.reddit.com/r/dailyprogrammer/comments/dv0231/20191111_challenge_381_easy_yahtzee_upper_section/

def yahtzee_upper(rolls):
    rolls_lst = rolls.split()
    rolls_lst = [int(r) for r in rolls_lst]
    score_lst = [rolls_lst.count(i) * i for i in range(1, 7)]
    return max(score_lst)

print("Welcome to Yahtzee Upper Score!")
print("This will take a list of five numbers and count the upper score")
print("Just input your list like this:")
print("1 1 3 2 5")
print("How yahtzee scoring works is like this:")
print("Take the above input: There are two 1's. 2 (number of 2's) * 1 = 2")
print("1 * 3 (number of 1's times the number) is 3")
print("1 * 2 is 2")
print("1 * 5 is 5")
print("So the highest attainable score is 5")
print("\n~*~----------------~*~\n")
yahtzee = True
while yahtzee:
    yahtzee_rolls = raw_input("Please put in your input and press enter. Give me no input: ")
    if yahtzee_rolls == 'q':
        print("Goodbye.")
        yahtzee = False
    print(yahtzee_upper(yahtzee_rolls))
raw_input("\nPress Enter to exit.")
#print(yahtzee_upper('2 3 5 5 6'))
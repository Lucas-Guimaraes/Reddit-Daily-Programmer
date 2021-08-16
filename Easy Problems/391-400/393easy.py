# https://www.reddit.com/r/dailyprogrammer/comments/nucsik/20210607_challenge_393_easy_making_change/
# Function
def examplania(n):
    coins = 0
    amt = [500, 100, 25, 10, 5, 1]
    #For every change, divide by the current change; add the coins
    #Take the amount of coins (cur) and multiply by the amount, to get the amount of money left
    for a in amt:
        cur = n / a
        coins += cur
        n -= cur * a
    return coins

# Intro
print("Welcome to Examplania!")
print("Put in a number, get your change")
print("\n~*~----------------~*~\n")

counting = True

# Input
while counting:
    n = raw_input("Put in your number: ")
    if n == 'q':
        break
    if n.isdigit():
        print(examplania(int(n)))

# Exit
raw_input("Press enter to exit.")
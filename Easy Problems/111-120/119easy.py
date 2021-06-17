#https://www.reddit.com/r/dailyprogrammer/comments/17f3y2/012813_challenge_119_easy_change_calculator/
from decimal import *

def spare_change(dollars):
    coins = {"Quarters": 0,
     "Dimes": 0,
     "Nickels": 0,
     "Pennies": 0}
    coins_worth = {"Quarters": 25,
     "Dimes": 10,
     "Nickels": 5,
     "Pennies": 1}


    for type, coin in reversed(coins_worth.items()):
        dollars = dollars * 100

        coin_count = dollars / coin

        remainder = (dollars % coin) / 100
        change = coin_count - remainder
        coins[type] = change
        dollars = remainder

    for key, value in reversed(coins.items()):
        print(key + ': ' + str(int(value)))

def check_quarters(test):
    test = test * 100
    og = test / 25
    remainder = test % 25
    print(remainder)
    new_coin = og - remainder
    print(new_coin)

print("Welcome to change converter!")
no_float = True
while no_float:
    num = raw_input("\nPlease put in a valid float: \n")
    try:
        num = float(num)
        no_float = False
    except:
        continue
print("\n~*~----------------~*~\n")
spare_change(num)
print("\n~*~----------------~*~\n")

raw_input("Press enter to exit.")

#test cases
#spare_change(00.06)

#https://www.reddit.com/r/dailyprogrammer/comments/19mn2d/030413_challenge_121_easy_bytelandian_exchange_1/

import math


def coin_counter(n):
    values = [n]
    while set(values) != set([0]):
        for value in values:
            if value > 0:
                values.remove(value)
                values.append(int(math.floor(value/2)))
                values.append(int(math.floor(value/3)))
                values.append(int(math.floor(value/4)))

    return len(values)


print("Please put in the amount of coins you put in the machine")
print("The output will be how many 0 valued coins come out")
print("Example: If you put in 100, it will first divide 100 by 2, then by 3, then by 4.")
print("This will be done over and over again until every coin is below 1")

print("\n~*~----------------~*~\n")

#Checks input
coin_count = True
while coin_count:
    num_coins = raw_input("Give me a number. Press 'Q' or 'q' to quit: ")
    if num_coins == 'q' or num_coins == 'Q':
        coin_count = False
        break
    if num_coins.isdigit():
        print(coin_counter(int(num_coins)))


raw_input("Press enter to exit.")

#test cases
#print(coin_counter(1000))
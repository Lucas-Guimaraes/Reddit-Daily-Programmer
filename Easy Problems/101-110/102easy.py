#https://www.reddit.com/r/dailyprogrammer/comments/10pf0j/9302012_challenge_102_easy_dice_roller/

import random
import string

def dice_roller(dice):
    dice = dice.split('d')
    sides = 0
    total = 0
    
    #How many rolls are included
    if dice[0] == '':
        rolls = 1
    else:
        rolls = int(dice[0])

    #The + and - are if it has said dice - calculates from the total early
    if '+' in dice[1]:
        split_die = dice[1].split('+')
        total += int(split_die[1])
        sides = int(split_die[0])
    elif '-' in dice[1]:
        split_die = dice[1].split('-')
        total -= int(split_die[1])
        sides = int(split_die[0])
    else:
        sides = int(dice[1])
        
    #rolls for every time
    for i in range(rolls):
        total += random.randrange(1, sides)

    return total

#This text is to explain to the user
print("This program is used for rolling dice")
print("Valid inputs include the following:")
print("1d8+0")
print("d8")
print("d8+0")
print("d8-0")
print("All of these mean the same thing.")
print("The digit before 'd' is how many dice")
print("The digit after the d is how many sides")
print("The + or - one is the number that is equal after the total roll\n")

print(dice_roller(raw_input("Give me a die to roll: \n")))

raw_input("\nPress enter to exit.")

#test case:
#print(dice_roller('10d6-2'))
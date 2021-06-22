# https://www.reddit.com/r/dailyprogrammer/comments/1givnn/061713_challenge_130_easy_roll_the_dies/

import random

def roll_the_dies(ndm):
    
    #This first splits the 'd' into two numbers'. How many die, and then the sides
    roll_list = ndm.split('d')
    roll_amt = int(roll_list[0])
    sides = int(roll_list[1])
    results = []
    
    #this rolls for every die (roll_amt)
    #the (sides) will be the amount of sides
    #If it is 6, each die will roll from '1 to 6'
    
    for i in range(roll_amt):
        results.append(random.randrange(1, sides))
    results = "".join(str(results))
    results = results.replace("[", "").replace("]", "")
    return results


print(roll_the_dies('2d20'))
print(roll_the_dies('4d6'))
raw_input()
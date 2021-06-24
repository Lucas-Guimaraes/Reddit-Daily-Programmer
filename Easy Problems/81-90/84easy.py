#https://www.reddit.com/r/dailyprogrammer/comments/xilfu/812012_challenge_84_easy_searching_text_adventure/
import random

#Starts the game
def searching_text():
    print("Hello! Welcome to searching text adventure")
    print("You will have the option of inputting a key")
    print("There are some collectables along the way, but your goal is to get closer to the distance")
    print("Good luck!")
    print("*--------*")
    
    
    dx = dice()
    dy = dice()
    xmapx = dice()
    xmapy = dice()
    ymapx = dice()
    ymapy = dice()
    easter_egg_1x = dice()
    easter_egg_1y = dice()
    easter_egg_2x = dice(100)
    easter_egg_2y = dice(100)


    not_found = True
    x_map = False
    y_map = False
    easter_egg_1 = False
    easter_egg_2 = False

    x_locale = (xmapx ** 2 + xmapy ** 2) ** .5
    y_locale = (ymapx ** 2 + ymapy ** 2) ** .5
    easter_egg_l1 = (easter_egg_1x ** 2 + easter_egg_1y ** 2) ** .5
    easter_egg_l2 = (easter_egg_2x ** 2 + easter_egg_2y ** 2) ** .5
    items_found = 0
    
    #Prints out all code properly
    while not_found:
        print(x_locale, y_locale, easter_egg_l1, easter_egg_l2)
        distance = (dx ** 2 + dy ** 2) ** .5
        
        #Handles all the items found
        if (distance < 1):
            print("You found the treasure!\n")
            if any([x_map, y_map, easter_egg_1, easter_egg_2]):
                print("You also found the following items:")
                if x_map:
                    print("X Map")
                    items_found += 1
                if y_map:
                    print("Y Map")
                    items_found += 1
                if easter_egg_1:
                    print("A nice message!")
                    items_found += 1
                if easter_egg_2:
                    print("A Safe Box!")
                    items_found += 1
                print("That's a grand total of {} items!").format(items_found)
                if items_found == 4:
                    print("Congratulations! You've found all the items.")
                else:
                    print("You missed {} item(s)").format(4 - items_found)
            else:
                print("You found no extra items! Maybe replay?")
            not_found = False
            continue

        #Checks if items are found or will be found
        if x_map is False:
            if distance < x_locale+.5 and distance > x_locale-.5:
                print('hi')
                print("Congratulations! You've found the map for X.")
                x_map = True
        else:
            print("The location of X is {}".format(dx))

        if y_map is False:
            if distance < y_locale+.5 and distance > y_locale-.5:
                print("Congratulations! You've found the map for Y.")
                y_map = True
        else:
            print("The location of Y is {}".format(dy))

        if easter_egg_1 is False:
            if distance < easter_egg_l1+.5 and distance > easter_egg_l1-.5:
                print("You've found a nice message! Treasure it.")
                easter_egg_1 = True

        if easter_egg_2 is False:
            if distance < easter_egg_l2+.5 and distance > easter_egg_l2-.5:
                print("Woah! You've found a safe box. Too bad there's no keys on this island.")
                easter_egg_2 = True

        s = "Distance: " + str(distance) + "\nWhich direction? (n, e, w, s)\n>"
        dir = raw_input(s)
        if (dir == "n"):
            dx -= 1
        if (dir == "e"):
            dy -= 1
        if (dir == "w"):
            dy += 1
        if (dir == "s"):
            dx += 1

#Rolls a dice
def dice(roll=10):
    return random.randint(-roll, roll)

#Checks if the user wants to replay
searching_text()
replay = True
while replay:
    answer = raw_input("Would you like to replay? Type 'yes' or 'replay' to replay. If not, I will close.")
    if answer == 'replay' or answer == 'yes':
        searching_text()
    else:
        print('Goodbye')
        replay = False
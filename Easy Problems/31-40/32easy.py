#https://www.reddit.com/r/dailyprogrammer/comments/rhrmx/3282012_challenge_32_easy/
#https://www.casinonewsdaily.com/roulette-guide/american-roulette/
#I did this better in a later one - this one was supreme headaches at first

#import for random and suspense
import random
import time
#making a roulette list that contains '00'
print("Welcome to bet generator!\n")
bet = int(raw_input("How much would you like to wager?\n\n"))

#checks color
color_check = True
color_list = ['black', 'red']

while color_check:
    color = raw_input("\nPlease put in a color. 'Red' and 'Black' are the only valid options:\n\n")
    color = color.lower()
    if color in color_list:
        color_check = False

print('\nYou bet {bet} dollars on {color}\n'.format(bet = bet, color = color.title()))
print("The wheel is spinning...\n")
spin = random.randrange(0,37)


time.sleep(1)

if spin == 0 or spin == 37:
    if spin == 0:
        spin_str = '0'
    else:
        spin_str = '00'
    print("The ball stopped on {spin} Green\n").format(spin = spin_str)
    
    print("You won " + str(int(bet)*100) + "!")
else:
    print ("The ball stopped on {spin} {color}\n".format(spin = spin, color = color_list[spin%2].title()))
    if color_list[spin%2] == color:
        print "You won " + str(int(bet)*2) + "!"
    else:
        print "You lost {bet} on your wager!".format(bet = bet)


raw_input()

#roulette_list = ['00']
#roulette_list += [str(x) for x in range(0,37)]
# I'm trying to find the word in python
#v i failed to understand how betting works
# while bet_check:
    # betting_number = raw_input("Please put in a betting number.\n\nValid numbers are 00, 0, and anything in the range of 1-36\n\n")
    # if betting_number in roulette_list:
        # bet_check = False
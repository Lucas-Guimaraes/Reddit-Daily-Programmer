#https://www.reddit.com/r/dailyprogrammer/comments/43ouxy/20160201_challenge_252_easy_sailors_and_monkeys/czm4om9/

#Finds out the amount of coconuts the sailor crew has
def coconuts(sailors):
        #If only 2 sailors
        if sailors == 2:
            return 11
        #If sailors are odd
        elif sailors % 2 == 1:
            return sailors**sailors - sailors + 1
        #If even
        else:
            return (sailors-1) * (sailors**sailors - 1)

print("Welcome to monkeys and coconuts!")
print("Throw in an input, an integer")
print("And find out how many coconuts are in the pile!")

print("\n~*~----------------~*~\n")

#Program loop.
stranded = True
while stranded:
    crew = raw_input()
    #Checks if input is digit.
    if crew.isdigit():
        print(coconuts(int(crew))
    #Quit option
    if crew == 'q' or crew == 'Q':
        break

raw_input("Press enter to exit.")
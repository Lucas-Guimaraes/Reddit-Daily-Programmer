#https://www.reddit.com/r/dailyprogrammer/comments/4nvrnx/20160613_challenge_271_easy_critical_hit/

#Checks for critical hit
def critical_hit(die, hp):
    #If it is possible with one roll, we roll that roll.
    #If not, we run the program until we get how many rolls it would take
    if hp <= die:
        return (die + 1 - hp) / die
    else:
        return critical_hit(die, hp - die) / die

#Explination
print("Welcome to critical hit")
print("Put in two digits: die and hp")
print("4 1")
print("\n~*~----------------~*~\n")

#Checks input, quit case included
critical = True
while critical:
    die = raw_input()
    if die.islower() == 'q':
        break
    die = die.split()
    if die[0].isdigit() and die[1].isdigit():
        print(critical_hit(float(die[0]), float(die[1])))

#test case
#print(critical_hit(float(4), float(1)))
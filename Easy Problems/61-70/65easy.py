# https://www.reddit.com/r/dailyprogrammer/comments/v3a89/6152012_challenge_65_easy/
from math import floor

#does all our change
def change_exchange(money):
    change = [0 for i in range(9)]
    money_dict = {'hundred': 100,
                  'fifty': 50,
                  'ten': 10,
                  'five': 5,
                  'dollar': 1,
                  'quarter': .25,
                  'dime': .10,
                  'nickel': .05,
                  'penny': .01, }

    if floor(money / money_dict['hundred']) > 0:
        change[0] = int(floor(money / money_dict['hundred']))
        money = money % money_dict['hundred']

    if floor(money / money_dict['fifty']) > 0:
        change[1] = int(floor(money / money_dict['fifty']))
        money = money % money_dict['fifty']

    if floor(money / money_dict['ten']) > 0:
        change[2] = int(floor(money / money_dict['ten']))
        money = money % money_dict['ten']

    if floor(money / money_dict['five']) > 0:
        change[3] = int(floor(money / money_dict['five']))
        money = money % money_dict['five']

    if floor(money / money_dict['dollar']) > 0:
        change[4] = int(floor(money / money_dict['dollar']))
        money = money % money_dict['dollar']

    if floor(money / money_dict['quarter']) > 0:
        change[5] = int(floor(money / money_dict['quarter']))
        money = money % money_dict['quarter']

    if floor(money / money_dict['dime']) > 0:
        change[6] = int(floor(money / money_dict['dime']))
        money = money % money_dict['dime']

    if floor(money / money_dict['nickel']) > 0:
        change[7] = int(floor(money / money_dict['nickel']))
        money = money % money_dict['nickel']

    if floor(money / money_dict['penny']) > 0:
        change[8] = int(money * 100)

    return change

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
print("Welcome to change exchange!")
print("This program will take in one input: A float")
print("It iwll output how many hundred dollar bills it can be transformed into")
print("Followed by fifties, tens, fives, dollars, quarters, dimes, nickels, and finally pennies")
print("Awesome, right?")

print("\nExample input:")
print("12.33")

print("\nExample logic:")
print("We can fit a ten in. That's a '1' for 10.  2.33.")
print("We can fit two dollars, so we make that 33 cents and a '2' for 1 dollar")
print("We can fit a quarter into .33, so .8")
print("1 Nickel, 3 Pennies")
print("To recap, '1' ten bill, '2' dollars, '1' quarter, '1' nickel, and '3' pennies")

print("\nExample output:")
print("[0, 0, 1, 0, 2, 1, 0, 1, 3]")
print("The four 0's are there to represent the currencies that weren't able to be used")

print("\n~*~----------------~*~\n")

changing = True
#this checks if the program is still running
while changing:
    change = raw_input("Please input your float. 'q' to quit: ").lower()
    if change == 'q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. This is not case sensitive").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
            d_and_t = False
            continue
    if isfloat(change):
        change = float(change)
        print(change_exchange(change))
    else:
        print("{} is not a valid float!".format(change))
    
raw_input("Press enter to exit.")


#print(change_exchange(12.33))

#print(change_exchange(101.33))
#print(change_exchange(12.33))
#166.41 prints a result that requires everything to have change.
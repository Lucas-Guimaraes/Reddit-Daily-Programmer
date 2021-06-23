#https://www.reddit.com/r/dailyprogrammer/comments/ywlvf/8272012_challenge_92_easy_digital_number_display/
#digital number display
dig_dict = {
'0': ["+--+", "|  |", "|  |", "+  +", "|  |", "|  |", "+--+"],
'1': ["   +", "   |", "   |", "   +", "   |", "   |", "   +"],
'2': ["+--+", "   |", "   |", "+--+", "|   ", "   |", "+--+"],
'3': ["+--+", "   |", "   |", "+--+", "   |", "   |", "+--+"],
'4': ["+  +", "|  |", "|  |", "+--+", "   |", "   |", "+--+"],
'5': ["+--+", "|   ", "|   ", "+--+", "   |", "   |", "+--+"],
'6': ["+--+", "|   ", "|   ", "+--+", "|  |", "|  |", "+--+"],
'7': ["+--+", "   |", "   |", "   +", "   |", "   |", "   +"],
'8': ["+--+", "|  |", "|  |", "+--+", "|  |", "|  |", "+--+"],
'9': ["+--+", "|  |", "|  |", "+--+", "   |", "   |", "+--+"]}


def dig_num_display(n):
    #this takes the number, converts it to a string, checks the amount of digits
    #and makes sure to use our full_clock
    check_clock = str(n)
    dig_amt = len(check_clock)
    full_clock = []
    #this appends the correct items from the dictionary
    #each horizontal line must be made individually
    for i in range(7):
        line = []
        for x in check_clock:
            line.append(dig_dict[x][i])
        full_clock.append(line)
    
    #for each part (each part is each of the seven lines)
    #they all join to create one individual line
    #that individual line is then printed, seven times
    for part in full_clock:
        final_part = part
        final_part = " ".join(final_part)
        print(final_part)

print("Hello! Welcome to digital clock input")
print("In this program, you will input a number")
print("The output?")
print("You will get your number in a digital number display!")
print("\n~*~----------------~*~\n")

dig_clock = True

#this is just a simple validity check. I could have made this into a function.
while dig_clock:
    new_clock = raw_input("Please put in your digit: ")
    if new_clock.isdigit():
        print("")
        dig_clock = False

dig_num_display(new_clock)
print("\n~*~----------------~*~\n")
raw_input("Press enter to exit.")

#dig_num_display(123456890)
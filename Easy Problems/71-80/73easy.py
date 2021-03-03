# https://www.reddit.com/r/dailyprogrammer/comments/w4l6e/762012_challenge_73_easy/
# reverse polish notation
def reverse_polish_notation(pol_str):
    num_1, num_2, symbol = pol_str.split()

    # this part checks if the numbers are floats
    if '.' in num_1:
        num_1 = float(num_1)
    else:
        num_1 = int(num_1)

    if '.' in num_2:
        num_2 = float(num_2)
    else:
        num_2 = int(num_2)

    # this checks whether it's +, -, /, **, or %
    if symbol == "+":
        result = num_1 + num_2
    elif symbol == "-":
        result = num_1 - num_2
    elif symbol == "/":
        result = num_1 / num_2
    elif symbol == "*":
        result = num_1 * num_2
    elif symbol == "**":
        result = num_1 ** num_2
    elif symbol == "%":
        result = num_1 % num_2

    return result


def quit_check(i):
    if i == 'q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. This is not case sensitive: ").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
            return True
    return False


print("Welcome to reverse polish notation!")
print("You will put in two numbers followed by a math symbol")
print("You know how 2 + 4 = 6?")
print("In reverse polish notation, that would be written out like this:")
print("2 4 +")
print("'+', '-', '/', '*', '**', and '%' are all valid math symbols")
print("\n~*~----------------~*~\n")

sym_lst = ['+', '-', '/', '*', '**', '%']

rpn = True
while rpn:
    note = raw_input("Put in your reverse polish notation! 'q' to quit: ").lower()
    if quit_check(note):
        break
    validate = note.split()
    if len(validate) == 3:
        if validate[0].isdigit() and validate[1].isdigit():
            if validate[2] in sym_lst:
                print(reverse_polish_notation(note))
            else:
                print("{} is not a valid symbol! Valid symbols include: '+', '-', '/', '*', '**', '%'".format(str(validate[2])))
        else:
            print("{} and/or {} aren't valid numbers".format(str(validate[0]), str(validate[1])))
    else:
        print("Only 3 items are allowed in {}!".format(note))

raw_input("Press enter to exit")

# print reverse_polish_notation('4 2 +')
# print reverse_polish_notation('4 2 -')
# print reverse_polish_notation('4 2 /')
# print reverse_polish_notation('4 2 *')
# print reverse_polish_notation('4 2 **')
# print reverse_polish_notation('4 2 %')
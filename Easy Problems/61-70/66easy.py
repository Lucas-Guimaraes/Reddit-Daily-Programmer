# https://www.reddit.com/r/dailyprogrammer/comments/v89c4/6182012_challenge_66_easy/

def roman_comparison(x, y):
    roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    for check in roman:
        if x.find(check) > y.find(check):
            return True
        elif y.find(check) > x.find(check):
            return False
    return False


def is_valid_roman(x):
    check_roman = x.replace("M", "").replace("D", "").replace("C", "").replace("L", "").replace("X", "").replace("V",
                                                                                                                 "").replace(
        "I", "")

    if len(check_roman) > 0:
        return False
    return True


def quit_check(i):
    if i == 'Q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. This is not case sensitive: ").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
            return True
    return False

print("Welcome to roman comparison")
print("This will compare two numbers and see which is larger")
print("Here is a chart for reference:")
print("M - 1000")
print("D - 500")
print("C - 100")
print("X - 10")
print("V - 5")
print("I - 1")

print("\n~*~----------------~*~\n")

romans = True
quitting = False

while romans:
    # gets first input
    first_put = True
    while first_put:
        first_roman = raw_input("Please input your first roman numeral. 'q' to quit: ").upper()
        if quit_check(first_roman):
                first_put = False
                quitting = True
                break
        if is_valid_roman(first_roman):
            first_put = False
            continue

    if quitting:
        break

    # gets second input
    second_put = True
    while second_put:
        second_roman = raw_input("Please input your second roman numeral. 'q' to quit: ").upper()
        if quit_check(second_roman):
                second_put = False
                break
        if is_valid_roman(second_roman):
            second_put = False
            quitting = True
            continue

    if quitting:
        break

    print(roman_comparison(first_roman, second_roman))

raw_input("Press enter to exit.")
# print(roman_comparison('X', 'VIII'))
# print(roman_comparison("CX", "MX"))
# print(roman_comparison("MDX", "MDXI"))
# print(roman_comparison("MDX", "MDV"))
# print(roman_comparison("MDV", "MDV"))
#        elif y.find(check) > x.find(check):
#            return False
#    return False
# https://www.reddit.com/r/dailyprogrammer/comments/aphavc/20190211_challenge_375_easy_print_a_new_number_by/
# this program will take each digit in a number and add 1
# so 44 becomes 55, 99 becomes 1010, etc
def digit_add(x):
    result = 0
    factor = 1
    while x:
        # Plus 1 will get the remaiander of it with 10, and add a 1
        # factor will see what placement the number is on
        plus_one = ((x % 10) + 1)
        result += plus_one * factor

        if plus_one != 10:
            factor *= 10
        else:
            factor *= 100
        x //= 10

    return result

print("Hello! Welcome to digit add")
print("This program will take every single number you have and add 1\n")
print("Say you have a number, 444.")
print("We take each of the 4's and add 1")
print("So the number would be 555!")
print("\nFor 9's, this number will carry over to a 10\n")
print("Take 998")
print("9 will be 10, the second 9 will be 10, and 8 will be 9")
print("10109")
print("\n~*~----------------~*~\n")
digit_c = True
while digit_c:
    dig = raw_input("Please input a digit. 'q' to quit: ").replace(' ', '')

    if dig == 'q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. This is not case sensitive").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
            digit_c = False
            continue

    if dig.isdigit():
        print(digit_add(int(dig)))
    else:
        print("{} is not a valid digit!".format(dig))

raw_input("Press Enter to exit.")
# https://www.reddit.com/r/dailyprogrammer/comments/wvc21/7182012_challenge_79_easy_counting_in_steps/

# step_sequencer
# what this does is takes a and b and divides them by the amount of steps (minus 1, ofc)
# this then gets us the number to increment a by to b for the stpes
def step_count(a, b, steps):
    inc = (b - a) / (steps - 1)
    step_lst = [round(a + inc * i, 6) for i in range(steps)]
    return step_lst


# checks if float
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


# check if quitting
def quit_check(i):
    if i == 'q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. This is not case sensitive: ").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
            return True
    return False


print("Welcome to step sequencer!")
print("This program takes one input consisting of two floats and an integer")

print("\n Example Input:")
print("13.50, -20.75, 3")

print("\n Example Output:")
print("13.5, -3.625, -20.75")

print("\n~*~----------------~*~\n")

# this checks the step sequence
step = True
while step:
    seq = raw_input("Please input your values. 'q' to quit: ").replace(",", "")

    # checks if break
    if quit_check(seq):
        break
    check = seq.split()

    # this checks if there are only 3 items input
    if len(check) == 3:

        if isfloat(check[0]) and isfloat(check[1]) and check[2].isdigit():
            print(step_count(float(check[0]), float(check[1]), int(check[2])))
        else:
            print("One of the following digits is in invalid: {0} {1} {2}".format(check[0], check[1], check[2]))
    else:
        print("{} is not a valid sequence! Remember, 'float float int'".format(seq))

raw_input("Press enter to exit")

# print(step_count(18.75, -22.00, 5))
# print(step_count(-5.75, 12.00, 5))
# print(step_count(13.50, -20.75, 3))
# print(step_count(9.75, 3.00, 9))
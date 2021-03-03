# https://www.reddit.com/r/dailyprogrammer/comments/uw14f/6112012_challenge_63_easy/

def reverse(amt, lst):
    revers = lst[amt - 1::-1] + lst[amt:]
    return revers


def quit_check(i):
    if i == 'q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. This is not case sensitive: ").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
            return True
    return False


print("Welcome to list reverse")
print("This program takes two inputs: The amount of items to reverse, and a list")

print("\nExample Input:")
print("2")
print("1 2 3 4 5]")

print("\nExample Output:")
print("2 1 3 4 5")

print("\nExplination:")
print("Since the number was 2, we swapped the first two items in the list")

reving = True
quitting = False

while reving:
    if quitting == True:
        reving = False
        break

    # this gets the amount of items to reverse
    first_put = True
    while first_put:
        rev_amt = raw_input("How many times would you like to reverse? 'q' to quit: ")

        if rev_amt == 'q' or rev_amt == 'Q':
            quitting = quit_check(rev_amt)
            if quitting == True:
                first_put = False
                break
        if rev_amt.isdigit():
            rev_amt = int(rev_amt)
            first_put = False
            continue
        else:
            print("{} is not a valid digit. Please input a valid digit.".format(rev_amt))

    # this gets the list to reverse
    second_put = True
    while second_put:
        lst_for_rev = raw_input("Please input your list. 'q' can quit: ").replace(',', '')

        if lst_for_rev == 'q' or lst_for_rev == 'Q':
            quitting = quit_check(lst_for_rev)
            if quitting == True:
                second_put = False
                break
        lst_for_rev = lst_for_rev.split()

        if len(lst_for_rev) < rev_amt:
            print("There are less items in {} than {}!".format(lst_for_rev, rev_amt))
        else:
            second_put = False
            continue

    print(reverse(rev_amt, lst_for_rev))
print("\n~*~----------------~*~\n")
raw_input("Press Enter to exit.")

# print(reverse(1, [1, 2, 3, 4, 5]))
# print(reverse(2, [1, 2, 3, 4, 5]))
# print(reverse(5, [1, 2, 3, 4, 5]))
# print(reverse(3, [51, 41, 12, 62, 74]))


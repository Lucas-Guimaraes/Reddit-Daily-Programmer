# https://www.reddit.com/r/dailyprogrammer/comments/30ubcl/20150330_challenge_208_easy_culling_numbers/

# cull_lst
def cull_lst(i):
    # Splits string + makes them integers for sorting
    i = i.split()
    i = [int(x) for x in i]
    # eliminates to set, sorts the set.
    i = set(i)
    i = sorted(i)

    # turns to string, join string
    i = [str(x) for x in i]
    i = " ".join(i)

    return i


# Explination
print("Welcome to Order Numbers")
print("Put in a string of numbers; the output will remove all duplicates")
print("Example Input: 1 2 4 1 1 3 2 4")
print("\n~*~----------------~*~\n")

# Checks input, quit case included
order = True
while order:
    n = raw_input().lower()
    if n == 'q':
        break
    test_n = n.replace(" ", "")
    if test_n.isdigit():
        print(cull_lst(n))

raw_input("Press enter to exit.")

# test case:
# print(int_lst('65 36 23 27 42 43 3 40 3 40 23 32 23 26 23 67 13 99 65 1 3 65 13 27 36 4 65 57 13 7 89 58 23 74 23 50 65 8 99 86 23 78 89 54 89 61 19 85 65 19 31 52 3 95 89 81 13 46 89 59 36 14 42 41 19 81 13 26 36 18 65 46 99 75 89 21 19 67 65 16 31 8 89 63 42 47 13 31 23 10 42 63 42 1 13 51 65 31 23 28'))
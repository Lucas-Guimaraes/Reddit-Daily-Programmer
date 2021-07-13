# https://www.reddit.com/r/dailyprogrammer/comments/8xbxi9/20180709_challenge_365_easy_uparrow_notation/

def up_arrow_notation(i, arrow, m):
    if arrow == 1:
        return i ** m
    elif m == 0:
        return 1
    else:
        i = i ** m
        return up_arrow_notation(i, arrow - 1, m)


print("Welcome to up arrow notation!")
print("Input a number, followed by an amount of '^' arrows, followed by another number")
print("\n~*~----------------~*~\n")

up_arrow = True

while up_arrow:
    notation = raw_input()
    if notation == 'q' or notation == 'Q':
        break

    notate_lst = notation.split()


    if len(notate_lst) == 3:
        i, arrow, m = notate_lst[0], notate_lst[1], notate_lst[2]
        if i.isdigit() and m.isdigit() and set(arrow) == set('^'):
            print(up_arrow_notation(int(i), len(arrow), int(m)))

raw_input("Press enter to exit.")

# test case
# print(up_arrow_notation(2, len('^^') ,4))
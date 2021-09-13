#https://www.reddit.com/r/dailyprogrammer/comments/6melen/20170710_challenge_323_easy_3sum/

from itertools import combinations

#gets the list of all numbers that equal 0
def sum_three(arr):
    combo = list(combinations(arr, 3))
    zero_lst = []

    #checks all combiniations to add to list
    for x in combo:
        if sum(x) == 0 and x not in zero_lst:
            zero_lst.append(x)

    return zero_lst

#Checks if negative or positive
def is_integer(i):
    is_negative = i.startswith("-") and i[1:].isdigit()
    is_positive = i.isdigit()
    return is_negative or is_positive

# Introduction
print("Welcome to sum three")
print("Insert a number list separated by spaces - can include negative numbers")
print("\n~*~--------~*~\n")

# input
z_lst = True

while z_lst:
    z = raw_input()
    z = z.split()
    is_digit = True

    #checks if all numbers are digits
    for i in z:
        if is_integer(i) == False:
            is_digit = False
            break

    #if digit, print all sum combinations
    if is_digit:
        z = [int(i) for i in z]
        sum_list = sum_three(z)
        if len(sum_list) == 0:
            print("There are no combinations that equal 0!")
        else:
            for p in sum_list:
               print(p)

raw_input("Press enter to exit.")

#test case
#str = "9 -6 -5 9 8 3 -4 8 1 7 -4 9 -9 1 9 -9 9 4 -6 -8"
#str = str.split()
#str = [int(i) for i in str]
#print(sum_three(str))
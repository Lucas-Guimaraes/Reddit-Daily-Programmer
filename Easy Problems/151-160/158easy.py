# https://www.reddit.com/r/dailyprogrammer/comments/230m05/4142014_challenge_158_easy_the_torn_number/
#would be fun to allow this program to do any number with an even amount of digits
from itertools import permutations

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def torn_number_creator():
    for i in permutations(num_list, 4):

        temp_perm = i
        temp_perm = [str(x) for x in temp_perm]
        compare_perm = ''.join(temp_perm)
        compare_perm = int(compare_perm)

        first_half, second_half = temp_perm[0:2], temp_perm[2:]
        first_half = int(temp_perm[0] + temp_perm[1])
        second_half = int(temp_perm[2] + temp_perm[3])
        test = first_half + second_half
        final_num = test * test

        if final_num == compare_perm:
            print("{} is a torn number!".format(final_num))
    return

def torn_number_checker(num):
    compare = num
    temp_num = str(compare)
    first_half, second_half = temp_num[0:2], temp_num[2:]
    first_half = int(temp_num[0] + temp_num[1])
    second_half = int(temp_num[2] + temp_num[3])
    test = first_half + second_half
    f_test = test * test

    if f_test == compare:
        return("{} is a torn number!".format(compare))
    else:
        return ("{} is not a torn number! When torn, it equals {}".format(compare, f_test))


print("Welcome to number checker!")
print("This program takes one input: A number with an even amount of digits")
print("It will then check whether that number is a torn number")
print("A torn number is when a number is split down the middle")
print("Then both of those numbers are added together")
print("Finally, it is multipled by itself")
print("Example: 1234")
print("Step 1, split the numbers")
print("'12' and '34")
print("Step 2, add the numbers")
print("12 + 34 = 46")
print("Step 3, multiply by itself")
print("2116")
print("Result: 2116 is not equal to 1234, therefor, it is not a torn number")
print("\n~*~----------------~*~\n")
invalid_input = True
while invalid_input:
    num_put = raw_input("Please put in a four digit number:\n")
    num_put = num_put.replace(' ', '')
    if len(num_put) == 4:
        if num_put.isdigit():
            invalid_input = False
print("\n~*~----------------~*~\n")
print(torn_number_checker(num_put))
print("\nHere are all torn numbers that have unique digits from 1 to 9999:\n")
torn_number_creator()
raw_input("\nPress Enter to exit.")

#torn_number_creator()

#print(torn_number_checker(3025))
#print(torn_number_checker(3026))

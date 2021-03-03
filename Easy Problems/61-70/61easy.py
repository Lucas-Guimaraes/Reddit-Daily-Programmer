# https://www.reddit.com/r/dailyprogrammer/comments/uo11f/662012_challenge_61_easy/
# ITS ALL BINARY
import random
from itertools import permutations
import random


# this creates the binary sequence
def binary_sequence(num):
    num_sequence = []
    bin_sequence = []

    bin_num = num_to_bin(num)
    bin_sequence.append(bin_num)

    has_zero = True

    bin_num_str = str(bin_num)
    while has_zero:

        bin_count = bin_num_str.count('0')

        if bin_count == 0:
            has_zero = False
            continue

        bin_num_lst = [int(digit) for digit in bin_num_str]

        index_out = bin_num_lst.pop()

        if index_out == 0:
            bin_num_lst = [str(digit) for digit in bin_num_lst]
            bin_num_str = ''.join(bin_num_lst)
            bin_sequence.append(bin_num_str)
            continue
        else:
            bin_num_lst.insert(0, index_out)
            bin_num_lst = [str(digit) for digit in bin_num_lst]
            bin_num_str = ''.join(bin_num_lst)
            bin_sequence.append(bin_num_str)

    for i in bin_sequence:
        num_convert = bin_to_num(i)
        num_sequence.append(num_convert)

    return bin_sequence, num_sequence


# this turns every number used into a binary
def num_to_bin(num):
    increment_count = 0
    newest_power = 0
    power_list = []
    while newest_power < num:
        newest_power = 2 ** increment_count
        increment_count += 1
        power_list.append(newest_power)

    len_power_lst = len(power_list)
    if power_list[-1] > num:
        power_list.pop()

    highest_digit = power_list.pop()

    no_bin = True
    len_power_lst = len(power_list)
    dict_of_nums = {}

    for i in range(len_power_lst + 1):
        dict_position = i
        amount_of_ones = i
        amount_of_zeros = len_power_lst - i
        bin_lst = []

        for i in range(amount_of_ones):
            bin_lst.append(1)
        for i in range(amount_of_zeros):
            bin_lst.append(0)
        dict_of_nums[dict_position] = bin_lst

    # print(dict_of_nums)

    all_combinations = []

    for i in range(len_power_lst):
        new_perms = dict_of_nums[i]
        for permutation in permutations(new_perms):
            all_combinations.append(permutation)

    # print(all_combinations)

    no_bin = True

    # print(power_list)
    while no_bin:
        bin_total = highest_digit
        new_switch = random.choice(all_combinations)

        for i in range(len_power_lst):
            test_switch = new_switch[i]

            if test_switch == 1:
                bin_total += power_list[i]

        if bin_total == num:
            no_bin = False

    switch_string = "".join(str(x) for x in new_switch)

    binary = '1' + switch_string[::-1]

    return int(binary)


# this turns every binary into a number
def bin_to_num(binary):
    binary_list = [int(digit) for digit in str(binary)]

    decimal = 0
    for i in range(len(binary_list)):

        current_check = 2 ** i
        bin_index = i + 1

        if binary_list[-bin_index] == 1:
            decimal += current_check

    return decimal


# print(bin_to_num(1100011))
# print(num_to_bin(4))
# print(binary_sequence(69))

print("Welcome to Binary Rotation Sequence!")
print("This program will take an integer you put in and convert it to binary.")
print("Afterwarsd, it will rotate the last number in the list to the beginning.")
print("If the last number is a 0, it is removed")

print("\nExample Input:")
print("69")

print("\nExample Output:")
print("Step #1: 69 -> 1000101")
print("Step #2: Move the last digit in 1000101. So it is 1100010")
print("Step #3: The binary number, 1100010, gets converted to 98")
print("And this continues to play out like this:")
print("69 -> 1000101 -> 98 -> 1100010 -> 49 - > 110001 -> 56")
print("(Picking up from 56) -> 111000 -> 28 -> 1100 -> 14 -> 1110 -> 7 -> 111")
print("The final print will look a little more like this:")
print("69 -> 98 -> 49 -> 56 -> 28 -> 14 -> 7 (Lists all regular number rotations)")
print("1000101 -> 1100010 -> 110001 -> 111000 -> 11100 -> 1110 -> 111 (Lists all binary rotations)")

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
        bin_print, num_print = binary_sequence(int(dig))
        num_print = [str(i) for i in num_print]
        bin_print = [str(i) for i in bin_print]
        num_print = " -> ".join(num_print)
        bin_print = " -> ".join(bin_print)
        print(num_print)
        print(bin_print)

    else:
        print("{} is not a valid digit!".format(dig))

raw_input("Press Enter to exit.")

# this is code that flips over the same number over and over again
# just flips - takes the digit at the end, puts it at the beginning, append to list IF its not a 0
# if a 0, it gets culled

# if 1 -> rotation -> append
# if 0 -> cull -> this repeats process
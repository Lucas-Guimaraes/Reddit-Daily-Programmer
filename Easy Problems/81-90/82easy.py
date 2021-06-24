# https://www.reddit.com/r/dailyprogrammer/comments/x8rl8/7272012_challenge_82_easy_substring_list/

import string


def substrings(n):
    a = string.ascii_lowercase[:n]

    for i in range(n):
        for j in range(n + 1):
            if (a[i:j]):
                print(a[i:j])


def sub_string_input(string):
    unique_list = []
    letter_check = ''
    for i in string:
        letter_check = i.lower()
        if letter_check in unique_list:
            continue
        elif letter_check.isalpha():
            unique_list.append(letter_check)
    unique_list = ''.join(unique_list)
    ul_len = len(unique_list)
    for i in range(ul_len):
        for j in range(ul_len + 1):
            if (unique_list[i:j]):
                print(unique_list[i:j])


def count_substrings(n):
    count = 0
    for i in range(n + 1):
        count += i
    return count

def mode_checker(n):
    if n in ['ss', 'cs', 'si']:
        return True
    else:
        return False

print("Hello! Welcome to string fest")
print("This program has three different options: Substrings, count substrings, and string input!")
print("You must first enter which type of string you would like (Substring, count substrings, and string_input")
print("First, decide your mode!:")
print("ss = substring")
print("cs = count substrings")
print("si = string input")

checking = True
print("\n~*~----------------~*~\n")
#this checks for valid input for the mode
check_put = ''
while checking:
    check_put = raw_input("Please put in your input. ['ss', 'cs', and 'si'] are the only valid inputs: ").lower()
    check_put_result = mode_checker(check_put)
    if check_put_result:
        checking = False

if check_put == 'ss':
    substr = int(raw_input("Put in the amount of times to loop!: "))
    substrings(substr)


if check_put == 'cs':
    count_substr = int(raw_input("Put in a number to count the amount of substrings!: "))
    print(count_substrings(count_substr))

if check_put == 'si':
    str_put = raw_input("Put in a string!: ")
    sub_string_input(str_put)


print("\n~*~----------------~*~\n")

raw_input("Press enter to exit")

#substrings(500)
#print(count_substrings(4))
#sub_string_input('Hello World')
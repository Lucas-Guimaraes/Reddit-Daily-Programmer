# https://www.reddit.com/r/dailyprogrammer/comments/35l5eo/20150511_challenge_214_easy_calculating_the/

from math import sqrt

def standard_dev(lst):
    mean = sum(lst) / len(lst)
    total = 0
    for i in lst:
        total += (mean - i) ** 2
    std_deviation = sqrt(float(total / len(lst)))
    return std_deviation


def str_to_num(lst):
    num_lst = []
    for i in lst:
        num_lst.append(int(i))
    return num_lst


print("Welcome to Standard Deviation!")
print("Input a list of numbers, get back the standard deviation")
print("\n~*~----------------~*~\n")

rovar = True

while rovar:
    num_lst = raw_input()
    if num_lst == 'q' or num_lst == 'Q':
        break
    num_lst = str_to_num(num_lst.split())
    print(standard_dev(num_lst))

raw_input("Press enter to exit.")

#Test case:
#9 2 5 4 12 7 8 11 9 3 7 4 12 5 4 10 9 6 9 4

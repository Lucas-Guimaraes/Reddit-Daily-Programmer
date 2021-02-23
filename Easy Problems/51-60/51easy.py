# https://www.reddit.com/r/dailyprogrammer/comments/ti5jc/5112012_challenge_51_easy/

import itertools

def perm_and_len(num_lst, length):
    if length == 1:
        perm_lst = [[x] for x in num_lst]
    else:
        perm_lst = list(itertools.combinations(num_lst, length))
    return perm_lst

#print(perm_and_len([1, 2, 3, 4, 5], 1                   ))
#print(perm_and_len([1, 2, 3, 4, 5], 3))

print("This takes two inputs: A list of integers, and how many numbers in each permutation set")
print("For example, if you use the list '1, 2, 3' and a perm set of '2', you will ")
print("\n~*~--------~*~\n")
p_str = raw_input("Please give me your list:\n")
p_object = p_str.split()
p_object = [int(x) for x in p_object]
l_object = int(raw_input("How big do you want your set to be?:\n"))
print()
print(perm_and_len(p_object, l_object))
raw_input("Press enter to exit.")
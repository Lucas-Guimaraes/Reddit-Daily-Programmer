#https://www.reddit.com/r/dailyprogrammer/comments/3e0hmh/20150720_challenge_224_easy_shuffling_a_list/

import random

#List Shuffle
def shuffle_list(list_input):

    len_lst = len(list_input)

    # Makes random idx list
    ran_idx = []
    while len_lst > len(ran_idx):
        r = random.randrange(0, len_lst)
        if r not in ran_idx:
            ran_idx.append(r)

    #Makes result list
    result_lst = ["*" for i in range(len_lst)]
    for i in range(len_lst):
        result_lst[i] = str(list_input[ran_idx[i]])

    return " ".join(result_lst)

#Input
print("Welcome to Shuffle List!")
print("Example Input:")
print("1 2 3 4")
print("Example Output:")
print("2 4 3 1")
print("\n~*~----------------~*~\n")

#Run Code

shuffling = True

while shuffling:
    l = raw_input()
    if l.lower() == 'q':
        break
    l = l.split()
    l.sort()
    print(shuffle_list(l))


raw_input("Press enter to exit.")

#Test case
#print(shuffle_list([1, 2, 3, 4, 5, 6]))
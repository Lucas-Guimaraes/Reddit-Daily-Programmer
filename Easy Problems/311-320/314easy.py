#https://www.reddit.com/r/dailyprogrammer/comments/69y21t/20170508_challenge_314_easy_concatenated_integers/

from itertools import permutations

#Grab all the permutations, join them all to strings
def concat_int(lst):
    combo = permutations(lst)
    concat = []
    for c in combo:
        i = ''.join(c)
        concat.append(int(i))

    #min and max from the list
    result_str = "{}, {}".format(min(concat), max(concat))
    return result_str


#Introduction text
print("Welcome to concatenate list")
print("Example input:")
print("5 56 50")
print("\n~*~----------------~*~\n")

# Checks input, quit case included

concatenate = True

while concatenate:
    n_lst = raw_input()
    if n_lst.lower() == 'q':
        break
    n_lst = n_lst.split()
    n_lst = [int(x) for x in n_lst]
    n_lst = [str(x) for x in n_lst]
    print(concat_int(n_lst))

raw_input("Press enter to exit.")

#Test cases:
#print(concat_int(['5', '56', '50']))
#print(concat_int(['79', '82', '34', '83', '69']))
#print(concat_int(['420', '34', '19', '71', '341']))
#print(concat_int(['17',  '32', '91', '7', '46']))
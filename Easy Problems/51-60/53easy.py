# https://www.reddit.com/r/dailyprogrammer/comments/tpxq9/5162012_challenge_53_easy/

def sort_comb(seq):
    length = len(seq)
    if length <= 1:
        return seq
    else:
        pivot = seq.pop()

    items_greater = []
    items_lower = []

    for item in seq:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return sort_comb(items_lower) + [pivot] + sort_comb(items_greater)


def prep_qs(lst1, lst2):
    sequence = lst1 + lst2
    return sort_comb(sequence)


print("Welcome to list sort and combine!")
print("This will take two lists of integers and combine them together")
print("While combining the lists, it will sort them!")
print("~*~----------------~*~")
lst_1 = raw_input("Please input your first list of numbers:\n")
obj_1 = lst_1.split()
obj_1 = [int(x) for x in obj_1]
lst_2 = raw_input("Please input your second list of numbers:\n")
obj_2 = lst_2.split()
obj_2 = [int(x) for x in obj_2]
obj_1 = sorted(obj_1)
obj_2 = sorted(obj_2)
print(pres_qs(obj_1, obj_2))

raw_input("Press enter to exit!")

#print(prep_qs([1, 5, 7, 8], [2, 3, 4, 7, 9]))
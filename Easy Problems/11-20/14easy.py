# https://www.reddit.com/r/dailyprogrammer/comments/q2v2k/2232012_challenge_14_easy/

def make_list():
    lst = []
    n = int(raw_input("Enter number of elements you would like to add to your list!: "))

    for i in range(0, n):
        ele = raw_input("Put in an element!: ")
        lst.append(ele)
    return lst


def list_inversion(list_input):
    string_swap = ""
    number_swap = 0
    list_size = len(list_input)
    list_size += 1
    for i in range(1, list_size):
        print i
        if i % 2 == 0:
            number_swap = i - 1
            string_swap = list_input[number_swap]
            del list_input[number_swap]
            number_swap = number_swap - 1
            list_input.insert(number_swap, string_swap)
    return list_input

print list_inversion(make_list())
raw_input()
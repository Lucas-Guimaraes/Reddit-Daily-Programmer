# https://www.reddit.com/r/dailyprogrammer/comments/t33vi/522012_challenge_47_easy/
# make sure when adding i/o you account for window size being bigger than len

def sliding_window(window, window_size):
    shift_size = len(window)
    shift_size = shift_size - window_size
    highest_num = 0
    lowest_num = 0

    for x in range(window_size):
        lowest_num += window[x]
    highest_window = []
    lowest_window = []

    for i in range(shift_size):
        current_shift = 0
        for x in range(window_size):
            current_shift += window[i + x]

        if current_shift < lowest_num:
            lowest_num = current_shift
            lowest_window = []
            for x in range(window_size):
                lowest_window.append(window[i + x])

        elif current_shift > highest_num:
            highest_num = current_shift
            highest_window = []
            for x in range(window_size):
                highest_window.append(window[i + x])

    return highest_window, highest_num, lowest_window, lowest_num

print("Welcome to the sliding window problem!")
print("You will give two inputs: \n1) A list of numbers \n2)A number for how big the window will be")
print("\n~*~----------------~*~\n")
lst = raw_input("Please insert a list:\n")
lst_obj = lst.split()
lst_obj = [int(x) for x in lst_obj]
wsize_obj = int(raw_input("Please insert the window size for your list:\n"))
h_w, h_n, l_w, l_n = sliding_window(lst_obj, wsize_obj)

print("You have chosen this list: {}".format(lst_obj))
print("With a window size of: {}".format(wsize_obj))
print("\n~*~----------------~*~\n")
print("The highest window is: {}".format(h_w))
print("The total of that window is: {}".format(h_n))
print("The lowest window is: {}".format(l_w))
print("The total of that window is: {}".format(l_n))
raw_input("\nPress enter to exit.")

#print(sliding_window([4, 3, 2, 1, 5, 7, 8, 1, 6, 4, 9, 8, 3, 2, 3, 1, 2, 3, 1, 3, 2, 1, 4], 3))
#print(sliding_window([4, 3, 2, 1, 5, 7, 8, 1, 6, 4, 9, 8, 3, 2, 3, 1, 2, 3, 1, 3, 2, 1, 4], 5))
#print(sliding_window([4, 3, 2, 1, 5, 7, 8, 1, 6, 4, 9, 8, 3, 2, 3, 1, 2, 3, 1, 3, 2, 1, 4], 2))
#print(sliding_window([4, 3, 2, 1, 5, 7, 8, 1, 6, 4, 9, 8, 3, 2, 3, 1, 2, 3, 1, 3, 2, 1, 4], 7))
#print(sliding_window([4, 3, 2, 1, 5, 7, 8, 1, 6, 4, 9, 8, 3, 2, 3, 1, 2, 3, 1, 3, 2, 1, 4], 8))
#print(sliding_window([4, 3, 2, 1, 5, 7, 8, 1, 6, 4, 9, 8, 3, 2, 3, 1, 2, 3, 1, 3, 2, 1, 4], 11))

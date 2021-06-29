# https://www.reddit.com/r/dailyprogrammer/comments/759fha/20171009_challenge_335_easy_consecutive_distance/

def racing(lst):
    lst = lst.split()
    for i in range(0, len(lst)):
        lst[i] = int(lst[i])

    sort_lst = sorted(lst)
    count = 0
    #For every item in our list, we check if the next highest is around
    #Then minus the lowest index from the highest
    for i in sort_lst:
        if i + 1 in sort_lst:
            low, high = lst.index(i), lst.index(i + 1)
            if low > high:
                low, high = high, low
            count += (high - low)

    return count

#More information
print("Put a list of integers. Put a space in-between each one")
print("\n~*~----------------~*~\n")

distance_check = True

#QUit case / run code
while distance_check:
    num_lst = raw_input()
    print(racing(num_lst))
    if num_lst == 'q' or num_lst == 'Q':
        distance_check = False
        break
        
raw_input("Press enter to exit.")

#print(racing('1 7 2'))
#print(racing('1 7 2 11 8 34 3'))
#print(racing('31 63 53 56 96 62 73 25 54 55 64'))
#print(racing('77 39 35 38 41 42 76 73 40 31 10'))
#print(racing('30 63 57 87 37 31 58 83 34 76 38'))
#print(racing('18 62 55 92 88 57 90 10 11 96 12'))
#print(racing('26 8 7 25 52 17 45 64 11 35 12'))
#print(racing('89 57 21 55 56 81 54 100 22 62 50'))
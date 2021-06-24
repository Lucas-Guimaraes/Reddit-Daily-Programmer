# https://www.reddit.com/r/dailyprogrammer/comments/xdwyb/7302012_challenge_83_easy_long_scale_and_short/

# Short scale and long scale lists
short_scale = ['hundred', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillikon']
long_scale = ['hundred', 'thousand', 'million', 'milliard', 'billion', 'billiard', 'trillion', 'trilliard']


def long_and_short_scale(num):
    str_num = str(num)
    check_len = len(str_num)

    slice_str = [i for i in str_num]

    num_lst = []
    remainder = check_len % 3
    amt = check_len / 3
    remainder_str = ''.join(slice_str[:remainder])
    num_lst.append(remainder_str)
    for i in range(remainder):
        if remainder == 0:
            break
        slice_str.pop(0)

    #print(slice_str)

    # checks the number go on the short_scale and high_scale
    if check_len > 21:
        future_range = 7
    elif check_len > 18:
        future_range = 6
    elif check_len > 15:
        future_range = 5
    elif check_len > 12:
        future_range = 4
    elif check_len > 9:
        future_range = 3
    elif check_len > 6:
        future_range = 2
    elif check_len > 3:
        future_range = 1
    else:
        if check_len == 3:
            return num + ' ' + short_scale[0]
        else:
            return num
    
    #Runs through the list
    for i in reversed(range(1, future_range + 1)):
        sliced = ''

        for x in range(3):
            sliced += slice_str.pop(0)

        num_lst.append(sliced)

    ss_lst = []
    ls_lst = []
    reversed(num_lst)
    
    #Appends all words
    for i in range(0, len(num_lst)):

        ss_add = str(num_lst[i]) + ' ' + str(short_scale[i])
        ls_add = str(num_lst[i]) + ' ' + str(long_scale[i])
        ss_lst.append(ss_add)
        ls_lst.append(ls_add)
        if i == 1:
            ss_lst.append('and')
            ls_lst.append('and')

    ss_lst = ', '.join(ss_lst)
    ls_lst = ', '.join(ls_lst)
    ss_lst = ss_lst.replace('and,', 'and')
    ls_lst = ls_lst.replace('and,', 'and')

    print(ss_lst)
    print(ls_lst)

    return


# Loops until user quits
scaling = True
while scaling:
    num_put = raw_input("Insert your number: ")

    if num_put.isdigit():
        long_and_short_scale(int(num_put))

    # Quit case.
    if num_put == "q" or num_put == "Q":
        break

raw_input("Press enter to exit.")

# Test case
# long_and_short_scale(1234567891111)
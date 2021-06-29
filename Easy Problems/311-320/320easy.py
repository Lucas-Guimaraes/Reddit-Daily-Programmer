# https://www.reddit.com/r/dailyprogrammer/comments/6i60lr/20170619_challenge_320_easy_spiral_ascension/

def ascend(i):
    big_i = i * i
    [] for x in range(i)
    a = 1
    idx_in = 0
    idx_out = 0

    right_check, down_check, left_check, up_check = i - 1, i - 1, 0, 0

    r = 'right'
    lst = []
    outer = [x for x in range(i)]

    for x in range(i):
        lst.append(outer)

    lst[idx_in][idx_out] = a

    while big_i > a:

        lst[idx_out][idx_in] = a
        a += 1
        if r == 'right':
            idx_in += 1
        elif r == 'down':
            idx_out += 1
        elif r == 'left':
            idx_in -= 1
        elif r == 'up':
            idx_out -= 1

        if idx_in == right_check:
            r = 'down'
            right_check -= 1
        if idx_in == down_check:
            r = 'left'
            down_check -= 1
        if idx_out == left_check:
            r = 'up'
            down_check += 1
        if idx_out == up_check:
            r = 'right'
            down_check += 1

    for x in lst:
        print(''.join(x))


ascend(4)
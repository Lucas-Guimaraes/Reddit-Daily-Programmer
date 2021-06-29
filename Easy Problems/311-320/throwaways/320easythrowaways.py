# https://www.reddit.com/r/dailyprogrammer/comments/6i60lr/20170619_challenge_320_easy_spiral_ascension/

def ascend(i):
    big_i = i * i
    a, idx_in, idx_out = 1
    
    #These check for when a number is at the top or bottom of an index
    right_check, down_check, left_check, up_check = i - 1, i - 1, 0, 1

    r = 'right'
    #createes a matrix
    lst = [[0 for x in range(i)] for j in range(i)]

    while big_i+1 > a:
        #adds to idx
        lst[idx_out][idx_in] = a
        a += 1
        #checks if down/up/left/right limit is reached
        if idx_in == right_check and r == 'right':
            r = 'down'
            right_check -= 1
        elif idx_out == down_check and r == 'down':
            r = 'left'
            down_check -= 1
        elif idx_in == left_check and r == 'left':
            r = 'up'
            left_check += 1
        elif idx_out == up_check and r == 'up':
            r = 'right'
            up_check += 1
        
        #increments the idx
        if r == 'right':
            idx_in += 1
        elif r == 'down':
            idx_out += 1
        elif r == 'left':
            idx_in -= 1
        elif r == 'up':
            idx_out -= 1

    #prints result
    for x in lst:
        thing = "".join(str(x))
        thing = thing.replace("[", "").replace("]", "").replace(",", "")
        print(thing)

ascend(3)
ascend(4)
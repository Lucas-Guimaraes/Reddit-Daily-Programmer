# https://www.reddit.com/r/dailyprogrammer/comments/53ijnb/20160919_challenge_284_easy_wandering_fingers/

def weave(arr_1, arr_2):
     cur_weave = 0
     new_arr = []
     for i in range(len(arr_2)):
        new_arr.append(arr_2[i])
        new_arr.append(arr_1[cur_weave])
        cur_weave += 1
        if cur_weave >= len(arr_1):
            cur_weave = 0
     return new_arr

print(weave([1, 2, 3], [1, 2, 3, 4]))
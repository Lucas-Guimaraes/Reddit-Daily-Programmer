#https://www.reddit.com/r/dailyprogrammer/comments/quli5/3132012_challenge_23_easy/
#doubles list

def double_list(lst):
    first_lst = []
    second_lst = []
    half_lst = len(lst) / 2
    
    count = -1
    for item in lst:
        count += 1
        if count < half_lst:
            first_lst.append(item)
        else:
            second_lst.append(item)
    return first_lst, second_lst;
            
print double_list(["hey", "hi", "yo", "yeah", "two", "more"])
raw_input()
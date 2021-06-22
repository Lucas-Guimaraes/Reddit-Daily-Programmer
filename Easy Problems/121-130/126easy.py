#https://www.reddit.com/r/dailyprogrammer/comments/1epasu/052013_challenge_126_easy_realworld_merge_sort/

#This function merges two lists to each other
#While List A is not sorted, list B MUST be sorted.
def merge_sort(list1, list2):
    #First, each of the lists are enumerated over
    for index, item in enumerate(list1):
        #We check the current item in the other list
        #And insert items from the first list through merging them
        for current in range(len(list2)-1):
            nxt = current + 1
            if list2[current] == 0:
                list2[current] = item
            if list2[current] <= list2[nxt]:
                break
            else:
                list2[current] = list2[nxt]
                list2[nxt] = item
    return list2

#Put in list A and B with it!
print(merge_sort([692, 1, 32], [0, 0, 0, 14, 15, 123, 2431]))
#Ends the program
raw_input()
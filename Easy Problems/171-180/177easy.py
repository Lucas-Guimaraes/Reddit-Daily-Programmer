# https://www.reddit.com/r/dailyprogrammer/comments/2ejl4x/8252014_challenge_177_easy_quicksort/
import random

#Starts the quick sort
def quick_sort(l):
    length = len(l)
    
    #Base case, or creates our random pivot
    if length <= 1:
        return l
    else:
        pivot = random.choice(l)
    items_greater = []
    items_lower = []
    
    #organizes items into greater and lower
    for item in l:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    
    #returns the final sort
    return quick_sort((items_lower)) + quick_sort((items_greater))


print(quick_sort([2, 3, 1, 7, 9, 8]))
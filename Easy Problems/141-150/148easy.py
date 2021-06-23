#https://www.reddit.com/r/dailyprogrammer/comments/1v4cjd/011314_challenge_148_easy_combination_lock/

def spin_lock(length, a, b, c):
    #spins the first digit. Length * 2, add it to A.
    answer = length * 2
    answer += a
    
    #spins the second one. Add the length, add A again, minus B to spin it counter.
    answer += length
    answer += length + a - b
    
    #spins the third! Minus B, but add C.
    answer += length - b + c
    
    #Returns our answer
    return answer
 
print(spin_lock(4, 2, 3, 1))
raw_input()


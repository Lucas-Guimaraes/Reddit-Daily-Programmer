#https://www.reddit.com/r/dailyprogrammer/comments/55nior/20161003_challenge_286_easy_reverse_factorial/

def reverse_factorial(n):
    cur = 2
    
    #Checks divisibility starting from 2
    while True:
        n = float(n / cur)
        cur += 1
        
        #Break cases
        if n == float(1):
            break
        if int(n) == 0:
            return None
            
    return "{}!".format(str(cur-1))

print(reverse_factorial(479001600))

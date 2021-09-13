#https://www.reddit.com/r/dailyprogrammer/comments/6s70oh/2017087_challenge_326_easy_nearest_prime_numbers/

import math

#Check if prime
def isprime(n):
    #If 1, true
    if n == 1:
        return True
    
    
    i = 2
    while i <= int(math.sqrt(n)):
        #If divisible by 0, false. Else, keep checking
        if n % i == 0:
            return False
        else:
            i += 1
            
        #If it is only divisible by itself, return True
        if i == int(math.sqrt(n)):
            return True

#Gets the nearest prime
def nearestprime(n):
    prime = isprime(n)
    #If Prime, return true
    if prime:
        return "{} is prime.".format(n)
    #Find Lowest and highest prime
    else:
        lower_pr = n-1
        higher_pr = n+1

        while isprime(lower_pr) == False:
            lower_pr -= 1
        while isprime(higher_pr) == False:
            higher_pr += 1

        return "{} < {} < {}".format(lower_pr, n, higher_pr)

#Intro
print("Welcome to permbase2")
print("Use 'd' for base 10, and 'b' for binary input")
print("'d' will be the default")
print("\n~*~--------~*~\n")

#Input
converting = True
while converting:
    i = raw_input()
    i = i.lower()
    mode = 'd'
    if i == 'q':
        break
    elif i == 'b':
        mode = 'b'
        print("Mode is now binary")
    elif i == 'd':
        mode = 'd'
        print("Mode is now decimal")

    if mode == 'd' and i.isdigit():
        print(permbase2(int(i)))
    elif mode == 'b':
        print(permbase2inv(i))

raw_input("Press enter to exit.")

#Test cases
#print(nearestprime(2010741))
#print(nearestprime(1425172824437700148))


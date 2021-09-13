#https://www.reddit.com/r/dailyprogrammer/comments/5xu7sz/20170306_challenge_305_easy_permutation_base/
import math

def permbase2inv(n):
    #replace string
    n = n.replace(" ", "")
    #Get the square of the length, and add the base 10 of the binary
    return (2**len(n))-2 + int(n, 2)

def permbase2(n):
    #Length to get minus amount
    length = math.floor(math.log(n+2, 2))
    n -= (2**length)-2
    #Grabs binary as string, cuts off the '0b'
    #Then adds spaces for string formatting
    val = str(bin(int(n)))
    val = list(val[2:])
    val = " ".join(val)
    return val

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

#test cases
#print(permbase2inv("1 1 1 0 0 0 1 1 1"))
#print(permbase2(54))
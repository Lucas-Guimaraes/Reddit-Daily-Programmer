# https://www.reddit.com/r/dailyprogrammer/comments/32goj8/20150413_challenge_210_easy_intharmonycom/

#Checks the compatability percentage
def compatability(a, b):
    #32-bit test
    x = '{:032b}'.format(a)
    y = '{:032b}'.format(b)
    
    #increases count for each bit equal
    count = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            count += 1
    count = count / 32.0
    
    return count * 100.0

#opposite
def opp(x):
    return x ^ 0xFFFFFFFF

print("Welcome to Compatability Checker!")
print("Example Input: 42 100")
print("\n~*~--------~*~\n")

compatable = True
while compatable:
    n = raw_input()
    if n.lower() == 'q':
        break
    n = n.split()
    a, b = n[0], n[1]
    if a.isdigit() and b.isdigit():
        a, b = int(a), int(b)
        c = compatability(a, b)
        print("{} and {} are {}% compatible".format(a, b, c))
        print("{} should avoid {}".format(a, opp(a)))
        print("{} should avoid {}".format(b, opp(b)))
raw_input("Press enter to exit.")

#test case
#print(compatability(100, 42))
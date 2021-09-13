#https://www.reddit.com/r/dailyprogrammer/comments/6nstip/20170717_challenge_324_easy_manual_square_root/

#Grabs the smallest square root
def sqrt(num, add, new=0):

    #X is how much we are adding by
    x = add

    #while our new num is smaller than our comparison num, multiply x by x
    #Previous state tracks our previous one
    while num > new:
        prev_state = x
        x += add
        new = x * x
    return prev_state

#Triggers sqrt
def manual_sqrt(n, fl=0):
    prev_state = sqrt(n, 1)

    #If there is a floating point larger than '0', we run prev_state again
    if fl > 0:
        floating_point = '.' + (fl * '0')
        floating_point = floating_point[:len(floating_point)-1] + '1'
        prev_state = sqrt(n, float(floating_point), prev_state)
        prev_state = round(prev_state, fl)

    #Return
    return prev_state

def isfloat(n):
    if '.' in n:
        n = n.split('.')
        if n[0].isdigit() and n[1].isdigit() and len(n) == 2:
            return True
    return False
    
# Intro text
print("Welcome to Square Root")
print("Input a floating point, followed by a float number")
print("\n~*~----------------~*~\n")

calculating = True

while calculating:
    c = raw_input()
    if c.lower() == 'q':
        break
    c = c.split(' ')
    fl, n = c[0], c[1]
    if fl.isdigit() and (n.isdigit()) or (isfloat(n)):
        print(manual_sqrt(float(n), int(fl)))

raw_input("Press enter to exit")

#Test cases:

#print(manual_sqrt(7720.17, 2))
#print(manual_sqrt(12345, 0))
#print(manual_sqrt(123456, 8))
#print(manual_sqrt(12345678901234567890123456789), 0)

#https://www.reddit.com/r/dailyprogrammer/comments/1jtryq/080613_challenge_134_easy_ndivisible_digits/

def ndivisible(n, m):
    #N is the amount of digits. This solves for N.
    x = 10 ** n-1
    formula = x - x % m
    
    #If the formula is more than 0, we print the result of the Formula
    if formula > 0:
        return formula
    else:
        return "There are no divisible numbers of {0} with {1} digits. Sorry!".format(m, n)

print("Drops the two numbers; The amount of digits and number")
print("Example Input: 3 2")
print("Example Output: 998")
print("\n~*~----------------~*~\n")
n_divisor = True

while n_divisor:
    nums_put = raw_input("Put in your two numbers. 'Q' or 'q' to quit: ")
    nums_put = nums_put.split()
    
    if nums_put[0].isdigit() and nums_put[1].isdigit():
        print(ndivisible(int(nums_put[0]), int(nums_put[1])))
    if nums_put == 'q' or nums_put == 'Q':
        n_divisor = False
    
raw_input("Press enter to exit.")

print(ndivisible(3, 2))
raw_input()
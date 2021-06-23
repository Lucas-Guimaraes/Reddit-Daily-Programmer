# https://www.reddit.com/r/dailyprogrammer/comments/1hvh6u/070813_challenge_132_easy_greatest_common_divisor/

#Greatest Common Divisor
def gcd(n, m):
    #if n is bigger than m, m and n will be flipped around
    if n > m:
        n, m = m, n

    #Remainder goes down until they find the highest divisible
    remainder = 1
    while remainder > 0:
        
        remainder = n % m

        #If it does not equal 0, m becomes the smaller number
        #The remainder becomes the larger number
        if remainder != 0:
            n = m
            m = remainder

    return m


print("Drops the two numbers; find the greatest common divisor")
print("Example Input: 32 12")
print("Example Output: 4")
print("\n~*~----------------~*~\n")
divising = True 

while divising:
    nums_put = raw_input("Put in your two numbers. 'Q' or 'q' to quit: ")
    nums_put = nums_put.split()
    
    if nums_put[0].isdigit() and nums_put[1].isdigit():
        print(gcd(int(nums_put[0]), int(nums_put[1])))
    if nums_put == 'q' or nums_put == 'Q':
        divising = False
    
raw_input("Press enter to exit.")

#Test cases
#print(gcd(32, 12))
#print(gcd(142341, 512345))
#print(gcd(65535, 4294967295))
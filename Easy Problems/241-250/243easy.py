#https://www.reddit.com/r/dailyprogrammer/comments/3uuhdk/20151130_challenge_243_easy_abundant_and/

def number_check(n):
    divisor_total = sum(find_divisors(n))
    n_squared = n*2
    if divisor_total < n_squared:
        return 'deficient by {}'.format(n_squared-divisor_total)
    elif divisor_total > n_squared:
        return 'abundant by {}'.format(divisor_total-n_squared)
    else:
        return '~~neither~~'

def find_divisors(n):
    lst = []
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)
    return lst

#Intro code
print("Welcome to Deficient, Abundant, or Neither")
print("Input a number: The output will be if that number is Deficient, Abundant, or Neither")
print("\n~*~----------------~*~\n")

#Runs Code
checking = True
while checking:
    n = raw_input()
    if n.lower() == 'q':
        break
    if n.isdigit():
        print(number_check(int(n)))

raw_input("Press enter to exit.")


#Test case
#print(number_check(6))
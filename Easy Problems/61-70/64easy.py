# https://www.reddit.com/r/dailyprogrammer/comments/uzx8b/6132012_challenge_64_easy/
# Five functions needed:
# 1) Get Divisors
# 2) the sum of the divisors
# 3) the number of the divisors
# 4) Get the totative - all the numbers between 1 and the target number that have no other common factors than 1 (so their greatest common denominator is one)
# 5) Get the totient - it's the len of the totatives
# - Greatest Common Denominator - what number is the highest


def get_divisors(n):
    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


# this can just be done through sum(get_divisors(n))
def sum_divisors(n):
    get_divisor_list = get_divisors(n)
    total_sum = 0
    for i in get_divisor_list:
        total_sum += i
    return total_sum


# this can just be done through len(get_divisors(n))
def amt_of_divisors(n):
    get_divisor_list = get_divisors(n)
    amt_of_divs = 0
    for i in get_divisor_list:
        amt_of_divs += 1
    return amt_of_divs


def get_totatives(n):
    totatives = []
    divisor_list = get_divisors(n)
    divisor_list.remove(n)

    for i in range(1, n + 1):
        totative_list = get_divisors(i)
        comparison = list(set(divisor_list).intersection(totative_list))
        if comparison == [1]:
            totatives.append(i)


    return totatives


def get_totient(n):
    get_totative_list = get_totatives(n)
    totient = 0
    for i in get_totative_list:
        totient += 1
    return totient

def sum_totatives(n):
    get_totative_list = get_totatives(n)
    total_sum = 0
    for i in get_totative_list:
        total_sum += i
    return total_sum

print("Welcome to total!")
print("In this program, you will input a number")
print("And it will return the following: \n")

print("1. Numbers that can divide that number and equal 0")
print("2. The sum of all numbers that divide it into 0.")
print("3. The amount of divisors")
print("4. All totatives - All numbers that have no common factors with the number chosen other than 1")
print("5. The sum of all the totatives")
print("6. The amount of totatives")
print("Apologies if that was a lot. Have fun!")

print("\n~*~----------------~*~\n")

d_and_t = True
while d_and_t:
    num_to_math = raw_input("Please input your number. 'q' to quit: ").lower()
    if num_to_math == 'q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. This is not case sensitive").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
            d_and_t = False
            continue
    if num_to_math.isdigit():
        num_to_math = int(num_to_math)
        print("")
        print(get_divisors(num_to_math))
        print(sum_divisors(num_to_math))
        print(amt_of_divisors(num_to_math))
        print(get_totatives(num_to_math))
        print(sum_totatives(num_to_math))
        print(get_totient(num_to_math))
        print("")
    else:
        print("{} is not a valid number!".format(num_to_math))

raw_input("Press enter to exit.")

#print(get_divisors(60))
#print(sum_divisors(60))
#print(amt_of_divisors(60))
#print(get_totatives(30))
#print(get_totient(30))
#print(sum_totatives(30))
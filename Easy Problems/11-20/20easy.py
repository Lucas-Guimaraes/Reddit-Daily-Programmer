# https://www.reddit.com/r/dailyprogrammer/comments/qnkro/382012_challenge_20_easy/

#checks if a number is prime
def check_prime(number):
    if (number <= 1):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

#takes only primes
#throws a loop that adds a number to a list
def primes_only(number):
    prime_list = []
    for num in range(0, number):
        if check_prime(num) is True:
            prime_list.append(str(num))
    return prime_list

user_input = int(raw_input("Put in a prime!: "))
print primes_only(user_input)
raw_input()
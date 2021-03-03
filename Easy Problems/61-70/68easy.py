# https://www.reddit.com/r/dailyprogrammer/comments/vfylp/6222012_challenge_68_easy/

def emirp(num_range):
    emirps = []
    reversed_num = 0

    for i in range(num_range + 1):
        if i > 1:
            if prime_check(i) == True:
                reversed_num = str(i)
                reversed_num = int(reversed_num[::-1])
                if reversed_num == i:
                    continue
                elif prime_check(reversed_num) == True:
                    emirps.append(i)
        else:
            continue

    return emirps


def prime_check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def quit_check(i):
    if i == 'q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. This is not case sensitive: ").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
            return True
    return False


print("Welcome to emirps!")
print("This program takes a number, and counts all the emirps in that!")
print("What's an emirp?")
print("It's a prime number that, done backwards, would also be a prime number!")
print("Example: 13 done backwards is 31, which is a prime number!")
print("For a refresher on prime numbers: They are numbers divisible to 0 by only 1 and itself")

print("\n~*~----------------~*~\n")

emirps = True
while emirps:
    prime_range = raw_input("Please input a num to convert. 'q' to quit: ").lower()
    if quit_check(prime_range):
        emirps = False
        continue
    if prime_range.isdigit():
        print(emirp(int(prime_range)))
    else:
        print("{} is not a valid digit!".format(prime_range))

raw_input("\nPress enter to exit.")

raw_input()
# print(emirp(180))
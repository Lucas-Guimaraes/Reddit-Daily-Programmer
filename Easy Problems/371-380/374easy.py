# https://www.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/

def add_pers(x):
    pers = 0

    while x >= 10:

        new = 0
        edit = x
        while edit >= 1:
            new += (edit % 10)
            edit /= 10
        x = new
        pers += 1

    return pers


print("Welcome to additive persistence!")
print("This program will take a number and print the amount of iterations it needs to find the additive persitence")
print("Additive Persistence is explained with examples below!")
print("\nExample #1\n")
print("13")
print("1 + 3 = 4")
print("Since 4 is below the number 10, that means it only had one iteration")
print("Output: 1")
print("\nExample #1\n")
print("Input: 199")
print("1 + 9 + 9 = 19")
print("19 is not below 10 and has two digits")
print("1 + 9 = 10")
print("1 + 0 = 1")
print("Since 1 is below the number 10, we have our final number")
print("Output: 3")
print("\n~*~----------------~*~\n")

digit_c = True
while digit_c:
    dig = raw_input("Please input a digit. 'q' to quit: ").replace(' ', '')

    if dig == 'q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. This is not case sensitive").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
            digit_c = False
            continue

    if dig.isdigit():
        print(add_pers(int(dig)))
    else:
        print("{} is not a valid digit!".format(dig))

raw_input("Press Enter to exit.")

print(add_pers(199))
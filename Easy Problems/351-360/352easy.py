# https://www.reddit.com/r/dailyprogrammer/comments/7yyt8e/20180220_challenge_352_easy_making_imgurstyle/

# Base 10 to 62 converter

# base_10 = "0123456789"
base_62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


# base 10 to new base converter
def imgur_style(num, base):
    result = []
    base_num = len(base)
    while num:
        num, rem = divmod(num, base_num)
        result.append(base[rem])
    return ''.join(result)


print("Welcome to imgur maker!")
print("Insert a number, and we will give you its Imgur URL!")
print("\n~*~----------------~*~\n")

basing = True
while basing:
    b_10 = raw_input()
    # Quit case
    if b_10 == 'q' or b_10 == 'Q':
        basing = False
        break
    # The base is automatic, but can be modified for input
    if b_10.isdigit():
        print(imgur_style(int(b_10), base_62))

raw_input("Press Enter to exit.")



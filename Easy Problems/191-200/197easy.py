#https://www.reddit.com/r/dailyprogrammer/comments/2s7ezp/20150112_challenge_197_easy_isbn_validator/

def isbn(isbn_num):

    isbn_num = [int(i) for i in isbn_num]

    total, x = 0, 10
    for i in isbn_num:
        total += i * x
        x -= 1

    return total % 11 == 0

print("Welcome to ISBN Number!")
print("This will take your input, a ten digit number, and output if it's a valid ISBN number!")
print("\n~*~--------~*~\n")

test = True

while test:
    t = raw_input("")

    if t.lower() == 'q':
        break

    if "-" in t:
        t = t.replace("-", "")

    if t.isdigit():
        print(isbn(t))

raw_input("Press enter to exit")
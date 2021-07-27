#https://www.reddit.com/r/dailyprogrammer/comments/8eger3/20180423_challenge_358_easy_decipher_the_seven/

numbers = {
    " ||_ _ ||": "0",
    "       ||": "1",
    "  |___ | ": "2",
    "   ___ ||": "3",
    " |  _  ||": "4",
    " | ___  |": "5",
    " ||___  |": "6",
    "   _   ||": "7",
    " ||___ ||": "8",
    " | ___ ||": "9"
}


def display_to_one(l1, l2, l3):
    n_str = ''
    r_begin = 0
    r_end = 3
    while 9 > len(n_str):
        temp = ''
        for i in range(r_begin, r_end):
            temp += l1[i] + l2[i] + l3[i]
        n_str += numbers[temp]
        r_begin += 3
        r_end += 3
    return n_str

print("Welcome to Display Seven.")
print("Input a digital clock over 3 lines, and this will output the number")
print("\n~*~----------------~*~\n")

clock = True
while clock:
    l1, l2, l3 = raw_input("First Line: "), raw_input("Second Line: "), raw_input("Third Line: ")
    if l1.lower == 'q' or l2.lower == 'q' or l3.lower == 'q':
        break
    print(display_to_one(l1, l2, l3))

raw_input("Press Enter to exit.")

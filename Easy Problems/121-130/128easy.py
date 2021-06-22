# https://www.reddit.com/r/dailyprogrammer/comments/1fnutb/06413_challenge_128_easy_sumthedigits_part_ii/
#This is part 2 to to the 'sumthedigits' from 122 easy
#This program will take a set of digits, sum them update
#And keep going until one digit is left

def sumthedigits(num):
    print(num)

    while len(str(num)) > 1:
        num_sep = [int(d) for d in str(num)]
        total = 0
        for i in num_sep:
            total += i
        num = total
        print(num)


print("Put in a number")
print("And then the program will add all the separate digits")
print("And it will keep going until they all add up")
print("\n~*~----------------~*~\n")

#Checks input.
num_put = True
while num_put:
    dig_num = raw_input("Give me a number. Press 'Q' or 'q' to quit: ")
    if dig_num == 'q' or dig_num == 'Q':
        num_put = False
        break
    if dig_num.isdigit():
        sumthedigits(int(dig_num))

raw_input("Press enter to exit.")


#test cases
#sumthedigits(9075194238108352910843902124193804230182134876870231456210357123598102347575108767534620017342381038461573640261364731250725634597864537789457368687567868789889899)
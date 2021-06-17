# https://www.reddit.com/r/dailyprogrammer/comments/1268t4/10272012_challenge_108_easy_scientific_notation/

# import random
# - gives a random float number
# random.uniform
# can be used on the calculator

def scientific_notation_calc(num):
    power = 0

    # This is for negative power
    if num < 1:
        while num < 1:
            temp_num = float(num)
            temp_num = temp_num * 10

            power -= 1
            num = temp_num

    # This is for positive power
    elif num >= 1:
        while num > 10:
            temp_num = float(num)
            temp_num = temp_num / 10

            power += 1
            num = temp_num

    # num + x + 10 ^ + power
    fancy_string = str(num) + ' x ' + '10 ^ ' + str(power)

    return fancy_string


# this function does the reverse. I did not put in a way to input it.
def decimal_notation_calc(num, exponent):
    decimal = num * (10 ** exponent)
    return decimal


print("Welcome to decoder. 'q' will quit the program.")
print("\n~*~----------------~*~\n")
dec_notate = True
while dec_notate:
    num_note = raw_input("Give me a float: ")
    # if digit, print!
    isfloat = False
    try:
        float(num_note)
        isfloat = True
    except:
        if num_note == 'q' or num_note == 'Q':
            dec_notate = False
            raw_input("Press enter to exit.")
            continue
        else:
            continue

    print(scientific_notation_calc(float(num_note)))
    # exit code


# test cases:
# print(scientific_notation_calc(.654))
# print(scientific_notation_calc(239487))
# print(decimal_notation_calc(935, -3))
raw_input()
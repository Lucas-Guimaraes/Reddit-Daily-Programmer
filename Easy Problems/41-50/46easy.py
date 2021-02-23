# https://www.reddit.com/r/dailyprogrammer/comments/szz5y/4302012_challenge_46_easy/

# counts the population
def pop_count(x):
    population = {i: 2 ** i for i in range(1, 30)}

    for num, power in population.items():

        if power >= x:
            bit_amt = num
            break

    num_bin = dectobin(x, bit_amt)

    pop_final = num_bin.count(1)
    num_bin = ''.join(str(num_bin))
    num_bin = num_bin.replace('[', '').replace(']', '').replace(',', '').replace(' ', '')
    return pop_final, num_bin


# s is the length of the decimal
# x is the number to convert
def dectobin(x, s):
    converted = [(x >> k) & 1 for k in range(0, s)]
    converted.reverse()
    return converted


print("Welcome to population count!")
print(
    "This application takes an integer, converts it to binary, and then counts the amount of 1's in it to get a population count")
print("\n~*~--------~*~\n")
# population, binary
p_num, b_num = pop_count(int(raw_input("Please put in the number to convert: ")))
print("The total population is {}".format(p_num))
print("Your chosen number in binary is {}".format(b_num))

raw_input()
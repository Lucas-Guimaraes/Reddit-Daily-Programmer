# https://www.reddit.com/r/dailyprogrammer/comments/3fmke1/20150803_challenge_226_easy_adding_fractions/


def gcd(lst):
    # this grabs the start, for the lowest common denominator
    # and prepares our list
    gcd_lst = lst
    gcd_lst.sort()
    gcd_start = gcd_lst[0]

    # loop code
    gcd_loop = True
    while gcd_loop:
        for i in gcd_lst:
            if i % gcd_start == 0:
                if i == gcd_lst[-1]:
                    gcd_loop = False
                    break
            else:
                gcd_start -= 1
                break
    return gcd_start


def fractions(numerator_lst, denominator_lst):
    # this gives a common denominator between all numbers
    new_denominator = denominator_lst[0]
    for i in denominator_lst[1:]:
        new_denominator *= i

    # this gives us the new numerators list
    new_numerators = []
    for idx, num in enumerate(numerator_lst):
        multi = new_denominator / denominator_lst[idx]
        new_num = multi * num
        new_numerators.append(new_num)

    new_numerator = sum(new_numerators)

    # this handles greatest common denominator, followed by string formatting
    lst_for_gcd = [new_numerator, new_denominator]
    gcd_final = gcd(lst_for_gcd)
    final_result = [new_numerator / gcd_final, new_denominator / gcd_final]
    final_str_result = (str(final_result[0]) + " / " + str(final_result[1]))

    return final_str_result


print("Welcome to fractions!")
print("This program takes a number input!")
print("Following that number, the amount of fractions")
print("\nExample Input:\n")
print("Number Input: 2")
print("Fraction #1: 1 / 6")
print("Fraction #2: 3 / 10")
print("\nExample Output:\n")
print("7/15")
print("\n~*~----------------~*~\n")

num_put = int(raw_input("Please devise a number: "))
lst_num, lst_den = [], []

for i in range(num_put):
    new_num = raw_input("Please put in a fraction: ")
    new_num_lst = new_num.split(" / ")
    lst_num.append(int(new_num_lst[0]))
    lst_den.append(int(new_num_lst[1]))

print("\n~*~----------------~*~\n")
print("Your result is: ")
print(fractions(lst_num, lst_den))

print("\n~*~----------------~*~\n")

raw_input("Press enter to exit.")
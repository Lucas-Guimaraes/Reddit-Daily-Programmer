# https://www.reddit.com/r/dailyprogrammer/comments/a72sdj/20181217_challenge_370_easy_upc_check_digits/


def upc(n):

    if 11 > len(n):
        n = ((11 - len(n)) * '0') + n
    odd = []
    even = []

    #appends to odd or even
    for i in range(1, 12):
        cur = int(n[i - 1])
        if i % 2 == 1:
            odd.append(cur)
        else:
            even.append(cur)

    #formula once odds and evens are amassed
    upc_formula = (((sum(odd) * 3) + sum(even)) % 10)
    if upc_formula == 0:
        return 0
    else:
        return 10 - upc_formula

#Introduction code


print("Welcome to valid UPC.")
print("Pick a number from 1 to 11.")
print("We will then answer what the last digit is")
print("\n~*~----------------~*~\n")


#Loop/running program

upc_true = True

while upc_true:
    n = raw_input()
    if n == 'q' or n == 'Q':
        break

    if n.isdigit() and 11 >= len(n):
        print(upc(n))

raw_input("Press enter to exit.")

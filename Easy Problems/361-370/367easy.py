# https://www.reddit.com/r/dailyprogrammer/comments/9cvo0f/20180904_challenge_367_easy_subfactorials_another/

def derangement(n):
    der = [0 for i in range(n + 1)]
    der[1] = 0
    der[2] = 1

    for i in range(3, n + 1):
        der[i] = (i - 1) * (der[i - 1] + der[i - 2])

    return der[n]

print("Welcome to derangements!")
print("Pick a number")
print("\n~*~----------------~*~\n")

derange = True

while derange:
    der_num = raw_input()
    if der_num == 'q' or der_num == 'Q':
        break

    if der_num.isdigit():
        print(derangement(der_num))

raw_input("Press enter to exit.")

#test cases
#print(derangement(5))
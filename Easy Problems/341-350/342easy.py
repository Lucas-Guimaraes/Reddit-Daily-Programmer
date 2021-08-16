#https://www.reddit.com/r/dailyprogrammer/comments/7fvy7z/20171127_challenge_342_easy_polynomial_division/

#This function gets the remainder and the quotient
def coeff(dividend, divisor):
    tempDividend = dividend
    # Grabs the initial Quotient, and the current index
    Quot = [0.0] * (len(coeffDividend) - len(coeffDivisor) + 1)
    index = len(Quot) - 1

    # Works to get our remainder
    while index >= 0:
        temp = [0.0] * len(tempDividend)
        interQuot = tempDividend[-1] / coeffDivisor[-1]
        Quot[index] = interQuot
        # Goes through all Divisor items
        for index2 in range(0, len(coeffDivisor) - 1):
            temp[index + index2] = coeffDivisor[index2] * interQuot
            # Goes through all divided items
        for index3 in range(0, len(tempDividend) - 1):
            tempDividend[index3] -= temp[index3]

        index -= 1
        tempDividend.pop()

    print("Remainder: " + format(tempDividend))
    print("Quotient: " + format(Quot))

#Allows input
poly = True
while poly:
    coeffDividend = [float(x) for x in raw_input("Dividend : ").split()]
    coeffDivisor = [float(x) for x in raw_input("Divisor : ").split()]
    coeff(coeffDividend, coeffDivisor)

#Test Cases:
#coeff([3, -6, 2, 4], [-3, 1])
#coeff([12, -26, 21, -9, 2], [-3, 2])
#coeff([-1, 0, -7, 0, 10], [3, -1, 1])
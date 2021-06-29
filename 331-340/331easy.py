# https://www.reddit.com/r/dailyprogrammer/comments/6ze9z0/20170911_challenge_331_easy_the_adding_calculator/

#Depending on the type of math symbol, it will process that function
#The functions are: Addition, subtraction, multiply, divise, and exponent
def add_calc(equation):
    comp = equation.split()
    comp[0], comp[2] = int(comp[0]), int(comp[2])
    a, b = comp[0], comp[2]
    if comp[1] == '+':
        return addition(a, b)
    elif comp[1] == '-':
        return subtraction(a, b)
    elif comp[1] == '*':
        return multiply(a, b)
    elif comp[1] == '/':
        return divise(a, b)
    elif comp[1] == '^':
        return exponent(a, b)

#Simple. Just addition.
def addition(a, b):
    return a + b

#Uses addition via subtraction
def subtraction(a, b):
    return a + -b

#For every item in b, we add a
def multiply(a, b):
    multi = 0
    if a > b:
        a, b = b, a
    if a < 0 and b < 0:
        a, b = abs(a), abs(b)
    for i in range(b):
        multi += a
    return multi

#we multiply I and b until it reaches the height of A
def divise(a, b):
    if b > a and a > 0:
        return "Non-integral answer"
    elif b == 0:
        return "Not-defined"
    
    i = 0
    if a < 0 or b < 0:
        i = multiply(a, b)

    while multiply(i, b) != a:
        i += 1
        if i > abs(a):
            return "Non-integral answer"

    return i

#Using a while statement to keep multiplying
def exponent(a, b):
    if b < 0:
        return "Non-integral answer"
    expon = a
    i = 1
    if b == 0:
        return 1
    while i < b:
        expon = multiply(expon, a)
        i += 1
    return expon

#Program introduction
print("Welcome to mathcal culator")
print("Addition, multiplication, subtraction, division, and exponention are all valid inputs")
print("Example input: 4 * 4")
print("Do NOT forget the spaces!")
print("\n~*~----------------~*~\n")

#Quit case / run code
math_user = True
while math_user:
    problem = raw_input('')
    if problem == 'q' or problem == 'Q':
        math_user = False
        break
    print(add_calc(problem))
raw_input("Press enter to exit.")



#test cases
#37, 130, 27, -25, 125
#print(add_calc('12 + 25'))
#print(add_calc('100 - -30'))
#print(add_calc('9 * 3'))
#print(add_calc('75 / -3'))
#print(add_calc('5 ^ 3'))
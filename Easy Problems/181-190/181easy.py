# https://www.reddit.com/r/dailyprogrammer/comments/2h5b2k/09222014_challenge_181_easy_basic_equations/

def intersect(equation_1, equation_2):
    a1, b1 = parse(equation_1)
    a2, b2 = parse(equation_2)

    try:
        return int((b1 - b2) / (a2 - a1)), int((a2 * b1 - a1 * b2) / (a2 - a1))
    except ZeroDivisionError:
        return 'No intersection!'


def parse(equation):
    equation = equation.replace('y=', '')
    a, b = equation.split('x')

    if a == '':
        a = 1
    if b == '':
        b = 0

    return float(a), float(b)


# Input
print("This program will use basic equations.")
print("Input two, find out if there is an intersection")
print("\n~*~----------------~*~\n")

# Run code, instantiate class
program = True

while program:
    e1 = raw_input("First equation: ").lower()
    e2 = raw_input("Second equation: ").lower()
    if e1 == 'q' or e2 == 'q':
        break
    if 'y=' in e1 and 'y=' in e2:
        print(intersect(e1, e2))

raw_input("Press enter to exit.")
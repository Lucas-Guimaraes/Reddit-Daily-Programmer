# https://www.reddit.com/r/dailyprogrammer/comments/2451r5/4282014_challenge_160_easy_trigonometric_triangle/

import math


# https://www.omnicalculator.com/math/right-triangle-side-angle
# https://stackoverflow.com/questions/32980003/basic-trigonometry-isnt-working-correctly-in-python

def find_angle(a=0, b=0, c=0, A=0, B=0, C=90):
    if C != 90:
        C = 90

    A = float(A)
    B = float(B)
    a = float(a)
    b = float(b)
    c = float(c)

    a_B = [a, B, c]
    A_b = [A, b, c]
    sides = [a, b, c]

    if 0 in sides:
        # this is to find sides
        if a == 0 and b == 0 and c == 0:
            print("Sorry. I can't find a triangle with that knowledge!")
            return
        if len(set(sides)) == 3:
            if a == 0:
                a = math.sqrt((c ** 2) - b ** 2)
            elif b == 0:
                b = math.sqrt((c ** 2) - a ** 2)
            elif c == 0:
                c = math.sqrt((a ** 2) + b ** 2)

        elif len(set(a_B)) == 1:
            a = b * math.tan(math.radians(A))
            c = math.sqrt((a ** 2) + b ** 2)

        elif len(set(A_b)) == 1:
            b = a * math.tan(math.radians(B))
            c = math.sqrt((a ** 2) + b ** 2)

        elif c != 0:
            if A != 0:
                a = c * math.sin(math.radians(A))
                b = math.sqrt((c ** 2) - a ** 2)
            elif B != 0:
                b = c * math.sin(math.radians(B))
                a = math.sqrt((c ** 2) - b ** 2)

    # this finds our angles
    if A == 0 and B == 0:
        A = math.degrees(math.asin(a / c))
        B = math.degrees(math.asin(b / c))
    elif A == 0:
        A = 180 - C - B
    elif B == 0:
        B = 180 - C - A

    lst = [a, b, c, A, B, C]
    str_lst = ['a', 'b', 'c', 'A', 'B', 'C']

    for item in range(len(lst)):
        cur_item = round(lst[item], 2)
        if cur_item.is_integer():
            cur_item = int(cur_item)
        print(str_lst[item] + "=" + str(cur_item))
    return


def quit_check(i):
    if i == 'q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. This is not case sensitive: ").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
            return True
    return False

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

print("Hello! Welcome to trigonometry finder!")
print("You will give an input: The number 2, 3, or 4")
print("As soon as you give one of these, it will calculate the rest of the right triangle")
print("\nExample input:\n")
print("3")
print('a=3')
print('b=4')
print("\nExample output:\n")
print('a=3')
print('b=4')
print('c=5')
print('A=36.87')
print('B=53.13')
print('C=90')
print("\n~*~----------------~*~\n")

# digit_c = True
loopy = True
q_check = False
while loopy:

    if q_check == True:
        loopy = False
        break

    lines = True
    while lines:
        l_amt = raw_input("Please input how many numbers to give me - 2-4. 'q' to quit: ").replace(' ', '')
        q_check = quit_check(l_amt)
        if q_check == True:
            break
        if l_amt.isdigit():
            if 1 < int(l_amt) < 5:
                lines = False
                l_amt = int(l_amt)
            else:
                print("{} is not between 2 and 4!".format(l_amt))
        else:
            print("{} is not a valid digit!".format(l_amt))

    angle_dict = {}
    valid = ['a', 'b', 'c', 'A', 'B']

    if q_check == True:
        loopy = False
        break

    for i in range(l_amt):
        invalid = True
        if q_check == True:
            break

        while invalid:
            a_or_s = raw_input("Please put in an angle or side. 'q' to quit: ").replace(' ', '')
            q_check = quit_check(a_or_s)
            if q_check == True:
                break
            if '=' in a_or_s:
                k, v = a_or_s.split('=')
                if k in valid and isfloat(v):
                    if v.isdigit():
                        angle_dict[k] = int(v)
                    else:
                        angle_dict[k] = float(v)
                    invalid = False
                else:
                    print("{0} is an invalid input").format(a_or_s)
            else:
                print("Invalid input. You forgot an '='".format(a_or_s))

    if q_check == True:
        loopy = False
        break

    for k, v in angle_dict.items():
        if k in valid:
            valid.remove(k)

    for i in valid:
        angle_dict[i] = 0

    a_lst = [angle_dict['a'], angle_dict['b'], angle_dict['c'], angle_dict['A'], angle_dict['B']]

    find_angle(a_lst[0], a_lst[1], a_lst[2], a_lst[3], a_lst[4], 90)

raw_input("Press Enter to exit.")

# find_angle(3, 4, 5, 0, 0, 90)
# find_angle(0, 0, 5, 0, 53.13, 90)
# find_angle(0, 3, 0, 34, 0, 90)
# find_angle(0, 0, 3, 30, 0, 90)

# find_angle(3, 4, 0, 0, 0, 90)
# find_angle(0, 3, 8, 0, 34, 90)
# find_angle(2, 1, 0, 0, 4, 90)
# https://www.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/

# xb, yb = x box, y box
# xc, yc = x crate, crate sizes
# this program sees how many of xb/yb sized boxes we can fit into a xc/yc create
def fit1(xc, yc, xb, yb):
    x_boxes = 0
    y_boxes = 0

    #tests if the box height or length is larger than what can fit in the crate
    if xb > xc or yb > yc:
        return 0
    # keeps adding the number of boxes until the number becomes more than the crate size
    while xc >= x_boxes * xb:
        x_boxes += 1
    while yc >= y_boxes * yb:
        y_boxes += 1

    # times both box size
    return (x_boxes-1) * (y_boxes-1)

print("Welcome to box fitter!")
print("You will give two sets of two coordinates - a list of four numbers")
print("Example input: 10, 10, 1, 1")
print("The first two numbers will be how big your crate is")
print("The next two will be how big your boxes are")
print("So let's say your crate size is 4 by 4")
print("And your box size is 1 (x) by 2 (y)")
print("1 + 1 is equal to 2, lower than 4. Adding 1 would be 3")
print("The final 1 would be the maximum that we can reach.")
print("Now, for the Y axis")
print("2. Adding another crate would be 4, exactly at 4.")
print("Visualizing it...")
print("\nX filled in:\n")
print("0 0 0 0")
print("0 0 0 0")
print("0 0 0 0")
print("1 2 3 4")
print("\nY filled in:\n")
print("2 0 0 0")
print("2 0 0 0")
print("1 0 0 0")
print("1 0 0 0")
print("\nAll filled in:\n")
print('5 6 7 8')
print('5 6 7 8')
print('1 2 3 4')
print('1 2 3 4')
print("\n~*~----------------~*~\n")

box_check = True
while box_check:
    coordinates = raw_input("Please put in your coordinates. 'q' to quit: ").replace(',', '')

    if coordinates == 'q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. Non case sensitive.").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
            box_check = False
            continue
    coordinates = coordinates.split()
    if len(coordinates) != 4:
        print("{} is not a correct amount of coordinates".format(coordinates))

    valid_digit = True
    for s in coordinates:
        if s.isdigit() is False:
            print("{0} in {1} is not a valid digit!".format(s, coordinates))
            valid_digit = False
            break

    if valid_digit:
        co = [int(s) for s in coordinates]

    print(fit1(co[0], co[1], co[2], co[3]))

# print(fit1(10, 10, 1, 1))
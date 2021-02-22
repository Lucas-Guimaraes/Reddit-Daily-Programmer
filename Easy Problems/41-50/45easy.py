# https://www.reddit.com/r/dailyprogrammer/comments/sv6lw/4272012_challenge_45_easy/

# def printer(rows, cols, width, height, solid, blank):
# print (((solid * width + blank * width) * cols)[:cols * width]  + '\n') * height,
# if rows > 1: printer(rows - 1, cols, width, height, blank, solid)
# printer(5, 3, 2, 2, '#', ' ')

def grid(rows, cols, width, height, solid, blank):
    wall = ''
    if solid != '*':
        wall = '*'

    else:
        wall = '@'

    print(wall * (width * cols + 2))

    temp_row = rows
    star_print = True
    while temp_row > 0:
        if star_print:
            for i in range(height):
                print(wall + ((solid * width + blank * width) * cols)[:cols * width] + wall)
            star_print = False

        else:
            for i in range(height):
                print(wall + ((blank * width + solid * width) * cols)[:cols * width] + wall)
            star_print = True
        temp_row -= 1
        if temp_row > 0:
            print(wall * (width * cols + 2))
    print(wall * (width * cols + 2))


print("Welcome to Grid Maker!")
print("You will input four numbers and what you want your star to be")
print("~*~--------~*~")
r = int(raw_input("How many rows?: "))
c = int(raw_input("Now how many columns?: "))
w = int(raw_input("How much do you want the width?: "))
h = int(raw_input("Now how much do you want the height?: "))
s = raw_input("Finally, what do you want the stars to be?: ")
b = ' '
grid(r, c, w, h, s, b)


#grid(10, 10, 8, 3, '#', ' ')
raw_input("Press enter to exit.")
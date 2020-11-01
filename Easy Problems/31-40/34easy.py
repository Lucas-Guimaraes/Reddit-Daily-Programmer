#https://www.reddit.com/r/dailyprogrammer/comments/rmmn8/3312012_challenge_34_easy/

#makes the list
int_list = raw_input("Give me three numbers; put a space in-between each ")
numbers = map(int, int_list.split())
#checks if Z is the lowest, then Y
#if none, moves to Z
def sum_of_highest(x, y, z):
    if z < x and z < y:
        sum_of_squares = (x**2) + (y**2)
    elif y < x and y < z:
        sum_of_squares = (x**2) + (z**2)
    else:
        sum_of_squares = (y**2) + (z**2)
    return sum_of_squares

print(sum_of_highest(numbers[0], numbers[1], numbers[2]))
raw_input("Press enter to exit")
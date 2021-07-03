# https://www.reddit.com/r/dailyprogrammer/comments/4dccix/20160404_challenge_261_easy_verifying_3x3_magic/

#checks if the list we put in is a magic square
def magic_square(lst):
    lst = lst.split(',')

    print(lst)
    #checks every row, followed by diagonals, then columns
    if check_15(lst[0], lst[1], lst[2]) \
            and check_15(lst[3], lst[4], lst[5]) \
            and check_15(lst[6], lst[7], lst[8]) \
            and check_15(lst[0], lst[4], lst[8]) \
            and check_15(lst[2], lst[4], lst[6]) \
            and check_15(lst[0], lst[3], lst[6]) \
            and check_15(lst[1], lst[4], lst[7]) \
            and check_15(lst[2], lst[5], lst[8]):
        return True
    else:
        return False

#Checks if all numbers add up to be 15.
def check_15(a, b, c):
    if int(a) + int(b) + int(c) == 15:
        return True
    else:
        return False


three_square = raw_input()
print(magic_square(three_square))

#Test cases:
#[8, 1, 6, 3, 5, 7, 4, 9, 2] 
#[2, 7, 6, 9, 5, 1, 4, 3, 8] 
#[3, 5, 7, 8, 1, 6, 4, 9, 2] 
#[8, 1, 6, 7, 5, 3, 4, 9, 2]
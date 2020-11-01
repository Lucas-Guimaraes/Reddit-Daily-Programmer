# https://www.reddit.com/r/dailyprogrammer/comments/rr4y2/432012_challenge_35_easy/

# i don't even know how much of this other stuff is needed
tri_size = int(raw_input("How large do you want your triangle?: "))


def make_row(tri):
    r_count = 0
    while r_count < tri:
        r_count += 1
        tri -= r_count
    return r_count


def make_setup(tri):
    rows = make_row(tri)
    new_count = 0
    for i in range(1, rows + 1):
        new_count += i
    return rows, new_count


def make_triangle(tri):
    rows, num = make_setup(tri)
    num_lst = range(1, num + 1)
    while rows > 0:

        new_lst = []
        for i in range(1, rows + 1):
            new_lst.append(num_lst[-1])
            num_lst.pop()
        new_lst.reverse()
        print('')
        print(' '.join("{0}".format(n) for n in new_lst))
        rows -= 1


make_triangle(tri_size)
print('')
raw_input("Press enter to exit")
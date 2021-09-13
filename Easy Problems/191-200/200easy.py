#https://www.reddit.com/r/dailyprogrammer/comments/2ug3hx/20150202_challenge_200_easy_floodfill/

#'floodfill.txt' is a supplementary file
#Code could be better; a bit of brute force involved

f = open("floodfill.txt", "r")
first = (f.readline()).split()
second = (f.readline()).split()

width, height = int(first[0]), int(first[1])
y, x, replace_char = int(second[0]), int(second[1]), second[2]

lst = []
for i in f.readlines():
    i = i.replace('\n', '')
    lst.append(list(i))

#dirs = ([0, 1], [0, -1], [1, 0], [-1, 0])

#Storing variables
lst[x][y] = replace_char
travelled = [[x, y]]
traversing = True

#Storing directions
west, east, north, south = [x, y+1], [x, y-1], [x-1, y], [x+1, y]
nw, ne, sw, se = True, True, True, True
xdir, ydir = x, y

while traversing:
    #West Direction
    if lst[west[0]][west[1]] != '#' and west not in travelled:
        travelled.append(west)
        lst[west[0]][west[1]] = replace_char
        west = [west[0], west[1]+1]

    #East Direction
    elif lst[east[0]][east[1]] != '#' and east not in travelled:
        travelled.append(east)
        lst[east[0]][east[1]] = replace_char
        east = [east[0], east[1] - 1]

    #North Direction
    elif lst[north[0]][north[1]] != '#' and north not in travelled:
        travelled.append(north)
        lst[north[0]][north[1]] = replace_char
        north = [north[0]-1, north[1]]

    #South Direction
    elif lst[south[0]][south[1]] != '#' and south not in travelled:
        travelled.append(south)
        lst[south[0]][south[1]] = replace_char
        south = [south[0]+1, south[1]]

    #Northwest check
    elif nw:
        xdir -= 1
        ydir += 1
        if lst[xdir][ydir] != '#' and [xdir, ydir] not in travelled:
            travelled.append([xdir, ydir])
            lst[xdir][ydir] = replace_char

        w_test = lst[xdir][ydir + 1] == '#' or [xdir, ydir + 1] in travelled
        e_test = lst[xdir][ydir - 1] == '#' or [xdir, ydir - 1] in travelled
        n_test = lst[xdir - 1][ydir] == '#' or [xdir - 1, ydir] in travelled
        s_test = lst[xdir + 1][ydir] == '#' or [xdir + 1, ydir] in travelled

        if lst[xdir][ydir] == '#' or (w_test and e_test and n_test and s_test):
            nw = False
            xdir, ydir = x, y

        west, east, north, south = [xdir, ydir + 1], [xdir, ydir - 1], [xdir - 1, ydir], [xdir + 1, ydir]

    #Northeast check
    elif ne:
        xdir -= 1
        ydir -= 1
        if lst[xdir][ydir] != '#' and [xdir, ydir] not in travelled:
            travelled.append([xdir, ydir])
            lst[xdir][ydir] = replace_char

        w_test = lst[xdir][ydir + 1] == '#' or [xdir, ydir + 1] in travelled
        e_test = lst[xdir][ydir - 1] == '#' or [xdir, ydir - 1] in travelled
        n_test = lst[xdir - 1][ydir] == '#' or [xdir - 1, ydir] in travelled
        s_test = lst[xdir + 1][ydir] == '#' or [xdir + 1, ydir] in travelled

        if lst[xdir][ydir] == '#' or (w_test and e_test and n_test and s_test):
            ne = False
            xdir, ydir = x, y

        west, east, north, south = [xdir, ydir + 1], [xdir, ydir - 1], [xdir - 1, ydir], [xdir + 1, ydir]

    #Southwest check
    elif sw:
        xdir += 1
        ydir -= 1
        if lst[xdir][ydir] != '#' and [xdir, ydir] not in travelled:
            travelled.append([xdir, ydir])
            lst[xdir][ydir] = replace_char

        w_test = lst[xdir][ydir + 1] == '#' or [xdir, ydir + 1] in travelled
        e_test = lst[xdir][ydir - 1] == '#' or [xdir, ydir - 1] in travelled
        n_test = lst[xdir - 1][ydir] == '#' or [xdir - 1, ydir] in travelled
        s_test = lst[xdir + 1][ydir] == '#' or [xdir + 1, ydir] in travelled

        if lst[xdir][ydir] == '#' or (w_test and e_test and n_test and s_test):
            sw = False
            xdir, ydir = x, y

        west, east, north, south = [xdir, ydir + 1], [xdir, ydir - 1], [xdir - 1, ydir], [xdir + 1, ydir]

    #Southeast check
    elif se:
        xdir += 1
        ydir += 1
        if lst[xdir][ydir] != '#' and [xdir, ydir] not in travelled:
            travelled.append([xdir, ydir])
            lst[xdir][ydir] = replace_char

        w_test = lst[xdir][ydir + 1] == '#' or [xdir, ydir + 1] in travelled
        e_test = lst[xdir][ydir - 1] == '#' or [xdir, ydir - 1] in travelled
        n_test = lst[xdir - 1][ydir] == '#' or [xdir - 1, ydir] in travelled
        s_test = lst[xdir + 1][ydir] == '#' or [xdir + 1, ydir] in travelled

        if lst[xdir][ydir] == '#' or (w_test and e_test and n_test and s_test):
            se = False
            xdir, ydir = x, y

        west, east, north, south = [xdir, ydir + 1], [xdir, ydir - 1], [xdir - 1, ydir], [xdir + 1, ydir]

    #If no more directions, finish
    else:
        break

#Print
for i in lst:
    print(''.join(i))
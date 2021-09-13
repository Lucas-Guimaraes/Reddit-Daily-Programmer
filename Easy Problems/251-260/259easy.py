# https://www.reddit.com/r/dailyprogrammer/comments/4bc3el/20160321_challenge_259_easy_clarence_the_slow/


coor = {"1": [0, 0], "2": [0, 1], "3": [0, 2],
        "4": [1, 0], "5": [1, 1], "6": [1, 2],
        "7": [2, 0], "8": [2, 1], "9": [2, 2],
        ".": [3, 0], "0": [3, 1]}


def clarence_typist(ip):
    total = 0
    pos = ip[0]
    for i in xrange(len(ip) - 1):
        x1, y1 = coor[ip[i]][0], coor[ip[i]][1]
        x2, y2 = coor[ip[i+1]][0], coor[ip[i+1]][1]

        total += ((x2-x1)**2+(y2-y1)**2) ** .5
    return "{}cm total".format(round(total, 2))

print("Welcome to clarence typer!")
print("You will give an input: an IP address")
print("The output will be how long Clarence's sole finger travels")
print("\n~*~----------------~*~\n")

typing = True
while typing:
    x = raw_input()
    if x == 'Q' or x == 'q':
        break
    print(clarence_typist(x))
print("Press enter to exit")

#test case
#print(clarence_typist('219.45.143.143'))
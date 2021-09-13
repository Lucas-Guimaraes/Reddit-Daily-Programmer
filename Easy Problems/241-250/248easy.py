#https://www.reddit.com/r/dailyprogrammer/comments/3zfajl/20160104_challenge_248_easy_draw_me_like_one_of/

def bitmap_draw(w, h, inputs):
    #Makes grid map to paste over
    grids = []
    for x in range(h):
        new = []
        for i in range(w):
            new.append([0, 0, 0])
        grids.append(new)

    #Draws out for each inserted
    for x in inputs:
        if x[0] == 'point':
            grids[x[4]][x[5]][0] = x[1]
            grids[x[4]][x[5]][1] = x[2]
            grids[x[4]][x[5]][2] = x[3]


        if x[0] == 'line':
            #Loops over the line point
            for i in range(x[5], x[6]+1):

                grids[x[4]][i][0] = x[1]
                grids[x[4]][i][1] = x[2]
                grids[x[4]][i][2] = x[3]

        if x[0] == 'rect':
            #Loops over all the square points
            for xdir in range(x[4], x[5]+1):
                for ydir in range(x[6], x[7]+1):
                    grids[xdir][ydir][0] = x[1]
                    grids[xdir][ydir][1] = x[2]
                    grids[xdir][ydir][2] = x[3]

    #For every grid line, print the line
    for grid in grids:
        new = ""
        for g in grid:
            new += "".join(str(g))
            new += "   "
        print(new.translate(None, "[],"))

#line: Row, followed by x begin and x end
#rect: x, y, rx, ry

bitmap_draw(5, 3, [['point', 0, 0, 255, 0, 0], ['line', 100, 100, 100, 0, 2, 4], ['rect', 77, 0, 0, 1, 2, 3, 4]])
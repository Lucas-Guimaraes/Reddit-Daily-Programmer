#https://www.reddit.com/r/dailyprogrammer/comments/3ltee2/20150921_challenge_233_easy_the_house_that_ascii/

#Various test cases; feel free to go with whichever fits

lst = ['   *  ', '  *** ', '******']
#lst = [' * ', '***', '***', '***', '***', '***', '***',]
#lst = ['    **', '*** **', '******']
top = "+---+"
mid = "|   |"
bot = "+---+"
box = [top, mid, bot]
top_roof = "  A  "
mid_roof = """ / \\ """
bottom_roof = """/   \\"""
roof = [top_roof, mid_roof, bottom_roof]
spacing = "     "
space = [spacing, spacing, spacing]

floors = [0 for i in range(len(lst)+1)]

for i in range(len(lst)+1):
    floor = []
    if i == 0:
        for x in lst[0]:
            if x == ' ':
                floor.append(space)
            else:
                floor.append(roof)
    else:
        for x in range(len(lst[i-1])):
            if lst[i-1][x] == ' ' and  lst[i][x] == ' ':
                floor.append(space)
            elif lst[i-1][x] == ' ':
                floor.append(roof)
            else:
                floor.append(box)
    floors[i] = floor

for floor in floors:
    for x in range(3):
        new_line = ''
        for i in range(len(floor)):
            new_line += floor[i][x]
        print(new_line)

#print(floors)
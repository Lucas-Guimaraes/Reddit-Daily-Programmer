#https://www.reddit.com/r/dailyprogrammer/comments/6qutez/20170801_challenge_325_easy_color_maze/

def color_maze(pattern, maze, start):
    start_pattern = 1
    end_pattern = len(pattern)
    cur_row = len(maze)-1
    points = []
    points.append(start)

    while cur_row >= 1:
        if start_pattern >= end_pattern:
            start_pattern = 0
        cur = points[-1]

        n_valid, w_valid, e_valid = len(maze) > cur[0]-1 > -1, len(maze) > cur[1] - 1 > -1, len(maze) > cur[1] + 1 > -1
        #Check North
        if n_valid and (cur[0]-1, cur[1]) not in points:
            if pattern[start_pattern] == maze[cur[0]-1][cur[1]]:
                points.append((cur[0]-1, cur[1]))
                cur_row -= 1
                start_pattern += 1
                continue

        # Check West
        if w_valid and (cur[0], cur[1]-1) not in points:
            if pattern[start_pattern] == maze[cur[0]][cur[1]-1]:
                points.append((cur[0], cur[1]-1))
                start_pattern += 1
                continue

        # Check East
        if e_valid and (cur[0], cur[1]+1) not in points:
            if pattern[start_pattern] == maze[cur[0]][cur[1]+1]:
                points.append((cur[0], cur[1]+1))
                start_pattern += 1
                continue

        else:
            break


    maze_final = [['/' for i in range(len(maze))] for x in range(len(maze))]



    for point in points:
        maze_final[point[0]][point[1]] = maze[point[0]][point[1]]
    for m in maze_final:
        print(''.join(m))
    points = [(p[1], p[0]) for p in points]
    print('')
    for point in points:
        print(point)


start = (4, 1)
pattern = ['O', 'G']
maze = [
	'B O R O Y'.split(),
	'O R B G R'.split(),
	'B O G O Y'.split(),
	'Y G B Y G'.split(),
	'R O R B R'.split()
]

color_maze(pattern, maze, start)
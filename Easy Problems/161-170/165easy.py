# https://www.reddit.com/r/dailyprogrammer/comments/271xyp/622014_challenge_165_easy_ascii_game_of_life/

# ascii_game_of_life

#Organizes text file
f = open("165easy.txt", "r")

sheet = []

for line in f.readlines():
    sheet.append(line.replace("\n", ""))


#for every game_of_life state, this runs the states
def game_of_life(lst, states, width, height):
    for i in range(states):
        lst = gol_state(lst, width, height)
    for l in lst:
        print(l)

#Checks all neighboring cells
def matrix(lst, max_row, max_col, cur_row, cur_col):

    check = [[cur_row - 1, cur_col - 1], [cur_row - 1, cur_col], [cur_row - 1, cur_col + 1], [cur_row, cur_col - 1],
             [cur_row, cur_col + 1], [cur_row + 1, cur_col - 1], [cur_row + 1, cur_col], [cur_row + 1, cur_col + 1]]
    m_result = ''

    #Used to check if the column and row generated is on the grid
    for i in range(8):
        if max_row > check[i][0] >= 0 and max_col > check[i][1] >= 0:
            m_result += lst[check[i][0]][check[i][1]]
    return m_result

#Runs for each Game of Life state
def gol_state(lst, w, h):
    gol_lst = []
    count = 0
    #Makes the new lst
    for row in range(w):
        for col in range(h):
            temp_str = ''
            temp_str += matrix(lst, w, h, row, col)
            if temp_str.count('#') == 3 and lst[row][col] == '.':
                gol_lst.append('#')
            elif temp_str.count('#') < 2 or temp_str.count('#') > 3 and lst[row][col] == '#':
                gol_lst.append('.')
            else:
                gol_lst.append(lst[row][col])

    #Slices list properly
    count = 0
    new_gol_lst = []
    gol_str = ''
    
    for x in range(len(gol_lst)):
        count += 1
        gol_str += gol_lst[x]
        if count % h == 0:
            new_gol_lst.append(gol_str)
            gol_str = ''
    return new_gol_lst

#file, states, width, height
game_of_life(sheet, 7, 10, 10)
raw_input()
#https://www.reddit.com/r/dailyprogrammer/comments/1rdtky/111113_challenge_142_easy_falling_sand/
#'124easysand.txt' is the supplementary file. This file may be changed

def falling_sand(file, num):
    hourglass = open(file, 'r')
    rows = []
    #creates our rows based on the amount of lines
    for row in hourglass.readlines():
        temp_row = row.replace("\n", "")
        temp_row = list(temp_row)
        rows.append(temp_row)
    
    #creates our columns. Based on the input about the number of columns
    columns = []
    for column in range(num):
        temp_col = []
        for row in range(num):
            temp_col.append(rows[row][column])
        
        columns.append(temp_col)
    
    #moves sand
    columns_moved = []
    for column in columns:
        new_col = column
        new_col.pop(0)
        new_col.insert(0, '!')
        
        #This swaps around any ' ' spots in the row to be filled
        for row in range(1, num):
            if column[row] == ' ':
                new_col[row], new_col[row-1] = new_col[row-1], new_col[row]
            else:
                break
       
        new_col_idx = new_col.index("!")
        new_col.pop(new_col_idx)
        new_col.insert(new_col_idx, ".")
        columns_moved.append(new_col)
    
    #converts columns to rows
    #Since right now, the whole lists are inside other lists
    rows_moved = []
    for column in range(num):
        temp_col = columns_moved[column]
        temp_row = []
        for row in range(num):
            temp_row.append(columns_moved[row][column])
        rows_moved.append(temp_row)
        
    #prints each row at a time
    for row in rows_moved:
        row_str = "".join(row)
        print(row_str)
        
sand_file = '142easysand.txt'
falling_sand(sand_file, 5)

raw_input()
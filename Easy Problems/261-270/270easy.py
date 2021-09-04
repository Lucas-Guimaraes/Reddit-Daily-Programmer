#https://www.reddit.com/r/dailyprogrammer/comments/4msu2x/challenge_270_easy_transpose_the_input_text/

def input_transpose(matrix_list, j):
    future_row_size = len(matrix_list)
    future_col_size = len(matrix_list[0])

    new_lst = []

    #Loops over future column size, then future row
    #Grabs the item and appends from temp list into perm list
    for x in range(future_col_size):
        new_temp = []
        for y in range(future_row_size):
            new_temp.append(matrix_list[y][x])

        if j:
            new_lst.append(' '.join(new_temp))
        else:
            new_lst.append(''.join(new_temp))

    #Prints from perm list
    for x in new_lst:
        print(x)

#test cases
input_transpose([['S', 'o', 'm', 'e', ' '], ['t', 'e', 'x', 't', '.']], False)
print("")
input_transpose([["A", " ", "B", " ", "C"], ["D", " ", "E", " ", "F"]], True)
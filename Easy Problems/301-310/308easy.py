#https://www.reddit.com/r/dailyprogrammer/comments/61ub0j/20170327_challenge_308_easy_let_it_burn/

#Makes items into list
def make_list(s):
    return [i for i in s]

#Makes matrix
def let_it_burn(matrix, i_lst):
    final_matrix = matrix
    for i in i_lst:
        
        #Checking if S or F
        if matrix[i[1]][i[0]] == "S":
            matrix[i[1]][i[0]] = "F"
            
            #Vertical replacement
            if matrix[i[1] + 1][i[0]] == "S":
                matrix[i[1] + 1][i[0]] = "F"
            if matrix[i[1] - 1][i[0]] == "S":
                matrix[i[1] - 1][i[0]] = "F"

        elif matrix[i[1]][i[0]] == " ":
            matrix[i[1]][i[0]] = "S"
        
        #Type conversion for checking horizontally
        for m in range(len(matrix)):
            if "SF" in "".join(matrix[m]):
                final_matrix[m] = "".join(matrix[m]).replace("SF", "FF")
            if "FS" in "".join(matrix[m]):
                final_matrix[m] = "".join(matrix[m]).replace("FS", "FF")
            if "S_F" in "".join(matrix[m]):
                final_matrix[m] = "".join(matrix[m]).replace("S_F", "F_F")
            if "F_S" in "".join(matrix[m]):
                final_matrix[m] = "".join(matrix[m]).replace("F_S", "F_F")
            if type(final_matrix[m]) != 'list':
                final_matrix[m] = make_list(final_matrix[m])

    for i in final_matrix:
        print(''.join(i))


burn_matrix = [make_list("#############/#"), make_list("#     |       #"), make_list("#     #       #"), make_list("#     #       #"), make_list("#######       #"), make_list("#     _       #"), make_list("###############")]a

lst = [[1, 1], [1, 2], [1, 3], [5, 6], [4, 2], [1, 1], [1, 2], [5, 5], [5, 5], [9, 1], [7, 5], [2, 2]]
#lst = [[0, 0], [0, 1], [0, 2], [4, 5], [3, 1], [0, 0], [0, 1], [4, 4], [4, 4], [8, 0], [4, 6], [1, 1]]

let_it_burn(burn_matrix, lst)
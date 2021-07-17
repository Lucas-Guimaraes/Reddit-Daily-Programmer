#rotates the matrix
def rotate_90(arr):
    n = len(arr)
    super_lst = []
    for j in range(n):
        temp_lst = []
        for i in range(n - 1, -1, -1):
            temp_lst.append(arr[i][j])
        super_lst.append(temp_lst)
    return super_lst

#Matrix, followed by how many repeats
matrix = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

repeats = raw_input("How many times would you like to rotate the data set?: ")
print("\n~*~----------------~*~\n")

#For every rotation
for i in range(int(repeats)):
    matrix = rotate_90(matrix)

#For each line in the finalized matrix, print
for line in matrix:
    temp_line = line
    temp_line = [str(n) for n in temp_line]
    temp_line = " ".join(temp_line)
    print(temp_line)

#Exit code
raw_input("\nPress enter to exit.")
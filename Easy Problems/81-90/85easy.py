#https://www.reddit.com/r/dailyprogrammer/comments/xq0yv/832012_challenge_85_easy_rowcolumn_sorting/
#'85easy-test.txt' is a supplementary file; intentionally made blank

matrix_file = open('85easy-test.txt', 'r+')
matrix_file.truncate(0)

def matrix_organizer(file, column_len):
    file = open(file, 'r+')
    matrix_old = []
    matrix = []
    
    for line in file.readlines():
        row = []
        temp_line = line
        temp_line = temp_line.replace("\n", "")
        row.append(temp_line)
        matrix_old.append(row)
    
    for line in matrix_old:
        temp_row = str(line)
        temp_row = temp_row.replace(']', '')
        temp_row = temp_row.replace('[', '')
        temp_row = temp_row.replace('"', '')
        temp_row = temp_row.replace("""'""", '')
        temp_row = temp_row.split()
        row_append = []
        
        for i in temp_row:
            row_append.append(int(i))
        matrix.append(row_append)
    
    sum_of_rows = []
    rows = {}

    for row in matrix:
        sum_of_rows.append(sum(row))
        value_row = str(sum(row))
        rows[value_row] = row
        #temporarily here for checking dupes:
#        if value_row in rows.keys():
#            rows[value_row].append(row)
#        else:
#            rows[value_row] = row
        
    sum_of_columns = []
    columns = {}
    for column in range(column_len):
        total = 0
        temp_col = []
        for row in matrix:
            total += row[column]
            temp_col.append(row[column])
        sum_of_columns.append(total)
        columns[str(total)] = temp_col
        
        #temporarily here for checking dupes
        #if str(total) in columns.keys():
        #    columns[str(total)].append(temp_col)
        #else:
        #   columns[str(total)] = temp_col
        
    #print(columns)
    print("\nSum of each row:")
    print(sum_of_rows)
    print("\nSum of each column:")
    print(sum_of_columns)
    
    sum_of_rows.sort()
    print("\nMatrix sorted by Row sums:")
    
    for i in sum_of_rows:
        print_row = rows[str(i)]
        print_row = str(print_row)
        print_row = print_row.replace('[', '')
        print_row = print_row.replace(']', '')
        print_row = print_row.replace(',', '')
        print_row = print_row.replace("""'""", '')
        print(print_row)
    
    sum_of_columns.sort()
    
    
    print("\nMatrix sorted by Column sums:")
    
    
    for column in range(len(sum_of_rows)):
        temp_row = []
        
        for i in sum_of_columns:
           
            temp_num = columns.get(str(i))            
            temp_row.append(temp_num[column])
        print_row = str(temp_row)
        print_row = print_row.replace('[', '')
        print_row = print_row.replace(']', '')
        print_row = print_row.replace(',', '')
        print_row = print_row.replace("""'""", '')
        print(print_row)
    
    
    file.close()
    return
    
print("*--------*--------*")
print("Hello! Welcome to Matrix. ")
print("*--------*--------*")
raw_input("Press Enter to Continue")

print("*--------*--------*")
print("This application takes one input - a list of digits")
print("You put spaces in each one")
print("Each list MUST be equally sized")
print("Example of Valid Input:")
print("""       40 39 20
20 30 10
5 10 69""")
print("Example of invalid input:")
print("""       40 420
    41 2 5 430""")
print("*--------*--------*")
raw_input("Press Enter to Continue")

print("*--------*--------*")
print("Please give me a matrix. Press '/s' to finish your matrix")
print("*--------*--------*")

matrix_loop = True
matrix_len = 0
line_count = 0

while matrix_loop:
    
    list_file = raw_input()
    list_file = list_file.split(" ")
    new_list_file = []
    list_string = ''
    
    if '/s' in list_file:
        matrix_loop = False
        break
    for i in list_file:
        if line_count == 0:
            matrix_len = len(list_file)
        elif line_count > 0:
            if len(list_file) != matrix_len:
                print("Something isn't right!")
                break
        try:
            int(i)
            new_list_file.append(i)
            
        except:
            print("Something isn't right!")
            if line_count == 1:
                line_count = 0
            break
        
    
    list_string = " ".join(new_list_file)
    
    if len(list_string) > 0:
        line_count += 1
        list_string += "\n"
        matrix_file.write(list_string)
        


file_name = matrix_file.name
matrix_file.close()

matrix_organizer(file_name, matrix_len)

print("\n")
print("*--------*--------*")
print("Those are your results!")
print("\n")
raw_input("Press Enter to Exit!")


#last_line = matrix_file.readline()[-1]
#del matrix_file[-1]
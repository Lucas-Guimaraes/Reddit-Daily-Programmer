#https://www.reddit.com/r/dailyprogrammer/comments/6v29zk/170821_challenge_328_easy_latin_squares/

#Checks if Latin Square
def latin_square(arr):
    #Makes initial set and columns
    s = set(arr[0])
    col = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]

    #Form list to check for duplicates
    lst = []
    lst.append(arr[0])
    lst.append(col[0])

    #Checks the initial list
    if s != set(lst[1]):
        return False

    #Checks every every array and column
    for i in range(1, len(arr)):
        if set(arr[i]) != s  or set(col[i]) != s or arr[i] in lst:
            return False
        lst.append(arr[i])
        lst.append(col[i])
    return True

#test cases
#print(latin_square([['1', '2', '3'], ['3', '1', '2'], ['2', '3', '1']]))
#print(latin_square([['1', '3'], ['3', '4']]))
#print(latin_square([['1', '2', '3', '4'], ['1', '3', '2', '4'], ['2', '3', '4', '1'], ['4', '3', '2', '1']]))
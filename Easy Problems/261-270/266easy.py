#https://www.reddit.com/r/dailyprogrammer/comments/4ijtrt/20160509_challenge_266_easy_basic_graph/

def solve(x, m):
    lst = []
    already_travelled = []

    #Makes the initial blank list of nodes
    for i in range(1, x+1):
        lst.append([i, 0])

    for l in m:
        #If we visited a variation of the node, don't add it
        if l not in already_travelled:
            #Add to both the node counts
            lst[l[0] - 1][1] += 1
            lst[l[1] - 1][1] += 1
            already_travelled.append([l[0], l[1]])
            already_travelled.append([l[1], l[0]])

    #Print
    for l in lst:
        print("Node {} has a degree of {}".format(l[0], l[1]))

#Test cases
#n = 5
#matrix = [[1, 2], [1, 3], [3, 1], [4, 1], [5, 1], [5, 3]]
#solve(5, matrix)

n = 16
matrix = [[1, 2], [1, 3], [2, 3], [1, 4], [3, 4], [1, 5], [2, 5], [1, 6], [2, 6], [3, 6], [3, 7], [5, 7], [6, 7], [3, 8], [4, 8], [6, 8], [7, 8], [2, 9], [5, 9], [6, 9], [2, 10], [9, 10], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11], [1, 12], [6, 12], [7, 12], [8, 12], [11, 12], [6, 13], [7, 13], [9, 13], [10, 13], [11, 13], [5, 14], [8, 14], [12, 14], [13, 14], [1, 15], [2, 15], [5, 15], [9, 15], [10, 15], [11, 15], [12, 15], [13, 15], [1, 16], [2, 16], [5, 16], [6, 16], [11, 16], [12, 16], [13, 16], [14, 16], [15, 16]]

solve(n, matrix)
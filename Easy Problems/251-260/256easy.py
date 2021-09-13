#https://www.reddit.com/r/dailyprogrammer/comments/48a4pu/20160229_challenge_256_easy_oblique_and_deoblique/
import itertools

#Test input
tri = [0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29], [30, 31, 32, 33, 34, 35]

#Grabs all index combinations for current triangle
def find_idx(n):
    num = range(n) + range(n)
    result = [seq for seq in itertools.permutations(num, 2) if sum(seq) == n]
    result.append((0, n))
    result.append((n, 0))
    return result

def oblique(matrix):
    col = len(matrix)
    lst = []

    #Grabs combinations, inputs them, saves them to list
    for i in range((col*2)-1):
        new_lst = []
        passed_combs = []

        l = find_idx(i)
        for p in l:
            if p[0] < col and p[1] < col and p not in passed_combs:
                new_lst.append(str(matrix[p[0]][p[1]]))
                passed_combs.append(p)
        lst.append(" ".join(new_lst))

    #Print list
    for i in lst:
        print(i)

oblique(tri)
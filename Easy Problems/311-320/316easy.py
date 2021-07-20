#https://www.reddit.com/r/dailyprogrammer/comments/6coqwk/20170522_challenge_316_easy_knights_metric/

from collections import deque

def knight_metric(a, b):
    root = (0, 0)
    moves = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, -1), (2, -1), (-2, 1), (2, 1)]

    #Sets up visited to our set, deque for  a quicker list
    visited = set([root])
    queue = deque([(root, 0)])

    while queue:
        #Get our current X and Y, along with depth
        (x, y), depth = queue.popleft()
        #If equal, breaks
        if (a, b) == (x, y):
            return depth

        for (xp, yp) in moves:
            next = (x + xp, y + yp)
            #Add Depth +1, and add the spots
            if next not in visited:
                queue.append((next, depth + 1))
                visited.add(next)

#Checks if negative or positive number
def is_number(n):
    pos_test = n.isdigit()
    neg_test = n[1:].isdigit()
    if pos_test or neg_test:
        return True

#Introduction text
print("Welcome to Knight Route")
print("Insert an x and y input for an infinite board for our knight")
print("Example input:")
print("5 56")
print("\n~*~----------------~*~\n")

# Checks input, quit case included

bfs_algorithm = True

while bfs_algorithm:
    n = raw_input()
    if n.lower() == 'q':
        break
    n = n.split()
    x, y = n[0], n[1]
    if is_number(x) and is_number(y):
        print(knight_metric(int(x), int(y)))

raw_input("Press enter to exit.")

#Test case
#print(knight_metric(3, 7))
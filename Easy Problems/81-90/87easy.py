# https://www.reddit.com/r/dailyprogrammer/comments/y26pr/8102012_challenge_87_easy_rectangle_intersection/

#Program that checks the triangles
def intersect(rect_1, rect_2):

    #computes first axis
    fx1 = rect_1[0]
    fy1 = rect_1[1]
    fx2 = rect_1[2]
    fy2 = rect_1[3]
    #computes second axis
    sx1 = rect_2[0]
    sy1 = rect_2[1]
    sx2 = rect_2[2]
    sy2 = rect_2[3]
    
    #Checks if both x axies are not in range
    if (fx1 not in range(sx1, sx2)) and (sx1 not in range(fx1, fx2)):
        return None

    #Checks if both y axieses are not in range
    if (fy1 not in range(sy1, sy2)) and (sx1 not in range(fy1, fy2)):
        return None

    else:

        return(max(fx1, sx1),
               max(fy1, sy1),
               min(fx2, sx2),
               min(fy2, sy2))

#Test cases
print(intersect([3, 3, 10, 10], [6, 6, 12, 12]))
print(intersect([4, 4, 5, 5], [6, 6, 10, 10])) #returns none
print(intersect([1, 1, 4, 4], [8, 8, 5, 5])) #returns none
print(intersect([1, 1, 4, 4], [2, 2, 5, 5]))
print(intersect([1, 1, 4, 4], [2, 2, 3, 5]))
print(intersect([1, 1, 4, 4], [2, 2, 5, 3]))
print(intersect([1, 1, 4, 4], [2, 2, 3, 3]))
print(intersect([1, 1, 4, 4], [0, 0, 5, 5]))
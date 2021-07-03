#https://www.reddit.com/r/dailyprogrammer/comments/5bn0b7/20161107_challenge_291_easy_goldilocks_bear/

#Checks all valid chairs
def valid_chairs(weight, temp, lsts):
    valid = []
    #For every item in range
    for i in range(len(lsts)):
        if weight < lsts[i][0] and temp > lsts[i][1]:
           new = str(i+1)
           valid.append(new)
    return ' '.join(valid)

#Test case
print(valid_chairs(100, 80, [[30, 50], [130, 75], [90, 60], [150, 85], [120, 70]]))
raw_input()
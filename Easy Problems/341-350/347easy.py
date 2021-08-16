#https://www.reddit.com/r/dailyprogrammer/comments/7qn07r/20180115_challenge_347_easy_how_long_has_the/
def light_length(light):
    time_list = []
    for i in light:
        for x in range(i[0], i[1]):
            if x not in time_list:
                time_list.append(x)
    return len(time_list)

#Test Cases
print(light_length([[1,3],[2,3],[4,5]]))
print(light_length([[2,4],[3,6],[1,3],[6,8]]))
print(light_length([[6,8],[5,8],[8,9],[5,7],[4,7]]))
print(light_length([[15,18],[13,16],[9,12],[3,4],[17,20],[9,11],[17,18],[4,5],[5,6],[4,5],[5,6],[13,16],[2,3],[15,17],[13,14]]))
#https://www.reddit.com/r/dailyprogrammer/comments/4q35ip/20160627_challenge_273_easy_getting_a_degree/

#can also be done via 180 / math.pi for r -> 
#or math/.pi / 180 to d -> r

import math

def degrees_radians(dr):
    if dr[-1] == "d":
        return math.degrees(float(dr[:len(dr)-2]))
    else:
        return math.radians(float(dr[:len(dr)-2]))

print(degrees_radians("3.1416rd"))
print(degrees_radians("90dr"))
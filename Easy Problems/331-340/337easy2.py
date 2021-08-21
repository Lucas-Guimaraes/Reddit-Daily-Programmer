#https://www.reddit.com/r/dailyprogrammer/comments/784fgr/20171023_challenge_337_easy_minimize_maximize/

from math import sqrt

a = [0,20]
b = [100,30]
p = [a[0] + .001, 0]

dist = sqrt((p[0])** 2 + (a[1]+p[1])**2) + sqrt((b[0]-p[0])** 2 + b[1]**2)
dist_compare = dist



while (dist<= dist_compare):
    p[0] += .0001
    dist_compare = dist
    dist = sqrt((p[0])** 2 + (a[1]+p[1])**2) + sqrt((b[0]-p[0])** 2 + b[1]**2)

print(p[0])
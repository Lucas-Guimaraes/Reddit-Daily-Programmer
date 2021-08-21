#https://www.reddit.com/r/dailyprogrammer/comments/784fgr/20171023_challenge_337_easy_minimize_maximize/

from math import pi

#Gets our initial radius
wire_length = 100
radius = wire_length / 2

#gets the length of the sector; saves as angle
sector_len = wire_length-2*radius
angle = sector_len

#gets the area to compare
area_compare = (angle/2)*(radius**2)
area = area_compare

#Change Area to be smaller over and over again
while (abs(area) >= abs(area_compare)):
    radius -= .0001
    area_compare = area
    sector_len = wire_length - 2 * radius
    angle = sector_len / radius
    area = (angle/2)*(radius**2)

#Convert to degrees; not rounded but can be
print(angle*(180/pi))
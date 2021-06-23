#https://www.reddit.com/r/dailyprogrammer/comments/1tixzk/122313_challenge_146_easy_polygon_perimeter/
import math

#This program takes the number of sides, along with the radius
#The radius is then multiplied by the sin (which uses pi / sides)
#That is multiplied by 2, and multiplied for the sides
#It returns the sine

def find_sine(sides, r):
    sine = sides * 2 * r * math.sin(math.pi / sides)
    return sine
    
print(find_sine(5, 3.7))
raw_input()
#https://www.reddit.com/r/dailyprogrammer/comments/qheeu/342012_challenge_17_easy/
#this one got deleted but something about making a triangle
#There's another solution I like in the comments but learning how this code worked was more interesting


#This function takes it so that it adds an "@" every single time to the line
#and so that the count keeps going up!
def first_side(height):
    count = 0
    triangle = ["@"]
    while count < height:
        print "".join(triangle)
        triangle.append("@")
        count = count + 1
#This function works similar to the last one.
#The only difference is it formatting. .format can do cool things!
def second_side(height):
    count = 0
    triangle = ["@"]
    while count < height:
        print '{:>65}'.format("".join(triangle))
        triangle.append("@")
        count = count + 1
#this time around, instead of using count
#i use the number in the range of the height
#and also times the number to the string
#to make it start out with user then keep removing
#thank you x!
def third_side(height):
    triangle = ["@"]
    triangle *= height
    for x in range(height):
        print "".join(triangle)
        triangle.pop()

#This function just allows the raw input that ends up calling the other functions
def create_triangle():
    height = int(raw_input("Please enter triangle height: "))
    first_side(height)
    second_side(height)
    third_side(height)

create_triangle()
raw_input()
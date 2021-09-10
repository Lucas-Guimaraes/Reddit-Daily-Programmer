#https://www.reddit.com/r/dailyprogrammer/comments/4uhqdb/20160725_challenge_277_easy_simplifying_fractions/

#Finds the greatest common divisor
def gcd(a, b):
    #gets lowest number
    i = min([a, b])

    #-1 until the lowest common divisor is obtained
    while i > 0:
        if a % i == 0 and b % i == 0:
            break
        i -= 1
    return i

#Grabs the div, divides the main numbers, formats result
def simple_fract(a, b):
    div = gcd(a, b)
    a, b = a / div, b / div
    result = "{} {}".format(a, b)
    return result

#Intro
print("Welcome to Simplifying Fractions")
print("Sample Input: 4 8")
print("Sample Output: 1 2")
print("\n~*~--------~*~\n")

#Input
simplify = True
while simplify:
    i = raw_input()
    i = i.lower()
    if i == 'q':
        break
    if " " in i:
        i = i.split(" ")
        if i[0].isdigit() and i[1].isdigit() and len(i) == 2:
            print(simple_fract(int(i[0]), int(i[1])))

raw_input("Press enter to exit.")

#Test cases
#print(simple_fract(4, 8))
#print(simple_fract(1536, 78360))
#print(simple_fract(51478, 5536))
#print(simple_fract(46410, 119340))
#print(simple_fract(7673, 4729))
#print(simple_fract(4096, 1024))
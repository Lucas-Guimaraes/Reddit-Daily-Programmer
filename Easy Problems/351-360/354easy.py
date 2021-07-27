#https://www.reddit.com/r/dailyprogrammer/comments/83uvey/20180312_challenge_354_easy_integer_complexity_1/

from math import sqrt
def integer_complexity(n):
    smallest_sum = n + 1
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0 and n/i+i < smallest_sum:
            smallest_sum = n/i+i
    return smallest_sum

#Intro
print("Welcome to Integer Complexity")
print("Insert a number; we will output the smallest sum")
print("From the two smallest numbers to multiply to get our smallest sum")
print("Example Input:")
print("12345")
print("Example Walkthrough: ")
print("""1*12345 => 1+12345 = 12346\n
3*4115 => 3+4115 = 4118\n
5*2469 => 5+2469 = 2474\n
15*823 => 15+823 = 838\n""")
print("Example Output:")
print("838")
print("\n~*~----------------~*~\n")

#Continue Code
complex = True
while complex:
    #Grabs input
    dig = raw_input()
    if dig.lower() == 'q':
        break
    if dig.isdigit():
        print(integer_complexity(int(dig)))

raw_input("Press Enter to exit.")

#print(integer_complexity(3456789))
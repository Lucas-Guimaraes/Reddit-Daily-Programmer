# https://www.reddit.com/r/dailyprogrammer/comments/2ggy30/9152014_challenge180_easy_looknsay/

from itertools import groupby


#Generates sequence
def look_say(n, output='1'):
    #Yields each generator result to form a list
    for x in xrange(n):
        yield output
        output = ''.join("{}{}".format(len(list(v)), k) for k, v in groupby(output))

#Introduces code
print("Welcome to look n say!")
print("You will give two inputs: Both are numbers")
print("The output will be ran as many times as your first input")
print("And it will use the second input to generate a 'Look n say' sequence based upon your first one!")
print("\n~*~----------------~*~\n")

#Loops program until user quits
look_and_say = True
while look_and_say:
    i = raw_input("How many times?: ")
    x = raw_input("What input? '1' usually receives the best results: ")

    if i.isdigit() and x.isdigit():
        print(list(look_say(int(i), x)))
    elif i.isdigit():
        print(list(look_say(int(i))))

    if i == 'q' or i == 'Q' or x == 'q' or x == 'Q':
        break

raw_input("Press enter to exit")

# test case
# print(list(look_say(3)))
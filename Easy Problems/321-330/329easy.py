# https://www.reddit.com/r/dailyprogrammer/comments/6wjscp/2017828_challenge_329_easy_nearest_lucky_numbers/

# Finds the nearest lucky number
def nearest_lucky_number(number):
    #Next traverses to get the next number
    #idx picks up on the amount to skip
    number_list = createList(number)
    idx = 1
    next = 0
    end = len(number_list)
    # Loops for the amount of times we run through the cycle
    while len(number_list) > idx:
        #Loop for each number to remove
        for i in range(idx, end, idx):
            #If I is higher than Len, break
            if i > len(number_list)-1:
                break
            #remove broken num
            r = number_list[i]
            number_list.remove(r)

        end = len(number_list)
        next += 1
        idx = number_list[next] - 1

    #Checks if number in list - if not, get smaller, number, bigger
    if number in number_list:
        return "{} is a lucky number!".format(number)
    else:
        absolute = lambda lst: abs(lst - number)
        closest = min(number_list, key=absolute)
        if closest > number:
            bigger, smaller = closest, number_list[number_list.index(closest)-1]
        else:
            bigger, smaller = number_list[number_list.index(closest)+1], closest
        return "{} < {} < {}".format(smaller, number, bigger)

#Creates list of numbers
def createList(number):
    number = number * 3
    return [item for item in range(1, number+1)]

# Introduction
print("Welcome to Nearest Lucky Number")
print("This program will tell you if the number you put in is a lucky number")
print("And if not, it will get the neighboring lucky numbers!")
print("\n~*~--------~*~\n")

# Input
nearest = True

while nearest:
    n = raw_input()
    if n.lower() == "q":
        break
    if n.isdigit():
        print(nearest_lucky_number(int(n)))

raw_input("Press enter to exit.")

#Test Cases
#print(nearest_lucky_number(103))
#print(nearest_lucky_number(128))
#print(nearest_lucky_number(231))
#print(nearest_lucky_number(997))
#print(nearest_lucky_number(5000))
#print(nearest_lucky_number(10000))
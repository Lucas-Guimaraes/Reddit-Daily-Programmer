#https://www.reddit.com/r/dailyprogrammer/comments/7ttiq5/20180129_challenge_349_easy_change_calculator/

import itertools

def change_calc(target, coins, f_small=0, f_big=99):
    #Goes over from lowest to highest amount in the comparison
    for l in range(f_small, f_big):
        #Each subset
        for subset in itertools.combinations(coins, l):
            #Sum subset; if equal to target, return
            sum_subset = sum(subset)
            if sum_subset == target:
                subset = str(subset).replace('(', '').replace(')', '').replace(',', '')
                return subset
    #No valid subset
    return "No possible subset"

#Checks list for coins
def list_digits(lst):
    #For each item in list, check if digit
    for i in lst:
        if i.isdigit() == False:
            return []
    lst = [int(i) for i in lst]
    return lst

#Intro code
print("Welcome to Change Calculator")
print("Input a list of digits; first with the target coin amount, followed by the amount of coins")
print("Then for 'output', input an operator")
print("Example Input:")
print("10 5 5 2 2 1")
print("n <= 3")
print("\n~*~----------------~*~\n")

#Runs Code
change = True
while change:
    i = raw_input("Input: ")
    o = raw_input("Output: ")
    if i.lower() == 'q' or o.lower == 'q':
        break
    i = i.split()
    t, c = i[0], list_digits(i[1:])
    o = o.split()

    temp = 0
    valid_operators = ['==', '>=', '<=', '>', '<']

    #(This could be cleaned up some)
    #Checks if operators are valid
    if o[2].isdigit() and o[1] in valid_operators:

        #Op, comparison number
        op, comp = o[1], int(o[2])

        #If "<= or >="
        if '=' in op and op != '==':
            if '<' in op:
                temp += 1

        #If '=='
        if '==' == op:
            beg, end = comp, comp+1

        #If '>', also handles '>' compared to '>='
        elif '>' in op:
            if '=' not in op:
                temp += 1
            beg, end = comp+temp, len(c)+1

        #If '<'
        elif '<' in op:
            beg, end = 0, comp+temp
    #If not valid, we skip and restart
    else:
        continue

    #If digit, and not empty list, we print result
    if t.isdigit() and len(c) > 0:
        print(change_calc(int(t), c, int(beg), int(end)))

raw_input("Press enter to exit.")


#print(change_calc(10, [5, 5, 2, 2, 1]))
#print(change_calc(150, [100, 50, 50, 50, 50]))
#print(change_calc(130, [100, 20, 18, 12, 5, 5]))
#print(change_calc(200, [50, 50, 20, 20, 10]))

#https://www.reddit.com/r/dailyprogrammer/comments/6fe9cv/20170605_challenge_318_easy_countdown_game_show/

from itertools import permutations

#Gets the list and the target
def countdown(lst, target):
    #Grabs permutations for list of numbers and operators
    lst_permutations = list(permutations(lst))
    add, mul, sub, div = ["+"] * 5, ["*"] * 5, ["-"] * 5, ["/"] * 5
    op = add + mul + sub + div
    operator_permutations = list(permutations(op, 5))
    #Loops over all permutations of the numbers
    for x in lst_permutations:
        #Loops over all operator permutations
        for i in operator_permutations:
            #Tests to see if target
            str_test = "((((({0} {1} {2}) {3} {4}) {5} {6}) {7} {8}) {9} {10})".format(x[0], i[0], x[1], i[1], x[2], i[2], x[3], i[3], x[4], i[4], x[5])
            test = eval(str_test)
            if test == target:
                result = "{}{}{}{}{}{}{}{}{}{}{}={}".format(x[0], i[0], x[1], i[1], x[2], i[2], x[3], i[3], x[4], i[4], x[5], target)
                return result
    #If no way to get to target, print this
    return "There are no combinations of {} that equal {}".format(lst, target)

#Checks whole list for is digit
def check_list(d):
    for i in d:
        if i.isdigit() == False:
            return False
    return True

#Intro text
print("Welcome to countdown")
print("Input a sequence of numbers followed by a target number")
print("Note: This program may not make coherent sense.")
print("\n~*~----------------~*~\n")

counting = True
while counting:
    c = raw_input()
    if c.lower() == 'q':
        break
    
    #Makes list of numbers
    c = c.split()
    c, target = c[:len(c)-1], c[-1]
    
    #If list items are digits, and the target is digit
    if check_list(c) and target.isdigit():
        print(countdown(c, int(target)))

#Test case
#print(countdown([3, 8, 7, 6, 1, 3], 250))
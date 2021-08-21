# https://www.reddit.com/r/dailyprogrammer/comments/76qk58/20171016_challenge_336_easy_cannibal_numbers/

#First input is number list, second is target num
def cannibal(lst, target):
    temp_lst = []
    #Compares all numbers in list
    for i in range(len(lst)):
        temp = lst[i]
        for x in range(len(lst)):
            if lst[i] > lst[x]:
                temp += 1
        temp_lst.append(temp)

    #Compares every item in lst to target
    count = 0
    for i in temp_lst:
        if i >= target:
            count += 1

    return count

#Checks if valid; if valid input, constructs list
def check_truth(w, t):

    #Checks if multiple items
    if ' ' in w:
        w = w.split()
        for i in w:
            if i.isdigit() == False:
                t = False
                
    #For one item
    else:
        if w.isdigit() == False:
            t = False
        else:
            w = list(w)
            
    #If true, int conversion
    if t:
        w = [int(x.replace(" ", "")) for x in w]
        
    #Returns list and boolean
    return w, t

# Introduction
print("Welcome to cannibal numbers")
print("Insert a number list and target number list")
print("\n~*~--------~*~\n")

#input
cannibal_n = True
while cannibal_n:
    #setup
    n = raw_input()
    q = raw_input()
    n_true, q_true = True, True
    
    #quit code
    if n.lower() == 'q' or q.lower() == 'q':
        break
        
    #checks truth, empty list
    n, n_true = check_truth(n, n_true)
    q, q_true = check_truth(q, q_true)
    lst = []
    
    #If both inputs are valid, works target
    if n_true and q_true:
        for x in range(len(q)):
            lst.append(cannibal(n, q[x]))

    #Formats target
    lst = [str(i) for i in lst]
    lst = " ".join(lst)
    print(lst)

raw_input("Press enter to exit.")

#test case
#print(cannibal([21, 9, 5, 8, 10, 1, 3], 10))
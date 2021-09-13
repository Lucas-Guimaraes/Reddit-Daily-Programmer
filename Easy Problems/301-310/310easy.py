# https://www.reddit.com/r/dailyprogrammer/comments/64jesw/20170410_challenge_310_easy_kids_lotto/

import random

#Kid Lotto
def kid_lotto(student, lst, n):
    cur_lst = []
    count = 0
    #While the iteration is smaller
    while n > count:
        kid = random.choice(lst)
        #Check if the kid is not on the list already
        if kid in cur_lst or kid == student:
            continue
        else:
            cur_lst.append(kid)
            count += 1
            #checks if it is not the last in list to add seperator
            if count != n:
                cur_lst.append("; ")
    cur_lst = "".join(cur_lst)
    return student + " > " + cur_lst

print("Welcome to Kid Lotto")
print("Example Input: Rebbeca Gann;Latosha Caraveo;Jim Bench;Carmelina Biles;Oda Wilhite;Arletha Eason")
print("3")
print("\n~*~----------------~*~\n")

# Checks input, quit case included
lotto = True
while lotto:
    l = raw_input('List of students: ')
    amt = raw_input('Amount of students for Lotto: ')
    
    if l.lower() == 'q' or amt.lower == 'q':
        break
    l = l.split(";")
    
    if amt.isdigit():
        final_list = []
        for i in l:
            final_list.append(kid_lotto(i, l, int(amt)))
        for f in final_list:
            print(f)

raw_input("Press enter to exit.")


#print(kid_lotto("jake", ["jake", "god", "jesus", "david", "hey"], 2))
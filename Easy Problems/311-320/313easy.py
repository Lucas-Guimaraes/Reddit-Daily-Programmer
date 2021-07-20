#https://www.reddit.com/r/dailyprogrammer/comments/68oda5/20170501_challenge_313_easy_subset_sum/

from itertools import combinations

#Takes all combinations equal to 2, checks for sum
def subset_sum(x):
    comb = combinations(x, 2)
    for x in comb:
        if sum(x) == 0:
            return True
    return False

def subset_bonus(x):
    comb = []
    #Makes combinations from 1 to end of list
    for i in range(len(x)):
        comb.append(combinations(x, i))
        
    #Outer loop is each of the lens made (i.e. 3 numbers, 2 numbers, etc)
    for x in comb:
        #Inner loop is each of the combinations (1, 2) (2, 3), (2, 4) etc
        for i in x:
            #Sum at the end
            if sum(i) == 0:
                return True
    return False


print("Welcome to subset sum")
print("Either insert a list of digits, or...")
print("'s' For regular sum, or 'b' for bonus, to switch between checking the sum of 2")
print("And the sum of all")
print("The default mode is 's'")
print("\n~*~----------------~*~\n")

# Checks input, quit case included

subset = True
mode = 's'

while subset:
    n = raw_input('')

    if n.lower() == 'q':
        break
    elif n.lower() == 's':
        mode = 's'
        print("Mode switched to Sum Two!")
    elif n.lower() == 'b':
        mode = 'b'
        print("Mode switched to Bonus Sum!")
    else:
        n = n.replace('[', '').replace(']', '').replace(',', '')
        n = n.split()
        n = [int(x) for x in n]

        if mode == 's':
            print(subset_sum(n))
        elif mode == 'n':
            print(subset_bonus(n))
raw_input("Press enter to exit.")

#test cases:

#print(subset_sum([1, 2, 3]))
#print(subset_sum([-5, -3, -1, 2, 4, 6]))
#print(subset_sum([]))
#print(subset_sum([-1, 1]))
#print(subset_sum([-97364, -71561, -69336, 19675, 71561, 97863]))
#print(subset_sum([-53974, -39140, -36561, -23935, -15680, 0]))

#print(subset_bonus([0]))
#print(subset_bonus([-3, 1, 2]))
#print(subset_bonus([-98634, -86888, -48841, -40483, 2612, 9225, 17848, 71967, 84319, 88875]))

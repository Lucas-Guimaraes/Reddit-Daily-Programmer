# https://www.reddit.com/r/dailyprogrammer/comments/sq3p9/4242012_challenge_43_easy/
# https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/?ref=leftbar-rightbar
# https://openbookproject.net/thinkcs/python/english3e/trees.html
# binary search tree
# I need to go back and learn this more
#oh my god im so proud of myself

def tree_array(num):
    tree_to_root = []
    while num > 0:
        tree_to_root.append(num)
        num /= 2
    tree_to_root.sort(reverse=True)
    return tree_to_root
    
def compare_tree(element_one, element_two):
    tree_array_one = tree_array(element_one)
    tree_array_two = tree_array(element_two)
    for index in tree_array_one:
        if index in tree_array_two:
            return index

print("*--------*--------*")
print("")
print("Hello! Welcome to Binary Tree")
print("")
raw_input("Press Enter to Continue")
print("")

print("*--------*--------*")
print("")
print("This application takes two inputs - both numbers")
print("From it, we will see the highest number that both numbers share as an ancestor")
print("It's a bit complicated to unpack what a binary search tree is")
print("So applications like google can come in handy!")
print("")
raw_input("Press Enter to Continue")
print("")

print("*--------*--------*")
print("")
number_one = int(raw_input("Please give me your first number: "))
print("")
number_two = int(raw_input("Please give me your second number: "))

print("")

print("*--------*--------*")
print("")
print("You entered {} and {} as your numbers".format(str(number_one), str(number_two)))
print("")
result = compare_tree(number_one, number_two)
print("The closest ancestor is {}".format(result))
print("")
print("*--------*--------*")

raw_input("Press Enter to exit.")
raw_input()


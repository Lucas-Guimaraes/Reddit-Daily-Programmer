#https://www.reddit.com/r/dailyprogrammer/comments/reago/3262012_challenge_30_easy/

def sum_check(lst, target):
    for x in lst:
        for i in lst:
            if int(i) + int(x) == int(target) and lst.index(i) != lst.index(x):
                return "%s and %s equal %s" % (x, i, target)
                        
    return "There are no numbers that equal %s" % (target)

print "This program takes two inputs: A list and a target number"
print "It checks if any two items in the list can be added to equal the target number"
num_str = raw_input("Please input a list - use only integers, and spaces to define each: ")
num_lst = list(num_str.split(" "))
print num_lst
tgt_num = raw_input("Now give me your target number!: ")

print sum_check(num_lst, tgt_num)
raw_input()
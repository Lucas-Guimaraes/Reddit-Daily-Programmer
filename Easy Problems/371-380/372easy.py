#https://www.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/


def balanced(str_put):
    if str_put == '':
        return True
    num_count = []
    
    for letter in str_put:
        num_count.append(str_put.count(letter))
        
    if len(set(num_count)) == 1:
        return True
    else:
        return False


print("Welcome to balanced string!")
print("You will input one item - a string. It will return whether the same amount of characters are all in the word")
print("aabb will return True because there are 2 a's and 2 b's")
print("aabbc will return False because there are 2 a's, 2 b's, but only 1 c.")
print("\n~*~----------------~*~\n")
balanced_check = True
while balanced_check:
    bal_put = raw_input("Please put in your input and press enter. 'letmequit' will give you the option to quit the program: ")
    if bal_put == 'letmequit':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. This is not case sensitive").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
        
            balanced_check = False
    print(balanced(bal_put))

raw_input("Press Enter to exit.")

#for letter in set(str_put):
#unique_lst.append(letter)
# print(balanced("xxxyyyzzz"))
# print(balanced("abccbaabccba"))
# print(balanced("xxxyyyzzzz"))
# print(balanced("abcdefghijklmnopqrstuvwxyz"))
# print(balanced("pqq"))
# print(balanced("fdedfdeffeddefeeeefddf"))
# print(balanced("www"))
# print(balanced("x"))
# print(balanced(""))

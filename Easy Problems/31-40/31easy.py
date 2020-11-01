#https://www.reddit.com/r/dailyprogrammer/comments/rg1vv/3272012_challenge_31_easy/

def product(str_1, str_2):
    num_str_1 = ""
    num_str_2 = ""
    prod_str = ""
    
    for c in str_1:
        num_str_1 += str(char_str.index(c))
        
    for c in str_2:
        num_str_2 += str(char_str.index(c))
    
    prod_num = int(num_str_1) * int(num_str_2)
    for c in str(prod_num):
        prod_str += str(char_str[int(c)])
        
    return "%s and %s equal %s. The numbers for these are %s, %s, and %s" % (str_1, str_2, prod_str, num_str_1, num_str_2, prod_num)


first_str = raw_input("Give me the first string!: ")
second_str = raw_input("Give me the second string!: ")
first_str = first_str.upper()
second_str = second_str.upper()
char_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print product(first_str, second_str)

raw_input()

# I'm trying to find the word in python
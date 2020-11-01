#https://www.reddit.com/r/dailyprogrammer/comments/pv98f/2182012_challenge_10_easy/
telephone_number = raw_input("Please put a telephone number!: ")
telephone_check = telephone_number
telephone_check = telephone_check.replace('x', 'a')
telephone_check = telephone_check.replace('0', 'x')
telephone_check = telephone_check.replace('1', 'x')
telephone_check = telephone_check.replace('2', 'x')
telephone_check = telephone_check.replace('3', 'x')
telephone_check = telephone_check.replace('4', 'x')
telephone_check = telephone_check.replace('5', 'x')
telephone_check = telephone_check.replace('6', 'x')
telephone_check = telephone_check.replace('7', 'x')
telephone_check = telephone_check.replace('8', 'x')
telephone_check = telephone_check.replace('9', 'x')

def telephone_print():
    print telephone_number + " is a real telephone number!"

if telephone_check == "xxxxxxxxxx":
    telephone_print()
elif telephone_check == "xxx xxx xxxx" or telephone_check == "xxx xxxxxxx" or telephone_check == "xxxxxx xxxx":
    telephone_print()
elif telephone_check == "xxx-xxx-xxxx" or telephone_check == "xxx-xxx xxxx" or telephone_check == "xxx xxx-xxxx":
    telephone_print()
elif telephone_check == "xxx.xxx.xxxx" or telephone_check == "xxx.xxx xxxx" or telephone_check == "xxx xxx.xxxx":
    telephone_print()
elif telephone_check == "(xxx)xxx-xxxx" or telephone_check == "(xxx)xxx.xxxx" or telephone_check == "(xxx)xxx xxxx":
    telephone_print()
elif telephone_check == "(xxx) xxx-xxxx" or telephone_check == "(xxx) xxx.xxxx" or telephone_check == "(xxx) xxx xxxx":
    telephone_print()
elif telephone_check == "xxx-xxxx" or telephone_check ==  "xxx xxxx" or telephone_check ==  "xxx.xxxx":
    telephone_print()
else:
    print "That's not a telephone number!"

raw_input()
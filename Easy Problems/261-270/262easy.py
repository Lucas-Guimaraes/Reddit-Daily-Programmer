#https://www.reddit.com/r/dailyprogrammer/comments/4eaeff/20160411_challenge_262_easy_maybenumeric/

def check_num(n):
    pos = n.isdigit()
    if '-' in n:
        n = n.replace('-', '')
    if '.' in n:
        n = n.replace('.', '')
    neg = n.isdigit()
    return neg or pos

#Intro
print("Welcome to Check Number")
print("Put in a string, and this program will check if it is a number, decimal, or negative")
print("\n~*~--------~*~\n")

#Input
check = True
while check:
    n = raw_input()
    if n.islower() == 'q':
        break
    print(check_num(n))

raw_input("Press enter to exit.")

#test cases:

#print(check_num('123'))
#print(check_num('44.234'))
#print(check_num('0x123N'))
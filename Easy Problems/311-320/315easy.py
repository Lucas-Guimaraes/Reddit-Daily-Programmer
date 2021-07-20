#https://www.reddit.com/r/dailyprogrammer/comments/6ba9id/20170515_challenge_315_easy_xor_multiplication/

def xor_multiply(a, b):

    #Gets the binary of our two numbers
    x = bin(a).replace("0b", "")
    y = bin(b).replace("0b", "")
    add_0 = ''
    lst = []

    #Checks through all of string, multiplying
    for i in reversed(range(len(y))):
        str_part = ''
        for idx in x:
            temp = int(y[i]) * int(idx)
            str_part += str(temp)
        str_part = str_part + add_0
        add_0 += "0"
        lst.append(str_part)
    sum = 0

    #Transfers everything in the list to int
    #^= XOR - If one of the two bits is 1
    for s in lst:
        sum ^= bin_to_dec(s)
    return "{}@{}={}".format(a, b, sum)

#Transfers binary to decimal
def bin_to_dec(n):
    return int(n, 2)


#Description
print("Welcome to XOR multiplication")
print("Put in two numbers and their binaries will be multipled")
print("Example input:")
print("5 9")
print("\n~*~----------------~*~\n")

# Checks input, quit case included

xor = True

while xor:
    n = raw_input()
    if n.lower() == 'q':
        break
    n = n.split()
    if n[0].isdigit() and n[1].isdigit():
        print(xor_multiply(int(n[0]), int(n[1])))

raw_input("Press enter to exit.")


#test cases
#print(xor_multiply(9, 5))
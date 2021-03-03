#https://www.reddit.com/r/dailyprogrammer/comments/vbr0z/6202012_challenge_67_easy/

#this performs the binary operation
#starting from getting the bin of the number, cutting the '0b' part of the string
#Multiplying '0' by the leftover and adding the bin_str at the end to get the binary
#finally, reversing it, and transforming the result into a decimal integer

def two_reverse(n):
    bin_str = bin(n)[2:]
    full_str = ('0' * (32 - len(bin_str))) + bin_str
    reverse_int = int(full_str[::-1], 2)
    return reverse_int

#this checks if the user wants to quit
def quit_check(i):
    if i == 'q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. This is not case sensitive: ").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
            return True
    return False

print("Welcome to two reverse!")
print("This program takes a binary number and converts the 32 bit version of it to it's alternative side")

print("\n Example Input:")
print("13")

print("\n Example Logic:")
print("13's binary number is 1101")
print("The 32 bit version is stored like this:")
print("00000000000000000000000000001101")
print("So we reverse the numbers to get this:")
print("10110000000000000000000000000000")
print("And then we convert it to decimal")

print("\n Example Output:")
print("2952790016")

print("\n~*~----------------~*~\n")

rev = True
while rev:
    bin_num = raw_input("Please input a num to convert. 'q' to quit: ").lower()
    if quit_check(bin_num):
        rev = False
        continue
    if bin_num.isdigit():
        print(two_reverse(int(bin_num)))
    else:
        print("{} is not a valid digit!".format(bin_num))

raw_input("\nPress enter to exit.")

#print(two_reverse(13))
#this function showcases off more
# def two_reverse(n):
    # bin_str = bin(n)[2:]
    # full_str = ('0' * (32 - len(bin_str))) + bin_str
    # full_str_int = int(full_str)
    # reverse_int_before = int(full_str[::-1])
    # reverse_int = int(full_str[::-1], 2)
    # return full_str_int, reverse_int_before, reverse_int
    
    #the full int is to show 13 but as a binary
    #Then, the binary reverses
    #Then, the binary conversion
    #this could probably look cleaner, honestly. If I run w/ this
# https://www.reddit.com/r/dailyprogrammer/comments/1berjh/040113_challenge_122_easy_sum_them_digits/

#This program sums up all the numbers of the input.
#this will continue until the digit is only one digit long

def digital_root(num):
    print(num)
    # base case
    if 10 > num:
        return

    #this makes all of the numbers in the string into a list
    num = [int(x) for x in str(num)]
    #Followed by the sum
    num = sum(num)
    #Constantly calling it until we get out number
    digital_root(num)

print("Put in a number")
print("The output will be the digital root, and all the numbers before")
print("Take the number 31337 as an example")
print("3+1+3+3+7 = 17. 1+7 = 8")
print("The program will print 31336, 17, and then 8.")
print("\n~*~----------------~*~\n")

#Checks input. Dig_num is used as our input; num_put is our loop checker
num_put = True
while num_put:
    dig_num = raw_input("Give me a number. Press 'Q' or 'q' to quit: ")
    if dig_num == 'q' or dig_num == 'Q':
        num_put = False
        break
    if dig_num.isdigit():
        digital_root(int(dig_num))

raw_input("Press enter to exit.")

#raw_input()
#digital_root(31337)

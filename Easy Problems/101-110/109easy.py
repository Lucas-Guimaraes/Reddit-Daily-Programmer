#https://www.reddit.com/r/dailyprogrammer/comments/12csk7/10302012_challenge_109_easy_digits_check/

#checks if it only contains the first ten digits (0 to 9)
def digit_check(n):
    return all(c in '0123456789' for c in n)

print("This program will check if your string is a valid digit. 'q' will quit the program.")
print("\n~*~----------------~*~\n")
stringy = True
while stringy:
    num = raw_input("Give me a string: ")
    if num == 'q' or num == 'Q':
        stringy = False
        break
        
    print(digit_check(num))


raw_input("Press enter to exit.")

#test cases:
#print(digit_check('124'))
#print(digit_check('abc'))
#print(digit_check('123.123'))
#print(digit_check('123'))
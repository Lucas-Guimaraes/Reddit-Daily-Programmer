#https://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/
import random
import string

number_of_passwords = 0
password_length = 0

#checks digit
def check_digit(x):
    while True:
        digit = raw_input(x)
        try:
            digit = int(digit)
            return digit
            break
        except ValueError:
            digit = str(digit)
            print(digit + " is not a number!")
def random_alphanumeric(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str
    
#password generator            
print "Welcome to password generator!"
number_of_passwords = check_digit("How many passwords would you like to generate?: ")
password_length = check_digit("How long?: ")

for x in range(0, number_of_passwords):
    print random_alphanumeric(password_length)

raw_input()
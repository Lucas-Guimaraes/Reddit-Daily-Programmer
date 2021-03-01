#https://www.reddit.com/r/dailyprogrammer/comments/cdieag/20190715_challenge_379_easy_progressive_taxation/

def taxation(paycheck):
    tax = 0

    if 10000 < paycheck <= 30000:
        tax = (paycheck - 10000) * 0.1
    if 30000 < paycheck <= 100000:
        tax = 20000 * 0.1
        tax += (paycheck - 30000) * 0.25
    if 100000 < paycheck:
        tax = 20000 * 0.1
        tax += 70000 * 0.25
        tax += (paycheck - 100000) * 0.4

    return int(tax)

print("Welcome to tax program!")
print("This program takes one value - a number. Also known as your paycheck.")
print("Afterwards, it will tell you how much money you owe in taxes.")
print("\n~*~----------------~*~\n")
taxes = True
while taxes:
    pay = raw_input("Please put in your input and press enter. No input will quit: ")
    if pay.isdigit():
        print(taxation(int(pay)))
    elif pay == '':
        print("Now exiting...")
        taxes = False
    else:
        print("{} is not a valid number!".format(pay))
        

raw_input("Press Enter to exit.")

#print(taxation(0))
#print(taxation(10000))
#print(taxation(10009))
#print(taxation(10010))
#print(taxation(12000))
#print(taxation(56789))
#print(taxation(90000))
#print(taxation(120000))
#print(taxation(1234567))
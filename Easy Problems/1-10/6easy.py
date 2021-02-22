#https://www.reddit.com/r/dailyprogrammer/comments/pp53w/2142012_challenge_6_easy/
#https://www.101computing.net/calculating-pi/ flowchart is cool
#https://stackoverflow.com/questions/63226007/tried-to-implement-the-nilakantha-algorithm-in-python
#I DONT FUCKING GET PI
#maybe write a program that asks if yyou get the solution instead?


from decimal import *
def p_pi(precision):
    getcontext().prec=precision
    c = float(3.141592654)
    d= float(1)
    dec_amt = str(1.)
    for i in range(precision-3):
        dec_amt += '0'
    pi=Decimal(c/d).quantize(Decimal(dec_amt),rounding=ROUND_UP)
    return pi

print("Welcome to Pi!")
print("\n~*~--------~*~\n")
print("You will input a digit - that will determine how many decimals you will get for pi")
print("\n~*~--------~*~\n")
dec_amt = int(raw_input("Please put in your amount: "))
print("\n~*~--------~*~\n")
dec_new = p_pi(dec_amt)
print("Your result is {}\n".format(dec_new))
raw_input("Press enter to exit.")

#print(p_pi(1))
#print(p_pi(6))
#print(p_pi(12))
#print(p_pi(30))
#print(p_pi(32))
#print(p_pi(34))
#print(p_pi(64))
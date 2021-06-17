# https://www.reddit.com/r/dailyprogrammer/comments/11paok/10182012_challenge_104_easy_powerplant_simulation/
import math

#This removes all the invalid operating days
def powerplant_sim(days):
    op_days = days
    for count in range(1, days):
        #Refer to function below
        if is_today_off(count):
            op_days -= 1
        else:
            continue
    return op_days

#If today is an off day
def is_today_off(num):
    if num % 3 == 0 or num % 14 == 0 or num % 100 == 0:
        return True
    else:
        return False

pp_sim = True
print("Welcome to powerplant sim. 'q' will quit the program.")
print("\n~*~----------------~*~\n")

#this runs in a loop to check inputs
#until the user quits or closes out of the program
while pp_sim:
    days = raw_input("Give me a digit: ")
    #if digit, print!
    if days.isdigit():
        print(powerplant_sim(int(days)))
    #exit code
    if days == 'q':
        pp_sim = False
        raw_input("Press enter to exit.")


#test cases:
#print(powerplant_sim(14))
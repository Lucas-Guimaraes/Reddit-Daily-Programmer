# https://www.reddit.com/r/dailyprogrammer/comments/zfe7v/9052012_challenge_96_easy_controller_chains/

def controller_chain(money):
    #Accounts for the initial controller
    total = 1
    money_count = money
    while money_count > 0:
        #Adds multitaps
        if total % 3 == 0:
            money_count -= 12
            
        #adds an extra controller
        if money_count > 20:
            total += 1
            money_count -= 20
            
        #No more controllers available; quit case
        else:
            money_count = 0
            
    return total


# Loops until user quits
money_table = True
while money_table:
    ctrl_put = raw_input("Insert your money: ")

    if ctrl_put.isdigit():
        print(controller_chain(int(ctrl_put)))

    # Quit case.
    if ctrl_put == "q" or ctrl_put == "Q":
        break

raw_input("Press enter to exit.")

# Test cases
# print(controller_chain(54))
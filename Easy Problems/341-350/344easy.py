# https://www.reddit.com/r/dailyprogrammer/comments/7j33iv/20171211_challenge_344_easy_baumsweet_sequence/


def baum_sweet(num):
    bin_num = str(bin(num))
    bin_num_lst = bin_num.split('1')
    for i in bin_num_lst:
        if len(i) % 2 != 0:
            return 0
    return 1


print(baum_sweet(4))
print(baum_sweet(5))
print(baum_sweet(19611206))

print("Welcome to baum sweet!")
print("This application will check whether there is an odd sequence of 0's in a binary number")
print("For example, 4 in binary is 100")
print("There are 2 00's next to each other, so that would be a 1.")
print("101, the binary for 5, however, would be 0. As 1 0 with no 0's next to it is an odd number")

print("\n~*~----------------~*~\n")

baum_blitz = True

while baum_blitz:
    baum_put = raw_input("Please put in your input and press enter. 'letmequit' will give you the option to quit the program: ")
    
    #checks if user wants to quit
    if baum_put == 'letmequit':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. This is not case sensitive").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
            baum_blitz = False
            continue
            
    #checks if digit
    if baum_put.isdigit():        
        print(baum_sweet(int(baum_put)))
        
    else:
        print("{} is not a valid number!".format(baum_put))

raw_input("Press Enter to exit.")



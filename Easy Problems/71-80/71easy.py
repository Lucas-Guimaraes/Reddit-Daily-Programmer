#https://www.reddit.com/r/dailyprogrammer/comments/vx3bk/722012_challenge_71_easy/

#this program 
def pythagorean_triple(n):
    no_valid = True
    for A in range(1, n+1):
        for B in range(1, n+1):
            C = n - A - B
            if (A <= B <= C) and (A**2 + B**2 == C **2):
                no_valid = False
                print(A, B, C)
    if no_valid:
        print("No pythagorean triple combination for {}!".format(str(n)))
        
#this quits the program
def quit_check(i):
    if i == 'q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. This is not case sensitive: ").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
            return True
    return False

print("Welcome to pythagorean triple!")
print("This will take in your input (a number) and show you all the possible Pythagorean Triples")
print("Your input will be the sum")

print("\n Example Input:")
print("240")

print("\n Example Output:")
print("15, 11, 113")
print("40, 96, 104")
print("48, 90, 102")
print("60, 80, 100")

print("\n Explination:")
print("The smaller two numbers, by the power of 2, will equal the biggest number")
print("A^2 * B^2 = C^2")
print("And if there is no valid one with your sum, we'll be sure to tell you!")

print("\n~*~----------------~*~\n")

valid_angle = True
while valid_angle:
    sum_a = raw_input("Put your number here. 'q' to quit: ")
    if quit_check(sum_a):
        break
    if sum_a.isdigit():
        print("")
        pythagorean_triple(int(sum_a))
        print("")
    else:
        print("{} is not a valid number!".format(sum_a))
    
raw_input("Press enter to exit")

#pythagorean_triple(90)
#print('')
#pythagorean_triple(180)
#print('')
#pythagorean_triple(240)
#print('')
#pythagorean_triple(69)
#print('')
#pythagorean_triple(270)
#print('')
#pythagorean_triple(400)
#print('')
#pythagorean_triple(504)
#print('')

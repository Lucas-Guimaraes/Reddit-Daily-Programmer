#https://www.reddit.com/r/dailyprogrammer/comments/65vgkh/20170417_challenge_311_easy_jolly_jumper/

def jolly_jumper(n, x):
    diff = []
    #add absolute for the range
    for i in range(1, n):
        temp = x[i] - x[i-1]
        diff.append(abs(temp))

    #Sorts, checks
    diff = sorted(diff)
    for i in range(1, n-1):
        if diff[i] - diff[i-1] != 1:
            return "Not Jolly"
    return "Jolly"

#Introduction text
print("Welcome to Jolly Jumper")
print("Example Input: 4 1 4 2 3")
print("The first number will be the amount of numbers; the others will be the Jolly check")
print("\n~*~----------------~*~\n")

# Checks input, quit case included
jolly = True
while jolly:
    n = raw_input(' ')

    if n.lower() == 'q':
        break
    n = n.split()
    amt, n = n[0], n[1:]
    n = [int(x) for x in n]

    if amt.isdigit():
        print(jolly_jumper(int(amt), n))

raw_input("Press enter to exit.")

#print(jolly_jumper(4, [1, 4, 2, 3]))
#print(jolly_jumper(5, [1, 4, 2, -1, 6]))
#print(jolly_jumper(4, [19, 22, 24, 21]))
#print(jolly_jumper(4, [19, 22, 24, 25]))
#print(jolly_jumper(4, [2, -1, 0, 2]))
# https://www.reddit.com/r/dailyprogrammer/comments/wa0mc/792012_challenge_74_easy/

# this makes a fibbinaci sequence
def make_fib_seq(n):
    fib_seq = [0, 1]
    while n > fib_seq[-1]:
        new_fib = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(new_fib)
    return fib_seq


# finds the zeckendorf representation of a number
def zeckendorf_rep(n):
    zecken_lst = []
    count = n
    skip = ''
    skip_list = []


    new_fib_seq = make_fib_seq(count)
    #this numbers each part of the list to give it a proper order
    #it also reverses the list
    # the count goes down by the number iterated through each time (so it doesn't iterate through everything)
    #and it appends to the list of what to add
    for i, e in reversed(list(enumerate(new_fib_seq))):
        if count == 0:
            break
        if e <= count and count - e >= 0:
            count -= e
            zecken_lst.append(e)
    return zecken_lst

#check if quitting!
def quit_check(i):
    if i == 'q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. This is not case sensitive: ").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
            return True
    return False

print("Hello! Welcome to zeckendorf rep")
print("You will be able to put in a number to find out all of the zeckendorf numbers.")
print("It's a bit confusing to explain, but basically, it is all the nums in the fibonacci sequence")
print("That can be added up together to get that number")
print("But here's the twost: The numbers can not be consecutive!")
print("\n~*~----------------~*~\n")

zeck = True
while zeck:
    num = raw_input("Please put in a number. Or 'q' to quit: ")
    if quit_check(num):
        break
    if num.isdigit():
        print(zeckendorf_rep(int(num)))
    else:
        print("{} is not a valid number!".format(num))
raw_input()

#print(zeckendorf_rep(14348907))
#print(make_fib_seq(47))
#print(zeckendorf_rep(14348907))
#print(zeckendorf_rep(3**15))
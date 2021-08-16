# https://www.reddit.com/r/dailyprogrammer/comments/njxq95/20210524_challenge_391_easy_the_abacaba_sequence/

#abacaba seq function
def abacaba_seq(num):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    seq = ''
    for i in range(num):
        seq = seq + letters[i] + seq
    return seq

# Intro
print("Welcome to abacaba!")
print("Put in a number")
print("\n~*~----------------~*~\n")

counting = True

#Input
while counting:
    n = raw_input("Put in your number: ")
    if n == 'q':
        break
    if n.isdigit():
        print(abacaba_seq(int(n)))

#Exit
raw_input("Press enter to exit.")
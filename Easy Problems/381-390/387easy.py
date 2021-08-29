#https://www.reddit.com/r/dailyprogrammer/comments/myx3wn/20210426_challenge_387_easy_caesar_cipher/

#Uses the Caeser Cipher!
def caesar(s, n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypt = ''

    for i in s:
        idx = alphabet.find(i) + n
        #Makes sure IDX is not out of range
        while idx >= 26:
            if idx >= 26:
                idx -= 26
        encrypt += alphabet[idx]

    return encrypt

#Intro
print("Welcome to Caeser Cipher")
print("Put in a string and a digit")
print("The output will be the Caesar conversion")
print("\n~*~--------~*~\n")

#Input
crypting = True
while crypting:

    word = raw_input("Word: ")
    amt = raw_input("Amount to shift by: ")

    if word == "q" and amt == "q":
        break

    if amt.isdigit():
        caesar(word, int(amt))

raw_input("Press enter to exit.")

#Test Case:
#print(caesar("jgorevxumxgsskx", 20))
#print(caesar("dailyprogrammer", 6+26))
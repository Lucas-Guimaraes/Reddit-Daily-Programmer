#https://www.reddit.com/r/dailyprogrammer/comments/45w6ad/20160216_challenge_254_easy_atbash_cipher/

#alpha str
lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()

#checks letter to see if it runs through cipher
def cipher(word):
    new_w = ''
    for w in word:
        if w.isalpha():
            idx = lower.find(w)+1
            if w.lower():
                new_w += lower[-idx]
            else:
                new_w += upper[-idx]
        else:
            new_w += w
    return new_w

print("Welcome to Atbash Cipher!")
print("Give a sentence. All letters in the alphabet will be converted to their opposite")
print("A will be Z. B will be Y. etc")
print("\n~*~--------~*~\n")

plain = True
while plain:
    w = raw_input()
    if w.lower() == 'q':
        break
    print(cipher(w))

raw_input("Press enter to exit.")

#test case
#print(cipher('foobar'))
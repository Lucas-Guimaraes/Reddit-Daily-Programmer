#https://www.reddit.com/r/dailyprogrammer/comments/879u8b/20180326_challenge_355_easy_alphabet_cipher/

import string

letters = string.ascii_lowercase

#make strings equal
def make_equal(s1, s2):
    idx = 0
    #loops until first string is equal to second string
    while len(s2) > len(s1):
        s1 += s1[idx]
        idx += 1
    return s1

#encrypts
def alphabet_encrypt(s1, s2):
    s1 = make_equal(s1, s2)
    encrypt = ''
    #grab the index of both s1 and s2
    for i in range(len(s1)):
        check = letters.find(s1[i]) + letters.find(s2[i])
        #if idx is out of alphabet range
        if check > 25:
            check -= 26
        encrypt += letters[check]

    return encrypt

#decrypts
def alphabet_decrypt(s1, s2):
    s1 = make_equal(s1, s2)
    decrypt = ''
    #grab the index of both s1 and s2
    for i in range(len(s1)):
        check = letters.find(s2[i]) - letters.find(s1[i])
        #if idx is out of alphabet range
        if 0 > check:
            check += 26
        decrypt += letters[check]

    return decrypt

#Intro
print("Welcome to decrypt/encrypt!")
print("Insert two words on the same line; the output will be the encrypt/decrypt")
print("\n~*~----------------~*~\n")

#Continue Code
crypt = True
mode = 'e'
while crypt:
    s = raw_input().lower()
    
    #Checks quit
    if s == 'q':
        break
    
    #Checks Encrypt/Decrypt
    if s == 'decrypt' or s == 'd':
        mode = 'd'
    if s == 'encrypt' or s == 'e':
        mode = 'e'
    s = s.split()
    
    #error handling
    if len(s) == 2 and s[0].isalpha() and s[1].isalpha():
        #Checks whether decrypt or encrypt
        #Finishes; repeat loop
        if mode == 'd':
            print(alphabet_decrypt(s[0], s[1]))
        elif mode == 'e':
            print(alphabet_encrypt(s[0], s[1]))

raw_input("Press Enter to exit.")
#https://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/

print("Welcome to Caeser Cipher!")

#encrypt
def encrypt(user_string):
    word_encrypted = ""
    for letter in user_string:
        letter_encrypted = chr(ord(letter) + 2)
        if ord(letter_encrypted) == 92:
            letter_encrypted = chr(66)
        if ord(letter_encrypted) == 93:
            letter_encrypted = chr(67)
        if ord(letter_encrypted) == 123:
            letter_encrypted = chr(97)
        if ord(letter_encrypted) == 124:
            letter_encrypted = chr(98)
        word_encrypted += letter_encrypted
    return word_encrypted

#decrypt            
def decrypt(user_string):
    word_decrypted = ""
    for letter in user_string:
        letter_decrypted = chr(ord(letter) - 2)
        if ord(letter_decrypted) == 64:
            letter_decrypted = chr(90)
        if ord(letter_decrypted) == 63:
            letter_decrypted = chr(89)
        if ord(letter_decrypted) == 96:
            letter_decrypted = chr(122)
        if ord(letter_decrypted) == 95:
            letter_decrypted = chr(121)
        word_decrypted += letter_decrypted
    return word_decrypted

#alphabetical check
while True:
    encode = raw_input("First, give me a string! Make sure it only has alphabetical characters: ")
    if encode.isalpha():
        print "Awesome! Your selected word is " + encode
        break
    else:
        print "Please make sure it only contains alphabetical characters"

#encrypt or decrypt?
while True:
    print("Next, choose to Encrypt or Decrypt!")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = raw_input("Put in 1. for Encrypt or 2. for Decrypt: ")
    if choice == "1":
        print encrypt(encode)
        break
    elif choice == "2":
        print decrypt(encode)
        break
    else:
        print "Please put '1' or '2'."

raw_input()
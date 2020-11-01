#https://www.reddit.com/r/dailyprogrammer/comments/pr2xr/2152012_challenge_7_easy/

morse_string = ""
morse_array = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
alphabet_transfer = "abcdefghijklmnopqrstuvwxyz"

#alphabetical check
print "Welcome to Morse Code Generator!"
#definitely add way to reverse around
#add sound eventually

while True:
    morse_word = raw_input("First, give me a string! Make sure it only has alphabetical characters: ")
    if morse_word.isalpha():
        print "Awesome! Your selected word is " + morse_word
        break
    else:
        print "Please make sure it only contains alphabetical characters"

for letter in morse_word:
    morse_string += morse_array[ord(letter) - 97]
    
print morse_string
raw_input()
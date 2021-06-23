#https://www.reddit.com/r/dailyprogrammer/comments/1ystvb/022414_challenge_149_easy_disemvoweler/

def disemvowel(readable):
    if readable == '':
        return
    readable = readable.replace(" ", "")
    vowel = ''
    consonant = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in readable:
        if letter in vowels:
            vowel += letter
        else:
            consonant += letter
            
    print(consonant)
    print(vowel)
    return
    
print("Welcome to disemvowel!")
print("This program will take in one input: a string")
print("From there, it will remove all spaces, then it will print all consonants, followed by vowels")
print("\n~*~----------------~*~\n")
print("Example input #1:")
print(" c a  t   ")
print("\nExample output #1:")
print("ct")
print("a")
print("\nExample input #2:")
print("all those who believe")
print("\nExample output #2:")
print("llthswhblv")
print("aoeoeiee")
print("\n~*~----------------~*~\n")
disemvoweling = True
while disemvoweling:
    str_put = raw_input("Your input here ('q' to quit): ")
    if str_put == 'q' or str_put == 'Q':
        quit_put = raw_input("Would you like to quit for sure? Press 'q' to do so.")
        if quit_put == 'q' or quit_put == 'Q':
            print("Goodbye")
            disemvoweling = False
    disemvowel(str_put)
    

raw_input("Press Enter to exit.")
#disemvowel("two drums and a cymbal fall off a cliff")
#disemvowel("all those who believe in psychokinesis raise my hand")
#disemvowel("did you hear about the excellent farmer who was outstanding in his field")

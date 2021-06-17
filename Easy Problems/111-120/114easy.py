# https://www.reddit.com/r/dailyprogrammer/comments/149kec/1242012_challenge_114_easy_word_ladder_steps/

def ladder_steps(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    file = '114easytest.txt'
    
    with open(file) as f:
        read_file = [line.rstrip() for line in f]
    for letter in word:
        new_word = ''
        for changed_letter in letters:
            new_word = word.replace(letter, changed_letter)
            if new_word in read_file:
                if new_word != word:
                    print new_word

print("Welcome to ladder steps!")
print("This program takes one input, a string")
print("Followed by the output, checking how many variations of that word exist with only replacing one letter")
print("Only four letter words may be accepted")
print("\n~*~----------------~*~\n")

testing = True
ladder_word = ''
while testing:
    ladder_word = raw_input("Give me a four letter string to ladder!: ")
    if len(ladder_word) == 4:
        testing = False
        
print("Your chosen word is {}".format(ladder_word))
print("\n~*~----------------~*~\n")
ladder_steps(ladder_word)
print("\n~*~----------------~*~\n")
raw_input("Press enter to exit")

#ladder_steps('puma')
#print('puma ladder')
#ladder_steps('cars')
#print('car ladder')
#ladder_steps('feel')
#print('feel ladder')

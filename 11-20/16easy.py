#https://www.reddit.com/r/dailyprogrammer/comments/q8aom/2272012_challenge_16_easy/

def remove_letters(first_word, second_word):
    for char in second_word:
        first_word = first_word.replace(char,"")
    return first_word
        
first_choice = raw_input("Input your first word!: ")
second_choice = raw_input("Input your second word!: ")

print remove_letters(first_choice, second_choice)

raw_input()
# https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/

# Function
def letter_value_sum(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    for w in word:
        count += alphabet.find(w) + 1
    return count

# Intro
print("Welcome to string value sum!")
print("Put in a string. The output will be its score.")
print("If you want to exit, type '17' and hit enter.")
print("\n~*~----------------~*~\n")

#Input handler
counting = True
while counting:
    l = raw_input("Put in your string: ").lower()
    # 17 is the number for q
    if l == 17:
        break
    if l.isalpha():
        print(letter_value_sum(l))

#Exit
raw_input("Press enter to exit.")

# Test Case
# print(letter_value_sum('a'))
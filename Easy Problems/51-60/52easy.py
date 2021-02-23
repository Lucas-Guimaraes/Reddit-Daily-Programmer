# https://www.reddit.com/r/dailyprogrammer/comments/tmnfq/5142012_challenge_52_easy/
import string

def order_words(word_lst):
    word_len = []
    alphabet = string.ascii_lowercase

    alphabet_dict = {}
    for i in range(26):
        idx = alphabet[i]
        alphabet_dict[idx] = i+1

    final_dict = {}
    final_lst = []

    for word in word_lst:
        word_len.append(len(word))

        l_total = 0
        for letter in word:
            lower = letter.lower()

            l_total += alphabet_dict[lower]

        l_total = l_total / word_len[-1]
        final_dict[word] = l_total

    for key in sorted(final_dict):
        final_lst.append(key)
    return final_lst


print("Welcome to order words!\n")
print("You will give me one input: A list of words!")
print("And then I will order them alphabetically")
print("\n~*~----------------~*~\n")
w_str = raw_input("Please give me your list of words: \n")
w_obj = w_str.split()
print("")
print(order_words(w_obj))
raw_input("\nPress enter to exit.")
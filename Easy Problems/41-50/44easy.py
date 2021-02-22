# https://www.reddit.com/r/dailyprogrammer/comments/srowj/4252012_challenge_44_easy/


def string_to_result(paragraph):
    paragraph = paragraph.replace('!', '.')
    paragraph = paragraph.replace('?', '.')
    paragraph_list = paragraph.split('.')
    sent_length = 0
    longest_lst = []

    for sentence in paragraph_list:
        word = sentence.split(' ')
        # checks if it has the most words
        if len(word) > sent_length:
            sent_length = len(sentence)
            longest_lst = word

    over_four_chars = []
    for word in longest_lst:
        if len(word) > 4:
            over_four_chars.append(word)

    long_sent = " ".join(longest_lst)

    return long_sent, sent_length, over_four_chars


print("*--------*--------*")
print("")
print("Hello! Welcome to Sentence Input")
print("")
raw_input("Press Enter to Continue")
print("")

print("*--------*--------*")
print("")
print("This application takes one Input - a string")
print("This string should have multiple sentences")
print(
    "From it, we will print out the sentence with the most words, how many words, and all words in that sentence above 4 characters!")
print("")
raw_input("Press Enter to Continue")
print("")

print("*--------*--------*")
print("")
sentence_string = (raw_input("Please give me your chosen sentences: "))

print("")

print("*--------*--------*")
print("")
print("You entered this as your paragraph:\n {}".format(sentence_string))
print("")
longest_sentence, word_length, above_four = string_to_result(sentence_string)
print("Your sentence is: '{}'\n The longest sentence has {} words.\n {} are all above four characters.".format(longest_sentence, word_length, above_four))
print("")
print("*--------*--------*")

raw_input("Press Enter to exit.")
raw_input()
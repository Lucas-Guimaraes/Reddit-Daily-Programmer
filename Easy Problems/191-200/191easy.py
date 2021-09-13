#https://www.reddit.com/r/dailyprogrammer/comments/2nynip/2014121_challenge_191_easy_word_counting/

#'191easy.txt' is a supplementary file

#Organizes data
file = open('191easy.txt', 'r')
data = file.read().split()
words = {}

#Adds how much of each data appears
for w in data:
    if w in words:
        words[w] += 1
    else:
        words[w] = 1

#Sets up the list of values
file.close()
lst = words.values()
ordered_lst = sorted(lst, reverse=True)
count = 20

#Counts until the top 20 words are printed out.
printing = True
while printing:
    for i in ordered_lst:
        if count == 0:
            break
        for key, value in words.items():
            if value == i and key.isalpha():
                print("{} {}".format(key, value))
                count -= 1

raw_input("Press enter to exit.")

# https://www.reddit.com/r/dailyprogrammer/comments/5seexn/20170206_challenge_302_easy_spelling_with/

import csv

#imports csv file
csv_file = '302easy.csv'
elements_and_symbols = []
with open(csv_file, 'r') as e_data:
    reader = csv.reader(e_data)
    for row in reader:
        elements_and_symbols.append((row[1].strip(), row[2].strip()))

#converts word
def convert_word(word):
    new_word = ''
    ele_lst = []
    skip = False
    for w in range(len(word)):
        #check if a word has been added, skip is for 'if next letter'
        check = True

        if skip:
            skip = False
            continue

        #checks first for any two elements
        for i in elements_and_symbols:
            if w < len(word)-1:
                if i[0] == word[w].upper()\
                        + word[w + 1]:
                    new_word += i[0]
                    ele_lst.append(i[1])
                    skip = True
                    check = False
                    break

        #checks if letter in elements
        if check:
            for i in elements_and_symbols:
                if i[0] == word[w].upper():
                    new_word += i[0]
                    ele_lst.append(i[1])
                    check = False
                    break

        #if letter combo isn't in elements, it is added
        if check:
            new_word += word[w]
    elements = "{} ({})".format(new_word, ", ".join(ele_lst).lower())
    return elements


# Introduction
print("Welcome to convert word!")
print("Each word will be converted to an element of the periodic table")
print("\n~*~--------~*~\n")

#input
conversion = True
while conversion:
    w = raw_input()
    if w.lower() == 'q':
        break
    print(convert_word(w))

raw_input("Press enter to exit.")
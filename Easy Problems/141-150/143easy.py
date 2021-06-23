# https://www.reddit.com/r/dailyprogrammer/comments/1s061q/120313_challenge_143_easy_braille/
#143easytest.txt is a supplementary file
#You may replace with your own supplementary file, or use the one I've included
#This program only supports a-z. No uppercase.

#Braille dictionary. 'O'  and '.' for the symbols
braille = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z'
}


def braille_to_english(file_name):
    braille_file = open(file_name, 'r+')
    #These three lists are because braille is set on three lines
    line_one = []
    line_two = []
    line_three = []
    final_word = ''
    current_line = -1
    #Goes over each individual line
    for line in braille_file.readlines():
        current_line += 1
        braille_letters = line.split(' ')
        final_word_range = len(braille_letters)
        
        #Sorts the braille into proper lists by going over each bit of characters
        for letter in braille_letters:

            new_letter = letter
            new_letter = new_letter.replace("\n", "")

            if current_line == 0:
                line_one.append(new_letter)
            elif current_line == 1:
                line_two.append(new_letter)
            elif current_line == 2:
                line_three.append(new_letter)

    #Combines each of the lines by going through the range of the brail letters
    for i in range(final_word_range):
        full_letter = line_one[i] + line_two[i] + line_three[i]
        final_word += braille[full_letter]
        
    #Final word!
    return final_word


print(braille_to_english('143easytest.txt'))
raw_input()

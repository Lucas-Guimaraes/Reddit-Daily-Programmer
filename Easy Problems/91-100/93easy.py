# https://www.reddit.com/r/dailyprogrammer/comments/z3a4y/8302012_challenge_93_easy_twoway_morse_code/
# 'ascii *to* morse'
a2m = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '--.-',
    'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.-', ')': '-.--.-', ' ': '', '': ' '
}

#makes 'morse *to* ascii' dictionary
m2a = {}
for key, value in a2m.items():
    m2a[value] = key

#Function
def morse_translator(word):
    
    print_word = ''
    #Is Morse
    if ' ' in word:
        word = word.split()
        for letter in word:
            print_word += m2a[letter]
    
    #Not Morse
    else:
        for letter in word:
            print_word += a2m[letter]

    return print_word

#Loops until user quits
morsing = True
while morsing:
    m_string = raw_input("Convert a morse to a word, or vice versa: ")
    #Quit case.
    if m_string == "q" or m_string == "Q":
        break
    print(morse_translator(m_string))

raw_input("Press enter to exit.")

#Test cases.
# print(morse_translator('... --- ...'))
# print(morse_translator('sos'))
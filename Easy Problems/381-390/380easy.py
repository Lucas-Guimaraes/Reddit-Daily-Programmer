#https://www.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/

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

def smorse(str_put):
    smorse_word = ''
    for letter in str_put:
        smorse_word += a2m[letter]
    return smorse_word
    
print("Welcome to smorse! Smooshed Morse Code.")
print("You will input one item - a string. It will return as morse code.")
print("No spaces will be added in-between letters though!")
print("\n~*~----------------~*~\n")
smorse_code = True
while smorse_code:
    smorse_put = raw_input("Please put in your input and press enter. Give me no input: ")
    if smorse_put == '':
        print("Goodbye.")
        smorse_code = False
    print(smorse(smorse_put))

raw_input("Press Enter to exit.")
#print(smorse("sos"))
#print(smorse("daily"))
#print(smorse("programmer"))
#print(smorse("bits"))
#print(smorse("three"))
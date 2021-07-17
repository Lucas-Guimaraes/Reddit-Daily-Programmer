# https://www.reddit.com/r/dailyprogrammer/comments/25clki/5122014_challenge_162_easy_novel_compression_pt_1/

#decompresses using our dictionary and chunk
def decompress(dic, chunk):
    chunk = chunk.split()
    output, delimiter, next_delimiter = '', '', ' '

    for c in chunk:
        if c in '.,?!;:':
            next_delimiter = c + ' '
        elif c is '-':
            next_delimiter = c
        elif c in 'rR':
            output += delimiter + '\n'
            next_delimiter = ''
        elif c in 'eE':
            output += delimiter
            break
        elif c.isdigit():
            output += delimiter + words[int(c)]
        elif c[-1] is '^':
            output += delimiter + words[int(c[:-1])].capitalize()
        elif c[-1] is '!':
            output += delimiter + words[int(c[:-1])].upper()

        delimiter = next_delimiter
        next_delimiter = ' '

    return output


# Introduction
print("Welcome to novel compression.")
print("Insert the amount of words, then words, then the chunk to decompress")
print("The chunks mean the following:")
print("1. '.,?!;:' mean their regular symbols")
print("2. 0 to however many numbers (minus one) will print a word")
print("3. '^' will capitalize the first letter")
print("4. '!' will make the whole word in caps lock")
print("5. '-' will put a '-' in-between two words instead of space")
print("6. 'R' will print a new line")
print("7. 'E' will be the end of the input")
print("\n~*~--------~*~\n")

# While loop
delimit = True
while delimit:
    n = raw_input("word range >>: ")
    words = []

    #quit case, or checks if digit
    if n.lower() == 'q':
        break
    if n.isdigit():
        #gets words for dict
        for i in range(int(n)):
            words.append(raw_input('words >> '))
        #after word loop, finish with the chunk
        try:
            chunk = raw_input('chunk >> ')
            print(decompress(words, chunk))
        except EOFError:
            break

raw_input("Press enter to exit.")

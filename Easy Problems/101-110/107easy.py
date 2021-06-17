# https://www.reddit.com/r/dailyprogrammer/comments/122c4t/10252012_challenge_107_easy_all_possible_decodings/

letters = ' abcdefghijklmnopqrstuvwxyz'


def decode(num="", output=""):
    # if no numbers
    if len(num) == 0:
        print(output)

    else:

        # Recursion to go through all possible decodings
        if int(num[:1]) in range(1, 10):
            decode(num[1:], output + letters[int(num[:1])])

        if len(num) > 1 and int(num[:2]) in range(1, 28):
            decode(num[2:], output + letters[int(num[:2])])


decoding = True
print("Welcome to decoder. 'q' will quit the program.")
print("\n~*~----------------~*~\n")

while decoding:
    decode_num = raw_input("Give me a digit: ")
    # if digit, print!
    if decode_num.isdigit():
        decode(decode_num)
    # exit code
    if decode_num == 'q' or decode_num == 'Q':
        decoding = False
        raw_input("Press enter to exit.")

# test cases:
# decode('123')
# decode('85121215')
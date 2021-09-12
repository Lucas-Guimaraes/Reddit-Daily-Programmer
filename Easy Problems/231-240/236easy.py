# https://www.reddit.com/r/dailyprogrammer/comments/3q9vpn/20151026_challenge_238_easy_consonants_and_vowels/

import random

#makes bag
def tetris_bag():
    bag = ['O', 'I', 'S', 'Z', 'L', 'J', 'T']
    random.shuffle(bag)
    return ''.join(bag)

#forms sequence
def tetris_seq(n):
    seq = ''
    while n > len(seq):
        seq += tetris_bag()
    # if not divisible by seven
    if len(seq) > n:
        seq = seq[:n]
    return seq

#checks fake bag, bonus
def tetris_validator(n):

    bag = ['O', 'I', 'S', 'Z', 'L', 'J', 'T']
    invalid_bag = [i * 3 for i in bag]
    if set(bag) != set(n):
        return False
    for i in invalid_bag:
        if i in n:
            return False
    else:
        return True

#Introduction code
print("Welcome to Tetris Sequence")
print("Put in a number, and you will get a Tetris Sequence for such")
print("Or, press 'validator' and insert your tetris sequence")
print("\n~*~----------------~*~\n")

#While loop
bag_form = True
while bag_form:
    how_many = raw_input().upper()
    #; three  options - Quit, Validate, and IsDigit
    if how_many == 'Q':
        break
    if how_many == 'VALIDATOR':
        tetris_test = raw_input().upper()
        print(tetris_validator((tetris_test)))
    if how_many.isdigit():
        print(tetris_seq(int(how_many)))



raw_input("Press enter to exit.")

#TEst cases
# print(tetris_seq(10))

#print(tetris_validator("LJOZISTTLOSZIJOSTJZILLTZISJOOJSIZLTZISOJTLIOJLTSZO"))
#print(tetris_validator("OTJZSILILTZJOSOSIZTJLITZOJLSLZISTOJZTSIOJLZOSILJTS"))
#print(tetris_validator("ITJLZOSILJZSOTTJLOSIZIOLTZSJOLSJZITOZTLJISTLSZOIJO"))
#print(tetris_validator("LJOZISTTTOSZIJOSTJZILLTZISJOOJSIZLTZISOJTLIOJLTSZO"))
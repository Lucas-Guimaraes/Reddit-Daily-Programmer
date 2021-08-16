#https://www.reddit.com/r/dailyprogrammer/comments/7p5p2o/20180108_challenge_346_easy_cryptarithmetic_solver/

import string
from itertools import permutations as perm

def cryptarithm(text):
    text = text.replace('==', '+').replace("\"", "").split(' + ')
    letters = ''.join(set(''.join(text)))
    p = (i for i in perm('0123456789', len(letters)))
    not_zero = {ord(i[0]):'0' for i in text if len(i)>1}

    for x in p:
        d = {i:j for (i, j) in zip(letters, x)}

        final = [[d[j] for j in i] for i in text]
        final = [int("".join(i)) for i in final]
        if sum(final[:-1]) == final[-1]:
            return {i:j for i, j in zip(letters, x)}

    return "No possible solution"

#Intro
print("Welcome to Cryptarihmetic Solver")
print("Example Input:")
print("\"WHAT + WAS + THY == CAUSE\"")
print("\n~*~----------------~*~\n")

#Run code
solving = True
while solving:
    code = raw_input()
    if code.lower() == 'q':
        break
    print(cryptarithm(code))

print("Press enter to exit")

#test case
#print(cryptarithm("THIS + IS + HIS == CLAIM"))
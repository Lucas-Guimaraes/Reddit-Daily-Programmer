# https://www.reddit.com/r/dailyprogrammer/comments/8q96da/20180611_challenge_363_easy_i_before_e_except/

import re


# (checks to see if 'ei' without starting with 'c' or 'iec')
def check(word):
    
    # CIE checker
    if 'cie' in word:
        return False
    
    #EI without 'C' checker
    ei = [m.start() for m in re.finditer('ei', word)]
    for i in ei:
        c_check = i - 1

        # Checks to not be in the back of index
        if c_check == -1:
            continue
        if word[c_check] != 'c':
            return False
    return True

#loops until user quits
print(""""Q" or "q" will quit the program \n""")
checking = True
while checking:
    str_put = raw_input()
    print(check(str_put))
    # Quit case.
    if str_put == "q" or str_put == "Q":
        break

raw_input("Press enter to exit.")

#print(check('a'))
#print(check('zombie'))
#print(check('transceiver'))
#print(check('veil'))
#print(check('icier'))
# cei -> TRUE!
# ei -> FALSE!
# ie -> TRUE!
# cie -> FALSE!
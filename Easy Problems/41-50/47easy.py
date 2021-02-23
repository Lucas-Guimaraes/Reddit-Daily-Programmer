# https://www.reddit.com/r/dailyprogrammer/comments/t33vi/522012_challenge_47_easy/


def caeser_cipher(string, shift, code):
    code = code.replace(' ', '')
    code = code.lower()
    decoded = ''
    encoded = ''
    is_caps = True
    char_num = 0
    shift_amt = 0
    if code == 'encode':
        for letter in string:

            letter_temp = ''

            if letter == ' ':
                encoded += letter
                continue
            elif letter.isalpha() == False:
                encoded += letter
                continue

            if letter.islower():
                is_caps = False
            else:
                is_caps = True

            if is_caps == False:
                letter_temp = letter
                letter_temp = letter_temp.upper()

                char_num = ord(letter)
                shift_amt = (char_num + shift) - 32
                shift_amt = check_num(shift_amt)
                letter_temp = chr(shift_amt)
                letter_temp = letter_temp.lower()

                encoded += letter_temp
            else:  # letter is already caps
                letter_temp = letter
                char_num = ord(letter)
                shift_amt = char_num + shift

                shift_amt = check_num(shift_amt)
                letter_temp = chr(shift_amt)
                encoded += letter_temp

        return encoded

    elif code == 'decode':
        for letter in string:

            letter_temp = ''

            if letter == ' ':
                decoded += letter
                continue
            elif letter.isalpha() == False:
                decoded += letter
                continue

            if letter.islower():
                is_caps = False
            else:
                is_caps = True

            if is_caps == False:
                letter_temp = letter
                letter_temp = letter_temp.upper()

                char_num = ord(letter)
                shift_amt = (char_num - shift) - 32
                shift_amt = check_num(shift_amt)
                letter_temp = chr(shift_amt)
                letter_temp = letter_temp.lower()

                decoded += letter_temp
            else:  # letter is already caps
                letter_temp = letter
                char_num = ord(letter)
                shift_amt = (char_num - shift)

                shift_amt = check_num(shift_amt)
                letter_temp = chr(shift_amt)
                decoded += letter_temp

        return decoded

    else:
        return "That's not valid"


def check_num(num):
    if num >= 91:
        num -= 26

    elif num <= 64:
        num += 26

    return num


print("Hello! Welcome to Caeser Cipher!")
print(
    "There are three inputs to this code:\n1) The string you want to encode or decode\n2) An amount to shift by\n3) Whether to encode or decode the given string")
print("\n~*~--------~*~\n")
# string object, shift object, code object
s_object = raw_input("Please give me the string to encode or decode:\n")
sh_object = int(raw_input("Now how much would you like to shift that by?:\n"))
c_object = raw_input(
    "Finally, encode or decode? The only valid inputs for this are the word 'encode' or the word 'decode:\n")
print("Now calculating...")
print("\n~*~--------~*~\n")
print(caeser_cipher(s_object, sh_object, c_object))

# print(caeser_cipher("""Spzalu - zayhunl dvtlu sfpun pu wvukz kpzaypibapun zdvykz pz uv ihzpz mvy h
# zfzalt vm nvclyutlua.  Zbwyltl leljbapcl wvdly klypclz myvt h thukhal myvt aol
# thzzlz, uva myvt zvtl mhyjpjhs hxbhapj jlyltvuf. Fvb jhu'a lewlja av dplsk
# zbwyltl leljbapcl wvdly qbza 'jhbzl zvtl dhalyf ahya aoyld h zdvyk ha fvb! P
# tlhu, pm P dlua hyvbuk zhfpu' P dhz hu ltwlylyvy qbza iljhbzl zvtl tvpzalulk
# ipua ohk sviilk h zjptpahy ha tl aolf'k wba tl hdhf!... Ho, huk uvd dl zll aol
# cpvslujl puolylua pu aol zfzalt! Jvtl zll aol cpvslujl puolylua pu aol zfzalt!
# Olsw! Olsw! P't ilpun ylwylzzlk!""", 7, 'decode'))
raw_input()
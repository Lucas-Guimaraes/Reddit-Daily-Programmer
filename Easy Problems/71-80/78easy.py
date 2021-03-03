# https://www.reddit.com/r/dailyprogrammer/comments/wrqbr/7182012_challenge_78_easy_keyboard_locale/
#this would be annoying to put input in for the user, so I opted not to
sub_shift = dict(zip("""`1234567890-=[]\;',./""", """~!@#$%^&*()_+{}|:\"<>?"""))
alternate_shift = {v: k for k, v in sub_shift.iteritems()}

#Lots of boolean switching
def keyboard_locale_simulator(string):
    print_string = ''
    hold = False
    caps = False
    shift = False
    held_down = True
    for letter in string:
        if letter == '^':
            hold = True
            continue

        if hold == True and letter == 'c':
            caps = True
            hold = False
            continue
        if hold == True and letter == 'C':
            caps = False
            hold = False
            continue

        if hold == True and letter == 's':
            shift = True
            hold = False
            continue

        if hold == True and letter == 'S':
            shift = False
            hold = False
            continue
        print_string += key_to_char(letter, caps, shift)

    return (print_string)

#this switches each key to upper and lower
def key_to_char(key, caps, shift):
    # checks for ONLY caps OR shift
    if key.isalpha():
        if caps == True and shift == False or caps == False and shift == True:
            if key.isupper():
                return key.lower()
            else:
                return key.upper()
        else:
            return key

    else:
        if shift == True:
            if key in sub_shift.keys():
                return sub_shift[key]
            elif key in alternate_shift.keys():
                return alternate_shift[key]
            else:
                return key
        else:
            return key


print(keyboard_locale_simulator("""^sm^Sy e-mail address ^s9^Sto send the ^s444^S to^s0^S is ^cfake^s2^Sgmail.com^C"""))
raw_input()

# either an 's' or 'S' for shift pressed or shift released, respectively, a 'c' or 'C' for caps on or caps off respectively, and a 't' 'T' for control down or up, and 'a' 'A' for alt down or up.,
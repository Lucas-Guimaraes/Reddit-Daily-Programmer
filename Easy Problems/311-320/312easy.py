#https://www.reddit.com/r/dailyprogrammer/comments/67dxts/20170424_challenge_312_easy_l33tspeak_translator/

#various dictionaries
leet_dict = {"A": '4',
"B": '6',
"E": '3',
"I": '1',
"L": '1',
"M": '(V)',
"N": '(\)',
"O": '0',
"S": '5',
"T": '7',
"V": '\/',
"W": '`//'}
lower_dict = {k.lower(): v for k, v in leet_dict.items()}
reverse_dict = {v: k.lower() for k, v in leet_dict.items()}

#translates sentence
def leet_translate(sen):
    new_w = ''
    count, two_skip, three_skip = 0, False, False

    #accounts for leet exceptions
    for i in range(len(sen)):
        idx = sen[i]
        if two_skip:
            two_skip = False
            continue
        if three_skip:
            count += 1

            if count == 2:
                three_skip = False
            continue


        #for the big leet speak
        if len(sen)-2 > i:

            two_l = idx + sen[i+1]
            three_l = two_l + sen[i+2]

            if two_l in reverse_dict.keys():
                new_w += reverse_dict[two_l]
                two_skip = True
                continue
            if three_l in reverse_dict.keys():
                new_w += reverse_dict[three_l]
                three_skip = True
                continue
        
        #adds proper dictionary
        if sen[i] in leet_dict.keys():
            new_w += leet_dict[idx]
        elif sen[i] in lower_dict.keys():
            new_w += lower_dict[idx
            ]
        elif sen[i] in reverse_dict.keys():
            new_w += reverse_dict[idx]
        else:
            new_w += idx
    
    #capitalizes the first letter in-case it's not 'l33t'
    new_w = new_w[0].upper() + new_w[1:]
    return new_w

#Introduction
print("Welcome to leet translator")
print("This will take a word and translate it to L33T")
print("...oh, and it automatically works in the reverse fashion.")
print("\n~*~--------~*~\n")

#While loop
translating = True
while translating:
    w = raw_input()
    if w.lower() == 'q':
        break
    print(leet_translate(w))

raw_input("Press enter to exit.")

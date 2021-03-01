# https://www.reddit.com/r/dailyprogrammer/comments/217klv/4242014_challenge_154_easy_march_madness_brackets/

import re

def unpack_string(string):
    lst = []
    b_lst = []
    bracket_start = ['[', '{', '(']
    all_bracket = bracket_start + [']', '}', ')']
    for r in range(len(string)):
        if string[r] in bracket_start:
            lst.append(r)

    if len(lst) == 0:
        return string

    mod_str = ''
    temp_str = string

    new_lst = reversed(lst)

    for i in new_lst:

        find = string[i]

        result = 0
        if find == '[':
            result = temp_str.find(']')
        elif find == '(':
            result = temp_str.find(')')
        elif find == '{':
            result = temp_str.find('}')
        mod_str += temp_str[i+1:result]
        temp_str = temp_str[:i] + temp_str[result+1:]
        if mod_str[-1] != ' ':
            mod_str += ' '
        mod_str = re.sub(' +', ' ', mod_str)
    return mod_str


print("Welcome to bracket decoder!")
print("This program takes one input: A string")
print("Afterwards, it will decode your message from that string.")
print("\n~*~----------------~*~\n")
str_decode = raw_input("Put your string to decode: \n")
print(unpack_string(str_decode))
raw_input("Press Enter to exit.")


#print(unpack_string('((your[drink {remember to}]) ovaltine)'))
#print(unpack_string('[racket for {brackets (matching) is a} computers]'))
#print(unpack_string('[can {and it(it (mix) up ) } look silly]'))
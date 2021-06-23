# https://www.reddit.com/r/dailyprogrammer/comments/1q6pq5/11413_challenge_140_easy_variable_notation/
import string

#Converts a string into camelcase
def camelcase(convert_str):
    str_lst = list(convert_str)
    new_lst = []
    skip_letter = False
    for letter in str_lst:
        #Accounts for any spaces
        if skip_letter == True:
            skip_letter = False
            pass
        
        #If the letter is a space, we want to add the next index
        elif letter == ' ':
            cur_idx = str_lst.index(letter) + 1
            cur_letter = str_lst[cur_idx]
            cur_letter = cur_letter.upper()
            new_lst.append(cur_letter)
            skip_letter = True

        else:
            new_lst.append(letter)

    camel_str = "".join(new_lst)
    return (camel_str)

#Converts a string into snakecase
def snakecase(convert_str):
    snakecase = convert_str.replace(' ', '_')
    return snakecase

#Converts a string into snake case - WITH added capitalization
def snakecasecaps(convert_str):
    snakecasecaps = convert_str.replace(' ', '_')
    snakecasecaps = snakecasecaps.upper()
    return snakecasecaps

#Converts from one snake case to another
def conversion(caps_type, new_id, convert_str):
    if caps_type == 0:
        caps_lst = list(convert_str)
        new_lst = caps_lst
        while set(new_lst) in set(string.ascii_uppercase):
            for letter in caps_lst:
                if caps_lst.upper():
                    new_lst.insert(caps_lst.index(letter), ' ')

        convert_str = ''.join(new_lst)

        convert_str = convert_str.lower()

    elif caps_type == 1:
        convert_str = convert_str.replace('_', ' ')
    elif caps_type == 2:
        convert_str = convert_str.replace('_', ' ')
        convert_str = convert_str.lower()

    if new_id == 0:
        return camelcase(convert_str)
    elif new_id == 1:
        return snakecase(convert_str)
    elif new_id == 2:
        return snakecasecaps(convert_str)

#Various test cases
print(conversion(1, 0, 'hello_world'))
print(camelcase('hello world'))
print(snakecase('hello world'))
print(snakecasecaps('hello world'))

raw_input("Press enter to exit.")
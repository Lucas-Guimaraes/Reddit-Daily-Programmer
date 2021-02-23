# https://www.reddit.com/r/dailyprogrammer/comments/tux8f/5192012_challenge_54_easy/

from random import choice
from string import ascii_lowercase
from math import floor, ceil


def matrix_cipher(str_put, key_amt, code):
    code = code.lower()
    if code == 'encode':

        initial_len = len(str_put)
        row_count = int(ceil(initial_len / key_amt))

        check_count = True
        remainder = 0

        while check_count:
            if initial_len % key_amt == 0:
                check_count = False
            else:
                initial_len += 1
                remainder += 1

        if remainder > 0:
            row_count += 1
        temp_lst = list(str_put)

        for i in range(remainder):

            temp_lst.append(choice(ascii_lowercase))

        matrix = []

        for row in range(row_count):
            n_row = []
            for i in range(key_amt):

                if temp_lst[0] == ' ':
                    temp_lst.pop(0)
                    n_row.append('_')
                else:
                    n_row.append(temp_lst.pop(0))
            n_row = " ".join(n_row)
            matrix.append(n_row)

        for row in matrix:
            print(row)

    elif code == 'decode':
        row_count = int(floor(len(str_put) / key_amt))
        remainder = len(str_put) % key_amt
        row_count += remainder

        new_str = str_put
        print(new_str)

        new_str = new_str.replace("/n", "")
        new_str = new_str.replace(" ", "")
        new_str = new_str.replace("_", " ")
        print(new_str)

print("Welcome to matrix cipher!\n")
print("This string will take three inputs:\n1) The string \n2) The akey amount to shift by \n3) Whether to encode or decode\n")
print("Example Input #1:\n")
print("'T h e _ c a k e _ i s _ a _ l i e !', 3, 'decode'")
print("Example Output #1:\n")
matrix_cipher('T h e _ c a k e _ i s _ a _ l i e !', 3, 'decode')
print("Example Input #2:\n")
print("""The cake is a lie!", 3, 'encode'""")
print("Example Output #2:\n")
matrix_cipher("The cake is a lie!", 3, 'encode')
s_obj = raw_input("\nPlease input a string to encode or decode:\n")
k_obj = int(raw_input("By how many spaces?\n"))
c_obj = raw_input("Last question. Encode or decode?:\n")
print("This is your result:")
matrix_cipher(s_obj, k_obj, c_obj)
raw_input("\nPress enter to exit")

#matrix_cipher('T h e _ c a k e _ i s _ a _ l i e !', 3, 'decode')
#matrix_cipher("The cake is a lie!", 3, 'encode')
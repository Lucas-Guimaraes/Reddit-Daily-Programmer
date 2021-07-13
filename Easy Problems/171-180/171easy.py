# https://www.reddit.com/r/dailyprogrammer/comments/2ao99p/7142014_challenge_171_easy_hex_to_8x8_bitmap/

bitmap_dict = {'0': '0000',
'1': '0001',
'2': '0010',
'3': '0011',
'4': '0100',
'5': '0101',
'6': '0110',
'7': '0111',
'8': '1000',
'9': '1001',
'A': '1010',
'B': '1011',
'C': '1100',
'D': '1101',
'E': '1110',
'F': '1111'}

valid_bitmap = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


# handles checking if the input is a valid bitmap
def bitmap_check(s):
    if len(s) != 2:
        return False
    for x in s:
        if x in valid_bitmap:
            continue
        else:
            return False


# handles printing
def bitmap_to_ascii(l):
    bin_lst = []
    bin_str = []
    # gets binary
    for i in l:
        bin_str = bitmap_dict[i[0]] + bitmap_dict[i[1]]
        bin_lst.append(bin_str)

    # makes binary into printable ascii
    for x in bin_lst:
        ascii_str = ''
        for i in x:
            if i == '0':
                ascii_str += ' '
            else:
                ascii_str += '*'
        print(ascii_str)


print("Welcome to hex_ascii!")
print("You will give an input: 8 ascii formats spelled")
print("\n~*~----------------~*~\n")

# Loops program until user quits
hex_ascii = True
while hex_ascii:
    ascii_input = raw_input("").upper()

    ascii_lst = ascii_input.split()
    trigger = True

    if ascii_input == 'Q':
        break

    # checks for 8 items
    if len(ascii_lst) != 8:
        trigger = False
        continue

    # makes sure every item in list is valid
    for i in ascii_lst:
        check = bitmap_check(i)
        if check == False:
            trigger = False
    # if our trigger is true...
    if trigger == True:
        bitmap_to_ascii(ascii_lst)
raw_input("Press enter to exit")

#test cases:
#18 3C 7E 7E 18 18 18 18
#FF 81 BD A5 A5 BD 81 FF
#AA 55 AA 55 AA 55 AA 55
#3E 7F FC F8 F8 FC 7F 3E
#93 93 93 F3 F3 93 93 93
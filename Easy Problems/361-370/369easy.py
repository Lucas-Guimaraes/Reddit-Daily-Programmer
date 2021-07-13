# https://www.reddit.com/r/dailyprogrammer/comments/a0lhxx/20181126_challenge_369_easy_hex_colors/

import math

def hex_convert(n):
    h = [(10, 'A'), (11, 'B'), (12, 'C'), (13, 'D'), (14, 'E'), (15, 'F')]
    if n > 9:
        return h[n % 10][1]
    else:
        return n

def rgb_to_hex(r, g, b):
    dec_one = float(r) / float(16)
    one = str(hex_convert(int(math.floor(dec_one))))
    two = str(hex_convert(int(math.floor((dec_one - math.floor(dec_one)) * 16))))

    dec_three = float(g) / float(16)
    three = str(hex_convert(int(math.floor(dec_three))))
    four = str(hex_convert(int(math.floor((dec_three - math.floor(dec_three)) * 16))))

    dec_five = float(b) / float(16)
    five = str(hex_convert(int(math.floor(dec_five))))
    six = str(hex_convert(int(math.floor((dec_five - math.floor(dec_five)) * 16))))


    hex_value = '#' + one + two + three + four + five + six

    return hex_value

def valid_rgb(s):
    if s.isdigit():
        if 255 >= int(s) >= 0:
            return True
    return False

print("Welcome to RGB to hex!")
print("Example input:")
print("255, 99, 71")
print("Example output:")
print("#FF6347")
print("\n~*~----------------~*~\n")

converting = True

while converting:
    color = raw_input()
    if color == 'q' or color == 'Q':
        break
    color = color.replace(' ', '')
    color = color.split(',')
    
    if len(color) == 3:
        r, g, b = color[0], color[1], color[2]
        if valid_rgb(r) and valid_rgb(g) and valid_rgb(b):
            print(rgb_to_hex(int(r), int(g), int(b)))
    
raw_input("Press enter to exit.")

#test cases
#print(rgb_to_hex(220, 99, 71))
#print(rgb_to_hex(255, 99, 71))
#print(rgb_to_hex(184, 134, 11))
#print(rgb_to_hex(189, 183, 107))
#print(rgb_to_hex(0, 0, 2))
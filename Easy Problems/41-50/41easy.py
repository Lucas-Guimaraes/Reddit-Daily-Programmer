# https://www.reddit.com/r/dailyprogrammer/comments/shp28/4192012_challenge_41_easy/

import textwrap

def fancy_wrap(plaintext):
    #textwrap helps us get pretty results; this helps us split the line for every 76 characters
    wrapped_text = textwrap.wrap(plaintext, 76)
    max_line_length = max(len(line) for line in wrapped_text)
    full_line_length = max_line_length + 4
    space_line_length = full_line_length - 2
    print '*' * full_line_length
    print '*' +  ' ' * space_line_length + '*'
    for line in wrapped_text:
        print '* {0} *'.format(line.center(max_line_length))
    print '*' +  ' ' * space_line_length + '*'
    print '*' * full_line_length

print("*--------*--------*")
print("Hello! Welcome to Fancy Text")
print("*--------*--------*")
raw_input("Press Enter to Continue")
print("*--------*--------*")
print("This application takes one input - a sentence")
print("We use this sentence print it out in a fancy format")
print("*--------*--------*")
raw_input("Press Enter to Continue")
print("*--------*--------*")
text = raw_input("Please give me a sentence! ")
fancy_wrap(text)
raw_input("Press Enter to Exit")
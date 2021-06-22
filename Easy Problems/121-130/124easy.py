# https://www.reddit.com/r/dailyprogrammer/comments/1ds3sn/050613_challenge_124_easy_newline_troubles/

#This program is the same as the '123easyextra.py' file.
#124easyfile.txt is the supplementary file
def newline_fixer(file, os):
    opened_file = open(file)
    for line in opened_file.readlines():
        #If the OS is windows, it will remove any instance of '\n' written down
        if os == 'windows':
            print(line.replace('\n', ''))
        #If this is for Unix, it will instead make every '\n' into a proper '/r'
        else:
            print(line.replace('\n', '/r'))
fn = '124easyfile.txt'
newline_fixer(fn, 'windows')
newline_fixer(fn, 'unix')
raw_input()
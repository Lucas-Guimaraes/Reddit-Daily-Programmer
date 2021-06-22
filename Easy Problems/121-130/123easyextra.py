#https://www.reddit.com/r/dailyprogrammer/comments/1dbpm9/042913_challenge_123_easy_newline_troubles/
#This program will take a windows file, or unix, and fix what newline characters are used
#123testfile.txt is a supplementary file to this one.
#This code is outdated compared to 124easy.py

def newlinefix(file, os):
    read_file = open(file, 'r+')
    read_lines = read_file.readlines()
    for line in read_lines:
        #adds 'r\n' into all new lines
        if os == "windows":
            print(line.replace("""\r\n""", """\n""").replace("""\n""", """\r\n"""))
        #replaces all 'r\n' with '\n'
        elif os == "unix":
            print(line.replace("""\r\n""", """\n"""))
    return
    
#og = original 
og = '123testfile.txt'

newlinefix(og, 'unix')
    
raw_input()

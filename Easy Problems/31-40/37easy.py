# https://www.reddit.com/r/dailyprogrammer/comments/rzdwq/482012_challenge_37_easy/
#for this to work, a text file is necessary 
def line_count(file):
    lines_to_count = open(file, 'r')
    line_c = 0
    word_c = 0
    for line in lines_to_count.readlines():
        line_c += 1
        line_split = line
        line_split = line_split.split()

        for word in line_split:
            word_c += 1
    return line_c, word_c

print(line_count('37easytest.txt'))
raw_input("Press enter to exit")
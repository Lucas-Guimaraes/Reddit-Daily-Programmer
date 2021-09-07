#https://www.reddit.com/r/dailyprogrammer/comments/3esrkm/20150727_challenge_225_easyintermediate/

#225easy is a supplementary file

lines = open('225easy.txt', "r").readlines()
indent = '****'
final = []
space = [" "]
for line in lines:

    line = line.replace("\n", "")
    if line[0] == "|" or line[0] == "+":
        if len(line) - line[::-1].find(line[0]) == 1:
            if line[0] == "|":
                line = line[len(line) - line[::-1].find("+"):]
            else:
                line = line[len(line) - line[::-1].find("|"):]

        else:
            line = line[len(line)-line[::-1].find(line[0]):]
    if line[-1] == "|" or line[-1] == "+":
        line = line[:line.find(line[-1])]

    if set(space) != set(line):
        line = line.lstrip(' ').rstrip(' ')

    if line != " ":
        final.append(line)

for f in final:
    print(f)


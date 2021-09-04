#https://www.reddit.com/r/dailyprogrammer/comments/4lpygb/20160530_challenge_269_easy_basic_formatting/

lines = open('269easysupplement.txt', "r").readlines()
indent = '****'
final = []
for line in lines:
    line = line.replace("\n", "")
    line = line.replace(".", "")

    if "THEN" in line or "IF" in line:
        final.append(indent + line)
    elif "PRINT" in line:
        final.append((indent * 2) + line)
    else:
        final.append(line)

for f in final:
    print(f)


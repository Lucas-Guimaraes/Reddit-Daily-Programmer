# https://www.reddit.com/r/dailyprogrammer/comments/72ivih/20170926_challenge_333_easy_packet_assembler/

import sys

lst = []


#ctrl+d to make the program run
#For every line in the input
for line in sys.stdin:
    line = line.replace('\t', ' ')
    x, y, z, t = line.split(' ', 3)
    t = t.replace('\n', '')
    n = (int(x), int(y), int(z), t)
    lst.append(n)

#Sort list, then print
lst.sort(lambda x, y: cmp(x, y))

for l in lst:
    l = [str(x) for x in l]
    l = ' '.join(l)
    print(l)

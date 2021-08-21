#https://www.reddit.com/r/dailyprogrammer/comments/2hssx6/29092014_challenge_182_easy_the_column_conundrum/
import textwrap

text = ''
f = open("182easyloremipsum.txt", "r")

#prepares our date list
for line in f.readlines():
    text += line.replace("\n", "")
    

columns = 4
columns_width = 10
space = 2

def chunks(t, n):
    c = sum(divmod(len(t), columns))
    for i in range(0, len(t), c):
        yield t[i:i + c]

new_columns = chunks(textwrap.wrap(text, columns_width), columns)
output = zip(*new_columns)

for l in output:
    print(space * ' ').join(map(lambda x: x.ljust(columns_width), l))      

raw_input()
# https://www.reddit.com/r/dailyprogrammer/comments/4gc24w/20160425_challenge_264_easy_sort_my_code/

zero_tab, one_tab, two_tab = [], [], []
zero_sort, one_sort = [], []

for line in open("264easy.txt"):

    if line[0] != ' ':
        zero_tab.append(line)
    elif line[2] != ' ':
        one_tab.append(line)
    elif line[4] != ' ':
        two_tab.append(line)

#sorts zero tab
zero_sort = [i for i in zero_tab if '#' in i]
zero_sort.append('')
zero_sort = zero_sort + [i for i in zero_tab if 'int' in i]
zero_sort = zero_sort + [i for i in zero_tab if '{' in i]
zero_sort = zero_sort + [i for i in zero_tab if '}' in i]

#sorts one tab
one_sort = [i for i in one_tab if 'int sum' in i]
one_sort = one_sort + [i for i in one_tab if 'for' in i]
one_sort = one_sort + [i for i in one_tab if '{' in i]
one_sort = one_sort + [i for i in one_tab if '}' in i]
one_sort = one_sort + [i for i in one_tab if 'std' in i]
one_sort = one_sort + [i for i in one_tab if 'return' in i]

new_code = zero_sort[0:4] + one_sort[0:3] + two_tab + one_sort[3:] + zero_sort[4:]
new_code = [i.replace('\n', '') for i in new_code]

for n in new_code:
    print(n)

raw_input("\nPress enter to exit.")
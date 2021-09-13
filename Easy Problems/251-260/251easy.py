# https://www.reddit.com/r/dailyprogrammer/comments/42lhem/20160125_challenge_251_easy_create_nonogram/
import sys

def count_columns(lst):
    cols = []
    highest_c = 0
    for l in lst:
        l = "".join(l)
        l = [x for x in l]
        cols.append(l)


    cols_t = zip(*cols)
    cols_t = [list(c) for c in cols_t]

    col_count_dict = {}
    final = 0
    count = 0
    idx = 0
    col_count_lst = []

    for x in cols_t:
        for i in x:
            final += 1

            if i == '@':
                if count > 0:
                    col_count_lst.append(str("{}").format(count))
                count = 0
            if i == '*':
                count += 1
            if final == len(cols_t):
                if count > 0:
                    col_count_lst.append(str("{}").format(count))

                idx += 1
                count = 0
                final = 0
                col_count_dict[idx] = col_count_lst
                col_count_lst = []

    cols_organized = []
    for k, v in col_count_dict.items():
        cols_organized.append(v)

    highest_c = 0
    for a in cols_organized:
        if len(a) > highest_c:
            highest_c = len(a)

    new = []
    new_dict = {}

    for i in range(highest_c):
        for a in cols_organized:
            try:
                new.append(a[i])
            except:
                new.append(' ')
        new_dict[i] = new
        new = []

    cols_organized = []
    for k, v in new_dict.items():
        cols_organized.append(v)

    new_lst = []
    for x in cols_organized:
        x = " ".join(x)
        new_lst.append(x)

    return new_lst[::-1]


def count_rows(lst):
    rows = []
    highest_c = 0
    for l in lst:
        nonogram_row = []
        gram_string = "".join(l)
        count = 0
        for i in range(len(gram_string)):
            if gram_string[i] == "@" and count > 0:
                nonogram_row.append(str("{} ").format(count))
                count = 0

            elif i == len(gram_string) - 1:
                if gram_string[i] == "*":
                    count += 1
                if count >= 1:
                    nonogram_row.append(str("{} ").format(count))

            elif gram_string[i] == "*":
                count += 1

        check_c = len(nonogram_row)
        if check_c > highest_c:
            highest_c = check_c

        rows.append(nonogram_row)

    new_rows = []
    for x in rows:
        times = highest_c - len(x)
        if times > 0:
            #Do more with formatting
            x = "".join(x)
            x = ("  " * times) + x
            x = list(x)
        new_rows.append(x)
    return new_rows


# ctrl+d to make the program run
# For every line in the input
lst = []
for line in sys.stdin:
    line = line.replace(' ', '@')
    line = line.split()
    lst.append(line)

nonogram_columns = count_columns(lst)
nonogram_rows = count_rows(lst)

print("\nColumns:")
for c in nonogram_columns:
    print(c)

print("\nRows:")
for r in nonogram_rows:
    r = ''.join(r)
    print(r)
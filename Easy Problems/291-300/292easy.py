#https://www.reddit.com/r/dailyprogrammer/comments/5d1l7v/20161115_challenge_292_easy_increasing_range/

def do(s):
    s = s.split(',')
    s = map(lambda s: s.replace(':', '-').replace('..', '-').split('-'), s)
    l = [0]
    for entry in s:
        entry[0] = get_number(l[-1], entry[0])
        if len(entry) == 1:
            l.append(entry[0])
        else:
            l += get_seq(*entry)
    return ' '.join(str(i) for i in l[1:])

def get_seq(prev, s, inc=1):
    return range(prev, get_number(prev,s)+1, int(inc))

def get_number(prev, s):
    ex = len(s)
    n = int(str(prev)[:-ex] + s)
    return n if prev < n else n + 10**ex

print("Input a range - only numbers and ',' '..' ':' and '-' are valid characters")
print("Output will be the range of numbers")
print("\n~*~--------~*~\n")

parsing = True

while parsing:
    parsing_str = raw_input()
    if parsing_str.lower() == 'q':
        break

    print(do(parsing_str))

raw_input("Press enter to exit.")

#Test Cases
"""
challenges=[
"1,3,7,2,4,1",
"1-3,1-2",
"1:5:2",
"104-2",
"104..02",
"545,64:11",
]
for c in challenges:
    print(do(c))
"""
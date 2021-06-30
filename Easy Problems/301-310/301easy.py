# https://www.reddit.com/r/dailyprogrammer/comments/5rlpz1/20170202_challenge_301_easyintemerdiate_looking/

# '301easysupplement.txt' is a supplementary file

from re import compile

# Opens the file
with open('301easysupplement.txt') as f:
    words = f.readlines()


# Finds all matches
def find_pattern(pattern, words):
    lst = [word[:-1] for word in words if pattern.search(word)]
    for i in lst:
        print(i)


# Makes whichever pattern the user inputs
def make_pattern(pattern):
    new_pat = ""
    if pattern == "XXYY":
        new_pat = compile("(.)\\1(?:(?!\\1)(.))\\2")
    elif pattern == "XXYYZZ":
        new_pat = compile("(.)\\1(?:(?!\\1)(.))\\2(?:(?![\\1\\2])(.))\\3")
    elif pattern == "XXYYX":
        new_pat = compile("(.)\\1(?:(?!\\1)(.))\\2\\1")
    return new_pat

#Program explination
print("Welcome to pattern finder!")
print("The following patterns are workable:")
print("XXYY, XXYYZZ, XXYYX")
print("\n~*~----------------~*~\n")

valid_pat = ['XXYY', 'XXYYZZ', 'XXYYX']
patterns = True

#Patterns
while patterns:

    pat = raw_input()
    pat = pat.upper()
    if pat == 'q' or pat == 'Q':
        patterns = False
        break
    if pat in valid_pat:
        pat = make_pattern(pat)
        find_pattern(pat, words)
        
raw_input("Press enter to exit.")

# Compile input could be created from the input pattern
#Couldn't quite get it working
#    elif pattern == "XYYX":
#        new_pat = compile("(.)\\1\\2")

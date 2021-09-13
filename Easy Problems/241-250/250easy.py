#https://www.reddit.com/r/dailyprogrammer/comments/41hp6u/20160118_challenge_250_easy_scraping/

#raw.txt is a supplementary file

from collections import defaultdict

#Opens all dailyprogrammer URL's
lines = open('raw.txt', "r").readlines()

#Checks which difficulty the link is a part of
def difficulty(s):
    if "easy" in s:
        return "easy"
    elif "intermediate" in s:
        return "medium"
    else:
        return "hard"

#Creates default dictionary to append
d = defaultdict(list)

#Scrapes every line to see if "_{}_ or _{}" num is in the URL
for i in lines:
    for x in range(1, 6):
        if "_{}_".format(x) in i or "_{}/".format(x) in i:
            d[str(x)].append(difficulty(i))

#Final sort
for k, v in sorted(d.items()):
    print(k + ": " + " ".join(v))


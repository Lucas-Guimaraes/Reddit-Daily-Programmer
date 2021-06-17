#https://www.reddit.com/r/dailyprogrammer/comments/11xje0/10232012_challenge_106_easy_random_talker_part_1/

#'106easybook.txt' is a supplementary file

import re

def word_count(book):
    r = open(book)
    r = r.read()
    
    text = re.findall(r'[".,:;!?()\[\]{}]|\w+', r.lower())
    #counts all unique occurances of each individual unique word
    count = [(text.count(w), w) for w in set(text)]
    #Sorts the highest ten
    top_ten = sorted(count)[-10:]
    top_ten = top_ten[::-1]
    for c in top_ten:
        print c[0], c[1]
        
word_count('106easybook.txt')
raw_input()
#https://www.reddit.com/r/dailyprogrammer/comments/3j3pvm/20150831_challenge_230_easy_json_treasure_hunt/

import json

f = open('dailyprogrammer.json',)
data = json.load(f)
for x, v in data.items():
    if 'dailyprogrammer' in v:
        print '{} -> 1'.format(x)
        break
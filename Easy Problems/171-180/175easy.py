#https://www.reddit.com/r/dailyprogrammer/comments/2d8yk5/8112014_challenge_175_easy_bogo/
import random
def bogo(scram, final):
    l = list(scram)
    count = 0
    while scram != final:
        random.shuffle(l)
        result = ''.join(l)
        count += 1
        if result[0] != final[0]:
            random.shuffle(l)
            result = ''.join(l)
            count += 1
    return count
    
print(bogo('lolhe', 'hello'))
#https://www.reddit.com/r/dailyprogrammer/comments/32goj8/20150413_challenge_210_easy_intharmonycom/

def compatability(a, b):
    x = '{:032b}'.format(a)
    y = '{:032b}'.format(b)
    count = 0
    for i in range(x):
        if x[i] == y[i]:
            count += 1
    count = count / 32.0
    return count
    
def opposite(x):
    return x ^ 0xFFFFFFFF

print(compatability(100, 42))
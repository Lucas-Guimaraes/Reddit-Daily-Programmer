#https://www.reddit.com/r/dailyprogrammer/comments/56tbds/20161010_challenge_287_easy_kaprekars_routine/

def kaprekar_routine(i):
    s = str(i)
    s = [int(x) for x in s]
    new = ''
    while len(s) > 0:
        new += str(max(s))
        s.remove(max(s))
    return int(new)

print(kaprekar_routine(1234))
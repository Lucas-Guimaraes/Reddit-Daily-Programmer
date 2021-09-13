#https://www.reddit.com/r/dailyprogrammer/comments/5196fi/20160905_challenge_282_easy_unusual_bases/

def fib_base(n):
    fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    #base = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]

    fib_seq = len(str(n))
    total = 0
    cur = 0
    for i in reversed(range(fib_seq)):
        if n[cur] == '1':
            total += fib[i]
        cur += 1
    return total

print(fib_base("1010010"))

# https://www.reddit.com/r/dailyprogrammer/comments/schtf/4162012_challenge_40_easy/
def p1000(num=1):
    print(num)
    print(num+1)
    print(num+2)
    print(num+3)
    print(num+4)
    print(num+5)
    print(num+6)
    print(num+7)
    print(num+8)
    print(num+9)
    if num and num < 990:
        p1000(num + 10)


p1000()
raw_input("Press enter to exit")


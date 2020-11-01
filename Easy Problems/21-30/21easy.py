#https://www.reddit.com/r/dailyprogrammer/comments/qp3ub/392012_challenge_21_easy/

def higher_num(num):
    count = num+1
    while True:
        if str(num) in str(count):
            False
            return count
        else:
            count = count+1

num_test = int(raw_input("Put in a number!: "))
print higher_num(num_test)

raw_input()
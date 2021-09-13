#https://www.reddit.com/r/dailyprogrammer/comments/2onyoq/2014128_challenge_192_easy_carry_adding/

def carry_add(i):
    inputs = i.split('+')
    numbers = [s.rjust(max(map(len, inputs)), '0') for s in inputs]
    columns = [[0]] + [map(int, t) for t in zip(*numbers)]
    answer = ''
    carry = ' '

    while columns:
        n = sum(columns.pop())
        if n > 9:
            carry = str(n / 10) + carry
            columns[-1] += [n/10]
            n = n % 10
        else:
            carry = ' ' + carry
        answer = str(n) + answer

    if answer[0] == '0':
        answer = answer[1:]
        carry = carry[1:]

    for s in inputs:
        print(s.rjust(len(answer)))

    print '-' * len(answer)
    print answer
    print '-' * len(answer)
    print carry[1:]

#Input
print("Welcome to Carry Add.")
print("This program works with a set of numbers separated with '+' symbols")
print("The output will be the carry addition of these numbers")
print("\n~*~----------------~*~\n")

#Run Code

carrying = True

while carrying:
    c = raw_input()
    if c.lower() == "q":
        break
    if '+' in c:
        carry_add(c)

raw_input("Press enter to exit.")

#Test cases
#carry_add('23+9+66')
#carry_add('559+447+13+102')
#https://www.reddit.com/r/dailyprogrammer/comments/46zm8m/20160222_challenge_255_easy_playing_with_light/

#'255easy.txt', '255easy2.txt', '255easy3.txt'

f = open("255easy.txt", "r")
first = int(f.readline())
light_amount = ['*' for i in range(first)]
second = []

for i in f:
    x = i.split()
    second.append((int(x[0]), int(x[1])))

for x in second:
    lower, higher = x[0], x[1]
    if lower > higher:
        lower, higher = higher, lower
    for i in range(lower-1, higher):
        if light_amount[i] == '*':
            light_amount[i] = '@'
        else:
            light_amount[i] = "*"

print(light_amount.count("@"))
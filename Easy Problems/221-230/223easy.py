# https://www.reddit.com/r/dailyprogrammer/comments/3d4fwj/20150713_challenge_223_easy_garland_words/

def garland(w):
    degree = 0
    for n in range(len(w)):
        if w[:n] == w[-n:]:
            degree = max(degree, n)
    return degree


print("Welcome to garland word!")
print("Give a string, please")
print("Afterwords, the output will be its Garland Degree")
print("\n~*~----------------~*~\n")

typing = True
while typing:
    w = raw_input().lower()
    if w == 'q':
        break
    print(garland(w))

print("Press enter to exit")

# test cases
# print(garland('onion'))
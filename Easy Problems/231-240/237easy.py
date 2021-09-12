# https://www.reddit.com/r/dailyprogrammer/comments/3pcb3i/20151019_challenge_237_easy_broken_keyboard/

# '237easy.txt' is a supplementary file

file = open('237easy.txt', 'r')
word_lst = []
for line in file.readlines():
    new = line.replace("\n", "")
    word_lst.append(new)


def broken_keyboard(letters):
    cur_word = ''
    for word in word_lst:
        w = "".join(set(word))
        l = "".join(set(letters))
        if w in l and len(word) > len(cur_word):
            cur_word = word
    return "{} = {}".format(letters, cur_word)


print("Welcome to Broken Keyboard")
print("Use a list of words and we'll print out the largest word")
print("\n~*~----------------~*~\n")

while True:
    lines = raw_input()
    lst = []
    if lines.isdigit():
        for i in range(int(lines)):
            lst.append(broken_keyboard(raw_input()))
        print(lst)
        break

raw_input("\nPress enter to exit.")
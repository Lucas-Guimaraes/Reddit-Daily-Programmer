#https://www.reddit.com/r/dailyprogrammer/comments/2jt4cx/10202014_challenge_185_easy_generated_twitter/

#'185easywords.txt' is a supplementary file to this challenge

word_lst = []
f = open("185easywords.txt", "r")

for line in f.readlines():
    new = line.replace("\n", "")
    word_lst.append(new)
f.close()

for w in word_lst:
    if len(w) > 1:
        if w[0] == "a" and w[1] == "t":
            print("@{} : {}".format(w[2:], w))

raw_input("\nPress enter to exit.")

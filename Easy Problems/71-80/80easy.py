# https://www.reddit.com/r/dailyprogrammer/comments/x0v3e/7232012_challenge_80_easy_anagrams/


def anagrams(word):
    word = word.strip().upper()
    lst = []
    tempdict = open("80easydict.txt", "r")
    
    for x in tempdict.readlines():
        if set(word) == set(x.strip().upper()) and len(x.strip().upper()) == len(word):
            lst.append(x.strip().upper())
    tempdict.close()
    return lst


print(anagrams('marbles'))

raw_input()
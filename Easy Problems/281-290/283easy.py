#https://www.reddit.com/r/dailyprogrammer/comments/52enht/20160912_challenge_283_easy_anagram_detector/

def anagram_check(a, b):
    #new words
    c, d = '', ''
    for x in a:
        if x.isalpha():
            c += x.lower()
    for y in b:
        if y.isalpha():
            d += y.lower()
    if sorted(c) == sorted(d):
        return "{} is an anagram of {}".format(a, b)
    else:
        return "{} is NOT an anagram of {}".format(a, b)

print("Welcome to Anagram Checker")
print("""Example Input: "Clint Eastwood" ? "Old West Action" """)
print("\n~*~--------~*~\n")

a_check = True
while a_check:
    w = raw_input()
    if w.lower() == 'q':
        break
    if "?" in w:
        w1, w2 = w.split("?")
        w1, w2 = w1[1:len(w1)-2], w2[2:len(w2)-1]
        print(anagram_check(w1, w2))

raw_input("Press enter to exit.")
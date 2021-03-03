#https://www.reddit.com/r/dailyprogrammer/comments/w1e7x/742012_challenge_72_easy/

print("Input two numbers in a range of 1 to 40.")
print("Example input:")
print("38, 39")
i=input("Input your range: ")
print("Now your line amount (Tip: Maybe make it higher than your range!")
o=int(input("How about your line amount?: "))
o=range(o)
l=''.join(' X'[c in i]for c in o)
for r in o:
    l = ''.join('X '[l[c - 1:c + 2] in ('XXX', '   ', 'X  ', '', '  ')] for c in o)
    print l

raw_input("\nPress enter to exit")
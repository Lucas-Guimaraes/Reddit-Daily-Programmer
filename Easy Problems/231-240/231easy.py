#https://www.reddit.com/r/dailyprogrammer/comments/3jz8tt/20150907_challenge_213_easy_cellular_automata/
#This one is actually 231 on daily programmer

def automata(num, r_range=25):
    prev = [ int(x) for x in num]
    #Joins first line
    print ("".join(str(e) for e in prev).replace("0", " ").replace("1", "x"))
    for i in range(r_range):
        #Checks bit-wise for the whole range; appends 0's at the beginning and end, then print
        next = [prev[i - 1] ^ prev[i] ^ prev[i + 1] for i in range(1, len(prev) - 1)]
        next.append(0)
        next.insert(0, 0)
        print ("".join(str(e) for e in next).replace("0", " ").replace("1", "x"))
        prev = next

print("Welcome to Cellular Automata!")
print("Input a sequence of 1's and 0's, followed by the amount of times to repeat")
print("If nothing is inputted, the default is '25'")
print("\n~*~--------~*~\n")

cellular = True
while cellular:
    bin_string = raw_input()
    range_string = raw_input()
    if bin_string.lower() == 'q' or range_string.lower() == 'q':
        break
    if range_string == "" and bin_string.isdigit():
        automata(bin_string)
    if range_string.isdigit() and bin_string.isdigit():
        automata(bin_string, int(range_string))

raw_input("Press enter to exit.")

#automata("00000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000", 100)
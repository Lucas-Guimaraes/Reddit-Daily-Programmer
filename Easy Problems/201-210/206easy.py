#https://www.reddit.com/r/dailyprogrammer/comments/2z68di/20150316_challenge_206_easy_recurrence_relations/

def recurrence_relations(seq, n):
    term = [0]
    seq = seq.split()

    for i in range(n):
        cur = term[i]
        for x in seq:
            if x[0] == '+': cur += int(x[1:])
            if x[0] == '-': cur -= int(x[1:])
            if x[0] == '*': cur *= int(x[1:])
            if x[0] == '/': cur /= int(x[1:])
        term.append(cur)

    for i in term:
        print("Term {}: {}".format(term.index(i), i))

# Explanation
print("Welcome to Recurrences")
print("Put in a string of operations. Example Input: '+4 -3 +2")
print("And put in how many times to do that operation")
print("This program will output all of the results")
print("\n~*~----------------~*~\n")

# Checks input, quit case included
terming = True
while terming:
    op = raw_input("Please put in your operations: ").lower()
    n = raw_input("Please put in your digit: ").lower()
    if n == 'q' or op == 'q':
        break

    if n.isdigit():
        print("")
        recurrence_relations(op, int(n))
        print("")

raw_input("Press enter to exit.")

#recurrence_relations('*3 +2 *2', 7)
#recurrence_relations('*9 +2 /4 -12', 20)


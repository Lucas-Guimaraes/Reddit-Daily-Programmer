#https://www.reddit.com/r/dailyprogrammer/comments/8g0iil/20180430_challenge_359_easy_regular_paperfold/

#For each number in the cycle, does the sequence
def paper_seq(cycles):
    #Initial list
    lst = ['1']
    if cycles > 1:
        #How many items in the sequence to add
        cur = 1

        #Loops over each cycle
        for x in range(2, cycles+1):

            #Loops over each automatic number to add
            #If even idx, add '1', if odd, add '0'
            cur *= 2
            for i in range(cur):
                if i % 2 == 0:
                    lst.insert(i+i, '1')
                else:
                    lst.insert(i+i, '0')

    #Joins; creates result
    return "".join(lst)

#Intro
print("Welcome to Paperfolding Sequence")
print("Put in a string, and this program will return its sequence")
print("\n~*~--------~*~\n")

#Input
paperfold = True
while paperfold:
    n = raw_input()
    if n.islower() == 'q':
        break
    if n.isdigit():
        print(paper_seq(int(n)))

raw_input("Press enter to exit.")

#Test cases:
#print(paper_seq(8))
#print(paper_seq(12))
#print(paper_seq(20))
#https://www.reddit.com/r/dailyprogrammer/comments/826coe/20180305_challenge_353_easy_closest_string/

def hamming_seq(dna):
    final = []
    #Loops over each string
    for d in range(0, len(dna)):
        distance = 0
        #Grabs the hamstring distance for every string in the list
        for x in range(0, len(dna)):
            distance += hamming_distance(dna[d], dna[x])
        final.append((distance, dna[d]))

    #Sorts final list, returns the winning sequence
    final = sorted(final)
    return final[0][1]

def hamming_distance(a, b):
    distance = 0
    #Checks each letter of the two proposed strings
    for i in range(len(a)):
        if a[i] != b[i]:
            distance += 1
    return distance

#Intro
print("Welcome to Closest String!")
print("Insert a number, that will be the amount of lines.")
print("Follow this by every line.")
print("\n~*~----------------~*~\n")

#Continue Code
hamming = True
while hamming:
    #Grabs amount of lines
    lines = raw_input()
    if lines.upper() == 'Q':
        break
    #checks Lines
    if lines.isdigit():
        seq = []
        #For every line, raw input
        for i in range(int(lines)):
            line = raw_input().upper()
            seq.append(line)
        print(hamming_seq(seq))

raw_input("Press Enter to exit.")

#Test Case
#print(hamming_seq(["CTCCATCACAC", "AATATCTACAT", "ACATTCTCCAT", "CCTCCCCACTC"]))
#Other Algorithms worth looking into
#https://en.wikipedia.org/wiki/String_metric
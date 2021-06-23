#https://www.reddit.com/r/dailyprogrammer/comments/1qwkdz/111113_challenge_141_easy_checksums/

#This function will take the unicode of each symbol in the list
#And then it will get the sum and return a s tring
#That equals its 'Fletcher 16' number
def fletcher16(data):
    sum1, sum2 = 0, 0
    
    for elem in (ord(d) for d in data):
        sum1 = (sum1 + elem) % 255
        sum2 = (sum2 + sum1) % 255
    
    return str(hex((sum2 << 8) | sum1)).replace("0x", "").upper()
    
    
#where all the intro text goes
ndx = input("How many Fletcher-16 conversions? ")
fletcher_lst = []

#Loops based on how high the number for 'ndx' is put
for i in range(0, ndx):
    fmt_idx = str(i + 1)
    line = raw_input("Input Data #{}: ".format(fmt_idx))
    
    #Makes the fletcher item for each input, then appends it
    fletcher_item = str(fmt_idx) + " " + fletcher16(line)
    fletcher_lst.append(fletcher_item)

#Prints out every item in the fletcher list when done
for idx in fletcher_lst:
    print(idx)
    
raw_input()
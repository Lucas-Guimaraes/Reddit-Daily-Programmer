# https://www.reddit.com/r/dailyprogrammer/comments/4xy6i1/20160816_challenge_279_easy_uuencoding/

def encode(string, file_out):
    print 'begin 644 ' + file_out
    
    interval_string = [string[i:i+45] for i in range(0,len(string),45)]
    
    #this takes each element of interval string to go through it
    for each in interval_string:
        full_line = ''
        
        #This goes over every item in the range of 'each'
        #Converts it to a binary section, then uses the binary
        #to convert it back into a character
        for i in range(0, len(each), 3):
            section = each[i:i+3]
            bits = ''.join([bin(ord(x))[2:].zfill(8) for x in list(section)])
            groups = [chr(int(bits[j:j+6],2)+32) for j in range(0,len(bits),6)]
            full_line = full_line + ''.join(groups)
        
        #prints each full line
        print(chr(int(len(each))+32) + full_line)
        
        print '`\nend'
        

#Interacting with the program.
print("Hello! Welcome to string encoder.")
print("This program takes one input: a string, and gives one output: that string encoded")
print("\n~*~----------------~*~\n")
str_put = raw_input("Gimme a string!: ")
print("\n~*~----------------~*~\n")
file_put = str_put + '.txt'
encode(str_put, file_put)
print("\n~*~----------------~*~\n")
raw_input("Press enter to exit")
#encode('cat','cat.txt')
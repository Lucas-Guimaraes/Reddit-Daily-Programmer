# https://www.reddit.com/r/dailyprogrammer/comments/1m1jam/081313_challenge_137_easy_string_transposition/

#Transpose the list
def transpose(lst):

    #Finds the maximum number; accounts for the extra space
    len_max = max([len(i) for i in lst])
    space_added = [i + ' ' * (len_max - len(i)) for i in lst]
    transposed_str = ''
    
    #Loop for each line
    for i in range(len_max):
        new_line = ''
        
        #Indexes the list
        for x in space_added:
            new_line += x[i]
        new_line += '\n'
        transposed_str += new_line
    return transposed_str
    
#This is a list used, and then the program
used = ['Kernel', 'Microcontroller', 'Register', 'Memory', 'Operator']
print(transpose(used))
raw_input()
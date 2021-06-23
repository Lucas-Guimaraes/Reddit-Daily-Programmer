# https://www.reddit.com/r/dailyprogrammer/comments/za9op/9032012_challenge_95_easy_reversing_text_in_file/
#'95easy-test.txt' is a supplementary file.

#Function 'reverse_file'
def reverse_file(filename):
    file = open(filename, 'r')
    start_list = []
    
    #Appends all lines to a list
    for line in file:
        line_fix = line.replace('\n', '')
        start_list.append(line_fix)
    
    line_count = len(start_list)
    
    #Reverses list to throw for each line
    while line_count > 0:
        #Prepares every word
        start_line = start_list[-1]
        start_line = start_line.split()
        start_word_count = len(start_line)
        finish_line = []

        #Makes sure every word is backwards
        while start_word_count > 0:
            finish_line.append(start_line[-1])
            start_line.pop()
            start_word_count -= 1
        
        #prints the reversed line, lowers the count
        finish_line = ' '.join(finish_line)
        print(finish_line)
        start_list.pop()
        line_count -= 1
        
    


reverse_file('95easy-test.txt')
raw_input() #This is just to run
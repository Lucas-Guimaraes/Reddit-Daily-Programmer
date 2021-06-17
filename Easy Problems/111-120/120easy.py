# https://www.reddit.com/r/dailyprogrammer/comments/17uw4s/020413_challenge_120_easy_log_throughput_counter/
#Supplementary file is '120easyreadfile.txt'
# I didn't do the actual assignment because it was vague but here's something close:

import datetime


def magic_man():
    #prints the current time
    first = datetime.datetime.now()
    print(first)

    file = open('120easyreadfile.txt', 'r')
    #prints every ten lines from the file
    for i in file.readlines():
        print(i * 10)
    
    #checks the total time the program took
    second = datetime.datetime.now()
    
    total_time = second-first
    print(first)
    print(second)
    print("The total time this program took: {}".format(total_time))

magic_man()
raw_input()
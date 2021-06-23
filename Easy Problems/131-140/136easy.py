# https://www.reddit.com/r/dailyprogrammer/comments/1kphtf/081313_challenge_136_easy_student_management/
#Allows multiple lines to be read
import sys

#This program handles the initial function
#Stu = 'students'
def student_management(stu_input):

    #This handles all of the new lines
    space = stu_input.find(' ') + 1
    line = stu_input.find('\n') + 1
    n, m = int(stu_input[0:space]), int(stu_input[space:line])
    average = 0
    students = stu_input[line::].split("\n")
    
    #checks the amount of students and loops from that
    for i in range(n):
        data = students[i].split(" ", 1)
        students[i] = data[0] + (" %.2f" % (sum(float(n) for n in data[1].split(" ")) / m))
        average += sum(float(n) for n in data[1].split(" ")) / (m * n)
    print "%.2f" % average
    
    #Prints each student at once
    for i in range(int(n)):
        print students[i]


s = sys.stdin.read()
#use ctrl+D after the input
student_management(s)
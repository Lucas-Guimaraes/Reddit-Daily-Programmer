# https://www.reddit.com/r/dailyprogrammer/comments/1iambu/071513_challenge_133_easy_foottraffic_analysis/
#'133easyvisitors.txt' is a supplementary file
#Sample input from the original URL, or your own input, will be accepted in the file



#Function that takes the files
def the_doors(file):

   #Splits all the lines, makes the room dictionary
   v_data = [line.split() for line in open(file)][1:]
   room_time = {}
   
   #Changes the time based on the direction
   for v, room_number, direction, time in v_data:    
        if room_number not in room_time:
            room_time[room_number] = []
        room_time[room_number].append(-int(time) if direction == 'I' else int(time))
   
   #Sorts by room time
   sorted_room_time = sorted(room_time, key=lambda x: int(x))
   for key in sorted_room_time:
        
        #sum of room time divided by visitors plus 1
        #avg_visit needs to be divided by 2, since the amount of people both enter and exit.
        visitors = len(room_time[key]) / 2
        avg_visit = sum(room_time[key]) / visitors + 1
        visit = ''
        
        #this just changes 'visitor' and 'visitors' based on the amount
        if visitors == 1:
            visit = 'visitor'
        else:
            visit = 'visitors'
        #what #, how long their average time was, 
        print("Room {0}, {1} minute average visit, {2} {3} total".format(key, avg_visit, visitors, visit))

file_name = '133easyvisitors.txt'
the_doors(file_name)
#room /dict title, sum list / 2, len(sum_lst) / 2
#Room _, _ minute average visit, _ visitor(s) total
raw_input("Press enter to exit.")
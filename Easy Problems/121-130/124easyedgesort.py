# https://www.reddit.com/r/dailyprogrammer/comments/1dsyrk/050613_challenge_124_easy_edge_sorting/
#g is put in the supplementary file to help organization
#'124easygedgesort.txt' is a supplementary file to this one.

def edge_sort(file):

   lines = [line.split() for line in open(file)][1:]
   
   regular_points = []
   regular_n_start = []
   regular_n_end = []
   
   #splits all into their own lines
   for line in lines:
        regular_points.append(line[0])
        regular_n_start.append(str(line[1]))
        regular_n_end.append(str(line[2]))
   
   #Sorts the start and end points
   sorted_start = sorted(regular_n_start)
   sorted_end = sorted(regular_n_end)
   final_sort = []
   
   #checks for duplicates
   seen = set()
   uniq = []
   dupes = []
   for x in sorted_start:
        if x not in seen:
            uniq.append(x)
            seen.add(x)
        else:
            dupes.append(x)
   
   dupes_dic = {}
   cur_idx = -1
   
   #gets the sorting started
   for i in sorted_start:
        cur_idx += 1
        item_idx = regular_n_start.index(i)
        
        #checks if it's going over a duped number
        if i not in dupes:
            final_sort.append(regular_points[item_idx])
        else:
            checker = str(i)
            
            if checker not in dupes_dic:
                dupes_dic[checker] = 0  
            else:
                dupes_dic[checker] += 1
            
            item_idx = [x for x, n in enumerate(regular_n_start) if n == i][dupes_dic[checker]]
            if dupes_dic[checker] > 0:
                prev_idx = [x for x, n in enumerate(regular_n_start) if n == i][dupes_dic[checker] - 1]
                
            final_sort.append(regular_points[item_idx])
            
        #if there's a duplicate, this reorders the lists properly to compensate
        if sorted_start[cur_idx] == sorted_start[cur_idx-1] and 0 != cur_idx:
            if regular_n_end[prev_idx] > regular_n_end[item_idx]:
                final_sort[cur_idx-1], final_sort[cur_idx] = final_sort[cur_idx], final_sort[cur_idx-1]
               
   return final_sort
   
file_name = '124easygedgesort.txt'
print(edge_sort(file_name))
raw_input()
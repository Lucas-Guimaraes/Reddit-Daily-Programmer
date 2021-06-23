# https://www.reddit.com/r/dailyprogrammer/comments/zkdv1/9082012_challenge_97_easy_concatenate_directory/
#'97-1test.txt' all the way to 6 (so 97-2, 97-3, 97-4, 97-5, 97-6) are ALL supplementary files
#'99easytest' can also be used as a supplementary file
#Really, any text file in your directory

import os

#For this problem, I opted to make a recursive solution, and then non-recurse it.

#Recursive solution
def recursive_solution(recurse_path):
    for dirpath, dirnames, filenames in os.walk(recurse_path):
        for file in filenames:
            if file.endswith('.txt'):
                filepath = os.path.join(dirpath, file)
                byte_size = '(' + str(os.path.getsize(filepath)) + ' bytes)'
                print('=== ' + str(file) + ' ' + byte_size)
                print(open(filepath).read())

#Non recursive solution. This solution is slightly faster.
def non_recursive_solution(non_r_path, level=1):
    non_r_path = non_r_path.rstrip(os.path.sep)

    assert os.path.isdir(non_r_path)
    num_sep = non_r_path.count(os.path.sep)
    for root, dirs, files in os.walk(non_r_path):

        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

        for file in files:

            if file.endswith('.txt'):
                filepath = os.path.join(root, file)
                byte_size = '(' + str(os.path.getsize(filepath)) + ' bytes)'
                print('=== ' + str(file) + ' ' + byte_size)
                print(open(filepath).read())


#non_recursive_solution('A:\Users\Lucas\Desktop\Programming Folder\Daily Programmer\Python Easy\91-100')
recursive_solution('A:\Users\Lucas\Desktop\Programming Folder\Daily Programmer\Python Easy\91-100')

raw_input()
#https://www.reddit.com/r/dailyprogrammer/comments/3ggli3/20150810_challenge_227_easy_square_spirals/

def find_matrix(n, search):
    #All info for changing directions
    cur_dir = 'right'
    space_limit = 1
    cur_space = 0
    
    change_dir = {'right': ['up', 0, 1],
                  'up': ['left', -1, 0],
                  'left': ['down', 0, -1],
                  'down': ['right', 1, 0]}

    #Outer is y axis, inner is x axis
    new_matrix = [['*' for i in range(n)] for i in range(n)]
    outer, inner = int(n / 2), int(n / 2)

    for i in range(1, (n*n)+1):

        #Break case
        if i == search:
            return inner+1, outer+1

        if type(search) == tuple:
            if inner+1 == search[0] and outer+1 == search[1]:
                return i

        new_matrix[outer][inner] = i

        #Changes direction
        if cur_space == space_limit:
            cur_dir = change_dir[cur_dir][0]
            cur_space = 0
            if cur_dir == 'left' or cur_dir == 'right':
                space_limit += 1

        outer += change_dir[cur_dir][1]
        inner += change_dir[cur_dir][2]
        cur_space += 1

#Test cases
print(find_matrix(3, 8))
print(find_matrix(7, (1, 1)))
print(find_matrix(11, 50))
print(find_matrix(9, (6, 8)))
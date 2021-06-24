# https://www.reddit.com/r/dailyprogrammer/comments/ynw53/8222012_challenge_90_easy_walkaround_rasterizer/

def rasterizer(height, width, directions):
    lst = []
    line = ' ' * width
    
    #adds lines for every height.
    for i in range(height):
        lst.append(line)
    
    up = 0
    right = 0

    
    directions = directions.lower()
    for d in directions:
        #when there's a 'p', prints a '*' from where the list is
        #then updates the list
        if d == 'n':
            up -= 1
        elif d == 's':
            up += 1
        elif d == 'e':
            right += 1
        elif d == 'w':
            right -= 1
        elif d == 'p':
            newline = lst[up][:right]+'*'+lst[up][right+1:]
            lst = lst[:up]+[newline]+lst[up+1:]
        newline = line


    return '\n'.join(lst)

#Test cases
print(rasterizer(5, 5, 'PESPESPESPESPNNNNPWSPWSPWSPWSP'))
print(rasterizer(20, 10, 'eeeeeeepswpepepsepwpwpwpwpswpepepepepepepsepwpwpwpwpwpwpwpwpepspepepepepepepswpwpwpwpwpsepepepswp'))
raw_input()
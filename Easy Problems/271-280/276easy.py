#https://www.reddit.com/r/dailyprogrammer/comments/4tetif/20160718_challenge_276_easy_recktangles/

def recktangle(n, w, h):
    # Creates switch
    cur_line = "Current"
    cur_h_line = 1

    #Initial logic
    opposite_n = n[::-1]
    line_one, line_two = n, opposite_n

    if w > 1:
        for i in range(w-1):
            if cur_line == "Current":
                line_one += opposite_n[1:]
                line_two += n[1:]
                cur_line = "Reversed"
            elif cur_line == "Reversed":
                line_one += n[1:]
                line_two += opposite_n[1:]
                cur_line = "Current"

    line_one = " ".join([x for x in line_one])
    line_two = " ".join([x for x in line_two])

    cur_line = "Current"
    #Creates space
    space = ((((len(n) - 2)) * ' ') * 2) + ' '


    for i in range((h*len(n))-1):
        line_space = ''
        if i == 0 or i == (h*len(n))-1 or len(n)-2 < cur_h_line:
            if cur_line == "Current":
                cur_line = "Reversed"
                cur_h_line = 1
                print(line_one)
            elif cur_line == "Reversed":
                cur_line = "Current"
                cur_h_line = 1
                print(line_two)

        elif cur_line == "Current":
            line_space += n[cur_h_line] + space + opposite_n[cur_h_line]
            if w > 1:
                for x in range(w-1):
                    line_space += space
                    if x % 2 == 0:
                        line_space += n[cur_h_line]
                    else:
                        line_space += opposite_n[cur_h_line]

            cur_h_line += 1
            print(line_space)

        elif cur_line == "Reversed":
            line_space += opposite_n[cur_h_line] + space + n[cur_h_line]
            if w > 1:
                for x in range(w-1):
                    if x != w-1:
                        line_space += space
                    if x % 2 == 0:
                        line_space += opposite_n[cur_h_line]
                    else:
                        line_space += n[cur_h_line]


            cur_h_line += 1
            print(line_space)

#test case
recktangle('REKT', 4, 4)
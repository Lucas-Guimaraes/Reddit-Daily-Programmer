# https://www.reddit.com/r/dailyprogrammer/comments/1undyd/010714_challenge_147_easy_sport_points/


def sports_points(points):
    #We can cull all invalid scores easily
    invalid_scores = [1, 2, 4, 5]
    if points in invalid_scores:
        return 'Invalid Score'
    
    #8, 7, 6, and 3 are our best point checkers
    best_combo = [0, 0, 0, 0]
    point_checker = [8, 7, 6, 3]
    remainder = points
    regular_scores = []

    for checker in point_checker:
        maximum_num = points / checker
        regular_scores.append(maximum_num)

        point_lst = remainder / checker
        index = point_checker.index(checker)
        best_combo.insert(index, point_lst)
        best_combo.pop(index+1)
        remainder = remainder % checker
        if remainder % checker == 0:
            break

    #Table to print
    football_table = "With {} points, the table shows the following:\n\n".format(points) + "the max amount of two extra point touchdowns would be {}\n".format(regular_scores[0]) + "The max amount of one extra point touchdowns would be {}\n".format(regular_scores[1]) + "The max amount of touch downs would be {}\n".format(regular_scores[2]) + "The max amount of field goals would be {}\n\n".format(regular_scores[3]) + "The best possible combo would be:\n\n" + "{} two extra point touchdowns\n".format(best_combo[0]) + "{} one extra point touchdowns\n".format(best_combo[1]) + "{} regular touchdowns\n".format(best_combo[2]) + "{} field goals".format(best_combo[3])

    return football_table

print("Welcome to football table!")
print("This program will take a football score and tell the optimal amount of scores")
print("\n~*~----------------~*~\n")
football = True
while football:
    num = raw_input("What score would you like to see? ('q' to exit): ")
    if num.isdigit():
        print(sports_points(int(num)))
    if num == 'Q' or num == 'q':
        football = False
        break

raw_input("Press enter to exit")


#Test cases
#print(sports_points(35))

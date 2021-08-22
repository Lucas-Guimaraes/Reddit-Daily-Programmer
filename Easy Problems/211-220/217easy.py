# https://www.reddit.com/r/dailyprogrammer/comments/3840rp/20150601_challenge_217_easy_lumberjack_pile/


def lumberjack(row_size, log_amt, pile_logs):
    new_pile = pile_logs.split()
    new_pile = [int(log) for log in new_pile]
    baum_blitz = True
    while log_amt > 0:
        min_checker = min(new_pile)
        for x in range(len(new_pile)):

            if new_pile[x] == min_checker:
                new_pile[x] += 1
                log_amt -= 1
                if log_amt == 0:
                    break


    final_pile = ''
    for i in range(row_size):
        for x in range(row_size):
            final_pile += str(new_pile.pop(0))
            if x != row_size:
                final_pile += ' '
        if i != row_size:
            final_pile += '\n'
    return final_pile

def create_input(txt):
    check = True
    while check:
        num_check = raw_input("Please put in your {}: ".format(txt))
        num_check = num_check.replace(' ', '')
        if num_check.isdigit():
            num_check = int(num_check)
            check = False
            return num_check
        else:
            print(invalid_txt(txt))
            continue
def invalid_txt(txt):
    return "{} is invalid. Please input a valid input".format(txt)

print("Hello! Welcome to Lumberjack")
print("You will give three inputs")
print("One is the amount of lines for your third input - the size of your grid")
print("The second input will be the amount of logs you have")
print("The third depends on number 1 - for example, if you answer 3, you will need to give 3 inputs of 3 numbers")
print("3 3 3")
print("4 3 2")
print("2 3 2")
print("From there, a log will be added to the lowest amounts until all logs are cleared.")
print("So with three logs, each of the 2's would turn into a 3")
print("With four logs, each 2 would turn into a 3, and the first 3 would turn into a 4")
print("Example:")
print("4 3 3")
print("4 3 3")
print("3 3 3")
print("\n~*~----------------~*~\n")

grid_size = create_input("grid size")
log_size = create_input("amount of logs")
log_pile = ''
i_grid = True
while i_grid:
    for i in range(grid_size):
        i_row = True

        while i_row:
            row = raw_input("Please input {} numbers: ".format(str(grid_size)))
            temp_row = row.split()
            digit_check = row.replace(' ', '')
            if len(temp_row) == grid_size:
                if digit_check.isdigit():
                    log_pile += row + ' '
                    i_row = False
                else:
                    print(invalid_txt(row))
                    continue
            else:
                print(invalid_txt(row))
                continue
    i_grid = False
    
print("")
print(lumberjack(grid_size, log_size, log_pile))
raw_input("Press Enter to exit.")

#print(lumberjack(3, 7, '1 1 1 2 1 3 1 4 1'))